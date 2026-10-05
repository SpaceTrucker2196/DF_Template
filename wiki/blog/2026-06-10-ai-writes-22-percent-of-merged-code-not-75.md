---
title: "AI writes 22 percent of merged code, not 75"
date: 2026-06-10
order: 4
tags: "Briefing, Metrics, Security, Autonomy"
description: "DX's data across 135,000 developers punctures the vendor headlines. Forrester names a new security operating model for agentic development. Salesforce posts the strongest first-party numbers yet. A cross-vendor prompt injection shows the pipeline is now the attack surface."
layout: default
---

# AI writes 22 percent of merged code, not 75

*Order 004 · 2026-06-10 · 8 min · Briefing, Metrics, Security, Autonomy*

> DX's data across 135,000 developers punctures the vendor headlines. Forrester names a new security operating model for agentic development. Salesforce posts the strongest first-party numbers yet. A cross-vendor prompt injection shows the pipeline is now the attack surface.

In June 2026 the conversation about autonomous software development moved. It moved from "can agents write the code" to "who governs the pipeline." Forrester named the phase in its report The State of Agentic Software Development, 2026. Forrester paired the report with a new security operating model. The least mature capability in that model is agent-aware quality gates.

Salesforce published the cleanest first-party proof of an organization-wide agentic shift. DX supplied the most useful reality check of the season. Across more than 135,000 developers, AI-authored code holds at about 22 percent of merged code. That is an order of magnitude below the "75 percent" and "100 percent" headlines. One throughline runs through every autonomous pipeline: the bottleneck is now the gate, not the generator.

## Forrester names the phase, and a paradox

Forrester's framing is blunt. TuringBots are becoming agentic. They are no longer assistants inside one tool. Agents now cover analysis and planning, design, build, test, and delivery, and teams increasingly orchestrate them together. You delegate intent, such as "build this feature." The agents then decompose the work, generate it, test it, and stage the release.

The sharpest finding is a productivity paradox. Coding alone may improve 30 to 40 percent. But if planning, testing, and release stay manual, whole-team productivity often rises less than 10 percent. The un-automated stages gate the lights-out win, not the coding stage. Forrester prescribes one fix: treat agents as first-class participants in a redesigned, collapsed SDLC, with humans firmly in control.

## The gate becomes its own product category

Forrester analyst Janet Worthington introduced **Agentic Development Security (ADS)** after RSAC 2026. She defines it as "a new security paradigm protecting AI-powered software development end to end." It covers prevention, detection, prioritization, and remediation. It treats security as autonomous, policy-driven actions, not as alerts. Forrester lists eight capability clusters. As of RSAC, no single vendor covers all eight.

The two least mature clusters are supply-chain defense against AI-specific vectors and agent-aware quality gates. Those AI-specific vectors include slopsquatting and hallucinated dependencies. AI-augmented code analysis is the most mature cluster. Read it this way. The verification layer a dark factory most needs is the layer the market is worst at. Teams have to build it themselves.

Codacy, CodeScene and TFiR are converging on three properties a verification layer must have. The first is **independence**, which means a different system than the one that wrote the code. The second is **deterministic pass/fail** for security and policy. The third is **context awareness**, so the layer can verify intent.

Multi-agent validation chains are now a named pattern. One agent writes. A second critiques. A third tests. A fourth checks compliance and architecture. Each agent communicates through files. The spec-driven command surface is stable across GitHub Spec Kit and its clones. That surface is constitution, specify, plan, tasks, analyze, implement, and checklist. Nothing changed structurally this cycle, which signals that the front-end spec layer has settled.

## Evaluate trajectories, not just outputs

The maturing guidance moves evaluation upstream of the answer. Score tool-choice correctness. Score argument validity, step count, time and cost, and policy compliance across the whole run. Do not score only whether the final diff passes tests. A loop that checks the end state alone cannot catch an agent that did the right thing in an unsafe way. Three controls are now cited together as the irreducible guardrail set: policy-as-code, approvals for irreversible actions, and prompt-injection defense.

Human approval checkpoints stay in the loop by design, even at the aggressive end of the market. InfoQ covered Anthropic's Claude Code "auto mode" in May 2026. It is autonomous execution with layered gates: input filtering, action evaluation, two-stage classification, and human approval for sensitive operations. Even the most aggressive vendor autonomy ships with a human gate on destructive verbs. That is the reference design, not a compromise.

## Proof points: the claims and the measurements

| Source | Finding | Number |
|---|---|---|
| Salesforce (first-party) | Work items completed per developer, April 2026 vs April 2025 | +50.8% |
| Salesforce (first-party) | Pull requests merged per developer, year over year | +79% |
| Salesforce (first-party) | "Effective Output" score (Salesforce-defined), year over year | +151.3% |
| Salesforce (first-party) | 231-person-day migration completed in 13 days | ~18x |
| DX (135k+ devs, 425 orgs) | AI-authored share of merged code, median | ~22% |
| DX | Time saved per developer per week | ~3.6 hrs |
| DX | Additional PRs merged by daily AI users | ~60% |
| Google (Pichai) | AI-generated (suggested, human-accepted) share of new code, April 2026 | 75% |
| Google | Velocity uplift attributed to AI | ~10% |


Salesforce's "How Engineering Became Agentic" is the strongest named-company, first-party dataset since Spotify's Honk. Salesforce moved the whole organization to Claude Code as the primary agent and removed token limits. The numbers above then arrived with fewer incidents, not more. Salesforce defines the Effective Output metric itself, but the direction is clear.

DX's Q4 Impact Report is the number to quote back at the "75 percent" and "100 percent AI-written" claims. Across more than 135,000 developers at 425 organizations, the real merged share is about a quarter. Daily users reach about 24 percent. Monthly users reach about 20 percent. The productivity gain is modest unless the use is daily.

Google's own trajectory runs from about 25 percent in October 2024, to about 50 percent in October 2025, to 75 percent in April 2026. Pichai consistently frames that number as AI-suggested and human-accepted or edited. He does not frame it as autonomous shipping. The gap between Google's "75 percent suggested" and DX's "22 percent merged" is the delegation gap, in numbers. Microsoft's baseline holds at about 30 percent. Also at Microsoft, 84 percent of developers use AI or plan to use it, and 51 percent use it daily.

## The pipeline itself is the attack surface

**"Comment and Control" is a cross-vendor prompt injection. Researchers disclosed it in April 2026 and it has escalated since.** Researchers working with Johns Hopkins put a malicious instruction in a GitHub pull request title. Anthropic's Claude Code Security Review action then posted its own API key as a comment. The same injection worked against Google's Gemini CLI Action and GitHub Copilot Agent. That was the first cross-vendor demonstration.

The root cause is structural. These actions run untrusted input, powerful tools, and secrets in the same runtime. The powerful tools include bash, git push, and API calls. Anthropic's own system card had already stated that the action is "not hardened against prompt injection."

**Microsoft Security followed up on June 5, 2026 with "Securing CI/CD in an agentic world."** It is a Claude Code GitHub Action case study on isolating agent runtimes in CI/CD. It is the direct successor to May's "When prompts become shells" disclosure, which covered Semantic Kernel CVE-2026-25592 and CVE-2026-26030. The lesson compounds. An agent in your pipeline that can read pull request text and hold deploy credentials is a confused deputy by construction.

**The supply chain is the bigger iceberg.** Cisco AI Defense found that 26 percent of roughly 31,000 agent "skills" carried at least one vulnerability. It also found a one-click remote code execution, CVE-2026-25253, CVSS 8.8, that ran from a single malicious webpage in milliseconds. Forrester's ADS data cites security-flaw rates from about 12 percent of AI-attributed files to more than 40 percent of AI-generated tasks for specific vulnerability classes. AI security in 2026 is a supply-chain problem first. It is a prompt-injection problem second.


An agent that can read a pull request comment and also push to production is the vulnerability. You have already built it.

The design implications are consistent. Scope every tool to least privilege. Put deterministic guards on irreversible verbs such as delete, force-push, deploy, and send. Keep per-action audit logs. Isolate the runtime between untrusted input and secret-holding agents.

## How we apply this at River.io

River.io builds native compiled software with zero third-party dependencies, test-driven development, and a GitHub-issue-driven SDLC. Regulated products lead the portfolio. CareTime and TimeForCare cover Medicaid electronic visit verification. MaterialsAndPractices covers organic-farm compliance.

**The less-than-10-percent paradox is our sequencing guide.** Forrester's finding says that automating coding alone barely moves the needle. The highest-leverage automation is not "let the agent write more code." It is automating the issue, spec, test, and pull request stages around our existing TDD, so the whole loop closes. Our tests are already the deterministic gate that the rest of the industry is hurrying to build.

**We satisfy the ADS independence rule by construction.** The hardest and least mature ADS capability is an agent-aware quality gate that is independent of the builder. Our native test suites plus a deterministic CI verifier are exactly that. They are a different system than the generating model. We treat that as the moat. We do not replace it with a model-based reviewer that shares the builder's blind spots.

**"Comment and Control" is the threat model for any issue-driven pipeline, including ours.** Our SDLC runs through GitHub issues and pull requests. That is exactly the untrusted-input surface that leaked secrets across all three major vendors. So any agent that acts on issue or pull request text in the regulated repositories runs with no deploy credentials, no PHI-scoped tokens, and no generic shell in the same runtime. We keep the agent that reads issues strictly separate from anything that can push, deploy, or touch a database.

**Regulated repositories stay human-gated.** On the EVV apps, database migrations, PHI exports, log purges, and production deploys are typed, allow-listed, human-approved tool calls. That follows the same pattern as Claude Code auto mode: autonomous execution, with a human gate on destructive verbs.

**Autonomous loops run first on low-stakes repositories.** MeowPassword, weathergalactic and sloth have no PHI and no regulatory surface. On those repositories we run multi-agent validation chains: a writer, a critic, a test-runner, and a constitution-checker, all communicating through version-controlled files. We scope each chain to a single task type. We measure it at the trajectory level, not only at the final diff.

**We plan around 22 percent, not 75.** The realistic merged AI-authored share at well-run shops is about a quarter. We plan the factory's economics around widening that number steadily on safe repositories. We do not plan around a lights-out fantasy that the data does not yet support.

---


## Sources

- [The State Of Agentic Software Development, 2026 (Forrester)](https://www.forrester.com/blogs/agentic-software-development-takes-the-lead-from-code-assistants-to-orchestrated-sdlc-agents/) · [Agentic Software Development: Defining The Next Phase (Forrester)](https://www.forrester.com/blogs/agentic-software-development-defining-the-next-phase-of-ai-driven-engineering-tools/) · [Agentic AI is rewiring the SDLC (CIO)](https://www.cio.com/article/4166035/agentic-ai-is-rewiring-the-sdlc.html) · [AI is rewiring the software industry (Business Standard, June 7, 2026)](https://www.business-standard.com/technology/tech-news/ai-is-rewiring-the-software-industry-by-collapsing-traditional-workflows-126060700668_1.html)
- [What Is Agentic Development Security (ADS)? (Augment Code)](https://www.augmentcode.com/guides/agentic-development-security) · [Agentic Development Security: Why AppSec Needs A New Operating Model (Forrester)](https://www.forrester.com/blogs/agentic-development-security-why-appsec-needs-a-new-operating-model/) · [Arnica in The Forrester Agentic Development Security Tools Landscape, Q2 2026](https://www.arnica.io/blog/arnica-included-in-the-forrester-agentic-development-security-tools-landscape-q2-2026)
- [How Salesforce Engineering Became Truly Agentic (Salesforce)](https://www.salesforce.com/news/stories/how-engineering-became-agentic/) · [Salesforce claims AI agents cut a 231-day migration to 13 days (The Decoder)](https://the-decoder.com/salesforce-claims-ai-agents-cut-a-231-day-migration-to-13-days-with-fewer-incidents/) · [Salesforce scales agentic engineering 18x (HeadsUp AI)](https://headsupai.io/updates/salesforce-compresses-231-day-migration-into-13-days-using-claude-code)
- [AI-generated merged code holds steady (DX)](https://getdx.com/blog/ai-generated-merged-code-holds-steady-at-30/) · [DX AI-assisted engineering Q4 impact report](https://getdx.com/report/ai-assisted-engineering-q4-impact-report/) · [93% of Developers Use AI. Why Is Productivity Only 10%? (ShiftMag)](https://shiftmag.dev/this-cto-says-93-of-developers-use-ai-but-productivity-is-still-10-8013/)
- [Google's 75% AI-Generated Code Claim Hides Shift (NovaKnown)](https://novaknown.com/2026/04/24/ai-generated-code-google/) · [Google's 75% AI Code Milestone (Metaintro)](https://www.metaintro.com/blog/google-75-percent-ai-generated-code-software-engineer-jobs-2026) · [AI Writes 30% of Microsoft's Code, 25% of Google's (Medium)](https://medium.com/@sohail_saifi/ai-writes-30-of-microsofts-code-and-25-of-google-s-6909f6e0b406)
- [Three AI coding agents leaked secrets through a single prompt injection (VentureBeat)](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) · [Comment and Control: Prompt Injection to Credential Theft (Aonan Guan)](https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot/) · [Claude Code, Gemini CLI, Copilot Agents Vulnerable via Comments (SecurityWeek)](https://www.securityweek.com/claude-code-gemini-cli-github-copilot-agents-vulnerable-to-prompt-injection-via-comments/)
- [Securing CI/CD in an agentic world: Claude Code GitHub Action case (Microsoft Security Blog, June 5, 2026)](https://www.microsoft.com/en-us/security/blog/2026/06/05/securing-ci-cd-in-agentic-world-claude-code-github-action-case/) · [When prompts become shells (Microsoft Security Blog, May 7, 2026)](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/) · [AI Agent Security Risks 2026: MCP, OpenClaw and Supply Chain (CyberDesserts)](https://blog.cyberdesserts.com/ai-agent-security-risks/) · [Top AI Security Vulnerabilities 2026 (Cycode)](https://cycode.com/blog/ai-security-vulnerabilities/)
- [Why Coding Agents Need Independent Quality Gates (Codacy)](https://blog.codacy.com/why-coding-agents-need-independent-quality-gates) · [AI Code Quality in 2026: Guardrails (TFiR)](https://tfir.io/ai-code-quality-2026-guardrails/) · [AI Code Guardrails (CodeScene)](https://codescene.com/use-cases/ai-code-quality) · [Inside Claude Code Auto Mode (InfoQ, May 2026)](https://www.infoq.com/news/2026/05/anthropic-claude-code-auto-mode/) · [AI Agents in 2026: Tools, Memory, Evals, Guardrails (Furmanets)](https://andriifurmanets.com/blogs/ai-agents-2026-practical-architecture-tools-memory-evals-guardrails)
- [The Dark Software Factory (BCG Platinion)](https://www.bcgplatinion.com/insights/the-dark-software-factory) · [What Is a Dark Factory Codebase? (MindStudio)](https://www.mindstudio.ai/blog/what-is-a-dark-factory-codebase) · [The Dark Factory Pattern (HackerNoon)](https://hackernoon.com/the-dark-factory-pattern-moving-from-ai-assisted-to-fully-autonomous-coding) · [GitHub Spec Kit](https://github.com/github/spec-kit) · [Diving Into Spec-Driven Development With GitHub Spec Kit (Microsoft for Developers)](https://developer.microsoft.com/blog/spec-driven-development-spec-kit)


*Vendor and blog figures cited here indicate direction, not audited benchmarks. This includes pull request counts, productivity multipliers, and the percentage of AI-authored code. Treat them as fast-moving signals.*


---

Canonical copy: [www.river.io/blog/posts/2026-06-10-ai-writes-22-percent-of-merged-code-not-75.html](https://www.river.io/blog/posts/2026-06-10-ai-writes-22-percent-of-merged-code-not-75.html). Mirrored into this wiki. The river.io blog is the source of truth.
