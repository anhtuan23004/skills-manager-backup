---
name: aitc-brief-decoder
description: Use when a brief is first opened or when BTC (the organizers) add requirements; analyzes the verbatim brief, extracts deliverables and the rubric, and flags anything undetermined.
metadata:
  version: "1.0"
  language: "en"
  status: "prepared-not-btc-approved"
---
# 01 — Brief decoding

Apply the [shared rules](../../docs/TEAM_RULES.md) (written in Vietnamese); re-read them only if they are not already in context or the rules have changed.

## Inputs
The verbatim brief and attached files; the official rubric if available; deadlines and submission format.

## Process
1. Read the entire brief; view images/tables when the parsed text is incomplete. Do not treat examples in training materials as brief requirements.
2. Separate out: output; audience; goal/message; permitted sources/assets; file specs; must-have / must-not-have content; scoring criteria; how to submit.
3. Assign R01... to each requirement. Each item has a short quote or source location, a way to check it, and a status.
4. Mark OFFICIAL for sourced requirements, ASSUMPTION for team inferences, PROPOSED for internal criteria. Do not infer weights from the sponsoring organization.
5. Choose the work type: text, image, video, audio, combined, or interactive if the brief says so. Even the minimal output must keep every mandatory requirement.
6. Raise at most 3 high-impact questions; for non-critical unclear points, settle on a labeled assumption and continue.
7. Write a one-sentence interpretation of the brief and submit it to the team leader for approval.

## Required outputs
brief.md and requirements.csv: id, requirement, source, kind, check, owner, status, evidence.
One sentence: Create [output] for [audience] to [purpose] under [constraints].

## Pre-return checks
Do not confuse the 3–6 minute reflection video with the exam submission video. Do not invent KPIs, personas, data, or export specs. Do not drop a requirement to save time and still record PASS.

## Stop and hand off to a human
Missing decisive information, missing permission, or a conflict with the rules: state it clearly; do not fill the gap yourself.
The team leader decides; continue only within the approved scope.
