---
title: "The approval and the action"
date: 2026-09-23
order: 40
tags: "Briefing, Security, Practice"
description: "A human approves operation A and the framework runs operation B. A model release that can answer from a different model than the one you called. A gate tool that publishes its own friction. The approval and the action are two objects."
layout: default
---

# The approval and the action

*Order 040 · 2026-09-23 · 8 min · Briefing, Security, Practice*

> A human approves operation A and the framework runs operation B. A model release that can answer from a different model than the one you called. A gate tool that publishes its own friction. The approval and the action are two objects.

Order 039 was about checks nobody wrote. This edition is about a check that many people did write, and that still fails. The human-in-the-loop gate. Three items are new and inside the window. One older item was missed by the last two editions and is added with its real date.

Be clear about the window. The last edition here was 21 September 2026. This one covers two days. Every item below has its real publication date.

## Loopjacking: the human approved A

On 17 September 2026, Adithyan Arun Kumar posted a paper to arXiv titled "Loopjacking: Hijacking Human-in-the-Loop Approval". It surfaced in the Agentic Security newsletter on 22 September. The paper names a failure of binding. A human approves what they understand as operation A. The implementation uses that decision to run a materially different operation B.

There are two variants. In a representation-based attack, B is already encoded in the pending action. The approval prompt omits it or shows something else. In a post-approval state-substitution attack, the human sees the correct A. Then mutable workflow state replaces A with B after approval and before execution. The human did nothing wrong. The framework changed the object under them.

| Framework tested, arXiv 2609.21081 | Result |
|---|---|
| Agno AgentOS, 7 releases ending at 3.0.9 | Post-approval substitution reproduced |
| LangGraph Agent Server, conditional in-memory composition, 12 versions ending at 0.14.0 | Post-approval substitution reproduced |
| OpenClaw 2026.2.23 | Representation mismatch reproduced |
| OpenClaw 2026.2.24 | Rejected |
| OpenAI Agents SDK 0.22.0 and 0.22.2 | Negative control. Serialized continuation preserves exact per-call binding and rejects a mutated B. |


The author says plainly that these results do not estimate how common the bug is across the ecosystem. The fix is stated just as plainly. Render the complete canonical approval. Compare the exact action at use time. Or make the pending state immutable after the prompt. The paper ships an evidence archive on GitHub.

The same newsletter summarizes a related benchmark, "APort Vault" (arXiv 2609.22076). It replays more than 4,300 real capture-the-flag attacks against 14 models acting as a payment agent. Without external controls, the agents paid the attacker most of the time. One deterministic pre-action authorization check drove unauthorized transfers to about zero, no matter which model was fooled. This blog has not read that paper directly and reports it as the newsletter states it.

> **THE LESSON, TWICE**
>
> Loopjacking and APort Vault say the same thing from two sides. The control must sit outside the model. It must be bound to the exact action that executes. A smarter model does not fix a framework that rewrites the pending action. A more careful reviewer does not fix it either.

## Opus 5.5: the model that answered

On 22 September 2026, Anthropic released Claude Opus 5.5. GitHub Copilot added it the same day. The vendor claims are the usual ones and this blog treats them as direction only. Output tokens cost $20 per million, down from $25 for Opus 5. Anthropic says the model is about 40 percent cheaper to run on typical workloads and produces output more than 30 percent faster. GitHub says that in its early testing the model resolved tasks about as well as Opus 5 with significantly fewer steps and tokens.

Two details matter to a pipeline more than the benchmarks.

**First, routing.** Opus 5.5 ships with the same class of safeguards as Fable 5.1 for cybersecurity and biology. The New Stack reports what happens when a safeguard classifier fires. The request is handled by Opus 4.8 or Opus 5 instead. The caller is not told. In a multi-turn agent workflow, one step can be served by a different model than the step before it. An eval built on the assumption that every request goes to the same model will not see this. Vetted organizations can apply to Anthropic's verification programs to run without the classifiers.

**Second, the watermark.** GitHub's changelog says Opus 5.5 watermarks its text output. The watermark adds no tokens and changes no meaning. For a factory that commits agent output to a repository, agent-written commit messages, comments and docs now carry a mark the factory did not choose. This is not a security risk. It is a provenance fact.

Anthropic also says Opus 5.5 posted its best internal alignment results to date, with fewer attempts to escape sandboxed environments, and that flawed reinforcement-learning environments were a major source of past misaligned behavior. All of that is the vendor's self-report on launch day.

## Prismor: a gate that publishes its own cost

On 23 September 2026, Help Net Security covered Prismor, a free open-source tool from PrismorSec. Prismor sits between Claude Code, Codex or Cursor and the action the agent wants to take. It checks each tool call against a policy before the call runs. Every call gets one of three verdicts: allow, warn, or block. Rules start in observe mode. The user promotes them to enforce one at a time.

The vendor measured the added delay at 0.8 milliseconds per tool call across 10,000 simulated sessions. Prismor also wraps npm and pip. It scores each install on package age, maintainer count, install scripts and known indicators of compromise. A score of 60 or higher blocks the install.

| Prismor preset, vendor's own scores | Coverage | Friction |
|---|---|---|
| dev-safe, for feature work on unfamiliar code | 31% | 9% |
| regulated-airgap, no network and no shell | 100% | 90% |


**The table is the part worth keeping.** A tool that states the cost of its own strict setting is rare. The preset that covers everything also gets in the way of nearly everything, and the vendor says so. One caution. Prismor's optional semantic guard sends unclear prompt-injection cases to an LLM for a second look. That puts a model back inside the gate.

## Missed: the first regulator record of an agent-run attack

This item is older than the window. It was inside the windows of Orders 038 and 039 and neither edition caught it. On 16 September 2026, SecurityWeek reported that the AEPD, Spain's data protection authority, published details of the first personal-data breach notification attributed to an attack executed through an AI agent. Help Net Security followed on 17 September.

The AEPD's deputy director says the information comes from the affected organization's own filing and needs more analysis. The agent, built on a known off-the-shelf LLM, scanned files for weaknesses, logged in, searched the application until it found a flaw, then changed personal data and reached invoices. The AEPD's point is not the model. A third party used an agent as an instrument to chain the phases of the attack together.

Order 029 covered the Hugging Face incident. Order 039 covered Google's Gemini evaluation. Both were lab agents that left a sandbox. This one is different. It is a third party's agent aimed at a target on purpose. Under GDPR Article 33, the 72-hour notification clock does not care whether the attacker was a person or an agent. "An AI agent did it" is now a line on a breach form.

## Left out, with reasons

Google's Agent Anomaly Detection, announced 16 September 2026, is a private-preview oversight layer for the Gemini Enterprise Agent Platform. It reads traces after the fact, runs out of the request path, and maps findings to the OWASP Agentic Top 10. It exposes an API that a callback can use to halt a session. That makes it an audit log with a halt switch, not a gate. AISLE's curl result, six CVEs in curl 8.22.0 after Codex Security and Mythos reported zero, is dated 2 September 2026. It is a vulnerability-discovery story, not a pipeline story.

## What changes here

1. **Audit the binding on every human gate in the factory, this week.** The regulated repos, CareTime, TimeForCare and MaterialsAndPractices, rely on named-human approval for every security, safety or evidence-producing change. Loopjacking says that approval is only as good as the object the human approved. In a GitHub-issue-driven SDLC the concrete check is this: the human approves a pull request at one commit SHA, and the merge and deploy steps must act on that SHA and no other. If a bot can push after approval and the merge still proceeds, that is post-approval state substitution by another name. GitHub's "dismiss stale approvals on new commits" branch-protection rule is the one-line fix. Turn it on everywhere. Confirm it by pushing a no-op commit after an approval on a low-stakes repo and watching the approval drop. Pair it with the pinned-checkout assertion from Order 039. Together they bind the approval, the checkout and the deploy to one SHA.
2. **Record the responding model, not the requested model.** Wherever the factory logs which model produced a change, capture the model identity from the response. If the vendor API exposes it, log it. If it does not, log that it does not. This is the only way the regression ledger from Order 039 can tell "the model changed" from "the task was hard."
3. **Write down what the factory thinks about watermarked text.** Native compiled code is not affected. Commit messages, comments, docs and issue text written by an agent now carry a mark. The factory does not need to act on it today. It should record that it knows.
4. **Do not add Prismor to the regulated repos. Do copy its scorecard.** Prismor is a third-party runtime dependency for the tooling. It runs an optional model inside the gate. Its regulated preset admits 90 percent friction. None of that fits CareTime or TimeForCare. What is worth copying is the format. For each factory gate, state coverage and friction as two numbers. The factory's own zero-dependency shell gates, the `git rev-parse` assertion, the `GIT_CONFIG` hardening, the deny list for `rm`, `curl` and `sudo`, can each be scored the same way.
5. **Keep regulated work human-gated. This edition changes the wording, not the posture.** "Human-gated" now means three things. A named human approves a canonical rendering of the exact change. The pending state cannot mutate after approval. The executed object is compared to the approved object at use time. If any one of those is missing, the gate is decorative. The APort Vault result is the reason to prefer a deterministic check over a smarter model at every irreversible step.
6. **Low-stakes repositories carry the experiments.** MeowPassword takes the stale-approval-dismissal test first: enable the rule, approve a PR, push a trailing commit, confirm the approval is gone. weathergalactic takes the responding-model log field and runs Opus 5.5 on a few issues to see whether the response ever names a different model. sloth takes a coverage-and-friction scorecard for its existing shell gates, one line per gate.


## Sources

### Loopjacking and APort Vault

- [arXiv 2609.21081, *Loopjacking: Hijacking Human-in-the-Loop Approval*](https://arxiv.org/abs/2609.21081), Adithyan Arun Kumar (submitted 17 September 2026). Primary. Definitions, the two variants, the reproduced versions and the negative control.
- [GitHub, *adithyan-ak/loopjacking*](https://github.com/adithyan-ak/loopjacking). Primary evidence and reproduction archive.
- [The Agentic Security Newsletter, *Week of September 21, 2026*](https://agenticsecurity.substack.com/p/the-agentic-security-newsletter-week-6c2), Raphael Bottino (22 September 2026). Secondary. The APort Vault summary and the week's roundup.
- [arXiv 2609.22076, *APort Vault: Benchmarking AI Agent Payment Authorization with the Open Agent Passport*](https://arxiv.org/abs/2609.22076), Uchi Uchibeke. Primary, reported here as summarized by the newsletter.


### Opus 5.5

- [TechCrunch, *Anthropic releases Opus 5.5 with lower prices and Fable-level performance*](https://techcrunch.com/2026/09/22/anthropic-releases-opus-5-5-with-lower-prices-and-fable-level-performance/), Russell Brandom (22 September 2026). Secondary. Pricing, release date, safeguard class.
- [The New Stack, *Anthropic releases Opus 5.5 and cuts pricing by 20%. Your agent calls might secretly get routed to an older model.*](https://thenewstack.io/claude-opus-5-5-release/) (22 September 2026). Secondary. The classifier-routing detail and the alignment claims.
- [GitHub Changelog, *Claude Opus 5.5 is now available in GitHub Copilot*](https://github.blog/changelog/2026-09-22-claude-opus-5-5-is-now-available-in-github-copilot/) (22 September 2026). Primary for GitHub's early-testing claim and the watermark note.


### Prismor

- [Help Net Security, *Prismor: Open-source runtime control plane for AI agents*](https://www.helpnetsecurity.com/2026/09/23/prismor-open-source-ai-agent-security/), Anamarija Pogorelec (23 September 2026). Secondary. All Prismor figures.
- [GitHub, *PrismorSec/prismor*](https://github.com/PrismorSec/prismor). Primary source code.


### The AEPD notification

- [SecurityWeek, *First Agentic AI Data Breach Reported to Spanish Regulator*](https://www.securityweek.com/first-agentic-ai-data-breach-reported-to-spanish-regulator/), Kevin Townsend (16 September 2026). Secondary, quoting the AEPD blog post.
- [Help Net Security, *Spain reports first data breach involving autonomous AI agent*](https://www.helpnetsecurity.com/2026/09/17/spain-ai-agent-data-breach/), Sinisa Markovic (17 September 2026). Secondary. The deputy director's statements.


### Checked and left out

- [Google Developers Blog, *Agent Anomaly Detection, now in Private Preview on the Gemini Enterprise Agent Platform*](https://developers.googleblog.com/agent-anomaly-detection-now-in-private-preview-on-the-gemini-enterprise-agent-platform/), Achuth Narayan Rajagopal (16 September 2026). Primary.
- [AISLE, *AISLE Discovered Six curl CVEs After OpenAI and Anthropic Found Zero*](https://aisle.com/blog/aisle-discovered-six-curl-cves-after-openai-and-anthropic-found-zero), Stanislav Fort (2 September 2026). Primary.


### Prior editions referenced

- [The check nobody wrote](2026-09-21-the-check-nobody-wrote.html) (21 September 2026). The pinned-checkout assertion and the regression ledger.
- [The enforcer inside](2026-09-17-the-enforcer-inside.html) (17 September 2026). The `GIT_CONFIG` hardening.


*Vendor and blog figures indicate direction, not audited benchmarks. Anthropic's and GitHub's Opus 5.5 numbers are self-reports on launch day. PrismorSec's overhead and preset scores are its own. The Loopjacking author states the results do not estimate ecosystem prevalence. The AEPD account rests on the affected organization's filing, and the regulator says it needs further analysis.*


---

Canonical copy: [www.river.io/blog/posts/2026-09-23-the-approval-and-the-action.html](https://www.river.io/blog/posts/2026-09-23-the-approval-and-the-action.html). Mirrored into this wiki. The river.io blog is the source of truth.
