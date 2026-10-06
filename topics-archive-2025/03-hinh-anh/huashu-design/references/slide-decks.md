# Slide Decks: HTML Slide Production Guide

Making slides is a high-frequency design task. This document explains how to build HTML slides well, covering the full path from architecture choice and single-slide design to PDF/PPTX export.

**What this skill covers**:
- **HTML presentation version (the base deliverable, always required by default)** → each slide is a standalone HTML file, aggregated by `assets/deck_index.html`; keyboard paging and full-screen presenting in the browser
- HTML → PDF export → `scripts/export_deck_pdf.mjs` / `scripts/export_deck_stage_pdf.mjs`
- HTML → editable PPTX export → `references/editable-pptx.md` + `scripts/html2pptx.js` + `scripts/export_deck_pptx.mjs` (requires the HTML to follow the 4 hard constraints)

> **⚠️ HTML is the foundation; PDF/PPTX are derivatives.** Whatever format is finally delivered, you **must** first build the aggregated HTML presentation (`index.html` + `slides/*.html`). It is the "source" of the slide work. PDF/PPTX are snapshots exported from the HTML with a single command.
>
> **Why HTML first**:
> - Best for live talks/presentations (projector / shared screen goes full-screen directly, keyboard paging, no dependency on Keynote/PowerPoint)
> - During development each slide can be opened on its own with a double-click for verification, with no need to re-run the export each time
> - It is the only upstream of PDF/PPTX export (avoids the dead loop of "discovering after export that the HTML must change and re-exporting")
> - The deliverable can be "HTML + PDF" or "HTML + PPTX", and the recipient uses whichever they prefer
>
> 2026-04-22 moxt brochure field test: after building 13 HTML pages + the aggregated index.html, `export_deck_pdf.mjs` exported the PDF in one line with zero changes. The HTML version itself is a deliverable that can be presented directly in a browser.

---

## 🛑 Confirm the delivery format before starting (the hardest checkpoint)

**This decision comes before "single file or multiple files".** Field test on the 2026-04-20 stock-option board project: **not confirming the delivery format before starting = 2-3 hours of rework.**

### Decision tree (HTML-first architecture)

All deliverables start from the same aggregated HTML (`index.html` + `slides/*.html`). The delivery format only determines the **HTML authoring constraints** and the **export command**:

```
[Always the default · mandatory] Aggregated HTML presentation (index.html + slides/*.html)
   │
   ├── Browser presentation only / local HTML archive   → done at this point; HTML gives the most visual freedom
   │
   ├── Also need PDF (print / send to a group / archive) → run export_deck_pdf.mjs for one-step output
   │                                          HTML authoring is free, no visual constraints
   │
   └── Also need editable PPTX (colleagues will edit text) → follow the 4 hard constraints from the very first line of HTML
                                              run export_deck_pptx.mjs for one-step output
                                              sacrifices gradients / web components / complex SVG
```

### Kickoff script (copy and use)

> Whether the final deliverable is HTML, PDF, or PPTX, I will first build an aggregated HTML version that can be switched and presented in the browser (`index.html` with keyboard paging). This is the permanent default base deliverable. On top of it, I will then ask whether you want an extra PDF / PPTX snapshot.
>
> Which export format do you need?
> - **HTML only** (presentation/archive) → fully free visually
> - **Also PDF** → same as above, plus one export command
> - **Also editable PPTX** (colleagues will edit text in PowerPoint) → I must follow the 4 hard constraints from the very first line of HTML, which sacrifices some visual capability (no gradients, no web components, no complex SVG).

### Why "wanting PPTX means following the 4 hard constraints from the start"

Editable PPTX depends on `html2pptx.js` being able to translate the DOM element by element into PowerPoint objects. It requires **4 hard constraints**:

1. Body fixed at 960pt × 540pt (matches `LAYOUT_WIDE`, 13.333″ × 7.5″, not 1920×1080px)
2. All text wrapped in `<p>`/`<h1>`-`<h6>` (no text placed directly in a div; no using `<span>` to carry the main text)
3. `<p>`/`<h*>` themselves cannot have background/border/shadow (put them on an outer div)
4. `<div>` cannot use `background-image` (use an `<img>` tag)
5. No CSS gradients, no web components, no complex SVG decoration

**This skill's default HTML has a lot of visual freedom**: heavy use of span, nested flex, complex SVG, web components (such as `<deck-stage>`), and CSS gradients. **Almost none of it passes the html2pptx constraints naturally** (in field tests, visually driven HTML run straight through html2pptx had a pass rate < 30%).

### Cost comparison of the two real paths (a real pitfall from 2026-04-20)

| Path | Approach | Result | Cost |
|------|------|------|------|
| ❌ **Write HTML freely first, patch up PPTX afterwards** | Single-file deck-stage + lots of SVG/span decoration | To get an editable PPTX only two options remain:<br>A. Hand-write several hundred lines of pptxgenjs with hardcoded coordinates<br>B. Rewrite the 17 HTML pages into Path A format | 2-3 hours of rework, and the hand-written version has **permanent maintenance cost** (change one word in the HTML and the PPTX must be manually synced again) |
| ✅ **Follow Path A constraints from step one** | One standalone HTML per slide + 4 hard constraints + 960×540pt | One command exports a 100% editable PPTX, and it can also be presented full-screen in the browser (Path A HTML is standard browser-playable HTML) | Spend 5 extra minutes while writing HTML thinking about "how to wrap text in `<p>`"; zero rework |

### What about mixed delivery

The user says "I want an HTML presentation **and** an editable PPTX". **This is not a mix**; the PPTX requirement subsumes the HTML requirement. HTML written to Path A can itself be presented full-screen in the browser (just add a `deck_index.html` stitcher). **There is no extra cost.**

The user says "I want PPTX **and** animations / web components". **This is a real conflict.** Tell the user: getting an editable PPTX means sacrificing these visual capabilities. Let them make the trade-off; do not quietly go with a hand-written pptxgenjs solution (it becomes permanent maintenance debt).

### What if you only learn that PPTX is needed afterwards (emergency remedy)

In rare cases the HTML is already written when you find out PPTX is needed. The recommended route is the **fallback flow** (full description at the end of `references/editable-pptx.md`, "Fallback: existing visual draft but the user insists on editable PPTX"):

1. **First choice: export a PDF** (visuals 100% preserved, cross-platform, the recipient can view and print). If the recipient's real need is "presenting/archiving", PDF is the best deliverable
2. **Second choice: have the AI use the visual draft as a blueprint and rewrite an editable HTML version** → export editable PPTX. Keeps the design decisions on color/layout/copy, sacrifices visual capabilities such as gradients, web components, and complex SVG
3. **Not recommended: rebuild by hand-writing pptxgenjs**. Position, fonts, and alignment all need manual tuning, maintenance cost is high, and every later HTML change requires another manual sync

Always tell the user the options and let them decide. **Never start hand-writing pptxgenjs as your first reaction**; it is the last-resort fallback.

---

## 🛑 Before batch production: build 2 showcase pages first to set the grammar

**Whenever the deck is ≥ 5 pages, never write straight from page 1 to the last page.** The correct order, validated in the 2026-04-22 moxt brochure project:

1. Pick **the 2 page types with the greatest visual difference** and build them as showcases first (e.g. "cover" + "emotion/quote page", or "cover" + "product showcase page")
2. Screenshot them and have the user confirm the grammar (masthead / fonts / colors / spacing / structure / Chinese-English bilingual ratio)
3. Once the direction is approved, batch-produce the remaining N-2 pages, each reusing the established grammar
4. When everything is done, compose the aggregated HTML + PDF / PPTX derivatives together

**Why**: writing all 13 pages straight through → user says "wrong direction" = 13 reworks. Building 2 showcase pages first → wrong direction = 2 reworks. Once the visual grammar is established, the decision space for the remaining pages narrows sharply to just "how the content fits in".

**Showcase page selection principle**: pick the two pages with the most different visual structure. If these two pass, all the in-between states will pass.

| Deck type | Recommended showcase page combination |
|-----------|---------------------|
| B2B brochure / product promotion | Cover + content page (philosophy/emotion page) |
| Brand launch | Cover + product feature page |
| Data report | Big data chart page + analysis conclusion page |
| Tutorial courseware | Chapter cover page + specific knowledge-point page |

---

## 📐 Publication grammar template (moxt field-tested, reusable)

Suited to B2B brochure / product promotion / long-report decks. Reusing this structure on every page = 13 visually consistent pages, 0 rework.

### Skeleton of each page

```
┌─ masthead (top strip + horizontal rule) ──┐
│  [logo 22-28px] · A Product Brochure                Issue · Date · URL │
├──────────────────────────────────────────┤
│                                          │
│  ── kicker (short green bar + uppercase label)   │
│  CHAPTER XX · SECTION NAME                 │
│                                          │
│  H1 (Chinese Noto Serif SC 900)           │
│  key words alone in the brand primary color │
│                                          │
│  English subtitle (Lora italic, subtitle)   │
│  ─────────── divider ──────────            │
│                                          │
│  [specific content: two columns 60/40 / 2x2 grid / list] │
│                                          │
├──────────────────────────────────────────┤
│ section name                     XX / total │
└──────────────────────────────────────────┘
```

### Style conventions (copy directly)

- **H1**: Chinese Noto Serif SC 900, size 80-140px depending on information volume, key words alone in the brand primary color (do not pile color across the whole text)
- **English subtitle**: Lora italic 26-46px; brand signature words (such as "AI team") in bold + primary-color italic
- **Body**: Noto Serif SC 17-21px, line-height 1.75-1.85
- **Accent highlight**: in the body, mark key words in bold primary color, no more than 3 per page (too many and they lose their anchoring effect)
- **Background**: warm off-white base #FAFAFA + very faint radial-gradient noise (`rgba(33,33,33,0.015)`) to add a paper feel

### The visual protagonist must vary

If all 13 pages are "text + one screenshot" it gets too monotonous. **Rotate the visual protagonist type on every page**:

| Visual type | Suitable section |
|---------|---------------|
| Cover layout (large type + masthead + pillar) | Home page / chapter cover |
| Single-character portrait (a huge single momo, etc.) | Introducing a single concept/character |
| Multi-character group shot / avatar cards side by side | Team / user cases |
| Timeline cards progressing | Showing "long-term relationship" or "evolution" |
| Knowledge graph / connected-node diagram | Showing "collaboration" or "flow" |
| Before/After comparison cards with an arrow in between | Showing "change" or "difference" |
| Product UI screenshot + outlined device frame | Specific feature demonstrations |
| Big quote (half-page large type) | Emotion page / problem page / quotation page |
| Real-person avatar + quote cards (2×2 or 1×4) | User testimonials / usage scenarios |
| Big-type back cover + URL oval button | CTA / ending |

---

## ⚠️ Common pitfalls (moxt field summary)

### 1. Emoji do not render during Chromium / Playwright export

Chromium does not ship a color emoji font by default, so emoji show as empty boxes in `page.pdf()` or `page.screenshot()`.

**Countermeasure**: replace them with Unicode text symbols (`✦` `✓` `✕` `→` `·` `—`), or switch to plain text directly ("Email · 23" instead of "📧 23 emails").

### 2. `export_deck_pdf.mjs` errors with `Cannot find package 'playwright'`

Cause: ESM module resolution looks upward from the script's location for `node_modules`. The script is in `~/.claude/skills/huashu-design/scripts/`, which has no dependencies.

**Countermeasure**: copy the script into the deck project directory (e.g. `brochure/build-pdf.mjs`), run `npm install playwright pdf-lib` at the project root, then `node build-pdf.mjs --slides slides --out output/deck.pdf`.

### 3. Screenshot taken before Google Fonts finish loading → Chinese displays in the system default sans-serif

Before a Playwright screenshot/PDF, wait at least `wait-for-timeout=3500` so webfonts can download and paint. Or self-host the fonts in `shared/fonts/` to reduce network dependency.

### 4. Imbalanced information density: too much stuffed into a content page

The first version of the moxt philosophy page used 2×2 = 4 paragraphs + 3 creeds at the bottom = 7 blocks of content, crowded and repetitive. After changing to 1×3 = 3 paragraphs, the breathing room returned immediately.

**Countermeasure**: keep each page to "1 core message + 3-4 supporting points + 1 visual protagonist"; if it exceeds that, split into a new page. **Less is more**: the audience looks at a page for 10 seconds, and giving them 1 memorable point is easier to remember than 4.

---

## 🛑 Decide the architecture first: single file or multiple files?

**This choice is the first step of making slides, and getting it wrong causes repeated pitfalls. Read this whole section before starting.**

### Comparison of the two architectures

| Dimension | Single file + `deck_stage.js` | **Multiple files + `deck_index.html` stitcher** |
|------|--------------------------|--------------------------------------|
| Code structure | One HTML, every slide is a `<section>` | Each slide is a standalone HTML; `index.html` stitches them with iframes |
| CSS scope | ❌ Global; one page's styles may affect all pages | ✅ Naturally isolated; each iframe has its own world |
| Verification granularity | ❌ Need JS goTo to switch to a page | ✅ A single page file can be opened in the browser with a double-click |
| Parallel development | ❌ One file; multiple agents editing will conflict | ✅ Multiple agents can build different pages in parallel, zero-conflict merges |
| Debugging difficulty | ❌ One CSS error breaks the whole deck | ✅ An error on one page only affects itself |
| Embedded interaction | ✅ Cross-page shared state is simple | 🟡 iframes need postMessage |
| Print PDF | ✅ Built in | ✅ The stitcher iterates iframes on beforeprint |
| Keyboard navigation | ✅ Built in | ✅ Built into the stitcher |

### Which to choose? (decision tree)

```
│ Ask: roughly how many pages will the deck have?
├── ≤10 pages, needs in-deck animation or cross-page interaction, pitch deck → single file
└── ≥10 pages, academic lecture, courseware, long deck, parallel multi-agent work → multiple files (recommended)
```

**Default to the multi-file path.** It is not an "alternative"; it is the **main path for long decks and team collaboration**. Reason: every advantage of the single-file architecture (keyboard navigation, printing, scale) is also available in multi-file, whereas the scope isolation and verifiability of multi-file cannot be recovered in single-file.

### Why is this rule so hard? (real incident record)

The single-file architecture once hit four pitfalls in a row while building the AI Psychology lecture deck:

1. **CSS specificity override**: `.emotion-slide { display: grid }` (specificity 10) beat `deck-stage > section { display: none }` (specificity 2), so all pages rendered simultaneously, stacked.
2. **Shadow DOM slot rule overridden by outer CSS**: `::slotted(section) { display: none }` could not stop the outer rule's override, and sections refused to hide.
3. **localStorage + hash navigation race**: after a refresh, instead of jumping to the hash position, it stayed at the old position recorded in localStorage.
4. **High verification cost**: you must use `page.evaluate(d => d.goTo(n))` to screenshot a page, which is twice as slow as a direct `goto(file://.../slides/05-X.html)` and often errors.

The root cause of all of them is the **single global namespace**; the multi-file architecture eliminates these problems at the physical level.

---

## Path A (default): multi-file architecture

### Directory structure

```
MyDeck/
├── index.html              # copied from assets/deck_index.html, edit the MANIFEST
├── shared/
│   ├── tokens.css          # shared design tokens (palette / type sizes / common chrome)
│   └── fonts.html          # <link> that imports Google Fonts (included by every page)
└── slides/
    ├── 01-cover.html       # every file is a complete 1920×1080 HTML
    ├── 02-agenda.html
    ├── 03-problem.html
    └── ...
```

### Template skeleton for each slide

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>P05 · Chapter Title</title>
<link href="https://fonts.googleapis.com/css2?family=..." rel="stylesheet">
<link rel="stylesheet" href="../shared/tokens.css">
<style>
  /* Styles unique to this page. Any class name will not pollute other pages. */
  body { padding: 120px; }
  .my-thing { ... }
</style>
</head>
<body>
  <!-- 1920×1080 content (locked by the body width/height in tokens.css) -->
  <div class="page-header">...</div>
  <div>...</div>
  <div class="page-footer">...</div>
</body>
</html>
```

**Key constraints**:
- `<body>` is the canvas; lay out directly on it. Do not wrap in `<section>` or any other wrapper.
- `width: 1920px; height: 1080px` is locked by the `body` rule in `shared/tokens.css`.
- Include `shared/tokens.css` for shared design tokens (palette, type sizes, page-header/footer, etc.).
- Each page writes its own font `<link>` (importing fonts separately is cheap, and it guarantees each page can be opened independently).

### The stitcher: `deck_index.html`

**Copy directly from `assets/deck_index.html`.** You only need to change one place, the `window.DECK_MANIFEST` array, listing all slide file names and human-readable labels in order:

```js
window.DECK_MANIFEST = [
  { file: "slides/01-cover.html",    label: "Cover" },
  { file: "slides/02-agenda.html",   label: "Agenda" },
  { file: "slides/03-problem.html",  label: "Problem Statement" },
  // ...
];
```

The stitcher has built in: keyboard navigation (←/→/Home/End/number keys/P to print), scale + letterbox, bottom-right counter, localStorage memory, hash page jumping, print mode (iterates iframes and outputs the PDF page by page).

#### Two overview modes (adaptive + pitfall-proofed, rewritten 2026-06)

Opening the deck defaults to the **overview**. When the user does not specify, it is chosen randomly by seconds: **grid 60% / infinite gallery 40%** (can be fixed with the URL `?ov=grid|gallery` or `window.DECK_OVERVIEW='grid'|'gallery'`).

- **Grid (the default workhorse)**: uses **iframes to render the real sub-pages** (sharp, WYSIWYG, no thumbnails needed). **Adaptive**: if it fits on one screen → diagonally tilted, centered, filling the screen; if there are too many pages to fit → cards keep a comfortable size and **scroll vertically** (never cram dozens of pages onto one screen shrunk to postage stamps).
- **Infinite gallery**: all pages are **seamlessly and infinitely tiled + slow drift + slight breathing zoom**; one tile contains all pages (shuffled layout; pages repeat only after all pages have been shown). With many tiles, it **must use `<img>` thumbnails** to carry performance (see below), falling back to iframes when there is no thumb.

🛑 **Three hard constraints from the field (must read before changing this file, otherwise you will repeat the mistakes)**:
1. **Never build the overview wall as a card wall using `transform-style: preserve-3d`**. In a preserve-3d 3D scene, browser hit-testing for "cards receding backwards" (the top row) is unreliable → the top row cannot be clicked and the middle row works intermittently. **The right solution**: treat the whole wall as a **single plane tilted in 3D** (do not enable preserve-3d), with all cards coplanar, so clicks back-project onto one plane → reliable. Use 2D `scale` for hover, not `translateZ`.
2. **Must adapt to any page count**: fixed column counts plus a hard-coded strong tilt on the whole wall overflows, collapses corners, and distorts perspective once there are many pages. You must compute the column count from page count + viewport, flatten the tilt when there are many rows, and scroll when it does not fit on one screen.
3. **Do not make thumbnail resolution too low**: gallery thumbnails < 1000px look blurry when enlarged on hover. Default is 1600px.

**Generate thumbnails for the gallery**: use `scripts/gen_deck_thumbs.mjs` (playwright screenshots each page + sharp downsampling):
```bash
npm install playwright sharp
node gen_deck_thumbs.mjs --slides slides --out thumbs --width 1600
```
Then add `thumb: "thumbs/<same-name>.jpg"` to each MANIFEST entry. Grid mode ignores thumb (always iframe); only gallery mode uses it.

### Single-page verification (the killer advantage of the multi-file architecture)

Every slide is a standalone HTML. **After finishing one, double-click to open it in the browser and look**:

```bash
open slides/05-personas.html
```

Playwright screenshots also just `goto(file://.../slides/05-personas.html)` directly, with no JS page jumping and no interference from other pages' CSS. This brings the cost of the "change a bit, verify a bit" workflow close to zero.

### Parallel development

Split each slide's task among different agents running at the same time. The HTML files are independent of each other, so there are no conflicts when merging. For a long deck, this parallel approach can cut production time to 1/N.

### What `shared/tokens.css` should contain

Only put in things that are **truly shared across pages**:

- CSS variables (palette, type-size scale, spacing scale)
- Canvas locking such as `body { width: 1920px; height: 1080px; }`
- Chrome that every page uses identically, such as `.page-header` / `.page-footer`

**Do not** put single-page layout classes in it; that would regress to the global pollution problem of the single-file architecture.

---

## Path B (small deck): single file + `deck_stage.js`

Suited to ≤10 pages, needing cross-page shared state (for example a React tweaks panel that must control all pages), or extremely compact scenarios such as a pitch deck demo.

### Basic usage

1. Read the contents from `assets/deck_stage.js` and embed them in the HTML `<script>` (or `<script src="deck_stage.js">`)
2. Wrap slides in `<deck-stage>` in the body
3. 🛑 **The script tag must be placed after `</deck-stage>`** (see the hard constraint below)

```html
<body>

  <deck-stage>
    <section>
      <h1>Slide 1</h1>
    </section>
    <section>
      <h1>Slide 2</h1>
    </section>
  </deck-stage>

  <!-- ✅ Correct: script after deck-stage -->
  <script src="deck_stage.js"></script>

</body>
```

### 🛑 Script placement hard constraint (a real pitfall from 2026-04-20)

**Do not put `<script src="deck_stage.js">` in `<head>`.** Even though it can define `customElements` in `<head>`, the parser triggers `connectedCallback` as soon as it parses the `<deck-stage>` start tag. At that point the child `<section>` elements have not been parsed yet, `_collectSlides()` gets an empty array, the counter shows `1 / 0`, and all pages render stacked at the same time.

**Three compliant ways** (pick any one):

```html
<!-- ✅ Most recommended: script after </deck-stage> -->
</deck-stage>
<script src="deck_stage.js"></script>

<!-- ✅ Also fine: script in head but with defer -->
<head><script src="deck_stage.js" defer></script></head>

<!-- ✅ Also fine: module scripts are deferred by nature -->
<head><script src="deck_stage.js" type="module"></script></head>
```

`deck_stage.js` itself already has a built-in `DOMContentLoaded` deferred-collection defense, so even if the script is placed in head it will not blow up completely, but `defer` or placing it at the bottom of body is still the cleaner approach and avoids relying on the defensive branch.

### ⚠️ CSS traps of the single-file architecture (must read)

The most common pitfall of the single-file architecture is **the `display` property being stolen by single-page styles**.

Common wrong pattern 1 (writing display: flex directly on the section):

```css
/* ❌ External CSS specificity 2 overrides the shadow DOM's ::slotted(section){display:none} (also 2) */
deck-stage > section {
  display: flex;            /* all pages will render stacked at the same time! */
  flex-direction: column;
  padding: 80px;
  ...
}
```

Common wrong pattern 2 (the section has a higher-specificity class):

```css
.emotion-slide { display: grid; }   /* specificity: 10, even worse */
```

Both make **all slides render stacked at the same time**. The counter may show `1 / 10` and pretend to be normal, but visually page 1 covers page 2 covers page 3.

### ✅ Starter CSS (copy at the start to avoid the pitfall)

**The section itself** only handles "visible/invisible"; **layout (flex/grid etc.) goes on `.active`**:

```css
/* section only defines general non-display styles */
deck-stage > section {
  background: var(--paper);
  padding: 80px 120px;
  overflow: hidden;
  position: relative;
  /* ⚠️ Do not write display here! */
}

/* Lock "hidden unless active": double insurance of specificity + weight */
deck-stage > section:not(.active) {
  display: none !important;
}

/* Only the active page gets the needed display + layout */
deck-stage > section.active {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* Print mode: all pages must show, overriding :not(.active) */
@media print {
  deck-stage > section { display: flex !important; }
  deck-stage > section:not(.active) { display: flex !important; }
}
```

Alternative: **put the single page's flex/grid on an inner wrapper `<div>`**, so the section itself is always just a `display: block/none` switch. This is the cleanest approach:

```html
<deck-stage>
  <section>
    <div class="slide-content flex-layout">...</div>
  </section>
</deck-stage>
```

### Custom size

```html
<deck-stage width="1080" height="1920">
  <!-- 9:16 portrait -->
</deck-stage>
```

---

## Slide Labels

Both Deck_stage and deck_index label each page (shown in the counter). Give them **more meaningful** labels:

**Multi-file**: write `{ file, label: "04 Problem Statement" }` in the `MANIFEST`
**Single-file**: add `<section data-screen-label="04 Problem Statement">` on the section

**Key: slide numbering starts at 1, not 0**.

When the user says "slide 5", they mean the 5th slide, never the array position `[4]`. Humans do not speak 0-indexed.

---

## Speaker Notes

**Not added by default**; add only when the user explicitly asks.

With speaker notes you can reduce the text on the slide to a minimum and focus on impactful visuals, since the notes carry the full script.

### Format

**Multi-file**: write this in the `<head>` of `index.html`:

```html
<script type="application/json" id="speaker-notes">
[
  "Script for slide 1...",
  "Script for slide 2...",
  "..."
]
</script>
```

**Single-file**: same location as above.

### Key points for writing notes

- **Complete**: not an outline, but the words you will actually say
- **Conversational**: like everyday speech, not written language
- **Corresponding**: the Nth array entry corresponds to the Nth slide
- **Length**: 200-400 characters (Chinese) per slide is best
- **Emotional line**: mark stress, pauses, and emphasis points

---

## Slide design patterns

### 1. Establish a system (mandatory)

After exploring the design context, **first state out loud the system you will use**:

```markdown
Deck system:
- Background colors: at most 2 (90% white + 10% dark section dividers)
- Typefaces: Instrument Serif for display, Geist Sans for body
- Rhythm: section dividers use full-bleed color + white text, regular slides on a white background
- Imagery: hero slides use full-bleed photos, data slides use charts

I'll build to this system; tell me if you have concerns.
```

Proceed only after the user confirms.

### 2. Common slide layouts

- **Title slide**: solid background + huge title + subtitle + author/date
- **Section divider**: colored background + chapter number + chapter title
- **Content slide**: white background + title + 1-3 bullet points
- **Data slide**: title + large chart/number + short explanation
- **Image slide**: full-bleed photo + small caption at the bottom
- **Quote slide**: whitespace + huge quote + attribution
- **Two-column**: left-right comparison (vs / before-after / problem-solution)

Use at most 4-5 layouts in one deck.

### 3. Scale (emphasized again)

- Minimum body text **24px**, ideally 28-36px
- Titles **60-120px**
- Hero text **180-240px**
- Slides are meant to be read from 10 meters away, so the text must be large enough

### 4. Visual rhythm

A deck needs **intentional variety**:

- Color rhythm: mostly white backgrounds + occasional colored section dividers + occasional dark segments
- Density rhythm: a few text-heavy slides + a few image-heavy slides + a few quote slides with whitespace
- Type-size rhythm: normal titles + occasional giant hero text

**Do not make every slide look the same**. That is a PPT template, not design.

### 5. Spatial breathing (must read for data-dense pages)

**The pitfall beginners fall into most easily**: stuffing every piece of information that can fit onto one page.

Information density ≠ effective information delivery. Academic/speech decks especially need restraint:

- List/matrix pages: do not draw all N elements at the same size. Use **primary/secondary layering**: enlarge the 5 you will discuss today as the protagonists, and shrink the remaining 16 into background hints.
- Big-number pages: the number itself is the visual protagonist. Captions around it should not exceed 3 lines, otherwise the audience's eyes bounce back and forth.
- Quote pages: leave whitespace between the quote and the attribution; do not stick them together.

Run two self-checks, "is the data the protagonist" and "is the text crowded together", and keep adjusting until the whitespace makes you slightly uneasy.

---

## Printing to PDF

**Multi-file**: `deck_index.html` already handles the `beforeprint` event and outputs the PDF page by page.

**Single-file**: `deck_stage.js` handles it as well.

The print styles are already written; no extra `@media print` CSS is needed.

---

## Exporting to PPTX / PDF (self-service scripts)

HTML-first is the first-class citizen. But users often need PPTX/PDF delivery. Two general-purpose scripts are provided, **usable with any multi-file deck**, located under `scripts/`:

### `export_deck_pdf.mjs`: export a vector PDF (multi-file architecture)

```bash
node scripts/export_deck_pdf.mjs --slides <slides-dir> --out deck.pdf
```

**Features**:
- Text **stays vector** (copyable, searchable)
- Visuals 100% faithful (Playwright's embedded Chromium renders then prints)
- **No need to change a single word of the HTML**
- Each slide gets its own `page.pdf()`, then they are merged with `pdf-lib`

**Dependencies**: `npm install playwright pdf-lib`

**Limitation**: the PDF text can no longer be edited; to change it, go back to the HTML.

### `export_deck_stage_pdf.mjs`: dedicated to the single-file deck-stage architecture ⚠️

**When to use**: the deck is a single HTML file + the `<deck-stage>` web component wrapping N `<section>` elements (the Path B architecture). In that case the "one `page.pdf()` per HTML file" approach of `export_deck_pdf.mjs` does not work, and this dedicated script is needed.

```bash
node scripts/export_deck_stage_pdf.mjs --html deck.html --out deck.pdf
```

**Why export_deck_pdf.mjs cannot be reused** (record of a real pitfall on 2026-04-20):

1. **Shadow DOM beats `!important`**: deck-stage's shadow CSS has `::slotted(section) { display: none }` (only the active one gets `display: block`). Even using `@media print { deck-stage > section { display: block !important } }` in the light DOM cannot override it: after `page.pdf()` triggers the print media, Chromium's final render has only the active one, so **the whole PDF has only 1 page** (the current active slide repeated).

2. **Looping goto per page still yields only 1 page**: the intuitive solution of "navigate to each `#slide-N` once and then `page.pdf({pageRanges:'1'})`" also fails, because the print CSS outside the shadow DOM also has a `deck-stage > section { display: block }` rule that gets overridden, so the final render is always the first item in the section list (not the page you navigated to). The result: 17 loop iterations produce 17 copies of the P01 cover.

3. **Absolute children spill onto the next page**: even if all sections are made to render, if the section itself is `position: static`, its absolutely positioned `cover-footer`/`slide-footer` is positioned relative to the initial containing block. When the section is forced to 1080px height by print, the absolute footer may be pushed onto the next page (shown as the PDF having 1 more page than the number of sections, with the extra page containing only an orphaned footer).

**Fix strategy** (already implemented in the script):

```js
// After opening the HTML, use page.evaluate to lift the sections out of the deck-stage slot
// and attach them directly under an ordinary div in the body, with inline styles ensuring position:relative + fixed size
await page.evaluate(() => {
  const stage = document.querySelector('deck-stage');
  const sections = Array.from(stage.querySelectorAll(':scope > section'));
  document.head.appendChild(Object.assign(document.createElement('style'), {
    textContent: `
      @page { size: 1920px 1080px; margin: 0; }
      html, body { margin: 0 !important; padding: 0 !important; }
      deck-stage { display: none !important; }
    `,
  }));
  const container = document.createElement('div');
  sections.forEach(s => {
    s.style.cssText = 'width:1920px!important;height:1080px!important;display:block!important;position:relative!important;overflow:hidden!important;page-break-after:always!important;break-after:page!important;background:#F7F4EF;margin:0!important;padding:0!important;';
    container.appendChild(s);
  });
  // Disable the page break on the last page to avoid a trailing blank page
  sections[sections.length - 1].style.pageBreakAfter = 'auto';
  sections[sections.length - 1].style.breakAfter = 'auto';
  document.body.appendChild(container);
});

await page.pdf({ width: '1920px', height: '1080px', printBackground: true, preferCSSPageSize: true });
```

**Why this works**:
- Pulling the sections out of the shadow DOM slot into an ordinary div in the light DOM completely bypasses the `::slotted(section) { display: none }` rule
- Inline `position: relative` makes absolute children position relative to the section, so they do not overflow
- `page-break-after: always` makes the browser put each section on its own page when printing
- The `:last-child` no-break avoids a trailing blank page

**When verifying with `mdls -name kMDItemNumberOfPages`**: macOS Spotlight metadata is cached; after the PDF is rewritten you must run `mdimport file.pdf` to force a refresh, otherwise it shows the old page count. Counting the files with `pdfinfo` or `pdftoppm` gives the true count.

---

### `export_deck_pptx.mjs`: export editable PPTX

```bash
# The only mode: text boxes are natively editable (fonts fall back to system fonts)
node scripts/export_deck_pptx.mjs --slides <dir> --out deck.pptx
```

How it works: `html2pptx` reads computedStyle element by element and translates the DOM into PowerPoint objects (text frame / shape / picture). Text becomes real text boxes that can be edited by double-clicking in PowerPoint.

**Hard constraints** (the HTML must satisfy them, otherwise that page is skipped; see `references/editable-pptx.md` for details):
- All text must be in `<p>`/`<h1>`-`<h6>`/`<ul>`/`<ol>` (no bare-text divs)
- `<p>`/`<h*>` tags themselves cannot have background/border/shadow (put them on an outer div)
- Do not use `::before`/`::after` to insert decorative text (pseudo-elements cannot be extracted)
- Inline elements (span/em/strong) cannot have margin
- Do not use CSS gradients (cannot be rendered)
- Do not use `background-image` on divs (use `<img>`)

The script has a built-in **automatic preprocessor** that wraps "bare text in leaf divs" into `<p>` (keeping the class). This resolves the most common violation (bare text). But other violations (border on p, margin on span, etc.) still require the HTML source to be compliant.

**Font fallback caveat**:
- Playwright measures text-box sizes using webfonts; PowerPoint/Keynote render with local fonts
- When the two differ, there will be **overflow or misalignment**, so every page needs a visual check
- Recommended: install the fonts used in the HTML on the target machine, or fall back to `system-ui`

**Do not take this path for visual-first scenarios** → use `export_deck_pdf.mjs` to output a PDF instead. PDF is 100% visually faithful, vector, cross-platform, and text-searchable. It is the real home of visual-first decks, not some "non-editable compromise".

### Make the HTML export-friendly from the start

For the most reliable deck: **write the HTML to the editable 4 hard constraints from the start**. Then `export_deck_pptx.mjs` can pass everything directly. The extra cost is small:

```html
<!-- ❌ Bad -->
<div class="title">Key Findings</div>

<!-- ✅ Good (wrapped in p, class inherited) -->
<p class="title">Key Findings</p>

<!-- ❌ Bad (border on p) -->
<p class="stat" style="border-left: 3px solid red;">41%</p>

<!-- ✅ Good (border on the outer div) -->
<div class="stat-wrap" style="border-left: 3px solid red;">
  <p class="stat">41%</p>
</div>
```

### When to choose which

| Scenario | Recommended |
|------|------|
| Archiving for the organizer / records | **PDF** (universal, high fidelity, searchable text) |
| Sending to collaborators so they can fine-tune text | **PPTX editable** (accept font fallback) |
| Live talk, no content changes | **PDF** (vector fidelity, cross-platform) |
| HTML is the preferred presentation medium | Play directly in the browser; export is just a backup |

## Deep path to export editable PPTX (long-term projects only)

If your deck will be maintained long-term, revised repeatedly, and collaborated on by a team, it is recommended to **write the HTML to the html2pptx constraints from the start**, so `export_deck_pptx.mjs` can pass everything directly. See `references/editable-pptx.md` for details (4 hard constraints + HTML template + quick reference of common errors + fallback flow for existing visual drafts).

---

## FAQ

**Multi-file: a page in the iframe will not open / white screen**
→ Check that the `file` path in the `MANIFEST` is correct relative to `index.html`. Use browser DevTools to see whether the iframe's src can be accessed directly.

**Multi-file: a page's styles conflict with another page's**
→ Impossible (iframe isolation). If it feels like a conflict, it is the cache; force-refresh with Cmd+Shift+R.

**Single-file: multiple slides render stacked at the same time**
→ A CSS specificity problem. See the section "CSS traps of the single-file architecture" above.

**Single-file: scaling looks wrong**
→ Check that all slides are attached directly under `<deck-stage>` as `<section>`. No `<div>` may be wrapped in between.

**Single-file: want to jump to a specific slide**
→ Add a hash to the URL: `index.html#slide-5` jumps to slide 5.

**Applies to both architectures: text position is inconsistent across different screens**
→ Use a fixed size (1920×1080) and `px` units; do not use `vw`/`vh` or `%`. Scaling is handled uniformly.

---

## Verification checklist (must pass after finishing the deck)

1. [ ] Open `index.html` (or the main HTML) directly in the browser; check that the first page has no broken images and fonts are loaded
2. [ ] Press the → key to go through every page; no blank pages, no layout misalignment
3. [ ] Press the P key for print preview; each page is exactly one A4 sheet (or 1920×1080) with no cropping
4. [ ] Pick 3 random pages and force-refresh with Cmd+Shift+R; localStorage memory works normally
5. [ ] Batch screenshots with Playwright (multi-file architecture: iterate `slides/*.html`; single-file architecture: switch with goTo), and review them by eye
6. [ ] Search for leftover `TODO` / `placeholder` and confirm all have been cleaned up
