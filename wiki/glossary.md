---
title: Glossary
layout: default
---

# Glossary

**Agent.** A program that uses a model to plan, call tools and act.

**Dark factory.** A plant that runs with no people on the floor. In software, a pipeline that turns a specification into tested code with little human involvement.

**Holdout set.** Tests or scenarios the building agent cannot see. They judge the result from outside. ([Order 005](blog/2026-06-15-the-holdout-set-how-to-trust-code-no-human-reviews.html))

**Oracle.** The check that says whether work is correct. In this template, the test suite named in `FACTORY.md`.

**Production order.** A GitHub issue whose body is the spec. One order runs to one pushed commit.

**Converge.** Run the oracle until it is green. The iteration count goes in `METRICS.md`.

**Autonomy contract.** The three written lists: what the agent decides, decides and flags, and stops and asks.

**Skill.** A rule file or tool bundle an agent loads. It is part of the agent's toolbox and a supply-chain risk. ([Order 011](blog/2026-07-13-every-skill-you-do-not-install.html))

**Spec-driven development.** A method where a written specification is the central artifact and code is the output. GitHub Spec Kit is one toolkit. ([Order 002](blog/2026-05-26-ninety-percent-of-ai-native-developers-are-stuck-at-level-2.html))

**Prompt injection.** Attacker text that an agent reads as an instruction.

**Control plane.** The part of a system that enforces policy. The history shows it moving out of the agent. ([Order 043](blog/2026-10-01-the-agent-does-not-hold-the-keys.html))
