# {{REPO_NAME}} — factory targets.
# FIRST RUN: wire `test` to this repo's real suite, or delete this
# Makefile and document the repo's canonical test command as the
# oracle in FACTORY.md.
# UPGRADING: if the repo already has a working oracle, delete this
# file — it must never shadow a real Makefile or test command.

# The workflow audit. Zero dependencies, so there is no excuse for it
# not to run. Green today (one push-triggered workflow); a red here is
# a real regression, not noise.
.PHONY: audit
audit:
	@tools/audit-workflows.sh

.PHONY: test
test:
	@echo "FIRST RUN: 'make test' is not wired to a real suite yet."
	@echo "See FIRST_RUN.md — the factory is not operational."
	@exit 1
