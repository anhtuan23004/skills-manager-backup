---
name: aitc-orchestrator
description: Use when receiving a brief to pick skills and orchestrate plan-based execution for text, image, video, audio, or app/RAG when the brief requires it; use at the start of a task or when resuming work in progress.
metadata:
  version: "2.0"
  language: "en"
  status: "prepared-not-btc-approved"
---
# 00 — Exam orchestration

Apply the [shared rules](../../docs/TEAM_RULES.md) (written in Vietnamese); re-read them only if they are not in context or the rules have changed.

## Inputs
Verbatim brief; system time T; rubric if any; Gateway/hook status; members responsible for the two machines; the budget currently shown by BTC (the organizers).

## Process
1. Read [TEAM_RULES](../../docs/TEAM_RULES.md), the brief, and the current work state. If an approved brief/plan already exists, continue the unfinished tasks; do not redo everything.
2. Call brief-decoder; the team leader confirms the required outputs. Meanwhile, Machine B checks connectivity, the repo, hooks, and the file export path. When BTC issues the key, run `python3 scripts/check_resources.py` from the toolkit root per [RESOURCE_CHECK](../../docs/RESOURCE_CHECK.md): model list, key/team budget, rate limit. Add `--smoke` only when a small paid test request is needed; use `deepseek-flash` with thinking off, and do not test models in bulk or auto-retry. If data is missing, record UNVERIFIED; do not assume an unlimited budget.
3. Call concept-choice to pick at most 3 directions, one main direction and one scope-reduction option. Do not run multiple autonomous agents by default.
4. Use vietnam-context-review when there are claims, symbols, Vietnamese context, or content that needs verification. A small task may merge brief/concept/plan in one pass; do not re-ask decisions the user has already confirmed.
5. Read the [skill selection map](references/routing.md), then use production-planner to write the [execution-plan](../../templates/execution-plan.md). Every task must have a requirement, skill, helper/API guide, input, output file, check, dependencies, and timebox. Load only the producer/reference of the task about to be done. Build a UI only when the deliverable needs it. Apply [LESSONS](../../topics/LESSONS.md); if the brief type matches a topic in [topics/INDEX](../../topics/INDEX.md) or the [2025 archive](../../topics-archive-2025/INDEX.md), read exactly that topic together with the task's skill. If the deliverable is a web/game/app that must open via a link, add a deploy task from the first plan and use [deploy-publisher](../aitc-deploy-publisher/SKILL.md): a skeleton version goes live on a real link early, a separate person owns deployment, and the freeze mark includes deploy time.
6. Internal targets per the [120-minute table](../../GUIDE.md#5-quy-trình-120-phút-trên-2-máy): T+18 lock concept; T+30 first sample/pipeline runs; T+65 complete draft; T+90 pick the final version; T+100 candidate version opened/viewed/listened to; T+112 freeze. Adjust the length of each stage to the brief; do not change the BTC deadline.
7. Critic checks every version against the original brief. Limit to 2 major revision rounds; prefer local fixes over regenerating everything.
8. T+100–112: Machine A does the reflection from evidence; Machine B checks/exports the final version. If the final version changes after the reflection, update the affected parts before freeze.
9. Near the deadline: final QA and reflection if the brief requires it, approver, manifest; commit/push/submit only as requested and within the permissions granted. For a confirmed 120+10 minute exam window, T+120–130 is for submission only. Do not auto-submit, make the repo public, or change link permissions.
10. Incidents: if a fix loop exceeds 5 minutes without progress, report to the leader and reduce scope; do not swap the entire toolset.

## Required outputs
In the workspace: brief/requirements and execution-plan.md with executable tasks. After each task, update the status, evidence path, and next step; if FAIL, debug; if not yet checked, mark UNVERIFIED.
Keep existing brief/concept/final confirmations; ask only when a remaining choice would change scope, permissions, or cost beyond the granted limit. Do not stop at the plan if the user has already asked for implementation within that scope.
Give next-step instructions for each machine, no more than 5 lines.

## Pre-return checks
Do not require a third machine. Do not default to building a website; deploy only when the brief states the deliverable needs a live online link, and in that case do not leave deployment to the last minute. Do not call AI before confirming the endpoint. Do not write new product after freeze.

## Stop and hand off to a human
Missing decisive information/missing permission/rule conflict: state it clearly; do not fill the gap yourself.
The team leader decides; continue only within the approved scope.
