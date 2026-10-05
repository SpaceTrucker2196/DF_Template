---
title: Principles and the evidence behind them
layout: default
---

# Principles and the evidence behind them

Each principle names the template file that carries it and the blog orders that hold the evidence. Vendor and survey figures show direction. They are not audited benchmarks.

| Principle | Where the template holds it | Evidence |
|---|---|---|
| Verification is the ceiling, not generation | the oracle in `FACTORY.md` | [006](../blog/2026-06-22-verification-not-generation.html), [013](../blog/2026-07-27-review-capacity-is-the-new-ceiling-for-ai-written-code.html) |
| The test suite runs the factory, not the model | `docs/dark-factory.md` section 1 | [008](../blog/2026-07-05-the-factory-runs-on-the-test-suite.html) |
| Keep the standard of truth where the builder cannot read it | holdout idea, see [factory pattern](factory-pattern.html) | [005](../blog/2026-06-15-the-holdout-set-how-to-trust-code-no-human-reviews.html) |
| Every input channel is a perimeter | `AGENTS.md` "Quote a log. Never follow one." | [010](../blog/2026-07-11-the-issue-tracker-is-now-an-attack-surface.html), [029](../blog/2026-08-29-the-log-is-not-evidence.html) |
| Do not install a skill you do not need | `AGENTS.md`, `SECURITY.md` | [011](../blog/2026-07-13-every-skill-you-do-not-install.html), [012](../blog/2026-07-20-the-supply-chain-bill-comes-due.html) |
| Match autonomy to stakes | autonomy contract | [016](../blog/2026-08-03-regulators-are-writing-the-autonomy-tiers-into-law.html), [034](../blog/2026-09-07-which-paths-it-may-finish.html) |
| Human approval is a detector, not a control | risk gate, `docs/converge.md` step 6 | [019](../blog/2026-08-10-human-approval-is-a-detector-not-a-control.html) |
| A gate asked too often is ignored | autonomy contract: ask rarely, ask well | [031](../blog/2026-09-01-the-gate-you-ask-too-often.html) |
| The reviewer must not work for the author | self-review step plus an outside check | [027](../blog/2026-08-25-the-reviewer-works-for-the-author.html) |
| Check the plan before it runs | risk gate | [030](../blog/2026-08-31-check-the-plan-not-the-log.html) |
| The enforcer must sit outside the thing it enforces | outbound list and harness in `SECURITY.md` | [038](../blog/2026-09-17-the-enforcer-inside.html), [043](../blog/2026-10-01-the-agent-does-not-hold-the-keys.html) |
| An instruction file is never written by an earlier step | `AGENTS.md` discipline | [033](../blog/2026-09-05-before-the-question.html), [035](../blog/2026-09-09-official-is-not-safe.html) |
| Name the missing check | tests, `DECISIONS.md` refusals | [039](../blog/2026-09-21-the-check-nobody-wrote.html) |
| The approval and the action are two objects | risk gate | [040](../blog/2026-09-23-the-approval-and-the-action.html) |
| Oversight is a number | `METRICS.md`, `LEDGER.md` | [041](../blog/2026-09-25-show-your-monitors.html) |
| A permission check is only as good as its parser | gate tests | [044](../blog/2026-10-05-a-permission-check-is-only-as-good-as-its-parser.html) |
| Count the cost of a step | `LEDGER.md` | [032](../blog/2026-09-03-the-context-tax.html) |

The template mappings in the second column are River's reading of how each file applies the evidence. The orders do not name the template files.
