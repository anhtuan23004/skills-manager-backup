---
name: aitc-topic-<slug>
description: Use when the brief is <deliverable + audience + hard requirement>.
metadata:
  version: "0.1"
  language: "en"
  status: "draft-from-template"   # draft-from-template | tested-in-rehearsal
---
<!-- Copy this folder to topics/<slug>/ (same depth keeps links valid). Replace every <placeholder>, delete comments. Keep section 4: tick or write "N/A because ...". -->
# Topic: <name>

Rules: [TEAM_RULES](../../docs/TEAM_RULES.md), [LESSONS](../LESSONS.md).

## 1. Deliverable contract (fill from the brief; "UNKNOWN - ask BTC" if missing)

| Item | Value |
|---|---|
| Deliverable and format | |
| Size / duration / pages | |
| Audience | |
| Public link needed? | yes / no |
| Data or sources given | |
| Music/slide source allowed | |
| Submission method | |

## 2. Baseline quick win

- **Quick win (T+<25-45>):** <simplest artifact meeting every mandatory requirement>
- **Pipeline:**
  1. <text/structure> `chat/completions` ([guide](../../docs/api-guides/02-text-generation.md))
  2. <assets> image / video / TTS ([image](../../docs/api-guides/03-image-generation.md), [video](../../docs/api-guides/04-video-generation.md), [TTS](../../docs/api-guides/05-text-to-speech.md))
  3. <assemble locally: HTML / ffmpeg / deck>
  4. <deploy or export>
- **Cost and guard:** <estimate x3; test call first>
- **Fallback:** <version that still meets mandatory requirements>

## 3. Timebox (assumes 2 h, unconfirmed)

| Time | Milestone | Owner |
|---|---|---|
| T+0-10 | requirements, resource check, smoke test, concept | |
| T+10-<45> | quick win saved in `final/` | |
| T+<45>-<70> | improve; at most one extra layer | |
| T+70 | freeze | |
| last 30 min | final QA, submit, backup | |

## 4. Checklist ([LESSONS](../LESSONS.md))

- [ ] L1 deploy skeleton live, deploy owner named
- [ ] L2 Vietnamese text inserted by code, checked at real size
- [ ] L3 reference image and fixed voice per character
- [ ] L4 every claim sourced, right year
- [ ] L5 first runnable version on time
- [ ] L6 owners assigned
- [ ] L7 media via BTC API; music/slide source confirmed
- [ ] L8 key in env, no blind POST retry, budget checked
- [ ] L9 minimum done before the extra layer
- [ ] L10 one-sentence message, usable product
- [ ] L11 AI content labeled, no real personal data
- [ ] L12 rehearsed on exam machine, backups made
- [ ] L13 prompts and intermediates saved
- [ ] L14 whole final file opened/heard/watched

## 5. Topic pitfalls

- <failure observed or expected>

## 6. Checks before QA

- [ ] <check on the real file>
- [ ] Every mandatory requirement is PASS with evidence.

## 7. Questions for BTC

- <question> (answers in `templates/btc-questions.md`)

## Team notes
- <date>: <rehearsal result: real time per step, cost, what broke, change>
