# Design Context: Starting from Existing Context

**This is the single most important thing in this skill.**

Good hi-fi design always grows out of existing design context. **Making hi-fi from thin air is a last resort and will certainly produce generic work**. So at the start of every design task, first ask: is there anything I can reference?

## What Is Design Context

In priority order, from highest to lowest:

### 1. The user's Design System/UI Kit
The component library, color tokens, type specs, and icon system that the user's own product already has. **The ideal case**.

### 2. The user's Codebase
If the user gave you a codebase, it contains living component implementations. Read those component files:
- `theme.ts` / `colors.ts` / `tokens.css` / `_variables.scss`
- Specific components (Button.tsx, Card.tsx)
- Layout scaffold (App.tsx, MainLayout.tsx)
- Global stylesheets

**Read the code and copy exact values**: hex codes, spacing scale, font stack, border radius. Do not redraw from memory.

### 3. The user's published product
If the user has a live product but did not give you the code, ask the user or the team for screenshots. Do not fetch pages from the web yourself (toolkit rules). Screenshots show you the real visual vocabulary.

### 4. Brand guidelines / Logo / existing assets
The user may have: logo files, brand color specs, marketing materials, slide templates. These are all context.

### 5. Competitor references
When the user says "like the XX website", ask them for the URL or a screenshot. **Do not** work from the vague impression in your training data.

### 6. Known design systems (fallback)
If none of the above exist, use a recognized design system as the base:
- Apple HIG
- Material Design 3
- Radix Colors (color)
- shadcn/ui (components)
- Tailwind default palette

Tell the user explicitly which one you are using, so they know it is a starting point and not a final draft.

## Process for Obtaining Context

### Step 1: Ask the user

The must-ask checklist at the start of a task (from `workflow.md`):

```markdown
1. Do you have an existing design system / UI kit / component library? Where is it?
2. Do you have brand guidelines, color / font specs?
3. Can you give me screenshots or a URL of your existing product?
4. Is there a codebase I can read?
```

### Step 2: When the user says "no", help them look

Do not just give up. Try:

```markdown
Let me see if there are any leads:
- Did your previous projects have related designs?
- What colors / typefaces does the company's marketing website use?
- What style is your product's logo? Can you give me one?
- Is there a product you admire that could serve as a reference?
```

### Step 3: Read all the context you can find

If the user gave a codebase path, you read:
1. **First list the file structure**: find files related to style/theme/components
2. **Read theme/token files**: lift the specific hex/px values
3. **Read 2-3 representative components**: see the visual vocabulary (hover state, shadow, border, padding node pattern)
4. **Read the global stylesheet**: base reset, font loading
5. **If there is a Figma link / screenshot**: look at the image, but **trust the code more**

**Important**: **do not** glance at it and work from impression. Only after reading 30+ specific values have you really lifted it.

### Step 4: Vocalize the system you will use

After going through the context, tell the user the system you will use:

```markdown
Based on your codebase and product screenshots, the design system I distilled:

**Color**
- Primary: #C27558 (from tokens.css)
- Background: #FDF9F0
- Text: #1A1A1A
- Muted: #6B6B6B

**Type**
- Display: Instrument Serif (from @font-face in global.css)
- Body: Geist Sans
- Mono: JetBrains Mono

**Spacing** (from your scale system)
- 4, 8, 12, 16, 24, 32, 48, 64

**Shadow pattern**
- `0 1px 2px rgba(0,0,0,0.04)` (subtle card)
- `0 10px 40px rgba(0,0,0,0.1)` (elevated modal)

**Border-radius**
- Small components 4px, cards 12px, buttons 8px

**component vocabulary**
- Button: filled primary, outlined secondary, ghost tertiary, all with 8px rounded corners
- Card: white background, subtle shadow, no border

I'll start with this system. Does that look right?
```

Start only after the user confirms.

## Designing from Thin Air (fallback when there is no Context)

**Strong warning**: output quality in this situation drops significantly. Tell the user explicitly.

```markdown
You have no design context, so I can only work from general intuition.
The output will be something that "looks OK but lacks distinctiveness".
Do you want to continue, or supply some reference material first?
```

If the user insists you proceed, make decisions in this order:

### 1. Pick an aesthetic direction
Do not deliver a generic result. Pick a clear direction:
- brutally minimal
- editorial/magazine
- brutalist/raw
- organic/natural
- luxury/refined
- playful/toy
- retro-futuristic
- soft/pastel

Tell the user which one you chose.

### 2. Pick a known design system as the skeleton
- Use Radix Colors for color (https://www.radix-ui.com/colors)
- Use shadcn/ui for component vocabulary (https://ui.shadcn.com)
- Use the Tailwind spacing scale (multiples of 4)

### 3. Pick a distinctive font pairing

Do not use Inter/Roboto. Suggested combinations (free from Google Fonts):
- Instrument Serif + Geist Sans
- Cormorant Garamond + Inter Tight
- Bricolage Grotesque + Söhne (paid)
- Fraunces + Work Sans (note that Fraunces has already been overused by AI)
- JetBrains Mono + Geist Sans (technical feel)

### 4. Every key decision has reasoning

Do not choose silently. Write it in an HTML comment:

```html
<!--
Design decisions:
- Primary color: warm terracotta (oklch 0.65 0.18 25) — fits the "editorial" direction  
- Display: Instrument Serif for humanist, literary feel
- Body: Geist Sans for cleanness contrast
- No gradients — committed to minimal, no AI slop
- Spacing: 8px base, golden ratio friendly (8/13/21/34)
-->
```

## Import Strategy (the user gave a codebase)

If the user says "import this codebase as a reference":

### Small (<50 files)
Read all of it and internalize the context.

### Medium (50-500 files)
Focus on:
- `src/components/` or `components/`
- All files related to styles/tokens/theme
- 2-3 representative full-page components (Home.tsx, Dashboard.tsx)

### Large (>500 files)
Ask the user to specify the focus:
- "I want to build a settings page" → read the existing settings-related files
- "I want to build a new feature" → read the overall shell + the closest reference
- Don't aim for completeness; aim for accuracy

## Working with Figma / Design Mockups

If the user gave a Figma link:

- **Do not** expect to be able to directly "convert Figma to HTML"; that needs additional tools
- Figma links are usually not publicly accessible
- Ask the user to: export as **screenshots** and send them to you + tell you the specific color/spacing values

If only Figma screenshots are given, tell the user:
- I can see the visuals, but cannot extract exact values
- Please tell me the key numbers (hex, px), or export as code (Figma supports this)

## Final Reminder

**The quality ceiling of a project is determined by the quality of the context you get**.

Spending 10 minutes collecting context is worth more than spending 1 hour drawing hi-fi from thin air.

**When there is no context, prioritize asking the user for it rather than pushing ahead blindly**.
