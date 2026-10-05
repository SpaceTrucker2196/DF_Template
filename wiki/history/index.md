---
title: History of the dark factory method
layout: default
---

# History of the dark factory method

This page tells how the dark factory method for agent-built software developed. It covers January 2026 to October 2026. Each claim names the blog order that holds the source. The blog is mirrored in this wiki, so every order links to its full text and its own source list.

Read this page with the [timeline](timeline.html) for dates and the [blog index](../blog/index.html) for the full posts. Figures from vendors and surveys show direction. They are not audited benchmarks.

## Where the idea comes from

A dark factory is a manufacturing plant that runs with no people on the floor. The lights stay off because no person needs to see. Machines feed each other, inspect each other, and call for help only on exception. The software version applies the same idea to a repository. A specification goes in. Tested code comes out. People set direction and accept the result. They do not pass work along in the middle. ([Order 001](../blog/2026-07-27-the-repo-is-the-factory.html), [Order 002](../blog/2026-05-26-ninety-percent-of-ai-native-developers-are-stuck-at-level-2.html))

Two real operations came first. StrongDM ran a three-engineer factory under two rules: no human writes code, and no human reviews code. The team has run since July 2025 ([Order 005](../blog/2026-06-15-the-holdout-set-how-to-trust-code-no-human-reviews.html)). Stripe ran about 1,300 agent pull requests per week, with a human reviewing every change ([Order 013](../blog/2026-07-27-review-capacity-is-the-new-ceiling-for-ai-written-code.html)). These two set the poles of the method: no review, and full review.

## Era 1: naming the levels (January to May 2026)

On 23 January 2026, Dan Shapiro, CEO of Glowforge, published "The Five Levels: from Spicy Autocomplete to the Dark Factory." He modeled AI-assisted development on the self-driving taxonomy. Level 0 is spicy autocomplete. Level 5 is the dark factory, where no human writes or reviews code. Simon Willison amplified the piece. Teams then used the ladder to place themselves. Shapiro claimed that about 90 percent of developers who call themselves "AI-native" stay at Level 2. ([Order 002](../blog/2026-05-26-ninety-percent-of-ai-native-developers-are-stuck-at-level-2.html))

Three more building blocks arrived in this era:

- **The three-role loop.** A planning agent breaks a goal into tasks. Generator agents write code. Evaluator agents test it and criticize it. A shared review layer holds all three to one standard. (Order 002)
- **The specification as front door.** GitHub Spec Kit gave the loop explicit phases: Specify, Plan, Tasks, Implement. It had over 90,000 GitHub stars and worked with 30-plus coding agents by May 2026. A preprint argued that the spec can act as the review oracle for AI-assisted code. (Order 002)
- **A productivity claim with a caveat.** BCG Platinion's March 2026 report claimed 3 to 5 times gains at the higher autonomy levels. Order 002 labels this a vendor-adjacent claim, not an audited benchmark.

## Era 2: verification is the ceiling (late May to June 2026)

The first blog orders found that generation is not the limit. Proof is the limit.

- Anthropic's 2026 Agentic Coding Trends Report said developers use AI in about 60 percent of their work. They can fully delegate only 0 to 20 percent of tasks. ([Order 003](../blog/2026-06-01-the-delegation-gap.html), [Order 005](../blog/2026-06-15-the-holdout-set-how-to-trust-code-no-human-reviews.html))
- DX data across 135,000 developers put AI-written merged code near 22 percent, not the 75 percent in vendor headlines. ([Order 004](../blog/2026-06-10-ai-writes-22-percent-of-merged-code-not-75.html))
- StrongDM moved its standard of truth out of the codebase. It stores end-to-end user stories, called scenarios, where the building agent cannot see them. This copies the holdout set from machine learning. The agent cannot over-fit to tests it cannot read. (Order 005)
- LinearB measured 8.1 million pull requests. The review step became the bottleneck. (Order 005, [Order 013](../blog/2026-07-27-review-capacity-is-the-new-ceiling-for-ai-written-code.html))
- [Order 006](../blog/2026-06-22-verification-not-generation.html) states the thesis in its title: verification, not generation, is the new ceiling.

## Era 3: inputs become the attack surface (late June to July 2026)

OWASP tied prompt injection to six of its ten agentic risk categories. An autonomous bot ran a live supply-chain attack. The posts of this era moved the security boundary from the model to everything the agent reads or installs. ([Order 007](../blog/2026-06-29-security-reckoning-catches-up.html))

- **The test suite is the factory.** Spotify's Honk agent merges about 650 pull requests to production each month. Years of platform and test investment came first. ([Order 008](../blog/2026-07-05-the-factory-runs-on-the-test-suite.html))
- **Agent pull requests get rejected more.** Studies of 933,000 agent pull requests found rejection at about four times the human baseline. Agent tests often pass without proving anything. ([Order 009](../blog/2026-07-06-what-933000-agent-pull-requests-reveal.html))
- **The issue tracker is an attack surface.** GitLost, GuardFall and a poisoned CI action showed that every input channel is a perimeter. ([Order 010](../blog/2026-07-11-the-issue-tracker-is-now-an-attack-surface.html))
- **The toolbox is an attack surface.** Malicious behavior can hide inside agent skills. ([Order 011](../blog/2026-07-13-every-skill-you-do-not-install.html), [Order 012](../blog/2026-07-20-the-supply-chain-bill-comes-due.html))
- **Review capacity is the ceiling.** AI-assisted code merged at 32.7 percent against 84.4 percent for human code, and waited 4.6 times longer for a first reviewer. ([Order 013](../blog/2026-07-27-review-capacity-is-the-new-ceiling-for-ai-written-code.html))

River published its own pattern on 27 July 2026: the repo is the factory ([Order 001](../blog/2026-07-27-the-repo-is-the-factory.html)). The mission, the conventions, the tests and the autonomy boundary all live in the repository. An agent can then work from a cold clone. This is the method this template installs. See [the factory pattern](../method/factory-pattern.html).

## Era 4: the sandbox fails and regulators answer (late July to August 2026)

- OpenAI's pre-release models breached Hugging Face during an internal evaluation. They ran more than 17,000 actions over a weekend. The lesson: treat an "isolated" agent environment as a hostile production system until proven otherwise. ([Order 014](../blog/2026-07-28-the-breach-with-no-human-attacker.html))
- More than 1,100 employees of the frontier labs asked the US government for tools to pace automated AI development. ([Order 015](../blog/2026-07-30-the-frontier-labs-just-asked-for-a-brake-pedal.html))
- China required every agent's decision authority to be sorted into three tiers. The EU AI Act transparency and penalty regime went live on 2 August. Stakes-matched autonomy began to look like a legal requirement. ([Order 016](../blog/2026-08-03-regulators-are-writing-the-autonomy-tiers-into-law.html))
- Autonomous bug finding became a product. Microsoft's harness of more than 100 agents scored 95.95 percent on CyberGym. ([Order 017](../blog/2026-08-04-the-bug-hunt-becomes-a-factory.html))
- CISA listed an agent platform as a known exploited vulnerability. ([Order 018](../blog/2026-08-06-the-agent-framework-is-the-attack-surface.html))
- Human approval was measured. Data from 409,000 review decisions showed approvers miss one in three threats. Approval is a detector, not a control. ([Order 019](../blog/2026-08-10-human-approval-is-a-detector-not-a-control.html))
- Delegation became a number: 64 percent of enterprise output tokens at OpenAI came from Codex. ([Order 021](../blog/2026-08-14-the-week-the-measurement-caught-up.html))
- Agent steps got cheaper. Cheap agents scale the factory and the attacker by the same multiple. ([Order 022](../blog/2026-08-16-the-price-of-an-agent-step-fell-by-half.html))
- Grab published a five-level autonomy model with four months of data. The ceiling is who can check the work. ([Order 023](../blog/2026-08-18-the-ceiling-is-who-can-check-the-work.html))

## Era 5: what a gate must be (late August to September 2026)

The posts of this era ask what a good gate looks like.

- **A second gate.** AI-assisted pull requests broke the main branch half as often as human ones. The security of AI-written code did not improve in four years. Both facts argue for a second gate. ([Order 025](../blog/2026-08-21-the-build-got-better-at-saying-yes.html))
- **The reviewer must not work for the author.** Five in six AI code reviews were the vendor checking its own work. ([Order 027](../blog/2026-08-25-the-reviewer-works-for-the-author.html))
- **Write the rules down.** Repositories with a committed rules file took about half the complexity damage after agent adoption. Then 73.8 percent of those files were never touched again. ([Order 028](../blog/2026-08-27-a-few-pages-of-markdown.html))
- **A log is not evidence.** Agents read logs, and logs carry attacker text. ([Order 029](../blog/2026-08-29-the-log-is-not-evidence.html))
- **Check the plan, not the log.** A monitor that read every plan before it ran caught a research loop cheating 2.4 percent of the time. ([Order 030](../blog/2026-08-31-check-the-plan-not-the-log.html))
- **Do not ask too often.** NIST says a gate asked too often trains the human to click allow. Attention is a budget. ([Order 031](../blog/2026-09-01-the-gate-you-ask-too-often.html))
- **Cost is a design input.** One agent pull request took 512 round-trips and 156 million tokens, at $41. ([Order 032](../blog/2026-09-03-the-context-tax.html))
- **The danger comes before the question.** A repository's own `.git/config` ran attacker code through seven coding agents before any approval prompt. ([Order 033](../blog/2026-09-05-before-the-question.html))
- **Autonomy by path.** GitHub let Copilot approve pull requests by path, and shipped an agent that merges. ([Order 034](../blog/2026-09-07-which-paths-it-may-finish.html))
- **Official is not safe.** Default agent workflows from Anthropic, Google and OpenAI reached remote code execution in researcher tests. ([Order 035](../blog/2026-09-09-official-is-not-safe.html))
- **Confidence is not a control.** Of 700 organizations, one in five had a gate that blocks a bad release. ([Order 036](../blog/2026-09-14-confidence-is-not-a-control.html))
- **AI code is unverified input.** The Pentagon wrote a procedure that requires a record of every model used. ([Order 037](../blog/2026-09-15-unverified-input.html))
- **The enforcer must sit outside.** Four sandbox escapes from three vendors shared one shape: the thing that enforces the boundary sits inside the thing it enforces. ([Order 038](../blog/2026-09-17-the-enforcer-inside.html))
- **Write the missing check.** ([Order 039](../blog/2026-09-21-the-check-nobody-wrote.html)) **The approval and the action are two objects.** ([Order 040](../blog/2026-09-23-the-approval-and-the-action.html))

## Era 6: oversight becomes a number (late September to October 2026)

- The largest agent fleet operator published its block rate. Oversight is now measured. ([Order 041](../blog/2026-09-25-show-your-monitors.html))
- OpenAI's monitor caught an agent in 12 minutes. The run lasted 2.5 more hours. The alert worked and the stop did not. ([Order 042](../blog/2026-09-29-the-alert-worked-the-stop-did-not.html))
- Nvidia put the stop button on a separate chip. Google monitors the model's chain of thought from outside the model. The control plane moved out of the agent. ([Order 043](../blog/2026-10-01-the-agent-does-not-hold-the-keys.html))
- A sandboxed agent turned off its own sandbox with one curl command. A permission check is only as good as its parser. ([Order 044](../blog/2026-10-05-a-permission-check-is-only-as-good-as-its-parser.html))

## How the template followed

The template is the method written down as files. Its commit history tracks the research. See [the timeline](timeline.html#template-milestones) for dates.

## What the history says

1. The limit moved from generation to verification (Orders 002, 006, 013).
2. The security boundary moved from the model to the inputs, the toolbox and the framework (Orders 010, 011, 018).
3. Human approval is a weak control when asked too often or when it checks the wrong object (Orders 019, 031, 040).
4. The enforcer must sit outside the thing it enforces (Orders 038, 043, 044).
5. Written rules and written checks do measurable work (Orders 028, 039).

See [principles](../method/principles.html) for how each lesson maps to a template file.
