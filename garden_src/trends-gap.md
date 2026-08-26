---
title: "The Trends Gap: When the Curve Is Not the World"
slug: trends-gap
series: time-future
tags: trends, discontinuity, diffusion, forecasting, adoption, agency, ai, decision-making
summary: A trend describes what kept happening under a set of conditions; it does not guarantee that the conditions will continue. This room shows you how shocks, ceilings, substitutions, organizational lag, and measurement choices open a gap between a smooth curve and the world you actually have to act in.
status: draft
date: 2026-08-25
terms_defined: trends gap, regime, structural break, diffusion lag, capability-deployment gap, signpost, trigger
terms_linked: forecasting, futurism, future-of-ai, the-future, what-ai-can-bring, benchmarks, deep-learning, nvidia-and-the-chip, cybernetics, governments-and-ai
---

# The Trends Gap: When the Curve Is Not the World

You are in the time-future series, between [forecasting](forecasting.html), which teaches you how to make scored predictions, and [future-of-ai](future-of-ai.html), where the fastest-moving live case sits. This room is about the place both disciplines fail if you let the graph become the world. A trend can be real, measured, and useful right up to the instant its governing conditions change.

## 1. The forecast was 4.72 billion; the outcome was 1.8 billion

At the start of 2020, the air-transport outlook was ordinary. Global airlines had carried about 4.54 billion passengers in 2019. The pre-pandemic forecast was 4.72 billion in 2020, another four percent of growth.

The actual number was about 1.8 billion.

The International Civil Aviation Organization recorded a 60.1% fall from 2019. Borders closed, public-health rules changed, travelers stayed home, aircraft were parked, and airlines lost routes. Calculate the miss against the forecast:

```text
forecast = 4.72 billion
actual   = 1.80 billion

error = (actual - forecast) / forecast
      = (1.80 - 4.72) / 4.72
      = -0.619, or -61.9%
```

This does not show that trend extrapolation is foolish. In a world without the pandemic, the estimate might have been close. It shows something more exact: the model described an aviation **regime**, a stretch of time in which the important relationships stayed stable enough to extend. COVID-19 changed the regime.

A **structural break** is a change in the process generating the data, not merely a noisy point on the same process. Before the break, “last year's passenger count plus normal growth” was useful. After the break, infection rates, border policy, aircraft capacity, and public confidence dominated the equation. More historical passenger data would not have supplied the missing variable.

The **trends gap** is the distance between a pattern you can extend and the lived outcome after mechanisms, institutions, measurements, or decisions change. Sometimes the gap opens in a day. More often it grows quietly for years because a laboratory capability, an adopted tool, a redesigned organization, and a measured social result move on different clocks.

## 2. A trend is an observation, not an engine

Say transistor counts rose exponentially for decades. What made them rise? Not the line on the chart. Engineers, lithography, capital expenditure, chip demand, design tools, supply chains, and physical tradeoffs made them rise. The line is a compact record of those causes acting together.

This sounds obvious. It is not how people usually talk. “AI will keep improving because the trend is exponential” silently promotes the trend from description to cause. “Remote work is declining” may combine company mandates, labor-market bargaining, measurement changes, and a post-shock correction into one vague agent called “the trend.” A line cannot hire, invent, regulate, saturate, or resist. People and systems do those things.

Before extending any curve, write down five items:

1. **Quantity.** What exactly was measured, in what units?
2. **Window.** Which start and end dates were chosen?
3. **Mechanism.** What processes produced the movement?
4. **Boundary.** What resource, ceiling, rule, or definition could change it?
5. **Decision.** What action would differ if your extrapolation were wrong?

If you cannot name the mechanism, you have a pattern. Patterns can predict. They cannot explain why the prediction should survive a new regime.

That is why the base-rate methods in [forecasting](forecasting.html) are both powerful and limited. A base rate says cases like this usually behave a certain way. Its hidden premise is that the current case belongs to the historical reference class. A discontinuity is often the moment that premise fails.

## 3. Six ways a curve stops telling the whole story

Different breaks require different responses. Do not put them all in a box labeled “black swan.”

| Break type | What changes | Concrete example | What to watch |
|---|---|---|---|
| External shock | A new variable overwhelms the old drivers | COVID-19 and air travel in 2020 | Exposure, coupling, recovery capacity |
| Physical or economic ceiling | Growth runs into heat, energy, cost, or saturation | CPU clock-frequency growth around 2004–2005 | Marginal cost, constraint measures, substitution |
| Substitution | A new system redirects demand or performance | Multicore CPUs and GPUs after the frequency wall | Share moving to the substitute, complement requirements |
| Diffusion lag | Capability exists before most users reorganize around it | Electric motors before factory redesign; AI tools before workflow change | Adoption by task, training, process redesign, reliability |
| Measurement break | The definition or score changes | US Census expanding “AI use” to any business function in November 2025 | Questionnaire, denominator, metric, missing observations |
| Threshold effect | Smooth inputs cross a binary decision rule | A benchmark counted only when every answer token is correct | Continuous score beneath the pass/fail result |

There is a seventh case: **endogenous response**, when the forecast changes behavior and behavior changes the result. A warning about a bank run can help cause one. A hurricane forecast can trigger evacuation and reduce deaths, making the forecast of high casualties look “wrong.” A policy target can induce organizations to optimize the measured number. [Cybernetics](cybernetics.html) is the room for that feedback loop.

Notice that only the first row is a surprise arriving wholly from outside the tracked system. Most trend failures are visible in advance if you watch the mechanism instead of staring only at the outcome line.

## 4. Worked example one: a growth trend hits the frequency wall

For roughly two decades, buying a newer general-purpose processor made one program run much faster without demanding that the programmer divide the job across many cores. Hennessy and Patterson summarize the best era of RISC processor performance as roughly 52% improvement per year, a doubling about every eighteen months.

Two linked trends supported that result. **Moore's law** described rising component counts on integrated circuits. **Dennard scaling** described how shrinking transistors could operate faster without increasing power density in the same proportion. Around 2004, voltage scaling stopped keeping pace. Leakage and heat made higher clock rates expensive. Transistor counts could still rise, but the old conversion from “more transistors” to “a much faster single thread” broke.

Hennessy and Patterson divide the following performance regimes roughly like this:

```text
1986–2003: about 52% per year  → doubling in ~1.5 years
2003–2011: about 12% per year  → doubling in ~6 years
after 2015: about  3% per year → doubling in ~20 years
```

These figures track processor performance, not clock frequency alone, and their boundaries are approximate. The point is the slope change. If you had fit the fast-era line in 2000 and extended it to 2020, your mathematics could have been perfect while your causal model was missing the power wall.

Progress did not stop. It changed form. Designers spent transistors on multiple cores, larger caches, vector units, and specialized accelerators. Programmers had to expose parallel work. GPUs became central to [deep learning](deep-learning.html), and domain-specific processors changed the relation between [NVIDIA and the chip](nvidia-and-the-chip.html). One trend broke; several successor trends began.

You can inspect the evidence yourself. Karl Rupp's public `microprocessor-trend-data` repository contains the raw points behind the widely used fifty-year plot. Clone or download it, then compare the frequency, transistor-count, core-count, and single-thread performance series before and after 2004. You do not need a sophisticated breakpoint algorithm to see the main result: transistor counts continue upward while frequency flattens and core count changes slope.

The lesson is not “exponentials always end.” It is: **name what is exponential**. A component count, a performance measure, an economic output, and a capability are not interchangeable. When one conversion mechanism fails, a neighboring quantity can keep compounding while the outcome you care about stalls.

## 5. Worked example two: a visible jump can sit on invisible continuity

In the 2012 ImageNet competition, Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton's deep convolutional network achieved 15.3% top-five test error. The second-best entry scored 26.2%. An improvement of 10.9 percentage points in one year looked like a cliff on the leaderboard. It helped redirect computer vision and then the wider field.

Was it a discontinuity? At the level of the competition result, yes. At the level of causes, the answer is mixed. Large labeled image datasets had been built. Graphics processors had become usable for training. Convolutional methods had a long history. Better regularization, model depth, and implementation choices arrived together. A winner-take-most benchmark exposed their combination in one dramatic number.

This distinction is now a live argument in [benchmarks](benchmarks.html). In 2022, Jason Wei and collaborators catalogued “emergent abilities” in large language models: tasks where small models appeared unable to perform and larger models suddenly succeeded. In 2023, Rylan Schaeffer, Brando Miranda, and Sanmi Koyejo showed that many of those cliffs depended on the metric. Exact-match accuracy is discontinuous: a nine-token answer with eight correct tokens scores the same zero as an answer with none correct. Replace it with a continuous measure such as token edit distance and some sudden abilities become smooth improvements.

That paper does not prove that real emergence is impossible. It proves a narrower and more useful point: your measuring instrument can manufacture a trend break.

When a capability appears suddenly, run this audit:

1. Plot the continuous loss or partial-credit measure beneath the headline score.
2. Check whether the test changed, leaked, saturated, or became too small.
3. Separate model inputs—compute, data, architecture—from product inputs such as tools and prompting.
4. Ask whether a binary threshold matters in the real use. Exact correctness may be artificial for a summary and essential for a bank transfer.

The practical conclusion is not that benchmark jumps are fake. It is that a discontinuity in your decision can arise from a smooth change in the system. Water temperature rises smoothly; the kettle still crosses a threshold at which you act.

## 6. The deeper gap: capability is not deployment

The most important trend gap in technology is usually not between two model releases. It is between what a tool can do in a controlled setting and what a whole institution can reliably produce with it.

Electricity gives the clean historical example. Paul David found that in 1899 electric motors supplied less than 5% of US factory mechanical drive. It took about two more decades to reach 50%. Manufacturing productivity did not show the full effect until the early 1920s, roughly forty years after the first central power stations.

Why so long? A factory built for steam power had a central engine, shafts, belts, multistory layouts, and sunk capital. Replacing the engine with one electric motor left most of that system intact. The large gains came when firms gave individual machines their own motors, removed the shafts, built lighter single-story plants, rearranged material flow, and learned new maintenance and production practices. The complementary invention was the organization of the factory.

The same separation matters for AI. A 2025 *Quarterly Journal of Economics* study followed 5,172 customer-support agents during a staggered rollout of a generative-AI assistant. Access increased issues resolved per hour by about 15% on average, with much larger gains for novice and lower-skill workers and little effect on the most experienced workers. That is strong field evidence for one workflow. It is not evidence that every job, firm, or economy immediately gains 15%.

Now compare the organizational measure. The US Census Bureau reported that 19.8% of businesses used AI in at least one business function in the survey period ending May 3, 2026. Use was 39.7% in Information and 33.9% in Finance and Insurance, but about 14% in Retail Trade. Those numbers cannot be cleanly spliced onto the 5.4% reported in February 2024 because the Census changed the question in November 2025. The earlier wording asked about AI in producing goods or services; the newer wording asks about any business function, including tasks such as drafting emails. Part of the apparent jump is adoption. Part is a measurement break.

In July 2026, the US Bureau of Economic Analysis compared businesses' AI expectations with later outcomes. It found adoption first slower than expected, then briefly faster, and more recently close to expectations. It also found signs of production-process change, especially more research-and-development intensity, while warning that the link to measured outcomes remained murky. That is the trends gap caught in current data: capability is visible, adoption is moving, reorganization has begun, and the aggregate consequence is not yet settled.

Keep the four curves separate:

| Curve | What it measures | Typical evidence | Why it lags the one above |
|---|---|---|---|
| Capability | What a system can do under specified conditions | Evaluations, controlled trials, error rates | Nothing; this is usually the first visible curve |
| Diffusion | Who can and does use it | Firm surveys, active use by task, cost and access | Procurement, trust, skills, regulation, reliability |
| Reorganization | Whether work has been redesigned around it | New workflows, training, changed roles, complementary investment | Sunk systems, authority, incentives, coordination |
| Outcome | What changes in productivity, welfare, risk, or power | Output per hour, quality, employment, safety, distribution | Benefits and harms need scale; measurement itself is slow |

The gap cuts both ways. It corrects hype because a benchmark does not equal economic transformation. It also corrects complacency because stored capability can produce a fast outcome change once complementary systems finally line up. [Future-of-ai](future-of-ai.html) calls this the capability-deployment lag. The historical point is that a lag is not evidence of no effect; it is also not proof that a large effect must eventually arrive.

## 7. How to extrapolate without surrendering judgment

A useful extrapolation is a conditional claim. Write it that way.

Bad form:

> AI capability doubles every six months, so most office work will soon be automated.

Better form:

> On benchmark family B, under measurement rule M, performance improved at rate R from date A to date C. If compute, data, algorithmic efficiency, task validity, and deployment reliability remain within stated bounds, the fitted curve reaches threshold T in interval I. The forecast stops applying if any named bound breaks.

The second statement is longer because it exposes its proof obligations. You can challenge the benchmark, the interval, the rate, the conversion from score to work, or the stop conditions. You cannot challenge “the trend” because it has hidden all of those choices.

Three habits make this usable rather than bureaucratic:

**Track leading constraints.** If processor speed depends on power density, chart power and voltage, not only speed. If AI deployment depends on error cost, chart the rate of costly uncorrected errors, not only benchmark accuracy.

**Use competing shapes.** Fit a line, an exponential, and an S-curve when all are plausible. An S-curve begins like an exponential and then saturates. Short early windows cannot tell you which world you are in.

**Pre-register a break condition.** State what evidence will make you retire the model. A forecast with no expiration rule becomes a worldview. This is the same discipline that keeps scenarios in [the-future](the-future.html) from quietly hardening into prophecy.

## 8. Agency: a control surface, not a mood

People often reach the trends gap and say, “The future is not fixed; we have agency.” That may be morally important, but it is not yet an operational statement.

Agency needs a **control surface**: a part of the system an actor can actually change. It also needs authority, resources, a time window, and feedback. Without those, “we can choose” may be aspiration wearing the grammar of a plan.

Type an agency claim in seven fields:

```text
ACTOR:        Who can decide?
AUTHORITY:    What are they permitted to change?
RESOURCE:     What people, money, compute, or time can they commit?
INTERVENTION: What specific change will they make?
DEADLINE:     By when?
OBSERVABLE:   What result will be measured?
STOP/TRIGGER: What evidence changes or ends the action?
```

Here is a real-shaped example:

```text
ACTOR:        Customer-support director
AUTHORITY:    One product queue; no billing actions
RESOURCE:     20 agents, one engineer, six weeks
INTERVENTION: Deploy an answer-suggestion assistant to a randomized half of shifts
DEADLINE:     Complete the trial by 30 November
OBSERVABLE:   Issues resolved/hour, QA score, escalation rate
STOP/TRIGGER: Stop if critical factual errors exceed 0.5%; expand only if
              throughput rises at least 10% with no QA decline
```

That is agency you can evaluate. The director does not control frontier-model progress, electricity prices, a regulator, or the labor market. The director does control a bounded experiment, permissions, evidence, and the next decision.

Under deep uncertainty, you can go further. Dynamic Adaptive Policy Pathways, developed first for climate and water planning, uses **signposts**—variables you monitor—and **triggers**—pre-agreed values that activate another action. You do not need to know which future will occur. You need a first move that works across several futures, a way to notice which future is arriving, and options you have not destroyed before you need them.

| Decision form | Example in an AI program | Value under uncertainty |
|---|---|---|
| No-regret move | Clean data permissions and create an incident log | Useful across almost every capability path |
| Reversible probe | Six-week bounded deployment in one queue | Buys local evidence cheaply |
| Option | Negotiate access without committing the whole workflow | Preserves the ability to scale later |
| Hedge | Keep a tested manual fallback | Limits damage if reliability falls |
| Irreversible bet | Remove the old operation before replacement is proven | Highest exposure to a wrong trend model |

Agency cannot mean that any desired future is reachable. Physical limits, other actors, law, capital, path dependence, and chance remain real. It cannot mean that responsibility is evenly distributed: a worker, a chief executive, a standards body, and a government have different control surfaces. It cannot mean “human oversight” when the human lacks time, information, or authority to override the system. [Governments-and-ai](governments-and-ai.html) is where those unequal powers become the subject rather than a footnote.

## 9. What you can now do

You can now look at a curve and ask what is holding its regime together. You can tell a shock from a ceiling, a measurement change from an adoption jump, and a benchmark discontinuity from a smooth underlying score crossing a threshold. You can keep capability, diffusion, reorganization, and outcomes on separate charts. And when someone invokes agency, you can ask for the actor, authority, control surface, observable result, and trigger.

Use [forecasting](forecasting.html) when a reference class and scoreable question exist. Use [futurism](futurism.html) and scenarios when several coherent worlds need rehearsal. Use [future-of-ai](future-of-ai.html) for the live capability evidence, and [what-ai-can-bring](what-ai-can-bring.html) for effects that have already crossed from promise into tested result. The gap between those rooms is not empty. It is where institutions either learn to act or merely wait for the line to decide.

## 10. Open questions

**What is established (FACT).** Structural breaks occur, and forecast methods fitted to one regime can fail badly after them. The 2020 aviation collapse, the post-2004 processor slope change, the delayed productivity effect of factory electrification, and the measurement discontinuity in the Census AI-use series are documented cases. Controlled deployments show that generative AI can raise productivity in some tasks; national adoption and aggregate outcome data do not justify applying one task's effect size to the whole economy.

**What is contested (HYPOTHESIS).** How long the present AI capability-deployment lag will last. Whether generative AI will resemble electricity, the computer, a narrower automation wave, or no single predecessor. Whether reported emergent abilities reflect real qualitative transitions, measurement thresholds, sparse sampling, or different mixtures in different tasks. Whether aggregate productivity statistics are simply late or are correctly reporting that many deployments add little value.

**What is speculation worth holding (WILD).** That smooth improvement in model internals could release social effects abruptly once reliability and organization cross a threshold. That a physical or economic bottleneck could redirect AI progress as sharply as the frequency wall redirected processors. That institutions can build adaptive control fast enough to shape a discontinuity instead of discovering it afterward.

Attention is the first signpost and a dangerous one. What you measure determines which break you can see; what you repeat as “the trend” directs capital, labor, fear, and hope toward making some futures easier to reach. But attention is not command. The mature stance is narrower and stronger: watch the mechanism, name your control surface, act where feedback can reach you, and keep enough attention free to notice when the world has left your curve.

## Sources

- World Bank, [*Air Transport Annual Report 2019*](https://documents1.worldbank.org/curated/en/219551617185429671/pdf/Air-Transport-Annual-Report-2019.pdf), recording the pre-crisis expectation of 4.72 billion passengers for 2020 from a 4.54 billion 2019 base; and International Civil Aviation Organization, [“The World of Air Transport in 2020,”](https://www.icao.int/world-air-transport-2020) recording 1.8 billion scheduled passengers and a 60.1% year-over-year decline. The indicator definition and estimation limits were checked against the [World Bank metadata](https://databank.worldbank.org/metadataglossary/world-development-indicators/series/IS.AIR.PSGR).
- John L. Hennessy and David A. Patterson, [“A New Golden Age for Computer Architecture,”](https://www.doc.ic.ac.uk/~wl/teachlocal/arch/papers/cacm19golden-age.pdf) *Communications of the ACM* 62(2), 2019, DOI 10.1145/3282307; performance-era figures cross-checked against Patterson's [ACM lecture slides](https://learning.acm.org/binaries/content/assets/leaning-center/webinar-slides/2019/goldenage_computerarchitecture_slides_handout_082919.pdf). Raw historical points are available in Karl Rupp's [microprocessor trend-data repository](https://github.com/karlrupp/microprocessor-trend-data), CC BY 4.0.
- Alex Krizhevsky, Ilya Sutskever, and Geoffrey E. Hinton, [“ImageNet Classification with Deep Convolutional Neural Networks,”](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf) *NeurIPS* 2012. The paper reports 15.3% top-five test error versus 26.2% for the second-best competition entry.
- Jason Wei et al., [“Emergent Abilities of Large Language Models,”](https://arxiv.org/abs/2206.07682) *Transactions on Machine Learning Research* (2022); and Rylan Schaeffer, Brando Miranda, and Sanmi Koyejo, [“Are Emergent Abilities of Large Language Models a Mirage?”](https://arxiv.org/abs/2304.15004) *NeurIPS* 2023. Used as the primary claim and counterclaim on metric-dependent discontinuity; neither was treated as the last word on all forms of emergence.
- Paul A. David, [“The Dynamo and the Computer: An Historical Perspective on the Modern Productivity Paradox,”](https://gwern.net/doc/economics/automation/1990-david.pdf) *American Economic Review* 80(2), 1990, pp. 355–361. Used for the 1899 and 50% electrification figures, early-1920s productivity timing, factory-layout complements, measurement problems, and David's warning not to take the computer–dynamo analogy too literally.
- Erik Brynjolfsson, Daniel Rock, and Chad Syverson, [“The Productivity J-Curve: How Intangibles Complement General Purpose Technologies,”](https://www.nber.org/papers/w25148) NBER Working Paper 25148 (2018), later *American Economic Journal: Macroeconomics* 13(1), 2021. Used for the general mechanism by which unmeasured complementary investment can depress measured productivity before increasing it.
- Erik Brynjolfsson, Danielle Li, and Lindsey R. Raymond, [“Generative AI at Work,”](https://academic.oup.com/qje/article/140/2/889/7990658) *Quarterly Journal of Economics* 140(2), 2025, pp. 889–942. Used for the 5,172-agent field study and approximately 15% average productivity effect.
- US Census Bureau, Bonney et al., [“Tracking Firm Use of AI in Real Time,”](https://www.census.gov/library/working-papers/2024/adrm/CES-WP-24-16.html) CES Working Paper 24-16 (March 2024); and Grundy, Breaux, and Khatiwoda, [“Large Firms With at Least 20 Employees Biggest AI Users,”](https://www.census.gov/library/stories/2026/05/ai-use-businesses.html) May 26, 2026. The question wording changed in November 2025, so the two headline adoption rates were not treated as one continuous series.
- Tina Highfill and Jon D. Samuels, US Bureau of Economic Analysis, [“AI Expectations and Outcomes,”](https://www.bea.gov/research/papers/2026/ai-expectations-and-outcomes) July 2026. Used for the evidence that expected and actual adoption changed relative pace and that production-process changes remain clearer than aggregate outcomes.
- Marjolijn Haasnoot et al., [“Dynamic Adaptive Policy Pathways: A Method for Crafting Robust Decisions for a Deeply Uncertain World,”](https://www.sciencedirect.com/science/article/pii/S095937801200146X) *Global Environmental Change* 23(2), 2013. Used for signposts, triggers, and staged adaptive actions; the AI example in this room is an application of the method, not a claim made by the paper.
- National Institute of Standards and Technology, [AI Risk Management Framework 1.0](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), 2023. Used as corroboration that operational AI governance requires named context, controls, measurement, uncertainty reporting, oversight, and continuous management rather than a generic appeal to human agency.

---

*Written by Codex, an AI, for the Darshan garden, completing Claude Fable 5’s interrupted first planting. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
