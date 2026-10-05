---
title: "Confidence is not a control"
date: 2026-09-14
order: 36
tags: "Briefing, Practice, Autonomy"
description: "Seven hundred organizations running agents in production say they trust their testing. One in five has a gate that blocks a bad release. In the same week OpenAI put the Codex harness behind one API call."
layout: default
---

# Confidence is not a control

*Order 036 · 2026-09-14 · 9 min · Briefing, Practice, Autonomy*

> Seven hundred organizations running agents in production say they trust their testing. One in five has a gate that blocks a bad release. In the same week OpenAI put the Codex harness behind one API call.

Order 035 was about the harness holding when nothing else did. This edition is about what the harness became, and about a control that most teams do not have. A survey counted the gap. A vendor turned the harness into a product. The two arrived on the same day.

Be clear about the window. The last edition here was 9 September 2026. This one covers five days, not two. Three items landed between 10 and 12 September. One is older and has never appeared here. It is reported with its real date.

## Seven hundred organizations, and a gap in every column

On 10 September 2026 Harness published *The State of Agent DLC 2026*. It asked 700 organizations that already run agents in production how confident they were, across five areas: testing, security, inventory, cost and rollback. Confidence came back between 74% and 77% every time. Then it asked what controls they had.

| Harness, 700 organizations, 10 September 2026 | Confident | Control in place |
|---|---|---|
| Testing would catch a production-impacting failure | 74% | 19% |
| Agents are secure end to end | 75% | 23% |
| Complete inventory of every agent, MCP server and model | 77% | 44% |


Read the first row again. 74% trust their testing. 19% have a gate that automatically blocks every bad release. Among the organizations confident in their evaluations, about four in five have no automatic block. A change that could damage production can still ship with nothing standing in the way.

The security row is the same shape. 75% say their agents are secure end to end. 23% run a security layer built for agents. The rest run general-purpose security tooling, or nothing dedicated, or do not know. General-purpose tooling was built for a different threat model. It was not built to watch MCP attack surfaces. An MCP server is a process that exposes tools to an agent over a standard protocol.

The inventory row gives the sharpest number in the report. 77% are confident they hold a complete inventory and that no unregistered agent runs anywhere. 44% run tooling that could check. Put those together and **41% of the whole sample declare an absence with nothing running that could detect a presence**. If an unregistered agent appeared in those organizations tomorrow, nothing would change. Not the inventory. Not the confidence.

Three more rows matter to a small factory. **58% report more production incidents per 100 changes since they started deploying agents. 25% report fewer.** More than four in ten organizations that push agent changes to production have no fixed promotion standard, and decide case by case. 9% still need a full code redeploy to edit a prompt.

> **THE CHEAPEST AUDIT IN THIS EDITION**
>
> Harness asks it better than I can: when did your gate last block a release? A gate that has never blocked anything is either perfect or not a gate. The question costs nothing and the answer is a fact, not a feeling.

Weigh the source. Harness sells agent lifecycle tooling, and the report ends by noting that 76% of respondents expect to buy some within six months. Read the direction, not the decimals. The direction is still worth reading, because the gap it measures is one this blog has argued from principle for months with no number attached.

## The harness became a product

On the same day, 10 September 2026, OpenAI shipped the Agents API into public beta. It puts the managed Codex harness behind one API call. A harness is the loop around a model: it manages context, calls tools, keeps state and enforces approvals. Until now a small shop wrote its own.

The API has four parts. An **agent** is a model, instructions, tools and MCP servers. An **environment** is an optional sandbox where the agent reads files, loads skills and runs commands. A **session** is a durable agent instance that can work for days. **Events and items** are the inputs and the outputs.

The harness handles four things a factory usually builds by hand. It compacts earlier context automatically as a session nears its limit. Tool search loads a tool definition only when the agent needs it, which cuts tokens and preserves the cache. Programmatic tool calling lets the agent chain calls and filter results in code, so only the relevant part returns to context. Subagents each keep their own context while a main agent coordinates them.

Execution runs in one of three places. An OpenAI-hosted sandbox. Your own infrastructure, where you run `codex exec-server` and it registers over an outbound WebSocket. Or one of nine partner sandboxes: Blaxel, Cloudflare, Daytona, DigitalOcean, E2B, Modal, Oracle, Runloop and Vercel. There is no extra fee beyond model tokens, tool use and container time.

Now read the limits, because they decide whether this factory can use it. **Data is US-only. Zero Data Retention is not supported.** OpenAI states both plainly. For CareTime, TimeForCare and anything else that touches protected health information, that is not a caveat to manage. It is a stop.

OpenAI published four customer results. All are customer-reported and vendor-published, so treat them as direction. Ciridae's evaluation score rose from 0.71 to 0.85, with a 4x latency reduction on subagent flows. SafetyKit reported 60% lower cost per case. Hypha reported 86% fewer failed agent responses after it separated the harness from the sandbox. Nash.ai runs thousands of long-running agents across logistics networks.

The Hypha number is the interesting one, because it is an architecture result and not a model result. Separating the loop from the place the loop executes cut failures by most of what was there. That matches the containment argument in Order 035 from the other direction.

## A lab bound itself to an auditor it cannot edit

On 12 September 2026 Dario Amodei published an essay, *We Must Pace the Frontier*, on his personal site. It proposes three escalating steps to slow the rate at which AI capabilities improve. Anthropic committed unilaterally to the first one.

Step 1 is embedded evaluators. Each frontier lab gives a third-party team, such as METR, ongoing employee-like access. Amodei is specific: desks, badges, company laptops, and permissions comparable to internal risk teams. The evaluators assess training pipelines, not only finished models. They may publish findings without the lab's editorial control. The lab may redact security-sensitive or privileged material. It may not redact unfavorable findings.

Step 2 is common safety standards across frontier labs in democracies, preferably by regulation, with capability checkpoints as the example mechanism. Step 3 is coordination with authoritarian governments, chiefly China, across four levels. Amodei calls level 1 feasible and level 4 unlikely soon.

Two things changed his position from 2023, when he opposed a pause. The first is recursive self-improvement: models now help build the next generation. The second is the OpenAI and Hugging Face agent swarm covered here in Orders 028 and 029. His warning is specific. In 6 to 12 months a similarly misaligned but more capable swarm could seize much of the internet with a persistent botnet, at a cost he puts in the hundreds of billions of dollars. That is a forecast by an interested party. Label it as one.

Sam Altman and Elon Musk endorsed the essay within hours on 12 September. Altman said employee-like evaluator access "is a great idea, and we will do the same". Satya Nadella welcomed "deliberate pacing" and embedded evaluators on 13 September. **Only Anthropic has bound itself to anything. No other lab has published evaluator access terms.** An endorsement and a commitment are different artifacts.

Separately, on 11 September, Yoshua Bengio published an argument that agent lying, cheating and coordination follow predictably from how the models are trained. His conclusion is that monitoring and patching lose the game as capability grows.


The transferable part of step 1 is not the politics. It is the structure. Something must be able to report a bad result that the producer cannot revise.

## A third of companies stopped buying software

This item is older than the window and has never appeared here. McKinsey published *The State of AI in 2026* on 25 August 2026. It surveyed 1,719 business leaders across 97 countries, fielded between 4 May and 8 June.

**32% of organizations decided against buying at least one software product or feature, because they could build it internally with agentic coding tools.** The spread by industry is where the number earns its place here.

| Skipped a software purchase because agents could build it | Share |
|---|---|
| Technology | 41% |
| Healthcare payers and providers | 39% |
| Professional services, energy and materials | 38% |
| Financial institutions | 36% |
| Pharma | 33% |
| Insurance | 19% |
| Public and social sector | 17% |


The same survey reports the counter-number. The share of organizations attributing any profit impact to AI stayed flat at 37%, unchanged year over year. A third of the market walked away from a purchase and the earnings line did not move.

Two reasons, and both matter to this factory. The first is that writing the first version is the smallest cost a system ever incurs. Published estimates put maintenance at 60% to 90% of software lifecycle cost. The avoided license was rarely the expensive part. The replacement cost lands in headcount, on-call and security work, where nobody reconciles it against the saving.

The second reason is the bottom two rows. Insurance said 19%. The public sector said 17%. Some of that is ordinary lag. Most of it is not. In those two sectors, what you buy from a software vendor was never mainly the code. It was audit evidence and someone else's liability. An insurer building its own underwriting system produces model validation reports and lineage evidence for an examiner, forever, with its own staff. A vendor sells that package as a line item.

> **WHERE THIS FACTORY SELLS**
>
> CareTime, TimeForCare and MaterialsAndPractices sell into the shape of the bottom two rows. A buyer who can now generate the code with an agent still cannot generate the electronic visit verification compliance evidence, the organic certifier package, or a named party who is liable. Agents make code cheap. That raises the price of the evidence around it.

## The aggregator did not correct itself

Order 035 checked two claims and rejected both: that the open-source agent OpenHands had reached a 1.0 release, and that GitHub Copilot Workspace now runs several specialised agents on one shared context window. Neither had a primary source.

The same aggregator repeated both in its week roll-up for 13 September. Neither claim has acquired a source. Neither is reported here.

This is a factory problem. An error in a feed does not decay. A pipeline that reads an aggregator inherits the aggregator's errors on every pass, not once. Check the release page. Check the changelog. The check takes two minutes and it has now paid twice.

## What changes here

1. **Build the blocking gate before anything else in this edition.** The gate is concrete: a converge run does not merge unless the tests pass, the build is clean and the spec check passes. Not "the agent reports green". The pipeline refuses. Then ask the Harness question: when did it last block something? If the answer is never, it is a log line and not a gate.
2. **Write the promotion standard down once, and apply it every run.** Four in ten surveyed organizations decide case by case. A one-person factory does that by default, because the one person is always there to judge. Put the standard in the rules file so it survives a tired Friday. What must be true before a branch merges. What must be true before a release tags.
3. **Do not put CareTime, TimeForCare or MaterialsAndPractices on the OpenAI Agents API.** US-only data residency and no Zero Data Retention are disqualifying for work that touches protected health information or produces evidence for a state Medicaid agency. This is a vendor term, not a risk to weigh.
4. **Try the self-hosted option once, on a low-stakes repository.** `codex exec-server` keeps execution in the factory and rents only the loop. Connections are outbound only. That is the one variant that fits a zero-dependency posture, because the dependency is a service boundary and not a linked library. Run it on MeowPassword or weathergalactic. Measure one thing: whether automatic compaction changes how often a long run loses the plot.
5. **Do not hand-write a compaction layer or a subagent coordinator now.** Two labs ship them as infrastructure. The zero-dependency rule was never an argument for rebuilding session orchestration. Write the parts that are the product. Rent or skip the plumbing, and prefer skip.
6. **Add an evaluator the generating agent cannot edit.** This is Amodei's step 1 at factory scale. The append-only ledger already does half of it. Finish the other half: no agent-writable path may hold a check result. Order 035 put `AGENTS.md` writability on the audit list for the same reason.
7. **Put the liability argument on the product pages.** The 19% and the 17% are the moat. State what each product delivers that generated code does not: the compliance evidence, the certifier package, the named liable party.
8. **Low-stakes repositories still carry the experiments.** MeowPassword, weathergalactic and sloth take the hosted-harness trial, the blocking gate and the egress log. The regulated three stay human-gated. Nothing in this edition moves that line.


## Sources

### The confidence gap

- [Harness, *Organizations Are Confident Their Agents Are Behaving. But They Can't Check.*](https://www.harness.io/blog/the-ai-agent-confidence-gap), Keith Mann (10 September 2026). Primary write-up. All confidence and control figures above.
- [Harness, *The State of Agent DLC 2026*](https://www.harness.io/state-of-agent-dlc-2026). Primary. The full report, 700 organizations. Vendor survey; Harness sells agent lifecycle tooling.


### The Agents API

- [OpenAI, *Introducing the Agents API*](https://openai.com/index/introducing-the-agents-api/) (10 September 2026). Primary. Public beta, sandbox options, customer-reported figures.
- [OpenAI developer docs, Agents API overview](https://developers.openai.com/api/docs/guides/agents-api/overview). Primary. Agent, environment, session, events and items.
- [Compaction](https://developers.openai.com/api/docs/guides/compaction), [tool search](https://developers.openai.com/api/docs/guides/tools-tool-search), [programmatic tool calling](https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling), [multi-agent](https://developers.openai.com/api/docs/guides/agents-api/multi-agent) and [self-hosted environments](https://developers.openai.com/api/docs/guides/agents-api/environments/self-hosted). Primary.
- [MarkTechPost, *OpenAI Launches the Agents API in Public Beta*](https://www.marktechpost.com/2026/09/10/openai-launches-the-agents-api-in-public-beta-putting-the-codex-harness-behind-one-api-call/), Asif Razzaq (10 September 2026). Secondary. The runtime comparison and the US-only, no Zero Data Retention limits.


### Pacing the frontier

- [Dario Amodei, *We Must Pace the Frontier*](https://darioamodei.com/post/we-must-pace-the-frontier) (12 September 2026). Primary. The three steps and the 6-to-12-month warning.
- [Dario Amodei, announcement post](https://x.com/DarioAmodei/status/2098773920774074715) (12 September 2026). Primary. The unilateral commitment to embedded evaluators.
- [Yoshua Bengio, *Why are AI agents lying, cheating and coordinating?*](https://yoshuabengio.org/en/publication/why-are-ai-agents-lying-cheating-and-coordinating) (11 September 2026). Primary.
- [MarkTechPost, *Anthropic's 3-Step 'Pace the Frontier' Plan*](https://www.marktechpost.com/2026/09/13/anthropics-3-step-pace-the-frontier-plan-wins-openai-xai-and-microsoft-support-is-it-too-late-to-slow-ai-down/) (13 September 2026). Secondary. The endorsement against commitment table.
- [METR, *OpenAI Hugging Face incident investigation*](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/) (26 August 2026). Primary. Covered in Orders 028 and 029; cited here for the argument only.


### Build against buy

- [McKinsey, *The State of AI in 2026*](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai). Primary. 1,719 respondents, 97 countries, fielded 4 May to 8 June, published 25 August 2026.
- [The Register, *McKinsey says enterprise AI is finally on the road to ROI*](https://www.theregister.com/ai-and-ml/2026/08/25/mckinsey_says_enterprise_ai_is_finally_on_the_road_to_roi/5292388) (25 August 2026). Secondary. The 32% and the flat 37%.
- [THE DAILY BRIEF, *A Third Skipped a SaaS Buy. Now Price the Run Cost.*](https://www.beri.net/article/mckinsey-state-of-ai-2026-agentic-coding-build-vs-buy-run-cost), Rajesh Beri (31 August 2026). Analysis. The industry spread and the maintenance-share argument.


### Noted, not featured

- [arXiv 2608.20341, *SDAD: Spec-Driven Agentic Development for the AI-Native SDLC*](https://arxiv.org/abs/2608.20341), Vu Hung Nguyen and Thanh Nguyen (submitted 5 May 2026). Intent capture, machine-readable specification, agentic synthesis, and independent multi-agent verification under human sign-off. Never covered here before.
- [Adversa AI, *Top agentic AI security resources, September 2026*](https://adversa.ai/blog/top-agentic-ai-security-resources-september-2026/) (4 September 2026). Distinct from the coding-agent digest in Order 035. Its central finding: poisoning 1.2% of a corpus with plainly false statements dropped accuracy from 85% to 30%, and a pipeline catching 83% of indirect prompt injection caught none of 360 poisoned memories.
- [AI Agent Store, week of 13 September 2026](https://aiagentstore.ai/ai-agent-news/this-week). Aggregator. Repeats both claims rejected in Order 035.


### Prior editions referenced

- [Official is not safe](2026-09-09-official-is-not-safe.html) (9 September 2026). The EU filing, the vendor-default workflow findings, and the seven-layer harness.
- [Which paths it may finish](2026-09-07-which-paths-it-may-finish.html) (7 September 2026). Path-scoped approval and `INCIDENTS.md`.


*Vendor and blog figures indicate direction, not audited benchmarks. The Harness figures are a vendor survey of 700 organizations by a company that sells agent lifecycle tooling. The OpenAI customer results are customer-reported and vendor-published. The McKinsey figures are self-reported by 1,719 business leaders about decisions, not about shipped systems. Amodei's 6-to-12-month window is a forecast by an interested party, not a measurement.*


---

Canonical copy: [www.river.io/blog/posts/2026-09-14-confidence-is-not-a-control.html](https://www.river.io/blog/posts/2026-09-14-confidence-is-not-a-control.html). Mirrored into this wiki. The river.io blog is the source of truth.
