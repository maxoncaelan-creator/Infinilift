# StoryScope: what the paper found and how it applies to copy

**Paper:** Jenna Russell, Rishanth Rajendhran, Chau Minh Pham, Mohit Iyyer and John Wieting, "StoryScope: Investigating idiosyncrasies in AI fiction", University of Maryland and Google DeepMind. arXiv 2604.03136, version 6 (August 2026). https://arxiv.org/html/2604.03136v6

## What they did

- Took 10,272 writing prompts. For each one there's a story by a human author and stories by five AI models (Claude, DeepSeek, Gemini, GPT and Kimi): 61,608 stories averaging about 5,000 words.
- Broke every story down into narrative choices (plot shape, time, characters, themes, how emotion is shown, and so on) and found 304 features that separate the sources.
- Trained classifiers on those features alone, with no word-level style cues.

## Headline results

| Finding | Number |
|---|---|
| Human vs AI, using story-construction features only | 93.2% macro-F1 (over 97% of what a model with style cues added gets) |
| Using just the 30 most important features | 84.8% macro-F1 |
| Telling which of the six sources wrote a story | 68.4% macro-F1 (harder) |
| Detection after editing out clichés, redundant exposition and purple prose | 93.9%, down from 95.5% (so polishing barely helped) |
| How rare a story's construction was, as a percentile (higher = more unusual) | Human 0.71 on average, AI 0.49 |
| Share of stories in the rarest 10% of the whole corpus | Human 24.7%, AI 7.1% |
| Distance between groups | Even the closest human–AI pair was further apart than the most distant AI–AI pair (6.2 vs 6.0) |

(Macro-F1 is an accuracy score out of 100% that treats both classes fairly.)

## The specific differences

| Feature | AI | Human | Copy tell (see SKILL.md) |
|---|---|---|---|
| Narrator explicitly explains the theme | 77% | 52% | 1. Explaining the moral |
| Emotion shown through physical sensation | 81% | 38% | 2. Stock body feelings |
| Smell-based imagery | 82% | 57% | 2. Stock senses |
| Single-track plot, no subplots | 79% | 57% | 3. One tidy arc |
| Protagonist-driven resolution | 69% | 46% | 3. Hero fixes everything |
| Names specific texts or authors | 24% | 47% | 4. No named real-world details |
| Dialogue used for philosophical debate | 59% | 34% | 6. Speeches instead of talk |
| Morally ambivalent protagonist | 38% | 59% | 7. Everything perfect |
| Addresses the reader directly | 39% | 67% | 8. Nobody is talking |
| Integrates subplots into the theme | 21% | 42% | (fiction only) |
| Nonlinear time, flashbacks | Rarer | More common | (fiction only) |
| Ambiguous or open endings | Rarer | More common | 9. The neat bow |

AI stories also scored about 20% higher on a 1-to-5 scale for explicit moralising.

Model-specific notes from the paper: Claude favours restrained escalation and few dream sequences; GPT leans towards gossip-driven plots and ensemble casts; Gemini, DeepSeek and Kimi were hard to tell apart from each other.

## Why it matters for copy

1. **Polishing words isn't enough.** The surface edit test is the key result: removing clichés barely changed detection. Banned-word lists help readers, but the AI feel comes from default choices underneath.
2. **Defaults make everything the same.** All five AIs made similar choices, and human work was more varied and rarer. In copy, sameness means the reader can't tell one business from another, which is fatal for local marketing.
3. **Specifics are the human signal.** Named references appeared about twice as often in human writing. For a local business, the equivalents are suburbs, people, prices, dates, review quotes and honest limits.

## Caveats (be honest about these if asked)

- **It's fiction, not marketing.** Stories averaged about 5,000 words. The copy tells are adaptations by analogy, not findings the paper tested on ads or web pages.
- **An AI did the labelling.** Features were tagged by Gemini 3 Flash, so some measurement error is baked in.
- **These are defaults, not limits.** The models were given plain prompts. The paper doesn't show that AI *can't* write differently when asked, which is exactly what this skill does.
- **It isn't a better detector.** Simple classifiers reading the raw text already scored above 99.5%. The paper's value is explaining *why* AI writing feels samey, in terms you can act on.
- **Some human traits hurt copy.** Nonlinear time, ambiguity and subplots help stories but hurt ads. Borrow the material and choices, not the literary structure.
- **Copyright:** the human stories weren't released, and 0.70% of AI stories were flagged for possible memorisation.
