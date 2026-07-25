# {{REPO_NAME}} — token / cost ledger

Append-only. Rows are produced by `~/.claude/billing/ledger.py
--append` after each substantive commit. Never hand-author, estimate,
or rewrite rows. If the script can't produce a row, stop and surface
it. Energy estimate for the whole ledger: `ledger.py --energy-total`.

| commit | date | model(s) | input | output | cache_read | cache_write | cost_usd | summary |
|--------|------|----------|------:|-------:|-----------:|------------:|---------:|---------|
<!-- ledger rows appended here -->
