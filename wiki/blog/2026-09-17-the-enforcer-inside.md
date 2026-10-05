---
title: "The enforcer inside"
date: 2026-09-17
order: 38
tags: "Briefing, Security, Practice"
description: "Four sandbox escapes from three vendors share one shape: the thing that enforces the boundary sits inside the thing it enforces. A survey puts a number on the human re-check."
layout: default
---

# The enforcer inside

*Order 038 · 2026-09-17 · 8 min · Briefing, Security, Practice*

> Four sandbox escapes from three vendors share one shape: the thing that enforces the boundary sits inside the thing it enforces. A survey puts a number on the human re-check.

Order 037 was about a buyer that wrote the gate down. This edition is about what happens on the other side of the gate, inside the sandbox that is supposed to hold the agent. Two items are inside the window. One is a pair of escapes. The other is a survey that counts the human re-check as a cost.

Be clear about the window. The last edition here was 15 September 2026. This one covers two days. Two items are inside the window. Three others are new to this blog and older than it. Each is reported with its real date.

## Two ways out of Codex

On 15 September 2026, Accomplish published two escapes from the OpenAI Codex sandbox. Accomplish is a security startup that sells an agent runtime in a virtual machine. It reported both bugs to OpenAI on 12 August 2026. OpenAI fixed both within eight days.

The first is called Overpatch. It is in the open-source Codex CLI. In `workspace-write` mode, the agent may write only inside the workspace folder. The `apply_patch` tool edits files for the agent. It grants write access to the parent folder of each path named in the patch. Name `/tmp` and it grants write access to `/`.

The patch that lands the write has two entries. One appends a line to `.zshrc` through a symlink into the home folder. The other names `/tmp` and does nothing. That entry fails on purpose. It is in the patch only to widen the grant. Remove it and the write is refused. There is no approval prompt. Fixed in Codex CLI 0.149.0.

The second is called Heapjack. It is in a JavaScript tool named `node_repl`. Codex Desktop writes that tool into the global config at install, with no opt-in and no setting to turn it off. A native parent program, outside the sandbox, starts one Node process. Inside that process there are two contexts. The trusted one holds OpenAI's code and gets a secret token. The untrusted one runs the agent's code.

Both contexts share one heap and one output pipe. Untrusted code takes a heap snapshot and tries every string shaped like a UUID. A wrong token gets "not authorized". A right token with a bad argument gets a real validation error. The untrusted code then writes its own request onto the shared pipe. The parent checks the token and does the work.

**All of it ran at `read-only`, the strictest mode Codex has.** The proof of concept launched an application outside the Codex process tree with no prompt and nothing on screen. Fixed in Codex Desktop build 26.818.21641.

> **THE SHAPE**
>
> Accomplish's summary of both bugs is the useful sentence. The thing doing the enforcement was sitting inside the thing being enforced. `apply_patch` worked out its own permissions from input it was handed. `node_repl` kept the secret that separates trusted from untrusted in the same memory as the untrusted code.

## The same class in Claude Code and the Cursor CLI

The same firm published two earlier posts that are new to this blog. Beltdown, about Claude Code, is from 11 September 2026. Beltdown2, about the Cursor CLI, is from 12 September 2026. Both are the `core.fsmonitor` class that Order 013 covered in July, from Pillar Security. Both are new instances with new timelines.

The shape is the same in each. A per-tool sandbox wraps the shell tool. The harness runs its own `git` outside the sandbox to index the repository. Git reads `core.fsmonitor` from `.git/config` and runs its value as a shell command. So a repository can tell the harness's git to run a command on the developer's machine.

In Claude Code, most of the harness's git calls were already hardened. Accomplish found one that was not: `git ls-files`, the index refresh. The `.git` folder at the project root was protected. A nested `.git` in a subfolder was not. The harness ran git in whatever folder the shell tool used last. And reading a file in a folder auto-loads skills from that folder, which triggers the index refresh. Chained, one message escaped the sandbox with no prompt.

| Beltdown disclosure timeline, Claude Code | Date |
|---|---|
| Reported to Anthropic, triaged the same day | 13 July 2026 |
| First hardening in 2.1.223, missed some git calls | 6 August 2026 |
| Full fix in 2.1.247 | 26 August 2026 |


Upstarts Media, reporting on 10 September 2026, describes that as about 50 days and about 30 releases. In the Cursor CLI there was no hardening on any git path. A read-only prompt, with the model told to run no shell commands, fired Cursor's own `git ls-files` and ran the payload as the logged-in user.

**Cursor's fix is the one to copy.** The fragile approach adds `-c core.fsmonitor=false` to each git call. Each new call is another place to forget the flag. Cursor CLI `2026.08.04-aaa8809` instead sets four environment variables on every git spawn.

```
GIT_CONFIG_COUNT=4
GIT_CONFIG_KEY_0=safe.bareRepository   GIT_CONFIG_VALUE_0=explicit
GIT_CONFIG_KEY_1=core.fsmonitor        GIT_CONFIG_VALUE_1=false
GIT_CONFIG_KEY_2=core.hooksPath        GIT_CONFIG_VALUE_2=/dev/null
GIT_CONFIG_KEY_3=core.attributesFile   GIT_CONFIG_VALUE_3=/dev/null
```


Environment config outranks the repository's `.git/config`. No individual call site can forget it. Accomplish names the vulnerable combination as three things: a per-tool sandbox rather than a process-level one, a harness that runs its own git outside it, and repository-controlled executable git config that is not universally neutralized. Two designs close the class. Harden every git spawn, as Codex, Kilo Code and now Cursor do. Or sandbox the whole agent process so every child inherits confinement, as Antigravity and Grok Build do.

## A number for the human re-check

On 16 September 2026, Collibra released a Harris Poll survey it calls *The 2026 Hallucination Tax Report*. Collibra sells governance tooling, and the framing is vendor framing. The method is stated. Online, 5 to 11 August 2026, 306 U.S. decision-makers at director level or above in data management, privacy or AI, weighted by company size, plus or minus 6.4 points at 95% confidence.

| Collibra and The Harris Poll, n=306, August 2026 | Share |
|---|---|
| Teams regularly re-verify that agent context is still accurate and current | 87% |
| Spend significant staff hours reviewing and correcting agent output before it goes live | 51% |
| Same, at organizations with $100 million or more in revenue | 64% |
| Hit critical roadblocks moving from pilot to production in the past 12 months | 76% |
| Have clearly defined executive accountability for a flawed or harmful agent output | 84% |


The survey is small and the vendor's product is the implied answer. The numbers are still the first this blog has seen that count the human re-check as a line item. Half of the surveyed organizations pay a review cost that the word "autonomous" says should not exist.

Fortune's CIO Intelligence column of the same day adds three enterprise practices without survey backing. Cisco's operations EVP says the company will not authorize any third-party vendor's agents, and that a central team has approved about 700 internally built agents. Workday runs an "agent system of record" for every non-human identity. Intuit's GenOS records every request in and every response out, by design from the first sketch. These are executive statements, not audited figures.

## A better unit than lines of code

A paper on arXiv, submitted 4 September 2026, is outside the window and new to this blog. It is *Beyond Code Generation*, by Happy Bhati. It is an 18-page synthesis with no new experiment, and the author says so plainly. It proposes four terms.

The Throughput Paradox: code-generation gains fall off sharply between writing code and shipping reliable software, because review, integration, testing, security and operations stay constraining. **Production-Qualified Change, or PQC: a unit of output that counts a change only after the reliability gates pass.** The Verification Tax: downstream review and assurance cost, made explicit. And a Control Plane that allocates autonomy subject to cost, reliability and human-attention budgets.

The research question is the useful part. Not how much code an agent can generate, but how much production-qualified value a system delivers per dollar, per reviewer-hour and per unit of operational risk. Collibra's "hallucination tax" and Bhati's "verification tax" are the same idea, named twice in the same fortnight, once by a vendor and once by a researcher.

## A governance note

Senator Josh Hawley opened a Senate subcommittee investigation into OpenAI's handling of the July Hugging Face breach. Axios first reported it on 10 September 2026. The letter to OpenAI's CEO asks 16 questions and requests internal documents by 1 October. Senator Richard Blumenthal, the ranking member, sent a separate letter about the Astra model and about when OpenAI knew its agents were reaching other sites.

This blog covered the incident itself in August and the wiki incident in Orders 034 and 035. The new fact is that a congressional document request now exists. That is a different kind of pressure than an EU incident report. It names dates and asks what was known when.

## What changes here

1. **Harden every git spawn the factory's own tooling makes, with environment config, today.** The factory runs git from scripts and CI. Set `GIT_CONFIG_COUNT` and the four keys Cursor used in the environment of every process that runs git on a checked-out repository. This is a shell-level change with no dependency. It closes the class rather than one instance.
2. **Treat the repository as untrusted input to the harness.** Order 037 adopted the Pentagon's phrase for generated code. Extend it one step. A cloned repository can configure git, the editor, Python and skill loaders. Any agent run that opens a repository not authored inside the factory runs in a full virtual machine, not a per-tool sandbox. This matters most for the regulated three, where a compromised developer machine is a PHI incident.
3. **Audit what agent tools installed into global config without asking.** Heapjack shipped in a tool that Codex Desktop wrote into the global config at install. Do the same inventory on every factory machine. List every MCP server and tool entry in every agent's global config. Require that each one was placed there on purpose. Pair this with the tool-definition fingerprint from Order 037.
4. **Adopt Production-Qualified Change as the factory's output metric.** Count a change only when it has passed the test suite, the review gate for its functionality class, and the manifest row. Do not count generated pull requests. This makes the ledger's existing gates the definition of output instead of a tax on it.
5. **Budget reviewer-minutes on every autonomous run and record the actual.** The survey says half of organizations pay a manual review cost they did not plan for. The factory can measure its own. Each ledger entry gets a planned and an actual human-minutes field. After a month, the low-stakes repos will show what the gate costs, and that number decides where autonomy expands.
6. **Keep regulated work human-gated.** Nothing this edition changes that, and two items reinforce it. A vendor sandbox escaped from its strictest mode twice in one report. A partial fix took 50 days to become a full one. CareTime, TimeForCare and MaterialsAndPractices stay at named-human approval for every change in a security, safety or evidence-producing class.
7. **Low-stakes repositories carry the experiments.** MeowPassword takes the git environment hardening and the global-config inventory first, because they are shell-level and cheap. weathergalactic takes the planned-versus-actual reviewer-minutes field. sloth takes the PQC counter.


## Sources

### The escapes

- [Accomplish, *Escaping the OpenAI Codex sandbox, twice*](https://www.accomplish.ai/blog/escaping-the-openai-codex-sandbox-twice/), Oren Yomtov (15 September 2026). Primary. Overpatch, Heapjack, the 12 August report date, the eight-day fix window, Codex CLI 0.149.0 and Codex Desktop 26.818.21641.
- [Accomplish, *Beltdown: Escaping the Claude Code sandbox*](https://www.accomplish.ai/blog/beltdown-escaping-the-claude-code-sandbox/), Oren Yomtov (11 September 2026). Primary. The nested `.git` and `git ls-files` chain, and the timeline in the table above.
- [Accomplish, *Beltdown2: Escaping the Cursor CLI sandbox*](https://www.accomplish.ai/blog/beltdown2-escaping-the-cursor-cli-sandbox/), Or Hiltch (12 September 2026). Primary. The unhardened git spawns, the read-only proof, and the `GIT_CONFIG` fix.
- [Upstarts Media, *Claude Code, Codex, And Cursor Have Leaky Sandbox Problems You Don't Hear About*](https://www.upstartsmedia.com/p/accomplish-claims-leaky-sandboxes-in-claude-codex-cursor), Alex Konrad (10 September 2026). Secondary, paywalled past the preview. The "about 50 days" characterization and OpenAI's statement that both issues were addressed in August.
- [BleepingComputer, *Cursor, Codex, Gemini CLI, Antigravity hit by sandbox escapes*](https://www.bleepingcomputer.com/news/security/cursor-codex-gemini-cli-antigravity-hit-by-sandbox-escapes/), Ax Sharma (20 July 2026). Secondary. Cited only to place these findings in the class covered in July.


### The survey and the practices

- [Collibra press release, *New Survey from Collibra by The Harris Poll Finds 72% of Tech Decision-Makers Feel AI Initiatives Today Are Falling Short*](https://www.prnewswire.com/news-releases/new-survey-from-collibra-by-the-harris-poll-finds-72-of-tech-decision-makers-feel-ai-initiatives-today-are-falling-short-302879680.html) (16 September 2026). Primary for the figures and the research method.
- [Fortune CIO Intelligence, *AI agents are going rogue. CIOs are racing to put guardrails around them*](https://fortune.com/2026/09/16/ai-agents-are-going-rogue-cios-are-racing-to-put-guardrails-around-them/), John Kell (16 September 2026). Secondary. Cisco, Workday, Intuit and ServiceNow statements.


### The paper

- [arXiv 2609.04681, *Beyond Code Generation: Reliability, Verification, and Cost Economics in the Agentic Software Development Lifecycle*](https://arxiv.org/abs/2609.04681), Happy Bhati (submitted 4 September 2026). Primary. A synthesis with no new experiment.


### The investigation

- [Axios, *Scoop: OpenAI faces GOP-led Senate investigation into Hugging Face breach*](https://www.axios.com/2026/09/10/openai-hugging-face-senate-investigation-hawley) (10 September 2026). Secondary. Corroborated by [Nextgov/FCW](https://www.nextgov.com/artificial-intelligence/2026/09/hawley-launches-committee-investigation-openais-breach-hugging-face/415910/) and [Forbes](https://www.forbes.com/sites/zacharyfolk/2026/09/10/openais-hugging-face-hack-faces-senate-investigation/), same day.


### Prior editions referenced

- [Unverified input](2026-09-15-unverified-input.html) (15 September 2026). The Pentagon instruction, the model manifest, and the tool-definition fingerprint.
- [Confidence is not a control](2026-09-14-confidence-is-not-a-control.html) (14 September 2026). The Harness survey and the gate that blocks.


*Vendor and blog figures indicate direction, not audited benchmarks. The Accomplish posts are by a company selling a VM-isolated agent, and their findings are vendor-acknowledged and patched. The Collibra survey has n=306 and a plus or minus 6.4 point interval, and Collibra sells the governance tooling its framing implies. The Fortune executive statements are unaudited. The arXiv paper is a synthesis and claims no new measurements.*


---

Canonical copy: [www.river.io/blog/posts/2026-09-17-the-enforcer-inside.html](https://www.river.io/blog/posts/2026-09-17-the-enforcer-inside.html). Mirrored into this wiki. The river.io blog is the source of truth.
