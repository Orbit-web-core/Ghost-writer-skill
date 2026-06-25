# Ghost-Writer

SEO blog writing skill that **interviews you like a journalist** before writing. Produces human-sounding blogs optimized for **Google rankings** AND **AI citations** (ChatGPT, Perplexity, Claude).

## What Makes This Different

Most AI blog writers generate content from prompts. Ghost-Writer **interviews you like a journalist**, then assembles a blog from your actual words, stories, and expertise.

**The result:** Blogs that sound like YOU wrote them — not ChatGPT. And they rank on Google AND get cited by AI.

---

## How It Works

1. **Keyword Lock** — Agent researches and confirms your target keyword
2. **Interview** — 3-5 questions to extract your voice, stories, and angle
3. **Assembly** — Draft assembled from raw materials (not generated from prompt)
4. **Quality Gates** — 5 gates + 100-point scoring rubric. Below 90 = rewrite.
5. **Delivery** — Title, meta, slug, body, FAQ — ready to publish

---

## Installation

### Claude Code
```bash
/plugin install ghost-writer@orbitweb
```

### Manual Install
```bash
git clone https://github.com/orbitweb/ghost-writer.git ~/.claude/skills/ghost-writer
```

---

## Usage

Say: "Write me a blog about [topic]."

The agent will:
1. Confirm your keyword
2. Interview you
3. Write the draft
4. Score it (0-100)
5. Deliver only if 90+

---

## Architecture

```
ghost-writer/
├── SKILL.md                      # Main orchestrator
├── references/
│   ├── writing-formulas.md        # PAS, Before-After-Bridge, etc.
│   ├── seo-eeat.md               # SEO + EEAT requirements
│   ├── ai-citation.md            # GEO/AEO optimization
│   ├── voice-rules.md            # Voice calibration + AI-ism blacklist
│   ├── headline-craft.md         # Headline formulas
│   ├── interview-patterns.md     # Interview question patterns
│   └── quality-scoring.md        # 100-point rubric
└── templates/
    ├── pas.md                     # Problem-Agitate-Solve
    ├── before-after-bridge.md     # Before-After-Bridge
    ├── the-ladder.md              # The Ladder
    └── the-inversion.md           # The Inversion
```

---

## Features

- ✅ **Human voice** — Interview-first, not prompt-first
- ✅ **SEO optimized** — Keyword placement, EEAT signals, on-page SEO
- ✅ **AI citation ready** — Structured for ChatGPT, Perplexity, Claude
- ✅ **100-point rubric** — Score every draft. Below 90 = rewrite.
- ✅ **5 quality gates** — AI-ism purge, voice check, fact-check, SEO, AI citation
- ✅ **Transferrable** — Works across Claude, ChatGPT, WebCore, any AI
- ✅ **One skill, many blogs** — Reusable for unlimited topics

---

## License

MIT — Share it with your clients. Use it in your agency. Build on it.

---

Built by [OrbitWeb](https://orbitweb.net) — Revenue systems, not websites.
