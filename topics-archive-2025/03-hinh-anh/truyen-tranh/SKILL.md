---
name: aitc-topic-truyen-tranh
description: Use when the brief asks for an educational/warning comic (e.g. online-scam prevention for students) and the deliverable is a multi-page comic; lessons from observing the VTV show.
metadata:
  version: "0.1"
  language: "en"
  status: "draft-from-vtv-observation"
---
# Topic — Educational / warning comic

Main part: [Images & communication materials](../SKILL.md).

Apply the [general rules](../../../docs/TEAM_RULES.md) (written in Vietnamese). Source: Issue 6 of the VTV show (observed from the broadcast, **not law and not a rubric from BTC (the organizers)**). Details: [episode-notes](references/episode-notes.md).

## Sample brief and deliverable
A comic warning middle and high school students about online scams, 5–10 A4 pages, free panel layout, "100% creative", both engaging and educational. The output format is flexible (web, ebook...); read the output section carefully. The show also scored a video of the making process and a presentation video.

## Suggested process
1. Plan the idea, characters, and the story from start to finish first; research the audience (students) and the specific kinds of scams.
2. Generate the character images first and use them as references for every page to keep them consistent.
3. **Leave the speech bubbles empty and fill in the text afterward** with tools/code (avoids Vietnamese text errors in images).
4. Each page has multiple panels, not just one large image; follow the arc "trap → crisis → turning point → solution".
5. Record the making process and prepare a presentation video if BTC requires it.

## Techniques worth using
- An engaging story title and cover; varied situations, not just games / strange links / lost accounts.
- Concrete lessons (spotting fake links, finding someone to help); elements that make the reader want to keep reading.
- Add a finishing layer (e.g. a website for viewing the comic) if time remains after the comic is done.

## Pitfalls observed
- Font/Vietnamese text errors in images (the most common); characters/settings inconsistent between pages.
- The image generation API failing midway; the team had not read the BTC API documentation carefully.
- Purely technical teams lacking storytelling sense; many teams using the same motif; 7 pages amounting to only 1–2 pages of a real comic.
- One team had no presentation video.

## What judges look at
A message that lands with students, Vietnamese language, consistency, use of the API/prompts, the making process, product thinking; an "AI artisan", not just an "AI laborer".

## Topic-specific checks before QA
Page count within the required range; Vietnamese text on every page; consistent characters; clear message; making-process/presentation video if required.

## Baseline quick win (API-based)

Full context: [BASELINE_PROCESSES](../../../docs/BASELINE_PROCESSES.md) (written in Vietnamese). Timeboxes assume a ~2 hour session (unconfirmed); verify models with `GET /v1/models` first.

- **Quick win:** 5 A4 pages with panels, images and dialogue, exported to PDF by minute ~40.
- **Pipeline:**
  1. `chat/completions` writes a 5-10 page script, 2-4 panels per page, as JSON.
  2. Fix a character sheet and repeat the same description in every prompt for consistency.
  3. One image per panel via Nano Banana, leaving speech bubbles empty ([image guide](../../../docs/api-guides/03-image-generation.md)).
  4. HTML fills the bubbles, export PDF; extra: a web version (the episode 6 winner did this).
- **Cost/guard:** regenerate only the failed panels.
- **Fallback:** fewer pages, simpler flat style.
- **QA gate:** characters consistent across pages, anti-scam message clear, 5-10 pages as briefed.

## Team notes (update yourself)
-
