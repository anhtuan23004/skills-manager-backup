# Visual-Draft HTML → Editable PPTX: Read the Rendered Result, Do Not Change the HTML

`references/editable-pptx.md` covers **the html2pptx path**: the HTML is written to the 4 hard constraints from the very first line,
and can be converted only after it is written that way. That document contains a conclusion: "**never force-run html2pptx on freely written visual HTML**;
field-tested pass rate < 30%", and gives two fallbacks: output a PDF, or rewrite an editable HTML version.

**This document covers the third path, which makes that fallback unnecessary.**

The core difference in one sentence: **html2pptx reads the source; this script reads the coordinates after the browser has rendered.**
Flex, centering, and auto-wrapping have all already been computed by the browser into absolute positions, so patterns like "bare text in a div", "used flex",
and "background on a p" are simply not a problem: in the eyes of `getBoundingClientRect` they are all just a rectangle.

---

## Pick the path first: choose one of three

| Situation | Which path | Why |
|---|---|---|
| **HTML not yet written**, you are building the deck from scratch | `scripts/html2pptx.js` (see `editable-pptx.md`) | A PPTX written to the 4 constraints has the cleanest structure; text-box merging and paragraph hierarchy are better for later editing |
| **HTML already written**, and visually driven (flex / centering / bare text / background images / SVG charts) | **`scripts/pptx_from_rendered.py` (this document)** | Converts directly with zero rework. Rewriting 20 pages of HTML to fit the constraints costs far more than measuring directly |
| **Client requires "you must use our template"** | **Only this path works** | pptxgenjs creates files from scratch and cannot use an existing pptx as a base to inherit its master; python-pptx can |

⚠️ **Do not mix the two paths in the same project.** Pick one and follow it through, otherwise the two coordinate systems will clash.

---

## Usage

```bash
python3 scripts/pptx_from_rendered.py deck.html -o deck.pptx --selector ".slide"
```

When inheriting the client's official template (the most common commercial-project scenario):

```bash
python3 scripts/pptx_from_rendered.py deck.html -o deck.pptx \
    --selector ".slide" \
    --template client-template.pptx \
    --layout "Content page" \
    --skip-class logo \
    --bg 05070B
```

(`client-template.pptx` is the client's official template; `--layout` takes the name of a layout inside that template, here the content-page layout. Both are example values.)

Dependencies: `playwright` (including chromium), `python-pptx`, `Pillow`.
Adding `--dump-json dom.json` writes the list of measured elements to disk, which is very useful when troubleshooting position problems.

---

## Inheriting the client template: so that when they change the master, it takes effect everywhere

The most common reason for rework in commercial projects is not "it doesn't look good"; it is "**you didn't use our template**".
When the client says this, they usually want two specific things: ① the logo is the latest version;
② **when they change the master, your pages change along with it**.

A PPT with one full-page image per slide can do neither; even if made into text boxes, a file built from scratch with pptxgenjs
does not have their master. The approach is to use their `.pptx` as the base:

1. Open it with `Presentation(client_template.pptx)`
2. **Delete the sample slides that come with the template**, leaving the master / layouts / theme / palette untouched (`strip_slides`)
3. For each page, `add_slide(official_layout)`, and delete from the page the empty placeholders the layout brings
4. **Do not draw common elements such as the logo into the content layer**; let the layout provide them. During rendering use `--skip-class logo`
   to skip the logo in the HTML, so only your content remains on the page and the logo comes from the layout.
   That way, when the client changes the master/layout, all pages change along with it.

⚠️ **Pitfall: a layout may hide a full-screen solid-color rectangle** with the same color and size as the layout's background (a redundant mask).
If kept, anything placed below it on the page is blocked. The script's `unblock_layout` deletes it,
and deleting it does not change the layout's appearance.

**The canvas size follows the template; do not follow the 960×540pt of `editable-pptx.md`.** Whatever size the client template is (26.67×15 inch has been encountered),
a size mismatch causes the whole thing to be scaled when merging files. The script automatically computes the scale ratio as
`slide width pt ÷ HTML canvas width px`; with an HTML canvas of 1920px and 1920pt, the ratio is exactly 1.0,
**1 CSS px = 1 PowerPoint pt**, no mental arithmetic needed.

---

## Six typesetting traps (each one has caused trouble)

`editable-pptx.md` does not cover any of these, because it assumes the HTML is newly written to the constraints.
When reading rendered results, every one of the following will directly wreck the output if left unhandled:

### 1. Line breaks and indentation in the HTML source become real line breaks in the PPTX

```html
<div>
    <em>68</em>
    <span>projects, and I set up daily data collection for all of them</span>
</div>
```

The line breaks and indentation between tags are **real text nodes**. The browser collapses them under `white-space:normal`
(consecutive whitespace → one space, leading and trailing whitespace dropped), but PPTX has no such rule: that `\n` is carried over as is,
and in PowerPoint it becomes a real line break, pushing the rest of the text to the next line and covering other elements.

**Fix**: perform HTML whitespace collapsing at extraction time, and discard runs that are empty after collapsing.

### 2. A container's font-size is often inherited, so you cannot use it to compute margins and line spacing

The `computedStyle.fontSize` of the div above may be only 16px (inherited from body),
while inside it is a number at 132px. Computing the text-box margin and line spacing from 16px is all wrong.

**Fix**: take the base font size as the **largest** font size among the `runs`.

### 3. Counting lines cannot dedupe by the rectangle's top

`Range.getClientRects()` returns multiple rectangles for runs of different font sizes on the same line. Their baselines are aligned,
but their top edges differ a lot. Deduplicating by `top` counts one line as several lines (in a field test one line was counted as 4 lines).

**Fix**: cluster by whether the y intervals overlap.

### 4. Multiple paragraphs of different font sizes in one box cannot share the same line spacing

PowerPoint line spacing is **paragraph-level**, while visual drafts often put lines of different font sizes in the same div:

```html
<div>The one I invested the most in<br>Worked on it for over a week, 40,000 lines of code<br><em class="big">Never got it running</em></div>
```

Applying one line spacing to the whole box stretches the small-text lines and squeezes the large-text line; in a field test adjacent lines
overlapped directly.

**Fix**: **split into paragraphs by `<br>`, with each paragraph becoming its own text box**, each with its own position and line height.
The number of text boxes increases (137 → 175 in a field test), but this is the necessary price of correctness.

### 5. A shrink-wrapped flex box has zero margin, and the last character drops to the next line

A flex child with `align-items:center` shrinks its width to the actual text width, with **no margin at all**.
In PowerPoint, as soon as the font metrics differ slightly, the last character is pushed to the next line
(in field tests the last character dropped in cases like "⋯⋯被用起来了" [the final "了"] and "稀缺的是判断力" [the final "力"]).

**Fix**: measure whether this passage actually wrapped in the HTML; if it was originally a single line, **turn off auto-wrap directly in the PPT**
(`word_wrap = False`), which makes wrapping impossible at the root. In field tests, 150 of 175 boxes belonged to this category.

### 6. Do not set exact line spacing for single-line paragraphs

The measured line-box height is larger than the actual line spacing (that is the **font line box**, not the CSS line spacing; 185 vs 148 in a field test).
Using it as exact line spacing pushes the text down overall.

**Fix**: set line spacing only for paragraphs that "wrapped by themselves"; leave single-line paragraphs to PowerPoint to lay out naturally by font size,
with text flush to the top of the box, which turns out to be the most accurate in position.

---

## 🔴 Verification: verify your verification tool first

**This is the biggest lesson of this path, worth more than all the technical details above.**

The same PPTX can produce completely different results in different renderers. With the wrong tool, traps 1, 3, 4, and 6 above
**will not be exposed at all**: all 20 pages look right, and the moment the client opens it, things overlap.

| Tool | Trustworthy? | Notes |
|---|---|---|
| **macOS `qlmanage -t` thumbnails** | ❌ **No** | Uses a simplified rendering path and is far more lenient on line spacing than real PowerPoint. In a field test it let through 4 bugs that cause text overlap |
| **LibreOffice (macOS)** | ⚠️ Layout is trustworthy, Chinese may be lost entirely | It cannot access macOS's system Chinese fonts, so it renders tofu blocks or even blanks |
| **Keynote + AppleScript** | ✅ **First choice for automation** | Real presentation-engine layout; can be scripted to export a PDF and then output images page by page |
| **Open in WPS / PowerPoint** | ✅ **Final confirmation** | The client mostly uses this kind of software. Review manually |

**Keynote automation (the only fully automatic and trustworthy route on this machine)**:

```bash
osascript <<'EOF'
tell application "Keynote"
  activate
  set d to open POSIX file "/abs/path/deck.pptx"
  delay 4
  export d to POSIX file "/abs/path/out.pdf" as PDF
  close d saving no
  quit
end tell
EOF
pdftoppm -png -r 54 out.pdf page     # then compare page by page side by side with the original HTML
```

**To judge whether a renderer is trustworthy, use a control experiment**: feed the **client's original template file** to the same renderer.
If Chinese is also entirely lost when it renders the official template, it is an environment problem and not a problem with your file. This step saves
hours of troubleshooting in the wrong direction.

⚠️ **Do not use System Events to inject keystrokes to page through and screenshot.** The keys will land in whatever window the user is currently typing in.

**Also run a mechanical check** (independent of any renderer):

- Character-by-character text comparison: extract the text from the `--dump-json` list and from the generated pptx, and after `re.sub(r'\s+','')` they must be exactly equal
- Count comparison: image counts and shape counts must line up page by page

---

## Fonts: delivery font ≠ layout font

Client guidelines often specify a font you do not have locally (for example Microsoft YaHei, a commercial font distributed under Windows licensing).
**Do not change the HTML's `font-family` for it.** If it is not installed locally, the preview and PDF will fall back, and
**the layout goes off immediately** (in a field test a whole line of numbers was pushed to the next line).

The correct approach is to **keep the two sides separate**:

- HTML / PDF are laid out with fonts actually installed locally, WYSIWYG
- The PPTX carries the font name specified by the client guidelines (their machines have it)

**The precondition for separating them is that Chinese full-width characters are monospaced**: changing fonts does not change the number of characters per line or the line-break positions; the differences are only in Latin text and punctuation.
Chinese-dominant drafts can safely be separated; Latin-dominant drafts need separate verification.
