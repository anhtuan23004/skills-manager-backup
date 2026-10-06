---
name: aitc-topic-ban-tin-video
description: Use when the brief is a news bulletin video with a virtual anchor and graphics (for example a bulletin on AI in Vietnam) and the deliverable is a 60–80 second video assembled from multiple short clips; playbook of experience from observation.
metadata:
  version: "0.1"
  language: "en"
  status: "draft-from-vtv-observation"
---
# Topic — News bulletin video with a virtual anchor

Main part: [Video & Audio](../SKILL.md).

Applies the [general rules](../../../docs/TEAM_RULES.md) (written in Vietnamese). Source: Issue 7 of the VTV show (observed from the broadcast, **not BTC (the organizers) rules or a rubric**). Details: [episode-notes](references/episode-notes.md). Use together with [video-director](../../../skills/aitc-video-director/SKILL.md) and [audio-producer](../../../skills/aitc-audio-producer/SKILL.md).

## Sample brief and deliverable
A ~60–80 second news bulletin video on the state of AI development in Vietnam (as of October 2025), with a virtual anchor speaking standard Vietnamese, illustrative images, charts, and suitable graphics. Submit a video file (MP4 is fine); no deployment needed.

## Suggested process
1. Write the script and split it into **scenes/shots with timestamps**; every piece of information needs a source and must be verified before it goes into the narration.
2. Create a consistent main anchor image and a single voice; make one key image per scene/shot first, then generate video from the image.
3. AI clips are only ~8 seconds long → plan to stitch many clips while keeping the anchor, voice, and style consistent.
4. Add infographics/illustrations following the narration; assemble, sync text/audio, export.
5. Watch/listen to the whole assembled cut from start to finish.

## Techniques worth using
- Journalistic quality: detailed, emotional, showing an understanding of how news is made; many news items in a short time.
- An anchor with a distinct identity; a stable voice throughout.
- Use the workshop/materials from before the contest to get started quickly; losing the first ~30 minutes because the workflow is unfamiliar is a risk.

## Pitfalls observed
- Vietnamese errors when adding voice/text; the anchor is inconsistent across clips.
- Authenticity is hard to verify; **interviewing AI-generated characters** was seen as crossing the line (interviews must be real people and real events).
- Network failure (a team had to use two phones broadcasting 4G); some teams did not finish (90 points).

## What judges look at
A bulletin that feels real; an anchor present throughout with a stable voice; rich in information; traceable news sources; solving the problem so the product is smooth and natural; practical, real-world execution.

## Topic-specific checks before QA
Every claim/figure in the news has a source; duration is 60–80 seconds per the brief; watched/listened to the whole thing; no AI character playing a real person being interviewed; label AI-generated content clearly where transparency is needed.

## Baseline quick win (API-based)

Full context: [BASELINE_PROCESSES](../../../docs/BASELINE_PROCESSES.md) (written in Vietnamese). Timeboxes assume a ~2 hour session (unconfirmed); verify models with `GET /v1/models` first.

- **Quick win:** a 60 s bulletin from still images, TTS voice and subtitles, even if AI video is not ready (minute ~45).
- **Pipeline:**
  1. Script with timestamps, each block at most 8 s, news from official sources with dates.
  2. `audio/speech` reads the whole script with one fixed voice; measure with `ffprobe` ([TTS guide](../../../docs/api-guides/05-text-to-speech.md)).
  3. Anchor/scene images from Nano Banana; Veo 4-8 s scenes via image-to-video (`input_reference`) to keep the anchor consistent ([video guide](../../../docs/api-guides/04-video-generation.md)).
  4. `ffmpeg` assembles, subtitles are added by code; watch the whole cut.
- **Cost/guard:** 72 s of Veo lite is about $3.6 per pass, so budget x3; try one 4 s scene first; poll every ~10 s; never retry the POST after a timeout.
- **Fallback:** stills with light motion plus voice-over.
- **QA gate:** 60-80 s as required, anchor and voice consistent, claims traceable; do not interview an AI character as if real.

## Team notes (update yourself)
-
