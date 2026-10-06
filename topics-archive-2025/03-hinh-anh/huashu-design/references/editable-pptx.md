# Editable PPTX Export: HTML Hard Constraints + Size Decision + Common Errors

This document covers the path that uses `scripts/html2pptx.js` + `pptxgenjs` to translate HTML element by element into truly editable PowerPoint text boxes. It is also the only path `export_deck_pptx.mjs` supports.

> ## 🔴 Pick the path first: this document covers only one of the two paths
>
> | Situation | Which path |
> |---|---|
> | **HTML not yet written**, building the deck from scratch | **This document** (write to the 4 hard constraints → `html2pptx.js`). Cleanest structure, best for later editing |
> | **HTML already written**, and visually driven (flex / centering / bare text / background images / SVG charts) | → `references/pptx-from-rendered-html.md` (reads rendered coordinates, **zero rework**) |
> | **Client requires "you must use our template"** | → same as above, **the only option**. pptxgenjs cannot use an existing pptx as a base to inherit its master |
>
> Do not mix the two paths in the same project. The 4 constraints below hold only for the path in this document.
> An already-written visual draft **does not need** to be rewritten into a compliant structure just to convert to PPTX.
>
> **Core premise**: to take this path, the HTML must be written to the 4 constraints below from the very first line. **Not "write first, convert later"**: patching up afterwards triggers 2-3 hours of rework (a real pitfall from the 2026-04-20 stock-option board project).

---

## Canvas size: use 960×540pt (LAYOUT_WIDE)

PPTX units are **inches** (physical size), not px. Decision principle: the body's computedStyle size must **match the inch size of the presentation layout** (±0.1", strictly checked by `validateDimensions` in `html2pptx.js`).

### Comparison of 3 candidate sizes

| HTML body | Physical size | Corresponding PPT layout | When to choose |
|---|---|---|---|
| **`960pt × 540pt`** | **13.333″ × 7.5″** | **pptxgenjs `LAYOUT_WIDE`** | ✅ **Default recommendation** (standard 16:9 for modern PowerPoint) |
| `720pt × 405pt` | 10″ × 5.625″ | Custom | Only when the user specifies an "old PowerPoint Widescreen" template |
| `1920px × 1080px` | 20″ × 11.25″ | Custom | ❌ A non-standard size on this path; text looks abnormally small when projected. ⚠️ But **when inheriting a client template, the canvas must follow the template** (26.67″×15″ has been encountered); for that path see `pptx-from-rendered-html.md` |

**Do not think of the HTML size as a resolution.** PPTX is a vector document; the body size determines the **physical size**, not the sharpness. An oversized body (20″×11.25″) will not make text sharper; it only makes the pt font size smaller relative to the canvas, which looks worse when projected/printed.

### Three equivalent ways to write the body

```css
body { width: 960pt;  height: 540pt; }    /* sharpest, recommended */
body { width: 1280px; height: 720px; }    /* equivalent, px habit */
body { width: 13.333in; height: 7.5in; }  /* equivalent, inch intuition */
```

Matching pptxgenjs code:

```js
const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';  // 13.333 × 7.5 inch, no custom layout needed
```

---

## 4 hard constraints (violations produce errors directly)

`html2pptx.js` walks the DOM once and, by tag and computed style, classifies each element as "text box / shape / image / ignored". The classification rules come from limitations of the PowerPoint file format itself, and projected onto HTML they become the 4 rules below. Run through them in your head while writing; it saves the time of fixing page by page after export.

### Rule 1: text cannot lie directly in a DIV; wrap it in `<p>` or `<h1>`-`<h6>`

```html
<!-- ❌ Wrong: text is a direct child text node of the div -->
<div class="metric">DAU 124,000, +8% MoM</div>

<!-- ✅ Correct: text wrapped in <p>/<h1>-<h6>; the div only handles positioning/background -->
<div class="metric"><p>DAU 124,000, +8% MoM</p></div>
```

**How it is judged**: the script checks whether the div's **direct child nodes** include a non-whitespace text node. Text nested in `<p>`/`<h1>`-`<h6>` does not count; only "text attached directly to the div" is a violation. The error includes the first 50 characters of the offending text (ending with `...` if longer), to make it easy to locate which passage.

**The same goes for span; it cannot stand alone**: span is an inline element, and the script treats it only as a local style override (bold, color change, underline) inside a `<p>`/`<h1>`-`<h6>`; it will not lift it out as a separate text box. To get a standalone editable piece of text, it must be wrapped in a `<p>`/`<h1>`-`<h6>`.

### Rule 2: CSS gradients are not supported (essentially a form of "background-image is not supported")

```css
/* ❌ Wrong: linear-gradient/radial-gradient both count as background-image */
.banner { background: linear-gradient(135deg, #FF6B6B, #4ECDC4); }

/* ✅ Correct: solid color */
.banner { background: #FF6B6B; }

/* ✅ To get a multi-color transition look, stagger several solid-color flex child blocks and simulate the gradient feel with opacity or color steps */
.banner { display: flex; }
.banner div { flex: 1; }
.banner .c1 { background: #FF6B6B; }
.banner .c2 { background: #FF9B6B; }
.banner .c3 { background: #4ECDC4; }
```

**Why**: the script's validation of a div only checks whether the computed `background-image` is `none`. As long as it is not `none`, whether it holds an image or a CSS gradient function, it is blocked (a gradient is essentially a special kind of background-image). Among PowerPoint's native shape fills, only solid color is stably supported by pptxgenjs; gradients need a separate set of OOXML structures that the toolchain has not implemented.

### Rule 3: background/border/shadow can only be attached to a DIV; text tags (including `<ul>`/`<ol>`) cannot have any

```html
<!-- ❌ Wrong: <h2> itself carries a background and rounded corners -->
<h2 style="background: #FFD700; border-radius: 6pt; padding: 6pt 10pt;">Key Conclusion</h2>

<!-- ✅ Correct: the outer div carries the background/border; <h2> only handles text -->
<div style="background: #FFD700; border-radius: 6pt; padding: 6pt 10pt;">
  <h2>Key Conclusion</h2>
</div>
```

**Why**: for every `<p>`/`<h1>`-`<h6>`/`<ul>`/`<ol>` (and the `<li>` absorbed inside them), the script first checks its own background/border/box-shadow separately. If any of the three is non-empty it errors immediately, without even considering whether it simultaneously hits other rules such as "placeholder" (a `class` containing `placeholder`); it is judged a violation outright. This check happens before all other classification, because in PowerPoint a "shape that can draw a background/border/shadow" and a "text frame that can hold text" are two different objects, and `<p>`/`<h*>` are translated only into the latter, leaving no place for the former's properties.

### Rule 4: DIV cannot use `background-image`; always use the `<img>` tag for images

```html
<!-- ❌ Wrong -->
<div style="background-image: url('trend.png'); width: 300pt; height: 200pt;"></div>

<!-- ✅ Correct -->
<img src="trend.png" style="position: absolute; left: 60pt; top: 80pt; width: 300pt; height: 200pt;" />
```

**Why**: the script generates image objects only from the (browser-resolved) absolute `src` of `<img>` elements; it does not parse the `url(...)` inside a div's `background-image` property at all. When this rule is hit, the script does not penalize the div's descendants: the `div` itself produces nothing, but any `<p>`/`<img>` etc. wrapped inside are still each processed separately; only that background image is lost. To overlay an image and text, place the `<img>` and the text layer as two independent elements and align them by positioning.

---

## Merging text boxes (`data-pptx-merge`)

**Default behavior**: each `<p>`/`<h1>`-`<h6>` in the HTML becomes an **independent text box** in the PPTX. Write 3 `<p>` in a card → 3 text boxes stacked in PPT; when editing you cannot press Enter to add a paragraph across the whole block, and must change the font size/alignment one by one.

**Solution**: add `data-pptx-merge="true"` to the outer div, and all `<p>/<h*>` in the container are merged into **one editable text box**, with paragraph separators between paragraphs, so in PPT you edit continuously paragraph by paragraph.

```html
<!-- ✅ Merged form: all 4 paragraphs in one text box -->
<div class="card" data-pptx-merge="true"
     style="position: absolute; top: 60pt; left: 60pt; width: 420pt;
            background: #1A4A8A; border-radius: 8pt; padding: 20pt 24pt;">
  <h2 style="font-size: 24pt; color: #FFFFFF;">Title</h2>
  <p  style="font-size: 14pt; color: #DDEEFF;">First paragraph of body text.</p>
  <p  style="font-size: 14pt; color: #FFD166;">Second paragraph: change the color for emphasis.</p>
  <p  style="font-size: 14pt; color: #DDEEFF;">Third paragraph: keep writing in the same text box.</p>
</div>
```

**Preserved styles** (written per paragraph as run options): `font-size`, `color`, `font-family`, `font-weight` (bold), `font-style` (italic), `text-decoration: underline`, and the inline styles of `<b>/<i>/<u>/<strong>/<em>/<span>`.

**Taken from the first paragraph and applied to the whole box**: `text-align`, `line-height`. Because PowerPoint's alignment and line spacing are at the paragraph/textbox level, one box can have only one alignment. If several paragraphs have different alignments, do not use merge; let them stay independent.

**The container's own `background`/`border`/`box-shadow`/`border-radius`** render as a shape as usual, behaving exactly like an ordinary div. That is, the blue card base + text is still the two layers "shape + text frame"; only the text layer collapses from 3-4 text boxes into 1.

**Limitations**:
- `data-pptx-merge` cannot be nested (it errors).
- The container cannot use `background-image` (same as Rule 4 of the 4 hard constraints).
- Do not place child divs with `background`/`border` inside the container. They are still rendered as independent shapes, but their text has already been merged away, which may cause visual misalignment.

**When to use**: scenarios where the content will be revised repeatedly and continue to be edited in PPT. For one-off export for archiving there is no need to add it; behavior is the same.

---

## Path A HTML template skeleton

One standalone HTML file per slide, with scopes isolated from each other (avoiding the CSS pollution of single-file decks).

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 960pt; height: 540pt;           /* ⚠️ matches LAYOUT_WIDE */
    font-family: system-ui, -apple-system, "PingFang SC", sans-serif;  /* PingFang SC = Apple's Chinese system font */
    background: #FEFEF9;                    /* solid color, no gradients */
    overflow: hidden;
  }
  /* DIV handles layout/background/border */
  .card {
    position: absolute;
    background: #1A4A8A;                    /* background on the DIV */
    border-radius: 4pt;
    padding: 12pt 16pt;
  }
  /* Text tags only handle font styling; no background/border */
  .card h2 { font-size: 24pt; color: #FFFFFF; font-weight: 700; }
  .card p  { font-size: 14pt; color: rgba(255,255,255,0.85); }
</style>
</head>
<body>

  <!-- Title area: outer div for positioning, inner text tags -->
  <div style="position: absolute; top: 40pt; left: 60pt; right: 60pt;">
    <h1 style="font-size: 36pt; color: #1A1A1A; font-weight: 700;">Titles are assertion sentences, not topic words</h1>
    <p style="font-size: 16pt; color: #555555; margin-top: 10pt;">Subtitle with supplementary explanation</p>
  </div>

  <!-- Content card: div handles the background, h2/p handle the text -->
  <div class="card" style="top: 130pt; left: 60pt; width: 240pt; height: 160pt;">
    <h2>Point One</h2>
    <p>Short explanatory text</p>
  </div>

  <!-- List: use ul/li, not manual • symbols -->
  <div style="position: absolute; top: 320pt; left: 60pt; width: 540pt;">
    <ul style="font-size: 16pt; color: #1A1A1A; padding-left: 24pt; list-style: disc;">
      <li>First key point</li>
      <li>Second key point</li>
      <li>Third key point</li>
    </ul>
  </div>

  <!-- Illustration: use the <img> tag, not background-image -->
  <img src="illustration.png" style="position: absolute; right: 60pt; top: 110pt; width: 320pt; height: 240pt;" />

</body>
</html>
```

---

## Quick reference of common errors

The error messages below are the strings output by `scripts/html2pptx.js` in this copy (translated to English; the upstream script printed them in Chinese). Messages are shortened here to their opening words.

| Error message | Cause | Fix |
|---------|------|---------|
| `<div> contains text written directly: "XXX"...` | Bare text in a div | Wrap the text in `<p>` or `<h1>`-`<h6>` |
| `<div> background cannot use a CSS gradient...` | Used linear/radial-gradient | Change to a solid color, or use flex children in segments |
| `Text tag <p> has background...set: background, border and shadow can only be applied to a <div>...` | A background color was added to the `<p>` tag | Wrap in a `<div>` to carry the background; `<p>` only holds text |
| `<div> cannot use background-image...` | The div used background-image | Change to an `<img>` tag |
| `Content overflows the page vertically by Xpt...` | Content exceeds 540pt | Reduce content or shrink font size, or truncate with `overflow: hidden` |
| `Page size mismatch: the HTML body is ... inches, the PPT layout is ... inches` | Body size does not match the pres layout | Use `960pt × 540pt` for body with `LAYOUT_WIDE`; or use defineLayout for a custom size |
| `Text box "XXX" is only ... inches from the bottom edge of the page; leave at least 0.5 inch` | A large-font `<p>` is < 0.5 inch from the bottom edge of the body | Move it up and leave enough bottom margin; the bottom of a PPT slide is partly covered anyway |

---

## Basic workflow (3 steps to PPTX)

### Step 1: write a standalone HTML per page following the constraints

```
MyDeck/
├── slides/
│   ├── 01-cover.html    # every file is a complete 960×540pt HTML
│   ├── 02-agenda.html
│   └── ...
└── illustration/        # all images referenced by <img>
    ├── chart1.png
    └── ...
```

### Step 2: write build.js to call `html2pptx.js`

```js
const pptxgen = require('pptxgenjs');
const html2pptx = require('../scripts/html2pptx.js');  // this skill's script

(async () => {
  const pres = new pptxgen();
  pres.layout = 'LAYOUT_WIDE';  // 13.333 × 7.5 inch, matches the HTML's 960×540pt

  const slides = ['01-cover.html', '02-agenda.html', '03-content.html'];
  for (const file of slides) {
    await html2pptx(`./slides/${file}`, pres);
  }

  await pres.writeFile({ fileName: 'deck.pptx' });
})();
```

### Step 3: open and check

- Open the exported PPTX in PowerPoint/Keynote
- Double-clicking any text should let you edit it directly (if it shows as an image, Rule 1 was violated)
- Verify overflow: each page should stay within the body bounds, with nothing cut off

---

## This path vs other options (when to choose which)

| Need | Choose |
|------|------|
| Colleagues will edit the text in the PPTX / sending to non-technical people to keep editing | **The path in this document** (editable; HTML must be written to the 4 constraints from the start) |
| Just for presenting / sending for archive, no more changes | `export_deck_pdf.mjs` (multi-file) or `export_deck_stage_pdf.mjs` (single-file deck-stage), outputting a vector PDF |
| Visual freedom first (animation, web components, CSS gradients, complex SVG), accepting non-editable | **PDF** (same as above). PDF is both faithful and cross-platform, more suitable than an "image PPTX" |

**Never force-run html2pptx on freely written visual HTML.** In field tests the pass rate of visually driven HTML is < 30%, and converting the rest page by page is slower than rewriting. In such scenarios, output a PDF rather than forcing a PPTX.

---

## Fallback: existing visual draft but the user insists on editable PPTX

Occasionally you hit this scenario: you/the user have already written a visually driven HTML (using gradients, web components, and complex SVG), and a PDF would be the best output, but the user says explicitly "No, it must be an editable PPTX".

**Do not force-run `html2pptx` expecting it to pass.** In field tests the pass rate of visually driven HTML on html2pptx is <30%, and the other 70% will error or look distorted.

> 🔴 **Since 2026-09, try the third path before considering A/B below**: `scripts/pptx_from_rendered.py` reads the coordinates
> **after the browser has rendered**, not the source, so visually driven HTML can be converted directly with zero rework (20 pages all passed in field tests),
> and the user does not have to choose between "losing visuals" and "losing editability". See `references/pptx-from-rendered-html.md`.
> A/B below should be raised only when that path also does not apply.

The correct fallback is:

### Step 1 · Tell them the limitations first (transparent communication)

Explain three things to the user in one passage:

> "Your current HTML uses [list specifically: gradients / web components / complex SVG / ...], and converting directly to editable PPTX will fail. I have two options:
> - A. **Output a PDF** (recommended): visuals 100% preserved; the recipient can view and print but cannot edit text
> - B. **Use the visual draft as a blueprint and rewrite an editable HTML version** (keeping the design decisions on color/layout/copy, but reorganizing the HTML structure to the 4 hard constraints, **sacrificing** visual capabilities such as gradients, web components, complex SVG) → then export editable PPTX
>
> Which do you choose?"

Do not play down option B; state clearly **what will be lost**. Let the user make the trade-off.

### Step 2 · If the user chooses B: the AI rewrites proactively; do not ask the user to write it

The doctrine here is: **the user gives design intent, and you translate it into a compliant implementation**. The user is not asked to learn the 4 hard constraints and rewrite it themselves.

Principles to follow when rewriting:
- **Keep**: color system (primary/secondary/neutral colors), information hierarchy (title/subtitle/body/annotation), core copy, layout skeleton (top-middle-bottom / left-right columns / grid), page rhythm
- **Downgrade**: CSS gradient → solid color or flex segments, web component → paragraph-level HTML, complex SVG → simplified `<img>` or solid-color geometry, shadow → delete or reduce to very faint, custom fonts → move toward system fonts
- **Rewrite**: bare text → wrap in `<p>` / `<h*>`, `background-image` → `<img>` tag, background/border on `<p>` → carried by an outer div

### Step 3 · Produce a comparison list (transparent delivery)

After the rewrite, give the user a before/after comparison so they know which visual details were simplified:

```
Original design → editable version adjustment
- Title area purple gradient → solid #5B3DE8 primary-color background
- Data card shadow → removed (replaced with a 2pt outline for separation)
- Complex SVG line chart → simplified to <img> PNG (generated from an HTML screenshot)
- Hero area web component animation → static first frame (web components cannot be translated)
```

### Step 4 · Export & dual-format delivery

- Run the `editable` HTML through `scripts/export_deck_pptx.mjs` to output the editable PPTX
- **Recommended: also keep** the original visual draft and run `scripts/export_deck_pdf.mjs` to output a high-fidelity PDF
- Deliver both formats to the user: the PDF of the visual draft + the editable PPTX, each with its own role

### When to flatly decline option B

In some scenarios the rewrite cost is too high, and you should persuade the user to give up on editable PPTX:
- The HTML's core value is animation or interaction (only a static first frame remains after the rewrite, losing 50%+ of the information)
- Page count > 30, so the rewrite cost exceeds 2 hours
- The visual design depends heavily on precise SVG / custom filters (the rewrite would be almost unrelated to the original)

In such cases tell the user: "The rewrite cost of this deck is too high; I suggest outputting a PDF rather than a PPTX. If the recipient really needs the pptx format, you would have to accept a much plainer look. Would you like to switch to PDF?"

---

## Why the 4 constraints are not a bug but a physical constraint

These 4 are not the laziness of the `html2pptx.js` author; they are the result of **constraints of the PowerPoint file format (OOXML) itself** projected onto HTML:

- Text in PPTX must live in a text frame (`<a:txBody>`), which corresponds to paragraph-level HTML elements
- In PPTX a shape and a text frame are two objects; you cannot both draw a background and write text on the same element
- PPTX shape fills have limited gradient support (only certain preset gradients; arbitrary-angle CSS gradients are not supported)
- A PPTX picture object must reference a real image file, not a CSS property

Once you understand this, **do not expect the tool to get smarter**: the HTML authoring must adapt to the PPTX format, not the other way around.
