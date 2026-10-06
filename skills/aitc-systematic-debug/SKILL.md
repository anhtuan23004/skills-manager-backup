---
name: aitc-systematic-debug
description: Use when diagnosing Gateway, file, export, or sync failures during the contest; for failing requests, clips that will not download, or outputs that will not open.
metadata:
  version: "1.0"
  language: "en"
  status: "prepared-not-btc-approved"
---
# 10 — Incident handling

Apply the [shared rules](../../docs/TEAM_RULES.md) (written in Vietnamese); re-read them only if they are not already in context or the rules changed.

## Inputs
Error message without secrets; operation/model; time of occurrence; job/request ID; last success; minutes remaining.

## Process
1. Record the symptom and the smallest reproduction; do not change many parameters/tools at once.
2. Classify: 401 key; 403 permission/model; 400 schema/endpoint; 429 rate or budget; timeout; processing; file/codec error. Base it on the actual message, not just the HTTP code.
3. 429 rate: wait/back off as instructed. 429 budget: waiting does not increase the budget; stop and reduce cost / report to the team leader.
4. Timeout after a POST that creates media: you do not know whether the task was created; do not retry automatically. Poll the existing job and check the logs/BTC (the organizers).
5. Model/endpoint mismatch: cross-check the BTC docs; do not switch to a third-party API or send the BTC key to a provider.
6. Test one hypothesis at a time; re-test with the same small input; save the result as evidence.
7. If not resolved after at most 5 minutes: report to the team leader and pick an approved fallback that keeps the requirements. Do not wait indefinitely on a single job.
8. Record the incident and the decision; do not delete failed records and do not fabricate logs. If a credential is exposed: stop and contact BTC; do not edit the original logs yourself.

## Required outputs
incident.md: symptom / evidence / hypothesis / test / result / next action / owner.

## Pre-return checks
Do not write "fixed" before re-running. Do not fire requests indefinitely. Do not auto-update dependencies or change frameworks mid-session.

## Stop and hand off to a human
Missing decision data, missing permission, or a conflict with the rules: state it clearly and do not fill the gap yourself.
The team leader decides; continue only within the approved scope.
