---
name: aitc-topic-podcast-audio
description: Use when the brief is a podcast or audio-video dialogue with two characters and background music (for example psychological counseling for older adults) and the deliverable is a podcast assembled from many short segments; playbook of experience from observation.
metadata:
  version: "0.1"
  language: "en"
  status: "draft-from-vtv-observation"
---
# Topic — Podcast / conversational audio

Main part: [Video & Audio](../SKILL.md).

Applies the [general rules](../../../docs/TEAM_RULES.md) (written in Vietnamese). Source: Issue 9 of the VTV show (observed from the broadcast, **not BTC (the organizers) rules or a rubric**). Details: [episode-notes](references/episode-notes.md). Use together with [audio-producer](../../../skills/aitc-audio-producer/SKILL.md).

## Sample brief and deliverable
A psychological counseling podcast for older adults: a dialogue between an older person and an expert (loneliness, health, the generation gap, the digital age); voices must not sound robotic, "warm, deep, and emotionally rich"; two characters with opposite personalities; with background music. Output is 2–4 minutes, audio or video. No deployment needed.

## Suggested process
1. Write the script using real data/stories as context; settle on a simple concept and build it early.
2. Fix the voice prompt (tone, age, regional accent, manner of speaking) for each character; check the voice of every segment.
3. Each audio/video segment is ~8 seconds → optimize block by block so the voice stays consistent when stitching dozens of segments.
4. Add natural vocal gestures ("dạ", "vâng" (polite Vietnamese "yes"), laughter).
5. Background music **only via the API/tools provided by BTC**; if that cannot be confirmed, make a no-music version if the brief allows it, or ask BTC ([evals E15](../../../evals/cases.json)).

## Techniques worth using
- Genuine emotion and empathy for older adults; characters with depth (for example a veteran with a touch of sadness).
- One consistent voice per character; do not mix Northern and Southern accents between blocks.
- Add video as well if time remains (the winning team made both audio and video).

## Pitfalls observed
- A voice that does not match the description (a deep male voice aged 70 coming out young); voices mixing Northern/Southern accents between blocks.
- The word "cô đơn" (lonely) displayed wrongly; the 8-second video transitions are not smooth and the character changes.
- The final audio broke; a backup plan is needed.
- Missing background music (not finished in time, or because only BTC tools were allowed).
- Losing the first 30–60 minutes with no results.

## What judges look at
A near-real, expressive voice; a plot that is psychologically accurate; meeting the brief's requirements (2 characters, background music); effective prompts; thinking from brief to product; consistent voices.

## Topic-specific checks before QA
Listen to everything from start to finish; each character's voice is consistent; Vietnamese text on screen is correct; background music comes from the right source; duration matches the brief.

## Baseline quick win (API-based)

Full context: [BASELINE_PROCESSES](../../../docs/BASELINE_PROCESSES.md) (written in Vietnamese). Timeboxes assume a ~2 hour session (unconfirmed); verify models with `GET /v1/models` first.

- **Quick win:** a two-voice audio dialogue without background music, ready by minute ~40.
- **Pipeline:**
  1. Dialogue script with contrasting characters and natural gestures ("dạ", laughter); normalize names and numbers (`templates/pronunciation.csv`).
  2. `audio/speech` one turn at a time with two fixed voices of the right model family; test one line per voice first ([TTS guide](../../../docs/api-guides/05-text-to-speech.md)).
  3. `ffmpeg` joins the turns; normalize loudness, check silences.
  4. Extra: a still-image video with subtitles.
- **Cost/guard:** no music endpoint exists in the Gateway docs; ask BTC about music before the session ([evals E15](../../../evals/cases.json)).
- **Fallback:** deliver the no-music version if the brief allows it, and say so.
- **QA gate:** listen end to end, voices keep their age and accent, duration 2-4 min.

## Team notes (update yourself)
-
