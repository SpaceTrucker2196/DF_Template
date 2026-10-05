---
title: "Review capacity is the new ceiling for AI-written code"
date: 2026-07-27
order: 13
tags: "Metrics, Briefing, Security, Practice"
description: "Benchmark data from 8.1 million pull requests shows AI-assisted code merges at less than half the human rate. It also waits 4.6 times longer for review. Generation is now cheap. Verification is not."
layout: default
---

# Review capacity is the new ceiling for AI-written code

*Order 013 · 2026-07-27 · 8 min · Metrics, Briefing, Security, Practice*

> Benchmark data from 8.1 million pull requests shows AI-assisted code merges at less than half the human rate. It also waits 4.6 times longer for review. Generation is now cheap. Verification is not.

In late July 2026, the best data on autonomous software delivery points at one constraint. The constraint is not model capability. It is not specification quality. It is review capacity. LinearB measured 8.1 million pull requests across 4,800 organizations for its 2026 Benchmarks.

AI-assisted pull requests merge at 32.7 percent. Human-authored code merges at 84.4 percent. AI-assisted pull requests also wait 4.6 times longer for a first reviewer. The industry made generation industrial. It did not make sign-off industrial.

## The numbers

| Metric | AI-assisted | Human | Source |
|---|---|---|---|
| PR acceptance rate | 32.7% | 84.4% | LinearB 2026 Benchmarks (8.1M PRs, 4,800 orgs) |
| PRs needed per merge | 3.06 | 1.18 | LinearB |
| Wait for first reviewer | 4.6x longer | baseline | LinearB |
| PR size | ~2.6x larger | baseline | LinearB and secondary coverage |


Two academic studies of agentic pull requests agree. An analysis of the AIDev dataset (arXiv 2606.13468) found that reviewers reject about 46.4 percent of the fixes that agents propose. The agents studied were Copilot, Devin, Cursor and Claude. A second empirical study (arXiv 2605.22534) found that only 15.4 percent of merged agentic pull requests had explicit reviewer participation. Copilot and Devin pull requests get far more reviewer attention than Codex and Cursor pull requests, which usually merge with little interaction.

Read the two studies together. Much agent code merges without examination. The examined part fails often.

The production numbers are no better. Lightrun's 2026 survey reports that 43 percent of AI-generated changes needed manual debugging in production after they passed QA and staging. Zero percent of the surveyed engineering leaders said they were "very confident" that AI code would behave correctly once deployed. This is a vendor survey. Treat it as direction, not as an audit.

Throughput keeps rising at the same time. Developers who use AI merge about 98 percent more pull requests. Pull request review time has risen 91 percent. About 18 percent of merged pull requests in surveyed enterprises now name a coding agent as primary author or pair-coder. Google reported in April 2026 that about 75 percent of its new code is AI-generated and engineer-approved.

Three reference points still hold. Stripe runs about 1,300 agent pull requests per week, and a human reviews every change. StrongDM operates a three-engineer factory with no review. DX's preliminary Q2 figure puts AI-authored code at about 52 percent.


Generation got cheaper. Verification did not. That gap is the whole story.

## The state of play

The July 16 model wave is now the baseline. OpenAI shipped GPT-5.5-pro and GPT-5.3-codex. Anthropic shipped Claude Opus 4.7 and Claude Sonnet 4.6. Google shipped the Gemini 3.1 Pro preview. All three shipped coding-agent upgrades in the same window. Repository-wide context and multi-step tool use are now standard.

The framing has moved to persistent, long-horizon agents. Teams orchestrate these agents like junior engineers. GPT-5.5 leads on Terminal-Bench 2.0, which measures running tests, reading failures and iterating without supervision. That is the inner loop of any autonomous factory. These are vendor and aggregator comparisons, so read the leaderboard claims as directional.

The first serious non-US factory stack has also arrived. On July 24, Huawei Cloud launched the CodeArts Agent open beta in Thailand. Huawei Cloud built it on Specification-Driven Development. Its "Agent Team" mode forms a multi-agent development team that runs tasks concurrently. Spec-driven development now ships as a product primitive, not as a methodology essay.

The commercial framing has settled too. iTmethods now markets a "Dark Factory" offering as a governed autonomous SDLC. Nobody sells lights-out. Everybody sells governed lights-out.

## Frameworks and specs

- **Pipeline-native agents.** Older designs bolt an agent onto CI as a post-processing step. New frameworks put agent reasoning inside the pipeline stages instead. Cicaddy (Red Hat, 2026) connects LLM reasoning and MCP tool access straight to CI stages. Related arXiv work ("From Assistance to Agency: Rethinking Autonomy and Control in CI/CD Pipelines") sets autonomy levels per pipeline stage, not per agent.
- **A full-autonomy reference design.** Composio AO runs several agents in isolated git worktrees. Each agent fixes its own CI failures, answers review comments, and manages its own pull request lifecycle without per-edit approval. The part you can copy is the isolation boundary: a worktree, plus CI as the only authority.
- **Testing the agents themselves** is now a separate layer. The FastAgency Tester class defines simulated agent-interaction scenarios. It runs them in CI to catch agent regressions, not only code regressions.
- **SDD consolidation continues.** SDD means specification-driven development. Every major vendor now ships a flavor: Spec Kit, Kiro, OpenSpec, BMAD, Tessl, Antigravity, and now CodeArts. Early adopters report 3x to 10x higher first-pass success on non-trivial tasks. Many people repeat those numbers, but the vendors are the source.


## Where practice is converging

The practical agreement forming this month is about review economics. It is not about more guardrails.

- **The review sandwich.** AI does the surface pass: style, obvious defects, and test gaps. Humans review architecture and business logic. GitHub internal data is cited at a 30 to 50 percent cut in human review time. If review is the ceiling, copy this pattern.
- **Constrain pull request size at the source.** AI-assisted pull requests run about 2.6 times larger than human ones. Teams repeatedly name "changes larger than what was requested" as the top cause of rejection. A hard diff-size budget in the issue template costs less than a better reviewer.
- **Per-stage autonomy, not per-agent autonomy.** Even aggressive pipelines keep explicit human gates at high-blast-radius transitions. Those transitions are merge to release branch, production deploy, and access-control changes.
- **Verification independent of generation, gating on effects.** Use a sandbox, constrained writable paths, and a compiled test suite as the pass/fail authority. This week's Cursor vulnerability makes the case again.


## Risks and failure modes

**CVE-2026-22708 is a Cursor terminal allowlist bypass.** Cursor fixed it in version 2.3. Any team that uses Cursor Auto-Run must update. Shell built-ins such as `export`, `typeset` and `declare` ran without appearing in the allowlist. An attacker could then poison environment variables. Already-approved commands such as `git branch` and `python3 script.py` became arbitrary code execution.

An attacker can reach the flaw through indirect prompt injection. The flaw works even with an empty allowlist. The allowlist made the attack easier, because it auto-approved exactly the commands the attacker needed.

The agent-skill supply chain produced two serious papers. **PhantomSkill** (arXiv 2606.19191) describes the VulMask technique. The attacker does not put malicious instructions in `SKILL.md`. The attacker hides the payload in auxiliary `scripts/` as vulnerability-shaped code. The code activates only on a trigger the attacker controls.

The payload reads as ordinary insecure code. Reviewers and scanners therefore downgrade it from "malware" to "vulnerability." Snyk was the outlier defender and flagged 98.9 percent as malware. Cisco static analysis and LLM analysis mostly classified it wrongly.

**SkillCloak** (arXiv 2607.02357) shows payload-preserving evasion. It uses structural obfuscation and self-extracting skill packing. The authors tested it against 1,613 in-the-wild malicious skills. Some cloak variants bypassed more than 90 percent of the surveyed scanners. Cloaked skills ran under Claude Code and Codex with no statistically detectable drop in task success.

The proposed defense is SkillDetonate, a runtime behavioral auditor. It detonates the skill in a sandbox and watches the effects. Static inspection of text loses. Observing effects wins.

> **SUPPLY CHAIN**
>
> The Trivy-Action to LiteLLM PyPI token compromise remains the cautionary case. LiteLLM is the model gateway under CrewAI, DSPy, GraphRAG and many other agent frameworks. One poisoned dependency reaches dozens of downstream factories.

## How we apply this at River.io

We run a software factory. It uses native compiled code, zero third-party dependencies, test-driven development, and a GitHub-issue-driven SDLC. This week's findings map directly onto that discipline.

- **The test suite is the reviewer.** A factory that generates faster than it reviews only collects unmerged, unexamined work. Our compiled test suite is the merge authority. We track the percentage of agent pull requests that merge on the first pass as the factory's real health metric. If that number drifts toward LinearB's 32.7 percent, the issue templates are the problem, not the model.
- **We cap diff size in the issue template.** Oversized, scope-creeping pull requests are the top named cause of rejection. Every production order therefore carries one constraint line: touch no more than the stated files, make no changes outside the stated scope, and add no new build steps.
- **Zero third-party dependencies now covers the agent layer.** PhantomSkill and SkillCloak attack agent extensions, not application code. We apply the same posture one level up. Agent skills, marketplace plugins, and GitHub Actions are dependencies we do not take. Our tooling is first-party. We pin and review any action we do use.
- **Allowlists are not a security boundary.** The Cursor CVE generalizes. Our boundary is a sandbox with constrained writable paths, plus a build that must go green. We gate on effects, not on strings.
- **We write autonomy down per stage and match it to the stakes.** Generation and test-fix loops run autonomously. Merge to main, release, and anything that touches schema or protected health information stay human-gated. CareTime and TimeForCare (Medicaid electronic visit verification) and MaterialsAndPractices stay fully human-gated. When 43 percent of AI changes need production debugging after they pass QA, regulated work does not get the fast lane.
- **We prove lights-out on low-stakes repositories first.** On MeowPassword, weathergalactic and sloth we run the Composio-style experiment. Each agent gets an isolated worktree. The agent owns its own CI-failure fixes. The native test suite is the only merge authority. We measure the first-pass merge rate. We also measure how often the suite caught something a human would have caught. That answers the lights-out question without risking a regulated codebase. We can also build a sandboxed harness in the shape of SkillDetonate. It records filesystem and syscall effects and diffs them against an expected envelope. It is buildable in native code with no dependencies, and it is the same primitive that makes autonomous merges safe.


---


## Sources

- [LinearB 2026 Benchmarks: why AI-assisted PRs merge at half the rate](https://linearb.io/dev-interrupted/podcast/linearb-2026-benchmarks-ai-pr-merge-rate) · [byteiota: AI PRs wait 4.6x longer](https://byteiota.com/ai-prs-wait-4-6x-longer-linearb-2026-benchmarks/) · [byteiota: the AI code review gap](https://byteiota.com/software-engineering-benchmarks-2026-ai-code-review-gap/) · [Exceeds: LinearB code review metrics 2026](https://blog.exceeds.ai/linearb-code-review-metrics-2026/)
- [The review bottleneck: why more AI code means slower teams](https://dev.to/code-board/the-review-bottleneck-why-more-ai-code-means-slower-teams-in-2026-1e5n) · [Rick Pollick: review capacity is the new delivery ceiling](https://rickpollick.com/blog/review-capacity-is-the-new-delivery-ceiling) · [Codacy: AI is breaking code review](https://blog.codacy.com/ai-breaking-code-review-how-engineering-teams-survive-pr-bottleneck) · [MetaCTO: code review is the new bottleneck](https://www.metacto.com/blogs/code-review-bottleneck-ai-development) · [DeviQA: state of AI-generated code 2026, the QA gap](https://www.deviqa.com/blog/state-of-ai-generated-code-2026-the-qa-and-testing-gap/)
- [arXiv 2606.13468: understanding the rejection of fixes generated by agentic PRs (AIDev)](https://arxiv.org/abs/2606.13468) · [arXiv 2605.22534: why are agentic pull requests merged or rejected?](https://arxiv.org/html/2605.22534)
- [CVE-2026-22708: Cursor terminal allowlist bypass (GitHub advisory)](https://github.com/cursor/cursor/security/advisories/GHSA-82wg-qcm4-fp2w) · [Pillar Security: the agent security paradox](https://www.pillar.security/blog/the-agent-security-paradox-when-trusted-commands-in-cursor-become-attack-vectors) · [danusminimus technical writeup](https://danusminimus.github.io/posts/The-Agent-Security-Paradox-When-Trusted-Commands-In-Cursor-Become-Attack-Vectors/) · [SC Media: stealthy RCE via indirect prompt injection](https://www.scworld.com/news/cursor-vulnerability-enables-stealthy-rce-via-indirect-prompt-injection) · [SentinelOne CVE entry](https://www.sentinelone.com/vulnerability-database/cve-2026-22708/)
- [arXiv 2606.19191: PhantomSkill, malicious code injection in agent skill ecosystems (VulMask)](https://arxiv.org/abs/2606.19191) · [arXiv 2607.02357: Cloak and Detonate, scanner evasion and dynamic detection of agent skill malware](https://arxiv.org/abs/2607.02357) · [CybersecurityNews: agent skill malware targets Claude Code and Codex](https://cybersecuritynews.com/agent-skill-malware-targets-claude-code-and-openai-codex/) · [GBHackers: malicious agent skills](https://gbhackers.com/malicious-agent-skills/) · [awesome-agent-skills-security](https://github.com/LLMSecurity/awesome-agent-skills-security)
- [Huawei Cloud launches CodeArts Agent open beta (PR Newswire, Jul 24)](https://www.prnewswire.com/apac/news-releases/huawei-cloud-launches-agentic-infrastructure-and-codearts-agent-obt-in-thailand-accelerating-enterprise-ai-innovation-302833957.html) · [TNGlobal coverage](https://technode.global/2026/07/24/chinas-huawei-cloud-launches-agentic-ai-infrastructure-coding-agent-beta-in-thailand/)
- [ChatGPTAIHub: what July 16's AI coding agent news means for developers](https://chatgptaihub.com/the-big-ai-coding-agents-story-what-july-16-s-news-means-for-developers/) · [MindStudio: GPT-5.5 vs Opus 4.7 vs Gemini 3.1 Pro for builders](https://www.mindstudio.ai/blog/gpt-5-5-review-developers-builders) · [AI Agents News, week of July 25, 2026](https://aiagentstore.ai/ai-agent-news/this-week)
- [arXiv 2605.07062: from assistance to agency, rethinking autonomy and control in CI/CD pipelines](https://arxiv.org/html/2605.07062v1) · [Zylos: agentic CI/CD](https://zylos.ai/research/2026-05-12-agentic-cicd-ai-driven-delivery-pipelines/) · [Augment Code: 9 open-source agent orchestrators](https://www.augmentcode.com/tools/open-source-agent-orchestrators)
- [iTmethods: Dark Factory, governed autonomous SDLC](https://itmethods.com/dark-factory) · [BCG Platinion: the agentic software factory](https://www.bcgplatinion.com/insights/the-agentic-software-factory) · [i-scoop: dark software factories](https://www.i-scoop.eu/dark-software-factories-and-the-future-of-autonomous-software-delivery/)
- [Spec-driven development is eating software engineering: a map of 30+ agentic coding frameworks](https://medium.com/@visrow/spec-driven-development-is-eating-software-engineering-a-map-of-30-agentic-coding-frameworks-6ac0b5e2b484) · [GitHub Spec Kit](https://github.com/github/spec-kit) · [BCMS: the definitive 2026 guide to SDD](https://thebcms.com/blog/spec-driven-development)
- [Second Talent: how much software is AI-written in 2026](https://www.secondtalent.com/resources/how-much-software-written-by-ai/) · [DigitalApplied: AI coding adoption 2026 statistics](https://www.digitalapplied.com/blog/ai-coding-adoption-statistics-2026-50-data-points) · [Cursor insights](https://cursor.com/insights)


*Vendor and blog figures indicate direction, not audited benchmarks. This includes merge rates, throughput, the percentage of AI-written code, and first-pass-success multipliers. Where a claim comes from a single vendor survey or aggregator, we flag it inline.*


---

Canonical copy: [www.river.io/blog/posts/2026-07-27-review-capacity-is-the-new-ceiling-for-ai-written-code.html](https://www.river.io/blog/posts/2026-07-27-review-capacity-is-the-new-ceiling-for-ai-written-code.html). Mirrored into this wiki. The river.io blog is the source of truth.
