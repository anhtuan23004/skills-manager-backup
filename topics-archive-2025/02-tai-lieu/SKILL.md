---
name: aitc-group-tai-lieu
description: Use when the deliverable is a slide deck or document of ≤10 pages with domain-specific content (financial report, marketing campaign); common principles for this group.
metadata:
  version: "0.1"
  language: "en"
  status: "draft-from-vtv-observation"
---
# Part 2 — Documents & strategy (slides/documents)

Apply the [common rules](../../docs/TEAM_RULES.md) (written in Vietnamese). Source: Issue 4 and Issue 11 of the VTV show (observation of the TV broadcast, **not BTC (the organizers) rules or rubric**). Summary: [INSIGHTS](../../docs/INSIGHTS_VTV_2025.md) (written in Vietnamese).

## Topics in this part
| Topic | Open file | Briefs seen |
|---|---|---|
| Financial report / analysis | [bao-cao-tai-chinh](bao-cao-tai-chinh/SKILL.md) | Issue 4 |
| Marketing campaign / idea | [marketing-chien-dich](marketing-chien-dich/SKILL.md) | Issue 11 |

Pair with [text-producer](../../skills/aitc-text-producer/SKILL.md), [vietnam-context-review](../../skills/aitc-vietnam-context-review/SKILL.md) when there are claims/figures, and [artifact-critic](../../skills/aitc-artifact-critic/SKILL.md). No deploy needed; submit the file.

## Common principles of this part
1. **Learn the domain first with AI** when the team lacks the background (finance, marketing), then start building; split people into background knowledge / data / presentation.
2. Official data, correct period, with sources; cap the time spent finding data so there is time left for analysis and presentation.
3. Stick to **the product/organization in the brief**: the real report format, the right colors/logo/identity, highlight the core value.
4. Page limit (≤10): one idea per page, with a concrete conclusion/recommendation, not stopping at an outline.
5. Build slides in HTML or by prompt if generating PowerPoint with code is unreliable; do not change direction near the end.
6. Automating data collection with structured prompts + code earns bonus points; batch several slides into one prompt to save API calls.
7. Manage versions; do not lose code/slides near the end.

## Common failures of this part
Figures from the wrong year/period; wrong logo/colors from AI; Vietnamese text errors in images; simple charts; cluttered layout; generic content that lacks the spirit of the product; poor time management (AI generates slide code, then 30 minutes of manual work at the end).

## What judges look at (common)
Sticking to the brief and the right product; understanding of the business context; accurate data and depth of analysis; creative but humane/culturally appropriate; aesthetics; degree of automation with AI; an "AI craftsman", not just an "AI operator".

## Common checks before QA
Every figure has a source and the correct period; page count within the limit; logo/colors correct; Vietnamese text has correct diacritics; view every page at actual size.

## Baseline quick win (API-based)

Baseline for this part: the Gateway has **no slide endpoint**, so text comes from `chat/completions` and pages are built locally (HTML to PDF or a deck library; export helpers live in [huashu-design](../03-hinh-anh/huashu-design/SKILL.md) and need team and BTC approval). Confirm the submission format first. See [BASELINE_PROCESSES](../../docs/BASELINE_PROCESSES.md).

## Team notes (update yourself)
-
