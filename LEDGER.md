# {{REPO_NAME}} — token / cost ledger

Append-only. Rows are produced by `~/.claude/billing/ledger.py
--append` after each substantive commit. Never hand-author, estimate,
or rewrite rows. If the script can't produce a row, stop and surface
it. Energy estimate for the whole ledger: `ledger.py --energy-total`.

| commit | date | model(s) | input | output | cache_read | cache_write | cost_usd | summary |
|--------|------|----------|------:|-------:|-----------:|------------:|---------:|---------|
<!-- ledger rows appended here -->
| f066bbe | 2026-08-05T16:44:28Z | claude-opus-5 | 131 | 65143 | 4392990 | 157363 | 5.3994 | Add Track C upgrade mode and cygnus code-viz integration to the template |
| 2db6926 | 2026-08-06T18:27:33Z | claude-opus-5 | 1694 | 828779 | 283774686 | 5074581 | 213.3611 | Add DECISIONS.md: the record of what the factory refused |
