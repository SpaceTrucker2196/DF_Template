# FIRST RUN — read this before anything else

You are an agent standing in a freshly installed dark-factory
skeleton. Your job in this session is to **adapt the factory to this
repository**, then delete this file. Until FIRST_RUN.md is gone, the
factory is not operational.

There are two ways this skeleton got here. Determine which, then
follow that track.

## Which mode am I in?

- **Inserted** — this repo already contains a product (source code,
  history, maybe CI). The skeleton was copied in beside it.
- **Fresh** — this repo is new; the skeleton is all there is.

`git log --oneline | wc -l` > a handful of commits that aren't this
skeleton → you're in **Inserted** mode.

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
8. **Replace every remaining `{{REPO_NAME}}` placeholder**, delete
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
7. Replace placeholders, delete this file, commit as in Track A.

## Both tracks — non-negotiable from day one

- `LEDGER.md` is live immediately: after every substantive commit run
  `~/.claude/billing/ledger.py --append --summary "<desc>"`, then
  commit `LEDGER.md` as its own `chore(ledger): <sha>` commit. Rows
  are append-only, script-generated, never estimated. If the script
  can't produce a row, stop and surface it.
- Never commit a red test. Warning-clean builds.
- The mission, conventions, tests, and autonomy boundary live
  in-tree. When the owner corrects you, the correction lands in a
  doc, not just in the conversation.
