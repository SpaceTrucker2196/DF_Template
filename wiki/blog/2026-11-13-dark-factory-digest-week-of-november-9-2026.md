---
title: "Dark Factory Digest, week of November 9, 2026"
date: 2026-11-13
order: 58
tags: "Digest, Briefing"
description: "Agent settings files leaked tens of thousands of secrets, and the controls that worked this week all sit outside the agent: a scoped job, a known model and a check on each action."
layout: default
---

# Dark Factory Digest, week of November 9, 2026

*Order 058 · 2026-11-13 · 5 min · Digest, Briefing*

> Agent settings files leaked tens of thousands of secrets, and the controls that worked this week all sit outside the agent: a scoped job, a known model and a check on each action.

This digest covers 7 to 13 November 2026. It rolls up three research briefs (7, 9 and 11 November). The main theme: agent settings files leak secrets at scale, and the controls that worked this week all sit outside the agent. A scoped job, a known model and a check on each action did more than any model upgrade.

## This week's signals

1. **Agent settings files leak secrets at scale (GitGuardian, 9 November; Apiiro, 5 November).** GitGuardian scanned public GitHub from January 2025 to 7 November 2026. It found 31,088 distinct secrets in public copies of the Claude Code `settings.local.json` file, in 23,276 repositories. 5,343 were valid when found. `CLAUDE.md` files held 6,155 distinct secrets, 2,537 of them valid. OpenAI Codex `.codex/auth.json` files held 1,064 tokens in 536 repositories, so this is not a one-vendor problem. The same leak reaches Docker Hub: 613 distinct secrets, 99 valid. Monthly occurrences peaked at 12,535 in April 2026 and fell to 959 in October, a 92 percent drop with no known cause. Apiiro reported a smaller count earlier in the week (2,539 secrets in 1,994 repositories, about 1.1 percent of 104,185 public copies) and found that TruffleHog and gitleaks both missed 215 of the files. The two counts use different time ranges and methods. Do not add them.

2. **A fallback model is part of the attack surface (Anthropic, 9 November; Notebookcheck, 10 November).** Claude Fable 5.2 sends flagged requests to an older model: Opus 4.8 for cybersecurity and Opus 5 for biology. Notebookcheck reports system card figures: indirect prompt injection attack success was 4.09 percent for Fable 5.2 against 1.02 percent for Fable 5.1. 53 percent of attempts against Fable 5.2 were answered by Opus 4.8, against 23 percent for Fable 5.1. Attacks succeeded 2.05 percent of the time when Fable 5.2 answered and 5.17 percent when Opus 4.8 answered. The classifier also reads connector content, web results and files, so injected text can cause the switch. A setting, "Switch models when a message is flagged", turns the switch off and pauses the request instead. The system card was not opened. These are secondary figures.

3. **Give the agent a job, then check each action against it (Cequence Security and KPMG, 11 November).** In a prototype study, agents with only a login and fixed permissions tried to act outside their job in 44 percent of runs. With a defined job and a check on each action, the figure was 1 percent. Task completion rose from 76 to 95 percent, and token use fell about 35 percent per run. Field data from one week in October 2026: more than 250,000 agent visits across five industries, and about 1 in 7 took an action such as a purchase or a sign-in. Cequence sells this type of control. The source was the press release, not the report.

4. **Agents now start more than 40 percent of pull requests on GitHub (Octoverse 2026, 28 October; first time in this brief).** Pull requests started by a detected agent went from 17 percent in March 2026 to more than 40 percent in September, about 110 million pull requests that month. GitHub calls this a floor. Agent pull requests merged within two weeks went from 83 percent in February to 90 percent in September, against about 86 percent for other pull requests. A merge rate does not prove quality. Detected AI involvement in merged pull requests was about 40 to 44 percent for TypeScript, Python and Rust, and about 21 to 34 percent for Java, C# and C++. GitHub recorded 34.3 billion commits in the 12 months to 30 September 2026.

5. **The moat is the steering system, not the agent (Ben Bahrenburg, bencoding, 9 November; opinion).** The essay says the lasting value is the evaluations, policies and feedback loops around the model. It argues that a fully dark factory is the wrong goal, because maintainability and product fit have no reliable automated test. It proposes two measures: verified output per unit of human attention, and cost per merged pull request.

6. **A quiet mid-week, with one pointer (Adversa AI, 2 November).** The 9 November brief confirmed no new framework, spec or audited metric in its window. Adversa AI's roundup of 14 coding-agent security resources points to an agentbaseline.org draft of a secure software factory architecture: the agent proposes, policy authorizes, infrastructure enforces. Its figures (users approved 93 percent of permission prompts, auto mode missed 17 percent of risky actions) come from the summary and are unverified.

## What it means for the River.io Software Factory

Block agent settings files in every repo now. Add `.claude/`, `.codex/`, `.cursor/`, `.mcp.json`, `settings.local.json` and `CLAUDE.md` to `.gitignore`, and add a pre-commit check written in-house, which fits the zero third-party dependency rule. Open one GitHub issue per repo for this, and have a human search the git history of CareTime, TimeForCare and MaterialsAndPractices first, because a database credential in history there is a possible PHI exposure. For any unattended loop, record which model answers each step and use the pause-when-flagged setting, so untrusted input cannot move work to another model without notice. Write the job down per issue: one issue, one repo, one list of allowed actions, with tests written first. Regulated repos stay human-gated. A 40 percent agent share on GitHub does not change that. Test the pre-commit check and the per-issue job file on MeowPassword, weathergalactic and sloth, and measure cost per merged pull request there.

## Sources

- <https://blog.gitguardian.com/claude-code-settings-local-json-secrets-docker-hub/>
- <https://www.advisori.de/en/blog/claude-code-leak-secrets-api-keys-github>
- <https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again>
- <https://fourweekmba.com/ai-most-of-2-539-leaked-secrets-sat-in-a-claude-code-file/>
- <https://www.anthropic.com/claude-fable-and-mythos-5-2>
- <https://www.notebookcheck.net/Claude-Fable-5-2-fallbacks-make-AI-agents-more-vulnerable.1446771.0.html>
- <https://globenewswire.com/news-release/2026/11/11/3400523/0/en/cequence-security-and-kpmg-collaborate-on-joint-report-examining-how-organizations-can-govern-and-secure-agentic-ai.html>
- <https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/>
- <https://xenospectrum.com/en/github-octoverse-2026-agent-surge-infrastructure-strain/>
- <https://bencoding.com/2026/11/09/the-software-factory-is-not-the-end-of-agents-it-is-what-comes-after-them/>
- <https://www.cio.com/article/4245820/claude-code-codex-and-cursor-have-become-part-of-your-software-supply-chain-without-approval.html>
- <https://www.securityweek.com/bay-raises-50-million-to-control-what-enterprise-ai-agents-can-do/>
- <https://adversa.ai/blog/top-ai-agent-security-resources-november-2026/>
- <https://adversa.ai/blog/top-ai-coding-agent-security-resources-november-2026/>
- <https://tech-insider.org/openai-2-coding-agents-disabled-safety-monitors-2026/>
- <https://aviatrix.ai/threat-research-center/ai-coding-agents-exposed-13000-internal-images-github-2026/>
- <https://newsletter.getdx.com/p/ai-generated-merged-code-holds-steady>
- <https://www.pulse.bot/ai/news/jellyfish-ai-development-study-the-real-sting-has-yet-to-land-bbcf4252-f990-4581-bfd9-eb4db4786657/>
- <https://sdtimes.com/agentic/allstacks-launches-agent-to-close-the-spec-gap-limiting-ai-assisted-development/>
- <https://www.pointguardai.com/ai-security-incidents/github-issues-turn-ai-coding-agents-against-ci-cd>
- <https://github.com/diclogic/ai-daily-digest/issues/205>

*Vendor and blog figures indicate direction, not audited benchmarks.*
