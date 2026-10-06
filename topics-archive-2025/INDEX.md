> **ARCHIVED (2026-10-06).** These 10 topics come from the 2025 season and are kept for reference. Current work uses [topics/INDEX](../topics/INDEX.md), [LESSONS](../topics/LESSONS.md) and the [base template](../topics/_template/SKILL.md). Links inside this folder keep the same depth as before the move.

# Topic index (by the 4 main parts)

`skills/` holds the common workflow (read the brief → plan → produce → QA → submit). `topics/` holds experience specific to each type of brief, drawn from 10 episodes of the VTV show "A.I Thực chiến 2025" (Episode 2 → Issue 11). The source is observation of the TV broadcast, **not BTC (the organizers) rules or rubric**; see [INSIGHTS](../docs/INSIGHTS_VTV_2025.md) (written in Vietnamese) for the big picture.

**Quick-win baseline per topic (API-based pipeline, timeboxes, fallbacks):** [BASELINE_PROCESSES](../docs/BASELINE_PROCESSES.md) (written in Vietnamese).

## How to use
1. From the deliverable in the brief, pick **one main part** and read that part's `SKILL.md` (principles, failures, criteria, common checks).
2. Open **one specific topic** if the brief matches; do not load the whole set.
3. Each topic has a `SKILL.md` and `references/episode-notes.md` (original notes from the episode). At the end of each `SKILL.md` there is a "Team notes (update yourself)" section for the team to update.

## The four main parts

### 1. [Web & App](01-web-app/SKILL.md) — runs online, **needs deploy**
| Topic | Episode | Deliverable |
|---|---|---|
| [website-du-lich](01-web-app/website-du-lich/SKILL.md) (tourism website) | Episode 2 | Local promotion website |
| [game-giao-duc](01-web-app/game-giao-duc/SKILL.md) (educational game) | Episode 3 | Educational web/mobile game |

### 2. [Documents & strategy](02-tai-lieu/SKILL.md) — slides/documents of ≤10 pages
| Topic | Episode | Deliverable |
|---|---|---|
| [bao-cao-tai-chinh](02-tai-lieu/bao-cao-tai-chinh/SKILL.md) (financial report) | Issue 4 | Board of Directors report / financial analysis |
| [marketing-chien-dich](02-tai-lieu/marketing-chien-dich/SKILL.md) (marketing campaign) | Issue 11 | Marketing campaign idea document |

### 3. [Images & print materials](03-hinh-anh/SKILL.md) — images/static pages with Vietnamese text
| Topic | Episode | Deliverable |
|---|---|---|
| [infographic-phap-luat](03-hinh-anh/infographic-phap-luat/SKILL.md) (legal infographic) | Issue 5 | Infographic summarizing a law |
| [truyen-tranh](03-hinh-anh/truyen-tranh/SKILL.md) (comic) | Issue 6 | 5–10 page comic |
| [to-roi-gap-ba](03-hinh-anh/to-roi-gap-ba/SKILL.md) (tri-fold leaflet) | Issue 8 | A4 tri-fold leaflet |

### 4. [Video & Audio](04-video-audio/SKILL.md) — assembled from short clips/segments
| Topic | Episode | Deliverable |
|---|---|---|
| [ban-tin-video](04-video-audio/ban-tin-video/SKILL.md) (news bulletin video) | Issue 7 | 60–80 second news bulletin video |
| [podcast-audio](04-video-audio/podcast-audio/SKILL.md) (podcast) | Issue 9 | Two-character podcast, 2–4 minutes |
| [sang-tac-bai-hat](04-video-audio/sang-tac-bai-hat/SKILL.md) (songwriting) | Issue 10 | Song + lyric video, ~3 minutes |

Across all parts: [aitc-deploy-publisher](../skills/aitc-deploy-publisher/SKILL.md) when the brief requires an online link; [DEPLOY](../docs/DEPLOY.md) (written in Vietnamese) and [deploy-checklist](../templates/deploy-checklist.md).

## Adding a new topic or part
- **New topic:** copy an existing topic folder into the right part, change `name`, update the content, add a row to that part's table (and to the part's `SKILL.md`).
- **New part:** create a folder `0N-<name>/` with a `SKILL.md` following the template of an existing part, and add it to this index.
- Keep the original notes in `references/` so it stays clear what was observed and what is the team's assumption.
