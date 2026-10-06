---
name: huashu-design-lite
description: Use when you receive a brief for a visual deliverable (infographic, flyer, poster, cover, slide deck) and must set the design direction, plan the layout system, self-critique, and export the result to PDF/PPTX.
metadata:
  version: "0.3"
  language: "en"
  status: "guideline-with-export-scripts"
  upstream: "https://github.com/alchaincyf/huashu-design"
  upstream_commit: "0830494"
  license: "MIT (upstream LICENSE)"
---

# Design guideline for a new brief (huashu-design, trimmed)

Shared rules apply: `../../../docs/TEAM_RULES.md` (written in Vietnamese) override this guideline on any conflict. This is mainly a guideline for when a brief arrives, plus the PDF/PPTX export helpers in `scripts/`. The scripts are untrusted third-party code: read them before use, and do not install (`npm`, Playwright) or run anything without team approval and BTC confirmation that the utility code is allowed. Image direction and final QA stay with the toolkit skills (see "Fit with the toolkit").

## Mindset
You are a designer, not a programmer who writes HTML. The output should not look AI-made; a viewer should ask "which studio made this?" Decide who leads before starting: art direction (taste, cutting), visual design (layout, color, type, hierarchy), implementation, copy. A deck is not a web page and an infographic is not a dashboard. Quality comes from the options you considered and rejected.

## Core principles (highest priority first)
1. **Start from existing context.** Read the brief, supplied assets, source files and screenshots first. Designing from nothing is a last resort and yields generic work; if the brief is vague, use the direction advisor below.
2. **Align assumptions before building.** Write assumptions, reasoning and placeholders at the top of your draft and show it early. A misunderstanding fixed early is far cheaper than late.
3. **Give variations, not a "final answer".** Offer distinct options in layout, color and tone, so the team can mix and match.
4. **Placeholder beats bad implementation.** No icon: a labeled gray box. No data: mark "waiting for real data". Never invent data that looks real.
5. **System over filler.** Every element earns its place. Fix emptiness with composition, not invented content. Watch for data slop (pointless stats), icon slop (an icon on every heading) and gradient slop.

### Facts, brands and images (toolkit rules)
- Facts: do not assume facts about real products, laws or figures. Take them from the brief, the team's source files or the BTC Gateway grounding feature; otherwise mark the claim UNVERIFIED.
- Brands: use only logos and brand assets supplied by the brief or approved by BTC (the organizers). Never download from the web. If a named brand's logo is missing, ask the team leader and use a clearly marked placeholder. Take colors only from supplied assets.
- Images: only from the BTC Gateway image API or supplied files; no stock or web downloads. If a content-critical image is unavailable, use a labeled placeholder and say so.
- Test for any image: "If I remove it, is information lost?" If not, it is decoration; skip it.

## Anti "AI slop"
AI slop is the visual lowest common denominator of training data; it carries no brand information. Avoid:

| Avoid | Why | Acceptable when |
|---|---|---|
| Aggressive purple gradients | Generic "tech" formula | The brand itself uses it |
| Emoji as icons | Filler for "not professional enough" | Brand or audience calls for it |
| Rounded card with a colored left border | Overused 2020-2024 default | Brand spec keeps it |
| SVG-drawn faces, scenes, objects | Always misaligned | Almost never; use a generated image or placeholder |
| CSS silhouettes standing in for a real product | Every product looks the same | Almost never |
| Inter/Roboto/Arial/system fonts as display type | Reads as "demo page" | Brand spec mandates it |
| Uniform dark navy plus generic cyan/purple glow | Lazy SaaS/AI look | Developer-tool brand that lives there |

Do instead: polish typography (`text-wrap: pretty`, grid, consistent rhythm); use colors from the brief, never invent them on the fly; push one detail to 120% and the rest to 80%. Full list: `references/content-guidelines.md`.

## Design direction advisor (simplified)
Purpose: avoid the worst design, not dictate good design. Real design grows from the brief and its content; the style library in `references/design-styles.md` is a spark when there is no idea, not a menu.

When the request is vague or there is no reference, do this in ONE turn (cap about 5 minutes; no subagents, no long spec):
1. Restate the need in 2-3 sentences: audience, message, tone, output format and pixel size.
2. Write THREE short directions. Each has: a name, one layout idea (the skeleton must differ structurally, not just recolor), a palette (3-5 colors with hex), a type pairing, one line on mood, optionally a reference style.
3. Present them and let the team leader pick. Do not pick on the team's behalf.

Readability floor: body text at least 14px (scale up for large canvases), labels at least 12px, body contrast at least 4.5:1. If the brief already fixes the style or the leader says "just build it", skip the advisor and note it in your assumptions. Use the real content from the brief in all three, not Lorem ipsum.

## Workflow when a brief arrives
1. **Clarify** only what is missing, in one batch (templates in `references/workflow.md`): assets, number of variations, what matters most. Skip for small edits.
2. **Explore context.** Read the brief and supplied assets. If nothing exists, run the advisor, then `references/design-context.md` as a taste anchor.
3. **Plan the system.** Answer five form questions for every page or screen before choosing style:
   - Narrative role: hero, transition, data, quote or closing?
   - Viewing distance: phone (10 cm), laptop (1 m), projector (10 m)? This sets type size and density.
   - Visual temperature: calm, excited, authoritative, gentle, sad?
   - Capacity: sketch three rough thumbnails; does the content actually fit?
   - Visual motif: what element, structure or metaphor belongs only to this content? If you cannot answer, you are drawing a style lottery.
   Then state the system (color, type, layout rhythm, components). The system serves the answers, not the reverse. Write one sentence on "where the form comes from in the content".
4. **Early draft with assumptions.** Skeleton with gray boxes, labels and an assumptions note. Show it before filling in.
5. **Build, then check by eye.** View the real render, check console errors, and read every text at final size. `scripts/verify.py` takes screenshots (see `references/verification.md`); verify the checker before trusting it.
6. **Critique** (below), then fix concept before execution.
7. **Export** when the brief needs PDF or PPTX (see "Slide decks and export").
8. **Summarize briefly:** caveats and next steps only.

Under time pressure: skip the early draft, build one option, and label it "not early-validated". If reference and brand brief contradict, stop, name the contradiction and let the leader choose.

## Slide decks and export
Decide the architecture first; the wrong one costs repeated CSS-scoping bugs. Read the "decide architecture first" part of `references/slide-decks.md`.
- Default: multi-file plus overview wall. Each slide is its own 1920x1080 HTML file with a `<section>`; copy `assets/deck_index.html` to `index.html` and edit its manifest. It provides keyboard navigation, scaling, page counter and overview modes; do not rewrite the overview. The gallery mode needs thumbnails from `scripts/gen_deck_thumbs.mjs`.
- Single file: only for 5 pages or fewer with no overview wall. Use `assets/deck_stage.js` (the `<script>` goes after `</deck-stage>`).
- Page numbers come from the deck shell only; never draw them inside a slide. Fixed-size content needs auto-scale with letterboxing.
- Delivery chain: HTML deck, then PDF with `scripts/export_deck_pdf.mjs` (multi-file) or `scripts/export_deck_stage_pdf.mjs` (single-file), then editable PPTX only if requested.
- PPTX route A (HTML not written yet): write it to the 4 hard constraints, then `scripts/export_deck_pptx.mjs` (calls `scripts/html2pptx.js`); see `references/editable-pptx.md`.
- PPTX route B (HTML already written, or a client template must be inherited): `scripts/pptx_from_rendered.py` reads rendered coordinates with zero rework; see `references/pptx-from-rendered-html.md`.
- Never mix the routes, and never degrade an existing design just to satisfy route A's constraints.
- Dependencies are not installed and not pinned in this copy. Node scripts need `playwright`, `pptxgenjs`, `pdf-lib`, `sharp`; Python scripts need `playwright`, `python-pptx`, `Pillow` (plus Chromium for Playwright). Install only with team approval, pin the versions you tested, and test one export with Vietnamese text before the contest.
- After any export, re-check Vietnamese diacritics and fonts in the output file; missing fonts fall back silently.

## Expert critique
Use for a review, scoring, or a self-check. Follow `references/critique-guide.md`. Critique the design, not the designer.
- Score six dimensions from 1 to 10: Concept, Philosophy alignment, Visual hierarchy, Craft quality, Functionality, Originality.
- Concept comes first and has veto power: "does this design have an idea?" and "if I swap the client or product name, does it still hold?" If yes, it is a template and Concept is 5 or below.
- Cap: if Concept is 5 or below, the overall score cannot exceed 6.0. Fix the concept before the execution.
- Output three blocks: Keep, Fix (with severity: fatal, important, polish), Quick wins (top 3 doable in 5 minutes).
- The guide has an emphasis table by output type and the top 10 common problems.

## Vietnamese deliverables
- Use fonts with full Vietnamese diacritic support and bundle them inside the build; no CDN or external font links. Check stacked marks (for example "ệ", "ữ", "ẵ").
- Save and declare UTF-8 (`<meta charset="utf-8">`).
- Use generous line-height (at least 1.4-1.5 for body, about 1.2-1.3 for large headings) because stacked diacritics clip; add padding above all-caps headings and avoid `overflow: hidden` on tight boxes.
- Never let an image model draw Vietnamese text: generate the image without text and overlay all text with HTML.
- Check every diacritic at final size, including after any export or conversion; missing fonts fall back silently.

## Fit with the toolkit
- Pairs with `../../../skills/aitc-image-director/SKILL.md` (image direction and prompts), `../../../skills/aitc-artifact-critic/SKILL.md` and `../../../skills/aitc-final-qa/SKILL.md`. The critique output (scores plus Keep / Fix / Quick wins) can be handed to artifact-critic.
- Time guidance uses the toolkit's T+ marks; do not invent new deadlines. "About 5 minutes" for directions is a cap, not a schedule.
- Process notes for image topics: `../references/skills-va-quy-trinh.md` (written in Vietnamese).

## Exceptions
State what happened in one sentence first, then act; never decide silently.

| Situation | Action |
|---|---|
| Request too vague to start | Run the direction advisor instead of asking ten questions |
| Team says "stop asking, just build" | Fill in assumptions yourself and list them |
| Conflicting design context | Stop, name the conflict, let the leader pick |
| Tight deadline | One option only, labeled "not early-validated" |
| Dense data screens | At least 3 pieces of meaningful information per screen; decorative icons stay banned |

## References (read only what the current task needs)
| Task | Read |
|---|---|
| Clarifying questions, setting direction | `references/workflow.md` |
| Anti-slop and content rules | `references/content-guidelines.md` |
| No context, need a style spark (60 styles: web, PPT, infographic) | `references/design-styles.md`, `references/design-context.md` |
| Critique and scoring | `references/critique-guide.md` |
| Building a deck | `references/slide-decks.md`, `assets/deck_index.html`, `assets/deck_stage.js`, `scripts/gen_deck_thumbs.mjs` |
| Editable PPTX, route A | `references/editable-pptx.md`, `scripts/html2pptx.js`, `scripts/export_deck_pptx.mjs` |
| Editable PPTX, route B | `references/pptx-from-rendered-html.md`, `scripts/pptx_from_rendered.py` |
| PDF export | `scripts/export_deck_pdf.mjs`, `scripts/export_deck_stage_pdf.mjs` |
| Validation | `references/verification.md`, `scripts/verify.py` |
