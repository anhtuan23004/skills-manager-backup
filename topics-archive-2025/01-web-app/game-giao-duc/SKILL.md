---
name: aitc-topic-game-giao-duc
description: Use when the brief is to build an interactive educational-communication game (for example food safety for students); lessons for when the deliverable is a game playable on web/mobile.
metadata:
  version: "0.1"
  language: "en"
  status: "draft-from-vtv-observation"
---
# Topic — Educational game (web/mobile)

Main part: [Web & App](../SKILL.md).

Apply the [general rules](../../../docs/TEAM_RULES.md) (written in Vietnamese). Source: Episode 3 of the VTV show (observed from TV, **not BTC (the organizers) rules or rubric**). Details: [episode-notes](references/episode-notes.md).

## Sample brief and deliverable
An interactive mobile game communicating food hygiene and safety to lower-secondary (THCS) students. The game runs on a web platform and is **hosted publicly so judges can play it directly**. Use [aitc-deploy-publisher](../../../skills/aitc-deploy-publisher/SKILL.md) from the start; deploy was the biggest bottleneck of the table.

## Suggested process
1. Pick a popular game scenario (quiz, runner, bodyguard...) and insert the knowledge into it; 2D scope, no 3D within 120 minutes.
2. Get data from authoritative sources (crawler or structured prompt) before writing questions/knowledge content.
3. Build a playable game skeleton early; on a real link by ~T+30.
4. Generate images as a same-style set, then assemble; generate audio/music **through the BTC API**, not outside tools.
5. From ~T+70 only polish and deploy; with ~12 minutes left, check the live link.

## Techniques worth using
- Several different interaction types (quiz, interacting with pictures), not just one.
- Vietnamese mascots (water buffalo...) instead of foreign symbols; no errors in text inside images.
- Play instructions, and replayability (AI generates multiple scenarios each round).
- Subtle educational message; the game must be engaging first.

## Pitfalls observed
- 2/10 teams could not host in time → not fully played/evaluated, finished last (157 and 183 points).
- Music-generation tool outside the BTC API → warned by the invigilator.
- Entered 15 minutes late, device fault → cut graphics and effects.
- Wrong layout (large picture, small choices); game too light for THCS; panda mascot.
- Educational message too obvious; missing play instructions.

## What judges look at
Idea → design → execution; using AI to increase efficiency; putting yourself in the player's shoes; reasonable scope; "doing it correctly and completely matters more than a beautiful product that lacks the required features".

## Topic-specific checks before QA
Play one full round on the live link from another machine and on mobile; check knowledge content against sources; all audio/image assets go through the BTC API; do not expose the key when the game calls the Gateway.

## Baseline quick win (API-based)

Full context: [BASELINE_PROCESSES](../../../docs/BASELINE_PROCESSES.md) (written in Vietnamese). Timeboxes assume a ~2 hour session (unconfirmed); verify models with `GET /v1/models` first.

- **Quick win:** a one-level playable web game with questions in a static JSON file, deployed early (episode 3 teams that missed hosting ranked last).
- **Pipeline:**
  1. Collect official content first (crawler or grounding), keep the sources.
  2. `chat/completions` with `response_format: json_object` generates the question set; validate the schema in code ([OpenAI/DeepSeek notes](../../../docs/api-guides/09-openai-deepseek.md)).
  3. Build the HTML/JS game loop with score; art via Nano Banana without text.
  4. Deploy by the last ~50 minutes at the latest, then polish; add levels or `audio/speech` voice-over only after the first live link works.
- **Cost/guard:** never embed `AITC_API_KEY` in client JS; call the Gateway only from a server if runtime AI is needed.
- **Fallback:** fewer levels but stable on a phone.
- **QA gate:** someone outside the team plays from the public link; content checked against sources.

## Team notes (update yourself)
-
