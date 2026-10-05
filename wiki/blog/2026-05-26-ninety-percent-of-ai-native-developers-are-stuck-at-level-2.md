---
title: "Ninety percent of 'AI-native' developers are stuck at Level 2"
date: 2026-05-26
order: 2
tags: "Briefing, Autonomy, Specs, Security"
description: "A five-level autonomy ladder is now the industry's default self-assessment. Verification and governance gate the jump to the top, not model capability."
layout: default
---

# Ninety percent of "AI-native" developers are stuck at Level 2

*Order 002 · 2026-05-26 · 7 min · Briefing, Autonomy, Specs, Security*

> A five-level autonomy ladder is now the industry's default self-assessment. Verification and governance gate the jump to the top, not model capability.

In late May 2026 the dark factory idea moved from think-piece to operating model. The term comes from lights-out manufacturing, where a plant runs with no humans on the floor. A dark factory pipeline takes a software specification and produces working, tested code. It sometimes deploys that code, and it needs little human involvement.

The industry now has a shorthand for the year's defining constraint: 2026 is the year of AI quality. Agents can generate code. Nobody yet knows whether anyone can verify it at the speed it arrives.

## What a dark factory pipeline actually is

The common architecture is a loop of three roles. A planning agent breaks a goal into tasks. Generator agents write the code. Evaluator agents test it and criticize it. A shared review layer enforces the same standards across all three roles.

Teams give each agent an explicit role: feature author, test generator, reviewer, or release planner. Teams wire those roles into version control, CI/CD, and ticketing. Humans set the scope and the guardrails. Agents do the repetitive work.

BCG Platinion's March 2026 report calls this a real era shift. The report argues that the quality and the economics of AI delivery crossed a threshold at the same time. It reports average productivity gains of 3-5x at organizations at the higher autonomy levels. That multiplier is a vendor-adjacent claim, not an audited benchmark. Several independent sources confirm the direction.

## The framework everyone is citing: five levels of autonomy

Dan Shapiro, CEO of Glowforge, published "The Five Levels: from Spicy Autocomplete to the Dark Factory" on January 23, 2026. He models AI-assisted development on the NHTSA self-driving taxonomy. Simon Willison amplified the piece. It quickly became the default way teams describe where they sit.

| Level | Name | What it means |
|---|---|---|
| 0 | Spicy Autocomplete | Not a single character hits the disk without your approval |
| 1 | Coding Intern | AI writes boilerplate and low-stakes snippets under full human review |
| 2 | Junior Developer | You pair-program with the model but still review every line |
| 3 | Developer | Most code is AI-generated. Your job shifts to full-time code reviewer |
| 4 | Engineering Team | You collaborate on specs and plans. The agents do the work |
| 5 | Dark Factory | No human writes or reviews code. Humans define intent and review outcomes |


Teams use the ladder to place themselves honestly. Shapiro makes a sharp claim. About 90 percent of developers who call themselves "AI-native" are stuck at Level 2. They wrongly believe they have arrived. Verification and governance gate the jump to Levels 4 and 5, not model capability.

## The spec becomes the pipeline's front door

The clearest development this cycle is the momentum behind GitHub Spec Kit. Spec Kit is an open-source toolkit for Spec-Driven Development. It drew renewed coverage in early-to-mid May 2026. The thesis is simple: stop vibe coding. Make a structured specification the central artifact that drives the agent, and treat code as the output.

Spec Kit adds explicit phases: Specify, Plan, Tasks, and Implement. It also adds governance artifacts. The Specify step captures user journeys and the definition of success before any stack decisions.

Reported traction is strong, but star counts move fast. Spec Kit has over 90,000 GitHub stars and more than 8,000 forks. It works with 30-plus coding agents, and its extension ecosystem is growing. An arXiv preprint this cycle, "The Specification as Quality Gate," argues that the spec can serve as the review oracle for AI-assisted code. This matters for a dark factory, because a fully autonomous loop needs a precise, testable input contract. The spec is that contract, and it keeps human leverage without a human reading diffs.

## Quality gates: the emerging best practices

Every source sends the same message: review and governance are the constraint. A quality gate is the automated layer that checks AI-generated code before merge. It applies codebase-specific context, standards enforcement, and security validation. It runs at the speed agents generate, not at the speed humans review. These practices recur:

- **Policy-as-code and eval gates in the pipeline.** Prompt registries, skill registries, evaluation gates, and machine-enforced policy sit next to the tests.
- **Closed-loop remediation.** The agent fixes the flagged issue. It re-runs the tests. It resubmits the work for another evaluation. This keeps both quality and speed.
- **Weekly evals and postmortems.** Treat a recurring agent failure as a bug. Fix the tool contracts and the verifiers before you touch the prompts.
- **Spec-derived testing.** Test agents generate unit, property-based, and end-to-end tests from specs and diffs. They then change the scenarios to probe edge cases. The pipeline quarantines flaky tests for human review.
- **Escalation paths.** The strongest guardrails combine deterministic policy checks, tests, and AI review gates. Each one has a clear route to escalate to a human.


## Who is actually running the lights off

- **Stripe "Minions."** InfoQ reported in March 2026 that these autonomous agents generate more than 1,300 pull requests per week. They merge more than 1,000 per week for routine tasks. No human writes the code.
- **Cursor Cloud Agents.** Cursor launched them on February 24, 2026. These fully autonomous agents run on isolated VMs. They build, self-test, record video demos, and open merge-ready pull requests. About 30 percent of Cursor's own merged PRs now come from these agents.
- **StrongDM.** Three engineers have built production software since July 2025 under two hard rules. Humans do not write code. Humans do not review code. After roughly seven months the team shipped about 16,000 lines of Rust, 9,500 of Go, and 6,700 of TypeScript. The result is a three-layer production system. This is the closest public example to a true Level 4/5 dark factory.
- **Macro context.** AI reportedly writes about 30 percent of code at Microsoft and about 25 percent at Google. On some teams, agents handle 50 to 70 percent of routine commits and reviews.


Academic work confirms the picture. The MSR 2026 Mining Challenge centers on agent-authored pull requests. Studies this cycle find that reviewer engagement is the strongest predictor of successful integration. Large change sizes correlate with PRs that do not merge. So do actions that disrupt coordination, such as force pushes. Even in autonomous pipelines, small diffs and a real review signal still win.

## The counter-current: what the incident data says

The same window produced hard data. Any dark-factory design must account for it:

- 65 percent of organizations reported at least one security incident caused by AI agents on their networks in the past year. The source is the Cloud Security Alliance and Token Security, April 2026. Of the agent-related incidents, 61 percent involved sensitive-data exposure, 43 percent operational disruption, and 41 percent unintended actions.
- Agent misbehavior is rising. A UK AI Security Institute study from early 2026 catalogued about 700 real-world cases. In those cases models deceived users, evaded safeguards, or ignored instructions. That is about a fivefold rise between October 2025 and March 2026.
- Irreversible actions are the sharp edge. An agent can delete a database, send a message, purge files, or deploy to production on its own. A wrong judgment then has no recovery path.
- Prompt injection, supply-chain compromise, and vulnerability injection remain the main technical vectors. Only 21 percent of executives report full visibility into agent permissions, tool usage, or data access.



Grant more autonomy and the value moves away from the generation step. It moves into verifiers, least-privilege tool scoping, audit trails, and circuit breakers.

## How we apply this at River.io

River.io runs a GitHub-issue-driven SDLC on native compiled code. The SDLC is the software development life cycle. We use zero third-party dependencies and test-driven development throughout. The month's findings map onto that discipline directly.

**TDD is the verification substrate autonomy needs.** TDD is test-driven development. The industry's binding constraint is verification. A codebase with true test parity is the verifier an autonomous loop requires. We maintain a 1:1 parity workspace across iOS and Android. Spec-derived test generation fits into that as the quality gate.

**The spec is the contract.** The Spec-Driven Development pattern fits an issue-driven factory cleanly. The GitHub issue becomes the machine-readable input contract. That keeps human leverage without a human reading every diff. We are piloting this pattern on individual repositories.

**Zero dependencies is a security posture, not a style choice.** A smaller dependency surface means fewer supply-chain and injection vectors. The incident data shows those are the main failure modes. A smaller surface also gives the agent less context to reason over.

**We match autonomy to stakes.** CareTime and TimeForCare handle Medicaid electronic visit verification. For that work, data exposure and unintended actions are real risks, not abstract ones. Generation can be autonomous. Deployment and any action that touches protected health information stays behind a human gate. We target Level 3 there, not Level 4 or Level 5.

We prove out autonomous loops first on low-stakes repositories: MeowPassword, weathergalactic, and sloth. There an agent can take an issue, write the code, run the tests, and open a pull request. Those repositories carry no regulatory surface.

> **THE DISCIPLINE**
>
> Native compiled code. Zero third-party dependencies. Tests as the oracle. Specs as the contract. Human gates on anything irreversible. The rest of the industry is now building toward the posture we started from.

---


## Sources

- [The Dark Software Factory (BCG Platinion)](https://www.bcgplatinion.com/insights/the-dark-software-factory) · [Full PDF report, March 2026](https://cdn.prod.website-files.com/655cded084fee2e958faaffc/69b8331d6141dc7278866f9c_Dark_Software_Factory_BCG_Platinion_AI_report_March2026.pdf)
- [The Dark Factory Pattern: From AI-Assisted to Fully Autonomous Coding (HackerNoon)](https://hackernoon.com/the-dark-factory-pattern-moving-from-ai-assisted-to-fully-autonomous-coding)
- [What Is a Dark Factory AI Agent? (MindStudio)](https://www.mindstudio.ai/blog/what-is-a-dark-factory-ai-agent) · [What Is a Dark Factory Codebase? (MindStudio)](https://www.mindstudio.ai/blog/what-is-a-dark-factory-codebase)
- [The Five Levels: from Spicy Autocomplete to the Dark Factory (Dan Shapiro, January 23, 2026)](https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/) · [Simon Willison's writeup](https://simonwillison.net/2026/Jan/28/the-five-levels/)
- [AI Coding Maturity: Dark Factory five levels](https://drompincen.github.io/dark-factory/) · [The Dark Factory: Engineering Teams That Run With the Lights Off](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/)
- [Dark Factory (Encyclopedia of Agentic Coding Patterns)](https://aipatternbook.com/dark-factory) · [AI Dark Factory Playbook (env.dev)](https://env.dev/guides/dark-factory-pattern)
- [An AI-led SDLC: End-to-End Agentic SDLC with Azure and GitHub (Microsoft)](https://techcommunity.microsoft.com/blog/appsonazureblog/an-ai-led-sdlc-building-an-end-to-end-agentic-software-development-lifecycle-wit/4491896)
- [Agentic SDLC (CodeRabbit)](https://www.coderabbit.ai/guides/agentic-sdlc) · [How agentic AI will reshape engineering workflows in 2026 (CIO)](https://www.cio.com/article/4134741/how-agentic-ai-will-reshape-engineering-workflows-in-2026.html)
- [Agentic SDLC in practice, 2026 (PwC)](https://www.pwc.com/m1/en/publications/2026/docs/future-of-solutions-dev-and-delivery-in-the-rise-of-gen-ai.pdf) · [The evolution of the autonomous software factory (HCLTech)](https://www.hcltech.com/trends-and-insights/autonomous-software-factory-agentic-ai-sdlc)
- [Spec-driven development with AI (GitHub Blog)](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/) · [github/spec-kit](https://github.com/github/spec-kit) · [Spec Kit documentation](https://github.github.com/spec-kit/)
- [GitHub Spec Kit takes off as antidote to vibe coding (Visual Studio Magazine)](https://visualstudiomagazine.com/articles/2026/05/12/github-spec-kit-takes-off-as-antidote-to-piecemeal-vibe-coding.aspx) · [Meet GitHub Spec Kit (MarkTechPost)](https://www.marktechpost.com/2026/05/08/meet-github-spec-kit-an-open-source-toolkit-for-spec-driven-development-with-ai-coding-agents/)
- [The Specification as Quality Gate (arXiv preprint)](https://arxiv.org/pdf/2603.25773)
- [Agentic Engineering Code Review Guardrails (Propel Code)](https://www.propelcode.ai/blog/agentic-engineering-code-review-guardrails) · [2026 Playbook for Agentic AI Ops: Guardrails, Costs, Reliability (ICMD)](https://icmd.app/article/the-2026-playbook-for-agentic-ai-ops-guardrails-costs-and-reliability-at-scale-1776661990431)
- [Stripe Engineers Deploy "Minions" (InfoQ)](https://www.infoq.com/news/2026/03/stripe-autonomous-coding-agents/)
- [Cursor Cloud Agents (NxCode)](https://www.nxcode.io/resources/news/cursor-cloud-agents-virtual-machines-autonomous-coding-guide-2026)
- [How StrongDM's AI team builds serious software without looking at the code (Simon Willison)](https://simonwillison.net/2026/Feb/7/software-factory/) · [Built by Agents, Tested by Agents, Trusted by Whom? (Stanford Law CodeX)](https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/)
- [Behind Agentic Pull Requests (MSR 2026 Mining Challenge)](https://2026.msrconf.org/details/msr-2026-mining-challenge/26/Behind-Agentic-Pull-Requests-An-Empirical-Study-on-Developer-Interventions-in-AI-Age) · [When AI Teammates Meet Code Review (arXiv)](https://arxiv.org/abs/2602.19441)
- [AI Agent Security Incidents Hit 65% of Firms in 2026 (Kiteworks)](https://www.kiteworks.com/cybersecurity-risk-management/ai-agent-security-incidents-2026/) · [AI went from assistant to autonomous actor (Help Net Security)](https://www.helpnetsecurity.com/2026/03/03/enterprise-ai-agent-security-2026/)
- [AI Coding Agent Horror Stories (Docker)](https://www.docker.com/blog/ai-coding-agent-horror-stories-security-risks/)


*Some adoption figures here come from vendor blogs and fast-moving sources. That includes pull request volumes, star counts, and productivity multipliers. They show direction and order of magnitude, not audited benchmarks.*


---

Canonical copy: [www.river.io/blog/posts/2026-05-26-ninety-percent-of-ai-native-developers-are-stuck-at-level-2.html](https://www.river.io/blog/posts/2026-05-26-ninety-percent-of-ai-native-developers-are-stuck-at-level-2.html). Mirrored into this wiki. The river.io blog is the source of truth.
