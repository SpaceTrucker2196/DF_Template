# {{REPO_NAME}} — dark factory

This repo runs as a **dark factory**: the mission, the conventions,
the tests, and the autonomy boundary are all in-tree, so an agent can
walk in cold and continue building without a human in the inner loop.
Canonical reference: `sloth/agents/dark-factory.md`; this file is the
repo-local adaptation.

## 1. The pattern

- **Production orders** are GitHub issues. `/converge <issue#>`
  (docs/converge.md) runs one order to a pushed commit.
- **The oracle is the test suite.** The merge gate is the local green
  suite enforced pre-push; CI is a post-hoc judge, never the gate.
- **A slow suite tiers the gate — it never lowers it.** When the full
  run grows too slow to pay at every commit, the owner may rule:
  targeted tests at commit, the full suite at the push, marathon
  suites at release only. Long runs go to a background task and get
  read when they land. Never start a full suite on a machine already
  running one — two runs halve each other. Tiering is an owner
  decision, recorded in DECISIONS.md, never improvised mid-session.
- **Instrumentation is mandatory**: every shipped order appends a
  `METRICS.md` row; every substantive commit appends a `LEDGER.md`
  row via `ledger.py`.

## 2. Level-5 readiness checklist

An agent self-checks on first run:

- [ ] Mission in-tree (`MISSION.md`) with sacred invariants
- [ ] Conventions in-tree (`AGENTS.md`) matching the real codebase
- [ ] Tests are ground truth and runnable one command from cold
- [ ] Build/infra runbook (`FACTORY.md`) works from a fresh clone
- [ ] Autonomy boundary written down (§4 below)

## 3. What agents must never do here

- Ship a red test, skip a failing test, or weaken an assertion to
  pass.
- Rewrite append-only records (LEDGER.md, METRICS.md rows).
- Add outbound network/OAuth/credential surface without stopping to
  ask.

## 4. Autonomy contract

> FIRST RUN: set these three lists with the owner. Until then,
> everything not listed under "decides" is stops-and-asks.
>
> UPGRADING an existing factory: the owner set these lists. Leave
> them alone — widening the agent's autonomy is the owner's call,
> never an upgrade's side effect.

**The agent decides** (no flag needed):
- [e.g. internal refactors that keep the suite green]

**The agent decides and flags** (lands the change, notes it for
owner spot-check):
- [e.g. behavioral changes visible to users]

**The agent stops and asks**:
- New dependencies; anything touching money, credentials, or
  outbound surface; destructive git operations; violating a sacred
  invariant.
