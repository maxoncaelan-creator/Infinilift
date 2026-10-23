---
name: alio-humaniser
description: Rewrites or writes marketing copy so it reads like a real person wrote it for one specific business, not like generic AI output. Built on the StoryScope study (arXiv 2604.03136), which found AI writing gives itself away through how it is built (explaining the moral, stock feelings, one tidy arc, no named real-world details, sameness) far more than through words like "delve" or em dashes. Use for Alio! Brand Studios copy and any client copy Alio! writes, such as website pages, Google Business Profile posts, Google Ads, social captions, cold emails, proposals and monthly reports. Use it whenever the user says humanise or humanize, "make this sound less AI", "this sounds like ChatGPT", "too generic", "punch this up" or "tighten this copy", pastes AI-written copy for review, or asks for a fresh draft of marketing copy, even if they don't name the skill.
---

# Alio! Humaniser

Copy that sounds AI-written gets skimmed and distrusted. This skill fixes that by changing what the copy is **made of**, not just which words it uses.

## Why this works (the short version)

The StoryScope study (University of Maryland and Google DeepMind, 2026) gave the same 10,272 prompts to one human writer and five AI models, then compared how the 61,608 stories were *built*. The findings that matter here:

- **Construction gives AI away, not vocabulary.** Structure alone identified AI stories with a 93.2% score. When the AI stories were edited to remove clichés and purple prose, detection barely moved (95.5% to 93.9%).
- **Every AI makes the same default choices.** All five models clustered together; human writing was spread out and rarer. AI copy for a plumber in Penrith reads like AI copy for a physio in Perth.
- **The specific defaults:** AI explains its point out loud, reaches for body feelings and smells, follows one tidy arc, avoids naming real things, talks in speeches, and wraps everything up with a bow.

So swapping "elevate" for "improve" won't make copy sound human. Real specifics, a reason for every sentence, and choices only this business could make will. Details and caveats are in `references/paper-findings.md`.

## The rule that matters most: never invent specifics

Humanising means adding **real** detail. Made-up detail is worse than generic: invented reviews, stats, customers or staff can breach the Australian Consumer Law, and health practitioners can't use testimonials at all under AHPRA's advertising rules. It also wrecks the trust this skill exists to build.

If a detail is missing, ask for it or leave a clear placeholder such as `[SUBURB]`, `[YEARS TRADING]` or `[REVIEW QUOTE: needs the customer's OK]`. A draft with three honest placeholders beats a finished draft with one invented fact.

## Workflow

### 1. Work out the job

- **Rewrite or new draft?** For a rewrite, keep the facts and intent and change the construction. For a new draft, gather material first (step 2).
- **Who is speaking?** Alio! itself: read `references/alio-voice.md`. A client: use their voice if they have one, otherwise plain, friendly Australian English. The humanising rules apply either way.
- **Format and channel:** check the limits table below, since limits shape structure.
- **The one thing the reader should do or believe** after reading. If you can't say it in a sentence, ask.

### 2. Gather the fuel

Generic copy is what you get when there's no material. Look for these in the user's message, pasted copy, and repo files (for Alio!: `docs/business-plan.md`, `index.html`, `docs/brand-guidelines/`):

| Fuel | Examples |
|---|---|
| Place | Suburbs served, street, landmarks, "10 minutes from Westfield Penrith" |
| Numbers | Years trading, review count and rating, response time, prices, results with dates |
| People | Owner's name, who answers the phone, who turns up |
| Customer words | Phrases from real reviews, questions customers actually ask |
| The offer | What's on, the price, the next step and what happens after it |
| Honest limits | What they don't do, minimum budget, how long results take |
| Proof | Before and after numbers, awards, licences, memberships |

Ask for what's missing, at most five questions and only ones that change this piece. If the user wants a draft now, write it with placeholders and list what you need underneath.

### 3. Diagnose (rewrites)

Two passes, in this order, because construction is where the AI feel lives:

1. **Construction pass:** check the nine tells in the next section. Note which ones appear.
2. **Surface pass:** run `python3 scripts/tell_scan.py <file>` (or pipe the text in) to flag stock phrases, explaining lines, em dashes, exclamation marks and US spellings. Treat the flags as prompts to look again, not orders.

### 4. Rebuild, construction first

Fix the construction tells, then polish the words. Keep structure simple and clear. The human part of good copy is the material and the choices, not cleverness.

### 5. Check before you hand it over

- **Swap test:** replace the business name with a competitor's. If the copy still works, it's generic. Add at least two things only this business can say.
- **Last-line test:** delete the last sentence of each paragraph. If nothing is lost, leave it deleted. This catches most "explaining the moral" lines.
- **Proof test:** every claim traces back to something the user gave you. Anything that doesn't becomes a placeholder.
- **Read-aloud test:** would the owner say this to a customer at the counter? If not, rewrite it until they would.
- **Limits:** count characters for ads, bios and meta descriptions.

## The nine construction tells

Each one comes from a StoryScope finding (AI rate vs human rate where the paper gives one).

| # | Tell | In copy it looks like | Fix |
|---|---|---|---|
| 1 | **Explaining the moral** (narrator spells out the theme: 77% AI vs 52% human) | "…which means more calls for you." "Because your family deserves peace of mind." "The result? Total confidence." | Cut it. End on the fact, the proof or the next step. Trust the reader to connect the dots. |
| 2 | **Stock body feelings and senses** (emotion through physical sensation: 81% vs 38%; smell imagery: 82% vs 57%) | "That sinking feeling when…" "Breathe easy." "The aroma of freshly brewed coffee…" | Swap in one observed detail from this business, or a customer's own words from a review. |
| 3 | **One tidy arc, every time** (no subplots: 79% vs 57%; hero fixes everything: 69% vs 46%) | Every piece runs problem, agitate, we fix it, happy ever after. "Say goodbye to X and hello to Y." | Choose the opening that fits the format: the number, the quote, the local fact, the price, or the question customers really ask. Clear is good; formulaic isn't. |
| 4 | **No named real-world details** (named references: 24% AI vs 47% human) | "The local area." "Our community." "Industry-leading equipment." | Name the suburb, the street, the equipment brand, the local club they sponsor. |
| 5 | **Sameness** (all five AIs clustered; human stories were rarer, averaging the 71st rarity percentile vs 49th) | Copy that would work for any competitor | Swap test. Add what only this business has: its history, people, area, quirks, numbers. |
| 6 | **Speeches instead of talk** (dialogue used for philosophising: 59% vs 34%) | "In today's digital landscape…" "At the end of the day, it's all about people." | Talk about the job, the price, the time, the next step. |
| 7 | **Everything perfect, no trade-offs** (morally mixed protagonists: 59% human vs 38% AI) | "Seamless." "Hassle-free." "We do it all." | Add one honest limit where it builds trust: "SEO takes 3 to 6 months." "We don't do WordPress." |
| 8 | **Nobody is talking** (addressing the reader directly: 67% human vs 39% AI) | "Our dedicated team of experts is committed to excellence." | A person talking to a person: "I'm Dave. I pick up the phone." Use "you" and "we" or "I". |
| 9 | **The neat bow** (AI resolves everything; people leave room) | "Ready to take your business to the next level?" A closing paragraph that repeats the page. | Stop when the point is made. End on one concrete next step and what happens after it. |

**Where the paper doesn't transfer.** Flashbacks, ambiguous endings and subplots are virtues in fiction but hurt marketing copy. Copy should stay clear, linear and end with one call to action. Borrow the human *material and choices*, not the literary structure.

## Surface tells (fix last, never stop here)

The paper shows these are the weakest signal. They're still worth cleaning because readers notice them:

- **Stock phrases:** elevate, unlock, seamless, leverage, delve, robust, game-changer, cutting-edge, "look no further", "whether you're X or Y", "we've got you covered", "passionate about", "dedicated team", "one-stop shop", "nestled in", "take your business to the next level".
- **Patterns:** "It's not X, it's Y." "Not just X, but Y." Colon reveals ("The secret? …"). An opening rhetorical question. Lists of three everywhere.
- **Punctuation:** em dashes, stacked exclamation marks, emoji bullets.

`scripts/tell_scan.py` flags all of these.

## Format limits

| Format | Limit | Notes |
|---|---|---|
| Google Ads headline | 30 characters (hard) | Up to 15 per responsive search ad. Make each one work alone. No symbols like ★. |
| Google Ads description | 90 characters (hard) | Up to 4. Put the offer and proof here. |
| Google Business Profile post | 1,500 characters (hard) | Only the opening shows before "more", so lead with the point. 80 to 200 words is plenty. |
| Page title / meta description | About 60 / 155 characters | Guidance: longer gets cut off in search results. |
| Instagram bio | 150 characters (hard) | |
| Social caption | No practical limit | The first line is the hook. It shows before "more". |
| Cold email | Aim for under 120 words | Say who you are, why them, one ask, and an opt-out (Spam Act 2003). |
| SMS | 160 characters per message | |

## Output format

Give the copy first, ready to paste. Then, briefly:

```
**What changed** (rewrites only): one bullet per change that matters, each naming the tell and the fix.
**Needs from you:** placeholders to fill and questions, if any.
```

For ads or anything with limits, use a table with a character count column. When several options would help (headlines, subject lines), give a handful that each lead with something different, not near-copies. For a responsive search ad, write as many headlines as the fuel supports (Google takes up to 15).

## Reference files

- `references/examples.md`: before and after rewrites for a Google Business Profile post, Google Ads, a homepage hero, a cold email and a monthly report. Read it before your first rewrite in a session; examples show the target better than rules do.
- `references/alio-voice.md`: Alio!'s voice, tone by situation, name rules and word list. Read it whenever Alio! is the one speaking.
- `references/paper-findings.md`: the StoryScope evidence, numbers and caveats. Read it when the user asks why, or when a judgement call needs grounding.
