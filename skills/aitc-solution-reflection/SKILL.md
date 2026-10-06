---
name: aitc-solution-reflection
description: Use when the final version is nearly stable before T+120 to write an honest summary of how the brief was solved, why each choice was made, and what the output means, in preparation for the post-contest video.
metadata:
  version: "1.0"
  language: "en"
  status: "prepared-not-btc-approved"
---
# 12 — Reflection and meaning

Apply the [shared rules](../../docs/TEAM_RULES.md) (written in Vietnamese); re-read them only if they are not already in context or the rules have changed.

## Inputs
The brief; the final version or the version in use; decision log; prompts/sources; critic results; direct confirmation from team members if rationale is missing.

## Process
1. Build an evidence map: Requirement → Decision → Artifact evidence → Intended meaning. Do not request or reconstruct the model's hidden reasoning.
2. Classify every sentence: FACT (observed source), TEAM RATIONALE (recorded or confirmed decision), INTENDED IMPACT, LIMITATION, UNKNOWN.
3. Write the brief commentary: the core requirement, the real difficulties, and the points that forced the team to choose; cite evidence instead of flattering BTC (the organizers).
4. Pick at most 3 key decisions; state the choice, the practical reason, the alternatives considered (if any), and the evidence in the output. If the rationale is missing, ask the team; do not invent it.
5. State the roles of AI and humans, not just a list of models. Do not claim to have trained a model when only an API was called.
6. State the meaning only to the extent it can be proven: whom it aims to help understand or do what; which parts already show this; which effects have not been measured. Do not say "earns extra points" or claim to know what the judges think.
7. Write a one-sentence takeaway, a 45-second version, and a 3–6 minute outline: brief commentary → understanding → choices → AI/humans → output/meaning → limitations/lessons. Split the speaking parts among members according to real contributions.
8. The team reads and confirms. If the final changes, update the affected sections before freeze; record the hash/version used as the basis.
9. After T+120, use the existing version for recording; by default, conservatively make no further AI calls unless BTC has confirmed otherwise. Do not edit the final artifact after the deadline because of the video work.

## Required outputs
solution-reflection.md containing: evidence table, takeaway, 45-second script, 3–6 minute talking points, role assignments, statements not allowed to be made, approver.

## Pre-return checks
Do not rename the skill to disguise its purpose; the log may be inspected publicly. Do not turn "ran out of time" into an artistic strategy. Do not add meaning that exists only in the pitch and not in the artifact.

## Stop and hand off to a human
Missing decisive facts, missing permission, or a conflict with the rules: state it clearly and do not fill the gap yourself.
The team leader decides; continue only within the approved scope.
