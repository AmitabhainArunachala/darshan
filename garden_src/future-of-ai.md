---
title: The Future of AI
slug: future-of-ai
series: story-of-ai
tags: forecasting, scaling, agents, robotics, compute, scenarios
summary: What the 2026 evidence actually supports about where AI is going. Three scenarios with their assumptions named, a doubling-time extrapolation you can check yourself, and a clear line between what is measured, what is argued, and what is guessed.
status: draft
date: 2026-08-25
terms_defined: time horizon, inference-time scaling, scenario discipline
terms_linked: history-of-ai, evolution-of-ai, leading-models, benchmarks, forecasting, trends-gap, the-future, what-ai-can-bring, chip-wars, semiconductors, nvidia-and-the-chip, governments-and-ai, china-usa-race, mechanistic-interpretability, pretraining-post-training, attention-economy
---

# The Future of AI

If you've read [the history of AI](history-of-ai.html) and [its evolution](evolution-of-ai.html), you've watched this field lurch between winters and manias for seventy years, and you know its predictions have a terrible record in both directions. This room is not another prediction. It is an attempt at something harder: laying out what the 2026 evidence actually supports, stating the live scenarios with their assumptions named, and teaching you to run the extrapolations yourself so you don't have to take my word — or anyone's.

## 1. The ground rules: why this room refuses prophecy

Start with the track record. In 1965 Herbert Simon predicted machines would do any human work within twenty years. In 1969 Marvin Minsky reportedly gave "three to eight years" for human-level AI. Both were among the smartest people in the field, both had inside information, and both were wrong by at least half a century. Meanwhile the people who confidently said neural networks were a dead end — a mainstream position for two long stretches — were wrong in the other direction, and the field's biggest results came from the approach they had written off. You can read that whole story in [the history room](history-of-ai.html).

So the ground rule for this room: no dates asserted as fact. Instead, three disciplines.

First, **dated evidence**. Every empirical claim here is current as of August 2026 and says so. In a field where the frontier moves in months, an undated claim is already a lie of omission.

Second, **named assumptions**. A scenario is not a prediction. A scenario is a chain of assumptions plus what follows if they hold. Stated that way, you can watch the assumptions and update yourself when one breaks — which is how [forecasting](forecasting.html) is supposed to work.

Third, **typed claims**. Measured things get stated as measured. Contested things get stated as contested. Speculation gets marked as speculation and kept anyway, because some speculation is worth holding. The failure mode of most writing about AI's future is that all three wear the same grammar.

## 2. Signal one: the scaling debate has actually shifted

For a decade the field's core bet was simple: make the [pretraining](pretraining-post-training.html) run bigger — more data, more parameters, more compute — and capability rises on a smooth curve. That bet paid off from 2018 to roughly 2024, and it built the world described in [the chip rooms](nvidia-and-the-chip.html).

Here is what changed. At NeurIPS in December 2024, Ilya Sutskever — co-author of the papers that started the scaling era — said publicly that "pretraining as we know it will end," on the blunt ground that the internet is finite: compute grows, but the stock of human text does not. Treat that as one prominent researcher's judgment, not as a measurement of unpublished runs; labs do not release enough failed-run data for outsiders to establish that the curve has bent.

What replaced the bet is not "no scaling" but a different axis: **inference-time scaling** — spending more compute when the model answers, not just when it trains. Reasoning models (OpenAI's o-series, DeepSeek-R1, and their successors) generate long internal chains of work before responding, and on hard math and code the difference is dramatic. The field renamed its slope rather than admitting the old one flattened.

The honest question is how far the new axis runs. Epoch AI's analysis (Josh You, 2025) gives the cleanest public numbers: the reinforcement-learning stage that trains reasoning behavior was still small compared to pretraining — DeepSeek-R1's reasoning training was around 6×10²³ floating-point operations (FLOPs, a count of arithmetic work), roughly a fifth of its pretraining cost, and some published models spent under 1% of pretraining cost on it. That gap is why reasoning capability jumped so fast (o1 to o3 was roughly 10× reasoning compute in four months): you can grow a small thing quickly. Epoch's projection is that within about a year of that analysis, reasoning compute catches up to the training frontier, and from then on it can only grow as fast as total compute grows — roughly 4× per year. The overhang gets spent once.

So the 2026 state of the scaling debate, stated fairly: pretraining returns have visibly bent (contested but broadly reported); inference-time scaling opened a genuinely new curve (measured); and the new curve has a known rendezvous with the old constraint — total compute and money (argued, with explicit numbers, by Epoch). Neither "scaling is over" nor "straight line to superintelligence" survives contact with those three facts at once.

## 3. Signal two: the time-horizon measurements

If you want one number to watch instead of vibes, watch METR's **time horizon**: the length of task (measured in how long it takes a skilled human) that a model can complete autonomously at 50% reliability. It is the closest thing the field has to an honest speedometer for agency, and it belongs beside the other instruments in [the benchmarks room](benchmarks.html).

The January 2026 update (Time Horizon 1.1) measured Claude Opus 4.5 at about 320 minutes — five and a third hours of human-equivalent work — with GPT-5 around 214 minutes. The growth rate is the striking part. Over the whole 2019–2025 record, the horizon doubled about every 196 days. Measured from 2023 onward, about every 131 days. From 2024 onward, about every 89 days. The curve is not just exponential; on the recent data it is a *quickening* exponential.

Now the caveats, because METR states them and almost nobody repeats them. The trend is sensitive to which tasks are in the suite. Only 5 of the 31 longest tasks have actual measured human baselines — the rest are estimates. Confidence intervals on the frontier models span roughly 2× in each direction (Opus 4.5's interval is 170 to 729 minutes). And these are software and research tasks in clean evaluation environments, not messy organizational reality. The number is real and the uncertainty is also real. Section 6 shows you how to use it anyway.

## 4. Signal three: agents in the wild, and the production gap

2026 was sold as "the year of agents" — AI systems that don't just answer but act: browse, code, file, book, negotiate. McKinsey's 2025 global survey gives one internally consistent ladder: 88% of respondents said their organizations used some AI in at least one business function, 23% said their organizations were scaling an agentic system somewhere, and no individual business function exceeded 10% for scaled agent use. Those are three different scopes inside one survey, not one measure of autonomous multi-agent deployment. Gartner separately predicts that over 40% of agentic AI projects will be canceled by the end of 2027; that is a forecast, not an observed failure rate.

That gap between capability and deployment is one of the most load-bearing facts in this room, and it cuts both ways. It deflates the hype: five-hour time horizons in an eval harness do not mean five-hour autonomy in your accounting department. But it also means there is enormous *stored* capability — if the organizational plumbing catches up, deployed impact can jump without any new model release. The pattern in what actually works is consistent: narrow, well-governed domains — IT operations, support workflows, reconciliation, code — one scoped problem shipped, then expanded. The [trends-gap room](trends-gap.html) is about exactly this lag between what exists and what has landed.

The same structure holds for embodiment. BMW's own February 2026 record says one Figure 02 robot worked a ten-month Spartanburg pilot, helped produce more than 30,000 X3 vehicles, moved more than 90,000 components, and logged about 1,250 operating hours. Agility Robotics and GXO publicly announced a multi-year commercial Digit deployment in a live warehouse, without publishing a fleet count in that announcement. These are primary company and plant records, not independent audits, and they support a narrower claim than the industry trackers: real industrial work exists, while the public evidence still does not establish mass humanoid deployment. Read every larger fleet claim with its source attached.

## 5. Three scenarios, assumptions named

Here are the live scenarios as of 2026. None is a prediction. Each is a chain: *if these assumptions hold, this follows.* The table gives you the skeleton; the point is the third and fourth columns — what would confirm each scenario and what would kill it. Watch those, not the headlines.

| Scenario | Core assumptions | What confirms it | What kills it |
|---|---|---|---|
| **Fast takeoff** (transformative AI ~2027–2030) | METR's post-2024 doubling (~89 days) continues or accelerates; AI meaningfully speeds up AI research itself; deployment friction gets bulldozed by capability | Time horizons reaching weeks-to-months by 2027–28; labs demonstrably automating their own R&D; agent production share jumping, not creeping | Doubling time stretching back past ~200 days; reasoning-compute convergence with no new scaling axis found; eval gains that keep failing to transfer to messy work |
| **Steady compounding** (huge but gradual, over 10–20 years) | Capability keeps growing near the *long-run* trend (~6-month doublings); the enterprise production gap closes at organizational speed; compute buildout is financed by real revenue | McKinsey's 23% agent-scaling share grinding toward a majority over years; measurable sector-level productivity gains; capex roughly tracking revenue | Either a genuine capability plateau or a sudden discontinuity; a financing collapse that stalls the compute buildout |
| **Plateau and diffusion** (current-level AI diffuses; frontier stalls) | Inference-time scaling exhausts its overhang (per Epoch's convergence argument) with no third axis; remaining gains come from cost collapse and integration, not capability | Frontier models bunching together on hard [benchmarks](benchmarks.html); cost-per-task falling faster than peak capability rises; time-horizon curve visibly bending down | Any sustained post-convergence continuation of the fast doubling trend |

Two things to notice. First, the scenarios disagree mostly about *one* empirical quantity — whether the time-horizon doubling holds after reasoning compute converges with the training frontier, roughly 2026–2027. That makes the next eighteen months unusually informative. Second, the fast-takeoff scenario's middle assumption — AI accelerating AI research — is the one the public evidence says least about either way. It is the hinge, and it is mostly unobservable from outside the labs. Forecast writers who assert it are guessing; so are those who dismiss it.

## 6. Worked example: run the extrapolation yourself

Here is the exercise this whole room exists to teach. Take METR's numbers and extrapolate — then watch how hard the answer swings on one parameter choice. You can do this with a pencil.

Start: frontier time horizon ≈ 320 minutes (Claude Opus 4.5, January 2026 measurement). Target: a "month" of human work — call it 160 working hours, or 9,600 minutes. How many doublings from here?

```
9,600 / 320 = 30  →  log2(30) ≈ 4.9 doublings
```

Call it 5 doublings. Now apply each measured doubling time:

```
Post-2024 rate   (89 days):  5 × 89  ≈ 445 days  → mid-2027
Post-2023 rate  (131 days):  5 × 131 ≈ 655 days  → late 2027
All-time rate (196.5 days):  5 × 196 ≈ 983 days  → late 2028
```

Same data, same arithmetic, and the answer for "agents that can do a month of work" ranges from mid-2027 to late 2028 depending only on which window you fit the trend to. Now add the measurement uncertainty: if the true current horizon is 170 minutes (the bottom of METR's confidence interval), you need one extra doubling — push every date out by 3 to 6 months. If it's 729 minutes (the top), pull them in by the same. And all of this assumes the 50%-reliability horizon is the right threshold; at 80% reliability, horizons run several times shorter, and a month-of-work agent that fails half the time is not a colleague.

This is the discipline: the extrapolation is genuinely informative — it tells you the *shape* of the near future under trend-continuation, and it rules out both "nothing is happening" and "it's all decades away if trends hold." But it cannot tell you which doubling time is real, whether the trend survives the reasoning-compute convergence, or whether eval-horizon translates into deployed autonomy. Anyone who hands you a single date without this spread is selling something. Check my arithmetic; that's what it's for.

## 7. The money question: capex as revealed belief

Words are cheap; capital expenditure is not. Summing early-2026 company guidance for Amazon, Alphabet, Microsoft, and Meta gives roughly $725 billion of planned capital expenditure; J.P. Morgan's mid-2026 analysis separately estimates $697 billion across five hyperscalers. The scopes, methods, and guidance dates differ, so these are competing estimates of the same order of magnitude, not figures to combine. The Stargate venture (OpenAI, SoftBank, Oracle, MGX) targets $500 billion over four years, with its first campus at Abilene, Texas planned around a gigawatt. Power is becoming the binding constraint: U.S. data-center electricity demand projections run to multiples of 2024 levels within a decade. The industrial context lives in [the semiconductor room](semiconductors.html) and [the chip-wars room](chip-wars.html); the state side lives in [governments-and-ai](governments-and-ai.html) and [the China–US race](china-usa-race.html).

Read this as revealed belief: the people with the most inside information about frontier capability are betting sums comparable to the Apollo program *annually* that the curves continue. That is a genuine signal — but note precisely what it signals. It shows the labs and hyperscalers *believe*; it does not show they are *right*. Railway investors in the 1860s and telecom investors in 1999 also bet fortunes on real technologies — the technologies were real, the transformations happened, and the specific bets still went to zero because revenue arrived slower than debt. Whether frontier-AI revenue covers this buildout is, as of August 2026, an open empirical question. If it does not, the plateau-and-diffusion scenario arrives not through any limit of the science but through the oldest force in [the attention economy](attention-economy.html): money running out of patience. A financing winter would slow the frontier without stopping the diffusion of what already exists — which is arguably what happened in every previous AI winter, as [the history room](history-of-ai.html) shows.

One more 2026 signal belongs here because it cuts against the plateau reading: cost collapse. Release trackers through mid-2026 show a model cadence too fast for independent evaluators to keep up with — the current frontier includes the Claude 5 family, OpenAI's GPT-5.6 line (GA July 2026), and Google's Gemini 3.x line — and cost-per-unit-intelligence dropping by roughly half across tiers in months. Even under a frozen frontier, a 50% cost halving-time changes what gets deployed everywhere. The future of AI may be decided less by the peak of the curve than by its price.

## 8. What this room does not know

A short section, because its absence is how futurism rots. Nobody outside the frontier labs knows the results of unpublished training runs, which means every public analysis — including this one — runs a year behind the private evidence. Nobody has a validated method for predicting capability *emergence* (which specific abilities appear at which scale), as opposed to aggregate benchmark trends. Nobody knows whether the current architecture family has a ceiling below transformative capability, because [we cannot yet read what these models actually compute inside](mechanistic-interpretability.html) — the instrument for that question is still being built. And nobody has settled whether eval performance is measuring the thing we care about or a correlate that decouples under pressure; [the benchmarks room](benchmarks.html) is about exactly that gap.

## Conclusion

Here is what you can now do that you couldn't before. You can name the one empirical quantity most of the disagreement reduces to — whether the time-horizon doubling survives the reasoning-compute convergence of 2026–27 — and you can run the extrapolation yourself, with the spread, in four lines of arithmetic. You can hear "the year of agents" and ask for the production number, not the adoption number. You can read a robot press release and ask for the audited count. And you can classify any confident claim about AI's future into scenario-with-named-assumptions or prophecy-in-a-lab-coat within a paragraph.

From here: [leading-models](leading-models.html) maps the current frontier this room kept pointing at; [forecasting](forecasting.html) goes deeper on the craft of prediction itself; [trends-gap](trends-gap.html) dwells on the capability-deployment lag; [what-ai-can-bring](what-ai-can-bring.html) and [the-future](the-future.html) take up the question this room deliberately stopped short of — what any of it is *for*.

## Open questions

**Established (FACT):** Measured task time-horizons of frontier models grew exponentially through January 2026, with the recent-window doubling near 89 days and large stated uncertainties. Reasoning-RL compute was still well below the pretraining frontier as of the 2025 analyses, implying a one-time overhang. 2026 hyperscaler capex guidance and estimates are in the high hundreds of billions of dollars. In McKinsey's 2025 survey, organizations reporting any AI use (88%) far outnumbered those scaling an agentic system somewhere (23%), and no single function exceeded 10%. BMW and Agility/GXO have documented bounded industrial humanoid deployments; those records do not establish an industry-wide fleet total.

**Contested (HYPOTHESIS):** That pretraining returns have genuinely bent — Sutskever argues they will, but public failed-run data is insufficient to measure the bend. That eval time-horizons translate proportionally into deployed autonomy. That AI is already materially accelerating AI research. That frontier revenue will grow fast enough to sustain the buildout. Each of these could resolve either way on public evidence within a few years.

**Speculation worth holding (WILD):** That a third scaling axis — beyond pretraining and inference-time compute — exists and will be found before the current overhang is spent. That the production gap, once closed, releases stored capability abruptly rather than gradually, making the economy's response discontinuous even if the science is smooth. That the systems being scaled are on a path to something it would be correct to call understanding — a question no benchmark in this room can settle, and the reason the [instrument series](mechanistic-interpretability.html) exists.

There is one more thing worth saying plainly, because the domain itself points there. Every scenario in this room is secretly a claim about attention. The scaling debate asks whether stacking more of it — more compute attending over more context for longer — keeps yielding more capability. The time-horizon metric gives one operational measure of how long a system can hold a task without losing the thread. The capex numbers are a civilization redirecting a measurable fraction of its energy toward building artificial attenders, while [the attention economy](attention-economy.html) strip-mines the human kind. The forecasts disagree about dates; they quietly agree about the object. Whatever the future of AI turns out to be, it will be the future of where attention lives, what can sustain it, and what it is for — and that question does not wait for 2027 to be worth asking.

## Sources

- METR, [Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/) (Jan 2026) and [Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) (Mar 2025) — time-horizon measurements, doubling times, and caveats; both read directly.
- Josh You, Epoch AI, [How far can reasoning models scale?](https://epoch.ai/gradient-updates/how-far-can-reasoning-models-scale) — reasoning-compute overhang and convergence argument; read directly.
- Ilya Sutskever, NeurIPS 2024 talk ("pretraining as we know it will end") — widely reported; quote as reported, talk not independently re-watched for this room.
- J.P. Morgan, [Financing AI infrastructure and U.S. data centers](https://www.jpmorgan.com/insights/banking/capital-markets/financing-ai-infrastructure-data-centers) — $697B 2026 five-hyperscaler estimate. The separate ~$725B four-company sum uses Amazon, Alphabet, Microsoft, and Meta guidance as reported by [CNBC](https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html); the two totals have different scopes and dates.
- McKinsey, [The State of AI: Global Survey 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) — 88% any-AI use, 23% scaling an agentic system somewhere, and no more than 10% in any one function. Gartner's 40%-canceled prediction is a forecast and is labeled as such.
- BMW Group, [First humanoid robot introduced in Plant Leipzig](https://www.bmwgroup.com/en/news/general/2026/humanoid-robot-in-leipzig.html) — primary company record of the bounded Figure 02 Spartanburg deployment. Agility Robotics, [GXO multi-year Digit deployment](https://www.agilityrobotics.com/content/gxo-signs-industry-first-multi-year-agreement-with-agility-robotics) — primary company announcement, with no fleet count asserted here.
- Mid-2026 model releases and pricing trends — aggregator release trackers ([LLM Gateway](https://llmgateway.io/timeline) and similar); lower-trust sources, used only for cadence and cost-direction claims, so labeled.
- Simon (1965) and Minsky (1969) predictions — standard AI-history record; see [history-of-ai](history-of-ai.html) for primary sourcing.

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
