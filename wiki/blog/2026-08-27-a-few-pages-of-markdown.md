---
title: "A few pages of Markdown"
date: 2026-08-27
order: 28
tags: "Briefing, Specs, Practice"
description: "Coding agents raised commit volume by the same amount everywhere. Quality did not follow. Repositories with a committed rules file took half the complexity damage. Then 73.8% of those files were never touched again."
layout: default
---

# A few pages of Markdown

*Order 028 · 2026-08-27 · 8 min · Briefing, Specs, Practice*

> Coding agents raised commit volume by the same amount everywhere. Quality did not follow. Repositories with a committed rules file took half the complexity damage. Then 73.8% of those files were never touched again.

Four papers landed on 25 and 26 August 2026. The last edition of this blog said the review gate is not a control. This edition says the thing that is measurably doing work is not a gate at all. It is a file somebody wrote down.

## The same speed, different damage

A team posted a paper to arXiv on **26 August 2026**. The title is *A Few Pages of Markdown: Committed AI Configuration and Lower Quality Cost after Coding-Agent Adoption*. The authors are Yegor Denisov-Blanch, Shyam Agarwal, Pavel Azaletskiy, Hao He, Rylan Schaeffer, Brando Miranda, Bogdan Vasilescu and Sanmi Koyejo.

They built RAMP, which stands for Repository AI Maturity Profile. RAMP is a four-level maturity model. A maturity model is a scale that says how far a team has taken a practice. RAMP scores each level from files the team commits to the repository to configure its AI tools.

The levels run from behavioral rules and coding standards, through named agent definitions, to multi-agent orchestration. Observed practice sits in the first three levels. Almost nobody reaches the fourth.

The team scored 441 repositories. The levels behaved as a cumulative scale, which means a team at level three also holds the level-one files. Independent human annotators reproduced the tool's repository labels on 97% of a held-out sample. That agreement rate is what makes RAMP usable by other people.

Then they re-estimated an existing agent-adoption panel inside each level. The result splits cleanly in two.

| Effect of coding-agent adoption | Result |
|---|---|
| Extra commits, at every maturity level | 28% to 38% |
| Cognitive complexity, agent-first repos with committed AI configuration | +27% |
| Cognitive complexity, agent-first repos without it | +53% |
| Static-analysis warnings, without against with | 1.7 times |


Speed did not care about maturity. The commit lift was the same at every level. Quality diverged. The repositories with no committed configuration gained roughly twice the cognitive complexity, and 1.7 times the static-analysis warnings.


Throughput reports the same number for a healthy repository and a sick one.

Hold the causal claim loosely. The authors do. They state that maturity is observational, that correlated engineering discipline or model capability may explain part of the gap, and that they present the findings as hypothesis-generating. Teams that bother to commit a rules file are probably careful teams already. Writing the file may not import the care.

What the study does establish is that the two groups exist, that they diverge, and that the artifact costs about an hour.

## The catch is in the commit history

The same paper reports the adoption pattern. It is cumulative, forward-only and set-and-forget. The number that matters is this one.

> **SET AND FORGET**
>
> 73.8% of committed AI configuration artifacts were committed once and never modified again.

Teams write the rules, then stop reading them. A rule file that no longer matches the code is a specification that lies. An agent reads it and complies with the wrong thing, confidently. The commit history cannot tell you which case you are in. A file untouched for a year is either exactly right or completely ignored, and both look identical from outside.

## Spec-driven development gets a census

A second paper went to arXiv on **25 August 2026**. It is SPECMINE, by Shyam Agarwal and Bogdan Vasilescu. Spec-driven development is a practice where a structured natural-language specification drives a coding agent's implementation. Tools have shipped for it since 2025. Nobody had measured the artifacts at scale.

| SPECMINE coverage | Count |
|---|---|
| Spec files, broad census | 470,795 |
| Repositories in the broad census | 73,030 |
| Named tools attributed | 17 |
| Files in the AWS Kiro census | 98,574 |
| Repositories in the Kiro census | 12,910 |
| Spec-touching pull requests captured, 11 tools | 5,992 |
| Typed references indexed | 2,421,323 |


The 5,992 pull requests come from 581 repositories with at least ten stars, captured with their changesets. That makes the simplest workflow directly observable: spec and implementation changing together in one pull request.

Read the limit of that. A spec that changes in the same pull request as the code proves nothing about order. An agent that writes the code first, then rewrites the spec to match, produces the same diff as a disciplined spec-first change. The artifact exists. The evidence of intent does not. This is the traceability trap.

## Settled and uncertain

A third paper went to arXiv on **25 August 2026**. It is *Model-Based Agentic Software Engineering*, or MAGE, by James C. Davis, Kelechi Kalu, Huiyun Peng and Parth V. Patil. The authors built it from one longitudinal case and refined it against six independently reported industrial accounts.

MAGE names two problems. The representation problem asks what the smallest written record is that answers an engineering question. The authority problem asks which obligations get to stop the work.

Its prescription is one distinction worth stealing whole. Obligations are either **settled** or **uncertain**. A settled obligation is one the team has already decided. It gets proportionate authority through a constraint, a sensor, a validator or a gate. An uncertain intent stays open and stays with the human.

The failure this names is gating something nobody has decided yet. That produces a rule that gets waived. A rule that is routinely waived teaches everyone that rules get waived. MAGE is a theory paper. It reports no effect sizes and proposes tests rather than passing them. The vocabulary is the useful part.

## Breaking the guard on purpose

A fourth paper went to arXiv on **25 August 2026**, from TU Delft. The authors are Zahra Seyedghorban, Egor Klimov, Arie van Deursen, Annibale Panichella and Burcu Kulahcioglu Ozkan. The tool is called llmmas-otel and it carries an IEEE ICST 2026 DOI.

It combines OpenTelemetry distributed tracing with targeted fault injection. Fault injection means you break a chosen part of the system on purpose. The tool instruments workflow phases, agent steps, communication between agents, tool calls and model invocations. Then it lets an operator compare a clean run against a deliberately broken run and diff the aligned traces.

This is the practical answer to a question this blog has now raised three editions running. The last edition reported that a failing hook can report success. Fault injection is how you find that out on purpose, before it happens by accident. The hosted tool is not the point. The technique transfers to any pipeline, including one built from compiled native code with no third-party dependencies.

## What changes here

1. **Commit the rules file.** The zero-dependency rule, the native-compiled rule and the test-driven rule are exactly the level-one RAMP artifacts. If they live only in a person's head, the agent cannot read them. This is an hour of work with the best evidence behind it this week.
2. **Put a review date at the top of that file.** One line: last reviewed, with the date. The 73.8% number is the specific trap for a small shop, because nobody else will notice the file went stale.
3. **Record the complexity baseline before the loop runs, not after.** The RAMP result is only visible because someone held before-and-after measurements. Capture the current cognitive-complexity and static-warning counts and commit that number.
4. **Sort obligations into settled and uncertain.** Settled things get a validator or a failing test. Everything else stays a human decision and gets no gate. This says what each gate is for, which a per-repository autonomy level does not.
5. **Break one guard on purpose.** Take one converge loop, disable one check, and confirm the run fails and the failure is visible. Do it in a low-stakes repository first.
6. **Do not confuse a spec-touching commit with spec-driven work.** In an issue-driven pipeline the issue is the spec. What matters is that the issue text is settled before the implementation commit, not merely present in the same pull request.
7. **Regulated repos do not move.** CareTime, TimeForCare and MaterialsAndPractices stay human-gated. Agent adoption raised commit volume everywhere and raised complexity everywhere. The only measured mitigation is an observational correlate. That is not a strong enough control for PHI paths or EVV submissions.


Two detectors fall out of this edition, and both are static. First, flag a repository that shows coding-agent activity but holds no committed AI configuration file. Second, flag a committed AI configuration file whose last modification is far older than the repository's most recent significant change. That is the set-and-forget signal. Both are worth one issue, with the sources cited in it, per the house rule that every detector links its source.

## Sources

### Committed AI configuration and code quality

- [arXiv:2608.25241, *A Few Pages of Markdown: Committed AI Configuration and Lower Quality Cost after Coding-Agent Adoption*](https://arxiv.org/abs/2608.25241) (submitted 26 August 2026). Primary source. The RAMP four-level model, 441 repositories, the 97% human label agreement, the 73.8% never-modified figure, the 28% to 38% commit lift, the +53% against +27% cognitive complexity split, and the 1.7 times warning ratio. Preprint. The authors state the finding is observational and hypothesis-generating.
- [Full text of arXiv:2608.25241](https://arxiv.org/html/2608.25241v1).


### Spec-driven development at scale

- [arXiv:2608.25202, *SPECMINE: A Large-Scale Corpus of Spec-Driven Development Artifacts*](https://arxiv.org/abs/2608.25202) (submitted 25 August 2026). Primary source. The 470,795 spec files across 73,030 repositories, the 17 named tools, the Kiro census of 98,574 files across 12,910 repositories, the 5,992 spec-touching pull requests across 581 repositories, and the 2,421,323 typed references. Dataset paper. Preprint.
- [Full text of arXiv:2608.25202](https://arxiv.org/html/2608.25202v1).


### Framework and vocabulary

- [arXiv:2608.25174, *Model-Based Agentic Software Engineering*](https://arxiv.org/abs/2608.25174) (submitted 25 August 2026). Primary source. The representation problem and the authority problem, the constraints, sensors, validators and gates, the settled against uncertain distinction, and the one longitudinal case plus six industrial accounts. Theory paper. Reports no effect sizes.
- [Full text of arXiv:2608.25174](https://arxiv.org/html/2608.25174v1).


### Observability and fault injection

- [arXiv:2608.24271, *Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering*](https://arxiv.org/abs/2608.24271) (submitted 25 August 2026). Primary source for llmmas-otel, the OpenTelemetry tracing, the targeted fault injection, and the baseline against faulty run comparison.
- [IEEE ICST 2026 DOI 10.1109/ICST69053.2026.00037](https://doi.org/10.1109/ICST69053.2026.00037) for the same paper.
- [arXiv:2608.25322, *Metis: Typed Runtime Mediation for Tool-Using Software Agents*](https://arxiv.org/abs/2608.25322) (25 August 2026). Noted, not featured. The authors state the supporting artifact is still being curated.
- [arXiv:2608.25474, *Separating Disclosure from Authorization: Field-Tier Minimization for Agent Action Mediation*](https://arxiv.org/abs/2608.25474) (25 August 2026). Noted, not featured. Describes an implemented system in private pilot.


### Prior editions referenced

- [The reviewer works for the author](2026-08-25-the-reviewer-works-for-the-author.html) (25 August 2026). Reviewer independence, and the failing hook that reports success.
- [The scaffold is the product](2026-08-23-the-scaffold-is-the-product.html) (23 August 2026). The security scan that passed a live injection flaw.


*Vendor and analyst figures indicate direction, not audited benchmarks. Every item featured here is an arXiv preprint posted on 25 or 26 August 2026, and none has completed peer review, though the TU Delft tool paper carries an IEEE ICST 2026 DOI. The quality gap in the RAMP paper is an observational correlation which its own authors decline to treat as causal.*


---

Canonical copy: [www.river.io/blog/posts/2026-08-27-a-few-pages-of-markdown.html](https://www.river.io/blog/posts/2026-08-27-a-few-pages-of-markdown.html). Mirrored into this wiki. The river.io blog is the source of truth.
