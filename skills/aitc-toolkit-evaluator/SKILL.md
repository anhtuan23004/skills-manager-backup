---
name: aitc-toolkit-evaluator
description: Use when preparing or changing the toolkit to test skills, MCP, and the entire two-machine workflow before contest day; do not run costly benchmarks on your own during contest hours.
metadata:
  version: "2.0"
  language: "en"
  status: "prepared-not-btc-approved"
---
# 14 — Pre-contest toolkit evaluation

Apply the [shared rules](../../docs/TEAM_RULES.md) (written in Vietnamese); re-read them only if they are not already in context or the rules have changed.

## Inputs
The current skill set; evals/cases.json; the contest machines; permitted tools/hooks/Gateway for testing; practice budget.

## Process
1. Check SKILL.md metadata and routing: the right task activates the skill; the wrong task does not pull in extra tools.
2. Take test cases with observable outcomes; test clear inputs, missing sources, prompt injection, Vietnamese typos, format conflicts, and running out of time.
3. Run a with-skill vs. without-skill comparison on the same brief through the permitted Gateway, with the same model and limits. Do not record fake performance when nothing has been run.
   For the new skill-first flow, use the [routing and timing practice brief](../../evals/skill-first-rehearsal.md): measure the time to an executable plan, the first passing output, and the number of fixes required. Do not conclude it is faster from unit tests or file counts alone.
4. Humans evaluate real artifacts/decisions; creative quality has no simple test string that fully replaces them.
5. Check the agent's competence: reading the brief, sticking to the rubric, not expanding scope on its own, and clearly separating real facts from guesses.
6. Test the connection to the BTC (the organizers) Gateway through a real agent; check that hooks record the log completely.
7. Run a full rehearsal on exactly two machines, 120 minutes + 10 minutes for submission; do not use a third machine or outside help.
8. Record the results, errors, and lessons learned before contest day.

## Required outputs
evaluation-report.md: case / expected / observed / pass-fail-unverified / evidence / next fix. A readiness checklist for both machines.

## Pre-return checks
Do not call the skill set "well benchmarked" when only the structure has been checked. Do not install new plugins during the contest session. Do not infer that an MCP is safe just because it has many GitHub stars.

## Stop and hand off to a human
Missing decisive facts, missing permission, or a conflict with the rules: state it clearly and do not fill the gap yourself.
The team leader decides; continue only within the approved scope.
