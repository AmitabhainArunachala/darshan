---
title: The Evolution of AI
slug: evolution-of-ai
series: story-of-ai
tags: ai, evolution, paradigms, scaling, compute, data, agents, history
summary: AI did not progress by plan; it mutated through five body plans — symbolic systems, statistical methods, neural networks, foundation models, and agents. Three selection pressures — compute, data, and money — decided which survived, and this room traces that mechanism with the real numbers.
status: draft
date: 2026-08-25
terms_defined: selection pressures in ai, paradigm succession, the bitter lesson
terms_linked: history-of-ai, future-of-ai, neural-networks, deep-learning, machine-learning, pretraining-post-training, nvidia-and-the-chip, chip-wars, benchmarks, leading-models, top-papers-ai, evolution, mechanistic-interpretability, attention-economy, governments-and-ai, sense-of-self
---

# The Evolution of AI

If you've read [history-of-ai](history-of-ai.html), you have the timeline: who did what, and when. This room asks a different question: *why did the field change shape the way it did?* The claim is that the field's history makes more sense read as an evolutionary process than as a sequence of ideas, and that three selection pressures — compute, data, and money — did most of the selecting. When you finish, [future-of-ai](future-of-ai.html) is where those pressures get extrapolated forward.

## 1. Evolution here is a mechanism, not a metaphor

People say "AI evolved" the way they say a phone "evolved" — loosely, meaning it changed. I want to use the word more precisely, because the precise version explains things the loose version can't.

[Evolution](evolution.html) needs three ingredients: variation, heredity, and selection. AI research has all three, concretely.

**Variation**: thousands of labs and researchers try different approaches every year. Rule systems, probabilistic models, network architectures, training recipes. Most fail. That's not waste — that's the variation an evolutionary process runs on.

**Heredity**: successful techniques get copied. Papers, open-source code, and researchers moving between labs are the field's genetics. When one architecture works, next year's models inherit it — often literally, as forked code.

**Selection**: this is the part people miss. Ideas in AI don't win because they're elegant or because a committee decides. They win because they perform under the resource constraints of their era — and those constraints changed. What was fit in 1975 (runs on tiny computers, encodes expensive human expertise) was fatally unfit in 2015. The environment shifted, and whole lineages died.

Nobody planned the sequence symbolic → statistical → neural → foundation models → agents. No individual chose it; several of the most important figures actively resisted each transition. It happened anyway. That's the signature of selection, not design.

One honest caveat before we start: this is a *lens*, and lenses distort. Research ideas cross-breed in ways genes mostly don't, and dead paradigms revive — you'll see [neural networks](neural-networks.html) do exactly that. Hold the frame as a tool, not a law.

## 2. The symbolic era: fitness by hand (1956–~1990)

The founding bet of the field — made at Dartmouth in 1956 and dominant for three decades — was that intelligence is symbol manipulation. Write down knowledge as rules; let the machine chain the rules. If a patient has fever AND stiff neck, THEN consider meningitis.

Understand why this was the *fit* strategy for its environment, not a mistake. In 1970, compute was scarce and astronomically expensive, and digitized data barely existed. But human experts were, relatively speaking, cheap and available. The rational move was to compress human expertise into rules — spend the abundant resource (expert time) to save the scarce one (compute). Expert systems did exactly that, and in the early 1980s they made real money: DEC's XCON system configured computer orders in production, and an entire industry of specialized Lisp machines grew up to run this software.

Then the environment collapsed on it, from two directions.

First, an internal ceiling: rules don't scale. Every rule an engineer writes can conflict with the others; a system with thousands of rules becomes brittle in ways no one can debug. The knowledge you most needed — how to recognize a face, how to parse a messy sentence — turned out to be knowledge experts *couldn't articulate as rules at all*. Philosophers had warned about this (tacit knowledge); engineering confirmed it.

Second, an external shock: the hardware niche vanished. General-purpose workstations got fast enough that dedicated Lisp machines lost their reason to exist, and that market collapsed in the late 1980s, taking investor confidence with it. Funding froze. This is the period called the second AI winter — and in the evolutionary frame, a winter is exactly what it looks like: a mass extinction when the resource climate turns.

The lesson to carry forward: the symbolic paradigm didn't lose an argument. It lost a *budget*. Its selection environment — expensive compute, cheap expertise, no data — stopped existing.

## 3. The statistical turn: data becomes food (~1988–2012)

The next body plan emerged where the new resource was: data.

The clearest single case is machine translation. For decades, translation systems were built by linguists writing grammar rules. Then, around 1988–1993, an IBM group (the Candide project, led by researchers from *speech recognition*, not linguistics) tried something that offended nearly everyone: ignore grammar. Take millions of sentence pairs from the Canadian parliament's bilingual proceedings, and compute the probability that a French word or phrase translates to an English one. No understanding — counting.

It worked better. Frederick Jelinek, who led IBM's speech effort, is famously credited with the line "every time I fire a linguist, the performance of the speech recognizer goes up." (The quote's exact wording and occasion are disputed — Jelinek himself later said he didn't remember saying it quite that way — but nobody disputes that it captured what the results showed.)

Look at this transition through the selection lens and it's textbook. A new food source appeared — digitized text, then the web — and a new organism evolved to metabolize it. The statistical paradigm's fitness didn't come from being smarter about language. It came from being able to *eat data*, which rule systems couldn't. [Machine learning](machine-learning.html) as a field is essentially this body plan generalized: systems whose competence grows with data instead of with engineering hours.

This era also built the field's measurement organs: shared datasets and [benchmarks](benchmarks.html), which made selection *fast*. Once everyone evaluates on the same test set, a better method displaces a worse one in months instead of decades. Benchmarks are to AI what a shared ecosystem is to biology — the arena where fitness gets settled.

## 4. The neural takeover: a dormant gene meets a new environment (2012–2019)

Here's the part that breaks the naive "march of ideas" story completely: the winner of the next era was an *old* idea.

[Neural networks](neural-networks.html) — trainable layers of simple units, tuned by backpropagation — were developed in their modern form by the mid-1980s (backpropagation was popularized in 1986). Then they spent roughly twenty years as a marginal lineage, kept alive by a small population of researchers — Hinton, LeCun, Bengio, and their students — while the mainstream considered them a dead end. In biology this is a dormant trait: genetically present, phenotypically invisible, waiting for an environment that rewards it.

The environment arrived as two mutations, neither from AI research itself:

- **Compute**: graphics cards, built for video games, happened to be massively parallel matrix-multiplication engines — which is precisely what neural network training is. See [nvidia-and-the-chip](nvidia-and-the-chip.html) for that whole story.
- **Data**: the internet produced, and the ImageNet project (2009) organized, over a million labeled images — a dataset large enough for deep networks to show what they could do.

The measurable moment is 2012. AlexNet — a deep convolutional network by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton, trained on two consumer GPUs — entered the ImageNet competition and scored a 15.3% top-5 error rate. Second place, using the best non-neural computer-vision methods, scored 26.2%. In a field where a one-point gain was a good year, an eleven-point gap is not an improvement. It's a fitness cliff.

What followed was ecological, not intellectual. Within about three years, hand-engineered features went extinct across computer vision, then speech, then translation — each subfield's specialized methods displaced by the same general organism fed with more data and compute. [Deep learning](deep-learning.html) covers the anatomy; what matters here is the pattern: *a general method that converts compute into performance will, given enough compute, displace any specialized method.*

Richard Sutton named this pattern in a short essay in March 2019, "The Bitter Lesson," and it's the closest thing this room has to a stated law: 70 years of AI history show that general methods leveraging computation — search and learning — beat human-knowledge-engineered methods, every time, eventually. It is bitter because it means the researcher's cleverness is, in the long run, the part that gets selected *against*. Read the essay itself — it's two pages, at incompleteideas.net — and check it against every transition in this room. It holds.

## 5. Foundation models: scaling becomes the strategy (2017–2023)

Until about 2018, "more compute helps" was folk knowledge. Then it became an equation, and the equation changed who could play.

Three steps:

**The dominant body plan.** In June 2017, "Attention Is All You Need" (Vaswani et al., Google) introduced the transformer — an architecture whose core operation, attention, lets every token in a sequence weigh its relevance to every other token, all computed in parallel. Its evolutionary advantage was not that it was cleverer than its predecessors; it was that it *parallelized*, meaning it could absorb more GPU compute per dollar than recurrent networks could. The architecture best shaped to metabolize the abundant resource won. Nearly every major model since — the entire roster in [leading-models](leading-models.html) — is a transformer variant. In body-plan terms, this is the field's Cambrian moment: one architecture, endless radiation.

**The growth law.** In January 2020, Kaplan et al. at OpenAI published scaling laws: language model performance improves as a smooth, predictable power law in model size, data, and compute. In 2022, DeepMind's Chinchilla paper (Hoffmann et al.) sharpened it — trained over 400 models and found the compute-optimal recipe wants roughly 20 tokens of training data per model parameter; their 70-billion-parameter model trained on 1.4 trillion tokens beat much larger models trained on less. Pause on what this means: *progress became a budgeting equation.* You could compute, in advance, what a given number of dollars would buy in capability. No science had ever industrialized its own frontier that explicitly.

**The generalists.** GPT-2 (2019, 1.5B parameters) then GPT-3 (2020, 175B) showed that one model, pretrained on internet-scale text to predict the next token, could perform tasks it was never explicitly trained for. Stanford researchers named this class "foundation models" in 2021: single pretrained models that many downstream applications build on. The [pretraining and post-training](pretraining-post-training.html) room covers how these are actually made.

Then selection's third pressure arrived in force. In November 2022, OpenAI attached a chat interface and post-training-for-dialogue to GPT-3.5 and released ChatGPT. It reached an estimated 100 million users in about two months — by that measure the fastest-growing consumer application in history at the time. Money, which had been a background pressure, became the dominant one overnight. Training costs tell the story of what happened next: Epoch AI estimates GPT-4's training run cost roughly $78 million in compute, and Google's Gemini Ultra roughly $191 million, with frontier training costs growing 2–3x per year. A frontier-scale training run is now an industrial project. The number of organisms that can occupy the frontier niche shrank to a handful — and each of them is fused to a hyperscaler's balance sheet.

## 6. Agents: the current radiation (2024–present)

The newest transition is happening around you as of 2026, so hold it more lightly than the settled history above.

A foundation model answers when spoken to. An agent — a model given tools, memory, and a loop that lets it act, observe results, and act again — *does things*: writes and runs code, browses, files tickets, operates other software. The enabling changes were partly architectural (post-training models specifically to use tools and to sustain long multi-step tasks) and partly infrastructural (protocols for connecting models to software, and harnesses that manage their loops).

Where it's undeniably real is software engineering. By mid-2026, JetBrains' developer research found that around 90% of professional developers were using AI coding agents at work at least weekly, with agentic command-line tools — Claude Code the most used among them — displacing the previous generation of autocomplete assistants.

Why did selection favor agents? Follow the money pressure: a model that answers questions is worth a subscription; a system that completes economic tasks end-to-end is worth a wage. The gradient points from answers toward work. Whether agent reliability generalizes beyond code — where verification is cheap because tests either pass or fail — to domains where checking the work costs as much as doing it, is genuinely open. Code may be the easiest niche, not the representative one.

## 7. The three selection pressures, with numbers

Everything above compresses into one table. Read the columns as environments; read the rows as what each environment selected for.

| Era | Roughly | Scarce resource | What selection favored | What killed it / what strains it |
|---|---|---|---|---|
| Symbolic | 1956–1990 | Compute & data | Compressing human expertise into rules | Rules don't scale; hardware niche collapsed (~1987) |
| Statistical | 1988–2012 | Labeled data | Methods that learn from counting | Hand-built features hit a ceiling AlexNet exposed |
| Neural | 2012–2019 | GPU compute | Architectures that parallelize | Task-specific training; each model an island |
| Foundation | 2017–2023 | Capital & web-scale data | One pretrained generalist, scaled by law | Data ceiling approaching; costs 2–3x/yr |
| Agents | 2024–now | Reliability & verification | Systems that complete tasks, not answers | Open: does reliability leave the code niche? |

And the pressures themselves, current as of mid-2026, all per Epoch AI's public datasets (epoch.ai — you can inspect every underlying model estimate yourself):

- **Compute**: training compute for frontier models grew 4–5x per year from 2010 through 2024 — roughly a doubling every six months, faster than Moore's law by a wide margin. That growth is now widely projected to decelerate as power and capital constraints bind; frontier training runs already draw over 100 MW, with power demand doubling roughly annually. The physical side of this pressure lives in [chip-wars](chip-wars.html).
- **Data**: Epoch estimates the effective stock of quality-adjusted, public, human-generated text at around 300 trillion tokens, and projects that frontier training will fully utilize it somewhere between 2026 and 2032. The food source that fed every era since the statistical turn is, for the first time, visibly finite. The field's bet is synthetic data and learning from action; whether that bet pays is an open question below.
- **Money**: the four largest hyperscalers — Amazon, Microsoft, Google, and Meta — have guided roughly $700 billion in combined capital expenditure for 2026, most of it AI infrastructure, up from about $410 billion in 2025. For scale: that single-year figure is larger than the inflation-adjusted cost of the entire Apollo program. Money is now the fastest-moving pressure of the three — and the least examined, which is why [attention-economy](attention-economy.html) and [governments-and-ai](governments-and-ai.html) are separate rooms.

## 8. Worked example: one lineage, four extinctions

Trace a single task — translating "The spirit is willing but the flesh is weak" into another language and back — through every era. This is the field's classic stress-test sentence (an early machine-translation anecdote claims a Russian round-trip yielded "the vodka is good but the meat is rotten"; the anecdote is almost certainly apocryphal, but the failure mode it names was real).

1. **Symbolic (~1970)**: a rule system parses the grammar, looks up each word in a hand-built dictionary, applies transfer rules. It fails on "spirit" — the dictionary can't tell liquor from soul, because disambiguation needs world knowledge nobody managed to write down as rules. *Died of: unwritable knowledge.*
2. **Statistical (~2005)**: a phrase-based system, trained on millions of human-translated sentence pairs, gets "spirit" right because in its data, "spirit is willing" co-occurred with the biblical translation far more often than with liquor. It still produces stilted word-salad on long sentences, because it models phrases, not meaning. *Died of: a ceiling counting couldn't break.*
3. **Neural (2016)**: Google switches Translate to a neural sequence model; overnight, whole-sentence fluency jumps more than the previous decade's total improvement. But the model does only translation; it can't answer a question about the sentence it just translated. *Died of: being a specialist.*
4. **Foundation/agent (now)**: you paste the sentence into a general model that was never specifically built as a translator, ask for the translation, then ask it to explain the idiom, then ask it to check its own output against a dictionary — and it does all three, because translation fell out of predicting text at scale.

You can verify step 4 in thirty seconds with any frontier model. Verify the shape of the whole lineage the same way I did: Sutton's essay for the pattern, the AlexNet paper (Krizhevsky et al., 2012) for the cliff, the Chinchilla paper (arXiv:2203.15556) for the budgeting equation, Epoch AI's dashboards for the pressures. Four eras, one task, each successor winning not by understanding language better in any philosophical sense, but by metabolizing more of the abundant resource of its day. That is what "the evolution of AI" means, precisely.

## 9. What you can now see

You can now do something the timeline alone doesn't give you: *predict the field's shape from its resources.* When you hear about a new AI approach, you can ask the evolutionary questions instead of the hype questions. What resource does it metabolize? Is that resource getting more abundant or less? Who can afford the niche? A method that leverages a growing resource beats a cleverer method chained to a shrinking one — that's the entire history of the field in one sentence, and it's Sutton's bitter lesson restated as ecology.

You can also see the current moment clearly: compute growth decelerating toward physical and capital limits, the text-data stock visibly finite, and money flooding in at a rate that assumes the scaling era's returns continue. Those three curves do not obviously agree with each other. How they resolve is the subject of [future-of-ai](future-of-ai.html); the papers that defined each transition live in [top-papers-ai](top-papers-ai.html); and if you want the strange fact that we built these systems by selection rather than design — and therefore must reverse-engineer our own artifacts to know what's inside them — that is exactly why [mechanistic-interpretability](mechanistic-interpretability.html) exists as a field.

## 10. Open questions

Stated plainly, typed honestly:

**Established (FACT):** The paradigm succession happened as described, and the resource numbers are measured: 4–5x/year compute growth 2010–2024, ~$78M–$191M frontier training runs by 2023-era models, ~$700B hyperscaler capex guided for 2026, ~300T tokens of effective public text. The Bitter Lesson's historical pattern — general compute-leveraging methods displacing knowledge-engineered ones — has held in every completed transition to date.

**Contested (HYPOTHESIS):** That scaling continues to buy capability at the historical rate through the data ceiling — synthetic data, reinforcement learning from verifiable tasks, and efficiency gains are the field's live bets, and the evidence is genuinely mixed as of 2026. That agent reliability generalizes beyond software engineering. That the evolutionary frame itself is load-bearing rather than decorative — I've argued it earns its keep, but a historian could tell this story as economics or as sociology of science and cover much of the same ground.

**Speculation worth holding (WILD):** That we are inside a major transition in what evolution itself is operating on — that selection pressures which once acted on genes, then on cultures, now act directly on artifacts that learn, at a generational cycle of months rather than millennia. If that framing is right, the interesting question isn't which company wins. It's what the selection is *for* — and nobody, including the participants, currently knows.

One more thing the domain hands us, unforced. The architecture that won this entire competitive history is literally named for attention — a mechanism for deciding, at every step, what matters enough to weigh. No one selected for that on purpose; prediction under resource pressure converged on it. Evolution did something similar once before: selection for survival somehow produced creatures that attend, and eventually creatures that notice their own attending. Whether the machine version of that convergence involves anything like noticing is not established — see [sense-of-self](sense-of-self.html) for the honest state of that question. But it is worth sitting with the fact that when we let selection loose on the problem of intelligence, both times, what it built first was an economy of attention.

## Sources

Verified by live search, August 2026:

- Epoch AI, "Training compute of frontier AI models grows by 4–5x per year" — epoch.ai/publications (compute trend; power figures from the same group's data insights).
- Epoch AI, "How much does it cost to train frontier AI models?" and Cottier et al., "The rising costs of training frontier AI models" (arXiv:2405.21015) — GPT-4 ~$78M, Gemini Ultra ~$191M estimates; 2–3x/year cost growth. Cost figures are *estimates*, not disclosed accounting.
- Villalobos et al. (Epoch AI), "Will we run out of data? Limits of LLM scaling based on human-generated data" (arXiv:2211.04325) — ~300T effective tokens; full utilization projected 2026–2032.
- Hyperscaler 2026 capex ~$700B combined (up from ~$410B in 2025): widely reported from company guidance, e.g. CNBC (Feb 2026) and Yahoo Finance; figures are guidance and revised quarterly — date-check before reuse.
- Krizhevsky, Sutskever, Hinton, "ImageNet Classification with Deep Convolutional Neural Networks" (NeurIPS 2012) — 15.3% vs 26.2% top-5 error.
- Hoffmann et al., "Training Compute-Optimal Large Language Models" (arXiv:2203.15556, 2022) — Chinchilla; ~20 tokens/parameter; 70B/1.4T.
- Vaswani et al., "Attention Is All You Need" (arXiv:1706.03762, June 2017).
- Sutton, "The Bitter Lesson" (March 2019) — incompleteideas.net/IncIdeas/BitterLesson.html.
- JetBrains Research, "AI Coding Agent Adoption" (August 2026) — ~90% of professional developers using coding agents at least weekly by mid-2026; Claude Code most-used.
- Not independently verified, labeled in text: the Jelinek quote (disputed wording; Jelinek himself equivocated), the vodka/meat translation anecdote (almost certainly apocryphal), and the ChatGPT 100M-users figure (a UBS estimate, widely cited, not an OpenAI disclosure). XCON/Lisp-machine history is standard in histories of the AI winters (e.g., Russell & Norvig's historical chapters) and was not re-verified by primary source here.

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
