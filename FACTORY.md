# {{REPO_NAME}} — factory runbook

> FIRST RUN: rewrite every section below with this repo's *real*
> commands. The TL;DR must work from a fresh clone. Adapt to CI that
> already exists — never replace working CI with generic CI.

## 0. TL;DR

```
[clone]
[install toolchain]
make test        # must exit 0
[build]          # must be warning-clean
```

If `make test` is green and the build produces no warnings, the
factory is operational.

## Layout

[Directory map — what lives where, what's generated vs authored.]

## Toolchain

[Languages, versions, package managers, how to install them.]

## CI

[Workflows that exist and what each judges. CI is the post-hoc
judge; the merge gate is the local green suite enforced pre-push.]

## Cold-start sanity loop

1. Fresh clone.
2. `make test` → exit 0.
3. Build → zero warnings.
4. [Smoke-run the product — one command, one observable result.]

## Where to read next

| Question | Read |
|---|---|
| What is this product? | `MISSION.md` |
| How do agents behave here? | `AGENTS.md`, `docs/dark-factory.md` |
| How does one order ship? | `docs/converge.md` |
| What's in flight? | `PROGRESS.md` |
