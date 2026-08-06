# FIRST RUN — read this before anything else

You are an agent standing in a dark-factory skeleton that has just
been installed into a repository. Your job in this session is to
**adapt the factory to this repository**, then delete this file.
Until FIRST_RUN.md is gone, the factory is not operational.

There are three ways this skeleton got here. Determine which, then
follow that track.

## Prime directive: evaluate and update, never replace

This applies to every track, but it is the whole job in Track C.

A skeleton file is a *stub* — placeholders, bracketed prompts,
`{{REPO_NAME}}`. A file already in the repo is *content* — someone,
human or agent, decided it. **Content always wins over a stub.** You
are here to fill gaps and refresh what has drifted, not to reset the
repo to factory defaults.

The cygnus "Install Factory" action is additive by design: it writes
only files the repo lacks and reports the rest as skipped. So on a
repo that already has a factory, the only new file is usually this
one — FIRST_RUN.md, which the first run deleted. **Its reappearance
is the upgrade trigger**, not a signal that the factory was reset.

Before you change anything:

    git status
    git diff --stat

Everything untouched is intentional. If some other tool *did*
overwrite a file that had real content, restore it first —
`git show HEAD:<file> > <file>` — and treat the skeleton version as
a checklist to read, not a file to keep. If skeleton copies landed
beside existing files (`FACTORY.md.new` and the like), diff them,
merge what's missing into the real file, then delete the copy.

## In all modes: the wiki and its site

The skeleton ships `wiki/` (the knowledge base — research accumulates
there with sources from day one) and `.github/workflows/pages.yml`
(publishes it as the repo's GitHub Pages site). After the repo exists
on GitHub, enable Pages once:

    gh api repos/{owner}/{repo}/pages -X POST -f build_type=workflow

Replace `{{REPO_NAME}}` in `wiki/README.md` with the rest. If the
repo already has a `wiki/` with pages in it, leave every page alone —
only add the house rules and the Pages workflow if they're missing.

## Which mode am I in?

- **Upgrade** — this repo already runs a factory: `FACTORY.md`,
  `AGENTS.md`, or `docs/dark-factory.md` exist with real content, or
  `LEDGER.md` / `METRICS.md` carry rows. → **Track C**.
- **Inserted** — this repo contains a product (source code, history,
  maybe CI) but no factory. → **Track A**.
- **Fresh** — this repo is new; the skeleton is all there is. →
  **Track B**.

Check in that order; the first match wins. `git log --oneline | wc -l`
> a handful of commits that aren't this skeleton rules out Fresh.

## Track A — Inserted into an existing repo

1. **Inventory the repo.** Read the README, walk the tree. Identify:
   language(s), package manager(s), build entry points, test
   runner(s), lint/format tools.
2. **Detect existing CI and tooling.** Look for `.github/workflows/`,
   `fastlane/`, `Makefile`, `package.json` scripts, `Package.swift`,
   `*.xcodeproj`/`project.yml`, `CMakeLists.txt`, `pyproject.toml`,
   Dockerfiles. **The factory adapts to what exists — never replace
   working CI with generic CI.**
3. **Rewrite `FACTORY.md`** so its TL;DR and cold-start loop use the
   repo's real commands. If the repo has CI workflows, document them
   as the post-hoc judge. If it has none, add one minimal workflow
   that runs the real test command.
4. **Make `make test` real.** Either wire the placeholder Makefile to
   the repo's actual test entry point, or — if the repo has its own
   canonical test command and adding a Makefile is alien to its
   ecosystem — document that command as the oracle in `FACTORY.md`
   and delete the placeholder Makefile.
5. **Draft `MISSION.md`** from what the repo evidently is. Mark every
   invariant you inferred with `(draft — owner to confirm)`. Do not
   invent sacred invariants the owner didn't state; propose them.
6. **Fill `AGENTS.md`** architecture + conventions sections from the
   observed codebase (match its real idioms, don't prescribe new
   ones).
7. **Run the cold-start loop** you just wrote in `FACTORY.md`. It
   must pass from a clean state. If it can't go green because of
   pre-existing failures, record that honestly in `PROGRESS.md` —
   never delete or skip failing tests to get to green.
8. **Wire up code visualization.** Fill FACTORY.md's "Code
   visualization" section for this repo — the coverage artifact its
   oracle produces (if any), whether CI flow comes from fastlane or
   the Makefile — then register it with cygnus and confirm the graph
   and the ops dashboard render.
9. **Replace every remaining `{{REPO_NAME}}` placeholder**, delete
   this file, and commit:
   `feat: adapt dark-factory skeleton to <repo>` with a body listing
   what you detected and what you decided.

## Track B — Fresh factory repo

1. **Ask the owner for the mission** if it wasn't given: what is the
   product, what are the non-negotiables, what is out of scope.
   Write `MISSION.md` first — the factory exists to serve it.
2. **Pick the toolchain** with the owner (language, build, test).
   Write `FACTORY.md`'s TL;DR and cold-start loop for it.
3. **Scaffold the build** so `make test` runs a real (initially
   tiny) suite and exits 0. A factory with no oracle is not a
   factory.
4. **Write the autonomy contract** in `docs/dark-factory.md` §4 with
   the owner: what you decide, what you decide-and-flag, what stops
   and asks.
5. Add one minimal CI workflow that re-runs the suite as post-hoc
   judge (never the merge gate — the gate is local green pre-push).
6. **Cold-start drill**: from a fresh clone, land one real (small)
   feature end-to-end. Every question you had to ask is the next
   doc to write.
7. **Wire up code visualization** — FACTORY.md's "Code
   visualization" section, then register the repo with cygnus.
8. Replace placeholders, delete this file, commit as in Track A.

## Track C — Upgrade a repo that already has a factory

The factory here is running. You are refreshing its scaffolding, not
rebuilding it. Read the prime directive above before step 1.

### Never touch

These are the repo's memory. Read them; do not rewrite, reformat,
renumber, or "clean up" them:

- `DECISIONS.md` — append-only. Supersede a decision with a new row;
  never edit or delete an old one. The refusals are the most valuable
  rows in the file precisely because nothing else in the repo records
  them.
- `LEDGER.md` and `METRICS.md` rows — append-only, script-generated.
  You may update the header prose above the table if the skeleton
  documents a flag the local copy is missing; never a row.
- `PROGRESS.md` history — append your upgrade entry at the top.
- `wiki/` and `research/` pages, and their sources.
- Sacred invariants in `MISSION.md` that the owner confirmed (they
  aren't marked `draft`), and the three lists in
  `docs/dark-factory.md` §4.
- Working CI, build files, and the real test command.

### 1. Establish the incumbent

Read the repo's `FACTORY.md`, `AGENTS.md`, `MISSION.md`,
`docs/dark-factory.md`, `SECURITY.md` and note, for each, whether
it's real content, a half-filled stub, or still template text. Run
the oracle (FACTORY.md's TL;DR) **before** you change anything and
record whether it was green — you need to know which failures you
inherited.

### 2. Audit against the skeleton

For every component the skeleton ships, classify the repo's version
as *missing*, *stale*, or *fine*:

| Component | Present and real means |
|---|---|
| `FACTORY.md` | TL;DR uses this repo's real commands and works from a fresh clone |
| `AGENTS.md` | Architecture + conventions describe the actual codebase; discipline bullets present |
| `MISSION.md` | Charter, numbered sacred invariants, non-goals — no bracketed stubs |
| `docs/dark-factory.md` | §4 autonomy contract filled with the owner's three lists |
| `docs/converge.md`, `.claude/commands/converge.md` | The converge loop is documented and invokable |
| `LEDGER.md` | Header documents `ledger.py --append`; rows exist if commits do |
| `METRICS.md` | One row per shipped order |
| `DECISIONS.md` | Decisions and refusals recorded with evidence, headers unchanged |
| `SECURITY.md` | Outbound surface list is exhaustive and current |
| `PROGRESS.md`, `ROADMAP.md` | Current, not stale by months |
| `wiki/` + `.github/workflows/pages.yml` | Wiki exists with house rules; Pages workflow present and enabled |
| Code viz | FACTORY.md's "Code visualization" section is present, and the ledger/metrics/converge/commit shapes it describes still hold |
| Oracle | `make test` (or the documented command) exits 0 |

### 3. Resolve each finding

- **Missing** → add the skeleton's version, then fill it for this
  repo in the same session. Never leave a fresh stub behind: an
  unfilled placeholder is worse than an absent file, because it
  reads as documentation.
- **Stale** → amend in place. Keep the local wording, structure, and
  ordering; change only what is wrong or absent. Prefer a
  three-line patch over a rewrite.
- **Fine, but different from the skeleton** → keep the repo's
  version. Divergence is not drift. If the local approach is better
  than the skeleton's, say so in the commit body — the template is
  the thing that should change.
- **Contradicts the skeleton on substance** (e.g. local docs treat CI
  as the merge gate) → don't silently flip it. Note it in
  `PROGRESS.md` and raise it with the owner.

### 4. Verify and land

1. Run the oracle again. It must be no worse than step 1 — same
   green, or the same inherited failures and no new ones.
2. Confirm no `{{REPO_NAME}}` or bracketed placeholder survives in
   any file you touched.
3. Add a `PROGRESS.md` entry: what you added, what you amended,
   what you deliberately left alone, and anything you're raising
   with the owner.
4. Delete this file and commit:
   `chore(factory): refresh dark-factory scaffolding` with a body
   listing added / amended / kept-as-is, and the oracle's state
   before and after.

## All tracks — non-negotiable from day one

- `LEDGER.md` is live immediately: after every substantive commit run
  `~/.claude/billing/ledger.py --append --summary "<desc>"`, then
  commit `LEDGER.md` as its own `chore(ledger): <sha>` commit. Rows
  are append-only, script-generated, never estimated. If the script
  can't produce a row, stop and surface it.
- Never commit a red test. Warning-clean builds.
- The mission, conventions, tests, and autonomy boundary live
  in-tree. When the owner corrects you, the correction lands in a
  doc, not just in the conversation.
