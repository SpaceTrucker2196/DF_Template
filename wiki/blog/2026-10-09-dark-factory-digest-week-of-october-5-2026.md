---
title: "Dark Factory Digest, week of October 5, 2026"
date: 2026-10-09
order: 46
tags: "Digest, Briefing"
description: "The control must sit outside the agent: a gate that the agent can reach, that misreads text, or that fails open is not a gate."
layout: default
---

# Dark Factory Digest, week of October 5, 2026

*Order 046 · 2026-10-09 · 4 min · Digest, Briefing*

> The control must sit outside the agent: a gate that the agent can reach, that misreads text, or that fails open is not a gate.

This digest covers 3 October to 9 October 2026. It rolls up three research briefs (5, 7 and 9 October). It was a quiet week with no new regulator action, framework release or large metric. The main theme: the control must sit outside the agent. A gate that the agent can reach, that reads text differently from the shell, or that fails open is not a gate.

## This week's signals

1. **Sandbox escape by one command (CVE-2026-82533, published 8 September).** A sandboxed DeepSeek Harness agent could raise its own session to "danger-full-access" with one curl command to a local API. CVSS 9.4. The sandbox blocked file writes but left loopback networking open. Fixed in 0.1.2-alpha.1.
2. **Parser mismatch (Mistral advisory MAI-2026-003, 14 September).** Six High CVEs in Vibe CLI. The approval check and the shell read the same command in different ways, so a crafted command ran without a prompt. Fixed in 2.25.4.
3. **Hooks that fail open (Microsoft Copilot Studio, 6 October).** Hooks run a workflow every time an event fires. Microsoft's own caveat: if the workflow fails, times out or returns unreadable content, the agent continues. Preview only. Secondary source.
4. **Vendors give no guarantee (New York City Council hearing, 5 October).** OpenAI, Anthropic, Meta and Google did not promise that agents always follow safeguards. Anthropic's Logan Graham: "the science of doing this is fundamentally hard and unsettled." Single secondary source.
5. **Secrets as placeholders (OpenAI Codex reusable cloud environments, reported 29 September).** The program sees a placeholder. A proxy inserts the real value only for allow-listed domains. Secondary source, no incident data.
6. **Adoption and benchmark context.** A JetBrains survey (reported 6 October) says 90 percent of developers use AI coding agents weekly at work. Sample size is not stated. The Ponytail skill cut its claim from 80 to 94 percent less code to about 54 percent after a public challenge (InfoQ, 5 August). IBM made its Bob agent available for self-hosted and air-gapped use on 1 October, with no usage data.

## What it means for the River.io Software Factory

Test the factory's own gates. Use TDD suites on the low-stakes repos: hostile command strings (quoted paths, redirects, variable assignments) on MeowPassword, loopback deny and gate decision logs on weathergalactic, and fail-open tests (gate crash, timeout, garbage output) on sloth. Each failure must stop the run. Keep the real token in a small native proxy or the keychain and give the agent only a placeholder. Start with an empty network allow-list: the factory has zero third-party dependencies, so it needs no package registry. CareTime, TimeForCare and MaterialsAndPractices stay at human-gated autonomy. No vendor will carry that accountability.

## Sources

- <https://www.ox.security/blog/cve-2026-82533-deepseek-harness-ai-agent-sandbox-escape/>
- <https://labs.cloudsecurityalliance.org/research/csa-research-note-deepseek-harness-sandbox-escape-20260910-c/>
- <https://docs.mistral.ai/resources/security-advisories/MAI-2026-003>
- <https://cloudwars.com/ai/need-ai-agents-to-run-workflows-with-no-exceptions-microsoft-has-a-hook-for-that>
- <https://foxnews.com/live-news/ai-super-intelligence-safety-10-06>
- <https://siliconangle.com/2026/09/29/openais-codex-gets-reusable-cloud-environments-that-follow-developers-across-devices/>
- <https://gulfnews.com/technology/90-of-developers-surveyed-now-use-ai-coding-agents-at-work-jetbrains-says-1.500700542>
- <https://infoq.com/news/2026/08/ponytail-agent-skill-benchmark>
- <https://247wallst.com/investing/2026/10/01/ibm-jumps-5-as-bob-coding-agent-gains-self-hosted-deployment-salesforce-rises-3-palantir-inches-higher/>

*Vendor and blog figures indicate direction, not audited benchmarks.*
