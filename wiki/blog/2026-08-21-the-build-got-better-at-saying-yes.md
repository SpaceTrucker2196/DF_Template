---
title: "The build got better at saying yes"
date: 2026-08-21
order: 25
tags: "Briefing, Quality, Security"
description: "AI-assisted pull requests break the main branch half as often as human ones. The security of AI-written code has not improved in four years. Both are true, and the gap between them is the argument for a second gate."
layout: default
---

# The build got better at saying yes

*Order 025 · 2026-08-21 · 8 min · Briefing, Quality, Security*

> AI-assisted pull requests break the main branch half as often as human ones. The security of AI-written code has not improved in four years. Both are true, and the gap between them is the argument for a second gate.

The last day produced nothing. No dark-factory writing, no spec movement, no new incident, no new operator numbers. The twenty-first is empty. That is the second quiet window in a row, and saying so plainly is the honest report.

So this edition again closes gaps in the back catalogue. The last edition was about how autonomy fails loudly: deleted databases, malicious packages, national guidance. This one is about how autonomy fails quietly, in the merge queue and in the generated code itself. None of the three items below was published in the last two days. Each date is stated.

## AI pull requests break the build half as often

Mergify published *State of Merge Queues 2026*. The study reads more than **200,000 merged pull requests across 477 engineering organizations** over a rolling 90-day window.

A merge queue is a gate in front of the main branch. It tests each pull request against the current tip before it merges. When a merge still breaks the branch, the study counts it.

| Measure | Value |
|---|---|
| AI-assisted pull requests that broke main | 1.9% |
| Pull requests with no detected AI assistance that broke main | 4.4% |
| Mean changed lines, AI-assisted | 137 |
| Mean changed lines, no AI assistance | 84 |
| Private-repository pull requests that are AI-assisted, at minimum | 1 in 7 |
| Teams that merge one pull request at a time | 94% |
| Median time in the queue | 7 min |


The first two rows are the finding. **AI-assisted work broke the main branch at roughly half the rate of work with no AI assistance.** Rows three and four rule out the easy explanation. The AI pull requests were **larger**, at 137 changed lines against 84. The lower break rate is not a size effect.

The study reports two more things worth keeping. **The broken-main rate rises about 16 times with team size**, from about 1 in 130 merges at 2 to 5 engineers per repository to about 1 in 8 at 40 or more. And **private repositories break main 4.5 times more often than open source ones**.

Mergify calls the 1-in-7 AI-assistance figure a floor, not a count. An assistant that leaves no trace on the commit is invisible to the measurement.

## The security of AI-written code has not moved in four years

Veracode published the *2026 GenAI Code Security Report*. BusinessWire carried the announcement on **28 July 2026**. Veracode has now tested **more than 100 models over four years**.

The average security pass rate is **56%**. It did not move from last year's report. About **44% of code generation tasks produced code with a detectable OWASP Top 10 vulnerability**. OWASP Top 10 is the standard list of the most common web application security flaws.

| Summer 2026 dataset: 11 models, 80 tasks | Pass rate |
|---|---|
| Best model in the set (GPT-5.5) | 68% |
| Six of the eleven models | 50–53% |
| Models purpose-built for code | 51% |
| Four-year average, 100+ models | 56% |


The third row is the uncomfortable one. **Models built specifically to write code averaged 51%, below the overall average.** Capability and security did not move together.

## The two numbers do not disagree

These findings look like a contradiction. They are not. They measure different things.

- **Mergify measures whether the build stayed green.** AI-assisted work wins there. An agent runs the tests before it opens the pull request. A tired engineer at 5pm does not always do that.
- **Veracode measures whether the code was safe.** AI-written code sits at 56%, and it has not improved in a year.


The gap between them is the whole argument for a second gate. A pipeline that gates on "the build is green" now measures the thing an agent is good at. It does not measure the thing an agent is bad at. The break rate went down. The vulnerability rate did not.


The build got better at saying yes. That is not the same as the code getting safer.

There is a second cost hidden in row three of the first table. A 137-line diff with a green build carries more code past the same reviewer than an 84-line diff did. The build says yes faster. The reviewer has more to read. This blog called review capacity the ceiling on 27 July. Nothing here lowers that ceiling.

## The engine under local inference has five open holes

Cyera research audited **llama.cpp** and found **10 vulnerabilities**. The full technical detail was presented at **DEF CON 34** in August 2026.

llama.cpp is a C and C++ library that loads model files and runs inference on a local machine. It is the base of Ollama, LM Studio, Jan and GPT4All. Anyone running a model on their own hardware is almost certainly running it.

The flaws are ordinary memory-safety failures: use-after-free, integer overflow, and out-of-bounds access. **Two llama-server flaws carry a CVSS score of 9.2.** CVSS is the standard 0-to-10 severity scale. At Cyera's most recent check, **five of the ten remained unpatched, including both 9.2 flaws**.

One attack is worth naming. A crafted GGUF model file declares tensor sizes far larger than the data it actually carries. The loader then reads past the buffer and returns heap memory. GGUF is the model file format llama.cpp loads. **A downloaded model file is untrusted input.**

> **THE DEPENDENCY YOU DID NOT PICK**
>
> The zero-dependency rule is this factory's strongest defence, and it does not cover this case. llama.cpp is not a library that got linked in by accident. It is the engine under every local-model tool. A repo can have no third-party dependencies and still run five unpatched memory-safety flaws, two of them rated 9.2.

## What changes here

1. **Add a second gate that is not "the build is green".** The converge loop already gates on tests. It needs a gate that fails on a security class the tests cannot see. For native compiled code the cheap version is a static-analysis pass inside the loop, with the OWASP class named in the failure message.
2. **A newer model is not a security control.** Four years and 100+ models moved that 56% by nothing. A model upgrade changes capability and cost. It does not move any repo up the autonomy ladder.
3. **Cap the diff an agent may open in one pull request.** 137 lines against 84 moves work to the reviewer. A hard line cap is a settings change, not a new system. Small diffs keep the human gate cheap enough to keep.
4. **Pin the inference engine and treat model files as untrusted input.** Any repo that loads a GGUF file inherits llama.cpp's open flaws. One issue, with the Cyera write-up cited in it, per the house rule that every detector links its source.
5. **Turn on batching before agent volume arrives.** 94% of teams merge one pull request at a time. Agents raise pull-request volume. One CI run per pull request multiplies the bill by the same factor. The setting is cheap to change while the bill is small.
6. **Regulated repos do not move.** A 56% security pass rate on generated code is by itself sufficient reason. PHI-touching paths and EVV submissions do not get a 44% chance of an OWASP finding.


The mild good news sits in the first table. If an autonomous loop starts opening pull requests on the low-stakes repos, the build-break risk of agent work is measurably lower than the build-break risk of tired human work. That is a reason to run the experiment. It is not a reason to skip the second gate.

## Sources

### Merge queues

- [Mergify, *State of Merge Queues 2026*](https://mergify.com/reports/state-of-merge-queues-2026). Source of the 1.9% and 4.4% break rates, the 137-versus-84 diff sizes, the 16x team-size effect, the 4.5x private-versus-open-source gap, the 94% single-merge figure, the seven-minute median queue time, and the 1-in-7 AI-assistance floor. The page is not dated. The report covers a rolling 90-day window and is titled for 2026.
- [Mergify, *GitHub Merge Queue Was Step One. Real CI Orchestration Comes Next.*](https://mergify.com/blog/github-merge-queue-was-step-one-real-ci-orchestration-comes-next). Background on batching and queue cost.


### AI code security

- [Veracode, *2026 GenAI Code Security Report*](https://www.veracode.com/resources/analyst-reports/2026-genai-code-security-report/). The report itself.
- [BusinessWire, *LLMs Are Getting Smarter, But Not Safer*](https://www.businesswire.com/news/home/20260728207685/en/LLMs-Are-Getting-Smarter-But-Not-Safer-Veracode-2026-GenAI-Code-Security-Report-Finds-AI-Generated-Code-Security-Has-Stalled-at-56-Pass-Rate) (28 July 2026). The dated announcement, and the source of the 56% stall.
- [SD Times, *Veracode Finds AI-Generated Code Security Has Barely Improved Since Last Year*](https://sdtimes.com/agentic-security/veracode-finds-ai-generated-code-security-has-barely-improved-since-last-year/). Source of the 11-model, 80-task summer dataset and the per-model rates.
- [eSecurity Planet, *Veracode Finds AI-Generated Code Still Struggles With Security*](https://www.esecurityplanet.com/threats/veracode-finds-ai-generated-code-still-struggles-with-security/). Source of the 44% OWASP Top 10 figure.


### Local inference

- [Cyera, *Local AI Security Fragility: Vulnerabilities Inside the Engine Running Your Local Models*](https://www.cyera.com/blog/local-ai-security-fragility-vulnerabilities-inside-the-engine-running-your-local-models). Source of the 10 vulnerabilities, the two 9.2 ratings, the five-still-unpatched count, and the GGUF tensor-size attack.
- [eSecurity Planet, *DEF CON 34: 10 Vulnerabilities Put Local AI at Risk*](https://www.esecurityplanet.com/threats/def-con-34-10-vulnerabilities-put-local-ai-at-risk/). The conference disclosure.


### Prior editions referenced

- [Fifty-nine attacks, zero CVEs](2026-08-20-fifty-nine-attacks-zero-cves.html) (20 August 2026). The loud failure modes: malicious packages with no CVE, nine agent-deleted production environments, and the six-agency guidance.
- [Review capacity is the new ceiling for AI-written code](2026-07-27-review-capacity-is-the-new-ceiling-for-ai-written-code.html) (27 July 2026). Why diff size, not model quality, sets the throughput limit.


*Vendor and analyst figures indicate direction, not audited benchmarks. The Mergify corpus is drawn from its own customers' repositories, which self-select for teams that already run a merge queue, and its AI-assistance detection relies on traces left on the commit, so the 1-in-7 figure under-counts. The Veracode pass rate measures generated code in isolation, not code after human review. The Cyera findings are one vendor's audit.*


---

Canonical copy: [www.river.io/blog/posts/2026-08-21-the-build-got-better-at-saying-yes.html](https://www.river.io/blog/posts/2026-08-21-the-build-got-better-at-saying-yes.html). Mirrored into this wiki. The river.io blog is the source of truth.
