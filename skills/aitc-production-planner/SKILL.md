---
name: aitc-production-planner
description: Use when a brief must be turned into executable tasks tied to a skill, helper/API, output, and check; plans media production or builds an app/RAG when the brief requires it.
metadata:
  version: "2.0"
  language: "en"
  status: "prepared-not-btc-approved"
---
# 04 — Production plan

Apply the [shared rules](../../docs/TEAM_RULES.md) (written in Vietnamese); re-read them only if they are not in context or the rules have changed.

## Inputs
Approved concept and brief; deadline; current budget; model configurations already test-called; capacity of the two machines.

## Process
1. Define the final artifact and requirements first; work backwards to the mandatory ingredients. Read [routing](../aitc-orchestrator/references/routing.md) to choose skills. Full multimodal or an app is not mandatory.
2. Assign asset IDs A001... or shot IDs S01...; for each asset record the requirement, machine owner, time needed, status, and file path.
3. For video: a shotlist with duration, visuals, action, audio, text overlay, input reference, and pass condition; total duration must match the brief. Test one hard scene before generating the whole sequence.
4. For images: composition, viewpoint, text areas, and a version plan; important text may be placed with ordinary editing tools when the rules allow.
5. For text: an outline and word count/format per the brief; for audio: script, reading pace, pronunciation, and measured duration.
6. Machine A handles concept/prompt/visual generation. Machine B handles audio/assembly/export/QA. One person acts as team leader/decision recorder; do not add machines.
7. Lock the filename convention `<ID>_<máy>_v<NN>.ext` (for example `S02_A_v03.mp4`, `A001_B_v01.png`); one owner per file being edited; never write to the same JSONL concurrently. Exchange large assets through channels BTC (the organizers) allows; do not set up an external shared cloud.
8. Set a cost ceiling per task and a shared reserve. The team budget comes from BTC; do not mistakenly add two API keys together as two budgets.
9. Follow the [120-minute table](../../GUIDE.md#5-quy-trình-120-phút-trên-2-máy): a full draft by T+65; final assets chosen by T+90. A fallback option must not violate the brief's format/content.

## Linking the plan to execution

- Use [execution-plan](../../templates/execution-plan.md) as the main table: each task has a skill/reference, helper/operation + guide, input, output path, check/command, and pass criteria. Read [SKILL_EXECUTION](../../docs/SKILL_EXECUTION.md) to reuse the Gateway/media helpers instead of writing new wrappers.
- For a requested app/API/UI, read [app workflow](references/app-workflow.md). For document Q&A, read [RAG workflow](references/rag-workflow.md). Do not read both if the task needs only one.
- Build one small, verifiable flow or sample first, then expand in dependency order. When assigned to execute, continue to the next task once the plan is clear enough; keep decisions already confirmed and do not ask again for the same permission.
- For generation tasks, state dry-run/live and the cost ceiling. For local editing tasks, state that no API is needed. After a check, update evidence and status instead of re-planning.

## Required outputs
execution-plan.md (or an equivalent table in the brief): task, skill, tool, file, check, dependency, owner, and timebox. Add [production-plan.csv](../../templates/production-plan.csv) when there are many assets and [storyboard.md](../../templates/storyboard.md) when a scene sequence is needed; do not create a storyboard for text-only or app-only work. Record the critical path and fallback.

## Pre-return checks
Do not use long or expensive generated video before testing the scene. Do not spend the whole time on the outline. Do not create music with an external AI service; if a music-generation API is not confirmed by the docs, treat it as unavailable.

## Stop and hand off to a human
Missing decisive facts, missing permission, or a rules conflict: state it clearly and do not fill the gap yourself.
The team leader decides; continue only within the approved scope.
