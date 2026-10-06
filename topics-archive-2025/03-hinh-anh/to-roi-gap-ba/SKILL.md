---
name: aitc-topic-to-roi-gap-ba
description: Use when the brief asks for a social-awareness flyer/folded leaflet (e.g. harms of stimulants/addictive substances) and the deliverable is a multi-panel print publication; lessons from observing the VTV show.
metadata:
  version: "0.1"
  language: "en"
  status: "draft-from-vtv-observation"
---
# Topic — Flyer / tri-fold flyer

Main part: [Images & communication materials](../SKILL.md).

Apply the [general rules](../../../docs/TEAM_RULES.md) (written in Vietnamese). Source: Issue 8 of the VTV show (observed from the broadcast, **not law and not a rubric from BTC (the organizers)**). Details: [episode-notes](references/episode-notes.md). Use together with [image-director](../../../skills/aitc-image-director/SKILL.md).

## Sample brief and deliverable
A tri-fold A4 sheet (6 sides/panels) raising awareness of the harms of alcohol, beer, drugs and other stimulants, to be placed in public places / tourist sites / hospitals. The content should be relatable and emotional; made entirely new with AI through the BTC API. Intermediate products (prompts, steps) are submitted along with the final piece. No deployment needed.

## Suggested process
1. Fix a one-sentence message, the audience (young people), the 6-panel layout, and the arc of psychological change.
2. AI generates the visuals (one continuous image for the whole sheet, or 6 images with the same style / shared "seed"); **insert text with HTML code or tools**, do not let the image model draw text.
3. Structured prompts (e.g. JSON), consistent output across calls; optimize API cost.
4. Check the effect when folded: light/dark panels placed side by side, the middle panel as the focal point.
5. Save the prompts/intermediate products to submit with the final piece.

## Techniques worth using
- A big message, large text, readable in a few seconds; have a call to action (a counseling hotline number, red emphasis on the middle page).
- Little text, few images, few people in the image; consistent style across the 6 panels.
- Direct figures combined with metaphorical imagery; a story of loss and hope.

## Pitfalls observed
- Faulty text in AI images (Vietnamese); fixing it by hand takes time.
- Too much text/imagery, scientific information too dense; small text.
- Image generation errors / machine freezing mid-session; a process prepared in advance that did not fit the type of brief.
- "A bit greedy", lacking systems-design thinking, led too much by the AI.

## What judges look at
Suitability for the audience and social norms; a simple, consistent message that touches emotions; use of AI/prompts; cost optimization; real-world usability; the role of human + AI.

## Topic-specific checks before QA
Print/view at real size; Vietnamese text with correct diacritics; one idea per panel; call to action present; intermediate products saved.

## Baseline quick win (API-based)

Full context: [BASELINE_PROCESSES](../../../docs/BASELINE_PROCESSES.md) (written in Vietnamese). Timeboxes assume a ~2 hour session (unconfirmed); verify models with `GET /v1/models` first.

- **Quick win:** an A4 landscape sheet with six panels in the correct fold order, exported by minute ~30.
- **Pipeline:**
  1. Assign roles to the six panels (cover, inner flap, content, contact).
  2. `chat/completions` writes short copy for the audience; sensitive topics (such as stimulants) need careful, sourced wording.
  3. 1-2 background images from Nano Banana, no text ([image guide](../../../docs/api-guides/03-image-generation.md)).
  4. HTML at 297x210 mm in three columns; check folds and cut margins; also submit intermediate files if the brief allows (the episode 8 winner did).
- **Cost/guard:** HTML text overlay avoids garbled Vietnamese from the image model.
- **Fallback:** a text-and-icon-only layout.
- **QA gate:** figures and sources correct, no text on a fold line, tone suits the audience.

## Team notes (update yourself)
-
