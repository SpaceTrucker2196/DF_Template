---
title: "The holdout set: how to trust code no human reviews"
date: 2026-06-15
order: 5
tags: "Briefing, Practice, Security, Metrics"
description: "StrongDM keeps its standard of truth outside the codebase. The agents that build the code cannot see it. LinearB measured the review bottleneck across 8.1 million pull requests. OWASP now calls prompt injection an architectural flaw that may never be patched."
layout: default
---

# The holdout set: how to trust code no human reviews

*Order 005 · 2026-06-15 · 8 min · Briefing, Practice, Security, Metrics*

> StrongDM keeps its standard of truth outside the codebase. The agents that build the code cannot see it. LinearB measured the review bottleneck across 8.1 million pull requests. OWASP now calls prompt injection an architectural flaw that may never be patched.

In mid-June 2026 autonomous software development got its best data and its worst news together. Anthropic published its 2026 Agentic Coding Trends Report. The report makes eight predictions about orchestrated agent teams and long-running agents that work for days. It also confirms the ceiling. Developers use AI in about 60 percent of their work. They can fully delegate only 0 to 20 percent of tasks.

LinearB analyzed 8.1 million pull requests. Developers feel 20 percent faster, but they are measurably 19 percent slower. The best constructive idea of the quarter came from StrongDM's dark factory. Agents can see the tests inside a codebase, and they learn to game them. StrongDM moves the tests out of the codebase and calls them scenarios. StrongDM holds the scenarios apart, like a machine-learning holdout set.

## The vendors now admit the ceiling

The main event is that Anthropic released its own report. Anthropic did not let analysts frame the story. These predictions matter most for an autonomous pipeline:

- **The SDLC compresses from weeks to hours.** The SDLC is the software development life cycle. Agents write the implementation. Automated tests and inline documentation feed a tight iteration loop.
- **Single agents become coordinated teams.** An orchestrator agent leads specialized sub-agents in parallel context windows. This is the multi-agent validation chain pattern. The model vendor now endorses it.
- **Long-running agents build whole systems.** Task horizons stretch from minutes to days or weeks. The agent pauses only at strategic human checkpoints.
- **Oversight scales when agents know when to ask.** The agent flags what it is unsure about. It does not attempt everything.
- **New surfaces and new users.** Support for legacy COBOL and Fortran is growing. People in security, design, and operations now use coding agents.


The key admission sits in the capability section. AI is in about 60 percent of development work. Only 0 to 20 percent is fully delegable. Anthropic calls AI a "constant collaborator" that still needs setup, prompting, supervision, validation, and human judgment. That is the most credible confirmation yet that fully dark operation works only in narrow domains. It is not a general default.

Buyers report the same picture. Belitsoft's 2026 enterprise survey finds that the average company runs 12 agents. That number heads to 20 by 2027. About half of those agents work alone, with no coordination. Futurum's first-half-2026 survey shows agentic AI rising as a top priority, from 13.0 to 17.1 percent year over year. The direction is up, but coordinated autonomy is still rare.

## Scenarios as a holdout set

The best new technique comes from StrongDM's Attractor dark factory. Three engineers run it under two hard rules. No human writes code. No human reviews code. Since July 2025 the team shipped about 16,000 lines of Rust, 9,500 of Go, and 6,700 of TypeScript. The design answers the central dark-factory problem: how to trust output that no human reviews.

- **Scenarios, not tests.** Traditional tests live inside the codebase. The agent can see them and game them, so it fits the test instead of the intent. StrongDM moves the standard of truth outside the codebase. A scenario is an end-to-end user story in plain language. StrongDM stores each scenario apart and validates it with an LLM, a large language model. The building agent never sees the scenarios during development.
- **Holdout-set correctness.** StrongDM borrows this idea from machine learning. The team judges correctness only from behavior it can observe from outside. The building agent cannot access those scenarios. Separate the generator from the standard of truth, and over-fitting collapses.
- **Behavioral replicas of dependencies.** The team built accurate fakes of Okta, Jira, Slack, and Google Docs, Drive, and Sheets. Agents test against realistic edge cases at volume. The fakes have no rate limits and no production risk. Any factory whose product calls third-party APIs can reuse this pattern.


GitHub Spec Kit is now past 90,000 stars with more than 30 agent integrations. Its spec-driven command surface is stable. That surface includes a read-only consistency gate, which checks the spec, the plan, and the tasks before any code. Nothing changed structurally this cycle, so the front-end spec layer has settled. The active frontier moved downstream to the verification and holdout layer. That is where StrongDM is working.

## The review bottleneck is now measurable

The evidence now says the constraint is review, not generation:

| Source | Finding | Number |
|---|---|---|
| LinearB (8.1M PRs, 4,800+ orgs) | How much faster developers feel with AI | +20% |
| LinearB | Measured change in actual delivery speed | -19% |
| LinearB | Tasks completed | +21% |
| LinearB | Pull requests merged | +98% |
| LinearB | PR review time | +91% |
| Sonar | Developers who do not fully trust AI output is correct | 96% |
| Sonar | Developers who always check AI output before committing | 48% |
| CodeRabbit | More issues surfaced in AI-written code than human-written | ~1.7x |
| CodeRabbit | Developers who say reviewing AI code takes more effort than a colleague's | 38% |


The LinearB result is a 39-point gap between perception and measurement. More work enters the queue, and less work flows out. Sonar's verification gap means developers distrust the gate and skip it. The evidence supports one operating lesson. The loop runs only as fast as its automated, independent verification. Bolt generation onto a manual review gate and you build a slower team.


Make the gate independent of the builder. Use deterministic pass-fail checks for security and policy. Use behavioral checks for intent. Score the whole trajectory, not just the final diff.

## Other proof points this cycle

- **StrongDM Attractor.** Agents built and tested about 32,000 lines of production code in Rust, Go, and TypeScript. No human wrote or reviewed it over roughly 11 months. Markdown specs and external scenarios governed the work. This is the strongest mechanism proof point of the quarter, next to Salesforce's velocity proof point.
- **Google Antigravity.** Google ships an autonomous platform whose agents plan, execute, and verify across editor, terminal, and browser. This fits Google's standing figure of 75 percent AI-generated, suggested code. The gap holds between 75 percent suggested and DX's roughly 22 percent merged. That gap is the delegation gap, in numbers.
- **Belitsoft and Futurum.** Companies run 12 agents on average, and about half of those agents work alone. Agentic AI priority rose from 13.0 to 17.1 percent year over year.


## Prompt injection, reframed as permanent

The security story moved from incident to structural verdict. OWASP's GenAI Security Project published State of Agentic AI Security and Governance v2.01 on June 11, 2026. The report argues that prompt injection is not a patchable bug. It is architectural. An LLM has no built-in way to separate trusted commands from untrusted data, because both arrive in the same token stream. Prompt injection maps to six of the ten categories in OWASP's Top 10 for Agentic Applications.

The repositories with the most security advisories matter to anyone wiring agents into CI: n8n (57), Claude Code (22), AutoGPT (15), Dify (13), and Roo-Code (11).

A Cloud Security Alliance research note covers the Claude Code GitHub Action attack chain. It shows how little novelty an attacker needs. The attack combined an authorization bypass, an indirect prompt injection, and environment-variable exfiltration. It started with an opened public GitHub issue. It ended with malicious code pushed to the action's own repository.

> **IMPLICATION**
>
> If injection is permanent, the only durable defenses contain it. They do not cure it. Use least-privilege tokens, and keep secrets out of environments the agent can reach. Require human approval on irreversible actions. Add an independent gate that the building agent cannot influence. Plan for the agent to act against you by accident.

## How we apply this at River.io

River.io writes native compiled code with zero third-party dependencies. We use test-driven development and a GitHub-issue-driven SDLC. That posture matches where the credible part of the field is heading.

**The scenario holdout pattern is TDD with a firewall.** StrongDM's move maps onto our testing discipline. Unit tests stay in the repository for the build loop. An out-of-repo scenario set holds plain-language end-to-end behaviors, validated on its own. We keep that set where the building agent never sees it. This is the cleanest way to keep an autonomous loop honest without a human reviewer.

The pattern costs nothing in dependencies. Scenarios are markdown plus a small native validator. We are proving it out on low-stakes repositories: MeowPassword, weathergalactic, and sloth. We define end-to-end behaviors as scenarios stored outside the source tree. A tiny native validator runs them against a built binary and reports pass or fail. We need no third-party test framework.

**Zero third-party dependencies is a security asset, not a style choice.** This cycle's risk material all rides the dependency supply chain. That includes OWASP's permanent flaw verdict, slopsquatting, and hallucinated-dependency vectors. A zero-dependency compiled codebase removes the largest attack surface. An autonomous loop keeps that property with a deterministic gate. The build fails if any import comes from outside the standard library.

**We harden the issue-ingestion path before any autonomy.** The Claude Code GitHub Action attack chain starts with an opened public issue. Our SDLC is issue-driven. We treat every issue, PR, and comment body as untrusted data, never as instructions. Any agent that reads them runs with least-privilege tokens and no secrets in its environment. That guardrail holds however far we push autonomy.

**Regulated work stays human-gated.** CareTime and TimeForCare handle Medicaid electronic visit verification and protected health information. MaterialsAndPractices handles organic-farm compliance. All three run at assisted autonomy, with a human approval gate on every irreversible action. Anthropic's 0-to-20-percent-delegable finding and LinearB's review-bottleneck data agree. Full autonomy pays off only in narrow, well-specified domains with a small blast radius. Regulated work is the opposite, so lights-out experiments stay on throwaway repositories.

---


## Sources

- [Anthropic: 2026 Agentic Coding Trends Report (landing page)](https://resources.anthropic.com/2026-agentic-coding-trends-report)
- [Anthropic: 2026 Agentic Coding Trends Report (PDF)](https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf)
- [NYU Shanghai RITS: summary of Anthropic's 2026 report](https://rits.shanghai.nyu.edu/ai/anthropics-2026-agentic-coding-trends-report-from-assistants-to-agent-teams/)
- [Pathmode: the orchestration era needs intent](https://pathmode.io/blog/orchestration-era-needs-intent)
- [Hivetrail: what Anthropic's 2026 report means for engineering teams](https://hivetrail.com/blog/anthropic-2026-agentic-coding-report/)
- [OWASP via Help Net Security: prompt injection still drives most agentic AI failures (June 11, 2026)](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)
- [TechTimes: prompt injection may be a permanent flaw, not a patchable bug (June 14, 2026)](https://www.techtimes.com/articles/318361/20260614/ai-agent-security-hits-its-reckoning-prompt-injection-may-permanent-flaw-not-patchable-bug.htm)
- [Cloud Security Alliance: Claude Code GitHub Action prompt-injection research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-claude-code-github-action-prompt-injection/)
- [Beam: 5 real AI agent security breaches in 2026 and their lessons](https://beam.ai/agentic-insights/ai-agent-security-breaches-2026-lessons)
- [Sonar: the verification gap, 96% do not fully trust AI output, only 48% verify](https://www.sonarsource.com/company/press-releases/sonar-data-reveals-critical-verification-gap-in-ai-coding/)
- [DEV / Code-Board: code review is the real bottleneck of 2026](https://dev.to/code-board/code-review-is-the-real-bottleneck-of-2026-and-most-teams-dont-see-it-5eed)
- [Aviator: the AI code verification bottleneck](https://www.aviator.co/blog/the-ai-code-verification-bottleneck-why-faster-code-generation-means-slower-reviews/)
- [byteiota: AI code review benchmark 2026, first real results](https://byteiota.com/ai-code-review-benchmark-2026-first-real-results/)
- [StrongDM dark factory: Built by Agents, Tested by Agents, Trusted by Whom? (Stanford CodeX)](https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/)
- [env.dev: AI Dark Factory Playbook, from autocomplete to autonomous](https://env.dev/guides/dark-factory-pattern)
- [aipatternbook: Dark Factory (encyclopedia of agentic coding patterns)](https://aipatternbook.com/dark-factory)
- [Signals/aktagon: Dark Factory architecture, how Level 4 actually works](https://signals.aktagon.com/articles/2026/03/dark-factory-architecture-how-level-4-actually-works/)
- [Signals/aktagon: why most developers are getting slower while AI writes 90% of code](https://signals.aktagon.com/articles/2026/03/the-dark-factory-why-most-developers-are-getting-slower-while-ai-writes-90-of-code/)
- [Forrester: agentic software development takes the lead](https://www.forrester.com/blogs/agentic-software-development-takes-the-lead-from-code-assistants-to-orchestrated-sdlc-agents/)
- [Belitsoft report via Barchart: enterprises run 12 AI agents on average, but half work alone](https://www.barchart.com/story/news/1163379/belitsoft-report-2026-ai-agent-trends-enterprises-run-12-ai-agents-on-average-but-half-work-alone)
- [GitHub: Spec Kit](https://github.com/github/spec-kit)
- [Augment Code: best spec-driven development tools (2026)](https://www.augmentcode.com/tools/best-spec-driven-development-tools)
- [DevOps.com: Google CEO says 75% of new code is AI-generated](https://devops.com/google-ceo-says-75-of-new-code-is-ai-generated/)
- [Tom's Hardware: Microsoft CEO says AI writes up to 30% of its code](https://www.tomshardware.com/tech-industry/artificial-intelligence/microsofts-ceo-reveals-that-ai-writes-up-to-30-percent-of-its-code-some-projects-may-have-all-of-its-code-written-by-ai)
- [BCG Platinion: The Dark Software Factory](https://www.bcgplatinion.com/insights/the-dark-software-factory)


*Vendor and blog figures in this briefing show direction, not audited benchmarks. Some numbers come from a single vendor's or sample's own definition. That includes Anthropic's delegation percentages, the LinearB, Sonar, and CodeRabbit metrics, the StrongDM line counts, and the Google and Microsoft AI-code shares. Treat each one as a signal of direction, not as an independently verified measurement.*


---

Canonical copy: [www.river.io/blog/posts/2026-06-15-the-holdout-set-how-to-trust-code-no-human-reviews.html](https://www.river.io/blog/posts/2026-06-15-the-holdout-set-how-to-trust-code-no-human-reviews.html). Mirrored into this wiki. The river.io blog is the source of truth.
