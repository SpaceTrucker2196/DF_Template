---
title: The factory pattern
layout: default
---

# The factory pattern

A dark factory repository holds everything an agent needs. A fresh clone, on a fresh machine, handed to an agent that never saw the project, must be enough. Source: [Order 001](../blog/2026-07-27-the-repo-is-the-factory.html). The template files below implement it.

## What the tree holds

| Need | Template file | Test |
|---|---|---|
| Why the software exists, what it must never become | `MISSION.md` | The "must never become" list holds the lines nobody crosses |
| How to build and where files go | `AGENTS.md`, `FACTORY.md` | An agent can do a routine feature with no questions |
| Ground truth | the test suite named in `FACTORY.md` | Green means ship-ready |
| When the agent stops | autonomy contract in `docs/dark-factory.md` | Three lists: decides, decides and flags, stops and asks |
| How one order ships | `docs/converge.md` | Nine steps. A failed gate loops back |
| What happened | `LEDGER.md`, `METRICS.md` | Append-only |
| What was refused | `DECISIONS.md` | A refusal is a decision |

## Three rules for the oracle

1. Write tests from first principles. Never feed a parser its own output.
2. Ship every bug fix with the test that would have caught it.
3. Keep builds warning-clean.

If the honest description of the suite is "it mostly catches things", the human is still the oracle (Order 001).

## The autonomy boundary

An agent with no written boundary asks about everything, or decides everything. The contract has three buckets:

- **Decides.** Naming, structure, obvious bug fixes, features that fit a documented pattern, refactors that keep the public contract.
- **Decides and flags.** Choosing between two reasonable architectures, disabling a test, adding a dependency. The commit message says what and why.
- **Stops and asks.** Edits to the non-negotiable rules, broken external contracts, destructive actions, reaching outside the repo, money, scope growth.

Tactical doubt is not a reason to stop. Structural doubt is. Most bad autonomous work is a structural question answered as if it were tactical (Order 001).

## The production order

A production order is a GitHub issue whose body is the spec. The command `/converge <issue#>` runs it. The nine steps are: read the order, plan, generate, converge, self-review, risk gate, ship, instrument, report. The full text is in `docs/converge.md`.

Step 8 makes it a factory. Each shipped order appends a row to `METRICS.md` with the issue, the commit, the iteration count and the test count. Cost goes in a separate ledger. Nobody rewrites rows. A factory that reports only its clean runs is a brochure (Order 001).

## The drill

Clone the repo onto a machine that never built it. Give it to an agent that never saw it. Ask for one real feature. Stay out of the room. Whatever the agent asks is the next document the repo needs.

## Where the pattern bends

- A standard of truth outside the codebase protects against agents that game visible tests ([Order 005](../blog/2026-06-15-the-holdout-set-how-to-trust-code-no-human-reviews.html)).
- A committed rules file lowers quality cost, but 73.8 percent of such files were never updated ([Order 028](../blog/2026-08-27-a-few-pages-of-markdown.html)). Keep the file alive.
- A slow suite tiers the gate and never lowers it. This is an owner decision recorded in `DECISIONS.md`.
