# /converge — run one production order to shipped

`/converge <issue#>` takes a GitHub issue (the production order) to a
pushed, instrumented commit. Steps run in order; a failed gate loops
back, it never skips forward.

1. **Read the order.** `gh issue view <n>` — the issue body is the
   spec. Ambiguity → comment on the issue and stop.
2. **Plan.** Small written plan (files touched, tests to add, risks).
3. **Generate.** Implement plan; tests land with the code.
4. **Converge.** Run the oracle (`FACTORY.md` TL;DR) until green.
   Count iterations — the count is reported in METRICS.md.
5. **Self-review.** Diff read end-to-end; simplify; check against
   AGENTS.md conventions and MISSION.md invariants.
6. **Risk gate.** Anything in the stops-and-asks list
   (docs/dark-factory.md §4) → stop and surface before shipping.
7. **Ship.** Commit (imperative subject, why in body,
   `Closes #<n>`), push.
8. **Instrument.** Append the METRICS.md row; run
   `~/.claude/billing/ledger.py --append --summary "<desc>"`; commit
   `LEDGER.md` as its own `chore(ledger): <sha>` commit.
9. **Report.** Comment the shipped commit + summary on the issue.
