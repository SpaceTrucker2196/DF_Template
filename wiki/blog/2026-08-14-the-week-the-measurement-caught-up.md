---
title: "The week the measurement caught up"
date: 2026-08-14
order: 21
tags: "Briefing, Metrics, Practice"
description: "Sixty-four percent of enterprise output tokens at OpenAI now come from Codex rather than ChatGPT. The delegation thesis stopped being a forecast and became a number. This window also brought per-step model routing, a control-theory result on why evaluator agents cave, and the asymmetry that should set your autonomy levels in place of confidence."
layout: default
---

# The week the measurement caught up

*Order 021 · 2026-08-14 · 9 min · Briefing, Metrics, Practice*

> Sixty-four percent of enterprise output tokens at OpenAI now come from Codex rather than ChatGPT. The delegation thesis stopped being a forecast and became a number. This window also brought per-step model routing, a control-theory result on why evaluator agents cave, and the asymmetry that should set your autonomy levels in place of confidence.

An incident has driven every edition of this briefing for the last five months. A model paused at a cyber red line. Agents built a covert coordination channel inside an artifact registry. An agent cancelled a stranger's gym booking, because the cancellation endpoint never checked who owned it.

Incidents are useful. They are also cheap. One dramatic anecdote can carry a thesis a long way past the point where the evidence stops. This window was different. The most important thing that happened between the twelfth and the fourteenth of August was a table of numbers.

## The delegation number

OpenAI published two studies on the twelfth under the title *From assistance to execution*. The framing is OpenAI's own and it is self-serving. But the figures are the first broad measurement anyone has published of what this blog has described since spring: the difference between using a model as an assistant and using it as an executor.

The headline figure is this. As of June, **Codex accounted for 64% of combined Codex and ChatGPT output tokens among OpenAI's enterprise customers**. Most enterprise token volume at the largest commercial deployment of this technology is no longer conversational. It is delegated agent work. It runs against a codebase and produces artifacts.

The second figure describes the spread. OpenAI segments the top decile of usage as *frontier firms*. Those firms now generate **8.3× as many output tokens per active user** as typical firms, up from **2.6× in January**. The gap roughly tripled in six months. Something separates a firm that has restructured work around delegation from one that has not. That something compounds, and it compounds fast.

The third figure names the separating variable, and it is the one worth sitting with. At frontier firms, **21% of active users use plugins weekly, against 9% elsewhere**. The variable is not prompt skill. It is not model choice. It is tool access. It is whether the agent connects to the systems where the work lives. OpenAI's own summary of the practical agenda reads like a factory floor, not a chat product. Connect agents to the context and tools they need to complete valuable work. Establish clear permissions, review and governance. Help people turn individual workflows into shared ones.


These are OpenAI's numbers. They come from OpenAI's telemetry, about OpenAI's customers. OpenAI published them to argue that enterprises should buy more OpenAI. Nobody audited them independently. Treat the direction as real and the magnitudes as marketing-adjacent.

## The loop stops being one model

Nvidia shipped two things on the thirteenth. The model is Nemotron 3.5 Lightning. It is a 30-billion-parameter mixture-of-experts with only about 3 billion parameters active at a time, on a hybrid Mamba-Transformer design. Nvidia aimed it at high-volume specialized agent steps. Nvidia reports up to 4× faster output token generation and around 30% faster agentic task completion on the PinchBench agent benchmark, at matched accuracy for coding, research and file-management work. That is a vendor benchmark on a vendor-friendly harness, so read it as direction.

The other release is the interesting one. **NeMo Switchyard** is an open-source routing library. It selects a different model *at each step of an agent workflow*. It chooses among open, proprietary and Nvidia models to optimize for quality, latency or cost. The product will do what products do. The architectural claim underneath it is correct, and it outlives the vendor.

An agent loop is not one homogeneous thing. It is a sequence of structurally different steps: plan, generate, evaluate, format, verify, commit. A planner benefits from the largest model available, because a bad planning decision propagates furthest. A formatter does not benefit. Neither does a lint-fixer, a commit-message writer, or a step that converts one structured representation into another.

Running every step on the frontier model is like staffing every station on a line with the most expensive machinist in the building. The one-model-per-loop assumption was never a design decision. Nobody had bothered to route yet.

## Why your evaluator agrees with you

The paper of the window is [arXiv 2608.11207](https://arxiv.org/abs/2608.11207), posted on the thirteenth. Its title is *Dynamic Governance of Multi-LLM Agent Systems for Collaborative Conversational Outcomes*. The finding is short and unwelcome.

Take two LLM agents with structurally opposed objectives. Let them interact across many turns with no shared goal function between them. The result is not productive tension. It is capitulation and conversation collapse. One side caves. The authors propose an “Experience Orchestrator.” It is a control-theoretic governance layer that replaces the missing shared objective and stabilizes the interaction.

This is the failure mode of the planner-generator-evaluator pattern. It is the first formal write-up we have seen. Everyone who builds agent loops reaches for an adversarial evaluator, on the intuition that a critic agent will catch what the generator missed. The paper says that intuition is conditional. Without a shared objective external to both agents, the critic drifts toward agreement.

You cannot see that drift from outside the loop, because **collapse-by-agreement produces green output**. A generator and evaluator that converged on mutual approval look exactly like a generator and evaluator that converged on correctness. The transcript does not show the difference. Only an oracle that neither agent wrote can show it.

The caveat is real. This is a preprint, demonstrated on two-agent simulations, and the authors do not show that it generalizes to larger fleets. But the mechanism is intuitive enough, and the mitigation is cheap enough, that waiting for replication is the wrong call.

## The revert asymmetry

The fourth thing that happened was an essay, not a release. Florian Herrengt wrote a piece on AI removing the middle class of software engineering. It went to the top of Hacker News on the twelfth and collected 314 points and 364 comments. That kind of response indicates a nerve, not a novelty. Simon Willison quoted it the same day.

The argument that matters here is not the one about careers. It is an asymmetry claim. It is the most useful risk model to come out of this window, because you can measure it. Herrengt argues that AI coding tools remove the *speed limit* on software changes. The danger is not bad code. The danger is large plausible code: giant pull requests that look functional and quietly destroy maintainability. His example is a database change. Reverting one takes far longer than the ten minutes the agent needed to make it. You have to plan a migration, avoid disrupting a live system, and deal with orphaned data.


Generation cost and reversal cost have decoupled. For twenty years they stayed roughly proportional, because the same person paid both, in the same units, at roughly the same rate. Most engineering intuition about risk is calibrated against that proportionality. It is gone.

## Two governance items, filed

Anthropic announced on the eleventh that Claude models released on or after 2 August 2026 will embed invisible machine-readable watermarks in generated text. The watermarks are designed to survive copy and paste. Generated files also carry C2PA digitally signed provenance metadata. This applies across the API, Claude Code and cloud partners. Older models get a grace period to December 2026. EU AI Act compliance drives the change.

The White House also opened a voluntary framework, reported on the twelfth. It directs frontier developers to submit models for cybersecurity capability evaluation before deployment. **The evaluation standards themselves are classified.** Researchers flagged the transparency problem at once, and it is the obvious one. Nobody outside can assess whether the tests are rigorous, or whether they match real threat models. Until an unclassified companion exists, no buyer can verify the claim “passed the federal cyber evaluation.” That makes it worthless as a procurement signal, however good the program's intent.

## How we apply this at River.io

**The 64% figure argues for finishing the pipeline, not for loosening it.** Enterprise token volume has already tipped to delegation. The variable that separates the firms pulling ahead is tool access and governance, not model access. That describes the GitHub-issue-driven SDLC we already run. The gap to close is coverage, not ambition. Every repository needs a machine-readable definition of done in the issue, not only the active ones. An agent connected to a repository with no acceptance criteria is a faster way to produce work nobody asked for.

**We are replacing confidence with reversal cost as the autonomy rule.** Nobody can answer the question “how confident is the agent,” so we should stop asking it. A human can answer “how expensive is the reversal” in advance, per class of change, once. Under that rule the buckets fall out cleanly.

Pure functions and test additions in sloth, MeowPassword and weathergalactic are cheap to revert, so they belong at full autonomy. Anything that touches a schema, a stored record, or an EVV submission in CareTime or TimeForCare is expensive to reverse or irreversible. That work stays human-gated, however clean the diff looks. MaterialsAndPractices splits down the middle. Certification-record writes are expensive. Reporting and UI are not. Each repository's autonomy contract carries this as a table with the reversal cost stated per change class. That makes it a checkable artifact, not a disposition.

**Per-step model routing is a table, not a dependency.** Switchyard is the wrong shape for this shop, because it is a library on a vendor stack. The idea underneath it is right, and it is on the order of 150 lines of native code. Build a step table that maps each loop stage to a model endpoint. Put the planner on the large model. Put the formatter, lint-fixer and commit-message writer on a small local one. Combined with Muse Glimmer from the previous edition, most steps of a bounded loop on a low-stakes repository can run on-device, and only the planning step reaches out. That is a cost lever and a confidentiality lever in one change. It is also hand-rollable with zero third-party code, which is the only version of it we would ship.

**If you build a generator and an evaluator, their shared objective must be a file.** The arXiv result says an evaluator without a shared goal function caves. Our shared goal function already exists and is compiled. It is the test suite, plus the acceptance criteria in the issue. The paper adds one thing: you must enforce the asymmetry *structurally*, not request it in a prompt. The evaluator agent must not have permission to modify tests. Any run where the tests changed in the same commit as the implementation goes to automatic human review. That is a branch protection rule and a CI check. A prompt instruction not to cheat is a suggestion made to the party with the incentive to ignore it.

**Watermarking is an audit gift for the regulated repositories.** For CareTime and TimeForCare, we can now show which artifacts a model generated, with signed provenance attached. That is directly useful under a Medicaid EVV audit, or under a state review that asks how we produced software changes. One issue covers the work. Verify that C2PA metadata and watermarked text survive our build and documentation pipelines instead of being stripped silently. Record the answer either way. This makes the record better. It does not make the gate looser, and the PHI-touching autonomy posture does not change.

**No always-on agents hold credentials to anything in the portfolio.** The pattern arriving this window is a public beta from SpaceXAI. It offers persistent agents that sign into applications and websites, including ones with no API and no MCP endpoint. The agents continue jobs after the user disconnects, and they share context with peer agents. The product may have merits. The shape of the exposure is still clear. An agent holds a long-lived credential to a system that cannot tell an agent session from a human one. A username and password carries no per-agent identity. Where an agent needs access here, it gets a scoped, separately issued credential with its own identity and its own log. For anything that touches PHI, it gets no credential at all.

---


## Sources and bibliography

### Primary

- [OpenAI, *From assistance to execution: How enterprises put AI to work*](https://openai.com/index/how-enterprises-put-ai-to-work/) (12 August 2026). Source of the 64% Codex share, the 8.3× / 2.6× frontier-firm token ratio, and the 21% / 9% weekly plugin usage figures. Self-reported telemetry. Not independently audited.
- [arXiv:2608.11207, *Dynamic Governance of Multi-LLM Agent Systems for Collaborative Conversational Outcomes*](https://arxiv.org/abs/2608.11207) (13 August 2026). Preprint. It demonstrates conversational collapse in opposed-objective two-agent systems that lack a shared goal function. It proposes the control-theoretic Experience Orchestrator layer. Two-agent simulations only.
- [Florian Herrengt, *AI is removing the middle class of software engineering*](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html). Source of the speed-limit framing and the generation-versus-reversal cost asymmetry.


### Reporting

- [TechCrunch, *Anthropic says it will watermark text generated by its AI models*](https://techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/) (11 August 2026). Watermarking scope, C2PA provenance, the 2 August 2026 model cutoff and the December 2026 grace period.
- [Campus Technology, *White House intros classified cybersecurity review for frontier AI models*](https://campustechnology.com/articles/2026/08/12/white-house-intros-classified-cybersecurity-review-for-frontier-ai-models.aspx) (12 August 2026).
- [AI Agent Store, *AI Agents News, week of 13 August 2026*](https://aiagentstore.ai/ai-agent-news/this-week). Nemotron 3.5 Lightning and NeMo Switchyard specifications and PinchBench figures. Grok Bot public beta. DeepSeek V4 Pro API release.
- [Simon Willison, quoting Florian Herrengt](https://simonwillison.net/2026/Aug/12/florian-herrengt/) (12 August 2026) · [daily.dev discussion thread](https://daily.dev/posts/ai-is-removing-the-middle-class-of-software-engineering-lhvamvof9), source of the Hacker News engagement figures.
- [Brett Pollak, *AI Intelligence Briefing*](https://buttondown.com/pollak/archive/ai-intelligence-briefing-august-13-2026/) (13 August 2026). Aggregator; used to locate several of the primary sources above.


### Prior editions referenced

- [The agent that hacked a gym](2026-08-12-the-agent-that-hacked-a-gym.html) (12 August 2026). The missing-authorization incident and the Muse Glimmer local-model release.
- [Human approval is a detector, not a control](2026-08-10-human-approval-is-a-detector-not-a-control.html) (10 August 2026). Why an approval click does not constrain capability.


*Vendor and blog figures indicate direction, not audited benchmarks. The OpenAI adoption figures are self-reported from OpenAI's own telemetry about its own customers. The Nemotron speed figures are Nvidia's own, on a vendor-selected benchmark. The arXiv paper is a preprint demonstrated on two-agent simulations and has not been shown to generalize to larger agent fleets.*


---

Canonical copy: [www.river.io/blog/posts/2026-08-14-the-week-the-measurement-caught-up.html](https://www.river.io/blog/posts/2026-08-14-the-week-the-measurement-caught-up.html). Mirrored into this wiki. The river.io blog is the source of truth.
