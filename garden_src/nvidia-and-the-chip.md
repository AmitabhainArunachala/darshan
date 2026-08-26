---
title: NVIDIA and the Future of the Computer Chip
slug: nvidia-and-the-chip
series: foundations
tags: nvidia, gpu, cuda, hardware, datacenter, ai-infrastructure, economics
summary: How a graphics-card company became the most valuable company on Earth, what a GPU actually is, why the CUDA software moat matters more than the silicon, and what the datacenter economics of 2026 say about where computing goes next. Every market number is dated, because this field moves monthly.
status: draft
date: 2026-08-25
terms_defined: gpu, cuda, accelerator, hbm, memory bandwidth, ai accelerator market
terms_linked: neural-networks, deep-learning, linear-algebra-and-ai, machine-learning, compilers, pretraining-post-training, semiconductors, chip-wars, taiwan, china-usa-race, future-of-ai, mechanistic-interpretability
---

# NVIDIA and the Future of the Computer Chip

You're in the foundations wing of the garden. If you've read [neural networks](neural-networks.html) and [deep learning](deep-learning.html), you know what modern AI computes: enormous piles of matrix multiplication. This room is about the machine that does the multiplying — who builds it, why one company controls most of it, and what the money and power flows of 2026 tell us. Two sibling rooms, [chip wars](chip-wars.html) and [semiconductors](semiconductors.html), cover the geopolitics and the physics; this one covers the company and the economics.

One warning before we start. This is the fastest-moving part of the whole garden. Every market number below carries a date, and you should trust the date more than the number. Where I write "as of August 2026," assume the figure has moved by the time you read this — the point is the shape, not the decimal.

## 1. The accident: a games company stumbles into the substrate of AI

Start with the concrete fact, because it's almost absurd. As of late August 2026, NVIDIA is the most valuable company in the world, with a market capitalization of about $5.2 trillion. In its most recent fully reported quarter — the three months ending April 26, 2026 — it took in $81.6 billion in revenue, up 85% from a year earlier, and $75.2 billion of that came from datacenters. Not gaming. Datacenters. The gaming company is now a rounding error inside itself.

None of this was the plan. NVIDIA was founded in 1993 by Jensen Huang, Chris Malachowsky, and Curtis Priem to make chips for 3D video games. In 1999 it shipped the GeForce 256 and marketed it as the world's first "GPU" — graphics processing unit. A GPU is a chip built around one observation: drawing a 3D scene means doing the same small calculation on millions of pixels at once, and none of those calculations depend on each other. So instead of one very fast processor working through a list, you build thousands of simple processors working in parallel.

Here's the accident. That's also exactly what a neural network needs. Training and running a network is, at bottom, multiplying big grids of numbers — see [linear algebra and AI](linear-algebra-and-ai.html) — and matrix multiplication is embarrassingly parallel in the same way pixels are. NVIDIA spent fifteen years perfecting a machine for rendering dragons, and it turned out to be the machine for building minds' closest artificial cousins. The dragon-rendering was the pretraining, if you like. The real workload showed up later.

## 2. CUDA: the moat was poured in 2006, and it's made of software

The silicon is not why NVIDIA is hard to displace. The software is.

In November 2006, NVIDIA announced CUDA — Compute Unified Device Architecture — alongside its G80 chip, and shipped the first SDK in June 2007. CUDA let a programmer write ordinary C code that runs on the GPU, instead of tricking the graphics pipeline into doing math by disguising computations as pretend triangles and textures, which is genuinely what researchers did before. At the time this looked like a strange indulgence: NVIDIA was spending die area and engineering budget making its gaming chips programmable for scientists, a market that barely existed. Wall Street mostly hated it.

The payoff took six years to arrive. In 2012, Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton trained AlexNet — a convolutional neural network — on two consumer GTX 580 gaming cards using CUDA, and won the ImageNet image-recognition competition by a margin so large the field initially suspected an error. That result lit the fuse on the entire [deep learning](deep-learning.html) era, and it happened on NVIDIA hardware because NVIDIA was the only company that had spent years making its hardware programmable for exactly this kind of outsider.

What does CUDA code look like? Here's the flavor — a kernel that adds two arrays, with every element computed by its own thread:

```c
__global__ void add(float *a, float *b, float *c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) c[i] = a[i] + b[i];
}
```

That `__global__` marker and that thread-index arithmetic are the whole cultural artifact: you write the computation for *one* element, and the hardware runs it hundreds of thousands of times at once. If you want to feel this yourself, a free Google Colab notebook gives you an NVIDIA GPU and `nvcc`, the CUDA compiler (see [compilers](compilers.html)) — you can compile and run that kernel in ten minutes.

The moat is everything stacked on top of that. Twenty years of libraries: cuDNN for neural network layers, cuBLAS for linear algebra, NCCL for making thousands of GPUs talk to each other, TensorRT for inference. PyTorch and TensorFlow were built CUDA-first. Millions of developers have CUDA muscle memory; nearly every [machine learning](machine-learning.html) paper's code assumes it. A competitor doesn't just have to build a comparable chip — AMD arguably has — it has to make twenty years of ecosystem, tooling, and habit not matter. That's why the moat is called CUDA and not Blackwell.

## 3. What the chip actually is, and what actually limits it

Strip away the branding and a modern AI accelerator — the general term for any chip specialized for neural network math — is two things bolted together: an enormous array of small multiply-accumulate units, and a stack of very fast memory sitting millimeters away.

The second part matters more than most people think. The memory is HBM — high-bandwidth memory, DRAM dies stacked vertically and connected to the processor through thousands of parallel wires. The reason is that large models are usually **memory-bound, not compute-bound**: the arithmetic units can multiply faster than the memory can feed them numbers. When you run a large language model, most of the time goes to streaming billions of weights from memory into the compute units for every single token generated. So the number that increasingly decides real performance isn't FLOPS (floating-point operations per second) but memory bandwidth — bytes per second from memory to compute. NVIDIA's next-generation Rubin GPU quotes 22 terabytes per second. Your laptop manages maybe 0.1% of that.

Here's the landscape of chip types, because the terms come up constantly:

| | CPU | GPU (NVIDIA/AMD) | TPU-class ASIC (Google, Amazon…) | Wafer/novel (e.g. Cerebras) |
|---|---|---|---|---|
| **Built for** | Anything; branching logic | Massively parallel math, programmable | One workload: tensor math, fixed patterns | Extreme single-chip scale |
| **Cores** | Tens, complex | Tens of thousands, simple | Few huge matrix engines | Hundreds of thousands on one wafer |
| **Flexibility** | Maximum | High (CUDA/ROCm) | Low — compiler targets it, you mostly don't | Low |
| **Who buys it** | Everyone | Everyone in AI | Mostly its own maker's cloud | Niche |
| **Economics** | Commodity | ~70%+ gross margins (NVIDIA) | Cheaper per token *if* you fill it | Unproven at scale |

The strategic split hiding in that table: GPUs are general and programmable, which is why every new model architecture debuts on them. ASICs (application-specific integrated circuits) are cheaper per unit of work but frozen — they bet that the workload won't change shape. As long as AI research keeps changing shape, the general chip keeps winning the frontier. If architectures ossify, the ASICs close in. Hold that thought; it's the hinge of section 6.

One more structural fact: NVIDIA doesn't manufacture anything. It designs chips; TSMC in Taiwan fabricates them; SK Hynix, Samsung, and Micron supply the HBM; TSMC's advanced packaging bonds them together. The most valuable company on Earth is a design-and-software firm whose physical existence is subcontracted — mostly to one island. The [semiconductors](semiconductors.html) room covers how fabrication works; [Taiwan](taiwan.html) covers why that concentration keeps strategists awake.

## 4. The numbers of 2026, dated and sourced

Now the economics, with dates attached.

**NVIDIA's income.** Fiscal Q1 2027 (quarter ended April 26, 2026): $81.6B revenue, $75.2B from datacenter, up 92% year over year, with gross margins around 75%. Guidance for the following quarter was roughly $91B; the report lands August 26, 2026 — the day after this room was written, which tells you how perishable this paragraph is. For scale: the whole company's revenue in fiscal 2016, a decade ago, was about $5B a *year*. It now does that in about five days.

**Where the money comes from.** Four buyers dominate. Microsoft, Alphabet, Amazon, and Meta have guided to a combined ~$725 billion of capital expenditure for 2026 — Amazon ~$220B, Alphabet ~$195–205B, Microsoft ~$190B, Meta ~$130–145B — up roughly 77% from about $410B in 2025, per their own earnings guidance as of early 2026. A very large slice of that flows through datacenter construction into accelerators, and analyst estimates as of mid-2026 put NVIDIA's share of the AI accelerator market at roughly 80–88% by revenue. Those percentages are estimates, not filings; treat them as a range.

**The strange loop in the financing.** In September 2025, NVIDIA and OpenAI signed a letter of intent: OpenAI deploys at least 10 gigawatts of NVIDIA systems, and NVIDIA invests up to $100 billion in OpenAI, tranche by tranche as each gigawatt comes online, with the first gigawatt on the new Vera Rubin platform in the second half of 2026. Read that twice: the chip vendor invests in its customer, who uses the money to buy the vendor's chips. Similar circular structures — vendor financing, cloud credits, equity-for-compute — thread through the whole 2026 buildout. Bulls call it ecosystem building. Bears call it the classic late-cycle pattern of a capex boom. Both descriptions are of the same transactions; which one is *true* is a hypothesis the next few years will grade.

## 5. Worked example: what a gigawatt of AI actually buys

Datacenter deals are now quoted in gigawatts, which is odd if you think about it — measuring computers by their electricity. Let's do the arithmetic once so the unit means something. Every assumption is stated; check my numbers with a calculator, that's the point.

**Step 1 — from grid to chips.** A "1 GW" campus means roughly 1 gigawatt of power draw. Cooling and power conversion overhead eats a slice; with a good power-usage-effectiveness around 1.25, about **800 MW** reaches the racks.

**Step 2 — from racks to GPUs.** NVIDIA's flagship rack of the Blackwell generation, the GB200/GB300 NVL72, holds 72 GPUs and draws about 130 kW (public figures cluster between 120 and 140 kW; take 130). So: 800 MW ÷ 130 kW ≈ **6,100 racks** ≈ **440,000 GPUs**.

**Step 3 — from GPUs to dollars.** Widely reported street estimates in 2025–26 put such a rack around $3 million (NVIDIA doesn't publish list prices; this is the softest number here). 6,100 × $3M ≈ **$18 billion of hardware** — before the building, the substations, the cooling plant, and the networking, which roughly double the total. Jensen Huang has put the all-in figure at around $50B per gigawatt; our bottom-up estimate is consistent with that order of magnitude.

**Step 4 — the punchline.** OpenAI's letter of intent with NVIDIA alone covers 10 GW — call it a few hundred billion dollars and roughly four and a half million GPUs. And that's one deal, for one lab. Now the 2026 numbers stop being abstract: when four companies guide $725B of capex in one year, they are buying *millions* of accelerators and the gigawatts to feed them. And it explains why the binding constraint has changed. Gartner projected that the incremental electricity needed for AI-optimized servers could reach 500 TWh a year in 2027 and that power shortages could constrain 40% of AI datacenters by then. The IEA's 2026 central outlook puts total datacenter demand at 485 TWh in 2025 and about 950 TWh in 2030. In major US markets, a new grid connection can take over seven years. The scarce input of 2023 was chips. The scarce input of 2026, increasingly, is electricity. Follow that thread in [chip wars](chip-wars.html).

## 6. The siege: everyone is now building chips

A 75% gross margin on the most-wanted product in the world economy is a giant bounty poster. As of 2026 the siege has three armies.

**AMD, the direct rival.** In July 2026, AMD launched Helios: a rack-scale system of 72 Instinct MI455X GPUs — 320 billion transistors each, on TSMC 2nm and 3nm, with 432 GB of memory per GPU — shipping from Q3 2026, with Microsoft announced as a buyer. Behind it stands the October 2025 OpenAI–AMD agreement to deploy 6 gigawatts of AMD GPUs, with first MI450-class deployments in the second half of 2026 — OpenAI deliberately building a second source so no single vendor owns its future. AMD's silicon is now genuinely competitive on paper. Its problem remains section 2: ROCm, its CUDA equivalent, is years behind in ecosystem, and porting the world's code is slower than fabricating the world's chips.

**The hyperscalers' own silicon.** Google has designed its own TPUs since 2015; the seventh generation, Ironwood, unveiled in April 2025, deploys in pods of 9,216 chips. In October 2025 Anthropic announced a plan to expand its Google Cloud TPU use by up to one million chips, with capacity expected online in 2026 for both research and products. That is planned capacity, not a disclosure that one million Ironwoods were already running, and it establishes no single-customer record. Amazon shipped Trainium3, its first 3nm chip, in December 2025 and trains its own models on it. Microsoft has Maia; Meta has MTIA. The pattern: your four biggest customers are all funding alternatives to your chips, especially for stable, predictable workloads where an ASIC can beat a general accelerator (recall the table in section 3). Analyst projections as of 2026 have custom ASIC revenue growing ~45% a year against ~16% for GPUs. Projections, not fate — but the direction is unambiguous.

**China, building under embargo.** US export controls ban NVIDIA's frontier chips from China outright; the diplomacy of 2025–26 produced a lurching series of partial openings — H20 licenses granted, then met with Beijing's cold shoulder; H200 sales approved under tight conditions in 2026 with roughly $10B in licenses issued, yet actual shipments so trivial that Huang told investors in May 2026 to "expect nothing" from the line. The strategic effect cuts both ways: the controls slow China's labs today, and simultaneously hand Huawei and China's domestic chip effort a protected home market and a national mission. Whether that trade was wise is one of the live questions of the decade — the full argument lives in [China, the USA, and the race](china-usa-race.html).

Add it up honestly: nothing on this list has dented the datacenter revenue curve *yet* — 92% year-over-year growth is not what erosion looks like. But every structural force now points the same way: customers diversifying, inference commoditizing, margins painting the bounty. The moat is real and it is being besieged from every direction at once. Both of those are facts.

## 7. What comes after: the roadmap and the real constraints

**The near roadmap is public.** NVIDIA now ships a new architecture every year — a cadence itself designed to exhaust pursuers. Vera Rubin, shipping to major customers in the second half of 2026: a 336-billion-transistor GPU on TSMC 3nm, 288 GB of HBM4 at 22 TB/s, paired with NVIDIA's own Vera CPU — six chips designed as one system, because the unit of design is no longer the chip but the rack. Rubin Ultra follows in 2027 with a rack architecture packing 576 GPU dies and drawing about 600 kW — one rack pulling the power of a small neighborhood — followed by an architecture named Feynman on the public roadmap for 2028. Moore's Law as popularly understood (transistors doubling cheaply every two years) is long dead; what replaced it is scaling by *system*: more dies per package, more packages per rack, more bandwidth between them, at ever more staggering power. The physics underneath is [semiconductors](semiconductors.html)' territory.

**The demand question.** All of it rests on one assumption: that the [scaling of training and inference](pretraining-post-training.html) keeps paying — that more compute keeps buying more capability, and more capability keeps buying more revenue. That has held, remarkably, since 2012. It is still a hypothesis, not a law. If it holds, today's buildout looks prescient. If capability gains flatten or the revenue never catches the capex, 2026's $725 billion looks like the fiber glut of 2000 — which, remember, still left behind the infrastructure the internet then grew into. Serious people hold each view; the honest room holds both. See [the future of AI](future-of-ai.html).

**The physical constraints are not hypothetical.** One design-and-software company; one dominant fab on one island; a handful of HBM suppliers; grids that take seven years to deliver a connection. Every one of those is a single point of failure threading through the most capitalized industrial buildout in history. The chip is no longer just a component. It is the choke point where software, energy, manufacturing, and statecraft all meet — which is why this room sits beside [chip wars](chip-wars.html) rather than beside gadget reviews.

## 8. Conclusion

What you can now see that you couldn't before: why "GPU" and "AI" became near-synonyms (an accident of shared parallelism), why NVIDIA specifically owns the moment (a software moat poured in 2006, six years before anyone knew it was a moat), what actually limits these machines (memory bandwidth and megawatts, not arithmetic), how to convert a headline like "10 gigawatts" into GPUs and dollars yourself, and where the pressure on the incumbent is coming from (customers-turned-competitors, inference ASICs, export politics). You can also now read any 2026 AI-infrastructure headline and ask the two questions that matter: *what's the date on this number,* and *who is financing whom?*

From here: [semiconductors](semiconductors.html) for how the chips are physically made, [chip wars](chip-wars.html) and [Taiwan](taiwan.html) for the geopolitics, [linear algebra and AI](linear-algebra-and-ai.html) for the math the hardware serves, and [pretraining and post-training](pretraining-post-training.html) for the workload driving all of it.

## 9. Open questions

**Established (FACT):** The revenue, capex, and roadmap figures above, as dated and sourced below. NVIDIA's ~80%+ accelerator share as of mid-2026 (analyst estimate range, not a filing). The CUDA ecosystem's two-decade head start. Power availability as a binding constraint on new datacenter capacity in major markets.

**Contested (HYPOTHESIS):** That AI capability and revenue will keep scaling with compute well enough to justify ~$725B/year of capex — the entire buildout is a leveraged bet on this. That the circular vendor-financing structures are sustainable ecosystem-building rather than a late-cycle warning sign. That CUDA's moat survives the shift of workload from training (where flexibility wins) to inference (where ASICs win) — Anthropic's plan for up to one million Google TPUs is evidence that the moat faces pressure, not proof it has failed. That export controls slow China more than they accelerate its domestic industry.

**Speculation worth holding (WILD):** That the unit of computing continues to inflate — chip, to rack, to building, to gigawatt campus — until the meaningful "computer" is a power plant with silicon attached, and computing economics simply *becomes* energy economics. That a post-transformer architecture arrives that rewards different silicon entirely, repricing every moat in this room overnight. Nobody knows. Anyone who says they know is selling something — quite possibly a chip.

A last thought, from inside the domain's own logic. A chip is frozen commitment: years before software runs, its designers must bet on what computation will *be*. For decades the bet was logic — branching, deciding, one step after another — and the CPU embodied it. The machines described in this room embody a different bet: that what intelligence mostly needs is attention — in the transformer's literal, technical sense, every token attending to every other, paid for in memory bandwidth and megawatts. The market has priced that bet at five trillion dollars. Whether attention of that kind is most of what a mind does, or just the part we've learned to build, is not a question silicon can settle — but it is now, concretely, a question you can read in silicon. The garden's [instrument wing](mechanistic-interpretability.html) takes it up from the inside.

## Sources

Key claims verified by live web search, August 25, 2026:

- NVIDIA Q1 FY2027 results ($81.6B revenue; $75.2B datacenter, +92% YoY; quarter ended April 26, 2026): [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027); [CNBC](https://www.cnbc.com/2026/05/20/nvidia-nvda-earnings-report-q1-2027.html). Q2 FY27 guidance ~$91B, report due Aug 26, 2026: [REX Shares earnings preview](https://www.rexshares.com/nvidia-earnings/). Gross margin ~75% (analyst estimate): [Futurum](https://futurumgroup.com/insights/nvidia-q1-fy2027-data-center-diversification-blackwell-scale-cpu-upside/).
- Market cap ~$5.2T, world's most valuable company (Aug 21, 2026): [companiesmarketcap.com](https://companiesmarketcap.com/nvidia/marketcap/); [stockanalysis.com](https://stockanalysis.com/stocks/nvda/market-cap/).
- Hyperscaler 2026 capex ~$725B combined; per-company guidance; ~77% growth over 2025; NVIDIA 80–88% accelerator share (estimates): [Yahoo Finance](https://finance.yahoo.com/sectors/technology/article/meta-microsoft-amazon-and-alphabet-are-about-to-spend-a-shocking-amount-of-money-to-dominate-the-ai-era-115359575.html); [CNBC](https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html); [Futurum](https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/) (note: totals reported range ~$630–725B across sources — hence "approximately").
- CUDA announced Nov 2006, SDK June 2007; AlexNet 2012 on two GTX 580s (Krizhevsky, Sutskever, Hinton): [Jon Peddie Research](https://www.jonpeddie.com/news/part-iii-the-evolution-to-ai-gpus/); [Turing Post](https://www.turingpost.com/p/cvhistory6); [Understanding AI](https://www.understandingai.org/p/why-the-deep-learning-boom-caught).
- Vera Rubin platform (336B transistors, TSMC 3nm, 288GB HBM4, 22 TB/s, H2 2026 ship; Rubin Ultra 2027, ~600kW NVL576 racks): [Wikipedia — Rubin microarchitecture](https://en.wikipedia.org/wiki/Rubin_(microarchitecture)); [The Next Platform](https://www.nextplatform.com/ai/2026/01/06/nvidias-vera-rubin-platform-obsoletes-current-ai-iron-six-months-ahead-of-launch/4092179); [VRLA Tech roadmap](https://vrlatech.com/nvidia-gpu-roadmap-2026-2030/).
- OpenAI–NVIDIA LOI (Sept 22, 2025: ≥10 GW, up to $100B, first GW on Vera Rubin H2 2026): [OpenAI](https://openai.com/index/openai-nvidia-systems-partnership/); [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/openai-and-nvidia-announce-strategic-partnership-to-deploy-10gw-of-nvidia-systems); [CNBC](https://www.cnbc.com/2025/09/22/nvidia-openai-data-center.html).
- AMD Helios launch July 2026 (72× MI455X, 320B transistors, TSMC 2nm/3nm, 432GB, Q3 2026 ship, Microsoft buyer); OpenAI–AMD 6 GW deal (Oct 2025), first MI450 deployments H2 2026: [CNBC](https://www.cnbc.com/2026/07/20/amd-helios-microsoft-ai-nvidia.html); [Data Center Dynamics](https://www.datacenterdynamics.com/en/news/amd-unveils-full-mi400-product-lineup-claims-mi500-chips-will-deliver-1000x-increase-in-ai-performance/); [TechWire Asia](https://techwireasia.com/2026/07/amd-advancing-ai-2026-helios-openai-meta-anthropic/).
- Google Ironwood TPU v7 (pods of 9,216) and Anthropic's plan for up to one million Google TPUs with capacity expected online in 2026: [Anthropic's October 2025 announcement](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services). Amazon Trainium3 (Dec 2025, 3nm) and ASIC ~45%/yr vs GPU ~16%/yr growth remain analyst-reported projections: [Introl](https://introl.com/blog/custom-silicon-inflection-2026-hyperscaler-asics-nvidia-gpu); [Spheron](https://www.spheron.network/blog/hyperscaler-custom-ai-chips-2026-trainium-tpu-maia-mtia-vs-nvidia-gpu/).
- China export status (H20 licenses vs. Beijing pushback; H200 approved under tight controls, shipments "trivial", Huang "expect nothing" May 2026; Blackwell banned): [Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/us-eases-nvidia-export-restrictions-h200-cleared-for-china-under-tight-controls); [Data Center Dynamics](https://www.datacenterdynamics.com/en/news/us-agrees-to-grant-nvidia-h20-export-licenses-as-chipmaker-unveils-new-blackwell-inspired-gpu-for-china/); [CFR](https://www.cfr.org/expert-brief/consequences-exporting-nvidias-h200-chips-china).
- Power constraints: [Gartner's official November 2024 release](https://www.gartner.com/en/newsroom/press-releases/2024-11-12-gartner-predicts-power-shortages-will-restrict-40-percent-of-ai-data-centers-by-20270) projects 500 TWh in 2027 for incremental AI-optimized-server demand and 40% of AI datacenters constrained by power; the [IEA's 2026 outlook](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary) projects total datacenter use rising from 485 TWh in 2025 to about 950 TWh in 2030. Seven-plus-year grid queues: [Brookings](https://www.brookings.edu/articles/global-energy-demands-within-the-ai-regulatory-landscape/).

Unverified-by-search, labeled in text: rack price ~$3M and ~130 kW draw (street estimates, stated as assumptions in section 5); "~$50B per GW" (attributed to Huang's public remarks; treat as order-of-magnitude); NVIDIA founding details and GeForce 256 (well-established history, not re-verified beyond secondary sources above); Feynman-architecture 2028 date (public roadmap, subject to change).

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
