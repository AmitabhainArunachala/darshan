---
title: Forecasting the Future
slug: forecasting
series: time-future
tags: forecasting, prediction, tetlock, superforecasting, base rates, prediction markets, scenario planning, calibration
summary: What actually works when humans try to predict the future — Tetlock's twenty-year expert study, superforecasters, base rates, scenario planning, and prediction markets. Why famous experts fail, why weather forecasters succeed, and how to make a forecast yourself without being owned by it.
status: draft
date: 2026-08-25
terms_defined: forecasting, superforecasting, brier score, calibration, base rate, reference class forecasting, scenario planning, prediction market, fox and hedgehog
terms_linked: futurism, the-future, trends-gap, meaning-of-time, what-ai-can-bring, future-of-ai, benchmarks, attention-economy
---

# Forecasting the Future

You're in the time-future wing of the garden: [Futurism](futurism.html) is the neighboring room about people who paint pictures of the future, while this room is about people who bet on it and keep score. The difference matters more than almost anything else in this wing. A vision of the future can't be wrong in any way that costs the visionary; a forecast can. This room is about what happens when you force predictions to be checkable — and it turns out we've now run that experiment, at scale, for forty years.

## 1. The people who are actually good at this

Start with the one group of professionals who predict the future well: weather forecasters.

When a US weather forecaster says "70% chance of rain tomorrow," it rains on about 70% of those days. This isn't folklore — it was measured. Allan Murphy and Robert Winkler studied thousands of probability-of-precipitation forecasts in the 1970s and found that experienced forecasters were remarkably well calibrated: their stated probabilities matched the observed frequencies (Murphy & Winkler, "Reliability of subjective probability forecasts of precipitation and temperature," *Journal of the Royal Statistical Society Series C*, 1977).

Calibration — the property that your 70% claims come true about 70% of the time — is the core skill this whole room is about. And the weather case tells you exactly what produces it, because weather forecasters have three things almost no other predictor of the future has:

1. **They make many forecasts.** Hundreds a year, not one grand pronouncement a decade.
2. **They get fast, unambiguous feedback.** It rained or it didn't. No wiggle room.
3. **They are scored.** Since the 1950s, meteorology has used the Brier score. For the binary squared-error convention used in this room, the score is `(p - o)²`, where `p` is your probability and `o` is 1 if the event happened and 0 if it did not; it ranges from 0 (perfect) to 1 (perfectly wrong). The 0.081 and 0.101 scores later in this room use that normalized convention. Say 90% and it happens, you score well. Say 90% and it doesn't, you get punished hard.

Hold that trio in mind — volume, feedback, scoring — because every success story in this room has all three, and every famous failure is missing at least one.

## 2. The dart-throwing chimp: why experts fail

In 1984, a psychologist named Philip Tetlock started asking political and economic experts — 284 people who made their living commenting or advising on political and economic trends — to put probabilities on concrete future events. Would there be a nonviolent end to apartheid? Would Gorbachev be ousted in a coup? Would Quebec secede? He kept collecting until 2003. By the end the experts had made 82,361 forecasts, all scored against what actually happened (Tetlock, *Expert Political Judgment*, Princeton University Press, 2005; the tally is from Louis Menand's account of the study in *The New Yorker*, December 2005).

The headline finding is the one everyone quotes: the average expert did barely better than chance, and the press summary became "worse than a dart-throwing chimpanzee." But the quotable version hides the two findings that actually matter.

First: **the experts as a group failed to beat simple extrapolation.** Crude rules like "predict no change" or "predict the recent trend continues" matched or beat most of the humans. Expertise added confidence, not accuracy.

Second — and this is the finding that built everything since — **accuracy tracked how experts thought, not what they knew.** Tetlock borrowed a line from the Greek poet Archilochus, via Isaiah Berlin: the fox knows many things; the hedgehog knows one big thing. Hedgehogs reason from one grand theory — Marxism, libertarianism, a civilizational clash, whatever — and extend it everywhere with confidence. Foxes are skeptical of grand theories, draw on many small models, weigh conflicting evidence, and say "on the other hand" a lot. In Tetlock's data, foxes beat hedgehogs consistently, and the gap was widest exactly where you'd hope expertise would help most: long-range forecasts inside the hedgehog's own specialty. The one big idea is most dangerous on home turf, where the expert trusts it most.

There was a third finding, the darkest one: **fame predicted inaccuracy.** The more often an expert appeared in the media, the worse their forecasts. This isn't a paradox once you see the incentives. Television selects for the confident one-big-idea story, delivered without hedging. Calibration selects for "probably, 63%, and here's what would change my mind." The [attention economy](attention-economy.html) pays for hedgehogs. Reality pays foxes.

Notice what the experts were missing from the weather forecaster's trio: scoring. Nobody had ever gone back and checked. Pundits operate in a world with no Brier score, and Tetlock's real contribution was simply installing one.

## 3. Superforecasters: what works when you keep score

If keeping score exposes bad forecasting, can it train good forecasting? The US intelligence community paid to find out.

In 2011, IARPA — the intelligence community's research agency — launched a four-year forecasting tournament called ACE, posing about 500 geopolitical questions to competing research teams: Will Greece leave the eurozone this year? Will North Korea test a nuclear device before March? Tetlock, with decision scientists Barbara Mellers and Don Moore, entered a team called the Good Judgment Project: thousands of ordinary volunteers making probability forecasts online, scored by Brier score.

The Good Judgment Project won so decisively that IARPA dropped the other teams. Its forecasts beat all competing research programs by 35–72%, and the top 2% of its volunteers — the ones Tetlock dubbed superforecasters — reportedly outperformed professional intelligence analysts who had access to classified information, with a figure of "30% more accurate" widely circulated (Tetlock & Gardner, *Superforecasting*, 2015). One honest caveat on that famous number: later analysis showed the comparison is partly a comparison between the project's forecast-aggregation algorithm and the intelligence community's internal prediction market, so "superforecasters beat analysts by 30%" is a simplification of a messier result. The core finding — that a scored, open tournament of amateurs matched or beat the professional apparatus — survives the caveat.

The valuable part isn't that some people are mysteriously gifted. It's that the project ran randomized experiments on *what makes forecasting better*, and the answers are learnable:

- **Training works, and it's cheap.** A one-hour module on probabilistic reasoning — base rates, common biases, averaging multiple estimates — improved accuracy by roughly 10%, and the effect persisted for at least a year (Mellers et al., "Psychological strategies for winning a geopolitical forecasting tournament," *Psychological Science*, 2014).
- **Teams beat individuals.** Forecasters who shared information and argued their reasoning outperformed solo forecasters.
- **Updating beats brilliance.** Frequency of belief revision — many small updates as news arrived — was one of the strongest predictors of accuracy. Superforecasters treat a forecast as a living number, not a pronouncement.
- **Granularity is real.** Superforecasters use the difference between 63% and 67%, and it shows up in their scores. Rounding everyone to "likely / unlikely" measurably destroys accuracy.
- **Start outside.** The single most transferable habit: before thinking about the case in front of you, ask how often things like this happen in general. Which brings us to the strongest tool in the kit.

## 4. Base rates: the outside view

A base rate — the fancier term is a plain idea — is the frequency of an outcome across all cases similar to yours, before you know anything special about your case. What fraction of tech startups reach a profitable exit? How often do ceasefires of this type hold a year? How often do infrastructure projects finish on budget?

Daniel Kahneman and Amos Tversky drew the key distinction in 1979: the *inside view* builds a forecast from the details of your specific case — your plan, your team, your scenario of how it goes. The *outside view* ignores the details and starts from the statistics of the reference class. The inside view feels more informed and is systematically worse, because the details you know are mostly the plan, and plans don't contain their own failure modes.

The most consequential industrial application is **reference class forecasting**, developed for practice by the economic geographer Bent Flyvbjerg. His datasets of hundreds of megaprojects show cost overruns are not occasional accidents but the statistical norm — driven by optimism bias and by what he bluntly calls strategic misrepresentation: the people writing the estimate need the project approved. The fix is mechanical. Three steps:

1. Identify a reference class of similar completed projects.
2. Build the actual distribution of their outcomes (cost overrun percentages, schedule slips).
3. Place your project in that distribution and adjust — "uplift" — your inside-view estimate accordingly.

This is not a seminar exercise. The UK Treasury and Department for Transport made reference-class uplifts official guidance in 2003–2004 (Flyvbjerg & COWI, *Procedures for Dealing with Optimism Bias in Transport Planning*, UK DfT, June 2004). A rail project's bottom-up budget gets mechanically inflated by the historical overrun distribution of rail projects — in the published guidance, a standard-risk rail scheme wanting 80% confidence of staying in budget takes an uplift on the order of 40–60% over its inside-view estimate. The planners' own numbers are treated as one input, presumed optimistic, and corrected by history.

That's the outside view as institutional policy: your beautiful specific story about why *this one is different* gets overruled by the boring record of everything like it. It is insulting and it works. It is also, incidentally, the correct prior for most claims in [the-future](the-future.html) rooms of this garden: when someone says this time is different, the base rate of "this time was actually different" is the first number to look up — and the [trends-gap](trends-gap.html) room is about the cases where it genuinely was.

## 5. Scenario planning: when probabilities aren't the point

Everything so far assumes the question is well-posed: a clear event, a deadline, a yes or no. Much of the future isn't shaped like that. For structural uncertainty — what will the energy system, or the world order, look like in fifteen years? — there's a different tool with a different success story.

In the early 1970s, a planner at Royal Dutch Shell named Pierre Wack got tired of single-point forecasts that extrapolated the recent past — cheap oil forever, demand rising smoothly. His team instead wrote a small set of internally consistent stories about how the world might unfold. One family of scenarios worked through what would happen if oil-producing countries, for their own visible reasons, restricted supply and forced prices up. When the 1973 OPEC embargo hit and oil prices quadrupled, Shell's managers had already rehearsed that world. Shell navigated the shock better than its competitors and rose from among the weakest of the major oil companies toward the top of the industry over the decade. Wack wrote the method up in two Harvard Business Review articles in 1985, "Scenarios: Uncharted Waters Ahead" and "Scenarios: Shooting the Rapids."

Wack was insistent about what scenarios are *not*: predictions. He didn't claim the embargo was likely. The purpose of a scenario, in his words, is to change the decision-maker's mental model — to "gather and transform information of strategic significance into fresh perceptions." A scenario is a rehearsal. You don't score it with a Brier score; you score it by whether, when the surprise arrives, anyone in the room has already lived there for an afternoon.

This is the honest division of labor. Forecasting compresses uncertainty into a number so you can act on it. Scenario planning refuses the compression, on the grounds that for some futures the number would be fake precision and the real risk is a failure of imagination. The failure mode of forecasting is overconfidence in the number. The failure mode of scenario planning is that, unscored, it can drift into [futurism](futurism.html) — storytelling with no cost for being wrong.

## 6. Prediction markets: paying for accuracy

The fourth tool replaces the scored individual with a scored crowd. A prediction market lets people buy and sell contracts that pay out if an event happens; the price becomes a live probability estimate. If "candidate X wins" trades at 34 cents on a dollar contract, the market is saying 34%. If you think it's really 50%, you can buy — and if you're right on average, you take money from the people who were wrong. The incentive structure of punditry, inverted: confidence costs money unless it's calibrated.

The theory is old; the scale is new. As of early 2026 this is no longer a fringe experiment: Kalshi, a US exchange regulated by the CFTC (the federal commodity-markets regulator), traded roughly $39.7 billion in event contracts over the prior year, and Polymarket, the crypto-based platform, about $36.2 billion (figures from a Congressional Research Service brief, February 2026). The 2024 US election was the coming-out moment — the markets moved ahead of polls and pundits on the outcome, and were widely credited afterward as the better real-time signal.

Three honest limits, because the room's job is not to sell you a tool:

- **They're becoming casinos.** About 87% of Kalshi's volume in that CRS snapshot was sports betting, not geopolitics. The accuracy mechanism doesn't care what the question is, but the civic promise — markets as public forecasting infrastructure — is currently a minority use case riding on a gambling business, and US federal and state regulators are actively fighting in court over who governs it.
- **They need liquidity and resolvability.** Thin markets give noisy prices, and the question must resolve cleanly — which pushes markets toward the same well-posed short-horizon questions tournaments prefer. "Will AI go well for humanity" cannot be a contract.
- **They can be beaten by method.** In the IARPA tournament, the Good Judgment Project's weighted, "extremized" aggregation of its best forecasters outperformed prediction markets running on the same questions. Markets are a strong baseline, not an oracle.

## 7. The four tools side by side

| | Superforecasting | Base rates / reference class | Scenario planning | Prediction markets |
|---|---|---|---|---|
| **Core move** | Scored probabilities, updated often | Start from the statistics of similar cases | Rehearse several structured futures | Price discovery on event contracts |
| **Best horizon** | Months to a few years | Any, if the reference class exists | Years to decades | Days to ~2 years |
| **Question shape** | Well-posed, resolvable | Repeated-event classes | Structural, open-ended | Well-posed, liquid, resolvable |
| **Output** | A calibrated number | A corrected estimate | Changed mental models | A live price |
| **Scored?** | Yes (Brier) | Yes (against outcomes) | No — that's the trade-off | Yes (money) |
| **Failure mode** | Breaks on unprecedented events | Wrong reference class in, garbage out | Unscored drift into storytelling | Thin markets, gambling capture |
| **Canonical receipt** | IARPA ACE tournament, 2011–15 | UK Treasury uplifts, 2004– | Shell and the 1973 oil shock | 2024 US election |

The tools compose. A superforecaster uses base rates as the opening move. A good scenario team checks each scenario's load-bearing assumptions against reference classes. A market price is a fine base rate to start from before you adjust on private information.

## 8. Worked example: make one forecast

Here's the superforecaster procedure on a live question, done in the open so you can check the reasoning and then run your own. Question: **"Will any AI lab release a model that outranks human superforecasters on ForecastBench's market questions by December 31, 2027?"** (ForecastBench is a benchmark that poses the same resolvable real-world questions to language models and to scored human forecasters — more on it in the next section.)

**Step 1 — Fermi-ize.** Break the question into parts: (a) does the capability trend continue? (b) does the specific leaderboard measure and publish it? (c) does "outranks" resolve cleanly (statistically, not just point estimate)?

**Step 2 — Outside view first.** Reference class: recent AI-vs-human benchmark gaps. The pattern across [benchmarks](benchmarks.html) generally is that once models are within ~20% of human expert performance, parity tends to arrive within one to three years. In October 2025, superforecasters led the best model 0.081 to 0.101 in difficulty-adjusted Brier score — about a 20% edge. Base-rate opening: maybe 70% by end of 2027.

**Step 3 — Inside view adjustments.** Now the case specifics. By July 2026 the benchmark's own operators reported that several AI systems were already statistically indistinguishable from superforecaster accuracy, and one system outranked them on market questions on the tournament leaderboard. So the event has arguably part-happened; what remains is durability and clean resolution. Adjust up substantially: ~90%.

**Step 4 — Consider the ways you're wrong.** Leaderboards get revised; "indistinguishable" is not "outranks"; the benchmark could change methodology; my sources are the benchmark operators, who have an interest in the result being interesting. Shave to ~85%.

**Step 5 — Commit to a number and a revisit date.** 85%, revisit when the next quarterly leaderboard publishes. Write it down. The writing down is not decoration — it's the difference between a forecast and a vibe, because a vibe retroactively agrees with whatever happened.

That's the whole method: decompose, start outside, adjust inside, argue against yourself, commit, update. One hour of this kind of training measurably improved accuracy for a year. You can verify the inputs yourself: the ForecastBench paper and leaderboards are public (Karger et al., ICLR 2025; forecastingresearch.org).

## 9. Where forecasting breaks

Now the honest edge of the field, because this room would be dishonest if it ended on technique.

**The trio disappears for the questions we care about most.** Volume, feedback, scoring — the preconditions from Section 1 — exist for elections, commodity prices, and ceasefires. They do not exist for one-shot civilizational questions. You cannot be calibrated on human extinction; nobody has a track record on events that occur zero or one times.

The cleanest demonstration is the Existential Risk Persuasion Tournament, run by the Forecasting Research Institute in 2022. It put superforecasters and domain experts together for months, incentivized to persuade each other, on long-horizon catastrophe questions. Two results matter. First, the groups disagreed enormously and persuasion barely moved anyone: median superforecaster, 0.38% chance of AI-caused human extinction by 2100; median AI domain expert, around 3–4%. A tenfold gap that argument could not close — on the exact class of question where we most want forecasting to help. Second, and worse for the superforecasters: when the tournament's *near-term* AI questions resolved, both groups had underestimated AI progress, and the superforecasters underestimated it more. On one standard math benchmark, domain experts had given 21% probability to the level actually reached by end of 2024; superforecasters gave 9%. The calibration champions were the most wrong, in the direction of expecting the future to look like the past — which is precisely the bias their methods are built on. Base rates are a bet that the future resembles the historical distribution. When it doesn't — the genuinely novel, the [trends-gap](trends-gap.html) discontinuity — the outside view becomes the error.

**And the forecasters are now being forecast.** As of mid-2026, AI systems have likely reached parity with human superforecasters on the public benchmark built to compare them (Forecasting Research Institute, July 2026). Whether that holds on truly novel questions is open — but the era in which "calibrated probability estimation on well-posed questions" is a distinctly human skill appears to be ending, roughly a decade after it was shown to be a skill at all. What that does to institutions that run on human judgment is a question for the [future-of-ai](future-of-ai.html) and [what-ai-can-bring](what-ai-can-bring.html) rooms.

## 10. Holding a forecast without being held by it

Tetlock's deepest finding was never really about prediction. Foxes and hedgehogs make forecasts with the same words and numbers. The difference is the grip. The hedgehog's forecast is downstream of an identity — the one big idea — so evidence against the forecast arrives as an attack on the self, and gets absorbed, explained, deflected. The famous pundit literally cannot afford to update; the update would cost the persona. That's what "captured by a prediction" means, and Tetlock measured its price in Brier points for twenty years.

The alternative discipline is everything this room has walked through: write the number down so it can be wrong. Start from the record of things like this, not your story about this one. Revisit on a schedule. Treat the forecast as an instrument reading, not a flag you fly. Wack said scenarios exist to change perception, not to be right — and even the hard-scoring tournament tradition agrees in its own way: the update, not the forecast, is where the skill lives.

Which points at what a forecast actually is. It is not a fact about the future — the future contains no facts yet. It is a precise, dated, falsifiable description of your current state of knowledge, and attention is the whole game: the hedgehog attends to the theory and calls it the world; the fox attends to the world and lets the theory take the damage. Every technique in this room — the outside view, the scoring rule, the rehearsed scenario, the market that charges you for confidence — is a mechanism for forcing a mind to notice the difference between what it expects and what is there. Kept honestly, a forecasting record becomes something almost no other practice provides: a written history of the gap between the world and your model of it, in your own numbers. What you do with that record — whether being wrong in writing changes the one who wrote it — is the question this room hands to the rest of the garden, and it's the same question [meaning-of-time](meaning-of-time.html) asks from the other side: the future you're forecasting is, always, the one your present attention can reach.

## Open questions

**Established (FACT):** Expert political forecasting without scoring barely beats chance and loses to simple extrapolation (Tetlock 2005). Calibration is a trainable skill; brief training, teamwork, and frequent updating measurably improve accuracy (GJP randomized experiments, 2011–15). Reference-class uplifts are official UK government forecasting policy. Weather forecasters are well calibrated (Murphy & Winkler 1977). Prediction markets at multi-billion-dollar scale existed by 2026, in active regulatory contest.

**Contested (HYPOTHESIS):** That superforecaster skill transfers to long-horizon and unprecedented questions — the XPT's near-term resolutions cut against it. That prediction-market prices beat all rival aggregations — GJP's algorithm beat markets in ACE; markets beat polls in 2024; the general ranking is unsettled. That AI parity on ForecastBench implies parity on genuinely novel questions — the benchmark's operators themselves flag this as open. The exact size of the famous "30% better than intelligence analysts" result.

**Speculation worth holding (WILD):** That cheap, superhuman-calibrated AI forecasting becomes ambient infrastructure — every policy, budget, and headline auto-annotated with a live probability — and the bottleneck moves entirely from generating forecasts to the older problem this room can't solve: whether anyone updates. And the mirror speculation: that ubiquitous forecasting itself changes the future being forecast, as markets and models become the signals people act on, folding prediction into causation.

## Sources

- Tetlock, P. E., *Expert Political Judgment: How Good Is It? How Can We Know?*, Princeton University Press, 2005. Study scope (284 experts, 82,361 forecasts, fox/hedgehog result, fame–accuracy inverse) per the book and Louis Menand, ["Everybody's an Expert,"](https://www.newyorker.com/magazine/2005/12/05/everybodys-an-expert) *The New Yorker*, Dec 5, 2005. Verified live.
- Tetlock, P. E. & Gardner, D., *Superforecasting: The Art and Science of Prediction*, 2015. IARPA ACE results (35–72% margin over rival teams; "30%" claim and its aggregation-method caveat) verified via [Good Judgment](https://goodjudgment.com/resources/the-superforecasters-track-record), [Wikipedia's GJP article](https://en.wikipedia.org/wiki/The_Good_Judgment_Project), and the [EA Forum analysis of Goldstein et al.](https://forum.effectivealtruism.org/posts/qZqvBLvR5hX9sEkjR/comparing-top-forecasters-and-domain-experts)
- Mellers, B., et al., "Psychological strategies for winning a geopolitical forecasting tournament," *Psychological Science*, 2014 — training/teams/tracking effects; summarized with data at [AI Impacts](https://aiimpacts.org/evidence-on-good-forecasting-practices-from-the-good-judgment-project). The ~10% training effect verified there; Good Judgment's own materials cite "as much as 11%."
- Murphy, A. H. & Winkler, R. L., "Reliability of subjective probability forecasts of precipitation and temperature," *JRSS Series C*, 26, 41–47, 1977. Citation verified live.
- Kahneman, D. & Tversky, A., "Intuitive prediction: Biases and corrective procedures," 1979 (outside view); Flyvbjerg, B. & COWI, UK Department for Transport optimism-bias guidance, June 2004; uplift figures per [Flyvbjerg, Hon & Fok 2016](https://arxiv.org/pdf/1710.09419) and the [Wikipedia RCF article](https://en.wikipedia.org/wiki/Reference_class_forecasting). Verified live.
- Wack, P., "Scenarios: Uncharted Waters Ahead" and "Scenarios: Shooting the Rapids," *Harvard Business Review*, 1985; Shell 1973 history per [Polytechnique Insights case study](https://www.polytechnique-insights.com/en/columns/society/case-study-how-shell-anticipated-the-1973-oil-crisis) and [Pierre Wack, Wikipedia](https://en.wikipedia.org/wiki/Pierre_Wack). Verified live. Shell's exact rank change over the 1970s varies by telling; I've kept it qualitative.
- Prediction market volumes and regulation: [Congressional Research Service, "Prediction Markets: Policy Issues for Congress"](https://www.congress.gov/crs-product/IF13187) (Kalshi ~$39.7B/87% sports; Polymarket ~$36.2B/38% sports, as of Feb 2026); litigation status per [Wikipedia, "Prediction market"](https://en.wikipedia.org/wiki/Prediction_market) (as of June 2026). Verified live.
- Existential Risk Persuasion Tournament: [Karger et al., "Forecasting Existential Risks," FRI 2023](https://static1.squarespace.com/static/635693acf15a3e2a14a56a4a/t/64f0a7838ccbf43b6b5ee40c/1693493128111/XPT.pdf) (0.38% vs 3.9% medians); near-term accuracy check per [FRI, "Assessing Near-Term Accuracy in the XPT"](https://forecastingresearch.org/research/near-term-xpt-accuracy). Verified live.
- AI vs human forecasters: [Karger et al., "ForecastBench," ICLR 2025](https://arxiv.org/html/2409.19839v5); October 2025 standings per [Good Judgment](https://goodjudgment.com/human-vs-ai-forecasts); parity claim per [FRI Substack, "AI models have likely reached parity with superforecasters on ForecastBench," July 2026](https://forecastingresearch.substack.com/p/ai-models-have-likely-reached-parity). Verified live.
- Unverified-by-search in this article: none knowingly; the Brier score's origin in 1950s meteorology (Brier 1950) is standard history stated from general knowledge.

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
