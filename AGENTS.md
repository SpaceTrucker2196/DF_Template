# {{REPO_NAME}} — agent instructions

Repo-local rules for any coding agent (Claude Code, Copilot, Codex).
Build/infra runbook lives in `FACTORY.md`; charter in `MISSION.md`;
the pattern and autonomy contract in `docs/dark-factory.md`.

> FIRST RUN: fill the Architecture and Conventions sections from the
> observed codebase. Match its real idioms — don't prescribe new ones.

## What {{REPO_NAME}} is

[Two or three sentences. Link to MISSION.md for the full charter.]

## Architecture

[The load-bearing structure: modules/targets, dependency rules,
where state lives, the seams. If a dependency rule matters, state it
as a rule ("X never imports Y"), not a description.]

## Discipline

- **Tests must pass.** The oracle is the command in FACTORY.md's
  TL;DR; it returns 0 before any push. Never commit a red test.
- **Builds are warning-clean.**
- **Dependencies are pinned and audited.** Anything new needs a
  MISSION.md audit recorded in `PROGRESS.md`.
- [repo-specific discipline — concurrency model, generated files,
  forbidden APIs…]

## Conventions

- **Commit messages.** Imperative subject, blank line, body
  explaining the *why*. `Co-Authored-By` trailer when an agent
  landed the change.
- **Branches.** Work on `main`. No long-running feature branches.
- **`git add` specific files.** Never `git add -A` or `git add .`.
- Don't run destructive git ops without explicit user authorisation.
- [repo-specific conventions]

## Token / Cost Ledger

The owner bills from `LEDGER.md` (exact, never estimated). After
every substantive commit: run `~/.claude/billing/ledger.py --append
--summary "<desc>"`, then commit `LEDGER.md` as its own
`chore(ledger): <sha>` commit. Never hand-author, estimate, or
rewrite rows (append-only); if the script can't produce a row, stop
and surface it. Start billable sessions **inside this repo**, not
the workspace root (ledger.py can't attribute sessions launched from
outside the repo).

Reporting (optional, read-only): `ledger.py --energy-total`
estimates the rough datacenter energy (kWh) behind the whole ledger;
`--energy` adds a per-row estimate to a `--dry-run`/`--append`
breakdown. Order-of-magnitude only — the coefficients are documented
in the script.

## User context

User: Jeff Kunzelman (`SpaceTrucker2196` on GitHub). river.io LLC.
