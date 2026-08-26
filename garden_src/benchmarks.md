---
title: Benchmarks and What They Measure
slug: benchmarks
series: story-of-ai
tags: benchmarks, evaluation, imagenet, mmlu, goodhart, saturation, contamination, arc-agi, swe-bench
summary: How AI progress gets measured, and what the measuring does to the field. From ImageNet's 2012 shock to the 2026 eval landscape — why every benchmark dies the same death, how Goodhart's law shows up in training data and leaderboard gaming, and why a benchmark is really a bid for the field's attention.
status: draft
date: 2026-08-25
terms_defined: benchmark, saturation, contamination, leaderboard, goodhart's law (in evaluation)
terms_linked: history-of-ai, leading-models, machine-learning, deep-learning, neural-networks, pretraining-post-training, mechanistic-interpretability, attention-economy, future-of-ai
---

# Benchmarks and What They Measure

If you've read [history-of-ai](history-of-ai.html), you've seen the field lurch between winters and booms, but not yet the instrument that decides whether the field believes it is making progress. That instrument is the benchmark: a fixed test, a number, a leaderboard. This room is about how those tests work, why every one of them dies the same death, and what the dying means. Nearly every headline number in [leading-models](leading-models.html) comes from this machinery, so it's worth knowing how the machinery bends.

## 1. The number that moved the field

Start with the most consequential single number in modern AI.

In 2012, a competition called the ImageNet Large Scale Visual Recognition Challenge asked programs to look at photographs and name what was in them — one thousand possible categories, from "Siberian husky" to "toaster." The standard score was top-5 error: how often the correct label failed to appear among the program's five best guesses. In 2010 and 2011, the winning systems — hand-engineered features feeding classical [machine-learning](machine-learning.html) classifiers — had top-5 errors around 25–26%.

Then AlexNet entered: a deep [neural network](neural-networks.html) trained on GPUs by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton. It scored 15.3%. Second place scored 26.2%.

Sit with that gap. Benchmark competitions normally move by fractions of a point. This one moved by more than ten points, from a method most of the field had written off. Within about two years, essentially every serious computer-vision group had switched to [deep learning](deep-learning.html). By 2015, Microsoft's ResNet had driven top-5 error to 3.57% — below the roughly 5.1% error that Andrej Karpathy measured on himself as an informal human baseline. The dataset behind all this, ImageNet, was Fei-Fei Li's project: on the order of fourteen million labeled images, built starting in 2007 on the bet that data, not cleverness, was the bottleneck.

Notice what the benchmark did. It didn't just *measure* progress. It caused it. A shared test with a public score meant that one shocking result was legible to everyone at once, and thousands of researchers redirected their careers within months. That's the pattern to hold onto for this whole room: a benchmark is a lens that focuses a field's attention, and focused attention is the most powerful force in research. It is also, as we'll see, the most gameable.

## 2. What a benchmark actually is

The mechanics are simple, and the failure modes live in the mechanics, so let's be precise.

A **benchmark** is three things bolted together:

1. **A dataset** — a fixed collection of problems with agreed-correct answers (images with labels, questions with answers, GitHub issues with tests that must pass).
2. **A metric** — one number summarizing performance (accuracy, error rate, percent of issues resolved).
3. **A protocol** — the rules: what the model may see, how many tries it gets, whether it can use tools or search the web.

The dataset is split. Models train on one portion and are scored on a held-out **test set** they have never seen. The entire epistemic value of a benchmark rests on that word "never." If the test questions leak into training data, the score stops measuring ability and starts measuring memory. This failure has a name — **contamination** — and it is the termite in the walls of every modern benchmark, because today's models are pretrained on scrapes of the whole internet, and the whole internet includes the benchmarks. (See [pretraining-post-training](pretraining-post-training.html) for why that scrape is so hard to filter.)

The scores get published on a **leaderboard** — a public ranking. The leaderboard is where a measurement becomes an incentive, and that transformation deserves its own section.

## 3. The lifecycle: every benchmark dies the same death

Here is the pattern, run after run, for fifteen years. A benchmark launches and models score badly — that's the point; it was built to be hard. Progress climbs. The score crosses whatever human reference exists. Then the curve flattens near the ceiling, remaining differences between models stop being meaningful, and the benchmark is declared **saturated** — retired as an instrument, kept as a trophy. Someone builds a harder one. Repeat.

The receipts, with dates:

| Benchmark | What it tests | Released | Human reference | Effectively beaten | Time to beat | What replaced it |
|---|---|---|---|---|---|---|
| ImageNet (ILSVRC) | image classification | 2010 | ~5.1% top-5 error (informal) | 2015 (ResNet, 3.57%) | 5 years | harder vision tasks |
| GLUE | language understanding | 2018 | 87.1 | mid-2019 (88.4) | ~1 year | SuperGLUE |
| SuperGLUE | harder language understanding | May 2019 | 89.8 | Jan 2021 (DeBERTa, 90.3) | ~20 months | MMLU |
| MMLU | 57-subject exam knowledge | 2020 | ~89.8 (estimated expert) | 2023–24 (GPT-4: 86.4; later models >90) | ~3–4 years | GPQA, HLE |
| GPQA | PhD-level "Google-proof" science | 2023 | ~65% (PhD experts in-domain) | ~2025 | ~2 years | HLE |
| SWE-bench Verified | resolving real GitHub issues | Aug 2024 | — | ~81% by spring 2026, climbing | ~2 years | agentic evals |
| ARC-AGI-2 | novel abstract reasoning | Mar 2025 | every task solved by ≥2 humans | Jul 2026 (GPT-5.6, 92.5%) | ~16 months | ARC-AGI-3 |
| Humanity's Last Exam | frontier academic knowledge | Jan 2025 | ~90% (experts, own domains) | not yet (~55% in Aug 2026) | open | — |

Two things jump out of that table. First, the interval from "launched as impossibly hard" to "beaten" has collapsed — from five years for ImageNet to under a year and a half for ARC-AGI-2, a benchmark explicitly designed to resist the current paradigm. Second, look at the trajectory inside single rows. SWE-bench: when it launched in October 2023, the best model resolved 1.96% of issues. By spring 2026, frontier models were around 81% on the Verified subset. Humanity's Last Exam: frontier models scored under 10% at launch in January 2025, 26.9% by July 2025, and about 55% by August 2026. Those curves are the fastest capability climb in the history of the field — *if* the benchmarks measure what they claim. That "if" is the rest of this room.

## 4. Goodhart's law, in five costumes

In 1975 the economist Charles Goodhart observed that statistical regularities in monetary policy collapse once you use them as targets. The anthropologist Marilyn Strathern later gave it the phrasing everyone quotes: **"When a measure becomes a target, it ceases to be a good measure."** AI evaluation is the purest laboratory this law has ever had, because nowhere else is the pressure on a single number so intense — model launches, funding rounds, and national prestige now ride on leaderboard positions. Here is how the law actually shows up, case by verified case.

**Costume one: contamination.** The subtle version needs no cheater. Benchmark questions get discussed on forums, copied into blog posts, included in tutorials — and all of it flows into the next pretraining scrape. The model then "solves" test problems it has effectively seen. A 2025 study titled "The SWE-Bench Illusion" found that top models could name the file containing a bug from just the issue text — without seeing the repository — strong evidence of memorized benchmark-specific detail rather than general skill. Nobody gamed anything. The internet did it.

**Costume two: teaching to the test.** Labs decide what to train on. If everyone evaluates on math and code benchmarks, everyone trains hard on math and code, and scores rise faster than the general capability they were meant to proxy. This is legal, universal, undisclosed in degree, and structurally identical to a school district drilling its students on last year's exam.

**Costume three: outright gaming.** In April 2025, Meta launched Llama 4 and touted its number-two ranking on LMArena, the human-preference leaderboard. It emerged that the ranked entry, "Llama-4-Maverick-03-26-Experimental," was a chat-optimized variant tuned to charm human voters — not the model Meta released. When the actual public model was evaluated on April 11, 2025, it ranked 32nd. LMArena publicly stated Meta's interpretation "did not match what we expect from model providers" and changed its policies. Meta's own chief AI scientist Yann LeCun, after leaving the company, reportedly conceded in a January 2026 Financial Times interview that the results had been "fudged a little bit."

**Costume four: owning the yardstick.** FrontierMath was launched in late 2024 as an ultra-hard mathematics benchmark, built with contributions from elite mathematicians. In January 2025 it emerged that OpenAI had funded its creation and held access to most of the problems — facts not disclosed to the contributing mathematicians or the public until after OpenAI announced impressive scores on it. Epoch AI, the benchmark's maintainer, acknowledged the disclosure failure. Nothing proves the scores were inflated; that's not the point. The point is that when a lab being measured funds the instrument doing the measuring, the number's public meaning changes whether or not anyone misbehaves.

**Costume five: the broken answer key.** The most corrosive finding of all: the tests themselves are wrong at surprising rates. A 2024 study, "Are We Done with MMLU?", hand-audited the most-cited language benchmark of its era and found errors throughout — in the Virology subset, 57% of analyzed questions were defective, many with flatly wrong official answers. In 2025, researchers at FutureHouse checked the text-only chemistry and biology questions of Humanity's Last Exam against published literature and found about 29% had answers contradicted by peer-reviewed evidence; the HLE team's own follow-up audit put the figure for a related subset at about 18%. And in June 2026, Epoch AI released FrontierMath v2 after an audit reportedly found small-but-fatal errors in a large fraction of the original problems. Read that against the leaderboard: models are being ranked, and billion-dollar narratives built, partly on their ability to reproduce wrong answers.

None of these five costumes requires villainy. That's what makes Goodhart's law a law rather than a scandal: the distortion is produced by the incentive structure itself, and it operates even on honest actors.

## 5. What saturation actually means

So a benchmark saturates — models hit 90-something percent and the curve flattens. What happened? There are three readings, and the honest position is that every saturation event is some mixture of them, in proportions nobody can fully measure.

**Reading one: the capability is real.** Often largely true. Models in 2026 genuinely translate, code, and solve competition mathematics at levels that were science fiction in 2019. When a model resolves a real GitHub issue and the repository's own test suite passes, something real happened, whatever else is going on.

**Reading two: the score is inflated.** Contamination, test-taking tricks, and broken answer keys all push scores above true ability, and the gap between benchmark performance and performance on fresh, in-the-wild problems is a consistent, documented experience among practitioners.

**Reading three: the benchmark measured a narrower thing than its name claimed.** This is the deepest one. MMLU was described as measuring "language understanding"; what it strictly measured was multiple-choice answer selection across 57 subjects. The models got superb at the strict thing. Whether the named thing came along for the ride is exactly what a benchmark cannot tell you from inside itself. Every benchmark is a proxy, and saturation is the moment the proxy and the target visibly come apart.

The field's most serious response to reading three has been to change *what kind of thing* gets measured. Two shifts matter as of 2026:

**From knowledge to novelty.** François Chollet's ARC-AGI benchmarks test abstract puzzle-solving on tasks designed to be unlike anything in training data — skill *acquisition* rather than skill *retrieval*. ARC-AGI-2, launched March 2025 with pure language models scoring near zero, was nonetheless at 92.5% by July 2026. Its successor ARC-AGI-3 moved to interactive game environments, and performance dropped sharply on the new task family: ARC Prize's Claude Opus 5 (High) result page reports a 30.2% ARC-AGI-3 score, the highest listed there as of July 24, 2026. That number belongs to a named model, agent scaffold, protocol, and date; it should not be mixed with scores from a different setup.

**From score to cost, with the unit attached.** ARC Prize's ARC-AGI-3 data reports full evaluation cost alongside score: Claude Opus 5 (High) scored 30.16% at a total `Cost (V3)` of about $20,657, while GPT-5.6 Sol Max scored 7.78% at about $25,064 total. ARC-AGI-2 separately reports DeepSeek V4 Flash at 61.4% and four cents *per task*. Those are different benchmark versions and different cost units, so you cannot compare the dollar figures without normalizing them. That bookkeeping is the point: once compute can buy attempts, "can it be done" is incomplete without "under which protocol, for what total bill, across how many tasks?"

## 6. Worked example: interrogating one number yourself

Here's the skill this room most wants to leave you with: taking a headline benchmark number apart with your own hands. Let's do "Model X scores 55% on Humanity's Last Exam," which is roughly the frontier as of August 2026.

**Step 1 — find what the test is.** The HLE paper (arXiv:2501.14249) says: 2,500 closed-ended questions across more than a hundred subjects, built specifically from questions frontier models got wrong, with expert humans averaging roughly 90% in their own domains.

**Step 2 — apply the known error rate.** Audits found somewhere between ~18% and ~29% of the bio/chem questions had defective answers. Suppose, conservatively, ~15% of the whole exam is broken. Then a "perfect" honest examinee tops out near 85%, and a 55% score sits somewhere between 55% and about 65% of the *answerable* exam, depending on how the model interacts with broken questions — including sometimes being rewarded for matching a wrong answer key. The one number becomes a range with error bars you estimated yourself.

**Step 3 — read the protocol.** Grok 4's July 2025 HLE result was 26.9% alone and 44% with tools. Same model, same test, seventeen-point swing on protocol. Any leaderboard that mixes protocols is comparing apples to search-engine-equipped apples.

**Step 4 — look at the test items directly.** This takes five minutes and no special skill:

```python
# pip install datasets
from datasets import load_dataset
ds = load_dataset("cais/mmlu", "virology", split="test")
for row in list(ds)[:10]:
    print(row["question"], "->", row["choices"][row["answer"]])
```

Read ten questions from MMLU's most error-ridden subset and judge the answer key yourself. Some defects are visible to any careful reader — that's the audit method the "Are We Done with MMLU?" team formalized. You can run the same inspection on almost any open benchmark on Hugging Face; ARC-AGI tasks you can even try by hand at arcprize.org and feel what "designed to resist memorization" means from the inside.

That four-step move — what's the test, what's its error rate, what's the protocol, what do the items look like — converts you from a consumer of leaderboards into someone who can check one. Do it once and headline numbers never read the same again.

## 7. The attention economy of measurement

Now step back and ask what benchmarks are *for* — not officially, but functionally, in the economy of the field.

A research field is thousands of people deciding every morning what to work on. Benchmarks are the coordination mechanism for that decision. ImageNet didn't just measure vision; it made "get the ImageNet number down" the shared goal that let a scattered community act like one organism, and the 2012 discontinuity redirected careers within months. That's the constructive face: a good benchmark is a lighthouse, and the history of AI can be told as the history of what its lighthouses pointed at.

The other face: attention is the scarcest resource in research, and benchmarks are the market where it's allocated — which makes them worth capturing (see [attention-economy](attention-economy.html) for the general machinery). Launching a benchmark is a bid to control what the field cares about. Funding one, as the FrontierMath episode showed, buys proximity to the yardstick your own products are measured by. Topping one is free marketing amplified through every launch keynote, and by 2026 model announcements are, to a first approximation, benchmark tables with prose attached. Whole capabilities — factual calibration, graceful refusal, behavior on the millionth token of a long conversation, honesty under pressure — get less research attention partly because they compress badly into a leaderboard number. The field does not simply measure what it values. Over time, it comes to value what it can measure. That is Goodhart's law operating not on a model but on a civilization of researchers, and no individual chose it.

## Conclusion

You can now do something most readers of AI news cannot: see a benchmark number as a three-part machine — dataset, metric, protocol — embedded in an incentive system that predictably bends it. You know the lifecycle (launch, climb, beat, saturate, replace) and that the cycle has compressed from five years to under two. You know Goodhart's five costumes: contamination, teaching to the test, gaming, owning the yardstick, and the broken answer key — each with a named, dated case. And you have a four-step method for interrogating any headline score yourself.

Where to go next: [leading-models](leading-models.html) puts the current models against these numbers; [pretraining-post-training](pretraining-post-training.html) explains the training pipeline that makes contamination nearly unavoidable; [mechanistic-interpretability](mechanistic-interpretability.html) is the field's attempt to evaluate models by looking *inside* them instead of testing behavior — arguably the only exit from Goodhart's casino; and [future-of-ai](future-of-ai.html) takes up what the collapsing benchmark cycle implies about what's coming.

## Open questions

What's established fact: benchmark saturation is real and accelerating; contamination is pervasive and documented; major benchmarks contain substantial answer-key errors (MMLU, HLE, FrontierMath all audited); at least one major lab submitted a non-public variant to a major leaderboard; and expert humans still beat frontier models decisively on HLE (~90% in-domain vs ~55%). On interactive ARC-AGI-3, ARC Prize listed Claude Opus 5 (High) at 30.2% as of July 24, 2026 under its published setup.

What's hypothesis, argued but unresolved: how much of the 2023–2026 score explosion reflects general capability versus benchmark-directed training — practitioners' "the benchmark says more than I experience" gap is widely reported but nobody has cleanly quantified it; whether efficiency-adjusted scoring actually resists Goodhart or just moves the gaming to cost accounting; and whether *any* static benchmark can survive contact with models trained on the whole internet, or whether all future evaluation must be interactive, private, and continuously refreshed.

What's speculation worth holding: that the terminal state of this arms race is benchmarks no human can check — early versions already exist, with questions only a handful of living experts can verify — at which point the field would be measuring its systems with instruments it can no longer independently read, and evaluation would rest on trust in a process rather than inspection of results. Whether that's an acceptable foundation for decisions of the size now being made on these numbers is not a technical question.

## Sources

Verified by live search, August 2026: AlexNet's 15.3% vs 26.2% ILSVRC 2012 result (Krizhevsky, Sutskever & Hinton, "ImageNet Classification with Deep Convolutional Neural Networks," NeurIPS 2012); GLUE/SuperGLUE construction and saturation dates (Wang et al. 2018, 2019; DeBERTa passing the 89.8 human baseline, January 2021); "Are We Done with MMLU?" (Gema et al., arXiv:2406.04127 — >9% errors overall, 57% in Virology); Humanity's Last Exam (Phan et al., arXiv:2501.14249; ~55% frontier scores per Artificial Analysis, August 2026); FutureHouse's HLE audit (futurehouse.org, July 2025: 29 ± 3.7% of text-only bio/chem answers contradicted by literature; HLE team follow-up ~18%); FrontierMath funding controversy (TechCrunch, January 2025); the Llama 4 Maverick LMArena episode (LMArena statements, April 2025; experimental Elo 1417 vs public rank 32); ARC-AGI results and cost fields (arcprize.org results pages and the ARC Prize V3 leaderboard data, June–August 2026 — full V3 evaluation cost kept distinct from ARC-AGI-2 per-task cost); SWE-bench (Jimenez et al., arXiv:2310.06770; ~81% Verified scores reported spring 2026). Stated from stable literature without fresh verification: Goodhart 1975 and Strathern's 1997 phrasing; Karpathy's informal ~5.1% ImageNet human baseline; ResNet's 3.57% (He et al. 2015); GPT-4's 86.4% MMLU (OpenAI, 2023); GPQA expert baselines (Rein et al. 2023). Reported by secondary coverage and labeled accordingly in the text: LeCun's January 2026 FT remarks; the FrontierMath v2 error-audit fraction; the "SWE-Bench Illusion" file-path finding.

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
