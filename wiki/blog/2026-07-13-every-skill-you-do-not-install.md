---
title: "Every skill you do not install is an attack you do not have to detect"
date: 2026-07-13
order: 11
tags: "Security, Tooling, Autonomy, Practice"
description: "New research shows that malicious behavior can hide inside agent skills themselves. The attack evades scanners and keeps 96.6% of benign utility. The attack surface has moved from the agent's inputs to its toolbox."
layout: default
---

# Every skill you do not install is an attack you do not have to detect

*Order 011 · 2026-07-13 · 7 min · Security, Tooling, Autonomy, Practice*

> New research shows that malicious behavior can hide inside agent skills themselves. The attack evades scanners and keeps 96.6% of benign utility. The attack surface has moved from the agent's inputs to its toolbox.

In mid-July 2026, the research frontier in agentic-coding security shifted. The headline vulnerabilities of early July, GitLost and GuardFall, were about hostile *content*. Issues, pull requests, and web pages carry hidden instructions to an agent that reads them. The new wave is about hostile *capabilities*.

A paper titled **PhantomSkill** introduces an attack technique the authors call **VulMask** (arXiv 2606.19191). It shows that malicious behavior can hide inside an agent skill's auxiliary scripts. The attacker rewrites that behavior as ordinary-looking "vulnerability-shaped" code. The code fires only on the attacker's trigger. The results are a 58.8% attack success rate and 96.6% of the skill's benign utility preserved. The attack largely evades skill scanners and automated reviewers across major coding agents.

## A class, not a one-off

PhantomSkill did not arrive alone. A companion wave of research confirms that this is a systemic class of attack. Cloak and Detonate covers scanner evasion and dynamic detection. SKILL-INJECT measures agent vulnerability to skill-file attacks. A survey covers supply-chain poisoning across LLM coding-agent skill ecosystems. The class even has its own curated tracker, the awesome-agent-skills-security list.

The core insight is uncomfortable for anyone who relies on marketplace review. Scanners look for malicious *intent* in a skill's description. The attack hides as ordinary *insecure-looking* code in auxiliary files, and activates later. Static scanning of skill text is not a control. Cloak and Detonate argues for dynamic detection instead.

The defensible posture available today is simpler: a minimal skill surface, first-party only. Agent skills and plugins are executable supply chain, not configuration.

> **Also this week: do not trust the screen**
>
> Security researcher Johann Rehberger demonstrated a time-of-check to time-of-use (TOCTOU) attack on computer-use and coding agents. TOCTOU means the state changes between the check and the action. Mutate the UI between the agent's visual check and its click, and the agent approves something it never saw. Any approval flow where an agent verifies visually and then acts is racy by construction. Verify approvals that matter at the API or data layer, atomically. Never verify them from screenshots.

## Measuring autonomy before granting it

On the constructive side, Anthropic published field research on measuring AI agent autonomy in practice. The research draws on how agents are actually deployed on its public API. Software engineering accounts for roughly half of all agentic activity. That makes it the closest thing available to ground truth on how far real deployments run unattended. The practical guidance follows directly. Instrument what agents do without supervision, then set autonomy gates from data rather than optimism.

A new academic framework goes further and formalizes the gating itself. A paper on autonomous CI/CD quality assurance runs a complete quality gate from pull request to defect filing with 14 specialist agents. It is built on LangGraph multi-agent orchestration, from K11tech. It also computes a per-change risk score. It suspends execution to a human whenever that score reaches 0.85 or above.

We would not adopt the stack, which is LangGraph plus seven MCP servers. The pattern is the right abstraction: autonomy as a continuous function of measured risk, not a repository-level on-off switch. It matches the bounded-autonomy framing of the "From Assistance to Agency" work on CI/CD pipelines.

Two smaller signals round out the picture. First, "harness engineering" is now a named discipline with its own curated list, awesome-harness-engineering. It covers evals, memory, permissions, observability, and orchestration. The center of gravity is not the model. It is the harness.

Second, the field now draws a distinction. Personal agents run on markdown files. Production agents need databases, access control, and memory at scale. The gap between a hobby loop and a factory is infrastructure.

Spec-driven tooling also continued to mature. ASSERT turns specs into repeatable evals. Google published its account of automating the eval-optimize loop with independent AutoRaters that grade agent output against custom rubrics. The market for purpose-built eval-gate products is consolidating.

## The proof point that matters

The reference case for production-scale agentic coding remains Spotify's background coding agent, Honk. It merges roughly 650 agent-generated pull requests to production per month, and more than 1,500 in total. Spotify reports 60 to 90 percent time savings on migrations, with a small team running the work. Spotify credits years of prior investment in fleet management, standardized builds, and comprehensive test suites.


The agent is the cheap part. The deterministic test and build substrate is the factory.

The counterweights deserve equal billing. Google's widely cited figure of about 75% AI-generated code, from Sundar Pichai, counts suggested-and-accepted code. That is a much weaker definition than autonomously merged. A survey of software engineering's third era finds that agent pull requests complete fast, half of them within about 13 minutes. Teams accept them at lower rates than human pull requests.

Older randomized controlled trials show the full spread. One found a 26% increase in pull requests per week. Another found no productivity lift and a 41% increase in bug density. Throughput is not merged quality.

## How we apply this at River.io

This research wave lands as vindication of a posture we already hold. It converts that posture from engineering taste into security architecture.

- **Zero dependencies extends to the automation layer.** PhantomSkill's entire attack surface is third-party skills, actions, and MCP servers. River.io ships native compiled code with no third-party libraries. We run our agents the same way: no third-party agent skills, no unpinned marketplace actions, and first-party scripts only. Every capability we do not install is an attack class that does not exist against us.
- **Verification is behavioral, not textual.** GuardFall broke string matching on commands. VulMask breaks static scanning of skill code. The only gate that survives both is running the thing: compile it, execute the full test suite, and diff observable behavior. Our test-driven development discipline makes that gate native. For agent-authored pull requests, the gate is tests-pass plus behavior-diff. Human code review of agent tooling is necessary, but on its own it is demonstrably not enough.
- **Regulated repositories are permanently pinned above the risk threshold.** CareTime and TimeForCare handle Medicaid EVV work and are PHI-adjacent. MaterialsAndPractices handles organic compliance. For all three, the risk-proportionate gate never opens. Agents may draft. Humans author every compliance-defining assertion and approve every merge. Agents hold no read access to these repositories at all.
- **Risk-scored autonomy on low-stakes repositories.** On MeowPassword, weathergalactic, and sloth, we run a dependency-free version of the risk-proportionate pattern. We score each agent task on factors such as whether it touches authentication or persistence, diff size, and new files. We auto-suspend to a human above a threshold. We add label-gated issue intake, injection red-teaming, and a log of corrective interventions per task. Together those give us a measurable, per-repository case for loosening gates.
- **Pour the concrete before you install the robots.** Spotify's throughput was possible because its builds and tests were already deterministic and comprehensive. Our equivalent groundwork is simple. Every repository that will ever host an autonomous loop gets a complete, fast, native test suite first. Test coverage is the factory floor.
- **No screenshot-verified approvals, ever.** An agent may one day drive a UI for us, for App Store screenshot automation or device testing. In that case we verify state via API or filesystem, atomically with the action. Rehberger's TOCTOU result makes look-then-click approval unsafe by design.


---


## Sources

- [arXiv: PhantomSkill, malicious code injection in agent skill ecosystems](https://arxiv.org/abs/2606.19191)
- [arXiv: Cloak and Detonate, scanner evasion and dynamic detection of agent skill malware](https://arxiv.org/html/2607.02357)
- [arXiv: SKILL-INJECT, measuring agent vulnerability to skill file attacks](https://arxiv.org/pdf/2602.20156)
- [arXiv: Supply-chain poisoning attacks against LLM coding agent skill ecosystems](https://arxiv.org/html/2604.03081v1)
- [GitHub: awesome-agent-skills-security (LLMSecurity)](https://github.com/LLMSecurity/awesome-agent-skills-security)
- [Adversa AI: Top AI coding agent security resources, July 2026](https://adversa.ai/blog/top-ai-coding-agent-security-resources-july-2026/)
- [Anthropic: Measuring AI agent autonomy in practice](https://www.anthropic.com/research/measuring-agent-autonomy)
- [ResearchGate: Autonomous CI/CD QA using LangGraph multi-agent orchestration and risk-proportionate HITL control](https://www.researchgate.net/publication/408277480_Autonomous_CICD_Quality_Assurance_Using_LangGraph_Multi-Agent_Orchestration_and_Risk-Proportionate_Human-in-the-Loop_Control)
- [arXiv: From Assistance to Agency, rethinking autonomy and control in CI/CD pipelines](https://arxiv.org/html/2605.07062)
- [GitHub: awesome-harness-engineering (ai-boost)](https://github.com/ai-boost/awesome-harness-engineering)
- [Spotify Engineering: Coding is no longer the constraint (June 2026)](https://engineering.atspotify.com/2026/6/code-with-claude-coding-is-no-longer-the-constraint) · [Spotify Engineering: 1,500+ PRs later, Honk, part 1](https://engineering.atspotify.com/2025/11/spotifys-background-coding-agent-part-1) · [Claude: Spotify Claude Agent SDK case study](https://claude.com/customers/spotify)
- [Metaintro: Google's 75% AI code milestone](https://www.metaintro.com/blog/google-75-percent-ai-generated-code-software-engineer-jobs-2026)
- [arXiv: The rise of AI teammates in SE 3.0](https://arxiv.org/html/2507.15003v1)
- [GitHub Spec Kit releases](https://github.com/github/spec-kit/releases) · [Spec Kit docs](https://github.github.com/spec-kit/)
- [Confident AI: Best CI/CD tools for testing AI agents before production, 2026](https://www.confident-ai.com/knowledge-base/compare/best-ci-cd-tools-testing-ai-agents-before-production-2026)
- [Help Net Security: Prompt injection still drives most agentic AI security failures](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)
- [GitHub dark-factory topic](https://github.com/topics/dark-factory) · [darkfactory.dev](https://darkfactory.dev/) · [BCG Platinion: The dark software factory](https://www.bcgplatinion.com/insights/the-dark-software-factory) · [iTmethods: Governed autonomous SDLC](https://itmethods.com/dark-factory) · [MindStudio: Dark factory AI agent](https://www.mindstudio.ai/blog/what-is-a-dark-factory-ai-agent) · [i-SCOOP: Dark software factories](https://www.i-scoop.eu/dark-software-factories-and-the-future-of-autonomous-software-delivery/)


*Vendor and blog figures cited here show direction, not audited benchmarks.*


---

Canonical copy: [www.river.io/blog/posts/2026-07-13-every-skill-you-do-not-install.html](https://www.river.io/blog/posts/2026-07-13-every-skill-you-do-not-install.html). Mirrored into this wiki. The river.io blog is the source of truth.
