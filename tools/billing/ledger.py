#!/usr/bin/env python3
"""
Billing-grade ledger row generator for Claude Code commits.

Reads the JSONL transcripts under ~/.claude/projects/<encoded-cwd>/ and emits
exactly one LEDGER.md row covering the window [last_ledger_date, HEAD_commit_date].

Design choices (these matter for invoices):
  - Aborts on unknown model/tier rather than silently skipping. A missing row
    is fine; a wrong row is not.
  - Distinguishes long-context (1M) variants via the [1m] suffix in
    message.model. They are priced separately in pricing.json.
  - Prices are effective-dated. A model in pricing.json may be a flat price
    object (in effect for all time) or a list of {"effective": ISO, ...}
    entries; each turn is priced at the rate whose `effective` date is the
    latest one <= the turn's own timestamp. Changing a price means appending a
    new dated entry, never editing an old one — so re-running a past window
    reproduces the originally-billed cost and a new rate never reaches backward.
  - Applies service_tier multipliers (batch=0.5x is the common case).
  - Counts server-tool requests (web_search) at per-request rates.
  - Window is half-open: (start, end]. Last ledger row's `date` is the start,
    so usage that funded that row is never double-counted.

Usage:
  ./ledger.py                    # repo at cwd, ledger covers since last row
  ./ledger.py --repo /path/to/r  # explicit repo path
  ./ledger.py --session-cwd PATH # transcripts come from a different cwd than the repo
                                 #   (e.g. session launched from ~/workspace but
                                 #    commit landed in ~/workspace/projects/foo)
  ./ledger.py --since ISO        # override start of window
  ./ledger.py --until ISO        # override end of window (default: HEAD commit time)
  ./ledger.py --commit SHA       # use this SHA's committer time as end and as the commit cell
  ./ledger.py --dry-run          # print row and breakdown, do not modify LEDGER.md
  ./ledger.py --append           # append the row to <repo>/LEDGER.md (creates file if missing)
  ./ledger.py --summary "msg"    # one-line summary for the row

Exit codes:
  0 = success, row printed/appended
  2 = no usage found in window (likely a non-AI commit) — no row emitted
  3 = unknown model or service tier — refuses to bill
  4 = unreadable transcript or missing dependency
"""
from __future__ import annotations
import argparse, glob, json, os, re, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path


def to_utc(ts: str) -> datetime:
    """Parse ISO 8601 (with Z or +/-HH:MM offset) to aware UTC datetime."""
    if not ts:
        raise ValueError("empty timestamp")
    s = ts.replace("Z", "+00:00")
    return datetime.fromisoformat(s).astimezone(timezone.utc)


def utc_iso(ts: str) -> str:
    return to_utc(ts).strftime("%Y-%m-%dT%H:%M:%SZ")

PRICING_PATH = Path.home() / ".claude" / "billing" / "pricing.json"


def die(code: int, msg: str) -> None:
    sys.stderr.write(f"ledger.py: {msg}\n")
    sys.exit(code)


def load_pricing() -> dict:
    if not PRICING_PATH.exists():
        die(4, f"pricing file not found: {PRICING_PATH}")
    with open(PRICING_PATH) as f:
        return json.load(f)


def encoded_cwd(repo: Path) -> str:
    # Claude Code encodes the absolute path by replacing '/' with '-'.
    return str(repo.resolve()).replace("/", "-")


def git(repo: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    if r.returncode != 0:
        die(4, f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r.stdout.strip()


def last_ledger_date(repo: Path) -> str | None:
    ledger = repo / "LEDGER.md"
    if not ledger.exists():
        return None
    # Rows look like: | abc1234 | 2026-06-12T... | ...
    # ISO timestamp lives in the second data column.
    last = None
    pat = re.compile(r"^\|\s*~?[0-9a-f]{7,}\s*\|\s*(\S+?)\s*\|")
    for line in ledger.read_text().splitlines():
        m = pat.match(line)
        if m:
            last = m.group(1)
    return last


def resolve_price(model_cfg, ts_dt: datetime, model: str, ts: str):
    """Pick the price entry in effect for a turn at ts_dt.

    A model in pricing.json is either:
      - a flat object {"in":..., ...}  → in effect for all time (legacy form), or
      - a list of dated entries [{"effective": ISO, "in":..., ...}, ...] → the
        entry with the latest `effective` <= the turn's timestamp applies.

    Effective-dating is what lets a price change without altering historical
    billing: a corrected/updated rate is appended as a new dated entry, so old
    turns still resolve to the rate that was in effect when they ran, and any
    re-computation of a past window reproduces the originally-billed cost.

    Returns (effective_iso, price_dict). `effective_iso` is "" for the flat form.
    """
    if isinstance(model_cfg, dict):
        return ("", model_cfg)
    if not isinstance(model_cfg, list) or not model_cfg:
        die(3, f"pricing for '{model}' is neither a price object nor a non-empty "
               f"list of dated entries. Update {PRICING_PATH}.")
    best = best_dt = None
    for entry in model_cfg:
        eff = entry.get("effective")
        if eff is None:
            die(3, f"dated pricing entry for '{model}' is missing an 'effective' "
                   f"date. Update {PRICING_PATH}.")
        eff_dt = to_utc(eff)
        if eff_dt <= ts_dt and (best_dt is None or eff_dt > best_dt):
            best, best_dt = entry, eff_dt
    if best is None:
        die(3, f"no pricing for model '{model}' effective at {ts}; the earliest "
               f"dated entry starts later. Add an entry covering this date to "
               f"{PRICING_PATH} and retry.")
    return (utc_iso(best["effective"]), best)


def collect_usage(projdir: Path, start: str, end: str, models_cfg: dict) -> dict:
    """Walk all *.jsonl files and aggregate assistant-turn usage in (start, end].

    Turns are bucketed by (model, service_tier, price_effective_date) so that a
    window straddling a price change is billed with the correct rate on each side.
    The resolved price for each bucket travels back in `resolved` so the pricing
    pass never has to re-derive which rate applied.
    """
    buckets: dict[tuple[str, str, str], dict] = {}
    resolved: dict[tuple[str, str, str], dict] = {}
    server_tools = {"web_search": 0, "web_fetch": 0}
    saw_any = False

    start_dt = to_utc(start)
    end_dt = to_utc(end)

    if not projdir.exists():
        die(4, f"transcript dir not found: {projdir}")

    for path in sorted(projdir.glob("*.jsonl")):
        try:
            with open(path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        d = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if d.get("type") != "assistant":
                        continue
                    ts = d.get("timestamp", "")
                    try:
                        ts_dt = to_utc(ts)
                    except (ValueError, TypeError):
                        continue
                    if not (start_dt < ts_dt <= end_dt):
                        continue
                    msg = d.get("message") or {}
                    u = msg.get("usage") or {}
                    if not u:
                        continue
                    model = msg.get("model")
                    if not model:
                        die(3, f"assistant turn at {ts} has no model field")
                    # Synthetic turns are Claude Code internals (compaction summaries,
                    # placeholder messages). They don't hit the API and aren't billed.
                    if model == "<synthetic>":
                        continue
                    model_cfg = models_cfg.get(model)
                    if model_cfg is None:
                        die(3, f"no pricing for model '{model}' (turn at {ts}). "
                               f"Update {PRICING_PATH} and retry.")
                    tier = u.get("service_tier", "standard")
                    eff_iso, price = resolve_price(model_cfg, ts_dt, model, ts)
                    saw_any = True
                    key = (model, tier, eff_iso)
                    resolved[key] = price
                    b = buckets.setdefault(key, {
                        "in": 0, "out": 0, "cr": 0, "cw5": 0, "cw1h": 0,
                    })
                    b["in"]  += u.get("input_tokens", 0) or 0
                    b["out"] += u.get("output_tokens", 0) or 0
                    b["cr"]  += u.get("cache_read_input_tokens", 0) or 0
                    cc = u.get("cache_creation") or {}
                    b["cw5"]  += cc.get("ephemeral_5m_input_tokens", 0) or 0
                    b["cw1h"] += cc.get("ephemeral_1h_input_tokens", 0) or 0
                    st = u.get("server_tool_use") or {}
                    server_tools["web_search"] += st.get("web_search_requests", 0) or 0
                    server_tools["web_fetch"]  += st.get("web_fetch_requests", 0) or 0
        except OSError as e:
            die(4, f"could not read {path}: {e}")

    return {"buckets": buckets, "resolved": resolved,
            "server_tools": server_tools, "any": saw_any}


def price_buckets(buckets: dict, resolved: dict, server_tools: dict, pricing: dict) -> dict:
    multipliers = pricing["service_tier_multipliers"]
    st_prices = pricing["server_tools"]

    total = {"in": 0, "out": 0, "cr": 0, "cw": 0, "cost": 0.0, "models": set(), "tiers": set()}
    for (model, tier, eff), b in buckets.items():
        if tier not in multipliers:
            die(3, f"no multiplier for service tier '{tier}'. Update {PRICING_PATH} and retry.")
        p = resolved[(model, tier, eff)]
        mult = multipliers[tier]
        cost = (
            b["in"]   * p["in"]
          + b["out"]  * p["out"]
          + b["cr"]   * p["cr"]
          + b["cw5"]  * p["cw5"]
          + b["cw1h"] * p["cw1h"]
        ) / 1_000_000.0 * mult
        total["in"]   += b["in"]
        total["out"]  += b["out"]
        total["cr"]   += b["cr"]
        total["cw"]   += b["cw5"] + b["cw1h"]
        total["cost"] += cost
        total["models"].add(model)
        total["tiers"].add(tier)

    # Server tools billed at flat per-request rates regardless of tier.
    total["cost"] += server_tools["web_search"] * st_prices["web_search_per_request"]
    total["cost"] += server_tools["web_fetch"]  * st_prices["web_fetch_per_request"]
    total["web_search"] = server_tools["web_search"]
    total["web_fetch"]  = server_tools["web_fetch"]
    return total


def format_row(commit: str, date: str, total: dict, summary: str) -> str:
    models = ",".join(sorted(total["models"]))
    if total["tiers"] - {"standard"}:
        models += " (" + ",".join(sorted(total["tiers"])) + ")"
    return (
        f"| {commit} "
        f"| {date} "
        f"| {models} "
        f"| {total['in']} "
        f"| {total['out']} "
        f"| {total['cr']} "
        f"| {total['cw']} "
        f"| {total['cost']:.4f} "
        f"| {summary} |"
    )


HEADER = (
    "| commit | date | model(s) | input | output | cache_read | cache_write | cost_usd | summary |\n"
    "|--------|------|----------|------:|-------:|-----------:|------------:|---------:|---------|"
)


# Rough datacenter energy-per-token coefficients (joules), by token role.
# These are order-of-magnitude figures for frontier-model serving, not
# measurements — public estimates themselves span ~10x. Output (decode)
# tokens each need a full forward pass and cost the most; fresh prompt
# tokens (input + cache_write) are cheaper parallel prefill; cache reads
# reuse already-computed KV state and are cheapest per token. PUE folds
# in cooling/power-delivery overhead. Central lands near published
# per-query figures (~0.3 Wh for a ~500-token GPT-4o-class response).
ENERGY_J = {
    #                low   central  high
    "out":         (2.0,   3.0,     6.0),
    "fresh":       (0.2,   0.5,     1.0),   # input + cache_write
    "cr":          (0.02,  0.05,    0.15),  # cache_read
}
ENERGY_PUE = (1.1, 1.2, 1.3)


def energy_estimate(inp: int, out: int, cr: int, cw: int) -> dict:
    """Return low/central/high kWh for the given token buckets."""
    fresh = inp + cw
    out_kwh, cr_kwh = {}, {}
    kwh = {}
    for i, band in enumerate(("low", "central", "high")):
        joules = out * ENERGY_J["out"][i] + fresh * ENERGY_J["fresh"][i] + cr * ENERGY_J["cr"][i]
        kwh[band] = joules * ENERGY_PUE[i] / 3.6e6
    # "Real work" = tokens that were actually generated or freshly
    # processed, excluding cache reuse — the unambiguous floor.
    real_j = out * ENERGY_J["out"][1] + fresh * ENERGY_J["fresh"][1]
    kwh["real_central"] = real_j * ENERGY_PUE[1] / 3.6e6
    return kwh


def energy_lines(inp: int, out: int, cr: int, cw: int, label: str = "energy") -> list[str]:
    e = energy_estimate(inp, out, cr, cw)
    total = inp + out + cr + cw
    return [
        f"{label}: ~{e['central']:.2f} kWh central "
        f"(range {e['low']:.2f}-{e['high']:.2f}); "
        f"real-work floor ~{e['real_central']:.2f} kWh\n",
        f"  over {total:,} tokens "
        f"({cr / total * 100:.0f}% cache reads — cheap reuse)\n"
        if total else "",
    ]


def parse_ledger_tokens(ledger: Path) -> dict:
    """Sum the four token columns across every data row of a LEDGER.md."""
    tot = {"in": 0, "out": 0, "cr": 0, "cw": 0, "cost": 0.0, "rows": 0}
    if not ledger.exists():
        return tot
    for line in ledger.read_text().splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 8 or cells[0] in ("commit", "") or set(cells[0]) <= set("-:"):
            continue
        try:
            tot["in"] += int(cells[3]); tot["out"] += int(cells[4])
            tot["cr"] += int(cells[5]); tot["cw"] += int(cells[6])
            tot["cost"] += float(cells[7]); tot["rows"] += 1
        except (ValueError, IndexError):
            continue
    return tot


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".", help="Repo path (default: cwd)")
    ap.add_argument(
        "--session-cwd",
        help=(
            "Override the cwd used to locate Claude transcripts. By default the "
            "transcript dir is derived from --repo, which assumes the Claude session "
            "was launched from inside the repo. If the session ran from a different "
            "cwd (for example a workspace dir that contains the repo as a "
            "subdirectory), pass that cwd here so transcripts are found correctly."
        ),
    )
    ap.add_argument("--commit", default="HEAD", help="Commit SHA or ref (default: HEAD)")
    ap.add_argument("--since", help="Override window start (ISO 8601)")
    ap.add_argument("--until", help="Override window end (ISO 8601)")
    ap.add_argument("--summary", default="", help="One-line summary for the row")
    ap.add_argument("--append", action="store_true", help="Append the row to <repo>/LEDGER.md")
    ap.add_argument("--dry-run", action="store_true", help="Print row + breakdown, no file changes")
    ap.add_argument("--energy", action="store_true",
                    help="Include a rough datacenter energy (kWh) estimate for this row")
    ap.add_argument("--energy-total", action="store_true",
                    help="Estimate energy over the whole existing <repo>/LEDGER.md and exit")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    if not (repo / ".git").exists():
        die(4, f"not a git repo: {repo}")

    # Whole-ledger energy: no commit/window needed, just read the file.
    if args.energy_total:
        tot = parse_ledger_tokens(repo / "LEDGER.md")
        if not tot["rows"]:
            die(2, f"no ledger rows found in {repo / 'LEDGER.md'}")
        sys.stderr.write(
            f"ledger: {tot['rows']} rows, ${tot['cost']:.2f} billed, "
            f"tokens in={tot['in']:,} out={tot['out']:,} "
            f"cache_read={tot['cr']:,} cache_write={tot['cw']:,}\n")
        for line in energy_lines(tot["in"], tot["out"], tot["cr"], tot["cw"],
                                 label="energy (whole ledger)"):
            sys.stderr.write(line)
        return

    pricing = load_pricing()
    session_cwd = Path(args.session_cwd).resolve() if args.session_cwd else repo
    projdir = Path.home() / ".claude" / "projects" / encoded_cwd(session_cwd)

    short_sha = git(repo, "rev-parse", "--short", args.commit)
    end_raw = args.until or git(repo, "show", "-s", "--format=%cI", args.commit)
    start_raw = args.since or last_ledger_date(repo) or "1970-01-01T00:00:00Z"
    # Normalize both to UTC ISO so comparisons and the ledger row are timezone-correct.
    start = utc_iso(start_raw)
    end = utc_iso(end_raw)

    raw = collect_usage(projdir, start, end, pricing["models"])
    if not raw["any"]:
        sys.stderr.write(
            f"no assistant turns in window ({start}, {end}] under {projdir}\n"
            "If this was an AI-assisted commit, the session may have been launched\n"
            "from a different cwd. Check ~/.claude/projects/ for the right path,\n"
            "then rerun with --session-cwd /path/to/session/cwd (or --repo / "
            "--since / --until).\n"
        )
        sys.exit(2)

    total = price_buckets(raw["buckets"], raw["resolved"], raw["server_tools"], pricing)
    summary = args.summary or git(repo, "show", "-s", "--format=%s", args.commit)
    summary = summary.replace("|", "/").strip()[:80]

    row = format_row(short_sha, end, total, summary)

    if args.dry_run or not args.append:
        # Breakdown to stderr so stdout stays pure (just the row).
        sys.stderr.write(f"window: ({start}, {end}]\n")
        sys.stderr.write(f"models: {sorted(total['models'])}  tiers: {sorted(total['tiers'])}\n")
        sys.stderr.write(
            f"tokens: in={total['in']} out={total['out']} "
            f"cache_read={total['cr']} cache_write={total['cw']}\n"
        )
        if total["web_search"] or total["web_fetch"]:
            sys.stderr.write(
                f"server_tools: web_search={total['web_search']} "
                f"web_fetch={total['web_fetch']}\n"
            )
        sys.stderr.write(f"cost_usd: {total['cost']:.4f}\n")
        if args.energy:
            for line in energy_lines(total["in"], total["out"], total["cr"], total["cw"]):
                sys.stderr.write(line)
        print(row)
        return

    ledger = repo / "LEDGER.md"
    if not ledger.exists():
        ledger.write_text(HEADER + "\n" + row + "\n")
    else:
        existing = ledger.read_text().rstrip()
        ledger.write_text(existing + "\n" + row + "\n")
    sys.stderr.write(f"appended to {ledger}\n")


if __name__ == "__main__":
    main()
