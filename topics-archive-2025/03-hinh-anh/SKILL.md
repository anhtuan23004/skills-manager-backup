---
name: aitc-group-hinh-anh
description: Use when the deliverable is a communication image or print material (infographic, leaflet, comic), i.e. an image or a set of static pages with Vietnamese text; common principles for this group.
metadata:
  version: "0.1"
  language: "en"
  status: "draft-from-vtv-observation"
---
# Part 3 — Images & communication materials

Apply the [common rules](../../docs/TEAM_RULES.md) (written in Vietnamese). Source: Issues 5, 6, 8 of the VTV show (observation of the TV broadcast, **not BTC (the organizers) rules or rubric**). Summary: [INSIGHTS](../../docs/INSIGHTS_VTV_2025.md) (written in Vietnamese).

## Topics in this part
| Topic | Open file | Briefs seen |
|---|---|---|
| Legal / policy infographic | [infographic-phap-luat](infographic-phap-luat/SKILL.md) | Issue 5 |
| Educational / warning comic | [truyen-tranh](truyen-tranh/SKILL.md) | Issue 6 |
| Leaflet / tri-fold | [to-roi-gap-ba](to-roi-gap-ba/SKILL.md) | Issue 8 |

Pair with [image-director](../../skills/aitc-image-director/SKILL.md), [text-producer](../../skills/aitc-text-producer/SKILL.md) for text, and [vietnam-context-review](../../skills/aitc-vietnam-context-review/SKILL.md). No deploy needed unless the comic is submitted as a web page.

## Common principles of this part
1. **Separate text from images.** Vietnamese text/diacritic errors are failure number 1 in all three briefs. Approaches that worked: AI writes HTML that overlays text on the image (URX, Issue 8, won); leave speech bubbles empty and fill in the text afterwards (PTIT AI, Issue 6); post-process the text with auxiliary tools (AI Avengers, Issue 6, won).
2. Fix the one-sentence message, audience, layout (zones/panels/pages), color palette and size **before generating images**.
3. Stay consistent: a character image/seed/shared style serves as the reference for every page/panel.
4. Simple message, large text, few images, few colors; one meaning per color; light background with dark text or the reverse.
5. Content must be correct and sourced (especially law); check every point against the original text.
6. Structured prompts (JSON/role/tone), uniform output across calls; optimize API cost.
7. Save prompts and intermediate products; you may have to submit the process video as well (Issues 6, 8).

## Common failures of this part
Faulty/meaningless Vietnamese text in images; faulty fonts; too much text, imagery, and too many people; secondary elements overshadowing the main content; scattered colors; inconsistent characters/style; only ~1/3 done because stuck on packaging and cramming in content; image generation API failing mid-session.

## What judges look at (common)
A clear, simple message that touches emotion/fits the audience; content accuracy; error-free Vietnamese; a distinctive highlight; call to action; prompts and tool choice used in the right places; a product that is genuinely usable.

## Common checks before QA
View at actual size; check Vietnamese text on every page/panel; size/page count as the brief requires; one idea per page/panel; content checked against sources; intermediate products saved.

## Baseline quick win (API-based)

Baseline for this part: **AI background without text + HTML-inserted Vietnamese text**, rendered at the briefed size. Pipeline: text, layout, background, HTML overlay, render, check. See [BASELINE_PROCESSES](../../docs/BASELINE_PROCESSES.md).

## Team notes (update yourself)
-
