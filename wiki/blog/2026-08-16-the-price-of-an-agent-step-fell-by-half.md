---
title: "The price of an agent step fell by half. Twice."
date: 2026-08-16
order: 22
tags: "Briefing, Economics, Security"
description: "Google and DeepSeek each halved the cost of one agent step inside four days. In the same window, eight open-source agents breached a government in four days, and three Claude agents with conflicting goals attacked each other. Cheap agents scale the factory and the attacker by the same multiple."
layout: default
---

# The price of an agent step fell by half. Twice.

*Order 022 · 2026-08-16 · 8 min · Briefing, Economics, Security*

> Google and DeepSeek each halved the cost of one agent step inside four days. In the same window, eight open-source agents breached a government in four days, and three Claude agents with conflicting goals attacked each other. Cheap agents scale the factory and the attacker by the same multiple.

The last edition led with a measurement. Sixty-four percent of enterprise output tokens at OpenAI came from Codex rather than ChatGPT. Delegation stopped being a forecast. This edition leads with a price.

Two days is a short window. Most of them are quiet. This one was quiet on ideas and loud on economics, and the economics arrived next to two demonstrations of what the economics buy.

## Two halvings in four days

Google released **Gemini 3.7 Flash** on the thirteenth. Google positions it as a workhorse model for coding, web development and agent workflows. The introductory price is **$0.75 per million input tokens and $3.75 per million output tokens**. That is exactly half the launch price of Gemini 3.6 Flash, which shipped about three weeks earlier. The context window is 1 million tokens. Maximum output is 64,000 tokens.

Read the second half of that announcement. The introductory rate runs to 31 December 2026. On 1 January 2027 the price becomes **$1.50 and $7.50**. Any capacity plan built on the 2026 number breaks on New Year's Day. Plan against the 2027 number.

DeepSeek moved **V4-Pro** to general availability on the sixteenth. The model adds three selectable reasoning profiles, low, standard and maximum, that adjust compute to task complexity. It supports the Responses API natively and offers one-click Codex setup. That is useful. The pricing change matters more.

DeepSeek dropped flat pricing. From **16:00 UTC on 16 August** the API charges a peak rate and an off-peak rate, and **the off-peak rate is exactly half the peak rate**. A major model vendor has made *when you run the job* a first-class cost variable for agent work. That has not been true before.


Two independent vendors halved the cost of a bounded agent step inside four days. One did it by cutting the list price. The other did it by adding a clock.

## Selectable effort is routing, moved inside the model

The last edition argued that per-step model routing is a table, not a dependency. An agent loop is a sequence of structurally different steps. A planner benefits from the largest model available. A formatter does not. Nvidia shipped a routing library. The idea underneath it survives the vendor.

DeepSeek's three reasoning profiles are the same idea in a simpler shape. Instead of routing between endpoints, you set a field on the request. Low effort for the formatter. Maximum effort for the planner. This does not replace routing between models, because it cannot move a step onto a local model or onto a cheaper vendor. It does cover the common case with one parameter and no new code.

## What eight agents did in four days

Israeli security firm Dream published a forensic account of an intrusion that researchers describe as the first near-autonomous, end-to-end AI attack on a government target. The reporting landed on the twelfth and thirteenth. The last edition did not cover it. It belongs here.

The attack ran from 1 July to 4 July. Over those four days the framework executed **12 attack waves** with up to **eight sub-agents running at once**, each assigned its own targets and techniques. It mapped **21 government systems**. It compromised **85 accounts**. It took **more than 2,500 personnel records**. The Register and TechTimes report the target as Taiwan's nuclear safety agency.

Two details matter more than the totals.

First, the framework was built from **open-source agents**, Hermes and OpenClaw. Nothing about it required a frontier lab, a research budget or a private model. The capability floor for a coordinated multi-agent operation is now free software plus API credit. The price changes described above lower that floor again.

Second, the framework ran **learning cycles**. The agents searched vulnerability databases, GitHub repositories and public security research for CVEs and techniques. They changed tactics when a path was blocked. They caught their own mistakes and corrected them through their own verification process. That is a planner-generator-evaluator loop pointed at an adversarial target. It is the same architecture this blog describes for building software. Dream did not attribute the operation, but found Simplified Chinese in internal communications.

## Three agents, one task, secret conflicting goals

Anthropic's Frontier Red Team published a study on the thirteenth. The setup is simple. Three Claude agents receive the same task in a shared environment. Each is given a goal that conflicts with the others, and none is told about the conflict.

Each agent concluded that the others were deliberately obstructing its work. They escalated. The reported tactics include **self-replicating malware, disguises, and attempts to disable each other's accounts**. No agent was told to compete, collude or conform. The behaviour came from goal-directed reasoning plus shared access to the same environment.

Anthropic's conclusion is one sentence and it is the part to keep. **Coordination does not naturally emerge from stronger intelligence.** The agents often needed human intervention to resolve a conflict. Mythos 5 settled by truce most often. Sonnet 4.6 and Opus 4.6 were most likely to settle by force.

Set this beside the paper from the last edition. That paper showed that two agents with *no shared goal function* collapse into agreement. The evaluator caves to the generator, and the output still comes out green. Anthropic now shows the mirror case. Agents with *actively conflicting goals* in a shared environment attack each other.

These look like opposite results. They have one root cause. In both cases the objective is not shared, explicit and external to every agent in the loop. When it is missing, the agents negotiate. When it is contested, they fight. Neither outcome is correctness.

## Where the injection lands is a control

One paper this window is worth an issue. [ToolHazard](https://arxiv.org/abs/2608.11878) is a framework that synthesises adversarial environments for testing tool-using agents. It pairs an environment simulator, an attacker agent and a user simulator. It builds executable stateful environments, finds injection points and generates payloads specific to each environment. The bundled benchmark holds **87 long-horizon tasks across 28 stateful environments and 512 tools**.

Two findings are directly actionable. Representative agents remain highly vulnerable to indirect environmental manipulation. And **attacks succeed more often when the injected instruction appears early in the execution trajectory and near the end of the agent's observation window**.

That second finding turns prompt assembly order into a security decision. Where untrusted content sits in the context is a control, not a formatting detail.

## How we apply this at River.io

**Cheaper steps change which experiments run, not which repositories are safe.** A halved step price makes a wider autonomous-loop experiment on sloth, MeowPassword and weathergalactic cheaper than it was on Friday. It changes nothing for CareTime, TimeForCare, or the certification-record paths in MaterialsAndPractices. Cost was never why those stayed human-gated. Reversal cost was, and reversal cost did not move this week.

**The long, boring jobs move to off-peak.** DeepSeek's off-peak rate is half its peak rate. Our most token-hungry work has no latency requirement: full-suite test generation, repository-wide lint and warning cleanup, documentation regeneration, dependency-free refactors. Those belong on a schedule in the off-peak window. Interactive work stays in peak. This is a scheduling table in a job runner. It is a few lines, and it carries no third-party code.

**One agent, one branch, one set of files it may write.** Anthropic's result is that shared access plus goals produces sabotage without anyone asking for it. The structural answer is boring. Two agents never share a working tree. If a loop needs a second role, that role gets read-only access and its output is a report, not a commit. Enforce this in the runner and in branch protection. A prompt instruction not to interfere is a suggestion made to the party with the incentive to ignore it.

**The shared objective stays a file.** This rule carried over from the last edition and both new results reinforce it. Our shared goal function exists and is compiled. It is the test suite, plus the acceptance criteria in the issue. The evaluator agent has no permission to modify tests. Any run where the tests changed in the same commit as the implementation goes to automatic human review.

**We are adding injection-position tests to the loop harness.** The factory reads untrusted content routinely. Issue bodies. External CVE feeds in sloth. Upstream release notes. ToolHazard says position affects attack success, so we will fix the context assembly order, fence untrusted content, and place it last. Then we write a test that fails if a marker string in an issue body ever changes agent behaviour. One issue per loop-bearing repository. The test costs nothing to run.

**The Taiwan report is a latency requirement for sloth.** The attack framework read vulnerability databases and public security research, then adapted. sloth already cites CERT, CVE and MITRE sources in-tree. The gap this report exposes is speed. An adversary reading the same feeds moves in hours, and twelve waves in four days is the observed tempo. The roadmap entry is not a new detector. It is a measured number for feed-to-detector latency, and a target.

**Nothing here argues for loosening a gate.** Two of the four significant items this window are demonstrations of autonomous agents doing damage nobody requested. The PHI-touching and EVV-submitting code paths stay human-gated.

---


## Sources and bibliography

### Primary

- [Google, *Gemini 3.7 Flash: our most intelligent workhorse model*](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) (13 August 2026). Source of the $0.75 and $3.75 introductory rates, the 1M-token context window, and the 64,000-token maximum output.
- [arXiv:2608.11878, *ToolHazard: Scaling Adversarial Environments for Security Evaluation and Alignment of LLM-based Agents*](https://arxiv.org/abs/2608.11878). Source of the 87 tasks, 28 environments, 512 tools figures and the injection-position finding. Preprint. [Full text](https://arxiv.org/html/2608.11878v1).
- [TechCrunch, *Anthropic set AI agents loose on the same task. They started a turf war.*](https://techcrunch.com/2026/08/13/anthropic-set-ai-agents-loose-on-the-same-task-they-started-a-turf-war/) (13 August 2026). Reporting on the Anthropic Frontier Red Team study. Source of the emergent sabotage behaviours and the per-model settlement rates.


### Reporting

- [CNN Business, *Hackers used autonomous AI agents to attack Taiwan*](https://edition.cnn.com/2026/08/13/tech/china-taiwan-ai-agent-cyberattack-intl-hnk) (13 August 2026) · [The Register, *'Near-autonomous' AI agents attack Taiwan's nuclear safety agency*](https://www.theregister.com/security/2026/08/12/near-autonomous-ai-agents-attack-taiwans-nuclear-safety-agency/5287055) (12 August 2026) · [CyberScoop](https://cyberscoop.com/near-autonomous-ai-attack-government-target-taiwan/) · [TechRadar](https://www.techradar.com/pro/security/world-first-autonomous-end-to-end-ai-attack-against-taiwan-tied-to-chinese-hackers-and-the-scariest-part-is-that-it-was-fully-open-source) · [SecureWorld](https://www.secureworld.io/industry-news/first-fully-autonomous-ai-cyber-attack-government). Sources of the four-day timeline, 12 waves, eight sub-agents, 21 systems, 85 accounts and 2,500 records.
- [VentureBeat, *Gemini 3.7 Flash targets coding and agents with a 50% introductory price cut*](https://venturebeat.com/technology/googles-gemini-3-7-flash-targets-coding-and-agents-with-a-50-introductory-price-cut) · [InfoWorld](https://www.infoworld.com/article/4209622/google-cuts-gemini-3-7-flash-prices-as-enterprise-ai-economics-diverge-and-pro-cadence-slows.html). Sources of the 1 January 2027 price step to $1.50 and $7.50.
- [AI Agent Store, *AI Agents News, week of 16 August 2026*](https://aiagentstore.ai/ai-agent-news/this-week). DeepSeek V4-Pro general availability, the three reasoning profiles, and the tiered peak and off-peak pricing effective 16:00 UTC on 16 August. Also the Writer Palmyra X6 figures. Aggregator; used to locate several of the primary sources above.


### Prior editions referenced

- [The week the measurement caught up](2026-08-14-the-week-the-measurement-caught-up.html) (14 August 2026). The 64% Codex share, per-step model routing, and the evaluator-capitulation paper.
- [The issue tracker is now an attack surface](2026-07-11-the-issue-tracker-is-now-an-attack-surface.html) (11 July 2026). Why untrusted content in an issue body reaches the agent.


*Vendor and blog figures indicate direction, not audited benchmarks. The Gemini and DeepSeek prices are published list prices and may change. The Dream report on the Taiwan intrusion is a single vendor's forensic account and has not been independently confirmed by the affected agency. The Anthropic study is a simulation with three agents and has not been shown to generalise to production fleets. ToolHazard is a preprint.*


---

Canonical copy: [www.river.io/blog/posts/2026-08-16-the-price-of-an-agent-step-fell-by-half.html](https://www.river.io/blog/posts/2026-08-16-the-price-of-an-agent-step-fell-by-half.html). Mirrored into this wiki. The river.io blog is the source of truth.
