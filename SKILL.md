---
name: ghost-writer
description: SEO blog writing skill for Claude Code that interviews you like a journalist before writing. Produces human-sounding blogs optimized for Google rankings AND AI citations (ChatGPT, Perplexity, Claude). Use when user asks to write a blog, create content, draft an article, mentions SEO writing, or says "ghost writer." The agent interviews the user like a journalist, then assembles a publish-ready blog from raw materials — not generates it from a prompt.
metadata:
  author: OrbitWeb
  version: 2.0.0
  mcp-server: none
  license: MIT
---

# Ghost-Writer — Interview-Based SEO Blog Writing for Humans and AI

## What This Does

Ghost-Writer interviews you like a journalist, then assembles a blog post optimized for:
- **Google rankings** — keyword placement, EEAT signals, on-page SEO
- **AI citations** — structured so ChatGPT, Perplexity, and Claude mention your content
- **Human readers** — your voice, your stories, your expertise

## The Promise

Every blog passes 5 quality gates and scores 90+ on a 100-point rubric before delivery. If it fails, the agent rewrites it. No exceptions.

## How to Use

Say: "Write me a blog about [topic]." The agent will:
1. Lock your keyword
2. Interview you (3-5 questions)
3. Assemble the draft
4. Score it (0-100)
5. Deliver only if 90+

---

## Phase 1: Topic + Keyword Lock

**Agent asks:**
1. "What's the topic?"
2. "Who's this for?"

**Agent does keyword research (2 minutes):**
- Searches topic + "2026" or "statistics"
- Identifies: dominant narrative, the gap, key stats, contrarian angles
- Surfaces keyword: **"Keyword: [X]. Does this work?"**

**Gate 1:** No confirmed keyword = NO writing.

---

## Phase 2: The Interview (3-5 Questions)

**Before interviewing, lock the voice persona in 4 dimensions:**

1. **Formal ↔ Casual:** "How do you talk to customers?"
2. **Serious ↔ Funny:** "Dry and direct, or do you drop jokes?"
3. **Respectful ↔ Irreverent:** "Polite or 'call it like it is'?"
4. **Matter-of-fact ↔ Enthusiastic:** "Just facts, or do you hype?"

**Interview patterns:**
- "What's your take — is this real or noise?"
- "What do most people believe? What's the real version?"
- "Give me a specific example — client, moment, number."
- "Who loses if they get this wrong?"
- "So the blog is basically: [thesis]. Missing anything?"

**Stop when you have:**
1. Clear thesis
2. Concrete evidence
3. Strong opinion

**Gate 2:** Missing any = NO drafting.

---

## Phase 3: Assembly (Not Generation)

**Assembly rules:**
- User's exact words preserved where they hit hardest
- One idea per paragraph
- 2-4 sentence paragraphs
- Minimum 500 words
- No corporate fluff

**Pick a structure:**
- **PAS** — Problem-Agitate-Solve (pain-point topics)
- **Before-After-Bridge** — vision pieces, category creation
- **The Ladder** — news → meaning
- **The Inversion** — contrarian takes

See `references/writing-formulas.md` for full formula details.

---

## Phase 4: SEO + AI Citation Optimization

**Apply these BEFORE showing the user. See `references/seo-eeat.md` for full checklist.**

### Google SEO
- Title (H1): keyword front-loaded, 50-65 chars
- Meta description: 150-160 chars, keyword included
- URL slug: keyword only, hyphens, no dates
- Keyword placement: title, first 100 words, one H2
- Heading hierarchy: H1 → H2 → H3
- Internal links: 2-3 links
- Image alt text: descriptive

### AI Citation Optimization (GEO/AEO)
See `references/ai-citation.md` for full GEO checklist.
- Answer-first formatting
- Passage-level citability (120-180 word blocks)
- FAQ schema (3-5 Q&A pairs)
- Entity clarity
- Direct quotes
- Statistics with named sources

---

## Phase 5: The 6 Quality Gates + 100-Point Rubric

Every draft scores 0-100. Below 90 = rewrite.

| Category | Points | What to Check |
|---|---|---|
| Content Quality | 25 | Thesis, evidence, opinion, readability |
| SEO Optimization | 20 | Title, headings, meta, slug, links |
| E-E-A-T Signals | 15 | Author voice, citations, trust |
| AI Citation Readiness | 15 | Answer-first, FAQ, quotable lines, entity clarity |
| Voice Match | 15 | Matches 4-dimension persona lock |
| **Humanizer Check** | **10** | **Burstiness, AI-phrase density, specificity** |

### Gate 1 — AI-ism Purge (0/25 if failed)

ZERO tolerance for these AI tells:
- delve, tapestry, furthermore, crucial, landscape, realm, vibrant, bustling, embark, navigate, uncover, a testament to, it's worth noting that, not only...but also, in conclusion, firstly/secondly/thirdly, moreover, double-edged sword, paradigm shift, game-changer, in today's fast-paced world, a deep dive, at the end of the day, moving forward, in these unprecedented times, a new era of, ushered in, transformed the landscape, a seismic shift, multifaceted, beacon, myriad, leverage (verb), synergy, holistic, cutting-edge, robust, ecosystem, space ("in the AI space"), unlock, supercharge, demystify, master, elevate, craft, unleash, harness, dive deep, shed light on, paint a picture, weave, underscore, foster, resonate, compelling, indeed, arguably, significantly

### Gate 2 — Structural AI Patterns (0/20 if failed)
- No triplet fragments: "Not X. Not Y. Z."
- No label-explain: "Speed. X happens."
- No stacked becauses
- No multiplier escalation: "10x... 100x..."
- No smug AI-vs-human punchlines
- No em dashes
- **Burstiness check:** Sentence length must vary. Short punch. Medium flow. Long build. Fragment.

### Gate 3 — Voice Check (0/15 if failed)
- Would the user say this out loud?
- Contractions naturally (it's, they're, we're)
- Fragments sparingly (2-3 per piece)
- Direct address: "Here's what they won't tell you."
- Matches 4-dimension persona lock

### Gate 4 — Keyword-in-Title (0/20 if failed)
- Primary keyword MUST appear in the title

### Gate 5 — SEO + AI Citation Check (0/15 if failed)
- Meta description written?
- URL slug proposed?
- EEAT checklist passed?
- AI citation elements included?
- **Fact-check:** Every stat has a named source. Can't name it? Cut it.

### Gate 6 — Humanizer Check (0/10 if failed)

Run the full humanizer checklist from `references/humanizer.md`:

1. **Burstiness:** Sentence length varies? (short/medium/long/fragment)
2. **AI-phrase density:** ≤1 Tier 1 hit per 100 words?
3. **Transitions:** ≤1 per 300 words? (use "But," "So," or nothing)
4. **Hedging:** ≤1 per 300 words? (replace with confident assertions)
5. **Specificity:** More specifics than abstractions?
6. **Imperfections:** 1-2 sentences start with "And" or "But"?
7. **Colloquial drops:** 1-2 per section?
8. **Concrete details:** At least 2 details only a human would know?

**If 7+ items checked:** Score = 10
**If 4-6 items checked:** Score = 6, light humanization
**If 0-3 items checked:** Score = 3, full humanization required

See `references/humanizer.md` for full detection metrics + fix techniques.

**If ANY gate fails:** Fix before showing user. No exceptions.

**Score and tell user:** "Draft score: [X]/100." 90+ = deliver. Below 90 = rewrite.

---

## Phase 6: Headline Craft

Generate 5-7 titles using at least 3 formulas. See `references/headline-craft.md` for full formula library.

**Tests:**
- Scroll test: Would ideal reader stop scrolling?
- Promise test: Does blog deliver what title promises?
- Specificity test: Could this title apply to 100 other posts?
- Keyword test: Is keyword front-loaded?
- **Love test: Does the user say "I love it" or "that's the one" — not just "that works"?**

**Love It Gate:**
Present 5-7 titles grouped by formula type. User MUST pick one they love. If they say "that works" or "I guess" or "whatever" — that's not good enough. Iterate with 5 more titles. Keep going until they say "I love it" or "that's the one."

**Why:** The title is 80% of whether the piece gets read. If the user doesn't love it, the reader won't either.

---

## Phase 7: Delivery

**Final package:**
1. Title (H1)
2. Meta description
3. URL slug
4. Blog body (markdown)
5. FAQ section (3-5 Q&A pairs)
6. Score card (0-100, category breakdown)

**Format:** Plain text/markdown. No HTML. Ready for any CMS.

**Pro tip:** Paste the FAQ section into a separate FAQ block or schema markup. This is what makes ChatGPT and Perplexity cite your content.

---

## Troubleshooting

### "I don't have a topic"
**Fix:** Ask the user: "What frustrated you this week? What did a client say? What did you see a competitor do?" Turn any of those into a topic.

### "The interview isn't unlocking the angle"
**Fix:** Switch interview pattern. If "Pull the Thread" isn't working, try "How It Actually Happened" or "The Emperor Has No Clothes." Or ask: "What's the thing you know that nobody else does?"

### "The user doesn't love any titles"
**Fix:** Go deeper on the user's voice. Ask: "If you were writing this for a friend, what would you call it?" Use their exact words.

### "The draft scores below 90"
**Fix:** Identify which gate failed. Don't rewrite everything — fix only the failing category. If Gate 1 (AI-ism) failed, purge AI words and rescore. If Gate 6 (Humanizer) failed, vary sentence length and add concrete details.

### "Keyword research returns no results"
**Fix:** The keyword is too niche. Broaden it slightly. "revenue generating website for HVAC" → "revenue generating website for service business." Then narrow in the body.

### "User wants to skip the interview"
**Fix:** Explain: "The interview is what makes this sound like you, not ChatGPT. 3-5 questions. 2 minutes. That's what separates good blogs from generic ones."

---

## Examples

### Example 1: Trend Topic
**User:** "Write me a blog about AI replacing web designers."
**Keyword:** "AI replacing web designers" → "AI web design disruption"
**Interview:**
- "Is this real or hype?"
- "Who gets hurt? Who wins?"
- "What's the version most people believe?"
**Angle:** "They're firing brick-makers, not architects. The people who know what to build are more valuable than ever."
**Formula:** The Inversion
**Title:** "AI Fired 1,000 Web Designers. Here's Who Actually Wins."
**Score:** 94/100

### Example 2: Case Study
**User:** "Blog about Matt's moving company."
**Keyword:** "moving company revenue system"
**Interview:**
- "Walk me through the before/after."
- "What number changed?"
- "Who needs to hear this?"
**Angle:** "From 3 calls a month to 47. Not because of a prettier website — because of a revenue system."
**Formula:** Before-After-Bridge
**Title:** "How MTS Moving Went from 3 Calls a Month to 47 — Without a Redesign"
**Score:** 96/100

### Example 3: User's Idea
**User:** "I want to write about why pretty websites don't convert."
**Keyword:** "pretty websites don't convert"
**Interview:**
- "What made you realize this?"
- "What's the cost of believing pretty = effective?"
- "What's the specific alternative?"
**Angle:** "Pretty websites are digital brochures. Revenue systems are engines. The difference is $5M vs. $0."
**Formula:** PAS
**Title:** "Your Pretty Website Is Costing You $50K a Year. Here's the Fix."
**Score:** 91/100

---

## Quick Reference

**Voice rules:** See `references/voice-rules.md`
**Interview patterns:** See `references/interview-patterns.md`
**Headline formulas:** See `references/headline-craft.md`
**SEO + EEAT:** See `references/seo-eeat.md`
**AI citation optimization:** See `references/ai-citation.md`
**Quality scoring:** See `references/quality-scoring.md`
**Humanizer check:** See `references/humanizer.md`
**Writing formulas:** See `references/writing-formulas.md`
