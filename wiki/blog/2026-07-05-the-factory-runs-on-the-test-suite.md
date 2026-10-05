---
title: "The factory runs on the test suite, not the model"
date: 2026-07-05
order: 8
tags: "Briefing, Autonomy, Tooling, Security"
description: "Spotify's Honk agent merges about 650 pull requests to production every month. The detail that matters is what came first. Years of platform and test investment made that possible."
layout: default
---

# The factory runs on the test suite, not the model

*Order 008 · 2026-07-05 · 8 min · Briefing, Autonomy, Tooling, Security*

> Spotify's Honk agent merges about 650 pull requests to production every month. The detail that matters is what came first. Years of platform and test investment made that possible.

In early July 2026, autonomous software production got its most concrete large-scale case study yet. Spotify's "Honk" agent runs on Claude Code. It now merges roughly 650 agent-generated pull requests to production per month. A QCon London 2026 figure puts continuous codebase-wide migration work at roughly 1,000 merged pull requests every 10 days. That work covers more than 20 million lines of code.

The catch is buried in Spotify's own telling. Honk only works because of years of prior infrastructure investment. Fleet Management since 2022, Backstage, standardized builds, and comprehensive test suites came first. The factory runs on the test suite, not the model. That is the single most transferable lesson of the cycle.

## What Spotify actually built

Spotify has displaced StrongDM as the most-cited real-world autonomous factory at scale. Its engineering organization reports large migrations run at roughly 90 percent time savings. Co-CEO Gustav Söderström said on the Q4 2025 earnings call that some teams "haven't written a line of code since December." That last line is an earnings-call claim, so read it as directional.

The under-quoted part is the architecture. A developer issues a request in Slack. The Honk agent picks it up. Fleet Management provides the standardized surface to operate on. A verification loop built on MCP tools checks the work. The output is an automated pull request.

The merge gate is an executable check, not a human glance. Spotify is explicit that the whole pipeline rests on infrastructure built since 2022 plus deep test coverage. Spotify earned autonomy through platform and test investment. It did not buy autonomy with a model subscription.


The dark factory is downstream of the test suite and the platform. It is not a model you drop in.

## Context files got their first honest evals

The second thread of the cycle qualified a piece of consensus advice. AGENTS.md has become a genuine cross-tool standard. Claude Code, GitHub Copilot's coding agent, and OpenAI Codex all recognize it. But new evidence weakens the "just write good context files" guidance:

- An "Evaluating AGENTS.md" analysis found that context files can **reduce** agent success compared with no context at all. They also add more than 20 percent inference cost. Unnecessary requirements make tasks harder.
- Vercel's internal evals cut the other way. Documentation embedded directly in AGENTS.md hit 100 percent pass rates on build, lint, and test checks. That content is always in the system prompt rather than progressively disclosed.
- Practitioner consensus now puts a hard cap at roughly 150 to 200 standing instructions before reliability degrades. Keep the file lean, and structure it around what, why, and how. Disclose anything beyond that progressively.


Reconciled: context files still help, but comprehensiveness is a failure mode. A tight, load-bearing instruction file beats a kitchen-sink one. It beats it by more than most teams assumed.

## Tooling kept hardening

GitHub Spec Kit passed 78,000 stars. Its core pipeline is Spec, Plan, Tasks, Implement. A read-only analyze gate cross-validates the project constitution, spec, plan, and tasks before any code is written. It looks for ambiguities, coverage gaps, and contradictions. An ecosystem of more than 70 extensions adds security, drift, and compliance gates, including CI Guard and Architecture Guard. For regulated work, presets can restructure spec templates to require regulatory traceability and enforce mandatory security-review and test-first gates.

Agent identity is also becoming a control plane. NIST's COSAiS project is building control overlays for single-agent and multi-agent use cases. It published a concept paper on agent identity in February 2026. Delegation, identity, and continuous monitoring are moving from nice-to-have to operational requirement.

## The numbers in circulation

| Organization | Reported figure |
|---|---|
| Spotify | ~650 agent PRs merged per month; ~90% time savings on migrations; ~1,000 merged PRs per 10 days for continuous migration; 20M+ lines under Claude Code |
| StrongDM | ~32,000 lines of production code by 3 people, no hand-written or hand-reviewed code |
| Cursor | ~35% of internally merged PRs agent-created; enterprise page claims 64% of the Fortune 500 use it and 100M+ lines per day written with it |
| Microsoft | 20–30% AI-authored (traces to 2024 and early 2025 statements being re-quoted) |
| Google | ~25–30% AI-authored (same caveat) |
| Broad tech sector | ~25–30% of new production code AI-written (estimate) |


## Security did not improve

One item cuts straight at the autonomous-merge ambition. A single prompt injection reportedly leaked secrets from Claude Code, Gemini CLI, and Copilot at the same time. The shared-tool, shared-pattern attack surface is real, and it crosses vendors.

Coding agents remain the primary target. OWASP's State of AI Surveyor finds 28 of 53 tracked agentic projects are coding agents. It cites prompt injection at 340 percent growth year over year. Adaptive attacks succeed against state-of-the-art defenses more than 85 percent of the time. A new arXiv study (2601.17548) maps prompt-injection vulnerabilities across the skills, tools, and MCP protocol surfaces of agentic coding assistants. An autonomous factory wires exactly those surfaces together.

The supply-chain precedent stays fresh. The March 2026 LiteLLM PyPI backdoor remains the cautionary tale for dependency-heavy agent stacks. Attackers harvested a publishing token, and the backdoor collected roughly 47,000 downloads in a three-hour window. LiteLLM sits under CrewAI, DSPy, GraphRAG, and other frameworks. An arXiv paper this cycle (2605.07062) argues CI/CD needs rethought control primitives as agents move from assistance to agency. Approval, reversibility, and blast-radius limits must be design constraints, not afterthoughts.

> **THE TRANSFERABLE SKELETON**
>
> Strip the branding, and Honk's shape is the same loop StrongDM and the research literature describe: request, plan, generate, verification loop against real tests, pull request. Any shop with a trustworthy test suite and a CI gate can run a scaled-down version. Any shop without one cannot, at any price.

## How we apply this at River.io

Our posture is native compiled code, zero third-party dependencies, test-driven development, and a GitHub-issue-driven SDLC. This cycle's credible findings line up with it. This cycle's dangers mostly do not reach it.

**Spotify's real lesson is TDD, not "buy a model."** Honk works because comprehensive test suites and a standardized build platform came first. That is our existing discipline. Our path to a working autonomous loop leans on test coverage as the merge gate. The model converges against our tests, native and dependency-free. We do not need Backstage. We need green tests and a CI gate, and we build both.

**We keep context files lean, because the evidence says bloat hurts.** Past roughly 150 to 200 instructions, agent success drops and cost rises more than 20 percent. Irrelevant content has the same effect. We audit our repository context documents down to invariants and validation steps. A lean AGENTS.md is attractive because it is cross-tool and adds zero dependencies.

**Regulated work stays human-gated.** The one-injection-three-agents report and the systematic vulnerability mapping reinforce the policy. Our CareTime and TimeForCare Medicaid EVV applications run human-in-the-loop. So does our MaterialsAndPractices organic-farm compliance application. Agents draft, and humans review and attest. Spec tooling on those repositories requires regulatory traceability and a mandatory security-review gate.

**Loop experiments run on the low-stakes repositories, copying Honk's shape.** MeowPassword, weathergalactic, and sloth are the sandboxes. There we replicate the transferable skeleton: issue, plan, generate, verification loop against our tests, pull request. The merge gate is a test-pass threshold, native and dependency-free. We instrument the loop and capture token cost, agent-authored pull request rate, and test pass rate. We then accumulate our own numbers instead of citing vendors.

**The supply-chain risks stay someone else's problem.** The LiteLLM backdoor and the framework RCE disclosures are attacks on dependency trees. Our zero-dependency native stack has a fraction of that blast radius. No autonomous-loop convenience may quietly pull in a package manager or a heavyweight agent framework. CrewAI, DSPy, and LangGraph all sit on the dependency chains that got backdoored.

---


## Sources

- [Spotify Engineering: Coding Is No Longer the Constraint (June 2026)](https://engineering.atspotify.com/2026/6/code-with-claude-coding-is-no-longer-the-constraint) · [InfoQ: QCon London 2026, Rewriting All of Spotify's Code Base, All the Time](https://www.infoq.com/news/2026/03/spotify-honk-rewrite/) · [The Neuron: How Spotify runs Claude across 20M+ lines of code](https://www.theneuron.ai/newsletter/how-spotify-runs-claude-across-20m-lines-of-code/)
- [DEV: How Spotify Automated Background Engineering with AI](https://dev.to/jcorral/how-spotify-automated-background-engineering-with-ai-5ep9) · [EveryDev: Spotify Built an AI Coding Agent (Honk)](https://www.everydev.ai/p/blog-spotify-built-an-ai-coding-agent-honk) · [Medium/CodeToDeploy: How Spotify Built an AI Coding Agent That Merged 1,500+ PRs](https://medium.com/codetodeploy/how-spotify-built-an-ai-coding-agent-that-merged-1-500-prs-6e913b9b4ca5)
- [MindStudio: What Is a Dark Factory?](https://www.mindstudio.ai/blog/what-is-dark-factory-autonomous-ai-codebase) · [BCG Platinion: The Dark Software Factory](https://www.bcgplatinion.com/insights/the-dark-software-factory)
- [GitHub: Spec Kit repo](https://github.com/github/spec-kit) · [Microsoft for Developers: Spec-Driven Development with Spec Kit](https://developer.microsoft.com/blog/spec-driven-development-spec-kit) · [MarkTechPost: Meet GitHub Spec-Kit](https://www.marktechpost.com/2026/05/08/meet-github-spec-kit-an-open-source-toolkit-for-spec-driven-development-with-ai-coding-agents/)
- [OpenAI Codex: Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md) · [Augment Code: How to write good AGENTS.md files](https://www.augmentcode.com/blog/how-to-write-good-agents-dot-md-files)
- [Blake Niemyjski: Agentic Driven Development, AGENTS.md, Skills, and the Full Workflow](https://blakeniemyjski.com/blog/agentic-driven-development/) · [Addy Osmani: How to write a good spec for AI agents](https://addyosmani.com/blog/good-spec/)
- [DronaHQ: Agentic SDLC in 2026 (NIST COSAiS and agent identity)](https://www.dronahq.com/agentic-sdlc-guide/) · [Augment Code: Agentic SDLC guide](https://www.augmentcode.com/guides/agentic-sdlc)
- [Simon Willison: The Software Factory (StrongDM)](https://simonwillison.net/2026/Feb/7/software-factory/)
- [getPanto: Cursor AI Statistics 2026](https://www.getpanto.ai/blog/cursor-ai-statistics) · [Second Talent: How Much Software Is Written by AI in 2026](https://www.secondtalent.com/resources/how-much-software-written-by-ai/)
- [Tom's Hardware: Microsoft CEO on AI-written code](https://www.tomshardware.com/tech-industry/artificial-intelligence/microsofts-ceo-reveals-that-ai-writes-up-to-30-percent-of-its-code-some-projects-may-have-all-of-its-code-written-by-ai) · [iDiallo: Is 30% of Microsoft's Code Really AI-Generated?](https://idiallo.com/blog/is-30-percent-of-microsoft-code-ai-generated)
- [VentureBeat: Three AI coding agents leaked secrets through a single prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Help Net Security: Prompt injection still drives most agentic AI security failures](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/) · [Tech Times: Prompt Injection May Be a Permanent Flaw](https://www.techtimes.com/articles/318361/20260614/ai-agent-security-hits-its-reckoning-prompt-injection-may-permanent-flaw-not-patchable-bug.htm)
- [arXiv 2601.17548: Prompt Injection Attacks on Agentic Coding Assistants](https://arxiv.org/html/2601.17548v1)
- [beam.ai: 5 Real AI Agent Security Breaches in 2026 (LiteLLM/PyPI)](https://beam.ai/agentic-insights/ai-agent-security-breaches-2026-lessons)
- [arXiv 2605.07062: From Assistance to Agency, Autonomy and Control in CI/CD Pipelines](https://arxiv.org/pdf/2605.07062)


*Vendor and blog figures cited here show direction, not audited benchmarks. This includes Spotify pull request counts, the "no code since December" line, and the Cursor, Microsoft, and Google percentages. Where a statistic traces to an earnings call or a marketing page, the text flags it.*


---

Canonical copy: [www.river.io/blog/posts/2026-07-05-the-factory-runs-on-the-test-suite.html](https://www.river.io/blog/posts/2026-07-05-the-factory-runs-on-the-test-suite.html). Mirrored into this wiki. The river.io blog is the source of truth.
