---
name: aitc-audio-producer
description: Use when a submission has voice-over or audio, to prepare narration, Vietnamese pronunciation, TTS/STT and audio checks.
metadata:
  version: "2.0"
  language: "en"
  status: "prepared-not-btc-approved"
---
# 08 — Audio production

Apply the [shared rules](../../docs/TEAM_RULES.md) (written in Vietnamese); re-read them only if they are not already in context or the rules have changed.

## Inputs
TTS: approved script, a voice supported by the Gateway, and the duration from the brief. STT: an audio file that is permitted for use and the transcript requirements. Both: proper nouns/numbers/abbreviations that need checking.

## Process
Choose the branch by task: TTS uses steps 1–5; STT focuses on step 6; apply the relevant QA in steps 7–8. Do not require a script/voice for transcription.

1. Separate the final narration from directions. Build a pronunciation sheet for proper nouns, numbers, place names and abbreviations.
2. Use the voice granted through the Gateway; do not imitate a real person/organization or claim an endorsement without a source.
3. Generate a short test segment and actually listen to it. Choose the voice for clarity and fit with the message, not just for sounding "formal" ("trang trọng").
4. Run TTS through the tested endpoint; do not assume the output file is MP3 just because it has an .mp3 extension; check the content type and ffprobe.
5. Measure the duration after generation. Adjust sentences/pacing before speeding up excessively.
6. STT can help review the wording, but compare a human listen against the transcript and the script; do not treat STT as verification.
7. Do not add a music-generation service on your own. Music/material may be used only if BTC (the organizers) provided/allowed it and usage rights exist. With no valid source, do not use it.
8. Check loudness, clipping, silent gaps, music-voice balance and sync. Do not claim compliance with a specific broadcast standard when BTC has not required it or it has not been measured.

## Tools and per-task verification

Read only the [TTS guide](../../docs/api-guides/05-text-to-speech.md) when generating a voice, or the [STT guide](../../docs/api-guides/06-speech-to-text.md) when transcribing. Call the API directly per the [execution guide](../../docs/SKILL_EXECUTION.md). Record the output path, duration and listening check points in the task. An STT-only task does not need a TTS script/voice.

## Required outputs
narration.txt; pronunciation.csv; voice takes; transcript if needed; audio-QA.md with listening timestamps.

## Pre-return checks
Do not treat passing audio metadata as passing audible content. Do not use auto-captions/AI voice built into tools outside the Gateway. Do not add commentary beyond the message in the brief.

## Stop and hand off to a human
Missing decisive information, missing permission, or a conflict with the rules: state it clearly and do not fill the gap yourself.
The team leader decides; continue only within the approved scope.
