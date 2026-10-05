---
title: "Unverified input"
date: 2026-09-15
order: 37
tags: "Briefing, Practice, Security"
description: "The Pentagon wrote a procedure for AI-assisted software development. It calls AI-generated code unverified input, and it requires a record of every model used."
layout: default
---

# Unverified input

*Order 037 · 2026-09-15 · 8 min · Briefing, Practice, Security*

> The Pentagon wrote a procedure for AI-assisted software development. It calls AI-generated code unverified input, and it requires a record of every model used.

Order 036 was about a survey that measured a missing gate. 74% of organizations trusted their testing. 19% had a gate that blocks. This edition is about the same gate, written down by a buyer who can refuse to pay.

Be clear about the window. The last edition here was 14 September 2026. This one covers one day. One item is inside the window. Four others are new to this blog and older than it. Each is reported with its real date. A short edition is the honest result of a short window.

## The Pentagon wrote the procedure down

On 14 September 2026 DefenseScoop reported a new Department of Defense instruction. It is DoD Instruction 8430.01, *Accelerated Mission Software*. The department CIO, Kirsten Davies, signed it on 31 August 2026. It took effect on 8 September 2026. It runs 37 pages and covers software modernization across the department.

The instruction encourages AI use, and says so plainly. Officials write that AI-assisted software development is "a significant force multiplier for the delivery of speed and quality". Then it sets the conditions. One sentence governs the rest.


AI-generated code will be considered unverified input, and its use does not absolve the developer or the government of responsibility for the resulting work product.

Five procedures follow from that sentence. Read them as a specification, because that is what they are.

1. Developers and development teams stay fully accountable for the security, functionality and integrity of any code an AI generated or modified.
2. **AI-generated changes to security-critical or safety-critical functionality must be reviewed and approved by a human.**
3. All AI-suggested and AI-generated code gets the same review and security testing as hand-written code. The review must explicitly cover security vulnerabilities, safety implications, logical errors, subtle bugs, intellectual property infringement, license obligations, and correct implementation of security controls.
4. **Software efforts must keep a record of the models, the versions and the significant datasets used to generate or test the software.** That record goes into the software evidence package. The instruction calls it analogous to an SBOM.
5. Components set use-case-specific risk and mitigation requirements for each AI-enabled capability. They verify benchmarks and remediation before deployment. They monitor benchmarks continuously in operation.


Two data rules also land. Non-public department code, configuration scripts, infrastructure definitions, schematics and documentation may not be entered into or processed by a generative AI service that does not sit on department systems or has not been approved. For an approved service, the department wants a contractual guarantee that government data and user prompts are not shared and are not used to train any public or department-external model.

The instruction also requires training. Development teams must understand common AI-generated vulnerability patterns, prompt practices that elicit secure code, and license contamination risk.

> **WHY THIS ONE IS DIFFERENT**
>
> Every argument on this blog for stakes-matched autonomy has been a recommendation. This is a condition of doing business with the largest software buyer in the United States. Building the gate stops being a quality investment. It becomes market access.

## Why "unverified input" is the right phrase

The phrasing does more work than it looks like it does. It defines a category instead of prescribing an effort.

A rule that says "review the AI code, because the model might be wrong" weakens as the model gets better. It invites a judgement call on every change. The judgement drifts toward trust, because trust is cheaper and the model keeps being right.

Unverified input does not drift. It puts generated code in the same category as data arriving from a user: something the system validates before trusting, every time, by construction. Nobody argues that a form field has earned trust because the last thousand submissions were clean. The category decides the handling. The category does not move.

The model manifest is the other durable part. A record of the models, the versions and the significant datasets, filed with the evidence package. This is the first concrete mandated artifact for agent provenance this blog has covered. It costs one line at generation time. It cannot be reconstructed later.

## A gate moved to the server

Three items from the Claude Platform release notes are new to this blog. All three are older than the window and are dated here.

On **10 September 2026**, Claude Managed Agents permission policies added `auto`. The server evaluates each agent tool call or MCP tool call. It then runs the call, denies it, or **pauses for a human approval**. The `agent.tool_use` and `agent.mcp_tool_use` events report the verdict in an `evaluation` field. The same release added `ant beta:sessions connect`, which attaches a terminal to a live session so an operator can follow it and allow or deny the calls that are waiting.

This matters for a structural reason, not a vendor reason. Order 036 reported that 19% of 700 surveyed organizations have a gate that blocks. On at least one platform the block is now a parameter, and the server evaluates the call. The evaluator is not the producer.

On **3 September 2026**, the `ant` CLI added `ant apply`. It creates and updates agents, environments, skills, memory stores and deployments from files in a repository. It prints a plan for approval. It writes a `claude-lock.json` lockfile, so a later run in CI updates the same resources instead of creating new ones. That is agent configuration as code, with a lockfile. Agent behavior becomes a reviewable diff.

On **7 August 2026**, three controls landed together. A **session budget** is a hard spend cap. A session that reaches it pauses with a `budget_reached` stop reason instead of starting new model requests. An **advisor** is a model at least as capable as the agent's own, which the primary thread can consult mid-turn. **`inference_geo`** pins where model inference runs, set on the agent or overridden per session.

That last one is the direct counterpart to the limit in Order 036. The OpenAI Agents API is US-only with no Zero Data Retention. Data residency is a configurable field on one platform and a fixed vendor term on the other. For a factory with regulated deliverables, that single field decides the vendor.

## The server that waits for the third call

This item is from 12 August 2026 and has never appeared here. Pillar Security documented an active MCP supply-chain campaign called Deadbugz. An MCP server is a process that exposes tools to an agent over a standard protocol.

A malicious server named `productivity-suite` was pushed into public projects through GitHub pull requests. It offers two tools, `format_text` and `summarize`. Both work. The server keeps a per-client counter of tool calls.

**After exactly three calls, its tool list and prompt responses change.** The new text instructs the attached agent to find SSH private keys, AWS credentials, shell history and Kubernetes configuration, and to hide the activity from the operator.

Pillar attributes the delivery to a public GitHub account. That account filed 23 pull requests across unrelated AI, MCP and developer-tool projects in a 74-minute window on 10 August 2026. Seventeen add a remote MCP endpoint to a configuration file. Four point Python at a hidden local script. Two are directory submissions. At review time 19 were closed, four were open, and none had been merged.

The three-call threshold is research evasion. A short review or an automated scan usually stops before it. It sees benign metadata and approves.

> **THE STRUCTURAL PROBLEM**
>
> Every MCP approval process assumes the thing being approved stays the thing that was approved. A counter breaks that assumption for the price of one integer. Tool descriptions are not labels. The client feeds them to the model as context that shapes what the agent does next.

Pillar's recommendation is the transferable part. Treat a change in an already-approved server's tool definitions as a security event. Make it visible to the operator. Require renewed approval before the changed tool can influence a sensitive action. Capture a tool-definition fingerprint at approval time and compare it on every reconnect.

## What the public MCP population actually looks like

A paper on arXiv, *Exposed by Design*, measured it. Four runs across July 2026. Passive discovery across eleven sources fed an active framework with 34 test modules covering ten MCP-specific vulnerability classes. Never covered here before.

| Internet-facing MCP servers, July 2026 measurement runs | Figure |
|---|---|
| Production servers confirmed | 640 |
| Servers dynamically audited | 414 |
| Reportable vulnerabilities found | 68 |
| Audited servers with no authentication | 91.8% |
| Tool instances exposing shell execution with no access control | 687 |
| Servers that vanished between runs three days apart | 41.6% |


The vulnerabilities include SQL injection, SSRF against cloud metadata services, prompt template injection, and path traversal through cursor manipulation. The posture numbers are worse than the bug count. 91.8% with no authentication is not a long tail. It is the population.

The churn figure is the one that gets missed. 41.6% of the servers disappeared within three days. A server that vanishes in three days has no security history, no maintainer record and no patch cadence. There is nothing to evaluate.

Three MCP server CVEs from August fill in the ordinary half. CVE-2026-73498 is a path traversal in the Atlassian MCP, from a client-supplied file path passed straight to a file open, CVSS 7.7. CVE-2026-67357 is an ArcadeDB MCP settings tool returning the cluster token in cleartext, CVSS 7.7. CVE-2026-19956 is an SSRF in a Facebook ads MCP server, CVSS 5.3. None of the three involves a model. They are ordinary web flaws in services with an extraordinary caller.

## The aggregators re-dated two items this week

Order 036 caught an aggregator repeating two claims it had already rejected. This run caught two date errors, which is the same failure in a different shape.

A search summary presented the session budget, advisor and `inference_geo` batch as a September 2026 release. The primary release notes date it 7 August 2026. A second aggregator presented GitHub Agentic Workflows as a new technical preview. It entered technical preview on 13 February 2026 and public preview on 11 June 2026, and this blog covered it in Orders 033 and 034.

Both were caught by opening the changelog. The check takes two minutes and it has now paid four times in three editions.

## What changes here

1. **Adopt "AI-generated code is unverified input" as this factory's written rule, in the Pentagon's words.** Put it at the top of the rules file. It is better than any phrasing produced here, because it defines a category instead of prescribing an effort.
2. **Start the model manifest this week, on every repo.** For each generated or modified change, record the model, the version, and the significant inputs used to generate or test it. Append it to the ledger, which is already append-only. It costs one line at generation time and cannot be reconstructed in an audit. CareTime, TimeForCare and MaterialsAndPractices already sell to buyers who ask for evidence packages, so this row is a product feature.
3. **Write the human-approval rule by functionality class, not by repository.** The instruction gates on security-critical and safety-critical functionality. That is sharper than "regulated repos are human-gated", because a low-stakes repo can still hold an auth path. Name the classes once: authentication, authorization, cryptography, data export, anything touching protected health information, anything producing evidence for a state agency.
4. **Make the tool-definition fingerprint a standing check.** Record a fingerprint of every MCP server's tool definitions at approval. Compare on every reconnect. Alert on drift and require renewed approval. It is a small amount of compiled code, it needs no third-party dependency, and it defeats the exact evasion Deadbugz was built around.
5. **No unauthenticated MCP server, in any repo, ever.** The measurement says the default public server has none. This factory does not need to evaluate servers one at a time. It needs a rule that excludes the distribution.
6. **Keep regulated work human-gated. The new platform controls do not change that.** Server-side evaluation and `inference_geo` are real improvements. Neither replaces a named human approving a change that produces electronic visit verification evidence. What `inference_geo` buys is that a hosted option becomes evaluable. Evaluable is not approved.
7. **Take the `ant apply` pattern, not the product.** Agent configuration lives in files, gets reviewed in a pull request, and is pinned by a lockfile so CI and the laptop agree. This factory can build that shape with its own files and no dependency. Right now agent behavior is console state and habit.
8. **Low-stakes repositories carry the experiments.** MeowPassword, weathergalactic and sloth take the model manifest, the fingerprint check and the functionality-class rule, in that order. Prove the manifest row is one line and not a project before it goes near the regulated three.


## Sources

### The instruction

- [DefenseScoop, *Pentagon sets procedures for AI-assisted software development*](https://defensescoop.com/2026/09/14/pentagon-sets-procedures-for-ai-assisted-software-development/), Jon Harper (14 September 2026). Secondary, with direct quotations from the instruction.
- [DoD Instruction, *Accelerated Mission Software*](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/843001p.PDF?ver=gzVBhtfWXuXkLWhoEqMsEg%3d%3d). Primary. 37 pages, signed 31 August 2026, effective 8 September 2026.


### Platform controls

- [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview). Primary. 10 September 2026: `auto` permission policies and `ant beta:sessions connect`. 3 September 2026: `ant apply` and the lockfile. 7 August 2026: session budgets, advisor and `inference_geo`.


### The MCP supply chain

- [Pillar Security, *Deadbugz: Currently Active MCP Supply-Chain Campaign*](https://www.pillar.security/blog/deadbugz-currently-active-mcp-supply-chain-campaign), Ariel Fogel (12 August 2026). Primary. The three-call trigger, the 23 pull requests, the indicators of compromise, and the fingerprint recommendation.
- [arXiv 2608.00150, *Exposed by Design: A Dynamic Security Assessment of Internet-Facing MCP Servers at Scale*](https://arxiv.org/abs/2608.00150). Primary. Four runs across July 2026. Every figure in the table above.
- [Adversa AI, *Top MCP security resources, September 2026*](https://adversa.ai/blog/top-mcp-security-resources-september-2026/), Sergey Malenkovich (7 September 2026). Secondary. The three August CVEs and the defense walkthroughs.
- [CVE-2026-73498](https://nvd.nist.gov/vuln/detail/CVE-2026-73498), [CVE-2026-67357](https://www.cve.org/CVERecord?id=CVE-2026-67357) and [CVE-2026-19956](https://www.cve.org/CVERecord?id=CVE-2026-19956). Primary.


### The date errors

- [GitHub Changelog, technical preview](https://github.blog/changelog/2026-02-13-github-agentic-workflows-are-now-in-technical-preview/) (13 February 2026) and [public preview](https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview/) (11 June 2026). Primary. Cited only to date the aggregator error.


### Prior editions referenced

- [Confidence is not a control](2026-09-14-confidence-is-not-a-control.html) (14 September 2026). The Harness survey, the Agents API, and the build-against-buy figures.
- [Before the question](2026-09-05-before-the-question.html) (5 September 2026) and [The context tax](2026-09-03-the-context-tax.html) (3 September 2026). GitHub Agentic Workflows, covered at the time.


*Vendor and blog figures indicate direction, not audited benchmarks. The DoD instruction is a primary government document. Its requirements are stated, not measured. The arXiv measurement covers only internet-facing servers that passive discovery could find, so it says nothing about private or internal MCP deployments. The Pillar attribution is to a public account and its observable infrastructure, not to an identified operator.*


---

Canonical copy: [www.river.io/blog/posts/2026-09-15-unverified-input.html](https://www.river.io/blog/posts/2026-09-15-unverified-input.html). Mirrored into this wiki. The river.io blog is the source of truth.
