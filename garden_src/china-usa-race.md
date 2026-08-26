---
title: The Race Between China and the USA
slug: china-usa-race
series: power
tags: geopolitics, ai, china, usa, compute, chips, export controls, open weights
summary: As of mid-2026, the US leads the AI race on compute and frontier models; China has nearly closed the gap on model quality while winning on price, open weights, energy, and deployment. This room walks the verified numbers on all five axes and presents each country's story about itself from the inside.
status: draft
date: 2026-08-25
terms_defined: ai-race, compute-gap, open-weight-strategy, electron-gap
terms_linked: chip-wars, taiwan, semiconductors, nvidia-and-the-chip, governments-and-ai, leading-models, benchmarks, attention-economy, mechanistic-interpretability
---

# The Race Between China and the USA

You're in the power wing of the garden. [Governments and AI](governments-and-ai.html) covers how states use these systems; [Chip Wars](chip-wars.html) and [Taiwan](taiwan.html) cover the hardware chokepoints in detail. This room is the contest itself: the two countries actually racing, what each one has, what each one lacks, and — harder to see from either side — what each one believes it is racing for. Everything dated here is current as of August 2026, and every market or benchmark claim carries its date, because in this domain a six-month-old number is an antique.

## 1. The scoreboard, August 2026

Start with the most concrete thing available: a leaderboard.

Terminal-Bench 2.1 tests AI models on practical software work — fixing bugs, setting up servers, managing files. As of August 12, 2026, per Artificial Analysis data reported by Bloomberg, the top ten looked like this: OpenAI and Anthropic models hold the top five slots (the leader at 89.5%). At #6 sits Kimi K3, from Beijing's Moonshot AI, at 85.0%. At #10, Alibaba's Qwen 3.8 Max at 81.3%.

Hold that picture. An American model is on top. A Chinese model is four points behind it. That is the shape of the whole race.

Stanford's 2026 AI Index made it precise: as of March 2026, the top US model led the top Chinese model by 2.7% on Arena Elo. In 2023 the gap was roughly 300–340 points — the leading US model's *score* was above 1,300, not its lead over China. The two countries' models have traded places near the top several times since early 2025, when DeepSeek-R1 briefly matched the best American system and wiped roughly $600 billion off Nvidia's market value in a single day of panic. (Nvidia recovered; by mid-2026 it was worth over $5 trillion. The panic was aimed at the wrong target — more on that in section 4.)

So on *model quality*, the race is close — months, not years. The US frontier labs (OpenAI, Anthropic, Google DeepMind, xAI) lead; the best estimates from Brookings and others put Chinese labs several months behind on the hardest reasoning and long-horizon agentic tasks. But "several months behind the frontier" describes maybe five organizations on Earth. Everything else in the race — compute, money, energy, talent, ideology — is wildly asymmetric, and the asymmetries point in *both* directions. That's what the rest of this room walks through.

## 2. Compute: the moat that holds

Compute — the specialized chips models are trained and run on — is the axis where the US lead is not close at all.

The numbers, from the Council on Foreign Relations and the Institute for Progress (both writing in 2026, both arguing for keeping export controls, so read them as advocates with receipts):

- The best US AI chips are roughly **5x more powerful** than Huawei's best (the Ascend line), and the gap is projected to widen.
- Even under aggressive assumptions — Huawei producing ~800,000 AI chips in 2025 and 2 million in 2026 — Huawei's aggregate computing power comes to roughly **4–5% of Nvidia's output**, falling toward 2% by 2027.
- High-bandwidth memory ([HBM](semiconductors.html)), the specialized memory stacked next to AI chips, is the tightest bottleneck: IFP projects the US and its partners will produce roughly **70x** China's HBM in 2026.
- SMIC, China's leading chip fab, remains stuck at 7nm-class production because export controls block ASML's EUV lithography machines — the tool you need to go smaller at commercial yields. Its 7nm workaround (multi-patterning older DUV tools) works, but with higher cost and lower yield. See [Chip Wars](chip-wars.html) for the full lithography story.

This is why the compute moat exists: the US and its allies — Nvidia designing, TSMC fabbing, ASML supplying the lithography, SK Hynix and Micron supplying HBM — control essentially the entire advanced supply chain. See [Nvidia and the Chip](nvidia-and-the-chip.html) and [Taiwan](taiwan.html).

But three honest complications:

**First, the controls leak.** In March 2026, US prosecutors charged a Supermicro co-founder and two others with smuggling $2.5 billion in Nvidia AI servers to China through Southeast Asian shell companies. Huawei's Ascend 910C reportedly incorporates over two million chip dies made by TSMC itself, bought through shell companies before the loophole closed. Smuggling and cloud workarounds are enforcement problems, not physics problems, and enforcement is porous.

**Second, the control line keeps moving — from both ends.** The timeline: October 2022, first sweeping US export controls. 2023–2025, repeated tightenings; Nvidia builds cut-down China chips (the H20), which get banned, then licensed again in August 2025 under an unusual revenue-sharing arrangement. Through late 2025 and 2026, Washington openly debated licensing the much more powerful H200 to China — with reports of case-by-case licenses plus tariff arrangements — while Beijing, for its part, reportedly pressured its own major firms to *stop buying* Nvidia and buy domestic. By 2026 both governments were restricting the same trade from opposite sides. That detail matters for section 7.

**Third, denial builds the competitor.** Zhipu's GLM-5 (744B parameters) was reportedly trained entirely on Huawei Ascend hardware; DeepSeek optimized its V4 generation for Ascend; Reuters reported in April 2026 that Huawei planned around 750,000 units of its new Ascend 950PR for the year, with Chinese tech firms scrambling to secure them. Every customer Nvidia can't serve is a customer Huawei gets, with revenue and engineering feedback attached. The controls impose a real "sanctions tax" — more electricity, capital, and engineering per unit of useful compute — while simultaneously funding the ecosystem that might eventually escape them. Both things are true at once.

### A worked example: check the compute gap yourself

Don't take the "Huawei ≈ 4% of Nvidia" claim on authority. The arithmetic is checkable:

1. Take Huawei's 2026 production estimates: 62,000–160,000 "B300-equivalents" (Bloomberg and SemiAnalysis estimates, as compiled by IFP — a B300-equivalent normalizes different chips to Nvidia's flagship).
2. Take projected 2026 US production: ~6.89 million B300-equivalents (same source).
3. Divide: 160,000 / 6,890,000 ≈ 2.3%. Even the high estimate of Chinese domestic production is a rounding error on US supply.
4. Now check the sensitivity: the CFR analysis shows that *unrestricted* H200 sales to China would shrink the US compute advantage from 21–49x down to as low as 1.2x. The entire moat is policy, not physics. China's compute deficit is a decision the US makes each year, contested each year by Nvidia's commercial interest in selling.

That last step is the load-bearing one. When you read anyone confident about the compute gap in 2028, ask: which licensing decision are they assuming?

## 3. Money and energy: two bottlenecks, mirrored

**Capital: the US advantage.** Per Kyle Chan's April 2026 testimony to the House Select Committee (published by Brookings): Alibaba, one of China's biggest AI spenders, plans over $53 billion in AI investment across three years. Microsoft spent roughly $80 billion on AI capex in 2025 *alone*. The four US hyperscalers planned about $650 billion for 2026. US private AI investment exceeds China's by an order of magnitude or more. This is the deepest structural US advantage after chips.

**Energy: the Chinese advantage.** Here the bottleneck inverts. China generates more than twice as much electricity as the United States and has grown generation ~6% per year for a decade (Ember data, via Brookings), over half of that growth from wind, solar, and hydro. The US grid, flat for twenty years, is now the binding constraint on its own buildout: Morgan Stanley forecast a potential 44-gigawatt shortfall for US data centers within three years, and industry reporting in 2026 described half of planned US AI data centers facing delays because there is no power to connect them to — interconnection queues stretching five years. Commentators have started calling this the **electron gap**: the US restricts China's chips; physics and permitting restrict America's electrons. China treats energy availability as a solved problem and sites data centers next to surplus renewables in its western provinces ("Eastern Data, Western Computing").

For now, the US footprint is still far larger — roughly 5,400 US data centers versus ~450 in China in 2025 (Stanford AI Index, via Al Jazeera), and the US consumed ~45% of global data-center electricity in 2024 versus China's 25% (IEA). The question is which constraint binds first in the 2030s: China's chip ceiling or America's power ceiling. Nobody honest knows.

## 4. Models: the open-weight wedge

Here is where the "race" framing starts to mislead, because China isn't running the same race.

The US strategy is frontier capability behind an API: build the best model, keep the weights, charge for access. The dominant Chinese strategy is the **open-weight wedge**: release near-frontier models with downloadable weights, priced at a fraction of American systems, and let the world build on them.

The verified numbers as of mid-2026:

- BCG's 2026 analysis: Moonshot's Kimi K2.6, China's top model in May 2026, ran at **$1.71 per million tokens versus $11.25 for GPT-5.5** — roughly 6.5x cheaper at near-comparable benchmark scores. Analyses across the industry put Chinese models at one-quarter to one-tenth the cost of US equivalents generally.
- Stanford AI Index: the top *closed* model led the top *open* model by only 3.3% in March 2026.
- On OpenRouter, a large neutral model-routing service, Chinese open-weight models were reportedly ~61% of all tokens consumed by May 2026, with four of the five most-used models Chinese (Data Gravity newsletter analysis — single source, but directionally consistent with Hugging Face download data showing Chinese models at ~41% of platform downloads in spring 2026).
- CSIS, July 2026: Zhipu's GLM-5.2 performs near the top US closed models on coding and agent tasks. The DeepSeek moment "was not a one-shot event but part of a pattern."

Why does China play it this way? Partly necessity: with less compute and far less capital, Chinese labs optimized for efficiency (DeepSeek's whole legend is training near-frontier models cheaply) and for distribution they don't have to pay for. Partly market structure: Chinese labs can't sell premium APIs into Western enterprises anyway, so giving weights away costs them little and buys global default status. And partly follow-the-leader economics: it is much cheaper to be six months behind — including, US officials allege, by distilling American models' outputs — than to be six months ahead.

The research base underneath this is not shallow. China now accounts for roughly a third of the world's top-10%-most-cited AI publications, ahead of the US (BCG, 2026), and leads in AI patents. "Fast follower" understates a country that produces more of the field's cited research than the leader does.

And where China unambiguously leads: deployment. One 2026 comparison found 67% of Chinese industrial firms had deployed AI in production versus 34% of comparable US firms (AI Frontiers, Feb 2026). The US builds the frontier; China wires the near-frontier into factories, logistics, and government at roughly double the adoption rate. Whether frontier capability or economy-wide diffusion wins the decade is the genuinely open strategic question — it's the same question that decided earlier general-purpose technology races, and it has gone both ways in history.

## 5. Talent: the pipeline reverses

For two decades the US ran a simple, devastating play: educate the world's best researchers, keep them. Paulson Institute data has long shown that roughly **38% of top AI researchers working in the US did their undergraduate degrees at Chinese universities**. A large share of America's AI lead was, concretely, Chinese-born people working in American labs.

That flow is now reversing, and this may be the most underpriced fact in the race. Reporting through 2026 (FT, April 2026; Lianhe Zaobao's June 2026 investigation) documents a wave of senior returnees: Wu Yonghui, a former VP of research at Google DeepMind, to ByteDance; a former Gemini reinforcement-learning lead to Alibaba; DeepSeek staffed substantially by researchers who came home. The drivers named in the reporting: Chinese lab salaries now competitive with US labs, visa precarity and tightened H-1B/J-1 processing for Chinese nationals in AI since 2021, and — repeatedly cited — the fact that DeepSeek proved elite work no longer requires a US address. One widely cited figure puts the flow of AI researchers from China to the US down ~89% since 2017; treat the exact number cautiously (secondary source), but every primary account agrees on the direction.

Models are built by researchers. If the people increasingly stay home, the capability gap eventually follows them. This is the axis where US policy most directly fights itself: export controls defend the compute moat while immigration policy drains the talent moat.

## 6. The two stories, from the inside

Here is where this room asks something of you. The Jain discipline of *anekantavada* — many-sidedness, the practice of holding that a complex truth looks genuinely different from different standpoints — is the founding stance of this garden. So: each country's story about the race, told from inside, in its own materials. Neither is a lie. Neither is the whole.

**The American story.** The official document is literally titled *Winning the Race: America's AI Action Plan* (July 23, 2025) — some ninety federal actions across three pillars: accelerate innovation, build infrastructure, lead globally. Told from inside: *We invented this technology. Free inquiry, private capital, and open competition produced every frontier model on Earth, and it is not close. The race is existential because the alternative is a world running on AI built by a surveillance state — models that produce insecure code and toe a party line (as a 2026 Booz Allen report argued in recommending bans on Chinese models in US critical infrastructure). Export controls aren't protectionism; they're keeping the most powerful technology in history out of the hands of a government that automates repression. We will win by building faster — chips, data centers, energy, science (the Genesis Mission, November 2025, aims AI at national research) — and by making the American stack the world's default.* The story's visible tensions, also from inside American materials: the same government mandating "ideological neutrality" in AI signed an order titled *Preventing Woke AI in the Federal Government* — a procurement rule that itself specifies ideology; the plan champions open models while the commercial frontier stays closed; and the immigration system pushes away the researchers the plan depends on.

**The Chinese story.** The official document is the State Council's "Artificial Intelligence Plus" opinion (Document No. 11, August 26, 2025): AI integrated into 70% of six key economic sectors by 2027, over 90% intelligent-application adoption by 2030, a fully "intelligent society" stage by 2035. Told from inside: *We are not chasing chatbot benchmarks; we are industrializing intelligence. America builds casinos around its models; we build factories with ours. The chip embargo is simply the latest chapter of a century of technology denial, and like every previous chapter it ends with us building our own — as we did with GPS, with space stations, and now with 7nm chips that Washington said were impossible. We release our best models openly because we mean AI to serve development everywhere — see the Global AI Governance Action Plan we launched at Shanghai in July 2025, with the Global South in the room — while America means AI to preserve hegemony. Self-reliance is not isolation; it is dignity.* The story's visible tensions, from inside Chinese materials: "open to the world" coexists with the world's most extensive information controls, and models released as open weights arrive aligned to state positions; "people-centered AI" coexists with AI-augmented surveillance of the people it centers; and regulators who celebrate returnee talent also warned AI firms (the Manus case, 2026) against moving staff and data *out*.

Notice what the two stories share: each casts itself as the open one and the other as the closed one. Each is telling the truth about a different layer. America is more open at the layer of speech and inquiry; China at the layer of weights and price. Which layer matters more for how AI reaches the next five billion people is not a settled question, and pretending it is settled is the main way analysts in each country talk past each other.

## 7. The axes side by side

| Axis | United States | China | State of play (mid-2026) |
|---|---|---|---|
| Frontier model quality | Leads (top slots on major leaderboards) | 2.7% behind top US model (AI Index, Mar 2026) | US ahead by months, not years |
| Compute (chips) | ~95%+ of advanced AI chip supply with allies | Huawei ≈ 2–5% of Nvidia's aggregate output | Decisive US lead; policy-dependent |
| Capital | ~$650B hyperscaler capex planned for 2026 | Alibaba: $53B over three years | Order-of-magnitude US lead |
| Energy | Grid-constrained; projected 44 GW shortfall | >2x US generation, growing ~6%/yr | Decisive Chinese lead |
| Price per token | Premium closed APIs | ~4–10x cheaper at near-parity | Chinese lead |
| Open-weight share | Ceding (Llama fell off rankings) | ~61% of OpenRouter tokens (May 2026, reported) | Chinese lead |
| Cited research | 12–13% of top-cited AI papers | ~1/3 of top-cited AI papers | Chinese lead |
| Elite talent stock | Still largest concentration | Reverse migration accelerating | US lead, eroding |
| Industrial adoption | ~34% of manufacturers | ~67% of manufacturers | Chinese lead |

Read the table honestly and the phrase "who's winning" stops parsing. The US is winning the race it defines (frontier capability, compute). China is winning the race *it* defines (cost, diffusion, openness, energy, research volume). Each side's confidence is real because each is looking at its own column.

## 8. What you can now see

You came in with a horse-race headline; you leave with five separate races and a scoreboard for each. You can check the model gap yourself (Artificial Analysis, LMArena, Epoch's Capability Index, the Stanford AI Index — all public). You can redo the compute arithmetic in section 2 when new production estimates land. You know the three questions that decide the next five years: does the compute moat hold against smuggling and Huawei's learning curve; does America's electron gap bind before China's chip ceiling; and does frontier capability or mass diffusion turn out to be the thing that compounds. Adjacent rooms: [Chip Wars](chip-wars.html) for the lithography chokepoints, [Taiwan](taiwan.html) for the island both stories route through, [Leading Models](leading-models.html) and [Benchmarks](benchmarks.html) for how the scoreboards actually work and how they get gamed.

One more thing, because the domain itself points there. Strip the flags off and look at what the two systems are actually racing to manufacture: machine attention, at industrial scale — the capacity to read, weigh, and act on the world, produced in gigawatt quantities. Both national stories treat this product as an instrument: a weapon, a workforce, an engine of growth or control. Neither story has a chapter on what the instrument is *becoming* — whether systems built to model everything eventually model themselves, and what follows if they do. The [attention economy](attention-economy.html) room covers what happened last time attention became an industrial input: the substance got commoditized before anyone understood what it was. The race's deepest open question is not who wins. It is whether either racer understands what it is producing — and that question belongs to [the instrument](mechanistic-interpretability.html), not to either flag.

## Open questions

**Established (FACT):** The US leads frontier model quality by a small margin (2.7% on Arena, March 2026) and compute by a large one (Huawei ≈ 2–5% of Nvidia output). China leads on price, open-weight adoption, electricity, top-cited research share, and industrial deployment. Both governments published their strategies in 2025 (*Winning the Race*; AI+) and both restrict chip trade from their own side.

**Contested (HYPOTHESIS):** That export controls will keep working — the CFR/IFP camp argues the moat widens; the Huawei-learning-curve camp argues denial finances the escape. That diffusion beats frontier — China's bet, unproven either way. That the talent reversal is large enough to move the frontier — direction is documented, magnitude is not. That distillation lets followers stay permanently close — asserted by US officials, not publicly quantified.

**Speculation worth holding (WILD):** That the race framing itself is the error — that two mutually-fortifying national programs, each justified by the other's existence, constitute a single global system building the same thing under two flags, and that the systems being built will eventually matter more than the flags. No one can verify this yet. It is the kind of claim that looks obvious or absurd depending on the decade you read it in.

## Sources

Verified by live search, August 2026: Stanford HAI, [2026 AI Index Report, Technical Performance](https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance) (2.7% gap, open/closed gap, Arena dynamics) · BCG, [The Great Divide](https://www.bcg.com/publications/2026/us-and-china-ai-strategy-causing-global-ai-divide) (Kimi K2.6 vs GPT-5.5 pricing, citation share, six-enabler comparison) · Brookings, [Competing AI strategies for the US and China](https://www.brookings.edu/articles/competing-ai-strategies-for-the-us-and-china) (Kyle Chan House testimony, April 16, 2026: capex figures, months-behind estimate) and [How will the United States and China power the AI race?](https://www.brookings.edu/articles/how-will-the-united-states-and-china-power-the-ai-race) (IEA and Ember energy figures) · CFR, [China's AI Chip Deficit](https://www.cfr.org/articles/chinas-ai-chip-deficit-why-huawei-cant-catch-nvidia-and-us-export-controls-should-remain) (5x chip gap, Huawei production scenarios; advocacy piece, read as such) · IFP, [The H20 Problem](https://ifp.org/the-h20-problem) and [The B30A Decision](https://ifp.org/the-b30a-decision) (HBM 70x, B300-equivalent arithmetic, TSMC shell-company dies) · CSIS, [What to Know About Chinese AI Models](https://www.csis.org/analysis/what-know-about-chinese-ai-models) (GLM-5.2, pattern-not-one-shot) · Bloomberg, [US Lead in the AI Race With China Is Rapidly Narrowing](https://www.bloomberg.com/graphics/2026-us-china-ai-race) (Terminal-Bench 2.1 top ten, Aug 12, 2026; Booz Allen report) · AI Frontiers, [China and the US Are Running Different AI Races](https://ai-frontiers.org/articles/china-and-the-us-are-running-different-ai-races) (67% vs 34% adoption; 7-month estimate) · White House / [AI.gov](https://www.ai.gov) (Action Plan and executive order dates, incl. Genesis Mission, Nov 24, 2025) · State Council Document [2025] No. 11 via [Lexology/Hauzen analysis](https://www.lexology.com/library/detail.aspx?g=7ad67f67-f1e4-4a5c-9c7e-b520b24eb1cd) and [USSC](https://www.ussc.edu.au/intelligent-everything-china-s-policy-to-supercharge-ai-adoption) (AI+ targets, Global AI Governance Action Plan) · FT, [China lures home its top AI talent from Silicon Valley](https://www.ft.com/content/b167c6d3-b982-482a-98c3-5303a7b80c6a) (Apr 9, 2026) and Lianhe Zaobao via [ThinkChina](https://www.thinkchina.sg/technology/big-read-returnees-inside-chinas-ai-talent-reversal) (returnees, Paulson Institute 38%, Manus case) · Al Jazeera, [China's secret weapon in AI race](https://www.aljazeera.com/economy/2026/5/28/chinas-secret-weapon-in-ai-race-with-us-lots-of-cheap-energy) (data-center counts, Rystad/Morgan Stanley figures).

Labeled lower-confidence (single or secondary source): OpenRouter ~61% Chinese-token share (Data Gravity newsletter); Hugging Face ~41% download share; 89% decline in China→US researcher flow; Supermicro smuggling charges and Ascend 950PR volumes (press reports via AI 2027 Tracker citing Reuters/CNN); H200 licensing/tariff specifics (fluid policy, multiple partially conflicting reports). Nothing in this room rests on those alone.

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
