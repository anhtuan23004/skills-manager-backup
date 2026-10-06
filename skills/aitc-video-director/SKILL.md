---
name: aitc-video-director
description: Use when a brief requires video or motion clips, to write shot prompts, generate video through the Gateway, track jobs and keep visual continuity.
metadata:
  version: "2.0"
  language: "en"
  status: "prepared-not-btc-approved"
---
# 07 — Video direction

Apply the [shared rules](../../docs/TEAM_RULES.md) (written in Vietnamese); re-read them only if they are not already in context or the rules have changed.

## Inputs
Approved storyboard; source frames; duration/aspect ratio from the brief; tested model/endpoint; cost ceiling.

## Process
1. Each request focuses on one scene/one action. Pace the narrative in the storyboard; do not cram the whole story into one short clip.
2. Separate character motion, camera motion and environment motion. For image-to-video, prefer describing motion; do not lengthily re-describe what the source frame already shows.
3. Lock character/style details through references and the prompt, but use only parameters the Gateway actually supports; do not guarantee absolute consistency.
4. Test risky scenes with the cheap/short configuration that has been granted. State seconds explicitly; do not rely on defaults.
5. Video workflow: create → save the job ID immediately → poll the same job → download when completed. While processing, do not recreate the job. If a timeout occurs after the POST, the state may be unknown; ask the team leader and check the ledger/BTC (the organizers) before recreating.
6. Video cost is charged at creation per the BTC documentation; do not auto-retry a POST that returned a network error, to avoid creating duplicate tasks.
7. Watch the actual clip at start, middle and end, and watch the transitions in the assembled cut. A contact sheet does not replace watching/listening to the whole video/audio.
8. When time runs out: use the best passing clip; switch to a still image with motion/regular editing only if the brief and the rules allow it; do not describe that as newly generated AI video.
9. Machine B assembles, checks audio/text sync and exports. There is no default requirement to deploy.

## Tools and per-task verification

Read the [Video guide](../../docs/api-guides/04-video-generation.md) and the [execution guide](../../docs/SKILL_EXECUTION.md). Follow this chain: create the video (`POST /videos`) → save the job ID → poll status (`GET /videos/{id}`) → download the video when complete (`GET /videos/{id}/content`). Use FFprobe and FFmpeg to check parameters and extract frames; join clips and audio with editing tools/FFmpeg; verify by actually watching and listening.

## Required outputs
video-jobs.csv; clips; review with timecodes; timeline/assembly instructions; final export per the brief.

## Pre-return checks
Do not assume a job succeeded just from HTTP 200. Do not let a failed/blank clip continue into assembly. Do not use external model APIs even if the Gateway is slow.

## Stop and hand off to a human
Missing decisive information, missing permission, or a conflict with the rules: state it clearly and do not fill the gap yourself.
The team leader decides; continue only within the approved scope.
