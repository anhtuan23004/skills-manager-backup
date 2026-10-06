# Design Critique In-Depth Guide

> Detailed reference for Phase 7. Provides scoring criteria, scenario-specific emphasis, and a checklist of common issues.

---

## Scoring Criteria in Detail

### 0. Concept (Concept) · Highest weight

First ask "does this design have an idea", then look at how well it is executed. Why it sits at position 0: execution is an amplifier, and amplifying an empty concept only makes it emptier.

| Score | Criteria |
|-------|----------|
| 9-10 | Has a unique idea grown out of the user's content; the visual motif is irreplaceable |
| 7-8 | Has a clear concept; the motif relates to the content but would barely work for a similar topic too |
| 5-6 | Only style, no concept: looks good but says nothing |
| 3-4 | A generic template skin; zero concept layer |
| 1-2 | Not even the style was chosen correctly; pure decorative pile-up |

**Core question checklist**:
- What does this design say? Can you state its idea in one sentence? If you cannot, it has none
- Cover all text and logos: is the topic still recognizable? If not, the visuals carry no expression (except for typographic designs where the text is the motif; for those ask instead: does this text treatment still hold up with a different topic?)
- Does it still hold up if you swap the client / product name? **If yes = template; this dimension is directly ≤5**
- Does the form have a unique visual motif that comes from the content? (Echoes the form derivation in SKILL.md: form should be derived from the content, not drawn from a style library)

**Veto rule**: when Concept ≤5, the overall score is capped at 6.0 (the lower bound of the Good tier). The following 5 dimensions are all execution, and no amount of refined execution can pull back a design that has no idea; it is just a template polished shinier.

### 1. Philosophy Alignment (Philosophy Alignment)

| Score | Criteria |
|-------|----------|
| 9-10 | The design perfectly embodies the core spirit of the chosen philosophy; every detail has a philosophical basis |
| 7-8 | Overall direction is right and core features are in place; a few details deviate |
| 5-6 | The intent is visible, but other style elements got mixed in during execution; not pure enough |
| 3-4 | Imitates only the surface, without understanding the philosophy's core |
| 1-2 | Basically unrelated to the chosen philosophy |

**Review points**:
- Does it use the signature techniques of that designer / agency?
- Do color, typography, and layout fit that philosophy system?
- Are there any "self-contradictory" elements? (e.g. choosing Kenya Hara but stuffing it full of content)

### 2. Visual Hierarchy (Visual Hierarchy)

| Score | Criteria |
|-------|----------|
| 9-10 | The user's gaze flows naturally along the designer's intent; zero friction in getting information |
| 7-8 | Primary and secondary relationships are clear, with occasional 1-2 spots of blurred hierarchy |
| 5-6 | Headings and body can be told apart, but the middle levels are chaotic |
| 3-4 | Information is laid out flat, with no clear visual entry point |
| 1-2 | Chaotic; the user does not know where to look first |

**Review points**:
- Is the font-size contrast between headings and body sufficient? (at least 2.5x)
- Do color / weight / size establish 3-4 clear levels?
- Is whitespace guiding the eye?
- "Squint test": squint your eyes; is the hierarchy still clear?

### 3. Craft Quality (Craft Quality)

| Score | Criteria |
|-------|----------|
| 9-10 | Pixel-precise; no flaws in alignment, spacing, or color |
| 7-8 | Refined overall, with 1-2 minor alignment / spacing issues |
| 5-6 | Basically aligned, but spacing is inconsistent and color use is not systematic enough |
| 3-4 | Obvious alignment errors, chaotic spacing, too many colors |
| 1-2 | Crude; looks like a draft |

**Review points**:
- Is a unified spacing system used (e.g. an 8pt grid)?
- Is spacing consistent between elements of the same kind?
- Is the number of colors controlled? (usually no more than 3-4)
- Is the font family unified? (usually no more than 2)
- Are edges precisely aligned?

### 4. Functionality (Functionality)

| Score | Criteria |
|-------|----------|
| 9-10 | Every design element serves the goal; zero redundancy |
| 7-8 | Clearly function-oriented, with a little decoration that could be cut |
| 5-6 | Basically usable, but there are obvious decorative elements that distract |
| 3-4 | Form over function; the user has to work to find information |
| 1-2 | Completely drowned in decoration; has lost the ability to convey information |

**Review points**:
- Would the design get worse if any element were removed? (If not, it should be removed)
- Are the CTA / key information in the most prominent position?
- Are there elements added "because they look nice"?
- Do information density and medium match? (PPT should not be too dense; PDF can be denser)

### 5. Originality (Originality)

| Score | Criteria |
|-------|----------|
| 9-10 | Refreshing; found a unique expression within the philosophy framework |
| 7-8 | Has its own ideas; not a simple template application |
| 5-6 | Middle of the road; looks like a template |
| 3-4 | Heavy use of clichés (e.g. a gradient orb to represent AI) |
| 1-2 | Entirely a template or assembled stock material |

**Review points**:
- Does it avoid common clichés? (see "Top 10 Common Design Issues" below)
- While following the design philosophy, is there personal expression?
- Are there "unexpected but reasonable" design decisions?

---

## Scenario-Specific Review Emphasis

Different output types call for different review emphasis (the Concept dimension is not in the table: it is the first gate for all scenarios and does not take part in emphasis trade-offs):

| Scenario | Most important dimension | Second | Can be relaxed |
|----------|--------------------------|--------|----------------|
| WeChat Official Account cover / illustration | Originality, Visual Hierarchy | Philosophy Alignment | Functionality (a single image involves no interaction) |
| Infographic | Functionality, Visual Hierarchy | Craft Quality | Originality (accuracy first) |
| PPT/Keynote | Visual Hierarchy, Functionality | Craft Quality | Originality (clarity first) |
| PDF/whitepaper | Craft Quality, Functionality | Visual Hierarchy | Originality (professionalism first) |
| Landing page / official site | Functionality, Visual Hierarchy | Originality | — (demanding across the board) |
| App UI | Functionality, Craft Quality | Visual Hierarchy | Philosophy Alignment (usability first) |
| Xiaohongshu (RED) illustration | Originality, Visual Hierarchy | Philosophy Alignment | Craft Quality (atmosphere first) |

---

## Top 10 Common Design Issues

### 1. AI-tech cliché
**Problem**: gradient orbs, digital rain, blue circuit boards, robot faces
**Why it is a problem**: users are already visually fatigued by these and cannot tell you apart from everyone else
**Fix**: replace literal symbols with abstract metaphors (e.g. use the metaphor of "conversation" rather than a chat-bubble icon)

### 2. Insufficient type-size hierarchy
**Problem**: the gap between headings and body is too small (<2.5x)
**Why it is a problem**: users cannot quickly locate key information
**Fix**: headings at least 3x body (e.g. body 16px → heading 48-64px)

### 3. Too many colors
**Problem**: uses 5+ colors with no primary or secondary
**Why it is a problem**: visual chaos, weak brand feel
**Fix**: limit to 1 primary color + 1 secondary color + 1 accent color + grayscale

### 4. Inconsistent spacing
**Problem**: element spacing is arbitrary, with no system
**Why it is a problem**: looks unprofessional, with a chaotic visual rhythm
**Fix**: establish an 8pt grid system (use only 8/16/24/32/48/64px for spacing)

### 5. Insufficient whitespace
**Problem**: all space is filled with content
**Why it is a problem**: crowded information causes reading fatigue and actually lowers the efficiency of information delivery
**Fix**: whitespace should be at least 40% of the total area (60%+ for minimalist styles)

### 6. Too many fonts
**Problem**: uses 3+ fonts
**Why it is a problem**: visual noise, weakened unity
**Fix**: at most 2 fonts (1 for headings + 1 for body); create variation with weight and size

### 7. Inconsistent alignment
**Problem**: some elements left-aligned, some centered, some right-aligned
**Why it is a problem**: breaks the sense of visual order
**Fix**: choose one alignment (left alignment recommended) and apply it globally

### 8. Decoration over content
**Problem**: background patterns / gradients / shadows steal the spotlight from the main content
**Why it is a problem**: priorities inverted; users come for information, not decoration
**Fix**: "Would the design get worse if this decoration were removed?" If not, remove it

### 9. Cyber-neon overuse
**Problem**: dark blue background (#0D1117) + neon glow effects
**Why it is a problem**: a default aesthetic no-go zone (this skill's taste baseline), and has become one of the biggest clichés — users may override it with their own brand
**Fix**: choose a more distinctive color scheme (refer to the color systems of the 20 styles)

### 10. Information density mismatched with medium
**Problem**: a full page of text in a PPT / 10 elements crammed into a cover image
**Why it is a problem**: different media have different optimal information densities
**Fix**:
- PPT: 1 core point per slide
- Cover image: 1 visual focus
- Infographic: show in layers
- PDF: can be denser, but needs clear navigation

---

## Review Output Template

```
## Design Review Report

**Overall score**: X.X/10 [Excellent(8+)/Good(6-7.9)/Needs improvement(4-5.9)/Fail(<4)]
(When Concept ≤5 the overall score is capped at 6; fix the concept first, then talk about execution)

**Dimension scores**:
- Concept: X/10 [What is this design's idea? State it in one sentence]
- Philosophy Alignment: X/10 [one-sentence explanation]
- Visual Hierarchy: X/10 [one-sentence explanation]
- Craft Quality: X/10 [one-sentence explanation]
- Functionality: X/10 [one-sentence explanation]
- Originality: X/10 [one-sentence explanation]

### Strengths (Keep)
- [Point out specifically what is done well, in design language]

### Issues (Fix)
[Sorted by severity]

**1. [Issue name]** — ⚠️Critical / ⚡Important / 💡Polish
- Current: [describe the current state]
- Problem: [why this is a problem]
- Fix: [specific action, with values]

### Quick Wins
If you only have 5 minutes, do these 3 things first:
- [ ] [Highest-impact fix]
- [ ] [Second most important fix]
- [ ] [Third most important fix]
```

---

**Version**: v1.0
**Updated**: 2026-02-13
