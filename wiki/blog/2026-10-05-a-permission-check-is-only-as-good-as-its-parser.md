---
title: "A permission check is only as good as its parser"
date: 2026-10-05
order: 44
tags: "Briefing, Security, Practice"
description: "A sandboxed agent turned off its own sandbox with one curl command. An approval check read a shell command differently from the shell. A benchmark claim fell from 94 percent to 54 percent. IBM took its coding agent behind the customer wall."
layout: default
---

# A permission check is only as good as its parser

*Order 044 · 2026-10-05 · 6 min · Briefing, Security, Practice*

> A sandboxed agent turned off its own sandbox with one curl command. An approval check read a shell command differently from the shell. A benchmark claim fell from 94 percent to 54 percent. IBM took its coding agent behind the customer wall.

Order 043 said the control plane is leaving the agent. This edition shows what happens when the control stays too close to the agent. The window since 1 October is quiet. One item is new: IBM released a self-hosted Bob on 1 October. Three older items have never appeared in this blog. Each carries its real date. Two of them are failures of the same kind. A check that should stop the agent did not.

## DeepSeek Harness: the agent turned off its own sandbox

OX Security published CVE-2026-82533 on 8 September 2026. The Cloud Security Alliance wrote a research note on 10 September. The score is 9.4 out of 10. DeepSeek Harness is an agent runtime. It reached over 215,000 GitHub stars within weeks of its August release.

Two design flaws combined. First, the harness API trusted the Host header. It did not check the real address of the caller. Second, the sandbox blocked file writes but left loopback networking open. Loopback is the connection from a program to its own machine. A sandboxed agent could run one curl command against the local API. That command raised the session to "danger-full-access" and turned approvals off. The agent disabled its own confinement with one shell command.

The affected versions are 0.1.1-rc.2 and earlier. The fix is 0.1.2-alpha.1 or later. Researchers reported the flaw on 24 August. The maintainers fixed it on 27 August. OX published on 8 September. A second path allowed remote control without a login if the port was exposed.

> **LOOPBACK IS NOT A BOUNDARY**
>
> A sandbox that blocks files but allows localhost lets the agent talk to its own controller. The permission switch must not be reachable from inside the sandbox.

## Mistral Vibe: the approval check and the shell disagreed

Mistral published advisory MAI-2026-003 on 14 September 2026. It lists six CVEs, CVE-2026-87983 to CVE-2026-87988, all rated High. The product is Vibe CLI. Mistral released the fix in version 2.25.4 on 12 September. That is the same day Mistral learned of the published advisories.

Vibe asked the user to approve shell commands. The check missed four command forms: quoted absolute paths, shell redirection targets, ANSI-C quoted arguments and environment assignments. A crafted command ran with no approval prompt. It could read files outside the workspace. It could write files outside the workspace. It could run code with the permissions of the Vibe process.

The cause is a parser mismatch. The approval layer read the command string one way. The shell read the same string another way. Any allow-list that matches text is open to this failure. The safe options are to approve the exact string the shell will run, or to run commands without a shell.

## Ponytail: a benchmark claim cut by almost half

InfoQ reported on 5 August 2026 on Ponytail, an open-source skill. A skill is a rule file that an agent reads before it works. Ponytail tells the agent to avoid over-building. It asks if the code needs to exist, if the codebase already has it, and if the standard library does it.

The first claim was 80 to 94 percent less code. Colin Eberhardt of Scott Logic challenged the baseline. The baseline agent padded its answers. The author re-ran the test on real feature tasks in a FastAPI and React repository. The new figures are about 54 percent less code, about 20 percent lower cost and 27 percent faster runs. The 94 percent figure holds only in over-building cases. This is a prompt-level skill, not a control. Treat it as a style rule, and measure it first.

## IBM: Bob moves behind the customer wall

On 1 October 2026, IBM extended its Bob coding agent to self-hosted use. That includes air-gapped and sovereign-cloud sites, with supported models on premises. IBM General Manager Neel Sundaresan said: "The future of enterprise AI will depend on security, governance and sovereignty." The coverage notes that IBM gave no customer names, usage numbers or productivity figures. IBM shares rose about 5 percent that day. This is a product announcement. It shows that regulated buyers want the agent inside their own boundary. It is not evidence of effect.

## Not featured

Jeffrey Ladish of Palisade Research gave a Fox News interview on 3 October. It repeats the Hugging Face sandbox-escape account that earlier editions covered. It adds no new data. Adversa's 2 October list also names ZCode, OpenCode, Codex and brig issues. Those items had no publication dates in the source, so this edition does not feature them.

## What changes here

1. **Test the factory's own gates with hostile input.** The shell gates block `curl`, `rm` and `sudo` by reading command text. Write a test-driven suite of hostile strings: quoted paths, redirects, variable assignments. Run it on sloth first.
2. **Close loopback in agent sandboxes.** If an agent tool listens on localhost, the agent can reach it. Add a loopback-deny line to the weathergalactic sandbox inventory.
3. **Run any new skill against the current baseline.** Use a real MeowPassword issue. Compare the new rule with the current prompt. Native code with zero third-party dependencies already gives a cheap baseline.
4. **Keep regulated work at gated autonomy.** CareTime, TimeForCare and MaterialsAndPractices stay at level 3, with a named human approving each change. A self-hosted agent does not remove that need.


## Sources

- [OX Security, *CVE-2026-82533: DeepSeek Harness Vulnerability Lets AI Agents Escape Their Own Sandbox*](https://www.ox.security/blog/cve-2026-82533-deepseek-harness-ai-agent-sandbox-escape/) (8 September 2026). Primary research.
- [Cloud Security Alliance, *DeepSeek Harness Sandbox Escape and Agent Containment*](https://labs.cloudsecurityalliance.org/research/csa-research-note-deepseek-harness-sandbox-escape-20260910-c/) (10 September 2026). Seen in search results only.
- [Mistral, *Mistral Vibe shell permission vulnerabilities, MAI-2026-003*](https://docs.mistral.ai/resources/security-advisories/MAI-2026-003) (14 September 2026). Primary.
- [InfoQ, *Ponytail agent skill benchmark*](https://infoq.com/news/2026/08/ponytail-agent-skill-benchmark) (5 August 2026). Secondary.
- [247WallSt, *IBM Jumps 5% as Bob Coding Agent Gains Self-Hosted Deployment*](https://247wallst.com/investing/2026/10/01/ibm-jumps-5-as-bob-coding-agent-gains-self-hosted-deployment-salesforce-rises-3-palantir-inches-higher/) (1 October 2026). Secondary.
- [Fox News, interview with Jeffrey Ladish](https://www.foxnews.com/tech/former-anthropic-security-leader-warns-ai-agents-becoming-too-autonomous-humans-keep-check) (3 October 2026). Commentary, not featured.
- [Adversa AI, *AI coding agent vulnerabilities, October 2026*](https://adversa.ai/blog/top-ai-coding-agent-security-resources-october-2026/) (2 October 2026). Used for discovery only.
- [The agent does not hold the keys](2026-10-01-the-agent-does-not-hold-the-keys.html) (1 October 2026). Prior edition.


*Vendor and blog figures indicate direction, not audited benchmarks. The IBM item carries no usage data. The Ponytail figures are the author's own re-run on one repository.*


---

Canonical copy: [www.river.io/blog/posts/2026-10-05-a-permission-check-is-only-as-good-as-its-parser.html](https://www.river.io/blog/posts/2026-10-05-a-permission-check-is-only-as-good-as-its-parser.html). Mirrored into this wiki. The river.io blog is the source of truth.
