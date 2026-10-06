---
name: aitc-topic-website-du-lich
description: Use when the brief is to design a tourism or local-promotion website; lessons for when the deliverable is a website that must open via a link.
metadata:
  version: "0.1"
  language: "en"
  status: "draft-from-vtv-observation"
---
# Topic — Tourism / local-promotion website

Main part: [Web & App](../SKILL.md).

Apply the [general rules](../../../docs/TEAM_RULES.md) (written in Vietnamese). Source: Episode 2 of the VTV show (observed from TV, **not BTC (the organizers) rules or rubric**). Details: [episode-notes](references/episode-notes.md).

## Sample brief and deliverable
A tourism-promotion website for a remote locality (for example Yên Hòa village, Nghệ An). It must be visual, promote effectively, preserve local culture, and not copy existing products. **It must be on a server so users can access it**: use [aitc-deploy-publisher](../../../skills/aitc-deploy-publisher/SKILL.md) from the moment you make the plan.

## Suggested process
1. Lock the menu structure, modules and features **before prompting**; if the AI misunderstands, fixing it costs a lot of time.
2. Prompt the whole site following the locked structure, then refine section by section; check the information the AI gives by hand.
3. Skeleton version on a real link by ~T+30; keep building on top of what already runs.
4. Add extra features (tour booking, chatbot, map) only after the main site is complete.

## Techniques worth using
- Accurately positioned map, bilingual Vietnamese/English interface, light interactive effects.
- A helper tool with clear value (travel cost estimate) helps stand out.
- Use local cultural motifs (brocade) as interface material; tell the story as a journey/timeline.
- Light, fast-loading homepage.

## Pitfalls observed
- AI images that do not match the locality (terraced fields, sea boats in a place that has none) cast doubt on authenticity.
- Plan too complex → redone midway; backend/database/video not finished in time.
- Finished locally but could not get onto a server.
- Little data on remote areas; real sources must be researched.

## What judges look at
Creativity and user experience, code organization/optimization, cost of producing the product, authenticity of content.

## Topic-specific checks before QA
Check every image/claim about the locality against a source; open the live link from another machine; Vietnamese text has correct diacritics; the main flow works on mobile.

## Baseline quick win (API-based)

Full context: [BASELINE_PROCESSES](../../../docs/BASELINE_PROCESSES.md) (written in Vietnamese). Timeboxes assume a ~2 hour session (unconfirmed); verify models with `GET /v1/models` first.

- **Quick win:** a static page with all agreed modules and AI-generated assets, deployed publicly by minute ~35.
- **Pipeline:**
  1. Fix the module structure before prompting.
  2. `chat/completions` writes each module as JSON; grounding (`tools: googleSearch`) for local facts, keep the source URLs ([text guide](../../../docs/api-guides/02-text-generation.md), [grounding](../../../docs/api-guides/07-web-grounding.md)).
  3. `images/generations` (Nano Banana, `aspect_ratio` 16:9 hero / 4:3 cards, prompt says no text, no logo), one request per image ([image guide](../../../docs/api-guides/03-image-generation.md)).
  4. Assemble static HTML and deploy ([DEPLOY](../../../docs/DEPLOY.md)); only then add search, a map or a RAG chatbot via `embeddings`, called from a backend so the key never reaches the client.
- **Cost/guard:** one image per request; AI photos that look unreal draw suspicion, so label them as illustrations and match the local setting.
- **Fallback:** drop runtime API features and keep the static site.
- **QA gate:** public link opens from another device, mobile layout OK, every fact has a source URL.

## Team notes (update yourself)
-
