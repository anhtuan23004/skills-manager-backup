---
name: aitc-submission-controller
description: Use after final QA and before/after the human's submit action to package the submission, reconcile it against the manifest, and guide the submitter to meet the deadline.
metadata:
  version: "1.0"
  language: "en"
  status: "prepared-not-btc-approved"
---
# 13 — Freeze and submit

Apply the [shared rules](../../docs/TEAM_RULES.md) (written in Vietnamese); re-read them only if they are not already in context or the rules have changed.

## Inputs
The version approved by the leader; the manifest; the source repo from BTC (the organizers); the submission instructions; the deadline as shown on the system.

## Process
1. Distinguish the main deliverable, source/prompts, the reflection video, and the proctoring recording video. Do not lump everything into one file by default.
1b. If the deliverable is a live online link: reconcile the URL, time, and commit/hash in the [deploy-checklist](../../templates/deploy-checklist.md) against the QA version; the link must open from another machine and must not be redeployed after freeze (see [deploy-publisher](../aitc-deploy-publisher/SKILL.md)).
2. Compare the submission's name/version/hash with the QA version. Training limits: 500 MB total attachments, at most 20 files; still read the actual brief/portal if there are updates.
3. A human checks the repo/source/prompts and logs per BTC. Do not overwrite hooks or change repo visibility on your own to match a slide.
4. From T+120, only perform the submit action. Do not call generation, edit the video, rewrite content, or export a version with different content.
5. The submitter performs the submission through the system; the agent only supports the checklist. Demand evidence of a successful submission: status, time, correct title/file. Do not conclude "submitted" from a zip command.
6. Keep the original recording as required; the reflection video is a separate version. Supplement via the Google Form within 24 hours; reflection length per the instructions is 3–6 minutes.
7. Video links must have access/download permission as BTC requires. Enabling that permission is an action a human confirms; do not widen permissions by default.
8. After submission, do not edit the source/final outside the BTC process; if a correction is needed, contact BTC.

## Required outputs
submission-checklist.md; receipt.md (fill in only when a receipt actually exists); the list of verified files/links.

## Pre-return checks
Do not submit, send email, change link permissions, or make a repo public on your own. Do not treat a hashed ZIP as having passed the submission gate. Do not skip the proctoring video.

## Stop and hand off to a human
Missing decisive facts, missing permission, or a conflict with the rules: state it clearly and do not fill the gap yourself.
The team leader decides; continue only within the approved scope.
