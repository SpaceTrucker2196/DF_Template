#!/bin/sh
# Installs the billing ledger where AGENTS.md expects it: ~/.claude/billing/.
# Never overwrites a newer pricing.json (prices are append-only, dated entries).
set -e
dst="$HOME/.claude/billing"
src="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$dst"
cp "$src/ledger.py" "$dst/ledger.py"
chmod +x "$dst/ledger.py"
if [ -f "$dst/pricing.json" ] && [ "$dst/pricing.json" -nt "$src/pricing.json" ]; then
  echo "kept newer $dst/pricing.json"
else
  cp "$src/pricing.json" "$dst/pricing.json"
fi
python3 "$dst/ledger.py" --help >/dev/null && echo "ledger installed at $dst"
