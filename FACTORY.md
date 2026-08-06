# {{REPO_NAME}} — factory runbook

> FIRST RUN: rewrite every section below with this repo's *real*
> commands. The TL;DR must work from a fresh clone. Adapt to CI that
> already exists — never replace working CI with generic CI.
>
> UPGRADING an existing factory: this file is a stub, and a stub
> never overwrites content. Keep the repo's runbook; amend only the
> sections that have gone stale. See FIRST_RUN.md Track C.

## 0. TL;DR

```
[clone]
[install toolchain]
make test        # must exit 0
[build]          # must be warning-clean
```

If `make test` is green and the build produces no warnings, the
factory is operational.

## Layout

[Directory map — what lives where, what's generated vs authored.]

## Toolchain

[Languages, versions, package managers, how to install them.]

## CI

[Workflows that exist and what each judges. CI is the post-hoc
judge; the merge gate is the local green suite enforced pre-push.]

## Cold-start sanity loop

1. Fresh clone.
2. `make test` → exit 0.
3. Build → zero warnings.
4. [Smoke-run the product — one command, one observable result.]

## Code visualization (cygnus)

This repo is meant to be legible in **cygnus** — our code-viz tool
(`~/projects/cygnus`, macOS). It models the system as a knowledge
graph from repository evidence, renders it as a 2D pattern visualizer
(cycles, coverage, callers, roles), and doubles as this factory's ops
dashboard. Register the repo once, re-index after large changes:

    cd ~/projects/cygnus/CygnusCore
    swift run cygnus register <path to this repo>
    swift run cygnus index

Or add it in the app, which also installs/refreshes the factory.

Keeping the picture honest is a repo-side job. Cygnus reads:

- **Source, directly** — Swift, Python, C, Rust; no build required,
  error-tolerant on checkouts that don't compile.
- **Factory docs** — `MISSION.md`, `AGENTS.md`/`CLAUDE.md`,
  `FACTORY.md`, `PROGRESS.md`, `ROADMAP.md`, `docs/milestones.md`,
  `README.md`, and markdown under `docs/`, `docs/wiki/`,
  `docs/views/`. Docs outside those roots don't reach the dashboard.
- **`LEDGER.md` / `METRICS.md` / `DECISIONS.md` tables** — parsed
  *positionally* by column order. Keep the shipped headers and column
  order exactly; a renamed or reordered column silently drops rows
  from the dashboard. `LEDGER.md` is machine-owned (read-only in the
  app), `METRICS.md` and `DECISIONS.md` are append-only.
- **`docs/converge.md` steps** — numbered `N. **Title.** detail…`.
  Keep that shape or the loop stops rendering.
- **Commit subjects** — `(closes #N)` / `fixes #N` / `resolves #N`
  links a commit to its production order; `chore(ledger):` and
  metrics commits are recognised and kept out of throughput.
- **Coverage rings** — SPM's llvm-cov export at
  `.build/<triple>/debug/codecov/*.json`. Where the toolchain
  supports it, the oracle should produce coverage (`swift test
  --enable-code-coverage`); with no artifact the rings stay empty.
  Cygnus only ever reads what a test run produced.
- **CI flow** — fastlane lanes when a `Fastfile` exists, otherwise
  `Makefile` targets and GitHub workflow steps. Target and lane names
  *are* the diagram; name them for what they do.
- **GitHub Pages** — the repo's published site (the `wiki/`
  workflow above) shows as a live preview per repo.

## Where to read next

| Question | Read |
|---|---|
| What is this product? | `MISSION.md` |
| How do agents behave here? | `AGENTS.md`, `docs/dark-factory.md` |
| How does one order ship? | `docs/converge.md` |
| What's in flight? | `PROGRESS.md` |
