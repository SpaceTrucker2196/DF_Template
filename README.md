# DF_Template

Bare dark-factory skeleton, modeled on sloth (the canonical
dark-factory repo). Three ways to use it:

**Insert into an existing repo** — copy every file except this
README into the repo (never overwrite files that exist), then point
an agent at `FIRST_RUN.md`. The cygnus app's "Install Factory"
button does exactly this.

**Start a new factory repo** — clone/copy the whole template, git
init, then point an agent at `FIRST_RUN.md`.

**Upgrade a repo that already has a factory** — install again. The
copy is additive, so existing files are skipped and only the missing
pieces land; the one file that always comes back is `FIRST_RUN.md`,
which the previous run deleted. That reappearance is the upgrade
trigger: the agent runs Track C, which **evaluates and updates the
existing factory rather than replacing it** — a template stub never
overwrites real content, and the append-only records (`LEDGER.md`,
`METRICS.md`), the wiki, and the owner's autonomy contract are never
touched.

Either way, `FIRST_RUN.md` carries the adaptation instructions:
determine the mode, inventory the repo, detect existing CI/build
tooling, adapt `FACTORY.md` to the real commands, fill placeholders,
delete `FIRST_RUN.md`. The factory is not operational until
FIRST_RUN.md is gone and `make test` (or the documented oracle) is
green.

`{{REPO_NAME}}` placeholders are replaced by the installer or by the
first-run agent.

Installed factories are meant to be read in **cygnus**, our code-viz
tool — see FACTORY.md's "Code visualization" section for what it
reads and which file shapes are a machine-read contract.
