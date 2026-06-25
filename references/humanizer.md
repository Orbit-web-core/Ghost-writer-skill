# Humanizer Check — Ghost-Writer

How to detect if content sounds like AI wrote it — and how to fix it.

## The Problem

AI content is smooth, uniform, and predictable. Human content is messy, varied, and specific. The humanizer check measures "humanness" and provides fixes.

---

## Detection Metrics

Run these checks on every draft. Score each 0-10. Total below 50 = needs humanization.

### Metric 1: Burstiness (Sentence Length Variance)

**What it measures:** AI tends to write uniform sentence lengths. Humans vary wildly.

**Check:**
- Count words in each sentence
- Calculate average and standard deviation
- AI text: most sentences within ±3 words of average
- Human text: sentences range from 3 words to 35+ words

**Score:**
- 8-10: High variance (short punch, medium flow, long build, fragments)
- 5-7: Moderate variance (some variation but mostly medium)
- 0-4: Low variance (AI-sounding uniformity)

**Fix if score < 8:**
- Find every sentence that's 15-20 words. Rewrite half of them.
- Add 2-3 short sentences (3-8 words).
- Add 1 long sentence (25+ words).
- Add 1 fragment.

---

### Metric 2: AI-Phrase Density

**What it measures:** How many Tier 1 AI-ism words appear per 100 words.

**Check:**
- Count Tier 1 AI-ism hits (from voice-rules.md)
- Divide by total word count, multiply by 100

**Score:**
- 8-10: 0-1 hits per 100 words (clean)
- 5-7: 2-3 hits per 100 words (suspicious)
- 0-4: 4+ hits per 100 words (AI-detected)

**Fix if score < 8:**
- Replace every Tier 1 hit with human alternative (see replacement table below)

---

### Metric 3: Transition Word Frequency

**What it measures:** AI overuses transitions (Furthermore, Moreover, Additionally, However).

**Check:**
- Count transition words: Furthermore, Moreover, Additionally, However, Therefore, Thus, Consequently, In addition, On the other hand, As a result
- Divide by total word count, multiply by 100

**Score:**
- 8-10: 0-1 transitions per 300 words
- 5-7: 2-3 transitions per 300 words
- 0-4: 4+ transitions per 300 words

**Fix if score < 8:**
- Replace 80% of transitions with: period + new paragraph, "But," "So," "And," or nothing.
- Keep 1-2 transitions max per 500 words.

---

### Metric 4: Hedging Frequency

**What it measures:** AI hedges constantly (might, could, potentially, arguably, perhaps, somewhat).

**Check:**
- Count hedging words: might, could, potentially, arguably, perhaps, somewhat, may, possibly, likely, presumably
- Divide by total word count, multiply by 100

**Score:**
- 8-10: 0-1 hedges per 300 words
- 5-7: 2-3 hedges per 300 words
- 0-4: 4+ hedges per 300 words

**Fix if score < 8:**
- Replace hedges with confident assertions
- "You might want to consider..." → "Do this."
- "This could potentially..." → "This will..."
- "Arguably, some..." → "Most..."

---

### Metric 5: Specificity Ratio

**What it measures:** AI writes in abstractions. Humans write in specifics.

**Check:**
- Count specific details: named people, named companies, numbers, dates, locations, concrete examples
- Count abstractions: generalizations, "many people," "some businesses," "various strategies"
- Ratio = specifics / (specifics + abstractions)

**Score:**
- 8-10: Ratio > 0.6 (more specifics than abstractions)
- 5-7: Ratio 0.4-0.6 (balanced)
- 0-4: Ratio < 0.4 (too abstract)

**Fix if score < 8:**
- Replace every "many people" with a specific number or named person
- Replace every "some businesses" with a specific example
- Add concrete details: "Last Tuesday," "Toronto Hydro," "$5K landing page"

---

## Humanizer Fix Techniques

### Technique 1: The Imperfection

Humans make minor "mistakes" that AI avoids:
- Starting a sentence with "And" or "But" (AI avoids this)
- Using a fragment. For emphasis.
- Repeating a word intentionally for rhythm
- Using a comma splice (occasionally, for effect)

**Example:**
❌ AI: "Furthermore, the implementation of revenue-generating systems requires careful consideration of multiple factors."
✅ Human: "And here's the thing about revenue systems. They work. But only if you build them right."

---

### Technique 2: The Colloquial Drop

Drop in informal phrasing that AI would never generate:

- "Here's the thing."
- "Nah."
- "Yep."
- "Big deal."
- "So what?"
- "Kind of."
- "Sort of."

**Use:** 1-2 per section. Keeps writing from sounding like a white paper.

---

### Technique 3: The Self-Correction

Humans correct themselves mid-thought. AI doesn't.

**Example:**
"Most agencies sell websites. Actually, no — they sell pretty pages. The difference matters."

"SEO takes 3-6 months. Well, that's not entirely true. We've seen results in 4 weeks with the right foundation."

---

### Technique 4: The Abrupt Pivot

Humans change direction without warning. AI transitions smoothly.

**Example:**
❌ AI: "Having discussed the technical aspects, we will now examine the financial implications."
✅ Human: "That's the technical side. Now let's talk money."

❌ AI: "Furthermore, it is important to consider the customer experience."
✅ Human: "But here's what actually matters to the customer."

---

### Technique 5: The Concrete Detail Only a Human Would Know

Add specific details that come from lived experience, not research:

- "Last Tuesday, I watched a client's Google Analytics go from 3 visitors to 47 in one hour."
- "The coffee shop on Matheson Boulevard — that's where I first pitched this to Matt."
- "It was 2:47 AM when the webhook finally fired."

**AI can't invent these.** Humans can.

---

## AI-Phrase Replacement Table

| AI Phrase | Human Replacement |
|---|---|
| delve into | dig into, go deep on |
| furthermore | And, So, Also |
| moreover | And, Plus, What's more |
| crucial | key, critical, important |
| landscape | industry, field, market |
| embark on | start, begin, jump into |
| navigate | handle, deal with, figure out |
| uncover | find, discover, figure out |
| a testament to | shows, proves, demonstrates |
| it's worth noting that | Note: [just say it] |
| not only...but also | [pick one] |
| in conclusion | [delete, or end with punch] |
| at the end of the day | [delete] |
| moving forward | Next, Going forward, From here |
| in these unprecedented times | [delete] |
| a new era of | [state what changed] |
| ushered in | caused, led to, created |
| transformed the landscape | changed, shifted |
| a seismic shift | [state the shift] |
| multifaceted | complex, complicated |
| beacon | example, model |
| myriad | many, tons, a lot |
| leverage (verb) | use, tap into |
| synergy | cooperation, working together |
| cutting-edge | new, advanced, latest |
| robust | strong, solid, tough |
| ecosystem | system, network |
| space ("in the AI space") | in AI, in the industry |
| unlock | enable, allow, open |
| supercharge | boost, improve, enhance |
| demystify | explain, clarify |
| master | learn, get good at |
| elevate | improve, raise, lift |
| craft | create, make, write |
| unleash | release, free, let out |
| harness | use, tap into, grab |
| dive deep | explore, examine, look into |
| shed light on | explain, clarify |
| paint a picture | describe, show |
| weave | combine, mix, blend |
| underscore | stress, point out, highlight |
| foster | encourage, support |
| resonate | connect, hit home |
| compelling | strong, powerful, gripping |
| indeed | yes, absolutely |
| arguably | [pick a side] |
| significantly | [give the number] |

---

## Humanizer Checklist

Before shipping, verify:

- [ ] **Burstiness:** Sentence length varies (short/medium/long/fragment)
- [ ] **AI-phrase density:** 0-1 Tier 1 hits per 100 words
- [ ] **Transitions:** 0-1 per 300 words (use "But," "So," or nothing)
- [ ] **Hedging:** 0-1 per 300 words (replace with confident assertions)
- [ ] **Specificity:** More specifics than abstractions (ratio > 0.6)
- [ ] **Imperfections:** 1-2 sentences start with "And" or "But"
- [ ] **Colloquial drops:** 1-2 per section ("Here's the thing," "Nah")
- [ ] **Self-correction:** 1 instance of mid-thought correction
- [ ] **Concrete details:** At least 2 details only a human would know

**If 7+ items are checked:** Human-sounding. Ship it.
**If 4-6 items checked:** Needs light humanization.
**If 0-3 items checked:** Full humanization required. Rewrite.
