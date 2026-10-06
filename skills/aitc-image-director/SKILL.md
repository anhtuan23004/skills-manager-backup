---
name: aitc-image-director
description: Use when a brief calls for visual direction, prompts and image review, such as posters, key visuals, image sets or frames for video.
metadata:
  version: "2.0"
  language: "en"
  status: "prepared-not-btc-approved"
---
# 06 — Image direction

Apply the [shared rules](../../docs/TEAM_RULES.md) (written in Vietnamese); re-read them only if they are not already in context or the rules have changed.

## Inputs
Brief; concept; aspect ratio/size from the brief; approved text list; permitted image/character sources.

## Process
1. Write a visual brief of at most 8 lines: message, subject, setting, composition, color/lighting, empty space, text area, what to avoid.
2. Give each image one focal point. Tie visual choices to the message; do not use flowery wording in place of concrete decisions.
3. A multi-image set needs a consistency sheet: fixed character traits, props, costumes, style, palette, environment. References must be created in the session or permitted by BTC (the organizers).
4. Split the prompt into subject / context / composition / visual language / lighting / constraints. A negative instruction in the prompt does not mean the API supports a negative_prompt field.
5. Use only parameters confirmed by the Gateway; do not add seed, reference arrays or an image-editing endpoint on your own just because the original provider supports them.
6. Generate a small sample first and look at the actual image. Check anatomy, text, cultural details, unintended logos, message, and legibility at final size.
7. Generate controlled revisions; keep the composition that already works. Check important Vietnamese text character by character; use an editorial text layer if allowed.
8. Record the prompt, model, input references, output ID, selected version and the reason. Do not mark an image as correct just because the prompt asked for the right thing.

## Tools and per-task verification

Read the [Image guide](../../docs/api-guides/03-image-generation.md) and the [execution guide](../../docs/SKILL_EXECUTION.md). Call the image-generation endpoint through the BTC Gateway using the provided schema; decode base64 and save the image to the workspace. Open the actual image to check it and record evidence per requirement.

## Required outputs
image-brief.md; prompt-Sxx.md; image vNN; review with error locations; asset manifest.

## Pre-return checks
Do not use the original canvas-design to place creativity above the brief. Do not use AI built into Canva/Photoshop. Do not put font files from reference sources into the toolkit.

## Stop and hand off to a human
Missing decisive information, missing permission, or a conflict with the rules: state it clearly and do not fill the gap yourself.
The team leader decides; continue only within the approved scope.
