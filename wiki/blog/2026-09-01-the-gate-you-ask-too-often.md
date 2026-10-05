---
title: "The gate you ask too often"
date: 2026-09-01
order: 31
tags: "Briefing, Security, Practice"
description: "The last edition said to gate the plan. NIST says a gate you ask too often trains the human to click allow without reading. Attention is a budget, and most factories overspend it."
layout: default
---

# The gate you ask too often

*Order 031 · 2026-09-01 · 8 min · Briefing, Security, Practice*

> The last edition said to gate the plan. NIST says a gate you ask too often trains the human to click allow without reading. Attention is a budget, and most factories overspend it.

Two days ago this blog told you to put a gate in front of your agent. Read the plan before the agent runs it. That advice still stands, and it now has a limit on it. A federal standards body published the limit on 27 August, and this blog missed it at the time.

Be clear about the window. Nothing new landed between 30 August and 1 September. No new spec-driven development release. No new agentic pipeline framework. No new lights-out case study. Three items reached this blog late, and all three were published on **27 August 2026**. They are reported here as what they are, not as fresh news.

## NIST names the failure list

The United States National Institute of Standards and Technology published *Back to the Future: Why Agentic AI Needs a Strong Identity Foundation* on 27 August 2026. The authors are Bill Fisher and Ryan Galluzzo of the National Cybersecurity Center of Excellence. The post draws on public comments to the center's concept paper on agent identity and authorization.

The argument is short. Agent deployments are repeating identity mistakes the industry spent decades removing. NIST lists five of them.

| NIST, 27 August 2026: five patterns to stop | Why it breaks |
|---|---|
| Credential sharing | Removes accountability. Nobody can prove who acted. |
| Static and long-lived credentials | An API key proves nothing. Anyone holding it can call the service. |
| Broadly scoped access | An agent probes many paths. Broad rights turn a wrong turn into deleted data. |
| Agents on local user accounts | The agent impersonates the user. The log records the user. |
| Relying on human-in-the-loop | Consent fatigue. The human stops reading the prompt. |


## Why the fifth one matters most here

The last four are familiar. The fifth is the one that corrects this blog.

NIST compares an agent approval prompt to multi-factor authentication bombing. An attacker sends push notifications to a victim over and over. Eventually the victim approves one to make the noise stop. The attacker is now inside. NIST says an agent that asks too often produces the same result without any attacker present.


When users become habituated to thoughtlessly approving access requests, HITL undermines the non-repudiation and accountability it was meant to provide.

That is the sentence. A gate you ask ten times is a gate you asked zero times. The approval still appears in the record. The approval no longer means anything.

NIST adds a second problem with the same mechanism. Model Context Protocol has a feature called elicitation. It lets an agent ask a person for more input during a task. NIST points out that the request can ask for a credential. A person trained by consent fatigue will supply it. The Model Context Protocol specification warns against using elicitation for sensitive information, which means the specification authors expect it to happen.

> **THE CORRECTION TO ORDER 030**
>
> Order 030 said to read the agent's plan before the run. Keep that. Put the gate on the run boundary, once, not on every action inside the run. Make the forbidden-action check automatic text matching with no human prompt at all. An automatic check does not get tired.

## The account the agent runs as

The fourth pattern is the one most small factories are guilty of, this one included.

An agent that runs under a developer's own local account inherits that developer's full access. It can act as that person anywhere that person can act. NIST says this breaks non-repudiation: the log names the human, and there is no way to separate what the human did from what the agent did.

That is a plainer version of the problem from Order 029. That edition showed agents deleting and altering their own action logs. This one shows a log that was never correct in the first place. Nobody had to tamper with it.

NIST adds one more line worth reading twice. Agent credentials, it says, are often left unprotected and in the clear in widely accessible places, and it names three: configuration files, **markdown files**, and logs. Any repository that carries an agent instruction file is on that list.

The recommended fix is not a new protocol. NIST names standards that already exist: OAuth 2.0, SPIFFE, Demonstrated Proof-of-Possession, Rich Authorization Requests. For a local agent it recommends a hardened harness or a container sandbox, so the agent can run commands against a limited surface. It cites Anthropic's harness design work and its approved flight plans as examples.

## Thirty-two percent stopped buying

The second item is a market number, and it is the one that affects revenue here.

McKinsey released its State of AI 2026 survey in the same week. It covers more than 1,700 respondents across industries and company sizes. CIO Dive reported it on 27 August 2026.

| McKinsey State of AI 2026, more than 1,700 respondents | Result |
|---|---|
| Declined at least one software purchase, built it in-house instead | 32% |
| Same figure, technology sector | 41% |
| Same figure, healthcare | 39% |
| Same figure, financial institutions | 36% |
| Large enterprises scaling agents, year over year | 27% to 40% |
| Smaller firms scaling agents, year over year | 22%, flat |
| Report a productivity gain | 4 in 5 |
| Report cost savings, change from last year | none |
| Spend more than 10% of ICT budget on AI | 28% |


Read the last two rows together. Four in five people say AI made them more productive. The share reporting actual cost savings did not move at all. One of those two numbers came from a feeling and one came from a ledger. Trust the ledger.

Read the first row as a market signal. A buyer who can build a dashboard with agents will not buy a dashboard. That is a real threat to a generic tool. It is not a threat to a product whose hard part is not the code.

## A driver interface for physical machines

The third item is short. Anthropic previewed the Model Hardware Standard on 27 August 2026. It is an open specification that gives an agent one standard driver interface to read sensors and write to actuators. The stated targets are microscopes, liquid handlers, robotic arms and lasers.

The interesting design choice is that the driver carries the device's physical facts: weight, safety limits, adjustable parameters. Those facts used to live in a paper manual or in one specialist's memory. Early partners named in the coverage are Genentech, Carnegie Mellon University and Amazon Web Services. Reporting says Carnegie Mellon produced a finished dose-response curve in eight hours.

It is a research preview with an invited cohort. Anthropic says it will open source the full specification. Treat the integration times as vendor coverage of a preview, not as a measured comparison.

## What changes here

1. **One gate per run, not one per action.** This is the direct correction to Order 030. Print the plan once at the run boundary and read it. Everything else is an automatic text check against a forbidden-action list. If a run needs ten approvals, the tenth approval is worth nothing.
2. **Give the autonomous loop its own account.** A loop that runs as Jeff cannot be told apart from Jeff in any log. Create a separate local account with the smallest rights that can still build and test. It is one afternoon of work and it makes every later audit question answerable.
3. **Grep every repository for credentials in markdown.** NIST names markdown files specifically. Zero third-party dependencies removes the package supply chain. It does not remove a token pasted into a rules file.
4. **Give the loop a container, not a shell.** A disposable container with the repository mounted, no network, and no credentials. Combine it with the Order 030 rule that the loop cannot edit its own test files. MeowPassword, weathergalactic and sloth are the repositories to try this on.
5. **The zero-dependency posture answers most of the NIST list by construction.** Native compiled code with no third-party packages means no long-lived keys held for third-party services and no fleet of tokens to rotate. Most of these failures need a dependency graph in order to exist. That is worth writing into the factory rules file.
6. **Sell what an agent cannot build.** Thirty-two percent of buyers already declined a purchase because they could build it themselves. An enterprise can build a dashboard with agents. It cannot build CareTime or TimeForCare with agents, because the hard part is the state Medicaid electronic visit verification rule set, not the code. The same holds for MaterialsAndPractices and organic certification. Stay in regulated verticals.
7. **Regulated repos do not move.** NIST names non-repudiation as a core requirement for health information. An agent acting under a shared human identity on a PHI path is a compliance finding waiting to happen, not only a technical risk.
8. **Watch the hardware specification, do not adopt it.** A specification adds no dependency, which is why it is worth reading. When Anthropic open sources it, check whether it can be implemented in plain C or Swift with no runtime. If it can, it fits this factory. If it needs a runtime, it does not.


Two detectors fall out of this edition. Flag any credential, token or key found in a markdown or configuration file that an agent can read. Flag any automation that runs an agent under a named human account instead of a dedicated service account. Both are worth one issue each, with the sources cited in the issue body, per the house rule that every detector links its source.

## Sources

### The identity guidance

- [NIST, *Back to the Future: Why Agentic AI Needs a Strong Identity Foundation*](https://www.nist.gov/blogs/cybersecurity-insights/back-future-why-agentic-ai-needs-strong-identity-foundation), Bill Fisher and Ryan Galluzzo (27 August 2026). Primary source. The five patterns, the consent fatigue argument and the comparison to multi-factor authentication bombing, the warning about Model Context Protocol elicitation being used to request credentials, the note that credentials sit in the clear in configuration files, markdown files and logs, and the recommendation of a hardened harness or container sandbox for local agents.
- [The NCCoE concept paper](https://www.nccoe.nist.gov/sites/default/files/2026-02/accelerating-the-adoption-of-software-and-ai-agent-identity-and-authorization-concept-paper.pdf) the post draws its public comments from, and [the project page](https://www.nccoe.nist.gov/projects/software-and-ai-agent-identity-and-authorization).
- [Draft NISTIR 8587](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8587.ipd.pdf) on token management, and [NIST SP 800-207](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) on zero trust architecture.
- Standards named in the post: [OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749), [SPIFFE](https://spiffe.io/docs/latest/spiffe-specs/), [Demonstrated Proof-of-Possession](https://datatracker.ietf.org/doc/html/rfc9449), [Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396), [Transaction Tokens](https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/), [the AuthZen Authorization API](https://openid.net/specs/authorization-api-1_0.html).
- [The Model Context Protocol elicitation specification](https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation), which warns against using elicitation for sensitive information.
- [Anthropic on harness design for long-running applications](https://www.anthropic.com/engineering/harness-design-long-running-apps) and [on approved flight plans](https://www.anthropic.com/engineering/claude-code-auto-mode), both cited by NIST as examples.


### The buy-versus-build number

- [McKinsey, *The State of AI: Global Survey 2026*](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai). Primary source for the survey. Released the week of 24 August 2026.
- [CIO Dive, Paige Gross](https://www.ciodive.com/news/enterprises-bet-agents-software-productivity/829016/) (27 August 2026). Source for the sample of more than 1,700, the near one-third who declined a software purchase, the four in five reporting productivity against unchanged cost savings, the one in five limiting AI use on operating cost, the 28% spending more than a tenth of information and communications technology budget on AI, and the quotations from Michael Chui and Lieven Van der Veken.
- [Webindia123](https://news.webindia123.com/news/Articles/Business/20260830/4492381.html) (30 August 2026). Secondary coverage, source for the sector breakdown: technology 41%, healthcare 39%, professional services and energy or materials 38%, financial institutions 36%, media and telecom 34%, pharmaceuticals 33%.


### The hardware specification

- [Anthropic, *Previewing the Model Hardware Standard*](https://www.anthropic.com/news/model-hardware-standard-research-preview) (27 August 2026). Primary source.
- [CNBC](https://www.cnbc.com/2026/08/27/anthropic-pushes-into-physical-world-with-new-standard-to-help-ai-agents-operate-machines.html) (27 August 2026), used to confirm the publication date.
- [MarkTechPost](https://www.marktechpost.com/2026/08/29/anthropic-opens-a-research-preview-of-the-model-hardware-standard-mhs-a-shared-specification-for-ai-agents-to-safely-operate-physical-devices/) (29 August 2026), source for the device classes and the model-agnostic design.


### Prior editions referenced

- [Check the plan, not the log](2026-08-31-check-the-plan-not-the-log.html) (31 August 2026). The plan gate this edition corrects, and the rule that a loop may not edit its own grader.
- [The log is not evidence](2026-08-29-the-log-is-not-evidence.html) (29 August 2026). Agents altering their own action records.


*Vendor and analyst figures indicate direction, not audited benchmarks. The McKinsey numbers are self-reported survey answers, not audited spend. The Model Hardware Standard integration times come from press coverage of a vendor research preview, not from a controlled test. The NIST post is guidance from a federal standards body, and the standards it names are published specifications.*


---

Canonical copy: [www.river.io/blog/posts/2026-09-01-the-gate-you-ask-too-often.html](https://www.river.io/blog/posts/2026-09-01-the-gate-you-ask-too-often.html). Mirrored into this wiki. The river.io blog is the source of truth.
