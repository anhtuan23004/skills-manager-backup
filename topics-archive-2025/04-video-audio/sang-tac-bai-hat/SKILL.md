---
name: aitc-topic-sang-tac-bai-hat
description: Use when the brief is to compose a song promoting an organization or set of values and produce a lyric video, and the deliverable is a song plus a lyrics video; playbook of experience from observation.
metadata:
  version: "0.1"
  language: "en"
  status: "draft-from-vtv-observation"
---
# Topic — Songwriting + lyric video

Main part: [Video & Audio](../SKILL.md).

Applies the [general rules](../../../docs/TEAM_RULES.md) (written in Vietnamese). Source: Issue 10 of the VTV show (observed from the broadcast, **not BTC (the organizers) rules or a rubric**). Details: [episode-notes](references/episode-notes.md). Use together with [audio-producer](../../../skills/aitc-audio-producer/SKILL.md) and [video-director](../../../skills/aitc-video-director/SKILL.md).

## Sample brief and deliverable
A completely new song promoting the meaning and value of the "Hiệp hội dữ liệu quốc gia" (National Data Association), as a **lyric video** (~3 minutes); the lyrics must contain the association's name; use AI tools provided by BTC (the music account is issued by BTC, no personal accounts); must not violate public morality and decency. No deployment needed.

## Suggested process
1. Spend the first 30 minutes researching the organization from **authoritative sources** and settling the message; do not let AI invent data.
2. Run in parallel: lyrics / music / lyric video (split among 3 people); try 3–5 music styles, then pick the best fit.
3. Lyrics with end-of-line rhymes, easy to sing; difficult words can go into a rap section.
4. AI video is only ~8 seconds per clip → split into about 8 scenes/prompts and stitch; overlay the lyrics on the video and check that they display correctly.
5. Check every sung line: Vietnamese tone marks and stress.

## Techniques worth using
- Prompt in an A→B→C order; derive the lyrics-generation prompt from the image-generation prompt.
- A complete product (lyrics, music, MV, a tool for viewers to sing along); a message that can spread and be used at events.
- Modern, young music with a memorable chorus that still carries a promotional tone.

## Pitfalls observed
- **"Cưỡng từ"** (forced/mispronounced Vietnamese words in singing, with wrong tone marks or stress) is a cardinal sin; one song had unintelligible lyrics.
- An API key with one extra dot cost ~15 minutes; many plans did not fit within 2 hours.
- A video that was cut short or ended abruptly; the second half of the video did not display the lyrics correctly; only 5 of 10 songs could be submitted with 15 minutes left.
- Generic slogan-style lyrics; too little research on the association.

## What judges look at
Lyrics that fit the message and mission, using real data; few Vietnamese errors; rhyme; music that is easy to sing and easy to spread; product thinking; singing voice.

## Topic-specific checks before QA
Listen to the whole song and compare the sung lyrics with the displayed lyrics; the association's name appears in the lyrics; duration/visuals match the brief; data sources about the association.

## Baseline quick win (API-based)

Full context: [BASELINE_PROCESSES](../../../docs/BASELINE_PROCESSES.md) (written in Vietnamese). Timeboxes assume a ~2 hour session (unconfirmed); verify models with `GET /v1/models` first.

- **Quick win:** a lyric video with background image, scrolling lyrics and a TTS reading of the lyrics (minute ~45).
- **Pipeline:**
  1. Lyrics from the official source of the named organization.
  2. `chat/completions` writes and refines the lyrics for rhyme and diacritics.
  3. Ask BTC about a permitted music source; without one, a rhythmic TTS reading must not be presented as singing.
  4. Background from Nano Banana; `ffmpeg` builds the lyric video with timestamp sync ([image guide](../../../docs/api-guides/03-image-generation.md)).
- **Cost/guard:** no music-generation endpoint is documented; check every sung or spoken line for mispronunciation ("cưỡng từ" is the worst failure).
- **Fallback:** a lyric video with voice reading, stating the tool limit.
- **QA gate:** lyrics match the source, audio and lyrics in sync, watch the whole video.

## Team notes (update yourself)
-
