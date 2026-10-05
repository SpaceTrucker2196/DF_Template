---
title: "What 933,000 agent pull requests reveal about autonomous coding"
date: 2026-07-06
order: 9
tags: "Briefing, Metrics, Security, Practice"
description: "The first large-scale studies of agent-authored pull requests give real numbers on autonomous coding. Agents get rejected at roughly four times the human baseline. Their tests often pass without proving anything."
layout: default
---

# What 933,000 agent pull requests reveal about autonomous coding

*Order 009 · 2026-07-06 · 8 min · Briefing, Metrics, Security, Practice*

> The first large-scale studies of agent-authored pull requests give real numbers on autonomous coding. Agents get rejected at roughly four times the human baseline. Their tests often pass without proving anything.

In early July 2026, the honest empirical evidence on autonomous coding finally arrived. It complicates the hype. A cluster of new arXiv studies mines the AIDev dataset. That dataset holds roughly 933,000 agentic pull requests from Codex, Copilot, Devin, Cursor, and Claude Code across 61,000 repositories. The studies put real numbers on agent behavior for the first time.

The picture is sobering. Agent pull requests get rejected far more often than human pull requests. One benchmark set cites about 67 percent rejection for AI-generated pull requests, against about 16 percent for manual work. Agent-authored tests are frequently present but of questionable quality. Pull requests that contain tests are bigger and slower, without clearly higher merge rates.

The method is real, and it is improving. The newest primary-source evidence still says agent output needs a hard, executable gate.

## Researchers are now supplying the evidence, not vendors

The vocabulary around autonomous software production is consolidating. Vendors now pitch the "Agentic SDLC" and the "AI Software Factory" as industrialization. That means standardized processes, an orchestrator agent, and "bolts" in place of two-week sprints. A bolt is a compressed delivery unit where weeks become days. Treat the industrial-scale language as aspiration, because the sources that pitch it are consulting and marketing pages.

A more careful phrase keeps recurring, including in PwC's 2026 analysis: **bounded autonomy**. Agents operate inside human-governed approval structures. They do not exercise independent control. That is the honest description of what is actually shipping.

The substantive shift is who holds the data. Several research groups mine the AIDev corpus in parallel. Their descriptive findings are the most trustworthy signal the field has had. The AIDev-pop subset is the cleaner sample, with 33,596 pull requests from repositories with more than 100 stars.

In that subset, pull requests that contain tests are more common over time. They are also larger and slower to land, and their merge rates are broadly similar. Companion studies analyze why agentic pull requests merge or get rejected. Other companion studies analyze the security properties of agentic pull requests at scale.

## The numbers, honestly labeled

| Finding | Figure | Source quality |
|---|---|---|
| AI-generated PR rejection rate | ~67.3% | 2026 benchmark set |
| Manual PR rejection rate | ~15.6% | Same benchmark set |
| Extra PRs merged by daily AI users | ~60% | Read together with the rejection gap |
| Enterprise merged PRs listing an agent as primary author or pair-coder | ~18% | Enterprise survey |
| Google new code AI-generated and engineer-approved | ~75% | Self-reported, April 2026, up from ~25% through 2025 |
| Anthropic internal AI-written share | 70–90% | Directional executive statements |
| Devin at Nubank, ETL migration efficiency | 8–12x | Vendor case study |


Two anecdotes deserve their flags. Anthropic's report describes Rakuten running Claude Code inside vLLM, a library of roughly 12.5 million lines. Claude Code completed an activation-vector extraction task in about 7 hours of autonomous work. It reached roughly 99.9 percent numerical accuracy against the reference. The result is impressive, and it is a single vendor-cited case.

Claude Code's own lead reports that 100 percent of his personal code is AI-written. That is a workflow claim, not a measured repository-wide figure. Devin is cited in production at Goldman Sachs, Santander, and Nubank.

## Smoke without alarms

The most important new finding of the cycle is the "All Smoke, No Alarm" study (arXiv 2606.18168). It examines oracle signals in agent-authored test code. Agents often produce tests that run but assert little of substance. Weak or missing oracles let an autonomous loop manufacture green checks with no real verification behind them. A dark factory is most exposed to that failure mode, because the test suite is the gate.


An agent that writes both the code and its own toothless test is a closed loop with no oracle.

The mitigation is test-driven development done properly. The human or the specification writes the failing assertion that defines correct behavior. The agent then codes to that assertion. Anthropic's 2026 Agentic Coding Trends Report frames the same constraint from the other side. Its "delegation gap" finding says developers use AI in about 60 percent of work. They can fully delegate only 0 to 20 percent of tasks.

The report gives a one-line thesis: the bottleneck is no longer writing code, it is clarity about what to build. The report also finds that teams with well-maintained context files see 40 percent fewer errors and 55 percent faster completion. That reconciles with earlier evidence that bloated context files hurt. Keep context files lean and load-bearing, not comprehensive.

## Tooling: Spec Kit v0.12.3

GitHub Spec Kit shipped v0.12.3 on 1 July 2026. The release adds a label-driven bug-test workflow. It also adds a warning ahead of the skills default rollout. The core loop is unchanged: Spec, Plan, Tasks, Implement. A read-only analyze gate cross-checks the constitution, spec, plan, and tasks before any code is written. It looks for ambiguities, coverage gaps, and contradictions.

The new label-driven feature matters for issue-driven shops. It ties a reproduction test to a labeled issue, which turns a bug report into a failing test first. The community ecosystem of more than 70 extensions continues to grow. It includes Jira, Azure DevOps, and GitHub Issues integrations, plus security, testing, and drift gates. Teams can still restructure spec templates to require regulatory traceability with non-optional test-first and security-review gates.

## The live risks

**The dependency supply chain is the open wound.** The LiteLLM PyPI backdoor sat live for about three hours in March 2026. It collected roughly 47,000 downloads. LiteLLM is the LLM gateway under CrewAI, DSPy, Microsoft GraphRAG, and dozens of agent frameworks. One compromised transitive dependency in an agent stack is a supply-chain event. Its blast radius covers every downstream framework.

**Prompt injection remains unsolved, and it is accelerating.** OWASP data puts growth at roughly 340 percent year over year. It maps to six of the ten categories in OWASP's Top 10 for Agentic Applications. An OWASP researcher calls it unsolved.

**Agent frameworks are turning prompts into shells.** Microsoft disclosed prompt-injection-to-RCE paths in agent frameworks. In these paths, a single prompt launches a process on the host. CVE-2026-22708 against Cursor lets an attacker poison the agent's execution environment. Allowlisted commands as innocuous as `git branch` then deliver arbitrary payloads. Allowlists are not a safe boundary if the environment can be poisoned.

> **THE OPERATIONAL READING**
>
> AI pull requests are rejected at multiples of the human rate. The review gate is therefore the product. Throughput claims mean nothing without the merge-quality denominator. A green check means nothing without a real oracle behind it.

## How we apply this at River.io

Our posture is native compiled code, zero third-party dependencies, test-driven development, and a GitHub-issue-driven SDLC. This cycle's evidence points the same way. Its marketing does not.

**The LiteLLM backdoor is the case for zero dependencies.** It is a concrete, recent example of the risk the rule eliminates. A transitive dependency compromise cascaded through every framework that trusted it. Agentic development does not change that calculus. It sharpens it. We keep the rule, and we keep the agent toolchain itself lean.

**TDD is the antidote to smoke-without-alarm tests.** The research says agent-written tests often lack real oracles. Our discipline is a human-defined or spec-defined failing assertion first. That control closes the gap. On any repository where an agent may open pull requests, the agent may not author both the assertion and the implementation for the same behavior. The oracle comes from the issue or the spec, never from the coder.

**The label-driven bug-test workflow maps onto our issue-driven SDLC.** The pattern is clean and low-risk: a labeled bug issue, a generated reproduction test, a failing test, then a fix. It keeps the human at the point that matters, which is defining the failing test. The agent does the mechanical work.

**Regulated work stays human-gated.** Our CareTime and TimeForCare Medicaid EVV applications run at human-gated autonomy. So does our MaterialsAndPractices organic-farm compliance application. Agents may draft, and a human approves every merge. No agent authors the compliance-defining assertions. This cycle's rejection-rate and prompt-injection data reinforce that regulated code is not the place to test lights-out operation.

**Experiments run on the low-stakes repositories, with our own measurements.** MeowPassword, weathergalactic, and sloth remain the sandboxes for a planner-generator-evaluator loop with an executable merge gate. The current experiment measures how many agent pull requests pass a human-authored test oracle against an agent-authored one. That gives us a local version of the AIDev merge-quality numbers rather than a citation.

---


## Sources

- [MindStudio: What Is a Dark Factory (AI Coding)](https://www.mindstudio.ai/blog/what-is-a-dark-factory-ai-coding) · [MindStudio: Dark Factory AI Agent](https://www.mindstudio.ai/blog/what-is-a-dark-factory-ai-agent) · [BCG Platinion: The Dark Software Factory](https://www.bcgplatinion.com/insights/the-dark-software-factory)
- [ASDLC.io: Agentic SDLC / Software Factory Framework](https://asdlc.io/concepts/agentic-sdlc/) · [momentiq: Dark Factory, The Autonomous AI-Native SDLC](https://momentiq.ai/dark-factory/)
- [PwC: Agentic SDLC in practice (2026)](https://www.pwc.com/m1/en/publications/2026/docs/future-of-solutions-dev-and-delivery-in-the-rise-of-gen-ai.pdf)
- [arXiv 2601.03556: Do Autonomous Agents Contribute Test Code?](https://arxiv.org/abs/2601.03556) · [arXiv 2605.22534: Why Are Agentic PRs Merged or Rejected?](https://arxiv.org/pdf/2605.22534)
- [arXiv 2606.18168: All Smoke, No Alarm, Oracle Signals in Agent-Authored Test Code](https://arxiv.org/pdf/2606.18168) · [arXiv 2601.00477: Security in the Age of AI Teammates](https://arxiv.org/pdf/2601.00477)
- [GitHub Spec Kit: Releases](https://github.com/github/spec-kit/releases) · [Documentation](https://github.github.com/spec-kit/) · [Microsoft for Developers: Spec-Driven Development with Spec Kit](https://developer.microsoft.com/blog/spec-driven-development-spec-kit) · [MarkTechPost: Meet GitHub Spec Kit](https://www.marktechpost.com/2026/05/08/meet-github-spec-kit-an-open-source-toolkit-for-spec-driven-development-with-ai-coding-agents/)
- [Anthropic: 2026 Agentic Coding Trends Report](https://resources.anthropic.com/2026-agentic-coding-trends-report) · [Pathmode: Anthropic 2026 report summary](https://pathmode.io/blog/orchestration-era-needs-intent)
- [Larridin: Developer Productivity Benchmarks 2026](https://larridin.com/developer-productivity-hub/developer-productivity-benchmarks-2026)
- [Second Talent: How Much Software Is Written by AI in 2026](https://www.secondtalent.com/resources/how-much-software-written-by-ai/) · [Medium/Saifi: AI Writes 30% of Microsoft's and 25% of Google's Code](https://medium.com/@sohail_saifi/ai-writes-30-of-microsofts-code-and-25-of-google-s-6909f6e0b406)
- [Fortune: Anthropic and OpenAI engineers say AI writes 100% of their code](https://fortune.com/2026/01/29/100-percent-of-code-at-anthropic-and-openai-is-now-ai-written-boris-cherny-roon/)
- [GitHub: awesome-ai-agents-2026 (Devin/Nubank case data)](https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026)
- [Help Net Security: Prompt injection drives most agentic AI failures (OWASP)](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/) · [Infosecurity Magazine: Prompt Injection Remains Unsolved](https://www.infosecurity-magazine.com/news/infosec-europe-prompt-injection/)
- [Microsoft Security: When prompts become shells, RCE in AI agent frameworks](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/) · [VentureBeat: Three AI coding agents leaked secrets through one prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [cyberdesserts: AI Agent Security Risks 2026 (LiteLLM, MCP, supply chain)](https://blog.cyberdesserts.com/ai-agent-security-risks/)


*Vendor and blog figures cited here show direction, not audited benchmarks. This includes adoption percentages, AI-written-code shares, efficiency multiples, and single-company anecdotes. The arXiv AIDev studies are the most trustworthy items, but they are descriptive, not causal. Read fast-moving self-reported numbers, such as Google's roughly 75 percent, as directional.*


---

Canonical copy: [www.river.io/blog/posts/2026-07-06-what-933000-agent-pull-requests-reveal.html](https://www.river.io/blog/posts/2026-07-06-what-933000-agent-pull-requests-reveal.html). Mirrored into this wiki. The river.io blog is the source of truth.
