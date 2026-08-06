# {{REPO_NAME}} — decisions and refusals

> FIRST RUN: leave the table headers exactly as they are — they are a
> machine-read contract (see FACTORY.md's "Code visualization"). Delete
> the example row. Add real entries as decisions get made.

Append-only. One row per decision that would otherwise be re-argued
from scratch in six weeks, and a section below carrying the reasoning.

**A refusal is a decision.** "We measured this and it does not work"
is the single most expensive thing to rediscover, and the easiest to
lose — it leaves no code behind, so nothing in the repository reminds
anyone it happened. Record refusals here with their numbers, or the
next agent will cheerfully rebuild them.

## Index

| id | date | decision | status | evidence | supersedes |
|----|------|----------|--------|----------|------------|
| D0 | 2026-01-01 | *(example — delete on first run)* | adopted | none | — |

`status` is one of:

- **adopted** — in force. Change it by superseding, not editing.
- **refused** — tried, measured, rejected. The numbers live below.
- **provisional** — in force but unproven; says what would settle it.
- **superseded** — replaced. The `supersedes` column on the newer row
  points back here.

`evidence` names where the numbers are: a `PROGRESS.md` date, a
`docs/spikes/` file, a benchmark, a commit. `none` is allowed and is
itself informative — an unevidenced decision is a preference, and
saying so lets a later agent overturn it cheaply.

## D0 — example, delete on first run

**Decision.** One `##` section per row, headed `<id> — <short title>`,
so the id joins the table to the reasoning.

**Why.** The table is what a tool reads; the prose is what an agent
reads. Keeping both in one file means they cannot drift apart, which
is what happens when the record lives in an issue tracker and the code
lives here.

**What would change this.** A second consumer that needs the reasoning
structured rather than prose.
