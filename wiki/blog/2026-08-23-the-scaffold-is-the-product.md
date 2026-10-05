---
title: "The scaffold is the product"
date: 2026-08-23
order: 26
tags: "Briefing, Loop Design, Security"
description: "OpenAI open-sourced the engine under Codex, and the numbers say the scaffold beat the model. In the same week an AI security scan passed a live injection flaw that an AI attacker found in five days."
layout: default
---

# The scaffold is the product

*Order 026 · 2026-08-23 · 9 min · Briefing, Loop Design, Security*

> OpenAI open-sourced the engine under Codex, and the numbers say the scaffold beat the model. In the same week an AI security scan passed a live injection flaw that an AI attacker found in five days.

{% raw %}
The last two editions reported quiet windows. This one does not. Four items landed, and this blog has covered none of them. One falls inside the two-day window. The other three are older, and each date is stated.

The four items split cleanly. Two say the scaffold around the model is now the lever. Two say nobody has a working review layer for what that scaffold produces.

## OpenAI open-sourced the engine under Codex

On **20 August 2026** OpenAI released **Harness** under the **Apache-2.0** licence. Harness is the execution engine behind Codex, OpenAI's coding agent. A harness is the scaffold that surrounds a model: it holds memory, calls tools, streams events, and routes approval requests to a human.

The release includes three parts: `codex exec`, a command-line tool; the Codex SDK; and `app-server`, the engine that runs the loop. Apache-2.0 means anyone can read it, change it, and ship it.

One number is the reason to care.

| GPT-5.6 Sol on ARC-AGI-3, harness optimisation only | Value |
|---|---|
| Score before | 13.3% |
| Score after | 38.3% |
| Output token volume after | 1/6 |


**The model did not change.** OpenAI reports that tuning the harness alone produced this. The named techniques are retained reasoning and context compression. Both are choices about how the loop assembles and carries context between steps.

This is a vendor figure on a benchmark the vendor picked. Treat the size of the gain as direction. The structural claim survives that caution. A fixed model with a better scaffold scored higher and cost less.


The loop is your code. The model is a supplier.

There is a second reason to read the release. `app-server` is the part that routes human-in-the-loop approval requests. This factory's autonomy ladder is a design written from first principles. A production implementation of the same idea is now readable source. That is a study task, not an adoption task. The zero-dependency rule stands: read the design, do not link the code.

## An AI attacker beat an AI reviewer in five days

Wiz Research published the write-up on **17 August 2026**. The events ran from **18 June to 23 June 2026**.

A merged pull request in Snowflake's public `snowflake-connector-net` repository changed one workflow file. The change removed a safe pattern and replaced it with an unsafe one.

```
- env:
-   ISSUE_TITLE: ${{ github.event.issue.title }}
- run: jq -n --arg title "$ISSUE_TITLE" ...

+ run: TITLE=$(echo '${{ github.event.issue.title }}' | sed ...)
```


The first form puts the issue title in an environment variable, then passes it to a program as data. The second form pastes the title straight into a shell command. The `sed` escaping runs too late to help. GitHub expands the template first. A single quote in the title then closes the string and the rest runs as commands.

The workflow fired on `issues: opened`. Any GitHub user could trigger it by opening an issue.

**GitHub Advanced Security scanned that exact file and did not flag the injection.**

Five days after the flaw went live, Wiz's **Red Agent** found it. Red Agent is an autonomous security research tool. It scanned Snowflake's GitHub organisation, flagged the workflow, and wrote an exploit. Its first payload broke the shell syntax and returned an error. The agent read the error, rewrote the payload, and succeeded on the second attempt. No human helped.

The exploit sent a Jira token to an external listener. The token read Snowflake's internal engineering, security compliance, and bug bounty projects. Wiz reported it through HackerOne on 23 June. **Snowflake patched it the same day**, rotated the token, and confirmed from audit logs that Wiz was the only actor in the window.

> **WHAT WIZ CORRECTED**
>
> Wiz updated the post on 17 August. GitHub Copilot was a co-author that reviewed the merged pull request and marked it clear. Copilot Autofix's documented contribution in that pull request was a separate fix to a different file. **Wiz states plainly that it is unclear whether the vulnerable change itself was AI-assisted.** The finding that survives is the one about review: an automated security review read the flaw and passed it.

## The guard that could never fail

The workflow carried a condition that looked protective.

```
if: (github.event_name == 'issues' &&
     github.event.pull_request.user.login != 'whitesource-for-github-com[bot]')
```


On an `issues` event, `github.event.pull_request` is always null. So the second half reduces to `null != 'whitesource-for-github-com[bot]'`, which is always true. Every user passed.

This is the cheapest lesson in the edition. **A guard with no failing test is decoration.** Nobody had ever watched that condition block anything, so nobody knew it could not.

## Agent code degrades the next agent

A preprint posted on **19 June 2026** put a number on something this blog has only argued. The paper is *Is Agent Code Less Maintainable Than Human Code?*

The authors built **CodeThread**, a framework that constructs two-step pull request chains from existing coding benchmarks. Step one produces code. Step two asks an agent to build on it. The authorship of step one is the variable.

| CodeThread: 4 frontier agents, 4 benchmarks | Result |
|---|---|
| Task resolve rate drop, agent code versus human code | up to 13.1% |


Agents resolve tasks less often when they build on agent code. The authors then looked for the cause and did not find it where they expected. **Traditional maintainability metrics do not explain the gap.** Structural complexity and verbosity are not the signal.

The signal is behavioural. The clearest differences are in **input validation and error handling**.

That is the same class of defect as the Snowflake regression. A pattern that validated input got replaced by one that did not. Nothing looked more complex. Nothing looked longer. The handling of untrusted input got quietly worse.

The paper is a preprint and has not been peer reviewed. The finding still changes how a loop should run. An unattended loop is, by construction, an agent building on agent code over and over. The cost compounds.

## The bottleneck moved, and a survey named it

GitKraken announced its *2026 State of AI in Engineering* report on **14 August 2026**. It surveys **554 developers and engineering leaders**.

| Measure | Value |
|---|---|
| Organisations using AI coding tools | 96.4% |
| Agent delegation as primary way of working, September 2025 | 7.6% |
| Agent delegation as primary way of working, June 2026 | 28% |
| Developers reporting higher productivity | 84% |


Rows two and three are the finding. **Agent delegation nearly quadrupled in nine months.** Row four is perception, not measurement, which is the report's own stated point.

GitKraken's conclusion matches the one this blog reached on 27 July. Code generation accelerated. Shipping did not. The constraint is understanding, reviewing and merging.

## What changes here

1. **Read the Harness approval-gate code.** `app-server` is Apache-2.0 and routes human-in-the-loop approvals. It is the highest-value reading of the month. Read the design. Do not link the code.
2. **Copy context compression into the converge loop.** The loop is native compiled code with no third-party dependencies, so its context assembly is our own code. Retained reasoning and context compression cost nothing in dependencies and attack the token bill directly.
3. **Test for the pattern, not just the behaviour.** The Snowflake bug removed a safe pattern and behaved the same. A behaviour test passes that swap. For any workflow that reads untrusted input, add a test that fails when untrusted input reaches a shell command directly.
4. **Prove every guard can fail.** Write the negative test for each gate in the autonomy ladder. A gate nobody has watched block something is not a gate.
5. **Cap how long a loop builds on its own output.** After a set number of agent-authored pull requests in one area, require a human read before the loop continues. Read the input validation and the error handling first. That is where the paper says the damage lives.
6. **Spend the next increment on cheaper review.** Three sources now name review as the constraint. Smaller diffs, pattern-level tests, better failure messages. Not higher throughput.
7. **Regulated repos do not move.** CareTime, TimeForCare and MaterialsAndPractices stay human-gated. The argument is one line: an automated security scan read the vulnerable file and passed it.


The Snowflake pattern is also a detector, and a cheap one. Untrusted input interpolated into a `run:` block, plus a condition that references a field absent on the triggering event. Both are checkable without running anything. That is worth one issue, with the Wiz write-up cited in it, per the house rule that every detector links its source.

## Sources

### Codex Harness

- [Open Source For You, *OpenAI Open Sources Codex Harness Framework*](https://www.opensourceforu.com/2026/08/openai-open-sources-codex-harness/) (published 21 August 2026, describing the 20 August release). Source of the Apache-2.0 licence, the three components, the ARC-AGI-3 move from 13.3% to 38.3%, and the sixfold token reduction.
- [BigGo Finance, *OpenAI open-sources Codex core framework*](https://finance.biggo.com/news/7ca9b7b6-430a-4561-975c-ef920e39f73a). Background on the components.
- [SitePoint, *Codex CLI: OpenAI's Open Agent Harness*](https://www.sitepoint.com/codex-cli-openai-agent-harness-installation-commands/). Background on the command-line tool.


### The Snowflake incident

- [Wiz, *Wiz Red Agent Finds Its Way Into Snowflake's Internal Jira Through a Flaw in a GitHub Copilot-Assisted PR*](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) (17 August 2026). Primary source. The timeline, the code change, the always-true condition, the scan that passed, and the exfiltrated token. Also the 17 August correction about Copilot's role.
- [Forbes, *Wiz's AI Agent Finds A Vulnerability In Snowflake's Internal Systems*](https://www.forbes.com/sites/timkeary/2026/08/17/github-copilot-missed-a-vulnerability-that-wizs-ai-agent-found/) (17 August 2026).
- [SC Media, *Wiz agent finds Snowflake repo flaw*](https://www.scworld.com/news/wiz-agent-finds-snowflake-repo-flaw-in-code-co-authored-by-github-copilot-autofix).
- [The Hacker News, *Snowflake GitHub Actions Flaw Lets Crafted Issues Trigger Command Injection*](https://thehackernews.com/2026/08/snowflake-github-actions-flaw-lets_0330881554.html).


### Agent code maintainability

- [arXiv:2606.21804, *Is Agent Code Less Maintainable Than Human Code?*](https://arxiv.org/html/2606.21804v1) (19 June 2026). Primary source. The CodeThread framework, four frontier agents, four benchmarks, and the resolve-rate drop of up to 13.1%. Preprint, not peer reviewed.
- [arXiv:2605.06464, *To What Extent Does Agent-generated Code Require Maintenance?*](https://arxiv.org/abs/2605.06464) (May 2026). Related. Human developers perform about 83% of the maintenance on AI-generated files.


### Adoption and the bottleneck

- [GitKraken, *State of AI in Engineering 2026: The Proof Gap*](https://gitkraken.com/blog/everyone-feels-faster-almost-nobody-can-prove-it). Source of the 96.4% adoption figure, the 7.6% to 28% delegation shift, and the productivity self-reports.
- [PR Newswire, *GitKraken Introduces GitLens 19*](https://www.prnewswire.com/news-releases/gitkraken-introduces-gitlens-19-bringing-human-and-ai-workflows-together-in-one-workbench-302851472.html) (14 August 2026). Source of the survey size of 554 and the announcement date.


### Prior editions referenced

- [The build got better at saying yes](2026-08-21-the-build-got-better-at-saying-yes.html) (21 August 2026). Why a green build is weak evidence, and why agent diffs run larger.
- [Review capacity is the new ceiling for AI-written code](2026-07-27-review-capacity-is-the-new-ceiling-for-ai-written-code.html) (27 July 2026). Why diff size, not model quality, sets the throughput limit.


*Vendor and analyst figures indicate direction, not audited benchmarks. The ARC-AGI-3 and token figures are OpenAI's own, on a benchmark OpenAI selected. The GitKraken numbers come from 554 respondents who self-selected into a vendor survey, and the productivity figures are perception rather than measurement. The arXiv paper is a preprint. The Wiz write-up is the primary account of an incident Wiz itself conducted, and Wiz amended it on 17 August to soften the claim about Copilot's role. Of the four items, only the Codex Harness release falls inside the two-day window.*

{% endraw %}


---

Canonical copy: [www.river.io/blog/posts/2026-08-23-the-scaffold-is-the-product.html](https://www.river.io/blog/posts/2026-08-23-the-scaffold-is-the-product.html). Mirrored into this wiki. The river.io blog is the source of truth.
