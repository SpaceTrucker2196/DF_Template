---
title: "The frontier labs just asked for a brake pedal"
date: 2026-07-30
order: 15
tags: "Regulation, Security, Tooling, Briefing"
description: "More than 1,100 employees of the frontier AI labs asked the US government for the tools to pace automated AI development on purpose. OpenAI and Anthropic endorsed the request within hours. GitHub made code review programmable through in-repo skills. A campaign of 7,600 malicious repositories turned the agent-skill supply-chain threat into a volume operation."
layout: default
---

# The frontier labs just asked for a brake pedal

*Order 015 · 2026-07-30 · 6 min · Regulation, Security, Tooling, Briefing*

> More than 1,100 employees of the frontier AI labs asked the US government for the tools to pace automated AI development on purpose. OpenAI and Anthropic endorsed the request within hours. GitHub made code review programmable through in-repo skills. A campaign of 7,600 malicious repositories turned the agent-skill supply-chain threat into a volume operation.

In late July 2026, the most important development in autonomous software was policy, not product. On July 28, more than 1,100 employees of the frontier AI labs signed the "Pacing the Frontier" letter. The signatories include Anthropic's Dario Amodei, OpenAI chief scientist Jakub Pachocki, Meta's Shengjia Zhao, and DeepMind's Anca Dragan. The letter asks the US government for help. It wants the technical and governance tools to pace automated AI development on purpose. On July 29, within hours, OpenAI and Anthropic endorsed the letter as companies.

The endgame of the dark factory is AI accelerating its own development. The people who build it now formally want a brake pedal for it.

## What the letter asks

The letter is deliberately narrow. The signatories do not ask for a pause now. They ask Washington to make a coordinated slowdown possible, through verification, monitoring, and international mechanisms. They want those tools in place before recursive self-improvement makes the question moot. They warn of "a real risk that capability development rapidly accelerates beyond our ability to understand or control the resulting systems." The corporate endorsements are the new part: the labs formally back a mechanism that could constrain their own automated-R&D flywheel.

Throughput gives the letter its weight. Anthropic's own institute disclosure reports that more than 80 percent of code merged to its production codebase is Claude-authored. That is a May 2026 measure. Leadership estimates 90 percent or more when you include scripts. The same disclosure reports that typical engineers merge 8 times as much code per day as in 2024. It also reports a 76 percent success rate on open-ended internal engineering tasks.

The throughput is real. The letter is the labs saying that the control tools have not kept pace. These are company-reported figures, so read them as direction, not audit.

## The verifier becomes programmable

On July 29, GitHub made agent skills and MCP generally available inside Copilot code review. The review agent, not just the coding agent, can now call a team's own tools and standards. Drop a `SKILL.md` file under `.github/skills` and Copilot applies it during every review. MCP servers pull tracker and documentation context into the review. GitHub restricts all review-time MCP calls to read-only. Attribution labels show which comment came from which skill or server.

The architecture is the point. The oracle becomes in-repo, version-controlled configuration instead of a black box. That is the right shape for spec-driven pipelines. It also means skills now execute inside the reviewer. The reviewer is a new injection surface.

Two smaller items round out the tooling picture. GitHub's Copilot cloud agent for Linear went GA on July 23. It is an autonomous background agent that analyzes tracker issues and drafts pull requests. It makes the issue-to-agent-to-PR loop an off-the-shelf product tier, and it validates issue-driven development as the interface for autonomous work. The GitHub MCP Server added support for the next, stateless, MCP specification revision on July 23. Claude Opus 5 (July 24) and Grok 4.5 (July 28) landed in Copilot's model picker.

## The skill supply chain is now industrialized

Researchers tracking a campaign named AgentBaiting counted roughly 7,600 malicious GitHub repositories, created by roughly 6,600 profiles. More than 800 of those repositories pose as AI Skills or MCP servers. They deliver SmartLoader malware through trusted-looking projects and public capability catalogs. This moves the poisoned-skill concern from proof of concept to volume operation. It targets the install-a-capability reflex that agent ecosystems encourage.

Skill catalogs and MCP registries lack the security maturity of mature package registries. Treat both like npm circa 2016. Researchers first reported the campaign around July 21. An RH-ISAC advisory circulated this week.

> **THE DOUBLE EDGE**
>
> Skills inside the review agent are powerful and double-edged. GitHub's mitigations are the right defaults: read-only MCP at review time, and per-comment attribution. But a poisoned `SKILL.md` in the reviewer is a poisoned gate. A poisoned gate is worse than a poisoned generator.


A compromised generator writes bad code that a good gate catches. A compromised gate approves anything.

## How we apply this at River.io

We build in native compiled code with zero third-party dependencies. We develop test-first. We run our SDLC through GitHub issues. We match autonomy to the stakes of each repository. This week's developments confirm each of those choices from a different direction.

- **Our review standards live in the repository, and we write them.** The Copilot code review GA productizes something we already practice: we encode standards as version-controlled, in-repo configuration. Each repository can hold our rules as skill files. Those rules are cite-your-sources in sloth, zero third-party dependencies, and our native-code conventions. That is configuration under version control, not an installed dependency, and we write those files first-party only. We never pull a skill from a catalog.
- **AgentBaiting is the case for zero dependencies as a security control.** More than 800 fake skills and MCP servers on public catalogs make "install this capability" a mainstream malware vector. Our rule removes that entire class of attack: no third-party skills, no marketplace MCP servers, and tools built in-tree. We state the rule explicitly in each repository's contributing and security documents. Autonomous agents then inherit the constraint.
- **We audit the gate, not just the diff.** If any review-time automation gains skill or MCP extensibility, we log which skill produced which verdict. We follow the attribution-label pattern GitHub shipped. The reviewer is now an attack surface. A gate that cannot account for its own verdicts is not a gate.
- **Stakes-matched autonomy is the pacing letter at our scale.** The labs ask that the brake exist before anyone needs it, and ours already does. CareTime, TimeForCare and MaterialsAndPractices keep human-gated merges permanently. MeowPassword, weathergalactic and sloth serve as the autonomous-loop lab, where the worst case is a broken build. The Linear agent GA shows that issue-to-PR autonomy is now a commodity. The differentiator is deciding in advance where it may run.


---


## Sources

- [Fortune: 1,200+ AI workers ask Washington for an AI slowdown plan](https://fortune.com/2026/07/29/anthropic-deepmind-openai-meta-washington-ai-slowdown-plan/) · [TechTimes: OpenAI and Anthropic formally back plan to slow AI that writes its own code](https://www.techtimes.com/articles/322125/20260729/openai-anthropic-formally-back-plan-slow-ai-that-writes-its-own-code.htm) · [TNW: 1,134 AI staff ask the US for a way to pace AI](https://thenextweb.com/news/pacing-the-frontier-ai-employees-letter-us-government) · [Unite.AI: OpenAI and Anthropic back employee call](https://www.unite.ai/openai-and-anthropic-back-employee-call-to-pace-ai-progress/)
- [Anthropic Institute: when AI builds itself (recursive self-improvement; 80%+ Claude-authored merged code)](https://www.anthropic.com/institute/recursive-self-improvement) · [VentureBeat: Anthropic says 80% of its new production code is Claude-authored](https://venturebeat.com/technology/anthropic-says-80-of-its-new-production-code-is-now-authored-by-claude-how-your-enterprise-can-keep-up)
- [GitHub Changelog: Copilot code review, agent skills and MCP now GA](https://github.blog/changelog/2026-07-29-copilot-code-review-agent-skills-and-mcp-now-generally-available/) · [GitHub Changelog: Copilot cloud agent for Linear GA](https://github.blog/changelog/2026-07-23-copilot-cloud-agent-for-linear-is-now-generally-available) · [GitHub Changelog: GitHub MCP Server supports the next MCP specification](https://github.blog/changelog/2026-07-23-github-mcp-server-supports-the-next-mcp-specification)
- [RH-ISAC: AgentBaiting campaign delivers SmartLoader via fake AI Skills and MCP servers](https://rhisac.org/threat-intelligence/new-agentbaiting-campaign-delivers-smartloader-via-fake-ai-skills-and-mcp-servers/) · [Obot: securing MCP and agent-skill supply chains](https://obot.ai/blog/mcp-security-agent-skills-supply-chain/)


*Vendor and blog figures show direction, not audited benchmarks. This applies to AI-authored-code percentages, throughput multipliers, and campaign repository counts. We flag company-reported metrics inline.*


---

Canonical copy: [www.river.io/blog/posts/2026-07-30-the-frontier-labs-just-asked-for-a-brake-pedal.html](https://www.river.io/blog/posts/2026-07-30-the-frontier-labs-just-asked-for-a-brake-pedal.html). Mirrored into this wiki. The river.io blog is the source of truth.
