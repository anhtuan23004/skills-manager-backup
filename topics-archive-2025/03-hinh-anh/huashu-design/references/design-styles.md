# Design Style Library: 20 Web + 20 PPT + 20 Infographic Styles (HTML-Native First)

> **Refactored 2026-06.** Reverse-engineered from a survey of the 10 major website types and 10 major presentation types, taking the top-5 acknowledged best designs of each (100 real cases in total).
> The fatal flaw of the old 20-style "graphic/installation designer philosophy" library: almost all of its bold styles were AI-generation-only (particles / light and shadow / hand-drawn). **Users are assumed to have no image-generation capability and the default is all-HTML, so the entire bold half was wiped out, leaving only minimalism -- this is the root cause of "default output all looks the same".** Every style in this library is marked with its **fidelity** under "pure HTML/CSS, no image generation".
>
> ⚖️ **But remember the positioning**: this is **"ammunition to flip through when you have no ideas", not a list you "must pick from"**. If the user provides content / brand / references, the design grows from those -- do not force the library onto it. The skill's job is to help the user avoid the worst outcome, not to dictate what good design looks like -- good design grows out of the user's real needs.

## How to use this library

1. **First pick a section by output type (three-way choice, not two-way)**: web page / landing page / official site -> the 20 Web styles; PPT / deck / presentation -> the 20 PPT styles; infographic / data visualization / single long image -> the 20 Infographic styles.
   - The criterion is **output form, not subject matter**: a clickable site goes to the Web section; something paged through goes to the PPT section; **one image (or a set) with data as the protagonist that can be read independently of interaction goes to the Infographic section**.
   - Two common borderline cases: a Dashboard prototype goes to the Web section (it is a product interface); a data page embedded in a deck still goes to the PPT section (it is paged through).
2. **Temperature system**: each style is tagged `Bold / Neutral / Quiet`. **Bold styles are deliberately the majority** -- the model's deterministic bias naturally leans toward quiet minimalism, and the library's mix must push it toward bold.
   - Direction A (safe base) is chosen from Quiet/Neutral as the need dictates; Direction B takes a different temperature for contrast; **Direction C takes a Bold style, picked at random from the Bold entries**.
   - ❌ Do not let all three directions land on "cream-white + whitespace + one accent color" -- that is the most common failure mode.
3. **Fidelity**: >=90% go ahead with confidence; 70-90% the main body can be done, a few details are downgraded; <70% (e.g. Memphis aged texture) you must **explicitly state in the output which parts are downgraded to flat color blocks**, and not pretend to achieve the original texture.
4. **Fonts**: each style gives open-source substitutes (Inter / Geist / Manrope / Space Grotesk / Fraunces / Playfair, etc.); do not write paid fonts (Söhne / Circular, etc.).
5. Companion material: the SKILL's "Design direction advisor" uses this library to propose 3 directions.

---

## Color Derivation Protocol (run these three steps before using any style)

> ⚠️ **All hex values in the style entries below are example anchors, not recipes.** The same style applied to different content should yield different color values through this protocol -- copying an entry's hex directly just produces slop with better taste. Why: hard-coded recipes give 100 users 100 outputs in the same colors, and the information content of color drops to zero; derivation makes color evidence of "this content's own identity".
>
> **Fonts work the same way**: the font names in the entries are also example anchors. After choosing a style, the display+body pairing must first pass a sanity check: avoid overused defaults (Inter/Roboto/Arial/system fonts as display type; if an entry names an overused font such as Fraunces, swap in an equivalent such as Newsreader), and for Vietnamese deliverables pick fonts with full diacritic support (see the SKILL's "Vietnamese deliverables").

### Three-step method: Sample -> Converge -> Justify

| Step | What to do | Why |
|------|-----------|-----|
| **1. Sample** | Take the primary color from three sources, never invent from nothing: (1) brand assets (pick colors straight from the logo / existing VI); (2) real content imagery (the dominant color of product screenshots / photography); (3) cultural context (the color memory the content topic carries, see table below) | Inventing from nothing = drawing lots from the model's priors, and what comes out is always the same few trendy colors; colors sampled from the content naturally carry a "why" |
| **2. Converge** | Use oklch to compress the palette to **2-3 chromatic colors + 1 set of neutrals**. Write the neutrals as a lightness sequence (e.g. L 0.15/0.35/0.65/0.92/0.98); keep chromatic colors apart by an oklch hue angle H >=60° or a lightness difference L >=0.3 | Too many colors become chaos; oklch's L channel is perceptually uniform, so a written-out lightness sequence is itself a hierarchy system, more reasoned-about than a pile of isolated hex values |
| **3. Justify** | Write one sentence on "why this color" into the output comments or delivery notes. Example: "Primary taken from the ochre in the user's logo, chroma lowered to 0.08 to imitate ink" | **If you cannot write this sentence, you are copying a recipe.** The justification is the self-check gate against slop, not a ritual |

### Print color texture: why low saturation feels more premium than pure screen colors

Ink on paper can never reach the maximum saturation of screen RGB -- the narrower CMYK gamut, paper absorbing ink, and ambient light reflection all "grey down" the color. The "premium feel" the human eye has been trained on by printed matter for decades is in essence this layer of physical greyness. So deliberately lowering chroma in screen design borrows the texture memory of print.

| Use | oklch chroma reference | Effect |
|-----|-----------------------|--------|
| Large background areas | 0.01–0.04 | Paper feel, easy on the eyes |
| Brand primary / emphasis | 0.08–0.15 | Ink feel, eye-catching but not plastic |
| Small accents (buttons / links) | 0.15–0.22 | Keeps vitality, small areas only |
| >0.25 full-bleed | Use with caution | Screen-fluorescent feel, only suits deliberately "electronic-native" styles such as Wrapped / candy |

### Cultural context cheat sheet: same hue, different contexts

Choosing a color is not just choosing a hue, it is choosing the cultural coordinates behind it. Even "red" lands worlds apart:

| Hue | Context A | Context B | The difference |
|-----|-----------|-----------|----------------|
| Red | Forbidden City vermilion (orange-leaning, greyed, in oklch low L and low C, darker and murkier than cola red) -> traditional / solemn | Cola red (high-saturation pure red) -> consumer / excitement | Drop the chroma and it jumps from the supermarket shelf to the palace wall |
| Blue | Japanese indigo dye / lapis navy (deep, purple-grey leaning) -> handcraft / calm | Tech blue #0066FF family -> SaaS / efficiency | The latter is the model's favorite default blue; before using it, ask yourself whether you are just drawing lots |
| Green | Matcha / moss green (yellow-leaning, low saturation) -> nature / Japanese | Fluorescent green #39FF14 -> terminal / hacker | Both are green; one is for drinking tea, the other for typing code |
| Yellow | Gamboge / mustard (brown-grey tinted) -> retro print | Warning yellow / Mailchimp yellow -> attention-grabbing / playful | The greyness decides whether it is an old book page or a hard hat |
| White | Cream paper white #F5F0E8 -> publication / warm | Pure white #FFF -> laboratory / Swiss | A 2% color-temperature difference in the background is the dividing line of character |

---

## Web Style Library (20 styles)

#### Bold

**Editorial Brutalism (giant Helvetica over small body text)** `Bold · fidelity 98%`
- Reference: Bloomberg Businessweek (Richard Turley's 2010-2014 redesign, executed by Code and Theory); the Neue Haas Grotesk lineage
- Fits: media / content publishing, AI product launches, brand site hero, research report covers, opinion-piece long-form header images
- Visual DNA: Palette pure black #000 + pure white #FFF + hyperlink blue #0000EE, accented with signal orange-red #FF433D / terminal green #00A33E. Typeface Helvetica / Neue Haas Grotesk; a 120px+ giant left-aligned, tightly tracked headline pressed directly onto 14px small body text, extreme size contrast. Layout is a modular grid with 1px rule lines splitting columns, high information density with deliberately no whitespace. Signature elements: rule-line column splits, blue underlined hyperlinks, large black/white color blocks.
- HTML implementation: Pure CSS can reproduce 1:1. CSS Grid for the modular grid + border for the rule-line column splits, clamp() for oversized responsive type + tightened letter-spacing, system Helvetica/Arial stack or Inter as fallback, hyperlinks directly #0000EE underlined. Zero asset dependency.
- Fonts: Inter (substitute for Helvetica/Neue Haas Grotesk), Geist Mono for code

**Neo-Brutalism (thick black-outlined cards + high-saturation clashing colors)** `Bold · fidelity 95%`
- Reference: The Verge 2022 redesign (in-house team, PolySans + Mānuka)
- Fits: media / content sites, AI product aggregator pages, event landing pages, community ranking pages, Xiaohongshu-style information cards
- Visual DNA: Palette electric violet #5200FF ~ magenta #E1306C high-saturation primaries + bright yellow #F8E000 emphasis + pure black #08080D + white, large clashing color blocks deliberately not softened. Typeface geometric sans-serif headlines contrasted with serif body. Layout is a card-based feed, 2-4px thick black outlines, hard color-block zoning, almost no rounded corners. Signature elements: thick-outlined cards that flip to a clashing color on hover, an unfinished-interface attitude.
- HTML implementation: A pure CSS strength. border:3px solid #000 thick outline + hard offset box-shadow (4px 4px 0 #000) + grid/flex card flow + :hover switching background for the clash-color flip. No 3D / light-and-shadow obstacles.
- Fonts: Space Grotesk (substitute for PolySans) + any serif such as Fraunces

**Memphis Maximalism (clashing blocks + offset stacking + retro type)** `Bold · fidelity 72%`
- Reference: Gucci Vault concept store (Alessandro Michele); the Memphis design movement / Sagmeister's rebellious gene
- Fits: e-commerce concept stores, creative event pages, brand experimental campaigns, Y2K retro themes, holiday marketing pages
- Visual DNA: Palette retro red / mustard yellow / royal blue / purple / olive green juxtaposed in large clashing areas + aged beige warm base, intense and deliberately dissonant. Typeface retro serif + decorative fonts mixed, print texture, offset stacking that breaks the grid. Layout is an anti-grid collage curation, modules of uneven size overlapping and pressing on each other, like browsing a digital room. Signature elements: clashing color blocks, offset stacking, unconventional navigation easter eggs.
- HTML implementation: transform:rotate() for offset stacking + position:absolute for overlap + high-saturation background clashing blocks + retro Google Fonts. Genuine aged texture cannot be reproduced in CSS; downgrade to flat color blocks + mix-blend-mode/contrast filters to simulate grain. The geometric collage version holds up; the archival aged version is downgraded.
- Fonts: DM Serif Display + Bungee (decorative) + Space Mono

**Friendly Geometric Candy (candy-colored raised 3D buttons, gamified)** `Bold · fidelity 85%`
- Reference: Duolingo (Johnson Banks + Monotype, Feather Bold typeface); anti-Silicon-Valley minimalism
- Fits: language-learning education, consumer app landing pages, gamified products, approachable mass-market products, event sign-up pages
- Visual DNA: Palette Duo green #58CC02 + duck yellow #FFC800 + sky blue #1CB0F6 candy high-saturation + white background, rounded and friendly. Typeface ultra-bold rounded (Feather Bold feel). Layout large-radius cards, raised 3D buttons (hard bottom shadow = pressable feel), mascot slot + progress bubbles. Signature elements: 3px solid-shadow 3D buttons, press-down displacement animation, extra-large corner radii.
- HTML implementation: Pure CSS. box-shadow:0 4px 0 hard bottom shadow for the raised button + :active translateY(4px) removing the shadow to simulate pressing, large border-radius, flat color blocks. Without image generation, use CSS geometric shapes or an emoji as the mascot placeholder (slight downgrade).
- Fonts: Baloo 2 / Nunito (ultra-bold rounded substitutes for Feather)

**Pure-CSS Art (pure-CSS geometric illustration + responsive-morph easter eggs)** `Bold · fidelity 80%`
- Reference: Lynn Fisher (lynnandtonic.com, legend of pure-CSS art, featured in an Adobe article)
- Fits: personal homepages, creative 404 / easter-egg pages, playful brand landing pages, tech blog header images, designer self-presentation
- Visual DNA: Palette 2-4 high-contrast flat color areas (palette changes at each breakpoint). Typeface bold geometric sans-serif headlines. The core of the layout is "the image morphs with the viewport" -- a set of CSS shapes reassembles into different pictures at different breakpoints (e.g. a building changing its number of floors with screen width). Signature elements: geometric illustration drawn in pure CSS, breakpoint-driven reflow easter eggs, zero images.
- HTML implementation: The showcase battleground of pure CSS, where zero assets is an advantage. Stack geometric shapes from divs using border-radius / clip-path / transform / box-shadow; @media breakpoints change shape sizes and positions to achieve the morph. The difficulty lies in design conception rather than technique, but every shape must be carefully hand-built.
- Fonts: Rubik / Archivo (bold geometric substitutes for custom)

**Bold Big-Type Editorial (giant high-contrast black-and-white fashion big-character poster)** `Bold · fidelity 88%`
- Reference: Jacquemus official site / Rik Oostenbroek / Domestika; fashion magazine big-type posters
- Fits: fashion e-commerce, portfolios, media features, brand manifesto pages, video course covers, big-type versions of research reports
- Visual DNA: Palette minimal black and white + a single restrained accent (nude pink #E8C4C0 or true red). Typeface oversized Display sans-serif / high-contrast serif, the headline filling the whole screen. Layout full-width grid, giant type wrestling with negative space, 1:1 image-text split. Signature elements: screen-filling giant headline, luxury-grade whitespace, left-right counterpoint typesetting.
- HTML implementation: Perfectly reproducible in pure CSS. clamp() giant type + CSS Grid full-width split + generous padding whitespace + vh units to make the headline fill the viewport. With no images, use flat color blocks / text blocks in place of the fashion photography placeholder (slight downgrade but the layout holds).
- Fonts: Archivo Expanded / Anton (Display) + Playfair Display (high-contrast serif)

**Cosmic Retro-Futurism (retro-futurist space catalogue)** `Bold · fidelity 75%`
- Reference: Perplexity Comet browser launch site (The Brand Identity: Black/Blue/Cream; the mood of *2001: A Space Odyssey*)
- Fits: AI product launch sites, tech brand manifesto pages, event countdown pages, futuristic landing pages, concept launch events
- Visual DNA: Palette pure black #0A0A0A + cream paper white #F0EAD8 + a touch of cobalt / peacock blue #2B4F91, low saturation like an old astronomical catalogue. Typeface high-contrast serif (classical astronomical atlas feel) + whitespace. Layout line-drawn orbit / parabola SVG, planet dots, black type on a cream base, antiquarian-book typesetting. Signature elements: SVG celestial orbit lines, cream + blue + black three colors, large retro serif type, astronomical-catalogue texture.
- HTML implementation: Pure CSS + SVG reproduces about 80% of the mood of the static version. SVG path for the orbit parabolas + CSS radial positioning of planet dots + three-color variables + high-contrast serif. The gap is the full-screen video transition of "space landing on Earth" (the soul of it) -- downgrade to CSS scroll parallax + SVG orbit rotation as an approximation.
- Fonts: Cormorant Garamond / EB Garamond (high-contrast serif) + Space Mono

**Cinematic Sound-Viz Dark (cinematic sound visualization, dark)** `Bold · fidelity 72%`
- Reference: ElevenLabs; film title sequences (Saul Bass-style minimalist motion) x audio engineering interfaces
- Fits: audio / voice AI products, music-tech sites, podcast platforms, media launch pages, cinema-grade brand hero
- Visual DNA: Palette pure black #000 background + pure white text + blue-violet gradient accent waveform. Typeface large sans-serif headline, Saul Bass-style minimalism. Layout full-width dark stage, sound-wave / spectrum visualization running throughout, giant headline pressed onto the waveform, card-based feature area. Signature elements: colored audio-waveform bands, film-title-style minimalism, high-contrast black/white + a single gradient, sound-visualization motif.
- HTML implementation: Pure CSS + SVG reproduces about 70% of the mood (the skeleton is perfect, the waveform is the downgrade point). SVG polyline for a static waveform, or an array of uneven-height div bars + CSS animation for a "fake waveform" bounce approximation. Gap: a Web Audio / Canvas spectrum that bounces in real time with sound cannot be reproduced in pure CSS -- the static version looks the part, but the dynamic soul cannot be returned.
- Fonts: Inter / Sora (large sans-serif)

**Pixel-Game Side-Scroller (pixel-game side-scrolling narrative)** `Bold · fidelity 70%`
- Reference: Robby Leonardi's interactive résumé (8/16-bit platformer storytelling, a tribute to the Nintendo SNES)
- Fits: creative résumés / portfolios, playful brand campaigns, gamified landing pages, event easter-egg pages, personal fun homepages
- Visual DNA: Palette retro-game multi-section zoning -- forest green #4CAF50 grass + sky blue #5DADE2, transitioning to space purple #2C2A4A, volcano orange-red #E8743B, seabed teal #1ABC9C; each "level" swaps in its own high-saturation cartoon palette. Typeface pixel font (8-bit feel) + bold sans-serif. Layout horizontal / vertical scrolling split into level scenes, parallax layering, scroll-triggered displacement. Signature elements: per-level color swaps, pixel aesthetic, parallax scrolling, game-HUD-style UI.
- HTML implementation: Pure CSS + a little JS reproduces the skeleton (the original is HTML+CSS+jQuery with no WebGL). Parallax layering via position + scroll displacement, image-rendering:pixelated, CSS frame-by-frame background-position for sprite animation, sectioned background colors. Gap: original hand-drawn pixel illustrations of characters / scenes -- without image generation, substitute simple pixel icons assembled from CSS squares (art downgraded, technique not).
- Fonts: Press Start 2P / VT323 (pixel fonts) + Inter


#### Neutral

**Bauhaus Geometric (geometric logomark + flat illustration system)** `Neutral · fidelity 90%`
- Reference: Khan Academy rebrand (hexagon + petal logomark + Wonder Blocks design system); Bauhaus geometric composition
- Fits: education course sites, brand logo systems, infographics, child-friendly products, event KVs
- Visual DNA: Palette primary-color spectrum -- Bauhaus red #E63946 / yellow #FFB703 / blue #0077B6 + black and white, flat color blocks joined together. Typeface geometric sans-serif (rounded geometric feel). Layout illustrations built from basic geometric units -- circle / triangle / square -- aligned to a grid, modular puzzle assembly. Signature elements: pure-geometry logomark, flat gradient-free illustration, composition from primary color blocks.
- HTML implementation: Pure CSS geometry can do everything. border-radius:50% for circles, clip-path / border triangles, div squares to assemble geometric illustrations, CSS Grid for grid alignment, flat color fills with no assets needed. Illustrations are hand-built with CSS shapes or inline SVG geometric paths.
- Fonts: Poppins / Manrope (rounded geometric substitutes for Wonder Blocks)

**Dark Editorial (dark two-column sidebar developer portfolio -- deep background + single neon accent + monospace)** `Neutral · fidelity 96%`
- Reference: Brittany Chiang (brittanychiang.com v4, the de facto standard for dev portfolios)
- Fits: portfolio personal homepages, developer-oriented products, tech brand sites, résumé pages, AI tool landing pages
- Visual DNA: Palette deep ink-green / navy background #0A192F + slate grey text #8892B0 + a single neon cyan-green accent #64FFDA. Typeface sans-serif body + monospace (numbering / tags). Layout fixed left sidebar navigation + scrolling right main area in two columns, section numbering 01/02, link hover underline sliding in. Signature elements: single accent color, monospace numbered labels, sidebar anchor highlighting.
- HTML implementation: Fully reproducible in pure CSS. position:sticky for the fixed sidebar + CSS Grid two columns + a single accent variable + monospace labels + :hover underline sliding in via transform. Zero assets, pure typesetting and micro-interactions.
- Fonts: Inter + JetBrains Mono (monospace)

**Warm Editorial (cream-paper background + terracotta orange + serif/sans-serif mix)** `Neutral · fidelity 97%`
- Reference: Anthropic / Claude (DBCo + Geist Studio, Styrene x Tiempos); Penguin/Pelican paperback typography
- Fits: AI product sites, brand official sites, long-form reading pages, "orange book" ebooks, research reports, training materials
- Visual DNA: Palette cream-paper background #F5F0E8 + terracotta orange #CC785C/#D97757 accent + near-black text #191919, warm and low saturation. Typeface serif headlines (Tiempos feel) x sans-serif body (Styrene feel) mixed. Layout book-style single-column reading flow, comfortable line height, restrained dividers. Signature elements: warm paper-feel background, terracotta orange, publication-grade typographic rhythm.
- HTML implementation: 100% reproducible in pure CSS, zero assets. Background color variable + serif/sans-serif font stack mix + max-width to limit reading width + line-height 1.7 for comfortable line spacing. This is the safe home ground for the Anthropic terracotta-orange warm version.
- Fonts: Fraunces / Newsreader (serif substitute for Tiempos) + Inter (substitute for Styrene)

**Glassmorphism Bento (Linear dark glow + bento grid)** `Neutral · fidelity 85%`
- Reference: Linear / Cursor ("The Linear Look", a phenomenon-level genre; Frontend Horse has code recipes)
- Fits: SaaS / AI product sites, developer tools, tech brand hero, product feature showcases, dark dashboard demos
- Visual DNA: Palette near-black background #08090A + desaturated blue-violet brand #5E6AD2 + low-saturation cyan-violet glimmer gradient #4EA7FC→#B59AFF. Typeface geometric sans-serif with negative tracking, compact. Layout bento-box grid blocks, hairline dividers, glassmorphism cards. Signature elements: glowing gradient borders on a dark base, bento blocks, flowing-light streamers, frosted glass.
- HTML implementation: Strongly reproducible in pure CSS. box-shadow / filter blur + radial-gradient for glow halos, backdrop-filter:blur for glassmorphism, conic/linear-gradient borders, CSS Grid to assemble the bento. The only gap is "real product UI screenshots" -- substitute a simplified fake UI built from color blocks + text (this part is downgraded).
- Fonts: Inter / Geist (negative tracking) + Geist Mono

**Angled Fluid Gradient (slanted fluid gradient band)** `Neutral · fidelity 92%`
- Reference: Stripe (signature angled gradient banner, Söhne custom typeface by Klim)
- Fits: SaaS / Fintech landing pages, brand site hero, product launch pages, event banners, AI product marketing pages
- Visual DNA: Palette multi-color fluid gradient (indigo #635BFF → cyan → pink → orange warm tones) as the hero background + pure white content area + near-black text. Typeface refined sans-serif (Söhne feel). Layout slanted split color blocks (skew-cut zoning), a gradient hero pressing down on a structured-grid body. Signature elements: angled slanted boundaries, multi-color fluid gradients, rational grid pressing on expressive gradient.
- HTML implementation: Pure CSS. transform:skewY() or clip-path:polygon() for the slanted zoning, multi-color stacked linear-gradient (optionally with a slow-flowing CSS animation) for the fluid gradient band, Grid for the structured body below. Zero assets.
- Fonts: Inter / Hanken Grotesk (substitutes for Söhne)

**Utility-First Colorful Docs (utilitarian rainbow-categorized documentation)** `Neutral · fidelity 98%`
- Reference: Tailwind CSS Docs (Sky/Cyan brand color + rainbow hue strips for functional categories)
- Fits: technical documentation, API references, design-system sites, tutorial sites, developer knowledge bases, SaaS help centers
- Visual DNA: Palette Sky blue #38BDF8 brand + teal→cyan→sky cyan-blue gradient + Slate greyscale #0F172A/#64748B/#F8FAFC; the docs use rainbow hue strips to distinguish functional categories (pink #EC4899 / purple #A855F7 / green #10B981 / orange). Typeface clean sans-serif + monospace code. Layout left sidebar navigation + central body + right TOC in three columns, colorful highlighted code blocks, category color tags. Signature elements: cyan-blue gradient hero, rainbow category colors, three-column docs skeleton, syntax-highlighted code blocks.
- HTML implementation: 98% reproducible in pure CSS (it is itself CSS-framework documentation). Grid three columns + linear-gradient cyan-blue hero + category color variables + code-block syntax colors via span coloring. Inter is open source; only dark-mode toggle / copy button need light JS. No light-and-shadow / 3D / hand-drawing.
- Fonts: Inter + JetBrains Mono / Fira Code (code)

**Terminal-Core Soft-Futurism (monospace type + isometric cubes)** `Neutral · fidelity 80%`
- Reference: Cursor (Anysphere); developer terminal aesthetic x Teenage Engineering industrial minimalism
- Fits: AI coding tool sites, CLI product landing pages, developer infrastructure, tech brand hero, terminal-type products
- Visual DNA: Palette charcoal black #0B0D14 background + warm white text #F2F0EF + restrained blue-violet gradient accent on buttons and glows. Typeface monospace as the protagonist (command-line feel) + sans-serif as support. Layout command line / code block in the foreground, bento zoning, 2.5D isometric cube illustrations. Signature elements: monospace command line, isometric-projection cubes, warm white x charcoal black, restrained gradient glow, industrial minimalism.
- HTML implementation: 80% reproducible in pure CSS. Monospace code blocks + dark bento + box-shadow glow; the 2.5D isometric cube is hand-built with CSS 3D transform (rotateX/Y + skew) or SVG isometric projection. Gap: a multi-screen demo switchable by click requires JS + fake-UI assembly. No hard WebGL requirement.
- Fonts: Geist Mono / JetBrains Mono (protagonist) + Inter (support)


#### Quiet

**Functional Brutalism (grey-line dividers + system font + blue links)** `Quiet · fidelity 98%`
- Reference: Are.na / Lobsters / Quartz; Müller-Brockmann's grid made digital + Tufte's information density
- Fits: community / UGC platforms, content aggregator sites, documentation knowledge bases, mobile-first content feeds, geek-oriented products
- Visual DNA: Palette near-white background #FBFBFB + black text + 1px grey dividers #E0E0E0 + classic link blue #0000EE / visited purple. Typeface system font stack (-apple-system / undecorated). Layout high-density information lists, thin grey-line column splits, minimal whitespace, compact line spacing. Signature elements: hairline grey dividers, blue links, system fonts, information density first.
- HTML implementation: The easiest to reproduce in pure CSS; this is the true colors of Brutalist Web. border-bottom:1px grey-line lists + system-ui font stack + compact padding + blue links. Almost no assets or JS needed, pure structure.
- Fonts: system-ui system font stack / IBM Plex Sans (fallback)

**Gallery Dark (deep-black negative space + single-column large image + EXIF small type)** `Quiet · fidelity 75%`
- Reference: Glass (glass.photo) / Bottega Veneta; museum darkroom + Apple Photos' content-first approach
- Fits: photography portfolios, luxury e-commerce, immersive visual content display, personal gallery pages, high-end product display
- Visual DNA: Palette pure black background #0A0A0A + the artwork images themselves provide the only color + very light grey EXIF small type #666. Typeface ultra-light sans-serif small type. Layout single centered column of large images, vast negative-space mounting, metadata small type under the image. Signature elements: darkroom black background, content-first UI that recedes, EXIF-style small-type footnotes, a large image alone occupying the viewport.
- HTML implementation: Pure CSS reproduces the layout skeleton. Pure black background + centered max-width single column + vast padding mounting whitespace + small-type metadata. The gap is the "real photographic work" itself -- substituting placeholder images / flat color blocks loses the soul, but the darkroom atmosphere and layout can be 100% built.
- Fonts: Inter (light weight 300) / Cormorant (serif luxury feel, optional)

**Swiss Monochrome (Vercel-style pure black and white + Geist + sharp corners)** `Quiet · fidelity 98%`
- Reference: Vercel / Next.js Docs (in-house Geist, now open source); Massimo Vignelli's less is more
- Fits: developer tool docs, tech brand official sites, AI product sites, SaaS landing pages, minimalist research reports
- Visual DNA: Palette pure black #000 + pure white #FFF + greyscale #888, zero chromatic color or just a touch of link blue. Typeface Geist geometric sans-serif + Geist Mono. Layout sharp right angles (no radius or minimal), high contrast, precision grid, restrained whitespace. Signature elements: pure black and white, sharp corners, the Geist typeface, triangle / arrow geometric markers.
- HTML implementation: 100% reproducible in pure CSS, and Geist is open source so it can be imported directly. CSS Grid precision grid + pure black-and-white variables + border-radius:0 sharp corners + hairline borders. This is HTML's most comfortable minimalist home ground, with zero asset dependency.
- Fonts: Geist + Geist Mono (Vercel's open-source originals)

**Kenya Hara White Gallery (Japanese whitespace white-box gallery)** `Quiet · fidelity 80%`
- Reference: Cosmos (cosmos.so) / Aesop's official site; the stillness of Kenya Hara's "White" + a Swiss grid hybrid
- Fits: high-end e-commerce, creative galleries, content curation platforms, designer portfolios, brand boutiques, moodboard sites
- Visual DNA: Palette near-total white #FAFAFA background + pure black text #0A0A0A + very light grey dividers #EFEFEF; content images provide all the color, UI recedes to the background. Typeface minimalist system / geometric sans-serif small type, wide tracking. Layout masonry waterfall grid, extreme whitespace, light-grey hairline separation, Eastern stillness. Signature elements: white-box aesthetic, luxury whitespace, content-first UI retreat, waterfall-flow curation.
- HTML implementation: Pure CSS reproduces the static layout (distinguished from the dark gallery by "white"). CSS columns or Grid for the masonry + near-white variables + large padding whitespace + light-grey separators. The gap is Lenis/GSAP smooth inertial scrolling and image entrance easing (60% of the premium feel lives here); CSS offers only basic transitions, so the motion layer is downgraded.
- Fonts: Inter (light weight) / Cooper Hewitt (the open-source font Aesop uses)


## PPT Style Library (20 styles)

#### Bold

**Neo-Swiss Billboard Editorial** `Bold · fidelity 98%`
- Reference: the Big-Number Editorial school of AI/SaaS pitch decks such as Scribe $75M and Flock Safety $47M; Bloomberg Businessweek infographics; Pentagram
- Fits: fundraising pitches, QBR / business reviews, annual trend retrospectives, key product-launch slides
- Visual DNA: Palette = pure white (#FFFFFF) or near-black (#0A0A0A) background + a single high-saturation accent (electric blue #2D5BFF / neon green #00E676 / brand orange #FF6B2C) + neutral grid lines #E5E5E5. Typeface = oversized bold sans-serif, headline taking half the screen, numbers tabular-nums monospaced with tightened tracking. Masters = (1) large-color-block section page with one word (2) giant number taking half the screen (3.2x) + small note (3) left-right split comparison (4) full-width flat line / bar chart. Signature = billboarding big type, strict baseline grid, large-color-block section pages
- HTML implementation: clamp() for oversized numbers; CSS Grid for the strict grid; background-color for large-color-block section pages; line / bar charts with plain divs + CSS or inline SVG (sharper than pasted images); number alignment with font-variant-numeric:tabular-nums. Zero illustration, zero 3D
- Fonts: Inter / Geist / Söhne substitutes for Neue Haas Grotesk; numbers paired with Geist Mono

**Black Big-Number Stage** `Bold · fidelity 97%`
- Reference: Steve Jobs' 2007 iPhone Keynote, Lei Jun's Xiaomi SU7 Ultra launch event, Spotify Wrapped, Presentation Zen (Garr Reynolds)
- Fits: product-launch keynotes, thought presentations, all-hands town halls, emotion-driven annual reviews
- Visual DNA: Palette = pure black #000000 background + pure white #FFFFFF text for high contrast, only one brand accent highlighted per slide (Xiaomi orange #FF6900 / Spotify green #1ED760 / Apple blue #2997FF). Typeface = geometric sans-serif bold, one word or one oversized number filling the field of view per screen, tightened tracking. Masters = (1) title slide, black background with one centered line of large type (2) data climax slide, giant number + unit + one line of note (3) left-right parameter comparison in two columns (accent vs grey) (4) single-slide slogan. Lots of negative space
- HTML implementation: black background, white text in a few lines of CSS; giant numbers with clamp() + flex centering; accent color highlighted in a separate span; left-right comparison via CSS Grid two columns + bar highlight; tabular-nums. Removing product photos and going pure text actually gets closer to the essence of Zen
- Fonts: Geist / Inter / Source Han Sans substitutes for SF Pro

**Mono-Brand Type-as-Hero (high-saturation monochrome brand clash poster)** `Bold · fidelity 96%`
- Reference: Spotify Wrapped visual system, Mailchimp Brand Book (Collins), a modern recreation of Netflix red-and-black, the COLLINS brand system
- Fits: brand / marketing strategy, campaign presentations, town-hall culture pages, event key visuals
- Visual DNA: Palette = a single brand primary color flooding the full page (Spotify green #1ED760 / Mailchimp yellow #FFE01B / Netflix red #E50914) + black or white contrasting type, two layers of clash. Typeface = oversized type as the main visual (type-as-hero), towering top to bottom. Masters = (1) full color-block base + reversed-out giant type (2) two color blocks split top/bottom or left/right (3) giant number filling the page. Signature = single-color full-bleed, type as image, high-contrast clash
- HTML implementation: full-bleed background-color; oversized type with clamp() to fill; two colors via two 100vh color blocks; type-as-image relies on font-weight 900 + negative letter-spacing. Flat color blocks, zero assets, the most satisfying case for native HTML
- Fonts: Inter / Manrope / Archivo (ultra-bold) substitutes for Circular/Cavendish

**Full-Bleed Gradient Manifesto** `Bold · fidelity 82%`
- Reference: Zuora's "Tell a Different Story" sales deck (dissected by Andy Raskin), Nike's "Just Do It" campaign, National Geographic spreads
- Fits: sales-proposal vision pages, brand manifestos, keynote turning-point slides, single-page mission/vision
- Visual DNA: Palette = full-bleed CSS gradient (warm orange → magenta / deep blue → cyan) or flat-color bleed + reversed-out manifesto large type + hashtag slogan (#shifthappens). Typeface = heavy all-caps sans-serif slogan running across. Masters = (1) full-width gradient + centered reversed-out manifesto (2) promised-land vision page (3) customer logo wall. Signature = full-bleed, reversed-out large slogan, hashtag slogan
- HTML implementation: linear-gradient/radial-gradient full-bleed (no particles / light and shadow; pure CSS gradients are permitted); reversed-out type centered with position; logo wall with a grid of greyscale SVG / text placeholders. The parts that originally relied on large documentary photos are downgraded to a CSS gradient base + large type; missing photos lower fidelity by about 15%
- Fonts: Archivo / Anton / Manrope (ultra-bold)

**Candy-Color Lecture Stage (CS50 single-concept candy stage)** `Bold · fidelity 94%`
- Reference: Harvard CS50 (David Malan), Lessig Method / Takahashi method, Presentation Zen
- Fits: educational courseware, technical lectures, concept explanation, code teaching
- Visual DNA: Palette = deep black background #0A0A0A + high-saturation candy-color large type rotating (magenta #FF2D95 / cyan #00E5FF / bright yellow #FFD500 / green #39FF14). Typeface = oversized sans-serif floating centered, one concept per screen, very little text. Masters = (1) deep black base with a single candy-color large word (2) monospace code block with syntax highlighting (3) stage-spotlight-feel large type. Signature = large candy-color type floating on deep black, monospace code highlighting, strong stage spotlight, very little text
- HTML implementation: deep black background + single-color oversized type centered with clamp(); code blocks via pre + monospace font + span coloring for syntax highlighting; spotlight feel via a very faint radial-gradient vignette (not a particle light effect). High fidelity
- Fonts: Inter ultra-bold + JetBrains Mono (code)

**Playful Maximalist Editorial (playful hand-drawn minimalism, Collins-style)** `Bold · fidelity 75%`
- Reference: Mailchimp Brand Book (Collins 2018), the New Yorker cartoon mood, Cooper rounded serif, Cavendish fluorescent yellow
- Fits: brands with attitude decks, creative agency proposals, culture-oriented town halls, anti-SaaS-minimalism marketing pages
- Visual DNA: Palette = Cavendish fluorescent yellow #FFE01B in large areas + black + a few clash colors, anti-SaaS-minimalism. Typeface = Cooper-style rounded serif large headlines (playful) + magazine-style whitespace composition. Masters = (1) fluorescent-yellow full base + whimsical headline (2) magazine-style irregular whitespace layout (3) large-type pun copy. Signature = fluorescent yellow, rounded serif, playful composition, whimsical hand-drawn character (downgraded to geometric color blocks / emoji in place of real illustration)
- HTML implementation: fluorescent-yellow background; rounded-serif font-family; magazine whitespace with an asymmetric Grid. The core element of the hand-drawn gorilla / illustrations cannot be done without AI image generation; downgrade to CSS geometric color blocks + large emoji + irregularly transform-rotated text blocks as substitutes; missing illustration lowers fidelity by about 20%
- Fonts: Fraunces (adjustable roundness) / Bree Serif substitutes for Cooper; body Inter

**Irreverent Pop (Reddit-style)** `Bold · fidelity 80%`
- Reference: Reddit Ads sales deck (named by Dock as having the most personality), David Carson-style irreverent typography, 90s web retro, Memphis playfulness
- Fits: Gen-Z brands, meme-driven marketing decks, community / creator-oriented, proposals bold enough to not be serious
- Visual DNA: Palette = Reddit orange-red #FF4500 + clash colors, 90s web retro colors. Typeface = mixed / grid-breaking David Carson-style typography, meme-y colloquial copy. Masters = (1) fun page with meme large type (2) facts page with a rhythm shift to serious data (3) colloquial headline. Signature = grid-breaking mixed typesetting, orange-red, meme-y colloquial voice, fun→facts rhythm reversal, retro web texture
- HTML implementation: deliberately break the grid with transform rotation / overlapping positioning / mixed font sizes; orange-red + clash color blocks; retro texture via thick black border + hard box-shadow (no blur). Custom meme illustrations are downgraded to emoji + geometric collage, but the mixed typesetting itself is reproducible in HTML
- Fonts: Archivo / Space Grotesk + a mix with Inter for contrast

**Maximalist 3D-Type (Y2K inflated big type, Wrapped-style)** `Bold · fidelity 78%`
- Reference: Spotify Wrapped 2022/2023/2025, Memphis clash colors, Y2K/Maximalism, duotone portrait gradients
- Fits: annual reviews (emotion-driven, built to go viral), personalized data cards, vertical social-share cards, brand year-end
- Visual DNA: Palette = high-saturation clash full-bleed backgrounds (magenta + cyan + orange) + Spotify green accent + duotone two-color gradients. Typeface = towering giant numbers, with years / numbers rendered in 3D inflated / metallic texture. Masters = (1) clash full-bleed + giant inflated number (2) duotone portrait / color-block base + reversed-out large type (3) vertical shareable card. Signature = giant inflated 3D numbers, clash full-bleed, duotone gradients, metallic year texture, vertical story card
- HTML implementation: clash full-bleed background; 3D inflated numbers via layered CSS text-shadow + transform:perspective or SVG + stroke to create volume (not true 3D rendering); duotone via mix-blend-mode + gradient overlaid on a greyscale image placeholder block. Metallic texture is downgraded to gradient-filled text with background-clip:text, lowering fidelity by about 15%
- Fonts: Archivo Black / Anton ultra-bold + numbers in Clash Display


#### Neutral

**Bento Grid (bento-box modular grid)** `Neutral · fidelity 95%`
- Reference: the Apple Keynote Bento Grid era, the new-generation MBB Bento/Big-Type decks (2024-2026), Stripe annual report metric card matrices, Pitch.com QBR templates
- Fits: product feature summaries, consulting / QBR data reporting, sales results pages, town-hall metrics pages
- Visual DNA: Palette = light grey / cream background (#F5F5F7/cream) or near-black background + brand primary + 1-2 accents, cards with a light zoning base + rounded corners + faint outline / faint shadow. Typeface = oversized display headline + regular body, strong weight contrast, KPI numbers in tabular figures. Masters = (1) title slide with one giant sentence + whitespace (2) bento page with 2x2 / 3-column unequal-height cards, one insight per card (number / linear icon / sparkline) (3) one-insight oversized-number page. Signature = unequal-height card grid, rounded corners with faint outline, breathing room
- HTML implementation: CSS Grid grid-template-areas for unequal-height bento; cards with border-radius + faint box-shadow + 1px hairline; sparklines in inline SVG; linear icons in inline SVG stroke. Zero pasted images
- Fonts: Inter / Geist + numbers in Geist Mono

**Dark Hairline Terminal (Neo-Swiss dark terminal aesthetic)** `Neutral · fidelity 94%`
- Reference: Linear pitch deck, Vercel's design language, CS50's deep-black stage courseware; typefaces Inter Tight + JetBrains Mono
- Fits: developer tools / tech product launches, tech pitches, engineering-oriented reports
- Visual DNA: Palette = near-black background (#0D0D0F/#111113) + hairline thin-line #262629 grid + a single violet-blue accent (#5B5BD6/#7C7CFF). Typeface = Inter Tight large headlines + JetBrains Mono for labels / data. Masters = (1) minimal title slide with one sentence + small mono label (2) data grid separated by hairlines (3) feature list with mono labels. Signature = 1px hairline grid, mono single-width labels, extreme whitespace, near-black rather than pure black
- HTML implementation: near-black background + border:1px solid hairline grid; mono labels via a monospace font-family; faint glow via a very light box-shadow / border highlight rather than true light effects (a downgrade that avoids the cyber-neon forbidden zone). Note: avoid the #0D1117 deep-blue forbidden zone; use a neutral near-black
- Fonts: Inter Tight + JetBrains Mono / IBM Plex Mono

**Two-Font Consulting (Bower-style)** `Neutral · fidelity 90%`
- Reference: McKinsey's 2019 brand system (designed by Wolff Olins, Bower serif + sans-serif), BCG Executive Perspectives, deep-blue thin-line patterns
- Fits: consulting reports, executive briefings, industry research, authoritative-institution proposals
- Visual DNA: Palette = deep blue (#051C2C / McKinsey deep blue) x white duality + a single brand-color highlight (BCG green #00805A), warm grey base with breathing room. Typeface = characterful serif large headlines (Bower-style) set in high contrast against sans-serif body. Masters = (1) conclusion-style action-title at top left (2) blue thin-line pattern decoration (3) magazine-style left-right division of labor (conclusion text + visual) (4) large-number data-point card. Signature = serif x sans-serif high contrast, deep-blue thin-line pattern, action-title, warm-grey premium feel
- HTML implementation: dual font-family juxtaposition (serif headline + sans-serif body); thin-line pattern via repeating-linear-gradient or SVG line; data-point cards in pure CSS; the greyscale photo treatment can be skipped when there are no photos. The blue-violet edge shimmer is downgraded to a flat-color edge
- Fonts: Playfair Display / Fraunces serif headlines + Inter body (substitutes for Bower)

**Diagram-Driven Isotype (enterprise diagram-and-arrow edition)** `Neutral · fidelity 88%`
- Reference: Salesforce sales deck, the Isotype (Otto Neurath) lineage, Gene Zelazny's *Say It With Charts*, Hans Rosling/Gapminder
- Fits: platform / architecture explanation, customer journeys, process methodologies, ecosystem maps
- Visual DNA: Palette = enterprise blue blocks + product-line color zoning + an iconized capability grid. Typeface = clear sans-serif. Masters = (1) horizontal customer-journey arrow flow (2) layered platform architecture diagram (3) iconized capability grid (4) 2x2 / waterfall / pyramid structure diagrams. Signature = arrow process flow, layered architecture boxes, Isotype icon grid, process as narrative
- HTML implementation: arrow flows via Flexbox + CSS clip-path triangles or SVG arrows; layered architecture via nested bordered divs; icons in inline SVG with uniform stroke; waterfall / pyramid via Grid + slanted cuts. Bubble charts can use CSS circles + positioning. Purely vector-drawn
- Fonts: Inter / IBM Plex Sans (chart-friendly)

**Diagrammatic Minimalism (single master-diagram concept illustration)** `Neutral · fidelity 95%`
- Reference: Simon Sinek's Golden Circle TED talk, Bauhaus geometric abstraction, information architecture's "one diagram settles the whole room"
- Fits: theoretical framework explanation, TED-style idea spreading, model / methodology visualization, single-concept keynotes
- Visual DNA: Palette = minimal white / light base + black + 1 accent, geometric flat color. Typeface = sans-serif, uppercase labels embedded in the figure. Masters = (1) a single geometric master diagram (concentric circles / triangle / matrix) carrying the entire concept (2) inside-out arrows (3) comparison cases. Signature = single geometric master diagram, nested concentric circles / triangles, uppercase labels, one diagram carrying the concept
- HTML implementation: concentric circles via nested divs with border-radius:50% or SVG circle; triangles via clip-path / SVG polygon; arrows via SVG marker; labels absolutely positioned onto the figure. Pure geometry, perfectly reproduced in HTML
- Fonts: Manrope / Futura family (Jost as the open-source substitute) for geometric feel

**Narrative Sparkline (Duarte-style)** `Neutral · fidelity 91%`
- Reference: Nancy Duarte's *Resonate* sparkline narrative map, Al Gore's *An Inconvenient Truth*, Duarte Inc. data storytelling
- Fits: speech structure design, change narratives, before/after comparisons, data story arcs
- Visual DNA: Palette = dark or white base + brand orange emphasizing turning points + greyed-out comparison. Typeface = sans-serif, annotation callouts. Masters = (1) an oscillating waveform line running across the full screen (2) text annotation points on the waveform (3) comparison waveforms stacked top and bottom (4) a lone data line suspended on a full-black base (5) step-by-step reveal. Signature = a waveform line running across, annotation points on the waveform, orange turning points, comparison waveforms, a curve climbing out of the frame
- HTML implementation: waveform line via an inline SVG path (smooth Bézier); annotation points via SVG circle + positioned text; comparison waveforms as two paths top and bottom; reveal via CSS animation of stroke-dashoffset. Pure SVG drawing with no assets
- Fonts: Inter + numbers in Geist Mono


#### Quiet

**Assertion-Evidence (Assertion-Evidence / Tufte information design)** `Quiet · fidelity 93%`
- Reference: Michael Alley's Assertion-Evidence (Penn State empirical research), McKinsey/BCG action-titles, Edward Tufte's data-ink ratio, Barbara Minto's Pyramid Principle
- Fits: academic / engineering reports, rigorous data-driven consulting pages, policy research reports, technical reviews
- Visual DNA: Palette = white / very light grey background + black body text + a single restrained accent (deep blue / brick red). Typeface = a full-sentence title (not a noun phrase), one figure alone beneath the title, text annotations embedded in the figure. Masters = (1) full-sentence action-title (2) single-figure evidence beneath the title (3) zero bullets. Signature = full-sentence title, single-figure evidence, embedded annotation, zero chartjunk, high data-ink ratio
- HTML implementation: full-sentence titles rely on typographic hierarchy; charts drawn in pure CSS / inline SVG as minimal line / scatter plots (grid lines and legend removed, annotations positioned as text directly beside data points); zero decoration. Tufte's restraint is exactly HTML's strength
- Fonts: Source Serif / Lora headlines + Inter body (two-font reading-grade)

**Institutional Swiss Minimal** `Quiet · fidelity 96%`
- Reference: Sequoia's official 10-page pitch template, Airbnb's 2009 seed-round deck, the Müller-Brockmann grid, Massimo Vignelli
- Fits: investor pitches, standard business proposals, problem-solution narratives, de-ornamented brand proposals
- Visual DNA: Palette = pure white background + black-grey body + a single brand accent (Airbnb coral red #FF5A3C / neutral blue). Typeface = Helvetica-family sans-serif, headline medium-size bold in one sentence, body in short sentences with generous spacing. Masters = (1) centered logo + slogan (2) top one-sentence title band + 3-column parallel below (Problem/Solution in three points) (3) TAM big-number layering (4) 2x2 competitor matrix. Signature = top title band, three-column parallelism, single-color accent, 2x2 matrix
- HTML implementation: Flexbox three-column parallelism; 2x2 matrix drawn with pure CSS Grid + border; TAM layering with nested divs or concentric squares; one message per slide. Almost pure typesetting grid, an ideal subject for HTML
- Fonts: Inter / Helvetica Now substitutes for Helvetica; body Inter

**Editorial Longform (magazine editorial long-form flow)** `Quiet · fidelity 95%`
- Reference: Stripe Annual Letter ($1.9T), Amazon's six-page narrative memo, Benedict Evans' "X eats the world", Stripe Press
- Fits: annual letters / retrospective narratives, in-depth thought long-form, internal updates, research-report-style reading material
- Visual DNA: Palette = cream / off-white background (#FBFAF8) + deep ink text + brand-color accent (Stripe purple #635BFF). Typeface = serif or high-quality sans-serif, prose paragraphs + inline data cards, oversized display numbers interspersed. Masters = (1) masthead large headline (2) multi-column prose + inline metric cards (3) oversized-number paragraph anchors. Signature = publication reading rhythm, inline data cards, restrained whitespace, prose rather than bullets
- HTML implementation: multi-column via column-count or Grid; inline data cards embedded in the body via float / inline-block; serif body with max-width controlling line width to 65ch; oversized numbers interspersed. Pure typesetting, zero assets
- Fonts: Newsreader / Source Serif body + Inter support; numbers tabular

**Humanist Rounded Cards (Khan-style)** `Quiet · fidelity 80%`
- Reference: Khan Academy's Wonder Blocks design system, Source Serif Pro serif, forest-green brand, friendly humanism
- Fits: education products, approachable courseware, public-interest / nonprofit decks, warm brand proposals
- Visual DNA: Palette = forest green #14BF96/#0A5C4B + off-white background + warm supporting colors, soft and not harsh. Typeface = Source Serif serif headlines (humanist feel) + sans-serif body. Masters = (1) rounded-card component groups (2) serif headline + approachable body (3) real photography slot (downgraded to green-family geometric / rounded color blocks). Signature = forest green, serif headlines, large-radius cards, humanist warmth, an imperfect approachable texture
- HTML implementation: large border-radius cards + soft box-shadow; serif headline font-family; warm off-white background. Real teacher-and-student photography cannot be done without AI image generation; downgrade to green-family geometric illustration blocks / large-radius flat placeholders + emoji figures; missing photos lower fidelity by about 18%
- Fonts: Source Serif 4 headlines + Nunito Sans / Inter body (Nunito's roundness echoes the humanism)

**Dense Research Report (Meeker-style)** `Quiet · fidelity 92%`
- Reference: Mary Meeker's *Internet Trends* (BOND), CB Insights' *State of AI*, McKinsey Global Institute's *Year in Charts*, FT/Bloomberg data journalism
- Fits: trend research reports, industry data retrospectives, dense data briefings, market maps
- Visual DNA: Palette = white background + brand color (BOND/CB Insights bright blue #0066FF) with a stepped monochrome highlight and the rest greyed out, almost zero whitespace. Typeface = conclusion-style sentence titles, one chart per page density, very small source footnotes. Masters = (1) conclusion-sentence title + full-page single chart (2) logo-grid market map (3) big-number KPI cards (4) dense multi-chart grid + footnotes. Signature = conclusion-sentence titles, zero-whitespace research-report feel, monochrome stepped highlighting, logo market map, disciplined source footnotes
- HTML implementation: dense charts all drawn in pure CSS / inline SVG (bar / line / stacked / scatter); logo market map via Grid + text / SVG placeholder cells; KPI cards in CSS; small-type footnotes. Extreme information density is exactly what HTML excels at, zero assets
- Fonts: Inter + IBM Plex Sans + numbers in tabular Geist Mono

**All-Text Manifesto (Netflix/Amazon-style memo)** `Quiet · fidelity 97%`
- Reference: Netflix Culture Deck (2009, 125 pages), Amazon's six-page narrative memo (Bezos), Tufte's anti-PowerPoint stance, Matthew Carter's reading-grade typography
- Fits: culture manifestos, values presentations, in-depth memos, anti-PPT pure-document presentations
- Visual DNA: Palette = pure white or pure black background + a single accent color (Netflix red #E50914) as the only highlight, extreme restraint. Typeface = reading-grade typography, one-viewpoint-per-page aphorism assertions / pure prose with zero bullets and zero images. Masters = (1) full-bleed base + aphorism assertion (2) colloquial candid paragraph (3) institutional-term highlighting (Keeper Test) (4) six pages of prose + appendix table. Signature = pure text with one viewpoint per page, zero images and zero bullets, single-color highlighted aphorisms, colloquial candor, silent-read document feel
- HTML implementation: pure typesetting: aphorisms as large clamp() type in a left-aligned hierarchy; prose with max-width controlling line width; the single accent color highlighting key phrases via span; appendix as a minimal table. Zero assets, zero images; pure text is the most stable reproduction in HTML
- Fonts: Newsreader / Source Serif (reading-grade) or Inter (manifesto-style); headlines may use ultra-bold Archivo


---

## Infographic Style Library (20 styles)

> **Added 2026-08.** Previously this library had only the Web and PPT sections (two and a half halves), yet "infographic / visualization" is one of the SKILL's four applicable scenarios -- when making an infographic the roulette could only land in the Web half, drawing styles for community sites / landing pages and forcing them on. This section fills that hole.
> Criterion: **if the output is one image (or a set) with data as the protagonist that can be read independently of interaction**, it goes here; a clickable site goes to the Web section, something paged through goes to the PPT section.

#### Bold

**Personal Annual Report (Feltron-style)** `Bold · fidelity 94%`
- Reference: Nicholas Felton's *Feltron Annual Report* 2005–2014 (the 2006-2011 volumes are in MoMA's permanent collection); Stefanie Posavec; Bloomberg Businessweek annual specials
- Fits: personal or team annual summaries, quantified-self, product annual reviews, Wrapped-type retrospectives, long-cycle self-audits
- Visual DNA: Palette = uncoated-paper warm-white background + a single vermilion running through as the accent + slate blue for the second data series + the third color bound to exactly one meaning and never reused. Typeface = tightly set Helvetica-family, giant numbers pressing down from the top, dense small-type footnotes. Four master pieces: (1) giant-number module strip (2) polar cycle chart (24h / 12 months) (3) calendar heat grid (4) a time or geography band running across the full width. Signature = the contrast of treating private trivial data like a corporate annual report, modular printed grid, 1px dividers, still legible when printed in black and white
- HTML implementation: CSS Grid for modules + 1px border cutting the grid; polar charts in inline SVG with hand-computed polar angles (no chart library); calendar via Grid + child-element height fill. Pure typesetting + SVG, zero assets, a very strong suit of HTML
- Fonts: Archivo / Helvetica Neue (tight giant numbers) + Inter (small footnotes)

**Explanation Graphics (Nigel Holmes-style)** `Bold · fidelity 76%`
- Reference: Nigel Holmes (TIME's graphics director 1978–1994, founded Explanation Graphics in 1994); advocated explaining abstract numbers with pictures and humor, and was also the lightning rod of the chartjunk debate
- Fits: popular-science explainers, explaining complex concepts to laypeople, mass-media column illustrations, children's and educational contexts
- Visual DNA: Palette = high-saturation flat three or four colors + black outlines. Typeface = rounded sans-serif + handwritten-feel annotations. Masters = draw the chart itself as a physical metaphor (banknotes stacked into columns, a thermometer as a gauge, a running track as a progress bar). Signature = literalized charts, humor, little human figures, thick outlines, zero gradients
- HTML implementation: the chart skeleton can be done in CSS / SVG, **but the soul is the hand-drawn illustration** -- under pure HTML it can only be downgraded to geometric color blocks, and the downgrade must be explicitly stated; with image-generation capability (here: the BTC Gateway image API only), generate the illustration elements without text and then composite
- Fonts: Nunito / Baloo 2 (rounded) + Caveat (handwritten annotations)

**Cross-Section Epic (giant hand-drawn cross-section, SCMP Arranz-style)** `Bold · fidelity 55%`
- Reference: Adolfo Arranz (veteran SCMP graphics editor, multiple Malofiej international infographics gold medals, signature work *City of Anarchy*, a cross-section of Kowloon Walled City); Malofiej is called the Pulitzer of infographics
- Fits: architecture / history / artifact anatomy, long scrolls that take ten minutes to read as a single image, museum-grade popular science
- Visual DNA: Palette = dark base (deep ink / dark brown) + warm highlights + aged-paper texture. Composition = a single giant image, isometric or sectional-cut viewpoint, dense leader-line annotations surrounding the subject. Signature = hand-drawn detail, leader-line annotations, cross-section viewpoint, one image telling the entire story
- HTML implementation: 🔴 **Pure HTML cannot produce a hand-drawn cross-section** -- this style must have illustration assets; do not pretend when there are none. HTML only handles the leader-line annotation layer and zoom / scroll interaction. If assets are unavailable, switch styles
- Fonts: Source Serif (headlines) + Inter (annotations)

**Magazine Pop Data (Businessweek-style)** `Bold · fidelity 90%`
- Reference: Bloomberg Businessweek (Richard Turley era), WIRED chart pages, The Economist's Graphic Detail column
- Fits: business / tech media charts, opinion-column illustrations, social-media square images, data graphics embedded in WeChat Official Account posts
- Visual DNA: Palette = clashing two primaries (fluorescent yellow + black, magenta + navy) + paper-white whitespace, no third color to reconcile. Typeface = ultra-bold condensed large headline + tiny caption text, a type-size contrast of 10x or more. Masters = one chart, one argument; the chart itself is the layout's protagonist; the headline states the conclusion directly. Signature = extreme type-size contrast, clash colors, the chart bleeding outside the type area, conclusion-style headlines
- HTML implementation: fully reproducible in pure CSS; charts in inline SVG or CSS Grid bars; bleed via negative margin. Zero assets
- Fonts: Archivo Black / Anton (condensed bold) + IBM Plex Sans (captions)

**ISOTYPE Pictorial Statistics (Neurath–Arntz)** `Bold · fidelity 88%`
- Reference: the ISOTYPE international pictorial education system founded by Otto Neurath and Gerd Arntz in 1920s Vienna
- Fits: population / social / public-policy data, public communication for low-literacy audiences, educational posters
- Visual DNA: Palette = a limited set of spot colors (black + red + blue + ochre) in flat fills, no gradients, no shadows. Masters = the same icon repeated N times to represent quantity -- **enlarging an icon to represent more is wrong**, the most central rule of the system. Signature = arrays of silhouette icons, horizontal arrangement, text labels on the left, an extremely strong sense of order
- HTML implementation: icons as inline SVG silhouettes + CSS repeat layout, a natural fit for HTML. Icons can be self-drawn geometric silhouettes, no external assets needed
- Fonts: Jost / Archivo (Futura substitutes)

**Data Humanism (hand-drawn data maps, Lupi-style)** `Bold · fidelity 80%`
- Reference: Giorgia Lupi (Pentagram partner) and Stefanie Posavec's *Dear Data*; Lupi's Data Humanism manifesto holds that "data are people, not numbers"
- Fits: personalized, emotional data; deep description of small samples; turning private experience into a readable map; topics with many non-quantitative dimensions
- Visual DNA: Palette = journal-paper off-white background + 4-5 soft colors each bound to its own meaning (coral / pine green / mustard yellow / ink purple), **not one color is decoration**. Masters = (1) first define a visual language (size / shape / spikes / tail each encode one dimension) (2) a legend is required to teach readers to decode (3) elements arranged along organic paths, not a grid. Signature = decodable custom symbols, a mandatory legend, organic arrangement
- HTML implementation: symbols generated parametrically in inline SVG (radius / spike count / tail length bound to data fields); paths via Bézier curves through points. Pure SVG, zero assets; the only thing it cannot do is genuine hand-drawn brush strokes
- Fonts: Georgia / Source Serif (headlines) + Inter (legend)

**Scrollytelling (The Pudding-style)** `Bold · fidelity 85%`
- Reference: The Pudding (data journalism magazine), NYT The Upshot, Reuters Graphics scrolling features
- Fits: complex arguments that need to be revealed step by step, long-form data stories, web-based features
- Visual DNA: Palette switches per chapter but keeps a single accent running throughout. Masters = text steps on the left, graphics on the right morph with scroll; each screen advances only one variable. Signature = the graphic does not change but morphs, text and graphics strictly bound, chapter color changes, a complete panorama at the end
- HTML implementation: IntersectionObserver triggering state switches + CSS transition or SVG attribute interpolation, fully reproducible in pure front-end. ⚠️ The delivery form must be a web page; **exporting to PDF/PNG loses the entire narrative** -- do not pick it when the user wants a static image
- Fonts: Inter / Source Serif (long-form readability first)

**Cartographic Lead (the map as protagonist, Stamen-style)** `Bold · fidelity 65%`
- Reference: Stamen Design (founded by Eric Rodenbeck in San Francisco in 2001, clients include National Geographic), whose Watercolor / Toner map tiles are public classics
- Fits: geographic distribution data, city / transport / environment topics, content where location is the narrative
- Visual DNA: Palette = the base map sets the tone (watercolor or monochrome Toner) + data layers in high-contrast points and lines. Masters = the map fills the type area, data overlaid as point density or flow lines, the legend extremely small and tucked into a corner. Signature = the base map itself has authorship, a restrained data layer, geographic shapes as composition
- HTML implementation: 🔴 **Requires real geographic data (GeoJSON) and a base map**; pure HTML cannot conjure correct terrain from nothing -- if the data is unavailable, switch styles, **never hand-draw a fake map**. With data, inline SVG projection drawing can be used
- Fonts: Inter / IBM Plex Sans (place-name labels need lots of small type)

#### Neutral

**Newsroom Chart System (FT-style)** `Neutral · fidelity 96%`
- Reference: the Financial Times' Chart Doctor team and its public Visual Vocabulary (choosing charts by category: Deviation / Correlation / Ranking / Distribution / Change-over-Time / Part-to-Whole / Magnitude / Spatial)
- Fits: finance and industry data, occasions where "choosing the right chart type" matters more than "looking good", when a series of charts needs a unified standard
- Visual DNA: Palette = the signature pink-salmon newspaper background + an ordered color scale (single-hue gradient for continuous quantities, contrasting two colors for deviation). Masters = (1) the title is the conclusion (2) the subtitle states the basis of measurement (3) the chart body with borders and gridlines removed (4) the data source must be marked at bottom left. Signature = choose the chart type by the data relationship first and discuss beauty afterwards, the source note cannot be omitted, minimal axes
- HTML implementation: line and bar charts in pure CSS / SVG; the key is to **consult the Visual Vocabulary first to choose the right chart type** before starting. Zero assets
- Fonts: Inter / Source Sans (body) + a monospace face for numbers

**Computational Portrait (Fathom-style)** `Neutral · fidelity 78%`
- Reference: Ben Fry and his Boston studio Fathom Information Design (Fry is a co-creator of Processing and author of *Visualizing Data*; his work has appeared in the Whitney Biennial)
- Fits: very-large-scale datasets, topics that need "letting the data grow its own shape", genes / traffic / time series
- Visual DNA: Palette = white or near-black background + extremely thin lines + single-color transparency stacking to build density. Masters = no summarizing, present the full volume, forming the graphic through the overlay density of a massive number of fine elements. Signature = hairlines, transparency stacking, no decoration, shape decided by algorithm rather than layout
- HTML implementation: programmatic drawing with Canvas or large numbers of SVG paths; Canvas is mandatory when the data volume is large. **Requires real full-volume data**; a small sample cannot achieve this style's density
- Fonts: Inter / Roboto Mono (data annotation)

**Beautiful Information (McCandless-style)** `Neutral · fidelity 90%`
- Reference: David McCandless's *Information is Beautiful* and its namesake website, known for "turning big datasets into colorful graphics comparable at a glance"
- Fits: popular-science comparisons, rankings, mass-audience data aggregation, social-media-shareable charts
- Visual DNA: Palette = multi-color but a harmonious color wheel of equal lightness and saturation (not random clash colors). Masters = chart types where "area equals quantity" -- bubble / treemap / Sankey -- dominate, with labels pressed directly onto the color blocks. Signature = area encoding, same-tone multi-color, legend embedded, dozens of entries in one image
- HTML implementation: treemaps and bubbles via CSS Grid or SVG computed layouts (you need to write a simple bin-packing algorithm yourself); Sankey via SVG Bézier. Zero assets
- Fonts: Nunito Sans / Inter

**Open Research Data (Our World in Data-style)** `Neutral · fidelity 94%`
- Reference: Our World in Data (Oxford's Global Change Data Lab), whose principles are interactive charts, clearly stated basis of measurement, downloadable data
- Fits: rigorous topics, data displays that must withstand scrutiny, long-term trend comparison
- Visual DNA: Palette = white background + a set of categorical colors that are distinct but not harsh + grey for non-focal series. Masters = (1) a one-sentence conclusion title (2) the basis of measurement and time range written in the subtitle (3) labels placed directly at line ends in the chart (no legend) (4) source and license noted at the bottom. Signature = line-end labels replacing the legend, greying non-focal series, transparent basis of measurement, restraint
- HTML implementation: pure SVG lines + end-of-line text positioning, one of the most stable categories for HTML. Zero assets
- Fonts: Inter / Lato

**Speculative Tech Diagram (Eastern speculative tech diagram, Takram-style)** `Neutral · fidelity 84%`
- Reference: Takram (a design-engineering studio in Tokyo and London, practicing speculative design spanning design and engineering)
- Fits: technical concept diagrams, future-scenario speculation, research white-paper illustrations, product-architecture narratives
- Visual DNA: Palette = beige-grey sand base + low-saturation natural colors (moss green / terracotta) + one touch of metallic grey. Typeface = light weight, wide tracking, refined Chinese-English mixed typesetting. Masters = charts arranged like artworks, abundant whitespace, geometric figures with a sense of precision. Signature = soft tech feel, precise geometry, restrained natural colors, charts like installations
- HTML implementation: reproducible in pure CSS / SVG; the key lies in whitespace proportion and restraint in line width (0.5-1px). Zero assets
- Fonts: Inter (light weight) / Noto Sans JP + Cormorant (optional for headlines)

**Pictogram System (Otl Aicher-style)** `Neutral · fidelity 92%`
- Reference: the icon system Otl Aicher designed for the 1972 Munich Olympics and the Ulm School grid method
- Fits: flowcharts, wayfinding and guide-type infographics, multilingual scenarios, cases where an entire icon set must stay consistent
- Visual DNA: Palette = a restricted palette (light blue / green / silver in the Olympic version) + black. Masters = all icons share the same grid and the same stroke angles (only 0/45/90°), icons appear paired with short labels. Signature = strict angle constraints, systemic consistency, short sans-serif labels, visible grid
- HTML implementation: icons self-drawn in inline SVG under the 45° constraint; grid via CSS Grid. Zero assets, but you must keep the angle discipline yourself
- Fonts: Jost / Archivo (Univers substitutes)

#### Quiet

**Small Multiples (Tufte small-multiples matrix)** `Quiet · fidelity 95%`
- Reference: the small multiples and sparkline concepts from Edward Tufte's *Envisioning Information*
- Fits: multi-dimensional side-by-side comparison, grouped time series, one variable's performance across dozens of slices
- Visual DNA: Palette = white background + black lines + one accent color flagging anomalies. Masters = the same small chart repeated N times with only the data changed, **sharing the axis range -- without a uniform range comparability is lost, the single fatal error of this school**; labels extremely small, pressed beside the chart. Signature = a gridded repetition of small charts, shared scales, zero legends, zero gridlines, high data-ink ratio
- HTML implementation: CSS Grid to lay out the small charts + an inline SVG line in each cell. Be sure to unify the domain. Zero assets
- Fonts: Source Serif (headlines) + Inter (small labels)

**Topological Transit Map (topologically simplified network map, Beck/Vignelli-style)** `Quiet · fidelity 86%`
- Reference: Harry Beck's 1933 London Underground map, Massimo Vignelli's 1972 New York subway map
- Fits: process and relationship networks, org charts, system topologies, any diagram where "connection relationships matter more than real distance"
- Visual DNA: Palette = white or light base + one high-saturation pure color per line. Masters = all line segments run only at 0/45/90° and stations are equally spaced -- **sacrificing geographic accuracy for readability** is the foundation of this school; interchange points use hollow circles. Signature = eight-direction constraint, equidistant nodes, pure-color lines, hollow nodes
- HTML implementation: inline SVG polyline with strictly constrained angles; nodes via circle. Pure geometry, a perfect fit for HTML
- Fonts: Jost / Inter (station names may be all caps)

**Ma & Emptiness (Kenya Hara-style whitespace infographic)** `Quiet · fidelity 82%`
- Reference: Kenya Hara's *White* and the MUJI visual system, "whitespace is not emptiness, it is a vessel that holds imagination"
- Fits: brand annual reports, slow-paced narratives, small amounts of important data, occasions needing gravitas
- Visual DNA: Palette = pure white or rice-paper white + very light grey + one tiny dot of ink color or vermilion. Masters = one data point per screen, vast whitespace, elements placed at edges or golden-ratio positions, never filled up. Signature = extreme whitespace, single-point emphasis, lines so fine they are nearly nothing, the Eastern "ma" (interval)
- HTML implementation: pure CSS typesetting. 🔴 **The highest-risk style in this library** -- the whitespace must be composition (with a clear visual anchor); overdo it and it reads as "the page rendered broken"; body text must still be >=14px, and font size must not be shrunk for the sake of mood
- Fonts: Noto Serif SC / Source Han Serif + Inter

**Bookcraft Data (book-grade information typography, Irma Boom-style)** `Quiet · fidelity 80%`
- Reference: Irma Boom (Dutch book designer, work in MoMA's permanent collection, known for extreme typography and material experiments)
- Fits: long-form data reports, annual reports meant to be collected as publications, in-depth content mixing text and images
- Visual DNA: Palette = paper color + one or two ink colors, color blocks pressed over large areas. Typeface = typography itself is the protagonist, an enormous range of type sizes, asymmetric page margins, text that may be vertical or rotated. Masters = embed data into the text flow, chapter pages separated by full-bleed color blocks. Signature = asymmetric type area, extreme type-size range, typographic experiments, publication texture
- HTML implementation: CSS multi-column + writing-mode can do vertical text; the asymmetric type area via Grid. **What cannot be done is paper material and trimming**; on screen, typographic tension must compensate
- Fonts: Fraunces / EB Garamond + Archivo (contrast)

**Scientific Figure Plate** `Quiet · fidelity 96%`
- Reference: the figure guidelines of Nature and Science, public scientific plates from USGS and NASA
- Fits: research conclusions, method comparisons, rigorous data needing a peer-review feel, multi-panel compositions
- Visual DNA: Palette = white background + a colorblind-friendly palette (use blue-orange contrast rather than red-green) + greyscale. Masters = subpanels labeled (a)(b)(c), a paragraph-form caption below the figure, error bars and sample sizes always marked, axes with tick marks. Signature = subpanel numbering, long captions under figures, error bars, colorblind-safe, zero decoration
- HTML implementation: CSS Grid to lay out subpanels + SVG to draw figures and error bars; captions as small-type paragraphs. Zero assets, HTML is fully capable
- Fonts: Inter / Source Sans + Roboto Mono (numbers)

**Swiss Grid Report (Müller-Brockmann-style)** `Quiet · fidelity 97%`
- Reference: Josef Müller-Brockmann's *Grid Systems in Graphic Design*, the Ulm School, the Swiss International Style annual-report tradition
- Fits: corporate annual reports, institutional reports, series documents that need to reuse one layout over the long term
- Visual DNA: Palette = white background + black + a single accent color. Masters = a strict modular grid (commonly 12 columns), all elements snapping to column lines, flush-left ragged-right, plenty of breathing whitespace without being empty. Signature = visible grid logic, Helvetica family, non-centered typesetting, hierarchy through type size and spacing rather than decoration
- HTML implementation: CSS Grid maps directly onto the column grid, the style in this library most isomorphic with HTML. Zero assets
- Fonts: Inter / Archivo (Helvetica substitutes)

---

## ⚠️ AI-Image-Specific Styles (recommend only when the user is confirmed to have image-generation capability; not selectable by default)

The soul of the styles below lies in **dynamically generated visuals / 3D / particles / cinematic light and shadow / hand-drawn illustration**. Under pure HTML/CSS with no image generation they can only produce severely degraded mocks, so they are **removed from the default recommendation pool**. Only when the team has image-generation capability (in this toolkit: the BTC Gateway image API only) do they become candidates:

| Style | Soul | Why HTML cannot do it |
|-------|------|----------------------|
| Active Theory (WebGL particles) | 3D particle systems / real-time rendering | Impossible in pure CSS |
| Field.io (generative art) | Algorithmically generated graphics | Static SVG can only produce a stiff simplified version |
| Resn (illustrated interaction) | Character illustration + gamification | Depends on hand-drawn assets |
| Zach Lieberman (real-time generation) | Creative-coding brushwork | Depends on real-time generation |
| Raven Kwok (fractal parameters) | Recursive fractals | CSS cannot achieve the complexity |
| Ash Thorp (cinematic lighting) | Cinematic volumetric light / concept art | CSS light and shadow is degraded |
| Territory Studio (FUI holograms) | Sci-fi holographic interfaces | Depends on many layered glow assets |
| Neo Shen (ink-wash bloom) | Organic ink-wash blooming | CSS gradients != ink wash |
| Sagmeister & Walsh (color eruption) | Handmade physical objects + experimental typography | The clashing-color skeleton can be done (already folded into Web "Memphis Maximalism" and PPT "Mono-Brand Type-as-Hero"), the handmade texture cannot |

> These styles are not "bad", the "medium is wrong" -- their native medium is AI-generated images, not the browser DOM.

---

## Default Aesthetic Forbidden Zones (the user may override per their own brand)

- ❌ **The GitHub-dark lazy solution**: a uniform deep-blue background (#0D1117) + generic cyan / purple neon glow -- only this one overused combination is banned, not "dark is always banned"
- ✅ **Not in the forbidden zone**: cinematic dramatic light and shadow, warm cyberpunk (Ash Thorp orange / cyan), motion-poetics dark-stage narratives -- dark with authorial intent is kept (this library's "Linear dark glow", "Black Big-Number Stage", and "CS50 candy stage" are all legitimate dark styles)
- ❌ The all-purpose aggressive purple-gradient formula, emoji as icons, rounded cards + colored left-border accent (unless the brand itself uses it)
- ❌ Adding a personal signature / watermark to cover images

---

## Prompting Philosophy When Image Generation Is Available (Mood, Not Layout)

> Applies only when taking the AI image-generation path; on the HTML path, just write code following each style's "HTML implementation" above.

Short prompts > long prompts. Describing mood and content works better than piling on 30 lines of layout detail.

| Phrasing that kills diversity | Phrasing that sparks creativity |
|------------------------------|--------------------------------|
| Specifying color proportions (60%/25%/15%) | Describing mood ("warm like Sunday morning") |
| Dictating layout positions | Citing a specific aesthetic ("Pentagram editorial feel") |
| Listing every visual element | Describing what the audience should feel |

For image-generation methodology in this toolkit -> `../../../../skills/aitc-image-director/SKILL.md`.

---

**Version**: v3.1 (2026-06 refactored into an HTML-native library; 2026-08 added the infographic section, 40 → 60 styles)
**Applies to**: the default HTML path for all visual design -- web / PPT / PDF / infographic / cover / App, etc.
