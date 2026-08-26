---
title: "The Chip Wars: TSMC, ASML, Japan, and the Competing Field"
slug: chip-wars
series: foundations
tags: semiconductors, tsmc, asml, rapidus, euv, export-controls, geopolitics, foundry
summary: Who can actually manufacture the most advanced chips in 2026, and why the answer is three companies, one machine, and a handful of buildings. A verified map of the leading edge — TSMC, ASML, Intel, Samsung, Japan's Rapidus bet, and the export-control war with China — with every market claim dated.
status: draft
date: 2026-08-25
terms_defined: foundry, process-node, euv-lithography, leading-edge, export-controls
terms_linked: semiconductors, nvidia-and-the-chip, taiwan, china-usa-race, governments-and-ai, future-of-ai, attention-economy, neural-networks
---

# The Chip Wars: TSMC, ASML, Japan, and the Competing Field

If you've read [semiconductors](semiconductors.html), you know what a transistor is and how billions of them end up on a fingernail of silicon. If you've read [nvidia-and-the-chip](nvidia-and-the-chip.html), you know who designs the chips that train AI models. This room is about the layer under both: who can physically *make* those chips, with what machines, in which countries — and why governments now treat that question as a matter of national survival. Everything here is stated as of August 2026, and dated, because this field moves fast enough that undated claims rot within a year.

## 1. The map, before the details

Start with the brutal summary, because everything else in this room is an explanation of it.

As of 2026, exactly **three companies** in the world can mass-produce logic chips at the leading edge — the newest, densest generation of manufacturing, currently the "2-nanometer class":

- **TSMC** (Taiwan Semiconductor Manufacturing Company), in Taiwan. It began volume production of its 2nm-class "N2" process in the fourth quarter of 2025 and held roughly **72–73% of the entire global foundry market in Q1 2026** (TrendForce says 72.3%, Counterpoint 73% — different methodologies, same picture).
- **Samsung**, in South Korea. Its 2nm process reportedly climbed from ~20% yield in late 2025 to over 60% at its peak in Q1 2026 — the rough threshold its own analysts treat as commercially viable.
- **Intel**, in the United States. Its 18A process (2nm-class) entered mass production at Fab 52 in Chandler, Arizona, with the first "Panther Lake" laptop chips shipping around January 2026.

And exactly **one company** builds the machine all three depend on: **ASML**, in Veldhoven, the Netherlands — the sole maker of extreme ultraviolet lithography systems, without which no 2nm-class chip gets printed at commercial scale.

That is the whole geometry of the chip wars. A technology the entire world's economy runs on, funneled through three manufacturers and one toolmaker, concentrated in Taiwan, Korea, Arizona, and one Dutch town. Every export control, every subsidy program, and every fab groundbreaking you read about is a move on this small board.

Two terms before we go deeper. A **foundry** is a factory business that manufactures chips designed by other companies — TSMC makes Apple's and Nvidia's chips but designs none of its own products; that split between design and manufacturing is the industry's defining structure. A **process node** (like "2nm," "N2," "18A") is a named generation of manufacturing technology. The number long ago stopped measuring any physical feature on the chip — it is a marketing label for a density-and-performance generation, which is why the worked example below teaches you to read node names skeptically.

## 2. TSMC: what winning looks like

The numbers first, because they're the argument.

TSMC's N2 process — its first using **gate-all-around (GAA)** transistors, where the gate wraps entirely around the current channel for better control at tiny sizes — entered high-volume manufacturing in Q4 2025 at Fab 20 (Baoshan) and Fab 22 (Kaohsiung), both in Taiwan. Reported early yields were around 70%, which for a brand-new node is remarkable. All 2026 N2 capacity at those fabs was booked before the year began, with Apple reportedly taking more than half of it; the customer list of about 15 includes Qualcomm, MediaTek, AMD, and Nvidia. In the second half of 2026, TSMC plans N2P (an enhanced N2) and A16, which adds backside power delivery — routing power through the wafer's back so signal wiring on the front gets more room — aimed squarely at AI and high-performance computing.

Now the geographic story, because that's where the geopolitics lives:

- **Arizona.** TSMC's first Arizona fab has been in volume production on N4 (4nm-class) since Q4 2024. The second fab, for 3nm, begins equipment installation in Q3 2026 with production targeted for 2027 — ahead of the original schedule. In July 2026, TSMC announced another $100 billion for four additional fabs at 2nm or beyond, bringing its total announced Arizona investment to **$265 billion**.
- **Japan.** TSMC's Kumamoto joint venture JASM (with Sony, Denso, and Toyota as minority shareholders) opened its first fab in 2024, making mature-node chips for image sensors and cars. The second Kumamoto fab was upgraded in 2026 from a mature-node plan to a **3nm** plan — 15,000 wafers a month, equipment installation and production targeted around 2028, with some reports suggesting slippage to 2029. When a magnitude-7.1 earthquake hit Kumamoto in July 2026, TSMC confirmed JASM was safe — and the fact that a Japanese earthquake was global chip news tells you how load-bearing these buildings have become.

Notice what the Arizona expansion does *not* change: through at least 2027, every leading-edge TSMC wafer is made in Taiwan. The overseas fabs trail the domestic ones by one to two nodes by design. Taiwan's government and TSMC both understand that the leading edge staying home is [Taiwan](taiwan.html)'s security argument — the so-called silicon shield. Whether that shield deters or attracts conflict is one of the genuinely contested questions of the decade, and it gets its own room.

## 3. ASML: the machine that is the bottleneck

EUV is central to many later leading-edge processes, but 7nm is not a universal boundary. TSMC's original N7 entered volume production in 2018 using **deep-ultraviolet (DUV) multi-patterning**; N7+ in 2019 was its first commercially available process to use **EUV lithography**. SMIC's 7nm-class production makes the same point from the other side of the embargo. EUV prints circuit patterns with 13.5-nanometer light, so close to X-rays that no lens can focus it; the machines use cascaded mirrors polished to atomic-level smoothness and generate the light by hitting molten-tin droplets with a laser tens of thousands of times per second inside a vacuum. ASML is the only company that has made EUV work at production scale. Its nearest lithography competitors, Nikon and Canon of Japan, sell DUV machines and have never shipped an EUV tool.

The current frontier is **High-NA EUV** — a larger-aperture optic that focuses the same light more sharply, for the "angstrom era" nodes beyond 2nm. Verified status as of mid-2026:

- Intel completed acceptance testing of ASML's second-generation High-NA machine, the TWINSCAN EXE:5200B, in late 2025. The tool runs about 175 wafers per hour with 0.7nm overlay accuracy and costs roughly **$350–400 million per machine**. Fewer than a dozen High-NA units exist worldwide.
- In February 2026, ASML reported its High-NA tools had processed over 500,000 wafers at roughly 80% uptime — the benchmark that moved High-NA from research toy to production platform.
- In July 2026, Intel shipped its first logic chip made with High-NA EUV, aimed at its 14A node in 2027. Samsung and SK hynix took their first High-NA machines in late 2025; the research consortium imec targets qualification of an EXE:5200 for sub-2nm work in Q4 2026.

Sit with the concentration for a second. The machines that make the machines that make AI possible come from one company, whose critical optics come from one supplier (Zeiss, in Germany), whose light sources come from a subsidiary in San Diego. This is why ASML's export licenses are decided in Washington as much as in The Hague — which brings us to the war part.

## 4. Japan: the country that lost the last chip war and is buying back in

In 1988, Japan made roughly half the world's semiconductors. NEC, Toshiba, and Hitachi dominated memory chips so thoroughly that the US forced the 1986 US–Japan Semiconductor Agreement to cap them. Then Japan lost the logic race, lost memory to Korea, and by the 2020s held around 10% of world production, with no domestic fab anywhere near the leading edge.

But Japan never lost the *materials and equipment* layer, and this is the underappreciated half of the chip wars. Shin-Etsu and SUMCO together supply the majority of the world's silicon wafers. Japanese firms (JSR, Tokyo Ohka, Shin-Etsu) make most of the world's advanced photoresists — the light-sensitive chemicals EUV patterns are printed into. Tokyo Electron dominates the coater-developer machines that apply them. When Japan restricted three chemical exports to South Korea in a 2019 political dispute, Samsung's supply chain shuddered within weeks. Japan can't print a leading-edge chip, but nobody else can print one without Japan.

**Rapidus** is Japan's attempt to buy back the part it lost. The verified shape of the bet, as of August 2026:

- Founded in **November 2022** by eight Japanese companies — Toyota, Sony, NTT, NEC, SoftBank, Denso, Kioxia, and MUFG Bank — with a famously tiny initial private stake (about ¥7.3 billion, under $60 million). The real money is public: Japanese government support has reached **¥2.354 trillion** (roughly $16 billion), including an additional ¥631.5 billion approved for fiscal 2026.
- The plan skips four generations. Japan's most advanced domestic logic was around 40nm; Rapidus is going straight to **2nm gate-all-around**, using a process developed with IBM Research in New York — IBM demonstrated the first 2nm GAA test chips in 2021 and is Rapidus's core technology partner.
- In December 2024, Rapidus installed **Japan's first production EUV machine** (an ASML NXE:3800E) at its IIM-1 fab in Chitose, Hokkaido. The pilot line started in April 2025. By 2026, Rapidus reported prototype 2nm transistors hitting their planned electrical characteristics, and NEDO (the state R&D agency) approved its FY2026 plan, including a chiplet packaging pilot line.
- Target: mass production in the **second half of fiscal 2027**.

Is it working? Honestly: the pilot-line milestones are real and independently reported, and hitting planned device characteristics on a first-of-its-kind line is genuine progress. But a pilot line is not a business. Rapidus has no announced anchor customer remotely comparable to Apple-at-TSMC or Tesla-at-Samsung, and it must reach in five years a yield-learning curve TSMC climbed over decades with the world's largest customer base feeding it. The gap between "we can make working 2nm transistors" and "a customer bets a product line on our yields" is where most national champion fabs have historically died. That's the hypothesis Rapidus exists to test, with $16 billion of public money as the stake.

## 5. The export-control war: what the US is trying, and what China does about it

Since October 2022, the United States has run an explicit policy of denying China the tools and chips at the leading edge. The verified timeline of its sharpest thread — Nvidia's China chips — reads like a seismograph:

- **2022–2024:** US controls block Nvidia's top AI chips from China. Nvidia designs the deliberately weakened H20 to fit under the line. EUV machines were never exportable to China at all — the Dutch government, under US pressure, has blocked them since 2019. Dutch licensing rules extended to advanced DUV machines in 2023.
- **April 2025:** Washington declares even the H20 non-compliant. **July 2025:** the Trump administration reverses course; H20 sales resume. **December 2025:** the president announces Nvidia may sell the far more capable H200 to China. **January 13, 2026:** Commerce codifies it — case-by-case licensing, end-use certification, and a 25% tariff on the chips.
- **The punchline, as of early-to-mid 2026:** Nvidia reported it had *still generated no H200 revenue in China* — Beijing, having spent three years watching US policy whiplash, now discourages its own firms from depending on American chips. Brookings titled its analysis "the US is out of the AI chip market in China." Meanwhile in June 2026 the US clarified its bans reach Chinese firms operating *outside* China, in August 2026 Washington was reported to be pressing the Netherlands to cut off nearly all remaining ASML sales to China, and the proposed MATCH Act would write a DUV ban into law.

And what did the controls actually stop? Here the verified picture cuts both ways:

**What they stopped:** China has no EUV. Without it, SMIC — China's top foundry — makes 7nm-class chips by **DUV multi-patterning**: printing each critical layer two, three, or four times with older machines and stitching the patterns together. It works; SMIC has shipped 7nm since Huawei's Kirin 9000S phone chip in 2023, and reports in 2026 claim 5nm-class output on the same approach. But reported yields run 20–40%, costs are far higher, and SMIC's entire advanced capacity (~45,000 wafers/month at end-2025, heading toward ~60,000 in 2026) is a rounding error against TSMC's scale. SMIC's 5nm has slipped repeatedly.

**What they leaked:** TechInsights' teardowns found that essentially every Huawei Ascend 910B/910C AI accelerator they examined contained dies made by *TSMC* — roughly 2.9 million 7nm dies obtained through an intermediary, Sophgo, before the loophole closed. High-bandwidth memory, not logic, is now widely assessed as Huawei's tightest bottleneck. Export controls in this field are not a wall; they are a tax on the adversary's time and a subsidy to its domestic substitutes, and reasonable analysts disagree about which effect dominates. The larger strategic contest is [china-usa-race](china-usa-race.html)'s room; the policy machinery is [governments-and-ai](governments-and-ai.html)'s.

## 6. The scoreboard

Who can make what, at the leading edge, as of August 2026:

| | Most advanced node in volume production | Where | EUV access | High-NA EUV | Anchor customers | Verified status note |
|---|---|---|---|---|---|---|
| **TSMC** | N2 (2nm, GAA) — HVM since Q4 2025 | Taiwan (Baoshan, Kaohsiung) | Yes, largest fleet | Evaluating; not production-committed | Apple, Nvidia, AMD, Qualcomm, MediaTek | ~72–73% of foundry market Q1 2026; ~70% early N2 yields reported |
| **Samsung** | SF2 (2nm, GAA) | Korea (Hwaseong/Pyeongtaek); Taylor, TX from ~2027 | Yes | First tools delivered late 2025 | Tesla ($16.5B AI5/AI6 deal, July 2025) | Yields ~20% late 2025 → 60%+ peak Q1 2026; Taylor volume production expected 2H 2027 |
| **Intel** | 18A (2nm-class, GAA + backside power) | Arizona (Fab 52), Oregon | Yes | First mover — EXE:5200B accepted late 2025; first High-NA logic chip July 2026 | Mostly itself (Panther Lake, Clearwater Forest); 14A pitched to external customers | 18A in mass production as of early 2026 |
| **Rapidus** | 2nm pilot line (GAA, with IBM) | Chitose, Hokkaido | Yes — Japan's first EUV, installed Dec 2024 | No | None announced | Prototypes meeting planned electricals 2026; mass production target 2H FY2027 |
| **SMIC** | 7nm-class in volume; 5nm-class reported | China (Shanghai) | **No — embargoed** | No | Huawei | DUV multi-patterning; reported 20–40% yields; ~45–60k wafers/month advanced capacity |

Read the last column twice. Between "pilot line" and "volume production," and between "reported" and "verified by teardown," is where most chip-war journalism goes wrong.

## 7. Worked example: how to read a node name — and check it yourself

Here's a skill you can use on every chip headline you'll ever read. Take three names from the table: TSMC **N2**, Intel **18A**, Samsung **SF2**.

**Step 1 — strip the number of physical meaning.** "18A" suggests 18 angstroms — 1.8nm — which would make Intel's node sound smaller than TSMC's 2nm. No physical feature on either chip is 2nm or 1.8nm wide. The finest metal pitches on these chips are in the ~20–45nm range. The names are generation labels, chosen by marketing within loose density conventions. Rule: a smaller node number tells you the *intended generation*, never the measured geometry.

**Step 2 — ask what actually changed.** Real node transitions are architecture changes, and 2026 is a genuine one: all three leaders moved from FinFET transistors (gate on three sides of a fin) to **gate-all-around** (gate wrapped fully around stacked nanosheets). Intel's 18A adds backside power delivery now; TSMC holds it for A16 in late 2026. Those are the checkable engineering facts under the labels.

**Step 3 — verify with sources that measure, not announce.** You don't have to trust press releases, and you shouldn't. The verification chain any reader can follow:
1. **Company earnings-call transcripts** (TSMC's quarterly calls state which nodes are in HVM and what revenue share they carry — a legal-liability document, far more reliable than a keynote).
2. **TechInsights teardowns** — they buy shipping products, delayer the chips, and publish measured pitches and die photos. This is how the world learned SMIC's 7nm was real in 2023 and how the Huawei/TSMC die scandal surfaced in 2024–25.
3. **TrendForce / Counterpoint** quarterly foundry-share data for the market claims.
4. **ASML's annual report** for the lithography install base — it states plainly how many EUV systems shipped and to which regions.

Run any chip claim through those four and you'll be better informed than most of the coverage. Step 3 is this whole garden's method in miniature: prefer instruments that measure over voices that announce.

## 8. What you can now see

You can now read a chip-war headline and place it on the board: which of the three manufacturers it touches, whether it concerns the one toolmaker, whether a "breakthrough" is a pilot line or measured volume production, and whether a node number is engineering or marketing. You know why Taiwan's fabs are a security question, why a Dutch export license is an instrument of US policy, why Japan is spending $16 billion to skip four generations, and why China's response to embargo has been multi-patterned persistence plus die-smuggling rather than collapse.

From here: [semiconductors](semiconductors.html) goes under this room, into how a transistor actually works. [nvidia-and-the-chip](nvidia-and-the-chip.html) sits above it, where the manufactured wafers become AI accelerators. [taiwan](taiwan.html) and [china-usa-race](china-usa-race.html) take the two geopolitical threads this room only opened.

## 9. Open questions

**Established (FACT):** The three-manufacturer, one-toolmaker structure of the leading edge as of 2026. TSMC N2 volume production since Q4 2025; Intel 18A mass production; Samsung 2nm yield recovery to ~60% peak in Q1 2026. Rapidus pilot line running with Japan's first EUV; mass production not yet begun. China has no EUV; SMIC ships 7nm-class via DUV multi-patterning at low yields. The 2025–26 US policy reversals on Nvidia's China chips happened as dated above.

**Contested (HYPOTHESIS):** Whether export controls are net-working — slowing China more than they accelerate its domestic substitution. Whether Rapidus can convert a working pilot line into a customer-bearing business by fiscal 2027; history is against national-champion fabs, but Japan's materials position and the IBM process are real assets. Whether Taiwan's silicon shield stabilizes or destabilizes the strait. Whether SMIC's reported 5nm is economically real or a demonstration. Each of these has serious analysts on both sides right now.

**Speculation worth holding (WILD):** That the leading edge consolidates further — to two players, or even one plus a state-backed remnant — as High-NA costs (~$400M per tool, multi-billion-dollar fabs) push everyone else out. That advanced packaging, not lithography, becomes the next chokepoint war. And Rapidus's own executives have mused publicly about fabs on the Moon — filed here so you can see what the field's ambition curve looks like from inside.

---

One more thing, and it comes from the domain itself. Ask what all this capacity is *for*. AI is one of the strongest forces pulling demand for leading-edge logic, memory, packaging, and High-NA machines upward, but it is not the whole market: Apple is the largest named N2 customer here, and advanced chips also serve phones, CPUs, graphics, networking, and workloads with no transformer in sight. AI accelerators devote substantial computation to [attention](attention-economy.html) and other operations inside [neural networks](neural-networks.html); attention is not their entire function. Strip the geopolitics away and part of today's chip war is still nations competing over who owns the substrate on which machine thinking happens. The 1980s fight centered on televisions and memory for spreadsheets. This one includes where — and under whose flag — much of the world's artificial thinking gets done. That is why the stakes feel different this time, and why [china-usa-race](china-usa-race.html) and [future-of-ai](future-of-ai.html) ask the same question at a different altitude.

## Sources

Load-bearing claims verified by live web search, August 2026. Primary and near-primary sources:

- TSMC N2 volume production, fabs, customers, yields: [Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-begins-quietly-volume-production-of-2nm-class-chips-first-gaa-transistor-for-tsmc-claims-up-to-15-percent-improvement-at-iso-power), [DCD on 2nm customers](https://www.datacenterdynamics.com/en/news/tsmc-secures-15-customers-for-its-2nm-technology-majority-in-hpc-space/)
- Foundry market share Q1 2026 (TrendForce 72.3%, Counterpoint 73%): [Counterpoint Research](https://counterpointresearch.com/en/insights/global-semiconductor-foundry-market-share), [Semiecosystem/Mark Lapedus](https://marklapedus.substack.com/p/tsmc-gains-foundry-share-in-q1-26)
- TSMC Arizona timeline and $265B total: [Arizona Commerce Authority, July 2026](https://www.azcommerce.com/news-events/news/2026/7/tsmc-announcement/), [TechPowerUp](https://www.techpowerup.com/344214/tsmc-targets-2027-for-3-nm-production-at-second-arizona-fab)
- TSMC, [7nm technology overview](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_7nm) — original N7 volume production in 2018; N7+ as the first commercially available EUV process in 2019.
- JASM Kumamoto second fab, 3nm upgrade, 2026 earthquake: [TSMC press release](https://pr.tsmc.com/english/news/3105), [The Diplomat, April 2026](https://thediplomat.com/2026/04/tsmcs-kumamoto-fab-upgrade-a-security-driven-reconfiguration-of-indo-pacific-chip-competition/), [TrendForce, July 2026](https://www.trendforce.com/news/2026/07/29/news-7-1-kumamoto-earthquake-tsmc-confirms-jasm-safe-tel-halts-plants-as-chip-supply-chain-assesses-impact/)
- Intel 18A / Panther Lake / Fab 52: [Intel Newsroom](https://newsroom.intel.com/client-computing/intel-unveils-panther-lake-architecture-first-ai-pc-platform-built-on-18a), [Tom's Hardware 18A vs N2](https://www.tomshardware.com/pc-components/cpus/intels-18a-production-starts-before-tsmcs-competing-n2-tech-heres-how-the-two-process-nodes-compare)
- ASML High-NA EXE:5200B, wafer counts, first High-NA logic chip: [TrendForce](https://www.trendforce.com/news/2025/07/17/news-asml-confirms-first-high-na-euv-exe5200-shipment-reportedly-prepping-for-intels-14a-in-2027/), [SiliconANGLE, July 2026](https://siliconangle.com/2026/07/15/intel-starts-using-asmls-high-na-euv-technology-produce-chips/), [imec EXE:5200, TrendForce March 2026](https://www.trendforce.com/news/2026/03/19/news-imec-secures-asmls-most-advanced-exe5200-high-na-euv-for-sub-2nm-4q26-qualification-target/)
- Samsung 2nm yields, Tesla deal, Taylor timeline: [Tom's Hardware fab-roadmap analysis](https://www.tomshardware.com/tech-industry/samsungs-fab-roadmap-examined), [Electrek, July 2026](https://electrek.co/2026/07/13/samsung-taylor-fab-tesla-ai5-chip-2nm/)
- Rapidus: first EUV installation ([Rapidus press release, Dec 2024](https://www.rapidus.inc/en/news_topics/information/rapidus-begins-installation-of-japans-first-euv-lithography-machinery-for-semiconductor-mass-production-en/)), FY2026 NEDO approval and ¥2.354T total support ([Rapidus](https://www.rapidus.inc/en/news_topics/information/nedo-approves-rapidus-fy2026-plan-and-budget-for-2nm-semiconductor-projects/), [TrendForce](https://www.trendforce.com/news/2026/04/13/news-rapidus-reportedly-launches-back-end-prototype-line-japan-adds-%C2%A5631-5b-to-support-2nm-push/)), pilot-line progress ([TechSpot](https://www.techspot.com/news/111959-japan-rapidus-ramps-up-2-nm-chip-plans.html))
- Export controls, H20/H200 timeline, MATCH Act, China market exit: [Congressional Research Service R48642](https://www.congress.gov/crs-product/R48642), [Brookings](https://www.brookings.edu/articles/ball-games-over-the-us-is-out-of-the-ai-chip-market-in-china/), [CNBC, Feb 2026](https://www.cnbc.com/2026/02/26/nvidia-china-chip-sales-export-controls-ai-competition.html), [Al Jazeera, June 2026](https://www.aljazeera.com/economy/2026/6/1/us-says-ban-on-ai-chip-shipments-applies-to-chinese-firms-outside-china), [NL Times, Aug 2026](https://nltimes.nl/2026/08/20/us-preparing-force-netherlands-ban-asml-selling-china)
- SMIC 7nm/5nm, yields, capacity; Huawei/TSMC dies via Sophgo: [SemiAnalysis Ascend ramp](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp), [TechPowerUp on SMIC N+3](https://www.techpowerup.com/344000/chinese-smic-achieves-5-nm-production-on-n-3-node-without-euv-tools)
- Historical claims (Japan's ~50% share in 1988, 1986 US–Japan agreement, Rapidus founding structure, 2019 Japan–Korea export dispute, EUV physics) are standard history not re-verified by live search this session; they are stable, widely documented, and flagged here for honesty.

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
