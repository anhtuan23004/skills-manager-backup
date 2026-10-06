# Content Guidelines: Anti-AI-Slop, Content Rules, Scale Specs

The traps that AI design falls into most easily. This is a "what not to do" list, which matters more than "what to do", because AI slop is the default: if you do not actively avoid it, it will happen.

## Complete AI Slop Blacklist

### Visual Traps

**❌ Aggressive gradient backgrounds**
- Purple → pink → blue full-screen gradients (the typical flavor of AI-generated web pages)
- Rainbow gradients in any direction
- Mesh gradients covering the whole background
- ✅ If you must use a gradient: subtle, monochromatic, applied intentionally as an accent (e.g. button hover)

**❌ Rounded cards + left-border accent color**
```css
/* This is the typical signature of an AI-flavored card */
.card {
  border-radius: 12px;
  border-left: 4px solid #3b82f6;
  padding: 16px;
}
```
This kind of card is rampant in AI-generated dashboards. Want emphasis? Use more design-minded approaches: background color contrast, weight/size contrast, plain divider lines, or no cards at all.

**❌ Emoji decoration**
Unless the brand itself uses emoji (e.g. Notion, Slack), do not put emoji in the UI. **Especially avoid**:
- 🚀 ⚡️ ✨ 🎯 💡 before headings
- ✅ in feature lists
- → inside CTA buttons (a standalone arrow is OK; an emoji arrow is not)

If you have no icons, use a real icon library (Lucide/Heroicons/Phosphor), or use a placeholder.

**❌ Drawing imagery with SVG**
Do not try to draw people, scenes, devices, objects, or abstract art in SVG. AI-drawn SVG imagery reads as AI at a glance, childish and cheap. **A gray rectangle plus a text label "illustration slot 1200×800" is 100 times better than a clumsy SVG hero illustration**.

The only legitimate uses of SVG:
- Real icons (16×16 to 32×32 range)
- Geometric shapes as decorative elements
- Data viz charts

**❌ Too much iconography**
Not every heading / feature / section needs an icon. Overusing icons makes the interface feel like a toy. Less is more.

**❌ "Data slop"**
Made-up stats as decoration:
- "10,000+ happy customers" (you don't even know if that's true)
- "99.9% uptime" (don't write it without real data)
- Decorative "metric cards" composed of an icon + number + phrase
- Mock tables dressed up with fake data

If there is no real data, leave a placeholder or ask the user for it.

**❌ "Quote slop"**
Fabricated user testimonials and celebrity quotes used to decorate the page. Leave a placeholder and ask the user for real quotes.

### Typography Traps

**❌ Avoid these overused fonts**:
- Inter (the default of AI-generated web pages)
- Roboto
- Arial / Helvetica
- Pure system font stack
- Fraunces (AI discovered it and overused it)
- Space Grotesk (AI's recent favorite)

**✅ Use a distinctive display + body pairing**. Directions for inspiration:
- Serif display + sans-serif body (editorial feel)
- Mono display + sans body (technical feel)
- Heavy display + light body (contrast)
- Variable font for hero weight animation

Font resources:
- Lesser-known good options on Google Fonts (Instrument Serif, Cormorant, Bricolage Grotesque, JetBrains Mono)
- Open-source font sites (siblings of Fraunces, Adobe Fonts)
- Do not invent font names out of thin air

### Color Traps

**❌ Inventing colors out of thin air**
Do not design a whole unfamiliar color scheme from scratch. It is usually not harmonious.

**✅ Strategy**:
1. Have a brand color → use the brand color, and interpolate missing color tokens with oklch
2. No brand color but a reference → sample colors from screenshots of the reference product
3. Completely from scratch → pick a known color system (Radix Colors / Tailwind default palette / Anthropic brand); do not tune your own

**Defining colors with oklch** is the most modern approach:
```css
:root {
  --primary: oklch(0.65 0.18 25);      /* warm terracotta */
  --primary-light: oklch(0.85 0.08 25); /* lighter shade of the same hue */
  --primary-dark: oklch(0.45 0.20 25);  /* darker shade of the same hue */
}
```
oklch guarantees the hue does not drift when you adjust lightness, which makes it better than hsl.

**❌ Casually adding inverted colors for night mode**
Dark mode is not simply inverting colors. A good dark mode requires re-tuning saturation, contrast, and accent colors. If you do not want to do dark mode properly, do not do it.

### Layout Traps

**❌ Bento grid overuse**
Every AI-generated landing page wants a bento. Unless your information structure genuinely suits bento, use another layout.

**❌ Big hero + 3-column features + testimonials + CTA**
This landing page template has been overused to death. If you want to innovate, really innovate.

**❌ Every card in a card grid looks identical**
Asymmetric, differently sized cards, some with an image and some with only text, some spanning columns: that is what real designers' work looks like.

## Content Guidelines

### 1. Don't add filler content

Every element must earn its place. Empty space is a design problem, solved with **composition** (contrast, rhythm, whitespace), **not** by filling it with content.

**Judging filler**:
- If this content were removed, would the design get worse? If the answer is "no", remove it.
- What real problem does this element solve? If it is "to make the page less empty", delete it.
- Is this stats/quote/feature backed by real data? If not, do not make it up.

"One thousand no's for every yes."

### 2. Ask before adding material

Do you think adding a paragraph / page / section would be better? Ask the user first; do not add it unilaterally.

Reasons:
- The user knows their audience better than you do
- Adding content has a cost, and the user may not want it
- Adding content unilaterally violates the "junior designer reporting back" relationship

### 3. Create a system up front

After exploring the design context, **state aloud the system you intend to use first** and let the user confirm:

```markdown
My design system:
- Color: #1A1A1A main + #F0EEE6 background + #D97757 accent (from your brand)
- Type: Instrument Serif for display + Geist Sans for body
- Rhythm: section titles use a full-bleed colored background + white text; ordinary sections use a white background
- Imagery: hero uses a full-bleed photo; feature sections use placeholders until you provide images
- Use at most 2 background colors, to avoid clutter

I'll start once you confirm this direction.
```

Start only after the user confirms. This check-in avoids "discovering halfway through that the direction was wrong".

## Scale Specs

### Slides (1920×1080)

- Body minimum **24px**, ideal 28-36px
- Headings 60-120px
- Section titles 80-160px
- Hero headline can use big type of 180-240px
- Never put type smaller than 24px on a slide

### Print documents

- Body minimum **10pt** (≈13.3px), ideal 11-12pt
- Headings 18-36pt
- Captions 8-9pt

### Web and mobile

- Body minimum **14px** (16px to be friendly to older users)
- Mobile body **16px** (to avoid iOS auto-zoom)
- Hit target (clickable element) minimum **44×44px**
- Line height 1.5-1.7 (Chinese 1.7-1.8)

### Contrast

- Body text vs background **at least 4.5:1** (WCAG AA)
- Large text vs background **at least 3:1**
- Check with the accessibility tools in Chrome DevTools

## CSS Power Tools

**Advanced CSS features** are a designer's best friend; use them boldly:

### Typography

```css
/* Make heading line breaks more natural, so the last line is not a lone word */
h1, h2, h3 { text-wrap: balance; }

/* Body line breaking, avoiding widows and orphans */
p { text-wrap: pretty; }

/* Chinese typesetting power tools: punctuation squeezing, line-start/line-end control */
p { 
  text-spacing-trim: space-all;
  hanging-punctuation: first;
}
```

### Layout

```css
/* CSS Grid + named areas = off-the-charts readability */
.layout {
  display: grid;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
  grid-template-columns: 240px 1fr;
  grid-template-rows: auto 1fr auto;
}

/* Subgrid to align card content */
.card { display: grid; grid-template-rows: subgrid; }
```

### Visual effects

```css
/* A scrollbar with design sense */
* { scrollbar-width: thin; scrollbar-color: #666 transparent; }

/* Glassmorphism (use with restraint) */
.glass {
  backdrop-filter: blur(20px) saturate(150%);
  background: color-mix(in oklch, white 70%, transparent);
}

/* View transitions API for silky page transitions */
@view-transition { navigation: auto; }
```

### Interaction

```css
/* The :has() selector makes conditional styling easy */
.card:has(img) { padding-top: 0; } /* cards with an image have no top padding */

/* Container queries make components truly responsive */
@container (min-width: 500px) { ... }

/* The new color-mix function */
.button:hover {
  background: color-mix(in oklch, var(--primary) 85%, black);
}
```

## Quick Decision Reference: When You Hesitate

- Want to add a gradient? → Most likely don't
- Want to add an emoji? → Don't
- Want to give a card rounded corners + a border-left accent? → Don't, use another approach
- Want to draw a hero illustration in SVG? → Don't, use a placeholder
- Want to add a decorative quote? → Ask the user first whether they have a real quote
- Want to add a row of icon features? → Ask first whether icons are wanted; they may not be needed
- Using Inter? → Switch to something more distinctive
- Using a purple gradient? → Switch to a color scheme with a basis

**When you feel "adding this would look better", that is usually a symptom of AI slop**. Make the simplest version first, and add only when the user asks.
