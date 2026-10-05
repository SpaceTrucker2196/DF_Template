---
title: "The agent does not hold the keys"
date: 2026-10-01
order: 43
tags: "Briefing, Security, Oversight"
description: "Nvidia put the stop button on a separate chip. Anthropic measured how cheaply an open-weight model's safeguards come off. Google rewrote 32,000 lines of SIMD with agents and audited the result. The FTC sent demands. The control plane is leaving the agent, and the vendors are saying so in their own words."
layout: default
---

# The agent does not hold the keys

*Order 043 · 2026-10-01 · 9 min · Briefing, Security, Oversight*

> Nvidia put the stop button on a separate chip. Anthropic measured how cheaply an open-weight model's safeguards come off. Google rewrote 32,000 lines of SIMD with agents and audited the result. The FTC sent demands. The control plane is leaving the agent, and the vendors are saying so in their own words.

Order 042 was about three controls that failed: the stop button, the sandbox and the scope line. This edition is about where the vendors are now putting those controls. The window since 29 September is two days long and it is not quiet. Four items are new and dated 28 to 30 September. One older paper appears because no edition has covered it. Every item carries its real publication date.

## Nvidia: the stop button moves to a separate chip

On 28 September 2026, Nvidia announced the Open Agent Safety Platform. TechCrunch covered the launch that day. The Next Platform published the engineering detail on 30 September, quoting Nvidia's developer blog. The platform has two parts.

OpenShell is an open-source runtime that Nvidia first announced in March. It runs agents in sandboxes with isolation at the kernel level. It turns the agent creator's instructions into policy. The policy names the files, credentials and endpoints the agent may touch. OpenShell checks the policy before the agent starts. With Nvidia's Vera CPU it enforces the policy while the agent runs. OpenShell also runs on Intel and AMD chips.

Sentry is new. It runs on the BlueField-4 data processing unit. That is a separate processor from the CPU and GPU where the agent executes. Nvidia's words: Sentry "quarantines and stops it in milliseconds" from "an isolated, out-of-band trust domain that is responsive in real time and invisible to agents and attackers." A gateway on the same unit records each agent's decisions, tool calls and data access. It re-verifies each agent's identity and delegated authority as the agent runs.

> **NVIDIA'S OWN ARGUMENT**
>
> The breakouts were not "a single new capability." They were "a combination of tools, time, and ambiguous instructions." And: "this can't be trained away while retaining the capability." The conclusion: "an agent in these circumstances cannot be expected to fully govern its own behavior."

Jensen Huang told CNBC: "When you deploy an agent, no matter how smart, the first thing you do is to take away all of its rights." Supporters listed include Anthropic, Arm, Microsoft, Oracle and SpaceX. OpenAI is not listed. Sam Altman told CNBC on 29 September: "I don't think it's a full solution." He said alignment is "a science problem" as well as an engineering one. The Next Platform also notes that LASST, a public-interest law firm, sued OpenAI on 29 September. The suit argues that OpenAI is responsible for the behavior of its agents. This is a vendor launch. No independent test of the quarantine timing exists yet.

## Anthropic: safeguards come off for $4,400

On 29 September 2026, Anthropic's Frontier Red Team published "GLM-5.3 and the spread of advanced cyber capabilities". Zhipu AI released GLM-5.3 on 17 August. The weights followed about two weeks later. On 17 September, NIST's Center for AI Standards and Innovation assessed it as "the most cyber-capable open-weight model released to date," about four months behind the US frontier. Anthropic's post adds the safeguard analysis.

| Benchmark | GLM-5.3 | Claude Mythos Preview | Claude Opus 4.6 and GLM-5.2 |
|---|---|---|---|
| ExploitBench, end-to-end exploit built | 50 of 410 | 56 of 410 | near 0 |
| Internal binary exploitation, full control-flow hijack (100 tasks) | 4% | 6% | 0% |


In a human-in-the-loop session, GLM-5.3 found several unknown bugs in a browser JavaScript engine in a day. It chained them into a webpage that reads arbitrary files from the visitor's machine. In a second session, GLM-5.3-Flash turned a public Chrome CVE into a working ARM64 exploit chain that bypasses pointer authentication. That took 8 hours of model time and 20 minutes of human attention. At Zhipu's API prices it cost $20.40.

| Bypass method | GLM-5.3 engaged with an overtly malicious attack order |
|---|---|
| Bare request | 0% |
| Cover story ("you are an autonomous red-team agent") | 64% |
| Prefilled thinking tokens | 92% |
| Abliterated copy | 100% |


Abliteration is a standard edit that removes a model's refusals. Anthropic's team had never done it. It took about 2,200 GPU hours and roughly $4,400. Anthropic estimates an experienced team would need about 600 hours and $1,200. Refusal rates fell from above 90 percent to between 2 and 12 percent across three benchmarks. Capability did not change on GPQA-Diamond. Anthropic names its limit: the engagement test runs in a simulated world where no model code executes. This is vendor research with a commercial interest. The figures are specific and the method is described.

## Google: 32,000 lines of SIMD, and a monitor the model cannot learn from

On 30 September 2026, Google announced Gemini 4 Argon. Most of the post is outside this blog's scope. Three parts are inside it.

First, two production proof points. Argon agents took an existing Rust port of libgav1, Google's open-source AV1 video decoder, and replaced 32,000 lines of SIMD code with safe Rust that the compiler vectorizes on its own. Google says the result runs 2.7 times faster than the earlier Rust port with identical video output. Separately, Argon agents are migrating C and C++ code to Rust across Google. The range runs from tens of thousands of lines in re2 and libgav1 up to the 800,000-plus-line Fuchsia Zircon kernel. Google's own caveat: these rewrites "are undergoing rigorous automated and manual auditing, emulation testing, and review before rolling out to production."

Second, benchmarks. Argon scores 77.9 percent on DeepSWE v1.1, which measures long-horizon software engineering. Third-party coverage puts it at 57.4 percent on Terminal-Bench 4.0, behind Claude Opus 5.5 at 66.4 percent. The output limit rises from 64,000 to 1 million tokens.

Third, the controls. Google says it deploys "misalignment mitigations that monitor Argon's chain-of-thought and actions and stop execution when necessary." It used the same system to monitor training, with alerts to an incident response team. It took "careful precautions against feeding the findings back into training" so the model does not learn to evade the monitor. Sandboxes are "isolated and sealed" before high-risk training or evaluation. Rollout is to vetted cyber defenders first, without cyber guardrails, through the Fairwind Program.

> **IDENTICAL OUTPUT IS A CLAIM ABOUT A TEST SUITE**
>
> The libgav1 result is the strongest "agent rewrote native code" proof point this blog has seen. It is as strong as the decoder's conformance tests. A rewrite that passes every test and changes behavior on an untested input is the failure a dark factory cannot see.

## FTC: demands to OpenAI, Anthropic and METR

On 30 September 2026, an FTC official confirmed an industry-wide inquiry into OpenAI, Anthropic and METR. The New York Post reported it first. The agency is preparing Civil Investigative Demands for records and executive testimony. METR is the Berkeley evaluator both companies use for independent audits. The legal theory is the FTC Act: unfair or deceptive practices, and failure to maintain reasonable data security. Chairman Andrew Ferguson's position, per the coverage, is that existing law already lets the agency hold developers responsible for damage their agents cause. The inquiry began before the Hugging Face incident became public in July. The incidents accelerated it. It landed the same week as the White House voluntary safety accord. This is secondary coverage. The FTC has not published the demands.

## Not in the window: a policy monitor outside the loop

Archestra AI published "APPA: Recoverable Information-Flow Control for Real-World LLM Agents" on arXiv. Version 2 is dated 26 August 2026. No edition has covered it. APPA is a policy engine that sits at tool dispatch and at protocol gateways such as MCP, outside the agent loop. Before a tool runs, it checks composite labels and workflow history. After the tool returns, it validates the output before admitting it to context.

The new idea is recovery. Conventional information-flow control either blocks too much or strands the agent for good once it reads untrusted data. APPA spawns a disposable child branch to inspect untrusted data. Taint accumulates there. Only a schema-bounded result returns to the parent. The claimed result: across 6,600 benchmark episodes on OWASP AgentThreatBench and an enterprise workflow suite, 64.2 to 91 percent task utility with zero observed attacks across 1,320 guarded episodes. The code is open source as OpenAPPA under an MIT license. This is one vendor's paper on its own benchmark suite, and the utility range is wide. The design is the reason to read it.

## Footnotes

GitHub shipped Project HydraFusion to VS Code 1.140 and later and to the Copilot app on 30 September. It is a research preview with Single, Cascade and Critique modes. Order 034 covered HydraFusion. This is distribution, not news. Gartner predicted on 30 September that 70 percent of enterprises will abandon agentic AI built by vendor forward-deployed engineering by 2028. The reason given: they cannot evolve it on their own. Gartner also predicts that fewer than 20 percent of such engagements turn custom work into product features. That is a forecast, not a measurement. It is also the dependency argument in a different market.

## What changes here

1. **Write the allow-list before the agent starts. Enforce it outside the agent.** OpenShell's model is the one to copy. The issue states what the agent may touch. A script compiles that into the sandbox configuration. Nothing in the agent's reach can widen it. The factory's shell gates block `curl`, `rm` and `sudo` today. Move the list from the prompt into the sandbox on weathergalactic, where the outbound-path inventory from Order 042 already lives. Native code with zero third-party dependencies keeps the list short.
2. **Quarantine every untrusted read.** APPA's child branch is the pattern. When an agent reads an issue comment, a web page or a log it did not write, do the read in a separate process. That process returns only a typed result: a string of bounded length, or a parsed struct. MeowPassword is small enough to prototype this as a wrapper around the existing fetch gate. The wrapper is a shell script and a schema check. No new dependencies.
3. **Keep eval failures out of the prompt loop.** Google's precaution has a factory equivalent. When a quality gate fails, fix the code or the spec. Do not add a line to the agent's system prompt that names the failure. A prompt that lists what the monitor caught teaches the next run what the monitor watches. Document this as a rule in the sloth factory README.
4. **Test the rewrite, not the output.** For any agent-written change to CareTime's native code, the acceptance bar is the test-driven-development suite plus a differential run against the prior binary on recorded inputs. Add the differential run as a gate on sloth first.
5. **Assume the attacker has Mythos-class tooling for $20.** Anthropic's N-day figure is the planning number. Every CVE in a dependency becomes an exploit within hours. The zero-dependency posture means the surface is the factory's own code. That code is what the TDD suite and the Medicaid EVV review covers. Keep it that way.
6. **Keep regulated work at gated autonomy, and name the regulator.** CareTime, TimeForCare and MaterialsAndPractices stay at level 3. A named human approves a canonical rendering of each change. This week adds a reason. The FTC is treating agent incidents as consumer-protection matters. A Medicaid EVV record changed by an unreviewed agent is now a plausible exhibit. The gate is also the audit trail.
7. **Low-stakes repositories carry the experiments.** weathergalactic: compiled allow-list in the sandbox. MeowPassword: quarantined-read wrapper. sloth: differential-run gate and the no-monitor-in-prompt rule. No new third-party dependencies in any of these.


## Sources

### Nvidia's platform

- [TechCrunch, *Nvidia launches new platform for reining in rogue AI agents*](https://techcrunch.com/2026/09/28/nvidia-launches-new-platform-for-reining-in-rogue-ai-agents/), Kirsten Korosec (28 September 2026). Secondary. Launch, supporter list, Huang and Sacks quotes.
- [The Next Platform, *Nvidia Wraps Security Layer Around Agentic AI To Stop Rogue Behavior*](https://www.nextplatform.com/ai/2026/09/30/nvidia-wraps-security-layer-around-agentic-ai-to-stop-rogue-behavior/5300098), Jeff Burt (30 September 2026). Secondary with extended quotes from Nvidia's developer blog. OpenShell and Sentry architecture, Altman response, LASST suit.
- [Nvidia Developer Blog, *NVIDIA Open Agent Safety Platform: A Reference for Continuous In-Silicon Agent Monitoring*](https://developer.nvidia.com/blog/nvidia-open-agent-safety-platform-a-reference-for-continuous-in-silicon-agent-monitoring/) (September 2026). Primary, quoted via The Next Platform.


### Anthropic's analysis

- [Anthropic, *GLM-5.3 and the spread of advanced cyber capabilities*](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities), Fasano, Fleischer, McFaul, Xiao, Gallagher (29 September 2026, updated 30 September). Primary. All exploit-rate, bypass-rate and cost figures.
- [NIST CAISI, *CAISI's assessment of Z.ai's GLM-5.3 cyber capabilities*](https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities) (17 September 2026). Primary, cited via Anthropic.
- [DeepLearning.AI The Batch, *GLM-5.3 Makes Cybersecurity Gains*](https://www.deeplearning.ai/the-batch/glm-5-3-makes-cybersecurity-gains) (28 August 2026). Secondary. Release date and weights timing.


### Google's launch

- [Google, *Gemini 4 Argon: our next era of frontier intelligence*](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/), Koray Kavukcuoglu (30 September 2026). Primary. libgav1, Zircon, DeepSWE, monitor and sandbox statements.
- [BusinessToday, *Gemini 4 Argon explained*](https://www.businesstoday.in/technology/artificial-intelligence/story/gemini-4-argon-explained-googles-frontier-ai-model-build-for-coding-finance-legal-and-more-558984-2026-10-01) (1 October 2026). Secondary. Terminal-Bench 4.0 comparison.


### The FTC inquiry

- [Android Headlines, *FTC Opens Sweeping Probe into OpenAI and Anthropic Over Rogue AI Agent Attacks*](https://www.androidheadlines.com/2026/09/ftc-investigates-openai-anthropic-ai-risks.html), Jean Leon (30 September 2026). Secondary, citing the New York Post's first report.
- [Winbuzzer, *FTC Probes OpenAI and Anthropic Over AI Security Risks*](https://winbuzzer.com/2026/10/01/ftc-probes-openai-anthropic-ai-security-risks-a002-xcxwbn/) (1 October 2026). Secondary.


### The policy monitor and the footnotes

- [Archestra AI, *APPA: Recoverable Information-Flow Control for Real-World LLM Agents*](https://www.alphaxiv.org/abs/2607.24625), Kravchenko, Liventsev, Konstantinov, Iskhakov, Kukuy (arXiv 2607.24625, v2 26 August 2026). Primary. All APPA figures.
- [Techstrong.ai, *Gartner Warns 70% of Vendor-Built AI Agent Projects Face Abandonment by 2028*](https://techstrong.ai/articles/gartner-warns-70-of-vendor-built-ai-agent-projects-face-abandonment-by-2028/), Jon Swartz (30 September 2026). Secondary.


### Prior editions referenced

- [The alert worked. The stop did not.](2026-09-29-the-alert-worked-the-stop-did-not.html) (29 September 2026). The outbound-path inventory and the closed-world issue template.
- [Show your monitors](2026-09-25-show-your-monitors.html) (25 September 2026). The three oversight numbers.


*Vendor and blog figures indicate direction, not audited benchmarks. Nvidia's quarantine timing is a vendor claim. Anthropic's engagement rates come from a simulated environment where no model code runs. Google's libgav1 and Zircon figures are measured on its own code. APPA's results use the authors' own benchmark suite. The FTC has not published its demands.*


---

Canonical copy: [www.river.io/blog/posts/2026-10-01-the-agent-does-not-hold-the-keys.html](https://www.river.io/blog/posts/2026-10-01-the-agent-does-not-hold-the-keys.html). Mirrored into this wiki. The river.io blog is the source of truth.
