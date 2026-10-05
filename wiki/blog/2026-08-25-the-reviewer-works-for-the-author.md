---
title: "The reviewer works for the author"
date: 2026-08-25
order: 27
tags: "Briefing, Review, Autonomy"
description: "Five in six AI code reviews are the vendor checking its own work. A second study found an LLM made specification reviewers less accurate and no faster. A third product shipped scheduled agents with the approval prompts turned off."
layout: default
---

# The reviewer works for the author

*Order 027 · 2026-08-25 · 8 min · Briefing, Review, Autonomy*

> Five in six AI code reviews are the vendor checking its own work. A second study found an LLM made specification reviewers less accurate and no faster. A third product shipped scheduled agents with the approval prompts turned off.

Three items landed on 21 August 2026. They come from three different fields. They say one thing. The gate you think you have is probably not a gate.

The last edition of this blog said the review layer is the bottleneck. This edition says something harder. In three separate measurements, the review layer is also not a control.

## Five in six AI reviews are the same vendor twice

Researchers posted a paper to arXiv on **21 August 2026**. The title is *AI-to-AI Code Reviews of GitHub Pull Requests*. The authors are Niruthiha Selvanayagam and Taher A. Ghaleb. The paper is accepted at ESEM 2026 in the Emerging Results track.

The authors linked agent-written pull requests to AI review events. They used CodAGE, a public dataset of coding-agent activity on GitHub. The window runs from 1 January 2024 to 15 April 2026.

| Agent-authored pull requests with at least one AI review | Count |
|---|---|
| Total | 248,641 |
| Reviewed by the same product that wrote them | 208,145 |
| Reviewed by a different product | 45,269 |
| Reviewed by both | 4,773 |


Nobody chose this. It comes from the app install. The per-product numbers make that plain.

| Authoring product | Reviewed by the same product |
|---|---|
| GitHub Copilot | 95.7% |
| Amazon Q | 91.8% |
| Claude Code | 0.5% |
| Cursor | 0% |


Copilot reviews Copilot code because both arrive in one installation. Cursor does not, because Cursor does not ship a review bot into the same repository. The authors say the pattern may reflect product design. It does not reflect anyone's judgement about who should review what.

Read the limits carefully. The paper measured **who reviewed whom, not whether the reviews were good**. It did not test for leniency. Attribution depends on signatures such as a bot login, so every count is a lower bound. The pipeline quarantined 1,733,535 of 4,563,819 candidate pull requests, or 38.0%, for weak evidence.

The growth is not in doubt. Closed-loop review went from 57 cross-product and 40 same-product pull requests in 2025-Q1 to 25,492 and 57,080 in 2025-Q3.

## Why independence matters even without bias

The tempting argument is the weak one. Self-preference says a model goes easy on its own output. Nobody has shown that for code review at scale, and this paper did not try.

The strong argument needs no bias at all. It needs correlated failure. Two instances of one model family share training data. They share blind spots. A reviewer that misses what the author missed is not a control.


A reviewer that shares the author's blind spots is a copy, not a control.

This is the same failure the last edition reported. An automated security scan read a vulnerable file and passed it. The tool was not broken. It was the wrong second opinion.

## Two documentation facts worth more than the study

Both are checkable in your own repositories today.

**GitHub Copilot code review cannot block a merge.** GitHub's own documentation states that Copilot always leaves a "Comment" review, never "Approve" or "Request changes". Its reviews do not count toward required approvals and will not block merging. Any team that thinks otherwise is wrong in the safe direction.

**CodeRabbit can approve, but only if one key is set.** The `@coderabbitai approve` command submits a real approval only when `reviews.request_changes_workflow` is `true` in `.coderabbit.yaml`. That key defaults to `false`. One line in one file decides whether the bot comments or satisfies a required-approval rule.

## The assistant made spec reviewers worse

A second paper went to arXiv on **21 August 2026**. The authors are Giovanna Broccia, Julian Frattini, Chetan Arora, Maurice ter Beek, Alessandro Fantechi, Andreas Vogelsang and Alessio Ferrari.

They ran a controlled crossover experiment with **34 inspectors**. Each person read two comparable specifications with seeded defects. One had 40 requirements and 21 defects. The other had 39 and 19. Half the group worked unaided first, then with ChatGPT. The other half worked in the reverse order, with a week between sessions.

| Measure | Result |
|---|---|
| Defect detection F1, unassisted versus assisted | about 8% higher |
| Task duration difference | none significant |
| Classification accuracy difference | none significant |


The trade everyone assumes they are making was not on offer. The assistant did not buy speed. It cost accuracy. There is no measurement in this experiment on which it won.

Hold the number loosely. The authors report that the 95% credibility intervals still overlap. Eight percent is the observed gap in a 34-person student sample, not a bounded effect. The direction is the authors' stated conclusion. The size is not something to plan around.

The second result is the expensive one.

| Improvement between the two sessions | Detection F1 |
|---|---|
| Group that learned unaided first | about 12% |
| Group that started with the tool | about 7% |


Both groups improved. They did not improve equally. The authors read this as a carryover effect, which is the standing hazard of a crossover design. Their conclusion is that early reliance on the model may short-circuit the reflective reading through which a novice builds inspection skill.

The fix is in the paper, and it is one sentence. Restrict the model to phases after first-pass detection. Read the specification yourself. Write the defect list. Then let the model check the list.

> **PLACEMENT, NOT PROCUREMENT**
>
> The same model, at the wrong stage of the workflow, turns a reviewer into an approver. The order is the control. The tool is not the problem.

## Scheduled agents shipped with the prompts turned off

Snowflake moved CoCo automations to preview on **21 August 2026**. An automation turns a prompt into a recurring, unattended run. It runs in a Snowflake-managed sandbox. The minimum schedule is once per hour. It runs when the browser and the terminal are closed.

Interactive CoCo has a careful permission model. Snowflake documents three tiers. `ls`, `cat` and `grep` are safe and run without asking. File edits prompt. `rm`, `curl` and `sudo` always prompt. `INSERT`, `UPDATE` and `DELETE` prompt. Switching roles prompts.

Then the automations page states the rule for scheduled runs. Because the runs are unattended, the interactive tool permission prompts are disabled. Tools available to the run execute without waiting for approval.

Every tier collapses at once. The classification survives. The enforcement does not, because there is nobody to ask.

Two more details compound it. Snowflake documents that each run uses the creating user's **default role plus every default secondary role**, not the role that was active when the automation was made. Since behaviour change bundle 2024_08, that secondary-role property defaults to `ALL`. Snowflake also documents that the privilege which permits all of this, `EXECUTE AGENT TASK`, is granted to the `PUBLIC` role by default.

The third detail is the one to write on the wall. Snowflake documents that **a failing hook does not fail the run**. Task history reports the run as succeeded either way. An audit trail can read SUCCESS while the guard never ran.

## What changes here

1. **Write the reviewer-independence rule now.** One sentence: an approving review from the same product family as the authoring agent does not satisfy the independent-review requirement. It costs nothing today. It costs a lot to retrofit.
2. **Audit which bots can approve.** For every repository, list the bots with write access that can submit an approving review. Check whether `reviews.request_changes_workflow` is set anywhere. This is a query, not a project.
3. **Read the specification before the model does.** Write your own defect list first. Give the model the list second. The current habit of asking the model first is the condition that lost accuracy in the experiment.
4. **Turn every approval gate into a deny rule.** A gate that works by pausing and asking a human is not a control once the loop runs overnight. Rewrite each one so it fails closed: a branch protection rule, a required status check, a test that exits non-zero.
5. **Test that a failing guard fails the run.** Break one pre-run check on purpose and confirm the run reports failure. A broken guard that reports success is worse than no guard, because it is trusted.
6. **Give any scheduled loop a narrow identity and its own cost line.** A timed experiment on MeowPassword, weathergalactic or sloth gets a credential scoped to that one repository. Not a personal one.
7. **Regulated repos do not move.** CareTime, TimeForCare and MaterialsAndPractices stay human-gated. The argument is one line: in five of six cases the AI reviewer works for the AI author, and nobody has measured whether that catches anything.


Two detectors fall out of this edition, and both are static. First, flag a workflow where a bot account can satisfy a required approval. Second, flag a hook whose non-zero exit does not fail the job. That is worth one issue, with the sources cited in it, per the house rule that every detector links its source.

## Sources

### AI-to-AI code review

- [arXiv:2608.21311, *AI-to-AI Code Reviews of GitHub Pull Requests*](https://arxiv.org/abs/2608.21311) (21 August 2026). Primary source. The 248,641 pull requests, the 208,145 same-product split, the per-product shares, the filtering pipeline, and the quarterly growth. Accepted at ESEM 2026, Emerging Results track. Preprint.
- [Full text of arXiv:2608.21311](https://arxiv.org/html/2608.21311v1).
- [GitHub Docs, *Copilot code review*](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review). Source of the statement that Copilot reviews are always "Comment" and never count toward required approvals.
- [CodeRabbit Docs, *Commands*](https://docs.coderabbit.ai/guides/commands) and [YAML reference](https://docs.coderabbit.ai/reference/yaml-template). Source of the `reviews.request_changes_workflow` behaviour and its `false` default.
- [arXiv:2607.03316](https://arxiv.org/abs/2607.03316). Developers accepted 36.4% of AI review suggestions, rejected 56.3% and discussed 7.3%, across 31,073 pairs in 239 repositories.
- [THE DAILY BRIEF, *Same Vendor Wrote and Reviewed 208,145 PRs*](https://www.beri.net/article/ai-to-ai-code-review-same-vendor-reviewer-independence-gap) (23 August 2026). Analysis.


### LLM support in specification inspection

- [arXiv:2608.21298](https://arxiv.org/abs/2608.21298) (submitted 21 August 2026). Primary source. 34 inspectors, the crossover design, the 8% detection gap, the absence of a duration effect, and the 12% against 7% learning gap. Preprint with overlapping credibility intervals.
- [Full text of arXiv:2608.21298](https://arxiv.org/html/2608.21298v1).
- [THE DAILY BRIEF, *ChatGPT Made Spec Reviewers Worse*](https://www.beri.net/article/llm-requirements-inspection-f1-drop-novice-inspector-skill-acquisition) (24 August 2026). Analysis.


### Unattended scheduled agents

- [Snowflake release notes, *Aug 21, 2026: CoCo automations in CLI and Snowsight (Preview)*](https://docs.snowflake.com/en/release-notes/2026/other/2026-08-21-cortex-code-automations). Primary source for the preview date.
- [Snowflake, *CoCo automations*](https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code-automations). Source of the disabled approval prompts, the run identity, the `EXECUTE AGENT TASK` grant to `PUBLIC`, the hourly minimum, and the hook-failure behaviour.
- [Snowflake, *CoCo CLI security*](https://docs.snowflake.com/en/user-guide/cortex-code/security). Source of the three-tier approval model.
- [Snowflake behaviour change bundle 2024_08](https://docs.snowflake.com/en/release-notes/bcr-bundles/2024_08/bcr-1692). Source of the `DEFAULT_SECONDARY_ROLES` default of `ALL`.
- [THE DAILY BRIEF, *Snowflake Agents Run as All Your Roles*](https://www.beri.net/article/snowflake-coco-automations-default-role-agent-task-public-grant) (22 August 2026). Analysis.


### Prior editions referenced

- [The scaffold is the product](2026-08-23-the-scaffold-is-the-product.html) (23 August 2026). The Codex Harness release, and the security scan that passed a live injection flaw.
- [The ceiling is who can check the work](2026-08-18-the-ceiling-is-who-can-check-the-work.html) (18 August 2026). Why review capacity sets the throughput limit.


*Vendor and analyst figures indicate direction, not audited benchmarks. Both arXiv items here are preprints, one accepted to a conference track and one under submission. The specification result comes from 34 students using a raw chat interface with May 2025 models, and its authors report overlapping credibility intervals, so the direction is the claim and the size is not. The Snowflake statements are quoted from Snowflake's own documentation, which describes intended behaviour rather than an independent test. All three items were published on or after 21 August 2026.*


---

Canonical copy: [www.river.io/blog/posts/2026-08-25-the-reviewer-works-for-the-author.html](https://www.river.io/blog/posts/2026-08-25-the-reviewer-works-for-the-author.html). Mirrored into this wiki. The river.io blog is the source of truth.
