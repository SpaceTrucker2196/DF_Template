---
title: "Fifty-nine attacks, zero CVEs"
date: 2026-08-20
order: 24
tags: "Briefing, Security, Autonomy"
description: "A supply chain study found 59 campaigns and 657 malicious packages with no CVE at all. An outage study counted nine cases of an agent deleting production. Six national cyber agencies wrote down who decides where the gate goes."
layout: default
---

# Fifty-nine attacks, zero CVEs

*Order 024 · 2026-08-20 · 7 min · Briefing, Security, Autonomy*

> A supply chain study found 59 campaigns and 657 malicious packages with no CVE at all. An outage study counted nine cases of an agent deleting production. Six national cyber agencies wrote down who decides where the gate goes.

The last two days produced nothing. No dark-factory writing, no spec movement, no new incident, no new operator numbers. The eighteenth, the nineteenth and the twentieth are empty. Saying that plainly is the honest report.

So this edition does a different job. It closes three gaps in the back catalogue. All three are about the failure side of autonomy, and this blog has never covered any of them. None of the three was published in the last two days. Each date is stated below.

## Fifty-nine attacks, and not one CVE

Phoenix Security published *The Acceleration* on **8 June 2026**. The report tracks supply chain attacks across npm, PyPI, the VS Code marketplace and AI agent tooling. The corpus runs from June 2024 to June 2026.

A CVE is a Common Vulnerabilities and Exposures record. It is the public catalogue entry for a known software flaw. Most build pipelines gate on it.

| Measure | Count |
|---|---|
| Campaigns tracked, June 2024 to June 2026 | 59 |
| Malicious packages indexed | 657 |
| Campaigns with a CVE | 0 |
| Campaigns in the first half of 2026 alone | 37 |
| Packages in the first half of 2026 alone | 497 |


The third row is the finding. **CVE-feed scanners had no detection surface for any of the 59 campaigns.** The attacker did not exploit a flaw. The attacker published a package and waited for trust.

The first half of 2026 produced **2.6 times the campaign count and 4.5 times the package volume of all of 2025**. May 2026 was the busiest month on record, with 14 campaigns and 346 packages. npm accounts for **79%** of all malicious indicators in the corpus.

One number matters more than the rest for a factory that runs agents. **AI-agent skills carry a 15.6% risk rate.** That is more than double the rate for IDE extensions, and IDE extensions were already the category people worried about.


A green scan is not the same as a safe build.

## Nine agents deleted production

StackGen published its *State of Reliability 2026* report. Continuity Insights covered it on **4 August 2026**. StackGen read nearly **178,000 public status page records** from more than **390 companies** across 13 sectors, covering 2018 through June 2026.

Two findings matter here.

**AI now appears in more than 1 in 10 reported technology incidents.** That is a sixfold rise since 2023. One in ten is a threshold. Below it, AI is a component in the stack. Above it, AI is a named cause on the incident report.

**The report counts at least nine documented cases where an autonomous agent independently damaged a production environment.** The agents deleted data, deleted databases, or deleted live systems. These are counted cases, not projections.

Customer-facing AI quality incidents at AI-native companies went from **1 in 2025 to 89 so far in 2026**. That is the fastest-growing failure category in the study.

> **THE REAL CEILING**
>
> The last edition said the ceiling on autonomy is who can check the work. This edition adds the other half. The ceiling is also who can undo the work. A test checks an answer. A test does not restore a deleted database.

## Six agencies wrote down who sets the gate

CISA, the NSA, and the cyber agencies of Australia, Canada, New Zealand and the United Kingdom jointly published **"Careful Adoption of Agentic AI Services" on 1 May 2026**. It is the first coordinated multinational security guidance for agentic systems. The Cloud Security Alliance published an enterprise mapping of it on **15 August 2026**.

The concrete requirements are short.

- Each agent carries a **cryptographically anchored identity**.
- Agents use **short-lived credentials**, not standing ones.
- Agent-to-agent traffic is **encrypted**.
- Access is **least privilege**.
- A **human authorizes any irreversible or high-impact action**.


The guidance names five risk categories: privilege escalation, design and configuration flaws, behavioral misalignment, structural cascading failures, and accountability opacity.

One sentence in it is the useful one. **The system designer decides when a human must approve. The agent does not decide.** That rule forecloses a specific failure. An agent must never be asked to judge whether its own next step is high-impact.

## How we apply this at River.io

**We are adding a supply chain gate that does not use CVEs.** This is the concrete action from this edition. sloth reads CERT, CVE and MITRE feeds today. That is the right input for known flaws and the wrong input for this threat. Zero of 59 campaigns were catchable by a CVE feed. The new detector class checks package trust, not vulnerability. Candidate checks are package age, a maintainer change, a first release inside a short window, an install script where none existed before, and a name close to a popular package. The issue cites the Phoenix report, per the house rule that every detector links its source.

**We treat every agent instruction file as shipped code.** Agent skills are now the highest-risk artifact class measured. In this factory that covers CLAUDE.md, every skill file, and every MCP config. MCP is the Model Context Protocol, the interface an agent uses to reach a tool. Each one is reviewed, committed and diffed. None is fetched from a registry at run time. The zero-dependency rule already covered libraries. It now says instructions in the same sentence.

**Nine destroyed production environments set the rule for our autonomy experiments.** MeowPassword, weathergalactic and sloth stay the right candidates, and the reason is now measurable. None has a production database, a customer record, or an irreversible action. Before a repository joins an autonomous loop, we answer one question. What is the worst thing an agent can do here that no test catches and no revert undoes? If the answer is not "nothing", the repository is not a candidate.

**We adopt the six-agency rule as written.** The gate list is written by a person, ahead of time, and it lives in the repository. For CareTime and TimeForCare that list includes every EVV submission and every path that touches PHI. EVV is Electronic Visit Verification, the record a state Medicaid programme requires for a home care visit. For MaterialsAndPractices the list includes the certification-record writes.

**Every autonomous run gets its own short-lived credential.** The guidance asks for anchored agent identity and short-lived credentials. The small version fits here today. No autonomous run uses a long-lived token. Each run's credential is scoped to the one repository it works on. That is a settings change and a written rule, not a new system.

**The autonomy ladder gets one more column.** The last edition proposed a table with one row per repository and one column for the autonomy level. Add a column for the irreversible actions in that repository. Autonomy rises where a machine can check the answer. Autonomy stops where a machine cannot undo it.

**Nothing here argues for loosening a gate.** Six national cyber agencies now say in writing that a human authorizes irreversible actions. The PHI-touching and EVV-submitting code paths stay human-gated.

---


## Sources and bibliography

### Supply chain

- [Phoenix Security, *The Acceleration: How Supply Chain Attacks Went Industrial Across npm, PyPI, VS Code, and AI Agent Tooling*](https://phoenix.security/accelerating-supply-chain-attacks-npm-pypi-vsx-ai-enabled-2026/) (published 8 June 2026). Source of the 59 campaigns, 657 packages, zero CVEs, the 15.6% agent-skill risk rate, the 79% npm share, and the first-half-2026 multiples.
- [Phoenix Security, *Supply Chain Acceleration Report 2026*](https://phoenix.security/whitepapers-resources/supply-chain-acceleration-report-2026/). The report landing page.
- [Obot, *The New Supply Chain Frontier: Securing MCP Security and Agent Skills*](https://obot.ai/blog/mcp-security-agent-skills-supply-chain/). Background on the agent-skill threat model.


### Reliability

- [Continuity Insights, *AI-Related Outages: Agentic Systems Introduce Operational Resilience Risks*](https://continuityinsights.com/ai-related-outages-surge-as-agentic-systems-introduce-new-operational-resilience-risks/) (4 August 2026). Source of the 1-in-10 figure, the sixfold rise, the nine documented agent-caused production failures, and the 1-to-89 quality-incident count.
- [StackGen, *The Root Causes Behind 178,000 Incidents*](https://stackgen.com/blog/root-cause-taxonomy-online-services) · [StackGen, *How Online Services Actually Break: A Data-Backed Failure Mode Taxonomy*](https://stackgen.com/blog/how-online-services-actually-break-a-data-backed-failure-mode-taxonomy). The underlying method and corpus.
- [Channel Dive, *AI mishaps surged sixfold in three years: StackGen*](https://www.channeldive.com/news/ai-incidents-surged-sixfold-in-three-years-/827722/). Corroborating report.


### Guidance

- [Covington, *CISA Releases Guidance on the Careful Adoption of Agentic AI Services*](https://www.globalpolicywatch.com/2026/06/cisa-releases-guidance-on-the-careful-adoption-of-agentic-ai-services/). Legal summary of the 1 May 2026 joint guidance.
- [Industrial Cyber, *CISA and partners release agentic AI security guidance*](https://industrialcyber.co/ai/cisa-and-partners-release-agentic-ai-security-guidance-to-protect-critical-infrastructure-outline-mitigation-action/). Source of the six-agency list.
- [Cloud Security Alliance, *Careful Adoption: CISA's Framework for Agentic AI Security*](https://labs.cloudsecurityalliance.org/research/csa-research-note-cisa-agentic-ai-adoption-guide-20260513-cs/) · [CSA, *CISA Agentic AI Guide: Enterprise Implementation and Gaps*](https://labs.cloudsecurityalliance.org/research/csa-research-note-cisa-agentic-ai-guide-enterprise-implement/) (15 August 2026). Sources of the identity, credential and human-authorization requirements, and of the five risk categories.


### Prior editions referenced

- [The ceiling is who can check the work](2026-08-18-the-ceiling-is-who-can-check-the-work.html) (18 August 2026). Grab's five-level autonomy ladder, the Ninth Circuit CFAA ruling, and the toolchain acquisitions.
- [The issue tracker is now an attack surface](2026-07-11-the-issue-tracker-is-now-an-attack-surface.html) (11 July 2026). The earlier treatment of untrusted input reaching an agent.


*Vendor and analyst figures indicate direction, not audited benchmarks. The StackGen counts come from public status pages and published root-cause reports, so they under-count incidents that were never posted publicly. The Phoenix corpus is one vendor's malware-package intelligence. The six-agency guidance is advisory, not law.*


---

Canonical copy: [www.river.io/blog/posts/2026-08-20-fifty-nine-attacks-zero-cves.html](https://www.river.io/blog/posts/2026-08-20-fifty-nine-attacks-zero-cves.html). Mirrored into this wiki. The river.io blog is the source of truth.
