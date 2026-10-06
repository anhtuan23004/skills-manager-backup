---
name: aitc-topic-infographic-phap-luat
description: Use when the brief asks for a policy/law communication infographic (e.g. Luật Bảo vệ dữ liệu cá nhân, the Personal Data Protection Law) and the deliverable is an infographic summarizing a long legal document; lessons from observing the VTV show.
metadata:
  version: "0.1"
  language: "en"
  status: "draft-from-vtv-observation"
---
# Topic — Law / policy infographic

Main part: [Images & communication materials](../SKILL.md).

Apply the [general rules](../../../docs/TEAM_RULES.md) (written in Vietnamese). Source: Issue 5 of the VTV show (observed from the broadcast, **not law and not a rubric from BTC (the organizers)**). Details: [episode-notes](references/episode-notes.md).

## Sample brief and deliverable
An infographic that summarizes and visualizes the core content of Luật Bảo vệ dữ liệu cá nhân 2025 (Personal Data Protection Law 2025) for the general public. Submit the infographic image; no deployment needed. Packaging/exporting the image at the correct size is where some teams got stuck; see [submission-controller](../../../skills/aitc-submission-controller/SKILL.md).

## Suggested process
1. Use AI to break the law text into core parts (concepts, rights, highlights, responsibilities, prohibitions), chapter by chapter / article by article, with multi-level summaries.
2. **Check every point against the original text** before designing; do not trust AI output.
3. Give the AI clear roles (content creator, infographic designer) and a writing style; use structured prompts.
4. Fix the layout (header/body/footer zones), size, and color palette before generating images; insert Vietnamese text with tools/code, do not let the image model draw text.
5. Export the image at sufficient resolution; get all the content into the finished piece before adding decoration.

## Techniques worth using
- Text/background contrast: dark text on light background, light text on dark background; use color sparingly, one meaning per color.
- Have a narrative thread and clear focal points; use a chart/timeline when there are figures or milestones (the law takes effect from 01/01/2026).
- A distinctive icon set/identity so it is memorable; secondary elements must not overwhelm the main content.
- Careful language that follows legal wording (distinguish "cấm" (prohibited) from "tuyệt đối cấm" (absolutely prohibited)).

## Pitfalls observed
- Vietnamese font/diacritic errors; text in the image that "makes no sense".
- Many images with unclear meaning; questions posed that nobody answers.
- Lack of graphics (looks like a page of text); rambling colors; secondary elements too large in proportion.
- Reached only about 1/3 of the requirements because the team got stuck at packaging and at fitting all the content into the image.
- The image depends on AI output, so there is a risk of wrong legal content.

## What judges look at
Absolute accuracy against the legal text; error-free Vietnamese; clear, simple message; a distinctive highlight; citizens' rights and obligations; prompting skill and choosing the right tool for the situation.

## Topic-specific checks before QA
Check every legal claim against the articles; correct effective date and law name; size/resolution as the brief requires; read the text carefully at real size; contrast.

## Baseline quick win (API-based)

Full context: [BASELINE_PROCESSES](../../../docs/BASELINE_PROCESSES.md) (written in Vietnamese). Timeboxes assume a ~2 hour session (unconfirmed); verify models with `GET /v1/models` first.

- **Quick win:** a one-page infographic with 4-6 information blocks exported to PNG by minute ~30.
- **Pipeline:**
  1. Take the official law text and select the articles needed.
  2. `chat/completions` summarizes each block and tags the article number; check each block in `templates/claims.csv`.
  3. Background/icons from Nano Banana (3:4 or 9:16, no text) ([image guide](../../../docs/api-guides/03-image-generation.md)).
  4. HTML overlays the text, check contrast, render PNG at the briefed size.
- **Cost/guard:** one image per request; keep passing images and regenerate only the failed ones.
- **Fallback:** a pure HTML/CSS infographic without AI images.
- **QA gate:** content matches the law, no wrong diacritics, readable when scaled down, and the export step has been rehearsed (a team got stuck there in episode 5).

## Team notes (update yourself)
-
