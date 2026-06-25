# Quality Scoring — Ghost-Writer

Every draft scores 0-100 across 5 categories. Below 90 = rewrite. No exceptions.

## The 100-Point Rubric

| Category | Points | What to Check | Pass Threshold |
|---|---|---|---|
| **Content Quality** | 30 | Thesis present? Evidence concrete? Opinion sharp? Readability good? | 24/30 |
| **SEO Optimization** | 25 | Title (keyword front-loaded)? Headings? Meta? Slug? Links? | 20/25 |
| **E-E-A-T Signals** | 15 | First-person story? Named sources? Trust signals? | 12/15 |
| **AI Citation Readiness** | 15 | Answer-first? FAQ? Quotable lines? Entity clarity? | 12/15 |
| **Voice Match** | 15 | Matches persona lock? Sounds like user? Not ChatGPT? | 12/15 |

## Scoring Bands

| Score | Band | Action |
|---|---|---|
| 90-100 | Exceptional | Deliver immediately |
| 80-89 | Strong | Fix 1-2 minor issues |
| 70-79 | Acceptable | Rewrite weak sections |
| 60-69 | Below Standard | Major rewrite required |
| Below 60 | Rewrite | Start over with better interview |

## How to Score

**Step 1:** Run Gate 1 (AI-ism purge). Count Tier 1 hits.
- 0-2 hits: Content Quality = 30
- 3-5 hits: Content Quality = 20
- 6+ hits: Content Quality = 10

**Step 2:** Run Gate 2 (Structural AI patterns).
- Pass all checks: SEO Optimization = 25
- 1-2 minor issues: SEO Optimization = 20
- 3+ issues: SEO Optimization = 15

**Step 3:** Run Gate 3 (Voice check).
- Perfect match: Voice Match = 15
- Close but slightly off: Voice Match = 12
- Sounds generic: Voice Match = 8

**Step 4:** Check Gate 4 (Keyword-in-title).
- Keyword present: SEO Optimization += 0 (already counted)
- Keyword missing: SEO Optimization = 0 (automatic failure)

**Step 5:** Check Gate 5 (SEO + AI citation).
- EEAT checklist passed: E-E-A-T = 15
- AI citation elements present: AI Citation Readiness = 15
- Missing elements: Deduct proportionally

**Step 6:** Total the score. If below 90, identify which category(ies) dragged it down and rewrite those sections.

## Score Reporting Format

Tell the user:

```
Draft score: [X]/100

Breakdown:
- Content Quality: [X]/30
- SEO Optimization: [X]/25
- E-E-A-T Signals: [X]/15
- AI Citation Readiness: [X]/15
- Voice Match: [X]/15

Status: [Ready to ship / Needs rewrite]

Issues: [Specific sections that need work]
```
