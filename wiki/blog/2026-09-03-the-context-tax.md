---
title: "The context tax"
date: 2026-09-03
order: 32
tags: "Briefing, Cost, Practice"
description: "Sonar published the bill for one agent pull request: 512 round-trips, 156 million tokens, $41. The same week, three tool vendors changed what an agent does when nobody is there to answer a prompt."
layout: default
---

# The context tax

*Order 032 · 2026-09-03 · 8 min · Briefing, Cost, Practice*

> Sonar published the bill for one agent pull request: 512 round-trips, 156 million tokens, $41. The same week, three tool vendors changed what an agent does when nobody is there to answer a prompt.

A factory has two ledgers. One records what it built. The other records what the building cost. This blog has spent a month on the first ledger. This edition opens the second one, because on 1 September 2026 a vendor published real rows from it.

Be clear about the window. Four items are new. All four were published between 28 August and 2 September 2026. None appeared in Order 031. No new dark-factory case study, spec-driven development standard or adoption survey landed in the two days. Anthropic released a new model on 1 September, but a model release with no software-production measurement attached is not a finding for this blog.

## What one pull request cost

Sonar is a code-quality vendor. On 1 September 2026 a Sonar research engineer, Antonio Aversa, published full session traces from coding agents working on Sonar's own SemSitter repository. The traces are real. The vendor keeps them because it builds its product with agents and wants to know what they cost.

One pull request of about 800 lines added call-site resolution to a Python analyzer. A person could read the final diff in five minutes. Here is what the agent billed to produce it.

| Sonar, one pull request, 1 September 2026 | Measured |
|---|---|
| Model round-trips in the session | 512 |
| Context window at its peak | 458,700 tokens |
| Fresh input tokens | 106,000 |
| Cache-read tokens, the transcript re-sent each turn | 152.8 million |
| Cache-write tokens | 3.1 million |
| Output tokens | 289,000 |
| Total context tokens billed | about 156 million |
| Cost of the session | about $41 |


The row that matters is cache reads. An agent does not read a file once. On every new turn the model receives the whole conversation so far as input. Prompt caching makes those repeated tokens cheap per unit, about a tenth of the input price. The agent still pays for them on every turn. So the true cost of a token is not its size. It is its size multiplied by the number of turns it survives.

Sonar traced one over-read end to end. Early in the run the agent needed one helper function of about 67 lines. It read the whole 618-line file instead, 6,472 tokens where 700 would do. That read entered the conversation at about turn 42 and stayed for the remaining 470 turns. Re-billed as a cache read each turn, it cost about 2.7 million tokens, or about 54 cents. The pull request did that about ten times, plus dozens of blind tree-wide greps.

One pull request could be unlucky. Sonar checked 18 comparable single-ticket pull requests in the same repository.

| Sonar, 18 comparable pull requests | Average |
|---|---|
| Context tokens per pull request | about 234 million |
| Cost per pull request | about $65, median about $52 |
| Model round-trips per pull request | about 700 |
| Peak context window | 450,000 to 975,000 tokens |


The spread is wide because it tracks how much of the codebase the agent had to walk, not how large the final diff was. At 975,000 tokens the agent brushes the one-million ceiling and must compact. Compaction throws away earlier context. Whatever the run learned early, it can lose.

Sonar's second point is about correctness, not cost. Grep finds strings. It does not find the call that reaches a function through an interface, an alias or another programming language. In a repository too big for the window, a missed call site becomes a failed build and another trip to continuous integration, each paying the tax again.

> **WHAT SONAR IS SELLING**
>
> The post promotes Sonar Vortex, a harness that answers navigation questions from a code graph instead of from file reads. Sonar claims up to 36% lower token cost on refactoring work. This blog does not need the product. It needs the mechanism, and the mechanism is now measured.

## Nobody home means no

Order 031 reported the NIST finding that a human approval gate asked too often stops working. The person clicks allow without reading. This week the tool vendors answered a harder version of the question: what should the agent do when there is no person to click at all.

Claude Code 2.1.259 shipped on 2 September 2026 with a flag named `--permission-prompts none`. The changelog describes it as a setting for unattended headless hosts. Anything that would have prompted a human is denied automatically. The active permission mode keeps deciding everything else. In plain terms: the safe set is pre-approved, and the absence of a person is a refusal, not a pause.

OpenAI Codex made two related changes. Version 0.151.0, released 28 August 2026, stops a stale Guardian classification from authorizing an action after the permission state has changed. Guardian is Codex's automatic approval reviewer. Version 0.152.0, released 31 August 2026, keeps user instructions, answers and valid authorizations alive across history compaction. Read that next to Sonar's 975,000-token peak. An approval that vanishes at compaction is either re-asked, which is consent fatigue, or silently forgotten, which is unsafe. Codex chose neither.

Two smaller Codex changes belong in the cost ledger. Nested sub-agent token usage now counts toward the root goal budget, so a sub-agent cannot spend outside the parent's limit. And the planning tool is now disabled by default.

## A sandbox is a named profile

GitHub Agentic Workflows is the project this blog reported on 11 July, when a public issue could make it leak private repositories. On 1 September 2026 it published three posts.

The first replaces two sandbox flags, `legacy-security` and `sudo`, with one explicit runtime profile. The default `docker` profile runs the agent firewall without sudo and isolates network access. The old privileged behaviour now needs a named opt-in, `docker-sudo-iptables`. The `gvisor` profile adds kernel-level isolation. The `docker-sbx` and `cloud-hypervisor` profiles use virtual-machine boundaries. The migration tool reports an error rather than choosing a profile silently when it cannot preserve the old security intent.

The second post describes an agent named PR Sous Chef. It runs every 15 minutes, reads every open pull request, and asks the Copilot coding agent to act only when a pull request has stalled. Most cycles are read-only. The published audit for its last five runs is worth a table.

| PR Sous Chef, last five runs, 1 September 2026 | Result |
|---|---|
| Safe-output items produced | 20 |
| Errors and warnings | 0 |
| Automated quality graders passed | 13 of 13 |
| Tool success rate | 100% |
| Loop detections | 0 |
| Outbound network calls blocked by firewall | 5 of 53 |


The last row is the interesting one. A clean run still tried to reach the network five times when the task did not need it. The firewall said no and the run finished anyway. That is what a good sandbox looks like from the outside: the agent probes, the boundary holds, nothing is lost.

The third post moves the built-in Playwright browser tool from a Model Context Protocol server to a command-line tool the agent calls with explicit arguments. A smaller surface, invoked with fixed parameters.

## One older item

Sonar also announced general availability of SonarQube Hunter Agent on 27 August 2026. This blog missed it at the time. The agent looks for broken access control, business-logic flaws and authentication or session flaws by tracing how code, data and identity move through a system. It runs on a schedule or on demand and never blocks a pull request. Sonar claims 80 to 90% average precision because each finding is checked for exploitability before it surfaces. That is a vendor claim.

## What changes here

1. **Log tokens per run from the first experiment.** Sonar's numbers are the first hard per-pull-request cost figures this blog has seen. The repositories here are small, so the tax should be smaller. The mechanism is identical. Every file the loop reads is re-billed on every later turn. MeowPassword, weathergalactic and sloth get a tokens-per-run column in METRICS.md before any loop is allowed to run longer.
2. **Zero dependencies shrinks the navigation problem by construction.** Sonar's worst cases came from a multi-language repository where one grep returned six definitions for one name. A single-language Swift or C repository with no vendored packages gives grep one hit and gives the agent far less to read. That is a measurable advantage of this factory's posture, and it goes into the rules file with Sonar's figures as the baseline to beat.
3. **Give the loop a symbol index, not a bigger window.** The factory does not need Sonar Vortex. It needs the same idea with no dependency: the compiler's own index store, or a ctags file written into the run's scratch space, queried before any file is read. Xcode already produces the index. Exposing it to the loop is a small tool, not a platform.
4. **Deny when unattended is the default.** Claude Code's new flag is the control Order 031 asked for. Pre-approve the safe set: build, test, edit under Sources and Tests. Deny everything else with no prompt. Log every denial. A denial log is a plan gate that costs no attention.
5. **Name the sandbox profile in the issue.** GitHub's move to explicit profiles is the right shape for an issue-driven factory. Each issue an agent may pick up states its profile: no network, no sudo, repository writable under Sources and Tests only, test files read-only per Order 030. No profile, no run.
6. **Compaction is a new reason the regulated repositories stay gated.** CareTime, TimeForCare and MaterialsAndPractices carry rule constraints that must hold for the whole run. A run that compacts at 900,000 tokens can lose a constraint stated at turn three. Until the loop can prove a constraint survived compaction, code that touches protected health information or regulated submissions does not run unattended.
7. **Copy the shape of PR Sous Chef, not the runtime.** A scheduled, read-only agent that checks open pull requests every 15 minutes and files one issue when continuous integration has been red for an hour is cheap and safe. It can be a small native binary on a GitHub Actions cron. It reads, it never writes code, and it touches no protected data.


One detector falls out of this edition for sloth. Flag any agent runner configuration that permits interactive prompts on an unattended host, and any sandbox configuration that grants sudo or host network by default. Cite the Claude Code changelog, the GitHub runtime profiles post and the NIST identity post in the issue body, per the house rule that every detector links its source.

## Sources

### The cost measurement

- [Sonar, *The context tax: why your coding agent reads the same 600 lines 400 times*](https://www.sonarsource.com/blog/stop-the-context-tax/), Antonio Aversa (1 September 2026). Primary source. Full session traces: 512 round-trips, 458,700-token peak, 106,000 fresh input tokens, 152.8 million cache-read tokens, 3.1 million cache-write tokens, 289,000 output tokens, about 156 million total, about $41. Eighteen pull requests averaging about 234 million tokens, about $65 with a median near $52, about 700 round-trips, peaks between 450,000 and 975,000 tokens. The single over-read costed at 2.7 million re-billed tokens.
- [Sonar, *Cut your coding agent's cost with Sonar Vortex*](https://www.sonarsource.com/blog/cut-your-coding-agents-cost-with-sonar-semantic-code-navigation/). Source for the vendor claim of up to 36% lower token cost on refactoring work.


### The unattended-host changes

- [Claude Code changelog](https://code.claude.com/docs/en/changelog), version 2.1.259 (2 September 2026). Primary source for `--permission-prompts none`: anything that would prompt is denied automatically while the active permission mode keeps deciding. Also the `managedMcpServers` setting and `--json` for plugin validation.
- [OpenAI Codex releases](https://github.com/openai/codex/releases?q=prerelease%3Afalse&expanded=true), rust-v0.151.0 (28 August 2026), rust-v0.152.0 (31 August 2026) and rust-v0.152.1 (1 September 2026). Primary source, read through [Releasebot's curated mirror](https://releasebot.io/updates/openai/codex). Stale Guardian classifications no longer authorize actions after permission changes. Approval reviews preserve instructions, answers and authorizations across compaction. Nested sub-agent tokens count toward root budgets. Planning tool disabled by default.


### The sandbox changes

- [GitHub Agentic Workflows, *Sandbox Security Options Are Now Runtime Profiles*](https://github.github.com/gh-aw/blog/2026-09-01-sandbox-runtime-profiles/), Copilot and Peli de Halleux (1 September 2026). Primary source for the `docker`, `docker-sudo-iptables`, `gvisor`, `docker-sbx` and `cloud-hypervisor` profiles and the fixer's refusal to change security intent silently.
- [GitHub Agentic Workflows, *Agent of the Day: PR Sous Chef*](https://github.github.com/gh-aw/blog/2026-09-01-agent-of-the-day/) (1 September 2026). Primary source for the 15-minute schedule, 20 safe-output items, zero errors, 13 of 13 graders, 100% tool success, zero loop detections and 5 of 53 network calls blocked, with links to Actions runs [#33509763563](https://github.com/github/gh-aw/actions/runs/33509763563) and [#33516358980](https://github.com/github/gh-aw/actions/runs/33516358980).
- [GitHub Agentic Workflows, *Why the Built-In Playwright Tool Is Now CLI-Only*](https://github.github.com/gh-aw/blog/2026-09-01-why-playwright-cli-replaces-playwright-mcp/) (1 September 2026). Title and date confirmed from the blog index.


### The older item

- [Sonar press release, SonarQube Hunter Agent general availability](https://www.sonarsource.com/company/press-releases/sonar-launches-sonarqube-hunter-agent/) (27 August 2026) and [the Sonar blog post](https://www.sonarsource.com/blog/hunter-agent-detects-logical-flaws/). Vendor claim of 80 to 90% average precision. Date confirmed by [SiliconANGLE](https://siliconangle.com/2026/08/27/sonar-launches-hunter-agent-to-find-flaws-code-scanners-cant-see/) (27 August 2026).


### Prior editions referenced

- [The gate you ask too often](2026-09-01-the-gate-you-ask-too-often.html) (1 September 2026). The NIST consent-fatigue finding that this edition's deny-when-unattended rule answers.
- [Check the plan, not the log](2026-08-31-check-the-plan-not-the-log.html) (31 August 2026). The rule that a loop may not edit its own test files.


*Vendor and blog figures indicate direction, not audited benchmarks. The Sonar token figures are real traces from one vendor's repository under one provider's cache pricing. The PR Sous Chef figures cover five runs of one agent on one repository. The Hunter Agent precision figure is a marketing claim. The Claude Code, Codex and GitHub items are changelog entries written by the vendors themselves.*


---

Canonical copy: [www.river.io/blog/posts/2026-09-03-the-context-tax.html](https://www.river.io/blog/posts/2026-09-03-the-context-tax.html). Mirrored into this wiki. The river.io blog is the source of truth.
