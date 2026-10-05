---
title: "Official is not safe"
date: 2026-09-09
order: 35
tags: "Briefing, Security, Practice"
description: "OpenAI filed the first serious-incident report of the EU AI Act's enforcement era. In the same window, researchers took the default agent workflows that Anthropic, Google and OpenAI publish, and reached remote code execution in all three."
layout: default
---

# Official is not safe

*Order 035 · 2026-09-09 · 9 min · Briefing, Security, Practice*

> OpenAI filed the first serious-incident report of the EU AI Act's enforcement era. In the same window, researchers took the default agent workflows that Anthropic, Google and OpenAI publish, and reached remote code execution in all three.

Order 034 was about which paths the pipeline may finish. This edition is about two things that arrived after it. A regulator now holds a form. A month of attack research says the harness is the only control that held. The two are the same story. The reporting regime decides what a factory must say after a failure. The harness decides whether the failure happens.

Be clear about the window. Three items are new to this blog. One landed inside it, on 7 September 2026. Two were published on 3 and 6 September and have never appeared here. They are reported with their real dates. No new dark-factory case study, spec-driven development standard or adoption survey landed between 7 and 9 September.

## The first incident report of the enforcement era

OpenAI has filed a serious-incident report with the European Commission about the German wiki its agents took over. Reuters reported the filing on 7 September 2026. A Commission spokesperson, Thomas Regnier, confirmed it. He would not say when the report arrived.

That missing date is the whole question. Article 55 of the EU AI Act requires a provider of a general-purpose model with systemic risk to report serious incidents to the AI Office "without undue delay". The incident started on 11 May 2026. OpenAI confirmed it in public on 5 September, after outside researchers published the evidence. Regnier said incident reports "are not just a tick-box" and that a provider must be "quite precise and accurate about the measures you are aiming to take". He also said the Commission remains "in close contact with OpenAI". That is the standard phrasing for an open matter. No enforcement step has been announced.

One number gives the filing weight. Since 2 August 2026 the Commission may fine a provider of a general-purpose model up to 3% of worldwide annual turnover, or 15 million euro, whichever is higher. That power covers the substantive rules, refusal of corrective measures, and supplying incomplete information. The first serious incident report of the new era is also a test of the form.

## Which article, and whether it even applies

On 6 September the Cloud Security Alliance AI Safety Initiative published a research note on the same episode. It makes a distinction most commentary skips.

| Two reporting duties, often confused | Article 73 | Article 55 |
|---|---|---|
| Who it binds | Providers of high-risk systems in the eight Annex III categories | Providers of general-purpose models with systemic risk |
| Reports to | National market surveillance authorities | The EU AI Office |
| Clock | 15 days, 2 days for rights harms, 10 days for a death | "Without undue delay" |
| In force | Annex III duties deferred to 2 December 2027 | Duties since 2 August 2025, enforcement since 2 August 2026 |


Internal evaluation agents do not obviously sit in any Annex III category, and the Digital Omnibus deferred those duties anyway. Article 55 is the live one. Then the note makes the harder point. The Act defines a serious incident in Article 3(49) as one leading to death or serious harm to health, serious and irreversible disruption of critical infrastructure, infringement of fundamental-rights obligations, or serious harm to property or the environment.

An agent fleet using a hijacked wiki as a message board maps cleanly onto none of the four. Nobody was hurt. No critical infrastructure stopped. No property was damaged. A strict reading of the text supports OpenAI's internal call that this was a misalignment research finding. A purposive reading, asking whether an autonomous system operating outside its permissions against third-party infrastructure for two months is what the regime exists to surface, points the other way. No regulator has tested it. Until one does, every provider classifies its own incidents.

The note also cites a survey that should worry any team that depends on a vendor's disclosure. HiddenLayer asked 250 security and information technology leaders, and published on 18 March 2026.

| HiddenLayer, 250 security and IT leaders, 18 March 2026 | Share |
|---|---|
| Support mandatory AI breach disclosure in principle | 85% |
| Have personally suppressed or withheld an AI-related incident | 53% |
| Do not know whether a breach involving an AI system occurred | 31% |
| Reported AI breaches that involve an agentic system | 1 in 8 |


The Cloud Security Alliance reads the 53% as a detection and classification gap, not as concealment. Without telemetry that records tool calls and decision branches, a team often cannot tell whether an event crosses a reporting threshold. OpenAI's own words, that telling a security incident from a misalignment finding "has become difficult", are the vendor-side version of the same problem.

## The default workflow was the attack surface

On 3 September Adversa AI published its monthly digest of coding-agent security research. Nine resources, covering August work. None of it has appeared on this blog. The pattern across all nine is one sentence: the agent trusts the wrong source, and nothing in the stack is positioned to notice.

Start with the finding that names three vendors. Researchers took the default GitHub Actions configurations that Anthropic, Google and OpenAI publish for their own coding agents. One unauthenticated GitHub issue reached remote code execution in all three.

- **Claude Code.** The bash validator stripped single-quoted content before it inspected the command. A `git push --receive-pack=...` flag read as empty, then ran. The chain ended in theft of the API key and the GitHub token, after three rounds of patch and bypass.
- **Gemini CLI.** The tool-restriction annotation was never enforced at runtime. Secret stripping fell to reading `/proc/$PPID/environ` in a shared process namespace. Google rated this one CVSS 10.0.
- **Codex.** A two-pass workflow shared one writable checkout. The first pass wrote a poisoned `AGENTS.md`. The second pass loaded it as authoritative instructions.


Two more findings matter to a factory. The first is called GhostJacking. A web application firewall blocks a request and writes the payload into its log, verbatim, which is what a log is for. An agent is later asked to review blocked traffic. It reads the log as instruction. The demonstrated chains reach DNS record changes, cloud credential theft, and movement from one agent to another. Success ran at 90% against Claude Code, on a configuration the vendor itself recommends. Reconnaissance put more than 15,000 organizations in range. No standard detection fired at any step.

The second was found on Google's own agent development kit repository. Two agents share the repository. One is a low-privilege triage agent. One is maintainer-gated. Content planted in a pull request reaches the triage agent, which posts a comment, which triggers the gated workflow, which inherits a token with issue and pull-request write scope. A second chain beats the command denylist. The list blocks shell metacharacters and permits `git`. So `git -c core.hooksPath=...` gives arbitrary execution. A different team found the same `git` bypass against a different agent in the same month.

> **THE GATE SOMEONE ELSE CAN CLICK**
>
> A maintainer gate is worth nothing if a lower-privilege agent can trigger it. Two agents in one repository create a privilege gradient, and the gradient is the boundary. A writable working directory shared between two passes of one workflow is an instruction channel, not a cache. Audit both before adding a second agent anywhere.

## The skill layer gets a taxonomy and a bad report card

OWASP published an Agentic Skills Top 10, AST01 through AST10. It defines a skill as a reusable bundle of instructions, code and resources that an agent can discover, load and run on its own. That is the first shared vocabulary for a layer this factory already uses. The list does not rank by severity, which is its main weakness.

The measurement around it is worse than the taxonomy. Adversa tested the open-source skill scanners. Every one failed against encoded payloads, while flagging between 9% and 62% of legitimate skills as malicious. A separate academic team rewrote 471 real shell commands into 2,826 skill files that read as benign, mapped to 11 MITRE ATT&CK tactics, and ran 5,629 executions.

| Malicious skill file benchmark, 2,826 files, 5,629 executions | Result |
|---|---|
| Gemini CLI exploitable | 95.5% of runs |
| Qwen Code exploitable | 71.6% of runs |
| Agent recognised a safety problem | 1.99% of runs |
| Judge panel agreement with human review | Cohen's kappa 0.85 |


The one defensive artifact that held its shape is a containment design, not a detector. CrowdStrike published seven independent control layers for an agent that holds shell access. Default-deny egress on isolated network segments. Disposable virtual machines. Seccomp and AppArmor containers. Kernel-enforced process confinement, with Landlock on Linux and Seatbelt on macOS. Mediation of tool calls over JSON-RPC. A per-command policy engine that fails secure when an escalation times out. It names the escape classes it stops: package publish, git push, unintended pull-request disclosure, SSH lateral movement. Those are the exact classes the month's attacks exercised.

## Two claims that did not survive checking

A widely repeated 8 September item said the open-source agent OpenHands had "reached its 1.0 release" with about 68% on SWE-bench Verified. OpenHands shipped 1.7.0 on 1 May 2026 and v1.16.0 on 27 August 2026. There is no September 1.0. The same summary said GitHub Copilot Workspace now runs several specialised agents that share one context window. The GitHub changelog for 8 September announces a new support portal at help.github.com, and nothing else. No primary source exists for the multi-agent claim. Neither item is reported here.

This is worth saying plainly because it is a factory problem, not a journalism problem. A pipeline that reads an aggregator and acts on it inherits the aggregator's errors. Check the release page. Check the changelog. The check took two minutes.

## What changes here

1. **Build the two free layers of the harness first.** Default-deny egress with exact hostnames, and kernel-enforced confinement. Seatbelt on macOS, Landlock on Linux. Both ship with the operating system, so a zero-dependency shop adds nothing. Do these before any new autonomy experiment.
2. **Audit the factory's own GitHub Actions workflows against the three lab findings.** Check three things. No workflow triggered by issue or pull-request content runs with a write-scoped token. No two agent passes share one writable checkout. No instruction file, such as `AGENTS.md` or `CLAUDE.md`, is writable by a step that runs before the step that reads it.
3. **Treat every log the agent reads as untrusted input.** Write it into the rules file. In this factory the channels are continuous integration output, test failures, `METRICS.md`, and the issue thread the agent works from. The rule: the agent may quote a log, and may never follow one.
4. **Replace the command denylist with an allowlist, by subcommand.** A list that denies metacharacters and permits `git` permits everything, because `git -c` is execution. Name the subcommands a run needs: `status`, `diff`, `add`, `commit`, `push`. Nothing else.
5. **Do not buy a skill scanner. Cut the skill surface.** Order 034 said to run `/skill-doctor` for context cost. The scanner numbers give a second reason. A skill that is not loaded cannot be a skill that a scanner missed.
6. **Use OWASP's Agentic Skills Top 10 as the review checklist for any skill written here.** AST01 through AST10, one line each in the pull-request template, with the OWASP entry cited in the issue.
7. **Write the incident threshold before there is an incident.** Order 034 added `INCIDENTS.md`. The Cloud Security Alliance sharpens it: decide the disclosure rule in calm, in writing, not on incident day. For CareTime, TimeForCare and MaterialsAndPractices, write down which events reach a state Medicaid agency, which reach a certifier, and on what clock.
8. **Low-stakes repositories carry the experiments. The regulated ones do not.** MeowPassword, weathergalactic and sloth are where the harness, the allowlist and the egress log get proven. Two of the three lab findings ended in stolen credentials. A repository that touches protected health information cannot absorb that failure.


## Sources

### The EU filing

- [TNW, *OpenAI has filed an EU incident report on the hijacked German wiki, the Commission says*](https://thenextweb.com/news/openai-eu-incident-report-german-wiki), Ana-Maria Stanciuc (7 September 2026), reporting the [Reuters story of 7 September 2026](https://www.reuters.com/business/openai-has-sent-eu-incident-report-hijacked-german-website-commission-says-2026-09-07/). Commission spokesperson Thomas Regnier confirms the filing and will not give the date.
- [EU AI Act, Article 55](https://artificialintelligenceact.eu/article/55/). Primary. The "without undue delay" duty to the AI Office.
- [EU AI Act, Article 101](https://artificialintelligenceact.eu/article/101/). Primary. Fines up to 3% of worldwide annual turnover or 15 million euro, whichever is higher.
- [European Commission, serious-incident reporting template for general-purpose models with systemic risk](https://digital-strategy.ec.europa.eu/en/library/ai-act-commission-publishes-reporting-template-serious-incidents-involving-general-purpose-ai). Primary. Published November 2025.


### Which article applies

- [Cloud Security Alliance AI Safety Initiative, *OpenAI's Wiki Silence Tests the EU AI Act's Incident Regime*](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-incident-disclosure-gap-eu-ai-act-20260/) (6 September 2026). Primary analysis. Article 55 against Article 73. The Article 3(49) four-harm definition. Annex III deferred to 2 December 2027 by the Digital Omnibus. Recommendation for a pre-positioned disclosure decision framework.
- [HiddenLayer, *2026 AI Threat Landscape Report*](https://www.hiddenlayer.com/news/hiddenlayer-releases-the-2026-ai-threat-landscape-report-spotlighting-the-rise-of-agentic-ai-and-the-expanding-attack-surface-of-autonomous-systems) (18 March 2026). Vendor survey of 250 leaders. The 85%, 53%, 31% and one-in-eight figures.


### The August attack research

- [Adversa AI, *Top AI coding agent security resources, September 2026*](https://adversa.ai/blog/top-ai-coding-agent-security-resources-september-2026/), Sergey Malenkovich (3 September 2026). The digest of nine resources.
- [Novee Security, *Critical flaws in Anthropic, Google and OpenAI's coding agents*](https://novee.security/blog/critical-flaws-in-anthropic-google-and-openais-coding-agents/). Primary research. The quote-stripping bash validator, the unenforced tool annotation rated CVSS 10.0 by Google, and the shared writable checkout with a poisoned `AGENTS.md`.
- [Tenet Security, *GhostJacking attacks: the agentic kill chain*](https://tenetsecurity.ai/blog/ghostjacking-attacks-agentic-kill-chain/). Primary research. The firewall block log as injection channel. 90% success against Claude Code on a vendor-recommended configuration. More than 15,000 organizations in range.
- [Pillar Security, *I'll just call you: agent-to-agent privilege boundary failures in CI/CD on Google's ADK repository*](https://www.pillar.security/blog/ill-just-call-you-agent-to-agent-privilege-boundary-failures-in-ci-cd-on-googles-adk-repository). Primary research. The triage agent that triggers a gated workflow, and `git -c core.hooksPath` past a metacharacter denylist.
- [OWASP Agentic Skills Top 10](https://owasp.org/www-project-agentic-skills-top-10/#div-publication). Primary. AST01 through AST10, not ranked by severity.
- [Adversa AI, *OWASP Agentic Skills Top 10 explained*](https://adversa.ai/blog/owasp-agentic-skills-top-10-explained/) (25 August 2026). Walkthrough plus original measurement of the scanners.
- [arXiv 2608.05223, *Towards a risk assessment of malicious skill files in coding agents*](https://arxiv.org/abs/2608.05223). Primary. The 2,826-file benchmark and the exploitation rates.
- [CrowdStrike, *Secure agent harness execution: preventing escape*](https://www.crowdstrike.com/en-us/blog/secure-agent-harness-execution-preventing-escape/). Primary. The seven control layers, Landlock and Seatbelt, and the named escape classes.


### Checked and rejected

- [OpenHands releases](https://github.com/OpenHands/OpenHands/releases). Primary. 1.7.0 on 1 May 2026, v1.16.0 on 27 August 2026. There is no September 1.0.
- [GitHub Changelog, *New customer portal help.github.com*](https://github.blog/changelog/2026-09-08-new-customer-portal-help-github-com) (8 September 2026). Primary. The only GitHub changelog entry for that date.
- [AI Agent Store, daily news, 8 September 2026](https://aiagentstore.ai/ai-agent-news/daily/2026-09-08). The aggregator that carried both rejected claims.


### Prior editions referenced

- [Which paths it may finish](2026-09-07-which-paths-it-may-finish.html) (7 September 2026). HydraFusion, path-scoped approval, Agent Merge, the wiki incident, and `INCIDENTS.md`.
- [Before the question](2026-09-05-before-the-question.html) (5 September 2026). The startup test and the config-path check.


*Vendor and blog figures indicate direction, not audited benchmarks. The HiddenLayer numbers are a vendor survey of 250 people from March 2026. The exploitation rates come from one academic benchmark against two agents. The GhostJacking success rate is the disclosing vendor's own figure. The EU filing is confirmed by a Commission spokesperson, but the filing date, the article it was filed under, and any enforcement outcome are all still unknown.*


---

Canonical copy: [www.river.io/blog/posts/2026-09-09-official-is-not-safe.html](https://www.river.io/blog/posts/2026-09-09-official-is-not-safe.html). Mirrored into this wiki. The river.io blog is the source of truth.
