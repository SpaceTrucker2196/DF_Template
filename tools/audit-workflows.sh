#!/usr/bin/env bash
# Audit this factory's GitHub Actions workflows against the three lab
# findings of August 2026, in which researchers took the DEFAULT agent
# workflows published by Anthropic, Google and OpenAI and reached remote
# code execution in all three from one unauthenticated GitHub issue.
#
# Zero dependencies on purpose: grep and awk, no yq, no pip. A check
# that needs installing is a check that stops being run.
#
# Exit 0 = clean. Exit 1 = at least one finding. Run it from `make audit`
# and before adding any workflow.
#
# WHAT THIS CANNOT CHECK, stated here rather than implied by silence:
# whether two passes of one workflow share a writable checkout at
# RUNTIME. That is the Codex finding — pass one wrote a poisoned
# AGENTS.md, pass two loaded it as authoritative instructions — and it
# depends on what the agent does, not on what the YAML says. Read any
# multi-pass workflow by hand.

set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

DIR=.github/workflows
FINDINGS=0

say()  { printf '%s\n' "$*"; }
fail() { printf '  FINDING  %s\n' "$*"; FINDINGS=$((FINDINGS + 1)); }
pass() { printf '  ok       %s\n' "$*"; }

# Triggers that carry attacker-controlled content into the run. An
# unauthenticated stranger can put text into every one of them.
CONTENT_TRIGGERS='issues|issue_comment|pull_request_target|workflow_run|discussion|discussion_comment|fork|watch'

# Instruction files: whatever the agent loads as authoritative.
INSTRUCTION_FILES='AGENTS\.md|CLAUDE\.md|\.claude/'

if [ ! -d "$DIR" ]; then
  say "No $DIR — nothing to audit."
  exit 0
fi

shopt -s nullglob
FILES=("$DIR"/*.yml "$DIR"/*.yaml)
if [ ${#FILES[@]} -eq 0 ]; then
  say "No workflows in $DIR — nothing to audit."
  exit 0
fi

for wf in "${FILES[@]}"; do
  say "$wf"

  # The `on:` block: from the `on:` line to the next top-level key.
  triggers=$(awk '/^on:/{f=1;next} f && /^[a-zA-Z_-]+:/{f=0} f' "$wf")
  # `on: [issues, push]` inline form too.
  inline=$(grep -E '^on:' "$wf")
  both="$triggers $inline"

  # The `permissions:` block, same shape.
  perms=$(awk '/^permissions:/{f=1;next} f && /^[a-zA-Z_-]+:/{f=0} f' "$wf")

  # ---- 1. A write-scoped token on a content trigger ------------------
  # The Google ADK finding: content planted in a pull request reached a
  # low-privilege triage agent, which posted a comment, which triggered
  # a maintainer-gated workflow, which inherited a token with issue and
  # pull-request write scope. A maintainer gate is worth nothing if a
  # lower-privilege agent can trigger it.
  if printf '%s' "$both" | grep -qE "^[[:space:]]*($CONTENT_TRIGGERS):|($CONTENT_TRIGGERS)[],]"; then
    if [ -z "$perms" ]; then
      fail "content trigger and NO permissions: block — the run inherits the repository default, which may be write"
    elif printf '%s' "$perms" | grep -qE ':[[:space:]]*write'; then
      fail "content trigger AND a write-scoped token: $(printf '%s' "$perms" | grep -E ':[[:space:]]*write' | tr -d ' ' | paste -sd, -)"
    else
      pass "content trigger, read-only token"
    fi
  else
    pass "no attacker-controlled trigger"
  fi

  # ---- 2. pull_request_target at all ---------------------------------
  # It runs with the BASE repository's secrets against the PR's code.
  # There is no safe default use of it in a factory that runs an agent.
  if printf '%s' "$both" | grep -q 'pull_request_target'; then
    fail "uses pull_request_target — base-repo secrets against fork code"
  else
    pass "no pull_request_target"
  fi

  # ---- 3. A workflow that writes an instruction file ------------------
  # The Codex finding's static half. An instruction file written by a
  # workflow is an instruction file an attacker may reach.
  if grep -nE "$INSTRUCTION_FILES" "$wf" | grep -qiE '>|>>|tee|sed -i|write|commit|checkout'; then
    fail "touches an instruction file ($(grep -noE "$INSTRUCTION_FILES" "$wf" | paste -sd, -))"
  else
    pass "writes no instruction file"
  fi
done

say ""
if [ "$FINDINGS" -eq 0 ]; then
  say "audit-workflows: clean (${#FILES[@]} workflow(s))."
  say "Not checked: runtime sharing of a writable checkout between two"
  say "agent passes. Read any multi-pass workflow by hand."
  exit 0
fi
say "audit-workflows: $FINDINGS finding(s). See SECURITY.md."
exit 1
