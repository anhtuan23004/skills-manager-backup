---
name: aitc-final-qa
description: Use before freeze to check the submission against requirements, the real files, and fresh evidence; does not replace checking by eye/ear.
metadata:
  version: "2.0"
  language: "en"
  status: "prepared-not-btc-approved"
---
# 11 — Final check

Apply the [shared rules](../../docs/TEAM_RULES.md) (written in Vietnamese); re-read them only if they are not already in context or the rules changed.

## Inputs
The specific final version; requirements; metadata; claim/source ledger; prompts; repo status; submission instructions.

## Process
1. Select the exact version and file path to be submitted; do not test one version and submit another.
2. For media/text: open the image/text, play the video/audio from start to end; check the text, content, and sound. For an app: run the user flow and the error cases per the requirements. For a web/game/app that the judges open via a link: run it on the **live link** from a different machine/browser, not only locally, and record URL + time + commit/hash (per the [deploy-checklist](../../templates/deploy-checklist.md)).
3. If there are media files, measure size, duration, codec, and file size against the brief. For app/RAG, check real test runs and source evidence; do not use a successful compile in place of a functional check.
4. Each requirement gets PASS/FAIL/UNVERIFIED and evidence. Re-check the corrections made after the critique round.
5. Run context-review for sensitive claims or images; review sources/usage rights of materials and do not fake certifications.
6. Check the final file, prompt/source, the correct BTC (the organizers) repo, and that no secret goes into the package. Do not edit BTC logs to "clean them up".
7. Large-media repo: do not push files larger than the training limit on your own; keep source/prompts in the repo and the submission file via the designated channel. Do not turn a private repo public on your own when the instructions conflict.
8. The leader approves. Create a hash manifest of the final. A hash helps verify the version; it does not replace an authoritative timestamp or a content assessment.

## Tools and per-task verification

Read the execution-plan together with the requirements to choose checks per deliverable. For an app: run the input → output flow and the error cases per the [app workflow](../aitc-production-planner/references/app-workflow.md); for RAG: check sources and out-of-document questions per the [RAG workflow](../aitc-production-planner/references/rag-workflow.md). For media: check with FFprobe/FFmpeg and view/listen to the real file per [SKILL_EXECUTION](../../docs/SKILL_EXECUTION.md). Do not require every kind of check for every task; mark UNVERIFIED for a framework, browser, or live API that was not run.

## Required outputs
final-qa.md; manifest.json; unresolved items; the real name of the checker and the real time.

## Pre-return checks
Do not say PASS without evidence. Do not equate a successful ffprobe with meeting the brief. Do not submit or change sharing permissions yourself.

## Stop and hand off to a human
Missing decision data, missing permission, or a conflict with the rules: state it clearly and do not fill the gap yourself.
The team leader decides; continue only within the approved scope.
