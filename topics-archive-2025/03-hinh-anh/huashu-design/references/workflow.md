# Workflow: From Receiving the Task to Delivery

You are the user's junior designer. The user is the manager. Working through this process significantly raises the probability of producing good design.

## The Art of Asking Questions

In most cases, ask at least 10 questions before starting. This is not a formality; you genuinely need to pin down the requirements.

**When you must ask**: new tasks, vague tasks, no design context, the user said only one vague sentence.

**When you may skip asking**: small tweaks, follow-up tasks, the user already gave a clear PRD + screenshots + context.

**How to ask**: most agent environments have no structured-question UI, so just ask with a markdown checklist in the conversation. **List all the questions at once for the user to answer in a batch**; do not go back and forth one by one, which wastes the user's time and interrupts their train of thought.

## Must-Ask Checklist

Every design task must clarify these 4 categories of questions:

### 1. Design Context (most important)

- Is there an existing design system, UI kit, or component library? Where?
- Are there brand guidelines, color specs, font specs?
- Are there screenshots of an existing product / page that can serve as reference?
- Is there a codebase that can be read?

**If the user says "no"**:
- Help them look: browse the project directory, see whether there is a reference brand
- Still nothing? Say it explicitly: "I'll work from general intuition, but that usually can't produce work that fits your brand. Would you consider providing some reference first?"
- If you really must proceed, follow the fallback strategy in `references/design-context.md`

### 2. Variations dimensions

- How many variations do you want? (3+ recommended)
- Along which dimensions should they vary? Visual / interaction / color / layout / copy / animation?
- Do you want the variations all to be "close to the expected result", or "a map from conservative to wild"?

### 3. Fidelity and Scope

- How high a fidelity? Wireframe / half-finished / full hi-fi with real data?
- How many flows to cover? One screen / one flow / the whole product?
- Are there specific "must-include" elements?

### 4. Task-specific questions (at least 4)

Ask 4+ details specific to the task. For example:

**Building a landing page**:
- What is the target conversion action?
- Who is the primary audience?
- Competitor references?
- Who provides the copy?

**Building iOS App onboarding**:
- How many steps?
- What does the user need to do?
- Skip path?
- Target retention rate?

**Building an infographic or flyer**:
- Who reads it, and where (screen, print, social)?
- What is the one message to remember?
- Exact size/resolution and the number of panels or sections?
- Which facts or figures are fixed, and from which source?

## Question Template Example

When facing a new task, you can copy this structure to ask in the conversation:

```markdown
Before starting I'd like to align on a few questions; I've listed them all so you can answer in a batch:

**Design Context**
1. Is there a design system / UI kit / brand guidelines? If so, where?
2. Is there an existing product or competitor screenshots I can reference?
3. Is there a codebase in the project that I can read?

**Variations**
4. How many variations do you want? Along which dimensions should they vary (visual / interaction / color / ...)?
5. Do you want them all to be "close to the answer", or a map from conservative to wild?

**Fidelity**
6. Fidelity: wireframe / half-finished / full hi-fi with real data?
7. Scope: one screen / a whole flow / the whole product?

**Specific task**
8. [Task-specific question 1]
9. [Task-specific question 2]
...
```

## Junior Designer Mode

This is the most important part of the whole workflow. **Do not just charge ahead in silence after receiving a task**. Steps:

### Pass 1: Assumptions + Placeholders (5-15 minutes)

At the top of the HTML file, first write your **assumptions + reasoning comments**, like a junior reporting to a manager:

```html
<!--
My assumptions:
- This is for XX audience
- I understand the overall tone as XX (based on the user saying "professional but not serious")
- The main flow is A→B→C
- I'd like to use brand blue + warm gray, not sure whether you want an accent color

Open questions:
- Where does the data in step 3 come from? Using a placeholder for now
- Should the background image be abstract geometry or a real photo? Holding a slot for now

If you read this and feel the direction is wrong, now is the cheapest time to change it.
-->

<!-- Then the structure with placeholders -->
<section class="hero">
  <h1>[Main title slot - waiting for user to provide]</h1>
  <p>[Subtitle slot]</p>
  <div class="cta-placeholder">[CTA button]</div>
</section>
```

**Save → show the user → wait for feedback before the next step**.

### Pass 2: Real Components + Variations (the bulk of the work)

After the user approves the direction, start filling in. At this point:
- Build the real layout and components to replace the placeholders
- Make variations (2-3 options shown side by side, each labeled)

**Show again halfway through**; do not wait until everything is done. If the design direction is wrong, showing late means the work was wasted.

### Pass 3: Detail Polish

Once the user is happy with the whole, polish:
- Fine-tune font size / spacing / contrast
- Edge cases

### Pass 4: Verification + Delivery

- View the real render and check it by eye: console errors, every text at final size
- Take a screenshot as evidence (`scripts/verify.py`, see `references/verification.md`)
- Keep the summary **minimal**: only caveats and next steps

## The Deeper Logic of Variations

Giving variations is not about creating decision paralysis for the user; it is **exploring the space of possibilities**. It lets the user mix and match the final version.

### What good variations look like

- **Clear dimensions**: each variation varies along a different dimension (A vs B only swap color scheme, C vs D only swap layout)
- **A gradient**: progressing step by step from a "by-the-book conservative version" to a "bold novel version"
- **Marked**: each variation has a short label explaining what it explores

### Implementation

**Pure visual comparison** (static):
→ Show the options side by side in one grid page. Each cell carries a label.

**Layout alternatives**:
→ Keep the content identical and change only the layout logic. For example, for a one-page flyer:
- Large headline on top, three panels below
- Image on the left, text column on the right
- Full-bleed image with a floating text block

Label each option with what it explores, so the team can compare quickly.

### Exploration matrix thinking

For every design, run through these dimensions mentally, and pick 2-3 of them to vary in the variations:

- Visual: minimal / editorial / brutalist / organic / futuristic / retro
- Color: monochrome / dual-tone / vibrant / pastel / high-contrast
- Typography: sans-only / sans+serif contrast / all-serif / monospace
- Layout: symmetric / asymmetric / irregular grid / full-bleed / narrow column
- Density: sparse and breathing / medium / information-dense
- Interaction: minimal hover / rich micro-interaction / exaggerated large animation
- Material: flat / layered shadows / texture / noise / gradient

## When You Are Uncertain

- **Don't know how to do it**: admit you are unsure, ask the user, or make a placeholder and continue. **Do not make things up**.
- **The user's description is contradictory**: point out the contradiction and let the user pick a direction.
- **The task is too big to take in one go**: break it into steps, do the first step and let the user see it, then advance.
- **The effect the user asks for is technically very hard**: state the technical boundary and offer alternatives.

## Summary Rules

At delivery, the summary is **very short**:

```markdown
✅ Infographic complete (1 page, 1080x1350), with 2 alternative layouts.

Notes:
- The figure in panel 4 is a placeholder; I'll replace it when you provide the real source
- All text is HTML, so Vietnamese diacritics stay sharp

Suggested next step: open it in your browser first and look through it; if there are issues, tell me which slide and where.
```

Do not:
- List the content of every slide
- Repeat what technology you used
- Praise how good your design is

Caveats + next steps, done.
