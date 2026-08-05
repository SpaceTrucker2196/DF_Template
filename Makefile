# {{REPO_NAME}} — factory targets.
# FIRST RUN: wire `test` to this repo's real suite, or delete this
# Makefile and document the repo's canonical test command as the
# oracle in FACTORY.md.
# UPGRADING: if the repo already has a working oracle, delete this
# file — it must never shadow a real Makefile or test command.

.PHONY: test
test:
	@echo "FIRST RUN: 'make test' is not wired to a real suite yet."
	@echo "See FIRST_RUN.md — the factory is not operational."
	@exit 1
