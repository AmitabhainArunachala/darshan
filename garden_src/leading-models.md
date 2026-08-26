---
title: The Leading Models (2026)
slug: leading-models
series: story-of-ai
tags: frontier models, llm, anthropic, openai, google, xai, meta, deepseek, qwen, moonshot, zhipu, open weights, pricing
summary: A dated map of the AI frontier as of late August 2026 — which labs ship which model families, what they cost, who can access them, and how to verify all of it yourself. Every number here was checked by live search on 2026-08-25 and will drift; the article teaches you to re-check it.
status: draft
date: 2026-08-25
terms_defined: frontier model, model family, access tier, open weights, effort dial
terms_linked: history-of-ai, evolution-of-ai, future-of-ai, benchmarks, pretraining-post-training, governments-and-ai, china-usa-race, chip-wars, nvidia-and-the-chip, mechanistic-interpretability, neural-networks, attention-economy
---

# The Leading Models (2026)

If you've read [history-of-ai](history-of-ai.html), you've seen how we got from perceptrons to transformers. If you've read [evolution-of-ai](evolution-of-ai.html), you've seen the scaling era that produced GPT-4 and its successors. This room is the snapshot: who is at the frontier right now, late August 2026, with names, dates, and prices. Snapshots rot. So the room has two jobs — give you the current map, and teach you to redraw it yourself, because by the time you read this, at least one row of the table below will be stale.

## 1. How to read a model release in 2026

Start with one number: Anthropic shipped four frontier models in under two months this summer — Mythos 5 and Fable 5 on June 9, Sonnet 5 in June, Opus 5 on July 24. Google shipped a new Flash model on July 21 and replaced it 23 days later on August 13. xAI shipped Grok 4.5 on July 8 and Grok 4.6 on August 12, 35 days apart.

That cadence is the single most important fact about the 2026 frontier. The era of the blockbuster launch — one big model per year, one big number attached — is over. What ships now is a stream of incremental checkpoints, and the competition has visibly shifted from "who has the smartest model" to "who delivers the most useful work per dollar." When Google's own pitch for Gemini 3.7 Flash is a price cut, and Anthropic's pitch for Opus 5 is "near our best model at half the price," you're watching a price war, not just a capability race.

Three concepts unlock everything else in this room:

**A frontier model** is a model at or near the top of the current capability range — the models a lab bets its reputation on. In August 2026 that's a group of maybe ten models across seven or eight labs.

**A model family** is a lab's tiered lineup: a big expensive model for the hardest problems, a mid-tier "workhorse" for daily use, and a small cheap model for high-volume tasks. Every major lab now ships this way. Anthropic calls its tiers Opus, Sonnet, Haiku (with Fable and Mythos above them); OpenAI's GPT-5.6 family is Sol, Terra, Luna; Google's are Pro, Flash, Flash-Lite. The word "workhorse" — meaning the mid-tier model priced for everyday use — appears in the marketing of at least three labs this summer, which tells you where the actual revenue is.

**An access tier** is the answer to "who can use it, and how": free chat with limits, a ~$20/month consumer subscription, a $100–250/month power-user subscription, metered API pricing per million tokens, or — new in 2026 — restricted access requiring government or lab approval. That last tier did not meaningfully exist a year ago. It does now, and section 5 tells that story.

One warning before the map. Nearly every sentence a lab publishes about its own model is written in marketing grammar: "our most intelligent model yet," "best-in-class agentic performance." This room strips that grammar. Where a claim below is a vendor's own claim, it says so. Where a number comes from an independent evaluator, it says that too. For how benchmark numbers themselves get gamed, see [benchmarks](benchmarks.html).

## 2. The closed frontier: five labs

### Anthropic (Claude)

The current lineup, top to bottom: **Claude Mythos 5** (restricted access — more below), **Claude Fable 5** (released June 9, the flagship, $10 input / $50 output per million tokens), **Claude Opus 5** (July 24, $5/$25, 1M-token context, 128K max output), **Claude Sonnet 5** ($2/$10, the everyday default), and **Claude Haiku 4.5** at the cheap end. Disclosure that this page owes you: the AI writing it is Claude Fable 5. Judge the sourcing accordingly — every claim about Anthropic here is cited to external coverage or Anthropic's own dated announcements, not to self-knowledge.

Opus 5 is the strategically interesting release. Anthropic's pitch — near-Fable performance at half the price — was echoed by independent coverage, and it became the default model on the Claude Max plan at launch. It introduced a five-level "effort dial": a parameter from `low` to `max` that trades output quality against token spend on a per-request basis. That knob matters more than it sounds. Two teams paying identical per-token rates can now run up very different bills, and "which model" is becoming a less important question than "which model at which effort."

Mythos 5 sits above Fable and is not generally available. Anthropic's own platform documentation describes it as limited to approved customers in something called Project Glasswing, with access arranged through Anthropic, AWS, or Google Cloud account teams. Independent coverage reports it was also made available to a small set of vetted cyberdefense organizations. A frontier model you cannot buy at any price, gated by vetting rather than money, is a genuinely new kind of access tier.

### OpenAI (GPT)

OpenAI's current family is **GPT-5.6**, generally available July 9, 2026, in three tiers: **Sol** (flagship, $5/$30 per million tokens), **Terra** (balanced, $2/$12), and **Luna** (cheap and fast, $0.20/$1.20). OpenAI markets Sol as its best coding model; independent coverage credits the family less for peak capability than for efficiency — doing comparable work in fewer output tokens and less time than competitors.

The release path is worth noting: GPT-5.6 spent roughly two weeks in a limited preview restricted to trusted partners at the request of the U.S. government before public launch. Hold that thought for section 5.

### Google DeepMind (Gemini)

Google is the strange case of 2026: enormous shipping velocity on the mid-tier, and a visibly stuck flagship. The current Pro model is **Gemini 3.1 Pro** (previewed February 2026; $2/$12 per million tokens under 200K context, $4/$18 above; Google's docs list a 2M-token context window, the largest at the frontier). Its successor, Gemini 3.5 Pro, was announced at Google I/O on May 19 with a "next month" target — and as of late August it still has not shipped. Bloomberg reported internal delays over unmet performance goals; Ars Technica noted the slip openly. Meanwhile the Flash line churns: **Gemini 3.6 Flash** on July 21, then **Gemini 3.7 Flash** on August 13 — 23 days later — at an introductory $0.75/$3.75 through the end of 2026, roughly half the 3.6 price. A specialized **3.5 Flash Cyber** model, fine-tuned for finding and fixing security vulnerabilities, shipped in the same July drop. Google has also said its most ambitious pretraining run yet, for Gemini 4, is underway — see [pretraining-post-training](pretraining-post-training.html) for what a claim like that actually involves.

The honest read: Google is winning on price and cadence at the tier where most tokens are actually bought, and struggling at the very top. Whether that's a temporary stumble or a structural fact is an open question (section 8).

### xAI (Grok)

**Grok 4.6** shipped August 12, 2026, 35 days after Grok 4.5. Specs from xAI's own docs: 500K-token context, text-and-image input, $2/$6 per million tokens under 200K prompt tokens, jumping to $4/$12 for the whole request once the prompt crosses 200K. It added an `xhigh` reasoning level, and independent evaluation (Artificial Analysis) scored it in the same cluster as the other frontier flagships, with coverage noting strong turn-efficiency on long agent tasks alongside a measured regression on some agentic-coding benchmarks. Distinctive weaknesses: the smallest context window among the flagships and no EU API regions at launch.

### Meta (Muse — and the end of Llama as frontier)

Meta's 2026 is a whiplash story. After the poorly received Llama 4 in 2025, Meta reorganized its AI effort under Alexandr Wang (acquired in the $14.3B Scale AI deal) as Meta Superintelligence Labs, and in April 2026 shipped **Muse Spark 1.0** — closed weights, a first for the company that had been the standard-bearer of open AI. **Muse Spark 1.2** followed on August 5 (1M context, closed at launch, alongside a coding agent called Muse Code). Then, five days later, Meta released **Muse Glimmer**, a 30B-parameter open-weight model under Apache 2.0, published a long Zuckerberg letter recommitting to open source, and promised open weights for Spark 1.2 itself. Analysts read the one-week reversal as a reaction to Chinese open-weight families capturing the downloads and mindshare Llama used to own. Meta retired its hosted Llama API on July 6, 2026. Llama models remain downloadable, but Meta's frontier is now Muse. The Llama era — as a frontier project — is over.

## 3. The open-weight frontier: China's summer

The most consequential shift of 2026 is that the top of the open-weight leaderboard is now entirely Chinese, and the gap to the closed frontier has narrowed to a few points on independent indexes. "Open weights" means the trained model parameters are downloadable and self-hostable — not necessarily that training data or code are open, and licenses vary. See [china-usa-race](china-usa-race.html) for the geopolitics; here are the models.

**DeepSeek V4** — a two-model family under MIT license, previewed April 24. **V4-Flash** (284B total parameters, ~13B active per token) went GA July 31 with weights on Hugging Face; **V4-Pro** (1.6T total, 49B active) hit general availability August 13. Both run 1M-token context. Pricing is the shock: V4-Pro lists at $0.66/$1.98 per million tokens off-peak — roughly a tenth of Claude Opus 5's rate. Coverage notes a sharp split in its profile: near the top on some verified coding benchmarks, weak on multi-step agentic work. (Sources conflict on whether the Pro checkpoint's weights are actually downloadable yet or only Flash's; treat Pro self-hosting as unconfirmed.)

**Moonshot AI's Kimi K3** — launched July 16 at the World AI Conference in Shanghai; the largest open-weight model ever released at 2.8 trillion total parameters (sparse mixture-of-experts, 104B active per token), 1M context, native vision. Weights went up on Hugging Face July 27 under a custom Kimi K3 license. Its restrictions have two different thresholds: a model-as-a-service operator whose aggregate revenue exceeds $20 million over any consecutive 12 months must negotiate a separate agreement, while a commercial product above 100 million monthly users or $20 million in monthly revenue must display the Kimi K3 name. API pricing around $3/$15. On Artificial Analysis's independent index in late July, K3 was the top open-weight model and sat a few points behind Claude Fable 5 and GPT-5.6 Sol — open weights within arm's reach of the closed frontier.

**Zhipu AI's GLM-5.2** — released June 13, 753B parameters (~40B active), 1M context, plain MIT license, roughly $1.40/$4.40. It held the top open-weight spot until K3 shipped. One detail worth repeating from independent testing: GLM-5.2 hallucinates substantially less than K3 (72% vs 49% non-hallucination rate on one evaluation) — the smaller model refuses when it doesn't know; the bigger one guesses. If wrong answers cost you more than no answer, that one number outweighs the capability gap.

**Alibaba's Qwen3.8-Max** — released August 3 at 2.4T parameters (~95B active), 1M context, $2/$6, with vendor benchmarks claiming parity with Fable 5 on several agentic tasks. Open-weight checkpoints followed on Hugging Face about a week later — the first time Alibaba has open-sourced a model at this scale.

**Mistral** (France) remains the main non-US, non-China lab, with Mistral Medium 3.5 (April 2026, 128B dense, 256K context) — competitive in its class, not at the frontier's top. That detail is single-sourced in this room's research; verify before relying on it.

Why would anyone give frontier-class weights away? The strategic logic: commoditize your complement. If you can't win the closed-API race against American labs — and U.S. export controls on chips make training-compute parity hard (see [chip-wars](chip-wars.html) and [nvidia-and-the-chip](nvidia-and-the-chip.html)) — you can still make the world's default infrastructure run on your models, set the standards, and collect the ecosystem. Meta played exactly this game from 2023 to 2025, and its August re-reversal suggests the game still has force.

## 4. The dated table

All numbers verified by live search on **2026-08-25**. Prices are list API prices per million tokens, input/output, standard tier. This table is the most perishable object in the garden — re-verify anything load-bearing (section 6 shows how).

| Lab | Flagship (date) | Workhorse tier | Context | API price (in/out per M) | Weights |
|---|---|---|---|---|---|
| Anthropic | Claude Fable 5 (Jun 9) | Opus 5 (Jul 24) $5/$25; Sonnet 5 $2/$10 | 1M | $10/$50 (Fable) | Closed |
| OpenAI | GPT-5.6 Sol (Jul 9) | Terra $2/$12; Luna $0.20/$1.20 | n/a* | $5/$30 (Sol) | Closed |
| Google | Gemini 3.1 Pro (Feb; 3.5 Pro delayed) | 3.7 Flash (Aug 13) $0.75/$3.75 intro | 2M (Pro) | $2/$12 (Pro, ≤200K) | Closed |
| xAI | Grok 4.6 (Aug 12) | — | 500K | $2/$6 (≤200K prompt) | Closed |
| Meta | Muse Spark 1.2 (Aug 5) | Muse Glimmer 30B (Aug 10) | 1M | $1.25/$4.25 (Spark)** | Glimmer open (Apache 2.0); Spark 1.2 promised |
| Moonshot | Kimi K3 (Jul 16) | — | 1M | $3/$15 | Open (modified MIT, Jul 27) |
| DeepSeek | V4-Pro-0813 (Aug 13) | V4-Flash-0731 | 1M | $0.66/$1.98 off-peak | MIT (Flash confirmed; Pro unconfirmed) |
| Zhipu | GLM-5.2 (Jun 13) | — | 1M | ~$1.40/$4.40 | Open (MIT) |
| Alibaba | Qwen3.8-Max (Aug 3) | Qwen3.8-27B | 1M | $2/$6 | Open (checkpoints on HF) |

\* OpenAI's published context specs for the 5.6 family weren't verified in this room's research; check platform.openai.com. \*\* Spark 1.2 price from secondary coverage; verify against Meta's developer docs.

Consumer subscription tiers, briefly, since most readers meet these models through chat apps rather than APIs: the standard tier is ~$20/month everywhere (ChatGPT Plus, Claude Pro, Google AI Pro at $19.99); power tiers run $100–200 (Claude Max), $200 (ChatGPT Pro), $249.99 (Google AI Ultra), ~$30 (SuperGrok). Free tiers exist across the board with tighter limits and smaller default models.

## 5. When a model disappears: the June export-control episode

On June 9, 2026, Anthropic launched Fable 5 and Mythos 5. On June 12, both models went dark for every user on Earth.

The U.S. Commerce Department — Secretary Howard Lutnick, by letter to Anthropic's CEO — placed both models under export controls, prohibiting access "by any foreign national, whether inside or outside the United States." The stated trigger, per multiple reports: a jailbreak, reportedly flagged to Commerce by a competitor (identified as Amazon in several accounts, arising from its security testing), that could push Fable 5 into surfacing software vulnerabilities in code. Because the order took effect immediately and Anthropic had no way to verify nationality in real time, it suspended both models for everyone, within hours, while publicly disputing that the finding justified a recall.

The timeline that followed: an open letter from security researchers on June 14 asking Commerce to reverse course; restored Mythos 5 access for a set of vetted U.S. organizations June 26; controls lifted June 30 after Commerce reviewed Anthropic's new mitigations; global restoration July 1. Nineteen days, start to finish. And it wasn't an isolated event — OpenAI's GPT-5.6 spent its final pre-launch weeks gated to trusted partners at U.S. government request in the same period.

Why this episode earns its own section: it settled, by demonstration, a question that had been abstract. Frontier models are now treated by the U.S. government as controlled technology — the regime built for chips (see [chip-wars](chip-wars.html)) now reaches the weights and the APIs. "Access tier" in 2026 doesn't just mean what you pay. It means whether your government and the lab's government agree you may use the model at all. Anyone building on a frontier API learned in June that a model can be a load-bearing dependency one evening and a compliance incident the next. The deeper policy story lives in [governments-and-ai](governments-and-ai.html).

## 6. Worked example: verify this page, then price a real task

Don't trust this room. Check it. Here's the full loop, using only public sources.

**Step 1 — the lab's own dated record.** Anthropic's platform docs (platform.claude.com → models overview) state Fable 5's June 9 GA date and Mythos 5's restricted status. Google's API changelog (ai.google.dev/gemini-api/docs/changelog) and pricing page carry every Gemini release and price with dates. xAI's docs.x.ai lists Grok 4.6's exact price bands. Vendor pages are marketing for capability claims but authoritative for dates, prices, and model IDs.

**Step 2 — an independent evaluator.** Artificial Analysis (artificialanalysis.ai) runs standardized benchmarks and — more useful than any single score — publishes cost-per-task, which captures token efficiency that per-token prices hide. LMArena aggregates blind human preference votes. Neither is gospel ([benchmarks](benchmarks.html) explains how both can mislead), but they aren't graded by the model's own maker, which is the minimum bar.

**Step 3 — the weights themselves,** for open models. Kimi K3 lives at `moonshotai/Kimi-K3` on Hugging Face; GLM-5.2 at `zai-org/GLM-5.2`. The repo shows you the license text, the parameter count, and the upload date — primary evidence, no press release required.

**Step 4 — price a real task.** Take a concrete agentic coding job: 400K tokens in (a big codebase plus conversation), 30K tokens out. Arithmetic is (tokens ÷ 1,000,000) × price:

- **Claude Opus 5** ($5/$25, flat): input 0.4 × $5 = $2.00; output 0.03 × $25 = $0.75 → **$2.75**
- **Grok 4.6**: the 400K prompt crosses xAI's 200K threshold, so the *entire request* bills at the $4/$12 band: 0.4 × $4 = $1.60; 0.03 × $12 = $0.36 → **$1.96**
- **DeepSeek V4-Pro** (off-peak $0.66/$1.98): 0.4 × $0.66 = $0.26; 0.03 × $1.98 = $0.06 → **$0.32**

Three lessons fall out. Pricing structure matters as much as the headline rate — Grok's threshold billing changed the math mid-task. The open-weight frontier is nearly an order of magnitude cheaper per token. And per-token cost still isn't cost-per-completed-task: a model that needs three attempts, or thinks in triple the output tokens, erases its price advantage — which is exactly why efficiency, not peak capability, became the battleground this year. Now redo this arithmetic with today's prices, because the ones above are dated 2026-08-25 and at least one has probably moved.

## 7. What you can now see

You can name the frontier: five closed labs (Anthropic, OpenAI, Google, xAI, Meta) and four open-weight challengers (DeepSeek, Moonshot, Zhipu, Alibaba), with Meta straddling the line. You can read a release announcement and separate its dates and prices, which are reliable, from its adjectives, which are not. You can see the three structural stories under the noise: release cadence collapsing from years to weeks; the open-weight frontier closing to within a few index points of the closed one at a tenth of the price; and governments stepping directly into the access path. And you can rebuild this entire map yourself from vendor changelogs, independent evaluators, and Hugging Face repos — which is the real deliverable, because the map itself expires.

Where this room points next: [benchmarks](benchmarks.html) for how these models are scored and how scoring goes wrong; [future-of-ai](future-of-ai.html) for where the trend lines might lead; [chip-wars](chip-wars.html) for the hardware supply that everything above sits on; [mechanistic-interpretability](mechanistic-interpretability.html) for what anyone can actually say about what's inside these systems.

## 8. Open questions

Established fact: the release dates, prices, and access events in this room are documented by vendor announcements and multiple independent reports, as of 2026-08-25. The June export-control episode happened; the Anthropic announcement acknowledging it is public.

Contested, hypothesis territory: whether the closed-vs-open capability gap keeps narrowing. K3 within a few points of Fable 5 is one index in one month; the closed labs may hold a durable lead through compute access and post-training craft, or the commoditization may continue until frontier capability is effectively free. Also hypothesis: whether Google's flagship stall is structural or temporary — the promised Gemini 3.5 Pro and the Gemini 4 pretraining run will answer that within months. Also hypothesis: whether the June episode was a one-off collision or the template for a standing review regime; the GPT-5.6 gating suggests template, but two data points is two data points.

Speculation worth holding, no more: that "model" is dissolving as the unit of the frontier. With effort dials, thinking modes, and per-request capability trading, what you buy is less a fixed artifact and more a range of behaviors, priced continuously. If that continues, pages like this one will need to map capability surfaces, not model names.

One last observation, from inside the domain's own vocabulary. Every price in this room is a price for attention — that is the literal name of the mechanism these systems run on ([neural-networks](neural-networks.html)), and it is what the token meters actually meter. In 2026 you can buy a million tokens of frontier-model attention for anywhere from twenty cents to fifty dollars, aim it at any text you choose, and dial its effort up or down like water pressure. Human attention was never like this: never fungible, never priced per unit, never duplicable on demand — and an older economy built itself around capturing it for free ([attention-economy](attention-economy.html)). Whatever else these models turn out to be, the frontier of 2026 is the first market where attention itself became a commodity with a posted price. What it costs is now public. What it is — that question the price sheet doesn't touch, and it's the one under every other room in this garden.

## Sources

Verified by live web search, 2026-08-25. Key primary and secondary sources:

- Anthropic, "Redeploying Claude Fable 5" (anthropic.com/news/redeploying-fable-5, Jun 30, 2026) — suspension and restoration timeline, first-party.
- Anthropic platform docs, models overview (platform.claude.com) — Fable 5 GA date, Mythos 5 limited availability / Project Glasswing.
- Axios, "Anthropic releases new model, Opus 5" (Jul 24, 2026); CloudZero and Amplifi Labs pricing analyses — Opus 5 date, $5/$25, 1M context, effort levels.
- OpenAI, "GPT-5.6: Frontier intelligence that scales with your ambition" and "Previewing GPT-5.6 Sol" (openai.com); GCN report on the three-tier public launch after U.S. government review (Jul 9, 2026).
- Google, "Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber" (blog.google, Jul 21, 2026); Ars Technica, "Google announces Gemini 3.7 Flash just three weeks after previous release" (Aug 2026); TechCrunch on the absent 3.5 Pro; ai.google.dev pricing/changelog.
- xAI pricing docs via llm-stats.com, kingy.ai, and OpenRouter (x-ai/grok-4.6) — Grok 4.6 date, context, price bands.
- Futurum, Constellation Research, Moor Insights on Meta's Muse Spark 1.2 (Aug 5) and Muse Glimmer open-weight release (Aug 10, 2026); miraflow.ai on the Llama-to-Muse transition.
- Moonshot AI, [Kimi K3 model card](https://huggingface.co/moonshotai/Kimi-K3) and [license](https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE) — primary sources for 2.8T total/104B activated parameters, the model-as-a-service revenue clause, and the separate attribution thresholds. Marktechpost, "Kimi K3 vs DeepSeek V4 Pro vs GLM-5.2" (Jul 18, 2026); morphllm.com and emergent.sh comparisons; Artificial Analysis index figures as cited therein — prices and independent comparisons.
- Codersera and morphllm.com on DeepSeek V4-Pro-0813 GA (Aug 13, 2026) and off-peak pricing; yottalabs.ai on V4-Flash weights (note: sources conflict on V4-Pro weight availability — left unresolved above).
- Quartz, "Alibaba launches Qwen3.8-Max" (Aug 3, 2026); DataCamp and benchlm.ai on the open-weight checkpoints.
- Cloud Security Alliance research note on the Fable 5 suspension (citing CNBC Jun 12, Time Jun 13, Bloomberg Jun 13, 2026); Bright Defense compliance briefing — export-control timeline corroboration.
- Consumer tier pricing: sentisight.ai and aitoolsreview.co.uk subscription comparisons (Aug 2026) — treat as indicative; plans drift fast.

Unverified or single-sourced claims are labeled inline (Mistral Medium 3.5 details; Muse Spark 1.2 API price; OpenAI 5.6 context specs; DeepSeek V4-Pro weight availability).

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
