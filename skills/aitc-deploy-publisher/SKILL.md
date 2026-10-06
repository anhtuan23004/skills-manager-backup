---
name: aitc-deploy-publisher
description: Use when the brief requires a product that runs online or the judges must open/play it directly, to put a web/game/app on the team's own VPS, verify the live link with real evidence, and prepare a fallback.
metadata:
  version: "1.1"
  language: "en"
  status: "prepared-not-btc-approved"
---
# 15 — Deploy and publish

Apply the [shared rules](../../docs/TEAM_RULES.md) (written in Vietnamese); re-read them only if they are not already in context or the rules have changed. Technical details and VPS preparation are in [DEPLOY](../../docs/DEPLOY.md) (written in Vietnamese); background is in [INSIGHTS](../../docs/INSIGHTS_VTV_2025.md).

## When to use
Only when brief-decoder records the deliverable as a web, game, app, or demo that the judges must be able to open via a link. If the brief asks for file submission (image, video, text, audio, slides), do not use this skill; packaging goes through [submission-controller](../aitc-submission-controller/SKILL.md).

## Inputs
The Requirement ID of the online deliverable; BTC (the organizers) instructions on where/how to submit the link and how long the link must stay alive; the team's VPS information (address, SSH alias, deploy path — excluding keys or passwords); the execution-plan; the person in charge of deploy; the T time.

## Process
1. **Check the VPS is alive (T+0–8, run on Machine B):** SSH from both machines, HTTPS opens from an outside network, the deploy script runs with an empty page. If anything fails, tell the leader immediately; do not wait until deploying the product. The host is a VPS the team prepared in advance; if the link submission location or the required uptime cannot be confirmed, mark it UNVERIFIED.
2. **One person is responsible for deploy** (recorded in the plan). This person does not also fix features in the last 30 minutes. Do not read SSH keys/`.env`/credentials into the agent context; use the existing aliases and environment variables.
3. **Early skeleton (target ~T+30, the same milestone as "first pipeline running"):** put a minimal page/flow on a real link before continuing, so that build, path, font, environment variable, and file permission errors surface early. Record the URL and the time.
4. **Lowest-risk architecture:** prefer content/assets generated at build time and served statically. Call the Gateway at runtime only if the brief requires it; in that case the key lives only on the server side (environment variable on the VPS), never in browser JS, with limits/caching so judges playing do not burn the budget.
5. **Each deploy is one release in `releases/`**, switch `current` to the new release; keep the previous release for rollback. Do not edit files that are being served directly. Operate only inside the deploy directory; do not delete/overwrite outside that scope.
6. **Feature freeze (target ~T+70):** only fix bugs and deploy the final version recorded in the plan.
7. **Smoke test on the live link**, from a machine/network different from the one used to make the work, without logging in: open the page over HTTPS, run the main flow end to end, check Vietnamese text and fonts, check that resources load, try mobile if the brief targets mobile, and confirm no keys/sensitive files are exposed. Each requirement gets PASS/FAIL/UNVERIFIED and evidence (URL, screenshot, time).
8. **Fallback prepared before T+100:** the previous release for rollback; a static build that runs locally with instructions; a recording of the main flow if BTC allows that format. Use only if the link breaks and the leader/BTC agree. Do not create new content for the fallback.
9. **Final milestones:** T+100 the candidate-version link opens from another machine/network; T+108 re-check the live link before freeze; T+112 freeze, record the URL + commit/hash of the deployed version in the manifest. After freeze, do not redeploy and do not edit files on the VPS.
10. **A human submits the link** through the BTC system. The agent only provides the checklist; it does not submit and does not change sharing permissions.

## Required outputs
deploy-checklist.md (from the [template](../../templates/deploy-checklist.md)); the verified URL with time and version (commit/hash); smoke test results; the list of UNVERIFIED items.

## Pre-return checks
Do not say "deployed" until the URL has been opened from another machine/network. Do not treat a finished deploy script as proof the product works correctly. Do not leave secrets in the repo, the build, or browser JS. Do not put pre-made product code/assets on the VPS. Do not use AI tools or services outside BTC to create content for the fallback.

## Stop and hand off to a human
Missing decisive facts, missing permission, or a conflict with the rules: state it clearly and do not fill the gap yourself.
VPS unreachable or HTTPS broken, or no location to submit the link yet: stop at step 1 and hand off to the leader.
The team leader decides; continue only within the approved scope.
