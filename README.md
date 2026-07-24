# DF_Template

Bare dark-factory skeleton, modeled on sloth (the canonical
dark-factory repo). Two ways to use it:

**Insert into an existing repo** — copy every file except this
README into the repo (never overwrite files that exist), then point
an agent at `FIRST_RUN.md`. The Cygnus app's "Install Factory"
button does exactly this.

**Start a new factory repo** — clone/copy the whole template, git
init, then point an agent at `FIRST_RUN.md`.

Either way, `FIRST_RUN.md` carries the adaptation instructions:
inventory the repo, detect existing CI/build tooling, adapt
`FACTORY.md` to the real commands, fill placeholders, delete
`FIRST_RUN.md`. The factory is not operational until FIRST_RUN.md is
gone and `make test` (or the documented oracle) is green.

`{{REPO_NAME}}` placeholders are replaced by the installer or by the
first-run agent.
