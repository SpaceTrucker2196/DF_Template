---
title: The autonomy levels
layout: default
---

# The autonomy levels

Teams use a ladder of levels to say how much of the work an agent does without a human. This page holds the two ladders the history uses, and the lesson both share.

## Shapiro's five levels (23 January 2026)

Dan Shapiro, CEO of Glowforge, published "The Five Levels: from Spicy Autocomplete to the Dark Factory." He modeled it on the self-driving taxonomy. Source: [Order 002](../blog/2026-05-26-ninety-percent-of-ai-native-developers-are-stuck-at-level-2.html).

| Level | Name | What it means |
|---|---|---|
| 0 | Spicy Autocomplete | Not one character reaches the disk without human approval |
| 1 | Coding Intern | AI writes boilerplate and low-stakes snippets under full human review |
| 2 | Junior Developer | A human pair-programs with the model and reviews every line |
| 3 | Developer | Most code is AI-generated. The human is a full-time reviewer |
| 4 | Engineering Team | The human works on specs and plans. Agents do the work |
| 5 | Dark Factory | No human writes or reviews code. Humans define intent and review outcomes |

Shapiro claims that about 90 percent of developers who call themselves "AI-native" stay at Level 2.

## River's driving-style levels (27 July 2026)

[Order 001](../blog/2026-07-27-the-repo-is-the-factory.html) uses the SAE driving levels. They ask who writes, who tests, who reviews and who decides scope.

| Level | Name | Writes code | Runs tests | Reviews | Decides scope |
|---|---|---|---|---|---|
| 0 | Manual | Human | Human | Human | Human |
| 1 | Assisted | Human | Human | Human | Human |
| 2 | Partial | Human and agent | Human | Human | Human |
| 3 | Conditional | Agent, supervised | Agent and human | Human | Human |
| 4 | High | Agent | Agent | Agent, spot-checked | Human |
| 5 | Full | Agent | Agent | Agent | Agent, within mission |

## Other ladders in the record

Grab published a five-level model with four months of data ([Order 023](../blog/2026-08-18-the-ceiling-is-who-can-check-the-work.html)). China requires three tiers of decision authority before deployment ([Order 016](../blog/2026-08-03-regulators-are-writing-the-autonomy-tiers-into-law.html)).

## What the ladders agree on

The move from Level 3 to Level 4 is repository work. It is not model work (Order 001). Verification and governance gate the jump to Levels 4 and 5, not model capability (Order 002). Match the level to the stakes of the work. A repository can hold different levels for different directories (see [Order 034](../blog/2026-09-07-which-paths-it-may-finish.html) for autonomy by path).
