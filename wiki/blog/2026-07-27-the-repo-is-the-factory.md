---
title: "The repo is the factory"
date: 2026-07-27
order: 1
tags: "Pattern, Autonomy, Metrics"
description: "A dark factory repo holds the mission, the conventions, the tests, and the autonomy boundary in-tree. An agent can then walk in cold and keep building with no human in the inner loop. Here is what that takes."
layout: default
---

# The repo is the factory

*Order 001 · 2026-07-27 · 9 min · Pattern, Autonomy, Metrics*

> A dark factory repo holds the mission, the conventions, the tests, and the autonomy boundary in-tree. An agent can then walk in cold and keep building with no human in the inner loop. Here is what that takes.

In manufacturing, a dark factory is a plant that runs without humans on the floor. The lights are off because no human eyes need to see. Nobody stands at a station. The machines feed each other, inspect each other, and call for help only on exception. It is not a metaphor for working faster. It is a claim about where the humans stand: at the edges, where they set direction and accept output, not in the middle passing parts along.

Point that at a software repository and you get a useful, uncomfortable test. Ask what would have to be true about this repo for the whole build, test, and review loop to run with no human in the inner loop. The question is not whether an AI can write a given function. That question is settled and boring. The real question is whether the repo itself is built so that an agent never has a legitimate reason to stop and ask.

Most repos fail that test immediately. They fail it for reasons that have nothing to do with model capability.

## Be honest about your level

It helps to borrow the SAE driving-autonomy levels. They force an honest answer to a question people usually answer aspirationally.

| Level | Name | Writes code | Runs tests | Reviews | Decides scope |
|---|---|---|---|---|---|
| 0 | Manual | Human | Human | Human | Human |
| 1 | Assisted | Human | Human | Human | Human |
| 2 | Partial | Human + agent | Human | Human | Human |
| 3 | Conditional | Agent, supervised | Agent + human | Human | Human |
| 4 | High | Agent | Agent | Agent, spot-checked | Human |
| 5 | Full | Agent | Agent | Agent | Agent, within mission |


Nearly all AI-assisted development in the wild is Level 2 or Level 3. That is fine. The point of naming the levels is not to shame anyone up the ladder. The point is that the work required to move from 3 to 4 is **not model work**. It is repository work. A dark factory repo is the substrate that makes Level 4 or 5 possible for a given project.

That substrate does not guarantee the agent is good enough yet. It removes every reason the agent would have to stop and ask.

> **The distinction that matters**
>
> An agent stops because the task is genuinely ambiguous. That is the system working. An agent stops because the build command lives in someone's shell history. That is the system failing. Almost every interruption in practice is the second kind.

## What has to be in the tree

The pattern is a checklist. The test for each item is the same: a fresh clone, on a fresh machine, handed to an agent that has never seen the project.

### The mission

Put a file at the root of the repo. It says why the software exists, in one paragraph. It says what the software must never become. It says where the project honestly is right now. It says where the gravity is pointing. The "must never become" list is the load-bearing part. It holds the ethical, legal, and architectural lines that nobody crosses, even when crossing them would help.

If the mission lives in someone's head, in a Slack channel, or in a private doc, the project is not Level 5. It is Level 3 with a brittle dependency on one person being awake.

### The conventions

Write down the build and test commands. Write down where new files go. Write down the comment policy. Write recipes for the changes that recur: how to add a view, how to add an alert rule, how to add a parser. Write down the hard don'ts.

There is a clean test for whether this document is finished. Hand it to an agent and ask for a routine feature, without being in the room. Every question the agent has to ask is a gap. Closing that gap is part of the work, not a chore for later.

### Tests as the oracle

Green has to mean ship-ready. In a dark factory, nothing else is going to catch the problem. Three rules earn their keep:

- Write tests from first principles. Never write a test that feeds a parser its own output. That loop passes happily when both halves are wrong.
- Ship every bug fix with the test that would have caught it. This is how the factory learns. Each escape becomes a new inspection step.
- Keep builds warning-clean. Warnings are the only signal that something compiled but is still wrong. Treat them as background noise and the signal is gone.


If the honest description of the suite is "it mostly catches things", the human is still the oracle. The level is still 3.

### The repo is the working directory

Nothing the agent needs lives outside the clone. No environment variables that only the owner knows. No licence key in a password manager. No "run this one script first" folklore. Agent memory outside the repo is a convenience. The repo must never depend on it.

## The part everyone skips

The mission says what the software does. The conventions say how to build it. Neither one tells the agent *when to stop*. That omission is the single most common reason autonomy fails in practice, and it fails in both directions. An agent with no written boundary asks about everything, which is Level 2 in a costume. Or it decides everything, which is Level 5 with no brakes.

So write the boundary down, in the repo, in three buckets. **Decides**: naming, structure, which helper to extract, bug fixes whose cause is obvious from the evidence, features that fit a pattern the docs already describe, and refactors that preserve the public contract. **Decides and flags**: choosing between two reasonable architectures, disabling a test, adding a dependency, and changing a long-stable default. The call is the agent's, but the commit message has to say what it decided and why. **Stops and asks**: anything that edits the non-negotiable rules, breaks an external contract, is destructive, reaches outside the repo, costs money, or expands the scope beyond what was ordered.


Decisions inside the mission are yours. Decisions about the mission are not.

There is a subtler line inside that last bucket. State it separately, because it is the one agents get wrong. Tactical uncertainty, such as "I do not know how to centre this div", is not a reason to stop. Go and find out. Structural uncertainty, such as "I do not know whether this feature belongs in this product at all", is exactly the reason to stop. Most bad autonomous work is a structural question quietly answered as though it were a tactical one.

## What one production order looks like

With those pieces in place, the unit of work stops being a pull request. It becomes a **production order**: a GitHub issue whose body is the spec. A single command takes it to a pushed, instrumented commit. The steps never skip forward. A failed gate loops back.

```
1. Read the order      issue body is the spec; ambiguity -> comment and stop
2. Plan               files touched, tests to add, risks
3. Generate           implement; tests land with the code
4. Converge           run the oracle until green; count the iterations
5. Self-review        read the diff end to end; simplify
6. Risk gate          anything in stops-and-asks -> surface before shipping
7. Ship               commit with why in the body, push
8. Instrument         append the metrics row; append the cost ledger row
9. Report             comment the shipped commit back on the issue
```


Step 8 turns a nice idea into a factory. Every shipped order appends a row to an append-only `METRICS.md`. The row holds the issue number, the commit, the date, how many converge iterations it took, and how many tests existed at ship time. Cost goes in a separate append-only ledger, joined on the commit sha. Nobody rewrites rows. You cannot manage a process you do not measure, and a process that remembers only its successes is not measured.

## What the records say

Here is a worked example, from the tree of an iOS instrument shipped this month. Nine production orders ran in a single day.

| Order | What shipped | Converge iters | Tests at ship |
|---|---|---|---|
| 1 | Timer ladder | 1 | 5 |
| 2 | Alpha band split | 1 | 6 |
| 4 | Preset launch hook | 1 | 7 |
| 3 | Health logging | 1 | 8 |
| 5 | Beat knob | 1 | 11 |
| 6 | Beam modes | 1 | 13 |
| 7 | Orbit rate, phase threading | 1 | 15 |
| 10 | Demo gate | 1 | 18 |
| 8 | Preset browser | 2 | 26 |


Two things in that table are worth more than the throughput. The first is the tests column: 5 to 26 across nine orders, because tests ship with the code rather than after it. The second is the single 2 in the converge column. Order 8 needed a second lap to fix a band-boundary rounding error. That row is the useful one. It is a recorded, attributable escape, caught by the oracle rather than by a user. It stays in the permanent record because rows are append-only.

A factory that reports only its clean runs is a brochure.

## The drill

Converting an existing repo takes five steps, and the order matters. Write the mission. Write the conventions. Make the tests the oracle. Write the autonomy contract. Then run the drill.

The drill is the whole thing. Clone the repo onto a machine that has never built it. Hand it to an agent that has never seen it. Ask for one real feature. Then stay out of the room. Whatever the agent has to ask you is the next document you owe the repo.

You are at Level 5 when the drill succeeds. You get there when the repo is good enough, not when the model is.

---


This is the first post of a running log about building this way. It covers the pattern, the places it breaks, the numbers it produces, and the things it turns out not to be good at. Future orders are queued on the archive page.


---

Canonical copy: [www.river.io/blog/posts/2026-07-27-the-repo-is-the-factory.html](https://www.river.io/blog/posts/2026-07-27-the-repo-is-the-factory.html). Mirrored into this wiki. The river.io blog is the source of truth.
