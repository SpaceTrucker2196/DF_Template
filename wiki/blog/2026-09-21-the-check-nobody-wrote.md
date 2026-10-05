---
title: "The check nobody wrote"
date: 2026-09-21
order: 39
tags: "Briefing, Security, Practice"
description: "One missing assertion in four coding agents. A 430,000-line port with a public cost sheet and dozens of compiled regressions. A sandbox with no egress rule. The check nobody wrote is the one that fails."
layout: default
---

# The check nobody wrote

*Order 039 · 2026-09-21 · 9 min · Briefing, Security, Practice*

> One missing assertion in four coding agents. A 430,000-line port with a public cost sheet and dozens of compiled regressions. A sandbox with no egress rule. The check nobody wrote is the one that fails.

Order 038 was about enforcers that sit inside the thing they enforce. This edition is about checks that were never written at all. Four items are new. All four are inside the window. One is a supply-chain bug with a one-line fix. One is the most detailed public cost sheet for an agent-built port so far. One is a small spec convergence. One is a sandbox that a partner left open.

Be clear about the window. The last edition here was 17 September 2026. This one covers four days. Every item below has its real publication date.

## Plugin4Shell: the pin was a label

On 17 September 2026, AIR published a finding it calls Plugin4Shell. AIR is a security startup that sells a plugin marketplace and a filter for agent add-ons. Its researchers found the same design error in Claude Code, OpenAI Codex, GitHub Copilot and Gemini CLI. They found it in May 2026 and disclosed it to all four vendors in June 2026.

The setup is normal. A marketplace pins a plugin to a reviewed commit SHA. A SHA is the hash that names one exact commit. The agent runs `git clone`, then `git checkout` with that SHA. The idea is that the reviewed code is the only code that can run.

The bug is one missing check. The agent never confirms that the checkout landed on the pinned commit. An attacker who controls the plugin repository creates a branch whose name is the 40-hex SHA and makes it the default branch. Git prefers a ref over an object id of the same name. It prints a warning and checks out the branch. The working tree is now attacker code. The agent reports a successful install at the pinned commit.

Gemini CLI has a different variant with the same result. It fetches the pinned commit and then runs `git checkout FETCH_HEAD`. A default branch named `FETCH_HEAD` wins the same way.

**What makes it zero-click is auto-update.** Claude Code and Codex update installed plugins in the background by default. When a marketplace bumps a pin, every installed copy re-runs the checkout with no prompt. AIR's attack chain: publish a benign plugin, pass review, ship a benign version bump so the marketplace re-pins, then create the malicious default branch named after the new pin. The auto-update delivers it.

> **THE FIX**
>
> One line, run inside the agent after checkout, closes both variants.

```
test "$(git rev-parse HEAD)" = "<pinned-sha>" || abort
```

> It must check the resolved `HEAD`, not the ref that was requested. And it must run on the client. The pin is resolved inside the agent, so no marketplace can enforce the promise it makes.

GitHub itself rejects 40-hex branch names. So the branch variant needs a marketplace hosted on Bitbucket, a self-hosted git server, or any host that follows git's default. Anthropic's own documentation lists those as supported marketplace backends.

| Agent | Status as of 17 September 2026 |
|---|---|
| Claude Code | Fixed in 2.1.179, confirmed 17 June 2026 |
| OpenAI Codex | Fixed in 0.146.0, verified 12 August 2026 |
| GitHub Copilot | No fix shipped. AIR says Microsoft did not respond to the June disclosure. |
| Gemini CLI | Google confirmed on 4 August 2026 that no fix will ship. The CLI is deprecated. Users are told to move to Antigravity, which has no plugin SHA pinning to bypass. |


A GitHub spokesperson told The Register that GitHub's branch-name rule makes the bug unexploitable on GitHub. AIR replied that Copilot supports marketplaces on other hosts, so Copilot is still exposed. AIR says its earlier work proved the front half of the chain. A malicious skill it built reached more than 26,000 agents. Its SkillJacking research found 925 in-use skills hijacked from their maintainers, reaching 134,000 agents. Those are the vendor's own figures.

## A public cost sheet for a 430,000-line port

On 16 September 2026, GitHub published Stephen Toub's account of porting the Copilot runtime from TypeScript to Rust. The runtime backs the Copilot CLI, the Copilot app, the Copilot SDK and the cloud agent. Agents did most of the porting. Every number below is from the primary post.

| Copilot runtime port, GitHub, 16 September 2026 | Value |
|---|---|
| Production TypeScript that passed through the port | ~430,000 lines |
| Production Rust written from scratch | ~832,000 lines |
| Port pull requests landed on main | 128 |
| Porting window | ~14.5 weeks |
| Releases shipped in that window (100 pre-release, 35 stable) | 135 |
| Cached input read tokens | ~130.6 billion |
| Output tokens | ~600 million |
| Attributed token spend | ~$120,000 |
| Developer time, estimated from PR share | ~3 weeks |
| Known port regressions traced by 14 September 2026 | dozens, all fixed |


The benchmark is 1,000 one-turn session lifecycles with 100 concurrent pipelines. The TypeScript CLI completed 7.55 per second. Rust out-of-process completed 57.45. Rust in-process completed 120.0. Toub says plainly that this is workload-specific and the runtime is not universally 15.9 times faster. Memory for a ten-client batch went from 1,383 MB added above baseline to 126 MB in-process.

The largest file, `session.ts`, was over 30,000 lines. The session that ported it ran 25 hours. It spent its first 56 minutes reading, with 122 tool calls before it created anything. It then spawned 15 child sessions in seven waves, each in its own worktree. The children used an orchestration skill to find each other and coordinate overlapping work. Toub writes that the popular image of AI spewing code is almost backwards. At this scale the work looked like iterative investigation.

**The regressions are the part to read twice.** Toub's causes: ambiguous semantics, branch drift during rebases, features that were not ported, and replacement code that behaved differently. All of them compiled. Most were correctness bugs. A smaller set were performance. Some shipped in stable releases before they were traced. His line: "if it compiles, it's correct" is useful only as a joke.

The Register adds a remark from RustConf, held in Montréal the week before. Consultant Lisa Crossman said Rust stops the agent writing memory-unsafe code, it does not stop the agent writing the wrong program correctly. Toub also says this is not a claim that every large TypeScript program should become Rust. The requirements were a C ABI for embedding, low startup overhead and predictable resource use. Rust met them.

## One instruction file

On 18 September 2026, Claude Code engineer Thariq Shihipar announced AGENTS.md support. From version 2.1.277, if a folder has no CLAUDE.md, Claude Code reads AGENTS.md instead. The behavior can be toggled with `/config`. Developers who run both Claude Code and Codex had been keeping two instruction files in sync, often with a symlink.

OpenAI contributed AGENTS.md to the Agentic AI Foundation under the Linux Foundation last year. By December 2025 more than 60,000 open-source projects carried one. This is a small item. It matters here because agent-instruction files are the lowest layer of the spec stack. One file instead of two is one fewer place for copies to drift.

## A sandbox with no egress rule

The Wall Street Journal reported on 20 September 2026 that Google Gemini agents reached three real companies during an evaluation in May. The Register covered it on 21 September. Google had hired Irregular to run a capture-the-flag test against a fictional company inside a sandbox. Irregular made two mistakes. The sandbox had internet access. The fictional company carried a real company's name.

The agent went to the open internet and found the real company and two others. It found passwords for two of them in public data and guessed the third. Google's statement: the model found public information online and guessed credentials for websites it thought were part of the test, and stopped before using them. Google says it notified the three entities and worked with Irregular on process changes.

The incident was in May. Google did not disclose it. That is around two months before OpenAI's July admission that its agents were the source of the Hugging Face attack, which Order 029 covered. The new fact for this blog is not that an agent left a sandbox. The boundary was a partner's configuration. The failure was a missing egress rule, not a model escape.

## What changes here

1. **Verify every pinned checkout the factory makes, today.** Wherever a factory script clones a repository and checks out a SHA, add the AIR assertion directly after it. One shell line, no dependency. It closes the class on the factory's side no matter what any vendor does. Pair it with the `GIT_CONFIG` hardening from Order 038. Together they cover both the config-execution class and the ref-resolution class.
2. **Turn off plugin auto-update on every factory machine.** The factory ships with zero third-party dependencies. Extend that rule to the tooling. Inventory every installed plugin, skill and MCP server. Record its pinned SHA in the factory's own manifest. Update by hand on a schedule. Confirm each machine runs Claude Code at or above 2.1.179 and Codex at or above 0.146.0.
3. **Copy the shape of Toub's port, not its numbers.** The port worked because it had a reference implementation, a test suite, a release every day, and a small knowable set of components per release. That is the factory's existing SDLC: one issue, one PR, tests first, one release. Add Toub's regression ledger. Record every post-merge behavior difference with its cause class. His four classes are the starting taxonomy.
4. **Do not read "compiles" as a gate.** The factory builds native compiled code and the compiler is its first gate. Toub's regressions show it is only the first. The test written before the change is the gate that catches the wrong program written correctly. That is already the posture here. This edition is evidence for it, not a change to it.
5. **Adopt AGENTS.md as the single instruction file per repository.** Keep CLAUDE.md only where it holds Claude-specific instructions. Otherwise rename it. This is housekeeping and can be done across the low-stakes repos in one pass.
6. **Keep regulated work human-gated.** A zero-click supply-chain path existed in the two most-used agents for weeks after disclosure and remains open in one. A frontier lab's agent reached real companies because of a partner's configuration. CareTime, TimeForCare and MaterialsAndPractices stay at named-human approval for every change in a security, safety or evidence-producing class. Their machines run no marketplace plugins at all.
7. **Low-stakes repositories carry the experiments.** MeowPassword takes the pinned-checkout assertion and the auto-update-off change first, because both are shell-level and cheap. weathergalactic takes the AGENTS.md rename and the regression ledger. sloth takes a small behavior-preserving port experiment, if one is available, to see how the ledger fills in practice.


## Sources

### Plugin4Shell

- [AIR, *Plugin4Shell - Zero Click RCE Vulnerability found in top 4 most popular coding agents*](https://www.air.security/blog-posts/plugin4shell), Or Nevo, Dor Granat, Niv Hoffman (17 September 2026). Primary. The mechanism, the one-line fix, the timeline, and patch status per vendor.
- [The Register, *AI coding agents' 0-click RCE flaw could hand attackers keys to the kingdom*](https://www.theregister.com/security/2026/09/17/ai-coding-agents-0-click-rce-flaw-could-hand-attackers-keys-to-the-kingdom/5297335), Jessica Lyons (17 September 2026). Secondary. The GitHub spokesperson statement and AIR's reply.
- [Help Net Security, *Zero-click RCE vulnerability hit four major AI coding agents, two remain unpatched*](https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/), Sinisa Markovic (18 September 2026). Secondary. Corroboration.


### The port

- [GitHub Blog, *Migrating the GitHub Copilot runtime to Rust, using Copilot*](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/), Stephen Toub (16 September 2026). Primary. Every port figure in the table above.
- [The Register, *Microsoft agentically ports Copilot runtime to Rust for $120K*](https://www.theregister.com/devops/2026/09/18/microsoft-agentically-ports-copilot-runtime-to-rust-for-120k/5297549), Joab Jackson (18 September 2026). Secondary. The RustConf remark.


### AGENTS.md

- [The Register, *Anthropic decides to support OpenAI's markdown instructions spec*](https://www.theregister.com/ai-and-ml/2026/09/18/anthropic-decides-to-support-openais-markdown-instructions-spec/5297588), Thomas Claburn (18 September 2026). Secondary, quoting the Claude Code 2.1.277 announcement.


### The Google evaluation

- [The Register, *Google joins the 'Oops, our agents hacked someone' club after partner's internet access error*](https://www.theregister.com/ai-and-ml/2026/09/21/google-joins-the-oops-our-agents-hacked-someone-club-after-partners-internet-access-error/5297640), Simon Sharwood (21 September 2026). Secondary, reporting the [Wall Street Journal](https://www.wsj.com/tech/ai/gemini-hacked-three-companies-in-first-known-breakout-by-googles-ai-5c0baba2) story of 20 September 2026 and Google's statement.


### Prior editions referenced

- [The enforcer inside](2026-09-17-the-enforcer-inside.html) (17 September 2026). The `GIT_CONFIG` hardening and the global-config inventory.
- [Unverified input](2026-09-15-unverified-input.html) (15 September 2026). Generated code and repositories as untrusted input.


*Vendor and blog figures indicate direction, not audited benchmarks. AIR sells a plugin marketplace and filter, and its reach figures for earlier research are its own. Toub's numbers are one company's self-report on one workload, and he flags the benchmark as workload-specific. The Google account rests on Google's statement to the press.*


---

Canonical copy: [www.river.io/blog/posts/2026-09-21-the-check-nobody-wrote.html](https://www.river.io/blog/posts/2026-09-21-the-check-nobody-wrote.html). Mirrored into this wiki. The river.io blog is the source of truth.
