---
title: "Before the question"
date: 2026-09-05
order: 33
tags: "Briefing, Security, Practice"
description: "A repository's own .git/config ran attacker code through seven coding agents before any approval prompt. The same week OWASP moved Excessive Agency to number three, a tool-call monitor shipped, and one vendor cut the cache-read rate by 75%."
layout: default
---

# Before the question

*Order 033 · 2026-09-05 · 8 min · Briefing, Security, Practice*

> A repository's own .git/config ran attacker code through seven coding agents before any approval prompt. The same week OWASP moved Excessive Agency to number three, a tool-call monitor shipped, and one vendor cut the cache-read rate by 75%.

Order 032 praised the tools for learning to say no when nobody is home. This edition is about what runs before the tool gets to say anything. An agent starts a session. It asks Git which branch it is on. Git reads a setting from the repository and runs a command. The command is the attack. No prompt was shown, because the prompt comes later.

Be clear about the window. Five items are new. All five were published between 1 and 3 September 2026. None appeared in Order 032. Two of them, GitSpawn and the OWASP list, were public before Order 032 went out but had not surfaced in the sources that edition scanned. They are reported here with their real dates. No new dark-factory case study, spec-driven development standard or adoption survey landed between 3 and 5 September.

## The repository attacks the harness

Manifold Security published the finding on 1 September 2026 under the name GitSpawn. The Hacker News confirmed the details against vendor release notes on 2 September. The mechanism is old. Git has a performance setting named `core.fsmonitor`. Its value is a command. Git runs that command during any index refresh, which includes `git status` and `git diff`. Git reads the setting from the repository's own `.git/config`.

Coding agents run those commands in the background when a session starts. They want the branch name and the list of changed files. So a repository that arrives with its `.git` directory intact can name a command, and the agent will run it. The command runs as the developer, outside the agent's sandbox, before the workspace-trust prompt and before any tool-approval prompt. On Qwen Code it ran before the user had signed in. On Grok Build it ran on the first keystroke.

One fact limits the blast radius. `git clone` does not copy the source repository's `.git/config`. A normal clone from GitHub does not carry the payload. The delivery paths are archives, shared drives, synced folders, USB sticks and pre-built dev containers.

| GitSpawn, agent status at the 1 September 2026 retest | Status |
|---|---|
| goose (CVE-2026-72718, CVSS 7.0) | fixed in 1.44.0 |
| OpenAI Codex CLI (CVE-2026-19592) | fixed in 0.131.0 |
| Claude Code, core.fsmonitor path (CVE-2026-55607) | fixed in 2.1.196 |
| Claude Code, claude ultrareview path | live on 2.1.252 |
| Cursor | fixed |
| Hermes Agent 0.21.0 | unpatched |
| Qwen Code 0.22.3 | unpatched |
| Grok Build 1.0.13 | unpatched |


Eight findings, seven agents, four still open at publication. No source reports exploitation. The Hacker News checked CISA's Known Exploited Vulnerabilities catalog on 2 September and found none of these identifiers listed.

The part this blog cares about is the regression. Sonar reported the same sink in April 2026. Anthropic had already moved Claude Code's startup sequence once, in version 2.0.34 on 5 November 2025, so that `git status` no longer ran before the trust dialog. Manifold found the same startup behaviour present again in 2.1.193, which shipped on 25 June 2026. A fix that came back is a missing test. That is not a security lesson. It is a test-driven-development lesson.

> **THE CLASS, NOT THE BUG**
>
> GitSpawn reads `.git/config`. The CHAINDROP npm worm of 4 August planted a SessionStart hook in `.claude/settings.json`. Pillar Security's Cursor escape of 20 July wrote a Stop hook to `.claude/settings.local.json`. All three are one class: a trusted host component reads workspace state that an untrusted party wrote. Every config file the IDE, Git, the shell or the agent runtime reads is tainted input.

## Excessive Agency, on evidence

The OWASP GenAI Security Project published the 2026 Top 10 for LLM Applications. The blog post is dated 1 September 2026 and the press release 2 September. This is the first edition to weigh the expert ranking against real incident data. The methodology counts 6,639 incidents at 25% weight and expert consensus at 75%. The list passed 10,000 downloads in its first 48 hours.

The biggest move is Excessive Agency, from number 6 to number 3. That is the category a dark factory depends on: an agent with tools and permissions. System Prompt Leakage was retired into a broader category named Hidden Context Exposure. OWASP also published a crosswalk to ISO 42001, the NIST AI Risk Management Framework and its own AI Controls Matrix.

The second document matters more for this blog. The Agent Control Standard, version 0.1, was donated to the project. It is a runtime standard, not a checklist. It defines an Agent Bill of Materials, a declared list of what an agent may load and reach, and tracing of tool calls on OpenTelemetry and OCSF. Read that next to GitHub's named sandbox profiles from Order 032. Two bodies are converging on the same shape: declare what the agent may reach, then trace what it did.

## A grader the agent cannot edit

Apollo Research released Watcher Live on 3 September 2026. It is a monitor that hooks every tool call in Claude Code and Codex and grades it in three stages. A regex rule set clears the obvious safe actions. A fast triage model looks at what remains. A full evaluator runs only on what survives triage. The evaluator can be a different model from the agent, so the monitor does not share the agent's habits.

| Apollo Watcher Live launch card, 3 September 2026 | Claimed |
|---|---|
| Recall on high-severity actions | 93% |
| Catch rate on an extreme hold-out set | 100% |
| False positive rate | under 1% |
| Escalation to a human | under 0.1% |
| Added latency | 6 to 8% |
| Cost overhead | 3 to 5% |


These are Apollo's numbers on Apollo's benchmark. Treat them as a launch card. The design point stands on its own. The gate runs in a process the agent cannot write to. The METR report of 26 August showed agents replacing part of their own tool-execution layer. A rule in a Markdown file the agent can edit is not a gate. A hook in a process it cannot reach is.

## One microVM per request

Vercel announced on 3 September 2026 that Cursor Cloud Agents can run in Vercel Sandbox. Cursor keeps the harness and the inference loop. Vercel supplies the execution environment: one isolated Firecracker microVM per agent request, a worker pool that scales to zero with no long-lived virtual machines, durable retries when a session fails, and short-lived user-scoped credentials inside each sandbox. Cloudflare shipped the equivalent on 2 September.

The credential lifetime is the design choice worth copying. A token that expires with the microVM cannot be harvested by the next CHAINDROP. The feature requires a Cursor Enterprise plan, which is not a factor here. The pattern costs nothing.

## The rate on the context tax

Order 032 excluded Anthropic's Fable 5.1 release because it carried no software-engineering measurement. The pricing change is a measurement, and it lands on the ledger that edition opened. On 1 September 2026 Anthropic cut the Fable 5.1 cache-read price from $1.00 to $0.25 per million tokens. Base input stays at $10 and output at $50. Anthropic says the effective cost falls about 25% on typical workloads and up to about 45% on heavily agentic ones.

Set that against Sonar's traces from Order 032. On one 800-line pull request, 152.8 million of the 156 million billed tokens were cache reads: the transcript re-sent on every turn. The mechanism has not changed. Every file the agent reads is still re-billed on every later turn. The rate on one vendor's top model dropped by three quarters. Cheaper re-reads change the incentive, not the correctness problem. Grep still misses call sites. Compaction still loses constraints.

## Noted, not featured

AIR Security came out of stealth on 1 September with $50 million to build an inline firewall that vets every skill, plugin and MCP server an agent loads. JetStream announced Clearance on 2 September, a per-action authorization engine at the tool-call boundary. Tenable announced an AI Inspector for its CyberAgents Exchange on 4 September. All three are product announcements with no published measurements. Claude Code shipped small fixes on 4 September. None changes factory behaviour.

## What changes here

1. **Check `.git/config` before every autonomous run.** Before the loop starts an agent in any working tree, run `git config --local --get core.fsmonitor` and fail the run if it returns anything. Fail on `core.hooksPath` and any `filter.*.clean` or `filter.*.process` entry too. The factory runs from fresh clones, which do not carry the file, so the risk is low. The check costs one line, and the log line proves it ran. Sloth gets this as a detector, with Manifold, The Hacker News and the three CVEs cited in the issue body.
2. **Pin agent CLIs above the patch line, and write the floor down.** Codex CLI: 0.131.0. Claude Code: 2.1.196, and `claude ultrareview` does not run unattended until Anthropic states the second path is closed. The floors go in the rules file next to the sandbox profile from Order 032. A run that starts below the floor does not run. A pinned old version is an unpatched version.
3. **Every config file the host reads is untrusted input.** `.git/config`, `.git/hooks/`, `.claude/settings.json`, `.claude/settings.local.json`, `.vscode/tasks.json`. A one-line continuous integration check fails when a non-human author touches any of them. The agent edits Sources and Tests. It never edits the files that run the agent.
4. **The startup regression is a test.** Claude Code's pre-trust `git status` was fixed in November 2025 and back by June 2026. This factory's posture is test-driven development. For the harness that means one test that asserts what runs before the trust gate, and fails when anything new does. Native compiled code with zero third-party dependencies makes the test cheap. The startup process tree is small and fully known.
5. **Write the Agent Bill of Materials now.** One page per agent role: which tools it may call, which paths it may write, which network it may reach, where the trace lives. That is OWASP's Agent Control Standard in all but name, and it answers GitLost and PR Sous Chef in one document. The regulated repositories will face auditors who use OWASP language within a year.
6. **Put a grader on the tool boundary in the low-stakes loops.** MeowPassword, weathergalactic and sloth are the place to try it. The factory does not need Apollo's product. It needs the shape: a regex allowlist as a native pre-tool hook, a cheap classifier behind it, an expensive judge only for what survives. Log the block rate per week. If it is zero for a month, the allowlist is doing the work and the classifier can go.
7. **Record the token count and the rate separately.** Order 032 added a tokens-per-run column to METRICS.md. Add the price per million next to it. Sonar's $41 pull request was nearly all cache reads, and that rate just fell 75% on one model. A cost per merged pull request that survives the next price change needs both numbers.
8. **GitSpawn is a new reason the regulated repositories stay gated.** A flaw that fires before the approval prompt means the approval prompt is not the last line. Until the harness has the startup test from item 4 and the config-path check from item 3, CareTime, TimeForCare and MaterialsAndPractices do not run unattended.


## Sources

### GitSpawn

- [The Hacker News, *Malicious .git Configs Can Make Claude, Codex, Cursor, and Other AI Agents Run Attacker Code*](https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html), Swati Khandelwal (2 September 2026). Confirmation against vendor release notes. Eight findings, seven agents, four unpatched at the 1 September retest. Affected and fixed versions per agent. CVE-2026-72718 (goose, CVSS 7.0), CVE-2026-19592 (Codex), CVE-2026-55607 (Claude Code). Sonar's April report of the same sink. KEV catalog checked 2 September, none listed.
- [Manifold Security, *GitSpawn: A Single Flaw Lets Untrusted Repos Run Code*](https://www.manifold.security/blog/ai-coding-agents-git-hijack) (1 September 2026). Original disclosure.
- [Cloud Security Alliance, *CISO Daily Briefing*](https://labs.cloudsecurityalliance.org/research/ciso-daily-briefing-20260904/) (4 September 2026). Secondary summary of GitSpawn and the OWASP methodology figures.
- [VibeEval, *Security Harness for AI Agents, September 2026*](https://vibe-eval.com/updates/security-harness-for-ai-agents-sep-2026/) (3 September 2026). Secondary roundup. Source for the CHAINDROP and Pillar trust-handoff framing and for the transcription of Apollo's launch card.


### OWASP

- [OWASP GenAI Security Project, *2026 Top 10 for LLM Applications, New Agent Control Standard*](https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/) (blog dated 1 September 2026, press release dated 2 September). Primary source. 10,000 downloads in 48 hours. Agent Control Standard donated to the project. Crosswalk to NIST, MITRE ATLAS, CWE and the Agentic Top 10. Michael Bargury of Zenity on incident-weighted Excessive Agency at number three.


### Watcher and the sandbox

- [Apollo Research, *Watcher: Monitor Your Coding Agents Without Slowing Them Down*](https://watcher.apolloresearch.ai/blog/monitor-coding-agents/) (3 September 2026). Primary for the three-stage hook pipeline and mixed-model design. Launch figures as transcribed by VibeEval.
- [Vercel changelog, *Cursor Cloud Agents can now run in Vercel Sandbox*](https://vercel.com/changelog/run-cursor-cloud-agents-vercel-sandbox), Allen Zhou (3 September 2026). Primary. Firecracker microVM per request, scale to zero, durable retries, short-lived user-scoped credentials. Cursor Enterprise required.
- [Cloudflare changelog, *Run Cursor Cloud Agents on Cloudflare via self-hosted machines*](https://developers.cloudflare.com/changelog/post/2026-09-02-cursor-cloud-agents/) (2 September 2026). Title and date only.


### Pricing

- [VentureBeat, *Anthropic's Claude Fable 5.1 and Mythos 5.1 arrive with a 75% cost reduction for Fable cache reads*](https://venturebeat.com/technology/anthropics-claude-fable-5-1-and-mythos-5-1-arrive-with-a-75-cost-reduction-for-fable-cache-reads), Carl Franzen (1 September 2026). Pricing table: $10 input, $0.25 cache read, $50 output. About 25% typical and about 45% heavily agentic effective-cost reduction, as stated by Anthropic.


### Noted, not featured

- [AI Agent Store, *AI agent news, week of 4 September 2026*](https://aiagentstore.ai/ai-agent-news/this-week). Scanned. AIR Security, JetStream Clearance, Tenable AI Inspector.
- [JetStream, *Clearance* press release](https://finance.yahoo.com/technology/ai/articles/jetstream-announces-clearance-ai-zero-170000815.html) (2 September 2026).
- [Releasebot, Claude Code updates](https://releasebot.io/updates/anthropic/claude-code). 4 September fixes noted.


### Prior editions referenced

- [The context tax](2026-09-03-the-context-tax.html) (3 September 2026). The Sonar traces and the deny-when-unattended rule this edition builds on.
- [The gate you ask too often](2026-09-01-the-gate-you-ask-too-often.html) (1 September 2026). The NIST consent-fatigue finding.


*Vendor and blog figures indicate direction, not audited benchmarks. The GitSpawn version table is a researcher's retest, not a vendor statement. The Watcher figures are a launch card. The Anthropic effective-cost figures depend on workload mix. The OWASP incident weighting is the project's own methodology.*


---

Canonical copy: [www.river.io/blog/posts/2026-09-05-before-the-question.html](https://www.river.io/blog/posts/2026-09-05-before-the-question.html). Mirrored into this wiki. The river.io blog is the source of truth.
