---
name: aitc-topic-marketing-chien-dich
description: Use when the brief is to design a marketing campaign/product-promotion idea (for example Tết marketing for a financial product); lessons for when the deliverable is a campaign idea document as slides or a document.
metadata:
  version: "0.1"
  language: "en"
  status: "draft-from-vtv-observation"
---
# Topic — Marketing campaign / idea document

Main part: [Documents & strategy](../SKILL.md).

Apply the [general rules](../../../docs/TEAM_RULES.md) (written in Vietnamese). Source: Issue 11 of the VTV show (observed from TV, **not BTC (the organizers) rules or rubric**). Details: [episode-notes](references/episode-notes.md).

## Sample brief and deliverable
Tết 2026 marketing campaign for the product "Techcombank sinh lời tự động" (automatic earning): an idea document of at most 10 slides or 10 A4 pages (PDF/PowerPoint/doc), with images, slogan, customer journey, illustrative ad samples; it must convey the Tết spirit and the product's core value, and feel close to Vietnamese customers. Submit a file; no deploy needed.

## Suggested process
1. Analyze the brief: 3 keywords (flagship product, Tết tied to tradition, creative use of AI). Use AI as a quick marketing "tutor" if you lack background.
2. Collect product/customer data with structured prompts + code; analyze the concept.
3. Choose one lead image/metaphor tying the product to Tết (for example "sowing fortune") and a chain of channels (mini game, AR filter, personalized card).
4. Build the 10 slides: use HTML if generating PowerPoint with code does not work well; you can batch several slides into one prompt to save API.
5. Assign roles clearly: prompt engineering / code & data / (deploy if there is a tool).
6. Version the code/slides; do not lose old versions (one team lost its code at the end of the session).

## Techniques worth using
- Highlight the product's **automatic earning feature**; clear business goal; specific recommendations (automatic greetings, AI cards, online ads).
- Humane, family tradition at Tết; a bold, memorable message line.
- Automate data collection with AI; the way AI is used is visible in the process.

## Pitfalls observed
- Traditional Tết greetings that do not convey the product's spirit and do not mention the feature.
- Stopped at an outline and a few actions; no concrete results; a greeting-generation app needs promotion cost.
- Brief is long and hard for 120 minutes; no marketing/finance background.
- No code version management → lost code, final version less complete.

## What judges look at
Sticks to the product; creativity; humane and traditional; complete product; degree of AI automation; data research and processing; an "AI craftsman", not just an "AI operator".

## Topic-specific checks before QA
Slides state the product and core value clearly; page count ≤ 10; every product figure has a source; Vietnamese text has correct diacritics; view every page.

## Baseline quick win (API-based)

Full context: [BASELINE_PROCESSES](../../../docs/BASELINE_PROCESSES.md) (written in Vietnamese). Timeboxes assume a ~2 hour session (unconfirmed); verify models with `GET /v1/models` first.

- **Quick win:** 6-8 pages: insight, big idea, message, channels, KPI, timeline, exported to PDF/slides.
- **Pipeline:**
  1. Pick one insight and one core idea.
  2. `chat/completions` writes all sections in one structured call.
  3. 2-4 key visuals from Nano Banana (16:9, no text); text is added in HTML ([image guide](../../../docs/api-guides/03-image-generation.md)).
  4. Build the deck locally; optional 4-8 s Veo lite mood clip ([video guide](../../../docs/api-guides/04-video-generation.md)). Run the Vietnamese context review for holidays and taboos.
- **Cost/guard:** Veo is billed at job creation (lite 720p is about $0.05/s); try one 4 s scene first.
- **Fallback:** drop the motion; keep the idea and the plan.
- **QA gate:** idea fits the sponsor and audience; page count and format as briefed.

## Team notes (update yourself)
-
