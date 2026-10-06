---
name: aitc-group-web-app
description: Use when the deliverable runs online as a web/game/app that judges must open or play via a link; common principles for this group, then open a specific topic.
metadata:
  version: "0.1"
  language: "en"
  status: "draft-from-vtv-observation"
---
# Part 1 — Web & App (runs online)

Apply the [common rules](../../docs/TEAM_RULES.md) (written in Vietnamese). Source: Episode 2 and Episode 3 of the VTV show (observation of the TV broadcast, **not BTC (the organizers) rules or rubric**). Summary: [INSIGHTS](../../docs/INSIGHTS_VTV_2025.md) (written in Vietnamese).

## Topics in this part
| Topic | Open file | Briefs seen |
|---|---|---|
| Tourism / local website | [website-du-lich](website-du-lich/SKILL.md) | Episode 2 |
| Educational game | [game-giao-duc](game-giao-duc/SKILL.md) | Episode 3 |

Always pair with [aitc-deploy-publisher](../../skills/aitc-deploy-publisher/SKILL.md), [DEPLOY](../../docs/DEPLOY.md) (the team's VPS), and the [app workflow](../../skills/aitc-production-planner/references/app-workflow.md).

## Common principles of this part
1. **Deploy is part of the deliverable, not the last step.** Two teams that could not get their site online in Episode 3 finished at the bottom of the ranking; two teams in Episode 2 only ran locally. Get a skeleton onto a real link around T+30, freeze features around T+70.
2. Fix the structure/modules/scenario **before prompting**; build one end-to-end flow before adding features.
3. Base content on **real sources** (a crawler, or structured prompts from authoritative sources); AI images must not create a false impression of the locality/audience.
4. Generate assets as a set in the same style, then assemble; Vietnamese text is inserted by code/tools.
5. Audio/images only through BTC's APIs, no outside tools.
6. Keys stay server-side only; pre-generate content at build time when possible; calculate the budget in advance if judges' play triggers Gateway calls.
7. One person owns deployment separately, apart from the person fixing features.

## Common failures of this part
Plan too complex and redone midway; backend/database/video not finished in time; running local only; arriving late and spending 15–20 minutes setting up the device; layout/gameplay not suited to the audience; missing usage instructions.

## What judges look at (common)
Creativity and user experience; completing all requirements rather than looking good but missing features; technique/optimization; the cost of building the product; authenticity of content; putting yourself in the user's shoes.

## Common checks before QA
Live link opens from another machine/network over HTTPS; the main flow runs end to end; Vietnamese text has correct diacritics; no key exposed; mobile if the brief targets mobile; [deploy-checklist](../../templates/deploy-checklist.md) filled in.

## Baseline quick win (API-based)

Baseline for this part: ship a **static site with pre-generated content and images** and deploy it first; add AI features at runtime only afterwards, from a server (never put the key in client code). See each topic's "Baseline quick win" and [BASELINE_PROCESSES](../../docs/BASELINE_PROCESSES.md).

## Team notes (update yourself)
-
