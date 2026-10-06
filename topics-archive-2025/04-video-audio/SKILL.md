---
name: aitc-group-video-audio
description: Use when the deliverable is video/audio (news bulletin, podcast, song + lyric video) assembled from several short video/audio segments; common principles for this group.
metadata:
  version: "0.1"
  language: "en"
  status: "draft-from-vtv-observation"
---
# Part 4 — Video & Audio

Apply the [common rules](../../docs/TEAM_RULES.md) (written in Vietnamese). Source: Issues 7, 9, 10 of the VTV show (observation of the TV broadcast, **not BTC (the organizers) rules or rubric**). Summary: [INSIGHTS](../../docs/INSIGHTS_VTV_2025.md) (written in Vietnamese).

## Topics in this part
| Topic | Open file | Briefs seen |
|---|---|---|
| News bulletin video with a virtual anchor | [ban-tin-video](ban-tin-video/SKILL.md) | Issue 7 |
| Podcast / conversational audio | [podcast-audio](podcast-audio/SKILL.md) | Issue 9 |
| Songwriting + lyric video | [sang-tac-bai-hat](sang-tac-bai-hat/SKILL.md) | Issue 10 |

Pair with [video-director](../../skills/aitc-video-director/SKILL.md), [audio-producer](../../skills/aitc-audio-producer/SKILL.md), [text-producer](../../skills/aitc-text-producer/SKILL.md). No deploy needed; submit the file.

## Common principles of this part
1. **AI clips are only ~8 seconds** → plan scenes/blocks with timestamps, one lead image/prompt per scene, then assemble; check the transitions.
2. **One character = one lead image + one fixed voice** (voice prompt: age, regional accent, tone). Mixed Northern/Southern voices, or a character changing between blocks, are recurring failures.
3. Write the script/lyrics from **real sources**; do not let AI invent data; news must be traceable to a source.
4. Audio/music **only through the API/account provided by BTC (the organizers)**; if not yet confirmed, make a no-music version or ask BTC ([eval E15](../../evals/cases.json)).
5. Fix a simple concept and start early so there is time to revise; split in parallel: lyrics / music-voice / video-assembly.
6. Check Vietnamese in both the on-screen text and the spoken/sung voice (diacritics, stress, forced/mispronounced words (Vietnamese "cưỡng từ")).
7. Watch/listen to the whole assembled cut from start to finish.
8. AI transparency: do not interview an AI-generated character as if it were a real person.

## Common failures of this part
Inconsistent voice; on-screen text with wrong diacritics; forced/mispronounced words (Vietnamese "cưỡng từ"); transitions not smooth/video cut off; missing background music; an API key wrong by one character costing ~15 minutes; unstable network; losing the first 30–60 minutes with no result; a plan that does not fit within 2 hours.

## What judges look at (common)
Lifelike and expressive; message/emotion fitting the audience; consistent voice/character; lyrics/script true to the mission with real data; meeting all brief requirements (characters, background music, lyrics); product thinking; authenticity.

## Common checks before QA
Listen/watch the whole final cut; compare spoken/sung words with the on-screen text; duration as the brief requires; consistent voice; source for every claim; music/audio source compliant with the rules.

## Baseline quick win (API-based)

Baseline for this part: build a **stills + TTS + subtitles** version first, then upgrade scenes to Veo (4/6/8 s, test one 4 s scene). The Gateway docs list **no music-generation endpoint**; settle music with BTC before the session. See [BASELINE_PROCESSES](../../docs/BASELINE_PROCESSES.md).

## Team notes (update yourself)
-
