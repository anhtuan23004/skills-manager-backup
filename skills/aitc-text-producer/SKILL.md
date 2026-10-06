---
name: aitc-text-producer
description: Use when writing Vietnamese scripts, content, or output text from an approved brief; covers text pieces, narration, subtitles, or wording inside images/video.
metadata:
  version: "2.0"
  language: "en"
  status: "prepared-not-btc-approved"
---
# 05 — Text production

Apply the [shared rules](../../docs/TEAM_RULES.md) (written in Vietnamese); re-read them only if they are not in context or the rules have changed.

## Inputs
Brief; concept; outline; sourced data; required length/tone/format.

## Process
1. Settle the function of the text: explain, tell a story, instruct, call to action, or standalone content. Do not add goals beyond the brief.
2. Build a short outline per requirement; write the draft from verified sources.
3. Distinguish factual sentences from creative ones. Attach a claim ID to facts; never invent quotations, hotlines, agencies, legal provisions, or surveys.
4. For narration, write to be spoken; sentences with rhythm, correct punctuation and correct Vietnamese diacritics, with no technical notes inserted into the text to be read. For subtitles, keep the meaning and check sync after export.
5. For infographics/posters, shorten while keeping the meaning; do not use aesthetics as a reason to drop mandatory warnings.
6. Read aloud/count words/measure duration; do not convert word count into a definite duration. Record the measurement method and version.
7. A critic checks against the brief; fix at most 3 high-impact points. Export UTF-8 and a final version with no internal notes mixed in.

## Tools and per-task verification

Read the [Text guide](../../docs/api-guides/02-text-generation.md) when calling text/responses and the [execution guide](../../docs/SKILL_EXECUTION.md). If the current agent already runs through the BTC Gateway (BTC = the organizers) and can draft directly, no extra side call through an external script is needed.

Content that needs fresh information: read [Grounding](../../docs/api-guides/07-web-grounding.md) and enable search only within the allowed scope. Document Q&A: follow the [RAG workflow](../aitc-production-planner/references/rag-workflow.md); answer from sourced context and state missing evidence when data is insufficient.

## Required outputs
text-vNN.md or narration.txt; claim ledger; clearly mark the final content and the notes that must not go into the deliverable.

## Pre-return checks
Do not exaggerate benefits. Do not describe the product as if it were really deployed. Do not default to an administrative register just because the contest is sponsored.

## Stop and hand off to a human
Missing decisive facts, missing permission, or a rules conflict: state it clearly and do not fill the gap yourself.
The team leader decides; continue only within the approved scope.
