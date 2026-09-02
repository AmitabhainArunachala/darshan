---
title: "Advanced Packaging: The Scaling Frontier"
slug: advanced-packaging
series: silicon
tags: cowos, chiplets, hybrid-bonding, soic, abf, interposer, tsmc, besi, substrates
summary: A scanner can print only about 858 square millimeters in one shot, so large accelerators became chiplets joined in the package. This room follows CoWoS, hybrid bonding, substrates, and the 2023–2025 packaging bottleneck, and shows why stacking is a yield problem before it is a bandwidth answer.
status: draft
date: 2026-09-02
terms_defined: reticle-limit, chiplet, cowos, silicon-interposer, hybrid-bonding, soic, abf-substrate, panel-level-packaging
terms_linked: semiconductors, chip-wars, nvidia-and-the-chip, taiwan, the-memory-wall, the-capital-cycle, bottleneck-migration, reading-the-filings, necessity-and-capture, the-japanese-layer, power-and-cooling, physical-accounting, china-usa-race, what-are-those-rings
---

# Advanced Packaging: The Scaling Frontier

A scanner prints a chip in rectangles. The largest rectangle it can print in one shot is smaller than the accelerator you actually want. That mismatch is why the industry cut the chip into pieces and spent the last decade learning how to join them. This room is the joining layer: the reticle, the chiplet, TSMC's CoWoS family, hybrid bonding, the substrate under the package, and the 2023–2025 bottleneck that decided who captured the value. [The memory wall](the-memory-wall.html) explains why those packages are stuffed with HBM. This room explains why stuffing them was hard.

## 1. The reticle is a box

A **reticle**, or photomask field, is the rectangular area a lithography scanner can expose in one pass. For the extreme-ultraviolet tools that print leading-edge logic, that field is **26 millimeters by 33 millimeters**, about **858 mm²**. The number is a scanner specification, not a foundry slogan. High-NA EUV, the next optical generation, halves the field in one direction, to 26 × 16.5 millimeters, which makes the box smaller still.

A single piece of silicon that large is already a yield problem. Defects land at random. The chance that a die is clean falls exponentially with area; the worked example at the end of this room makes that arithmetic visible. Past the reticle you cannot even print the die as one shot without stitching fields together, which is expensive and alignment-sensitive. So the industry stopped insisting on one die. It cut the function into **chiplets** — smaller dies that can be printed, tested, and then joined — and moved the joining into the package.

That is the physical reason packaging became a scaling frontier. Transistor density still matters; see [semiconductors](semiconductors.html) and [chip wars](chip-wars.html). But once the product you want is several reticles of logic plus several stacks of [high-bandwidth memory](the-memory-wall.html), the product is a package. [Nvidia and the chip](nvidia-and-the-chip.html) designs that package. Someone still has to build it.

## 2. CoWoS: three ways to sit side by side

**CoWoS**, Chip-on-Wafer-on-Substrate, is TSMC's 2.5D packaging family. "2.5D" means the dies sit side by side on a fine-wired layer, not stacked face-to-face. The layer is then mounted on an organic substrate that talks to the board. TSMC has sold the platform since 2012. After generative-AI demand arrived in late 2022, the company said, the demand for CoWoS "has become even greater" (TSMC CoWoS technology page, accessed 2 September 2026).

There are three named variants. The names are TSMC's; the differences are physical.

**CoWoS-S** uses a **silicon interposer**: a thin slice of silicon, wired like a chip, with through-silicon vias to the substrate below. TSMC's page says CoWoS-S can take an interposer up to **3.3× reticle**, about **2,700 mm²**. The silicon gives the densest lateral wiring and a place to embed deep-trench capacitors. It also inherits silicon's problems: the interposer itself is a large die, often stitched across several reticle fields, with a yield and a warpage of its own.

**CoWoS-R** replaces that silicon sheet with a **redistribution-layer interposer** — copper traces in polymer. TSMC says it has been in volume production since 2023, with a minimum 4-micrometer pitch (2-micrometer line and space). The organic layer is more flexible, which helps the solder joints that attach the module to the substrate. Density is lower than silicon. Area can be larger.

**CoWoS-L** is the hybrid. Small silicon bridges, which TSMC calls local silicon interconnects or LSI, sit where you need silicon-density wiring; an RDL interposer carries power and the rest. TSMC says the first CoWoS-L at 3.5× reticle entered volume production in 2024, and that larger interposers using the same idea are the path past 3.3×. A 2024 TSMC OIP presentation, reported by Tom's Hardware on 27 November 2024, put a 5.5×-reticle package with up to twelve HBM4 stacks on a 2025–2026 path and a 9×-class "super carrier" on a 2027 qualification path. In April 2026, C.C. Wei told the first-quarter call that TSMC had "a very large reticle size CoWoS" in the market, was working on **CoPoS** (chip-on-panel-on-substrate), and had "a pilot line right now and expect production a couple of years later." "Today the main supply is still a large-sized CoWoS."

Intel's answer to a full silicon interposer is **EMIB**, a silicon bridge embedded in the organic substrate, and **Foveros** for face-to-face stacks. Samsung has I-Cube. Those are real platforms. They were not the binding constraint on NVIDIA-class accelerators in 2023–2025. CoWoS was.

IEEE's Heterogeneous Integration Roadmap (HIR), hosted by the Electronics Packaging Society at eps.ieee.org/hir, is the industry's shared nomenclature document for these constructions. Chapter 22 of the 2021 edition distinguishes 2D organic (2DO) from 2D silicon/glass (2DS) and 3D stacks, and publishes a pitch roadmap. It is a pre-competitive forecast, not a shipment ledger. Use it for vocabulary. Use TSMC's pages and filings for what actually shipped.

## 3. Hybrid bonding, SoIC, and Besi's clock

**Hybrid bonding** joins two dies (or a die and a wafer) by copper-to-copper pads set in a dielectric, without a solder bump. The pitch can drop below ten micrometers; TSMC's SoIC page says the bond pitch "starts from the sub-10 µm rule." Shorter, denser connections mean more bandwidth at less energy than a micro-bump. They also mean a tool that can place a die to tens of nanometers, a surface clean enough to bond, and a stack that survives the heat of the rest of the package.

**SoIC**, System on Integrated Chips, is TSMC's wafer-level 3D stacking service built on that idea. TSMC's 2025 annual report says 3-nanometer SoIC stacking "successfully entered volume production in 2025." The SoIC technology page repeats it. SoIC-X covers chip-on-wafer and wafer-on-wafer. The stacked chip can then go into CoWoS or into TSMC's wafer-scale SoW. That is 3D on top of 2.5D, not a replacement for it.

The tool story is where expectations and outcomes parted. **BE Semiconductor Industries (Besi)**, in the Netherlands, makes die attachers, including the hybrid bonders that pair with Applied Materials' surface-preparation tools as the Kinex platform. Applied holds a minority stake in Besi, about 9% in 2026 reporting. The two companies have run a joint lab in Singapore.

Date the clock:

- **24 October 2024.** Reuters reported that Besi's third-quarter orders missed estimates, and that an unidentified customer delayed taking delivery of hybrid-bonding systems due in the fourth quarter. Besi still said it expected a sharp rise in demand in 2025.
- **21 November 2025.** At SEMICON Europa, Applied and Besi presented Kinex as a high-volume-ready die-to-wafer platform. An Applied speaker, cited by EE Times, said "this is not a mature technology yet" and also that some products had been running in high volume for two or three years.
- **23 April 2026.** Besi reported first-quarter orders of **€269.7 million** and revenue of **€184.9 million**. Hybrid-bonding unit orders exceeded the previous peak; the company said adoption had reached twenty customers. CEO Richard Blickman said memory customers were evaluating to a common end-customer spec, with volume implications for 2027.
- **6 July 2026.** The Wall Street Journal reported Besi shares down 6.7% after a report that Samsung and SK hynix were questioning the need to adopt Besi's hybrid bonding for their most advanced stacks.
- **August 2026.** At Hot Chips, SK hynix's Jaesik Lee said a JEDEC stack-height change, from 720 to 775 micrometers, reduced the near-term need to thin dies further, and that hybrid bonding in HBM was effectively pushed to HBM5, with micro-bumps remaining through HBM4E (Bits & Chips, 26 August 2026). Twelve-high HBM was in mass production; sixteen-high was in customer qualification.

The honest summary is not "hybrid bonding failed" and not "hybrid bonding took over." Logic stacking at TSMC (SoIC) is in volume. HBM hybrid bonding was repeatedly expected earlier than the memory makers were willing to put it into a revenue stack. Besi's order book in 2026 showed real demand and a clock that still slipped. Anyone who treated a 2024 "surge in 2025" sentence as a shipment forecast learned the difference between a tool order and a qualified stack.

## 4. The board under the package: ABF, glass, panels

Under the interposer sits an organic **substrate**, a many-layer board that fans the package out to solder balls. The insulating film in the high-end version is **Ajinomoto Build-up Film**, or **ABF**, a dielectric from Ajinomoto Fine-Techno. Yole Group, in a 26 February 2026 note, called the 2021 ABF shortage "a harsh lesson on how a single material can paralyze an entire supply chain" and treated Ajinomoto's position as a near-monopoly in that film. Substrate fabrication is a short list: **Ibiden** and **Shinko** in Japan, **Unimicron**, **Kinsus**, and **Nan Ya PCB** in Taiwan, plus AT&S. [The Japanese layer](the-japanese-layer.html) is where Ibiden and Ajinomoto belong as materials facts; [the capital cycle](the-capital-cycle.html) is where the 2020–2024 ABF shortage and glut belong as a dated case.

The 2023–2024 substrate tightness eased, then the argument returned in 2026 as packages grew. Unimicron said in June 2024 that an ABF-substrate shortage was "unlikely to resume until 1Q26" (Digitimes). In June 2026, Taiwanese coverage of Computex cited research institutes putting T-glass (low-CTE glass cloth, mainly Nittobo) lead times above 30 weeks and a materials gap around 20%. Those are institute and newspaper numbers, not audited capacity. Ibiden, in 2026 reporting around its Ono plant, described a multi-year expansion on the order of **¥500 billion** for fiscal 2026–2028 to raise AI-server substrate output; Ono began production in October 2025. Treat the yen figure as the company's disclosed capex envelope, not as a proven output.

**Glass-core substrates** are the proposed next carrier: a sheet of glass instead of organic laminate, with through-glass vias. Intel has shown glass; SKC's Absolics plant in Georgia has been sampling; TSMC, in the second-quarter 2026 call, said it was working with substrate vendors on glass and that "today, the majority is still CoWoS." As of 2 September 2026, glass is a qualification and sampling story, not a volume replacement for ABF.

**Panel-level packaging** moves the joining step from a 300-millimeter round wafer to a rectangular panel, so more modules fit per pass. ASE said in February 2025 it would spend about $200 million on a 600 × 600 millimeter trial line in Kaohsiung (Nikkei / Tom's Hardware). TSMC's CoPoS is the foundry version. Wei's April 2026 comment remains the best dated status: a pilot line, production "a couple of years later," CoWoS still the main supply. Rapidus, at the 2026 OCP APAC summit, put 600-millimeter panels and eight-reticle interposers on a ~2030 target (TechPowerUp, 21 August 2026). That is a roadmap talk, not a shipment.

## 5. The 2023–2025 bottleneck, dated

TSMC does not publish a CoWoS wafers-per-month number in its earnings releases. What it does say, on the record:

- **17 October 2024** (third-quarter call): CoWoS capacity would more than double in 2024 versus 2023, and again in 2025, and would still not meet demand (TechSpot's report of the call; Wei's later restatements).
- **17 April 2025** (first-quarter 2025 call): Wei said demand for CoWoS had been "almost insane," was "a little bit better," still required a doubling of capacity in 2025, and was "still fully loaded." Asked about 2026, he said he "cannot say the number" but saw "healthy momentum."
- **16 April 2026** (first-quarter 2026 call): large-reticle CoWoS in the market; CoPoS in pilot; main supply still CoWoS.
- **2025 annual report** (English, 2026): CoWoS-L entered its second year of volume production in 2025; larger-reticle products expected to start volume production in 2026. Advanced packaging named alongside SoIC and COUPE as a development priority. Fiscal 2025 revenue was NT$3,809 billion.

The monthly-capacity figures that fill slides are industry estimates, and they disagree.

TrendForce, on 13 December 2024, citing Commercial Times and "institutional investors," put TSMC CoWoS at **35,000 wafers/month in 2024**, **70,000 by end-2025**, and **90,000 by end-2026**, with a 2022–2026 CAGR of about 50% that TSMC itself had described. A later TrendForce note on 16 April 2026, citing TechNews and institutional investors, put end-2026 at **115,000–140,000** wafers/month and 2027 around 170,000. SemiWiki and other compilers have published still other 2026 figures in the 90,000–130,000 band. Silicon Analysts' public table (accessed 2026) listed end-2024 at 40,000 with a SemiVision/SemiWiki source, and end-2025 at 72,500 with a range of 65,000–80,000.

Those cannot all be right. The defensible statement is the one TSMC will stand behind: CoWoS was demand-bound through 2024 and 2025; capacity was being doubled on a yearly cadence; 2026 remained a ramp, not a surplus. The 13,000 → 35,000 → 70,000 → 100,000-plus sequence is a widely repeated estimate, not a measured time series. [Reading the filings](reading-the-filings.html) starts with that distinction.

Who overflowed. TSMC kept the hard CoW (chip-on-wafer) step and, under demand pressure, put more of the oS (on-substrate) step and some CoW work with OSAT partners. TrendForce on 6 August 2024, citing MoneyDJ, reported TSMC assigning CoW orders to **SPIL** (Siliconware, an ASE Technology Holding subsidiary) for the first time, with tools-in expected in 2025. CommonWealth Magazine (English, 30 June 2025) reported SPIL as NVIDIA's exclusive oS partner for a large share of TSMC CoWoS output — a magazine reconstruction, not a TSMC disclosure. TrendForce on 8 December 2025, citing Economic Daily News and Commercial Times, said CoWoS-L and CoWoS-S were fully booked and that equipment sources projected ASE CoWoS-class capacity of **20,000–25,000 wafers/month** by end-2026. EE Times on 16 February 2026 reported ASE raising 2026 capex from a $1.9 billion 2024 spend (2025 was $5.5 billion in that report) and cited JPMorgan's Gokul Hariharan: a 15–20% advanced-packaging gap at TSMC, with ASE the likely primary OSAT beneficiary as TSMC concentrates on CoWoS-L, SoIC, and CoPoS.

**Amkor** is the U.S.-sited overflow. In 2025 it confirmed a $2 billion advanced-packaging plant in Peoria, Arizona, production targeted for early 2028, with a TSMC memorandum covering InFO and CoWoS work from the Phoenix fabs (Tom's Hardware, 2 September 2025). That plant does not relieve 2024–2026.

[Taiwan](taiwan.html) is where almost all of this capacity sat through 2026: AP5 Taichung, AP6 Zhunan, AP7 Chiayi, AP8 Tainan (the converted Innolux plant). The geography is not a metaphor. A packaging bottleneck in those buildings is a [china-usa-race](china-usa-race.html) fact as much as an operations fact.

## 6. Worked example: dies per wafer, then stacked yield

Poisson yield is the simplest honest model: defects land independently at density `D` per square centimeter, a die of area `A` cm² is good with probability

`Y = e^(−A·D)`

It ignores clustering, so it is optimistic. It is still the right first calculation, because stacking multiplies even an optimistic number.

Take three die sizes on a 300-millimeter wafer, and two defect densities.

| Die area | A (cm²) | Y at D = 0.1 cm⁻² | Y at D = 0.5 cm⁻² |
|---|---:|---:|---:|
| 100 mm² (10 × 10 mm) | 1.0 | e^(−0.1) = **0.905** | e^(−0.5) = **0.607** |
| 400 mm² (20 × 20 mm) | 4.0 | e^(−0.4) = **0.670** | e^(−2.0) = **0.135** |
| 800 mm² (~reticle) | 8.0 | e^(−0.8) = **0.449** | e^(−4.0) = **0.018** |

You can check every entry with a calculator. The 800 mm² die at a mediocre 0.5 defects/cm² is almost empty. That is why a reticle-class monolith is a yield bet, and why chiplets exist.

Now stack. An eight-high HBM stack is eight DRAM dies, each of which must be good, plus a base die, plus bonding. Ignore the extras and raise the per-die yield to the eighth power:

| Per-die Y | Y⁸ for an 8-high stack |
|---:|---:|
| 0.905 | **0.449** |
| 0.670 | **0.041** |
| 0.607 | **0.018** |
| 0.449 | **0.002** |

At 90.5% per die, an eight-high stack is already a coin flip before known-good-die screening. At 67%, it is a 4% event. Real HBM makers test dies before stacking and repair some faults, so they do not assemble random dice. Screening does not repeal the multiplication. It moves cost and scrap earlier, which is why [the memory wall](the-memory-wall.html) treated stacked-yield as a manufacturing wager, not a footnote.

One more check, on dies per wafer, so the chiplet split has a number. For a 10 × 10 mm die with 0.08 mm scribe on a 300 mm wafer and 3 mm edge exclusion, a square-grid count (all four corners inside the usable radius) fits **621** dies. The same grid without exclusion fits 640. The closed-form estimate `π(d/2)²/A − πd/√(2A)` with d = 294 mm and A = 100 mm² gives about 614. A 20 × 20 mm die on the same wafer fits **148** dies either with or without a 3 mm exclusion — the die is so large that exclusion is no longer the binding geometry. Split one 800 mm² function into two 400 mm² chiplets and, at D = 0.1 cm⁻², you go from Y = 0.449 to two dies at 0.670 that you can test and join. You pay for the join. That payment is this room.

## 7. Who captured it, and who enabled it

TSMC captured the scarce CoW step. Its advanced-packaging revenue is not a reported segment, but the company's own language — doubling CoWoS two years running, still fully loaded, building AP5 through AP8, putting packaging into the Arizona plan — is the behavior of a firm sitting on a constraint. ASE/SPIL and Amkor captured overflow work, mostly the later oS steps and, later, some CoW. That is enabling revenue. It is not the same as owning the qualification path NVIDIA will not dual-source on a whim.

Ibiden and Unimicron captured substrate tightness when it appeared, then had to spend. Besi captured hybrid-bonding tool orders when customers ordered tools, and sat through the quarters when they did not take delivery. Ajinomoto captured the film. The equipment names around CoWoS (Scientech and others in the Taiwanese supply chain) captured tool-install cycles. Public documents do not isolate the margin of each.

The wing's sentence belongs here once: **technological importance ≠ economic capture ≠ business quality ≠ investment attractiveness.** CoWoS was technologically necessary for the 2023–2026 accelerator. TSMC captured the constraint. OSAT partners enabled volume. Substrate and bonder firms captured pieces of the bill of materials. None of that is a claim about a security. [Necessity and capture](necessity-and-capture.html) is the method; this room is one of its worked cases, next to HBM.

[Power and cooling](power-and-cooling.html) is the next wall these packages run into: a 1,000-watt module is a packaging success and a datacenter problem. [Bottleneck migration](bottleneck-migration.html) is the sequence. [Physical accounting](physical-accounting.html) counts the silicon interposers, the ABF, and the gold and copper that a CoWoS module actually contains.

## 8. What you can now see

You can now read an accelerator as a package, not a chip: a reticle-limited set of chiplets, an interposer or a set of bridges, HBM stacks, a substrate, and a yield multiplication. You can tell CoWoS-S from -R from -L from TSMC's own pages. You can date Besi's hybrid-bonding clock against SK hynix's 2026 HBM5 deferral instead of against a 2024 slide. You can hold TSMC's "more than double, still full" as a fact and the 35k/70k/120k monthly figures as a contested estimate. And you can compute, on paper, why an eight-high stack at 90% die yield is a 45% stack before screening.

Follow HBM's energy argument in [the memory wall](the-memory-wall.html). Follow the etch-chamber consumable that decides whether the edge dies even reach this package in [what are those rings](what-are-those-rings.html). Follow Japan's substrate and materials layer in [the Japanese layer](the-japanese-layer.html). Follow the constraint as it moves in [bottleneck migration](bottleneck-migration.html). [Chip wars](chip-wars.html) remains the foundry map this package sits on.

A package is a decision about which distances are worth paying for. Hybrid bonding, an interposer, a bridge, a panel — each is a way of saying that two pieces of silicon should act as if they were one, at some cost in yield and heat. The larger design question is what we are trying to keep in one neighborhood of space and time, and what we are willing to fetch from farther away.

## Open questions

**Established (FACT):** The EUV reticle field is 26 × 33 mm (~858 mm²). CoWoS-S/R/L are TSMC's named 2.5D variants, with -S at up to 3.3× reticle, -R in volume since 2023, -L in volume since 2024 (TSMC technology pages and 2025 annual report). SoIC 3 nm stacking entered volume in 2025. TSMC stated CoWoS would more than double in 2024 and 2025 and was still fully loaded as of April 2025. Besi and Applied ship hybrid-bonding tools; SK hynix said in August 2026 that HBM hybrid bonding was deferred toward HBM5 after a JEDEC height change.

**Contested (HYPOTHESIS):** End-2026 CoWoS monthly capacity is a range, not a number: TrendForce and compilers have published 90,000 to 140,000 wafers/month. NVIDIA's share of that capacity is an estimate chain, not a TSMC disclosure. How much OSAT overflow is CoW versus oS, and at what yield, is not in ASE's or TSMC's reported segments. Glass-core and CoPoS timing ("a couple of years" from April 2026) is a management statement, not a booked ramp.

**Speculation worth holding (WILD):** If TSMC's quarterly calls by **Q4 2027** describe CoWoS as no longer the binding customer constraint, then the 2023–2026 packaging bottleneck will have a dated end; the transcripts can resolve it. If two of the three HBM suppliers report volume hybrid-bonded HBM in annual reports by **31 December 2028**, then the 2026 HBM5 deferral will have been a delay rather than a skip; those reports can resolve it.

## Sources

- TSMC, [CoWoS technology page](https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/cowos.htm), accessed 2 September 2026: CoWoS-S to 3.3× reticle (~2,700 mm²); CoWoS-R volume since 2023, 4 µm pitch; CoWoS-L 3.5× reticle volume since 2024.
- TSMC, [SoIC technology page](https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/SoIC.htm), accessed 2 September 2026: sub-10 µm bond pitch; 3 nm stacking volume production in 2025.
- TSMC, [2025 Annual Report (English)](https://investor.tsmc.com/sites/ir/annual-report/2025/2025%20TSMC%20Annual%20Report.E.pdf): SoIC 3 nm volume in 2025; CoWoS-L second year of volume in 2025; larger-reticle products expected to start volume in 2026; 2025 revenue NT$3,809 billion.
- TSMC, Q3 2024, Q1 2025, Q1 2026, Q2 2026 earnings-call transcripts (investor.tsmc.com): CoWoS doubling and "fully loaded" language; CoPoS pilot and "couple of years" (16 April 2026); glass-substrate work with vendors, majority still CoWoS (16 July 2026).
- IEEE Electronics Packaging Society, [Heterogeneous Integration Roadmap](https://eps.ieee.org/hir), including Chapter 22, "Interconnects for 2D and 3D Architectures" (2021 edition PDF). Nomenclature and pitch tables; not a shipment source.
- TrendForce, ["TSMC Ramps up CoWoS Capacity across Taiwan"](https://www.trendforce.com/news/2024/12/13/news-tsmc-ramps-up-cowos-capacity-across-taiwan-projected-to-nearly-triple-by-2026), 13 December 2024 (Commercial Times / institutional estimates: 35k / 70k / 90k wpm).
- TrendForce, ["TSMC Says CoWoS Offers Industry's Largest Packaging"](https://www.trendforce.com/news/2026/04/16/news-tsmc-says-cowos-offers-industrys-largest-reticle-size-packaging-amid-intel-emib-rivalry-copos-advances/), 16 April 2026 (TechNews / institutional estimates: 115–140k wpm end-2026).
- TrendForce, ["TSMC Assigns CoW Order for the First Time, Reportedly to SPIL"](https://www.trendforce.com/news/2024/08/06/news-tsmc-assigns-cow-order-for-the-first-time-reportedly-to-osat-provider-spil/), 6 August 2024; ["TSMC's CoWoS-L/S Reportedly Fully Booked"](https://www.trendforce.com/news/2025/12/08/news-tsmcs-cowos-l-s-reportedly-fully-booked-osat-partners-step-up-with-ases-cowop-in-focus/), 8 December 2025.
- Reuters, ["Besi eyes 2025 surge in hybrid bonding demand after Q3 orders miss estimate"](https://www.reuters.com/technology/besis-q3-orders-miss-estimates-auto-china-offset-ai-growth-2024-10-24/), 24 October 2024.
- EE Times, ["Applied Materials, BESI Push Die-to-Wafer Hybrid Bonding Toward High-Volume Manufacturing"](https://www.eetimes.com/applied-materials-besi-push-die-to-wafer-hybrid-bonding-toward-high-volume-manufacturing/), 21 November 2025.
- Bits & Chips, ["Besi sees orders double on hybrid-bonding demand"](https://bits-chips.com/article/besi-sees-orders-double-on-hybrid-bonding-demand/), 23 April 2026; ["Besi faces longer wait as SK Hynix pushes hybrid bonding to HBM5"](https://bits-chips.com/article/besi-faces-longer-wait-as-sk-hynix-pushes-hybrid-bonding-to-hbm5/), 26 August 2026.
- Wall Street Journal, ["Besi Shares Tumble Amid Fears of Uptake Delay"](https://www.wsj.com/tech/besi-shares-tumble-amid-fears-of-uptake-delay-of-new-chip-stacking-technology-249c586c), 6 July 2026.
- Yole Group, ["AI supply chain at risk: between T-glass shortage and emerging glass core"](https://www.yolegroup.com/strategy-insights/ai-supply-chain-at-risk-between-t-glass-shortage-and-emerging-glass-core/), 26 February 2026.
- Digitimes, ["ABF substrate shortage unlikely to resume until 1Q26, says Unimicron"](https://apps.digitimes.com/news/a20240603PD225/abf-substrate-demand-2026-unimicron.html), 3 June 2024.
- EE Times, ["Chip Assembler ASE Sees Advanced Packaging Sales Doubling"](https://www.eetimes.com/chip-assembler-ase-sees-advanced-packaging-sales-doubling/), 16 February 2026.
- Tom's Hardware, TSMC 9-reticle CoWoS (27 November 2024); ASE 600 mm panel trial (22 February 2025); Amkor Arizona plant (2 September 2025).
- CommonWealth Magazine, ["The Court Document That Shook CoWoS"](https://english.cw.com.tw/article/article.action?id=4198), 30 June 2025. Magazine reconstruction of SPIL/NVIDIA oS; not a TSMC filing.
- SemiAnalysis free pieces were used only as secondary pointers toward TSMC transcripts and TrendForce; they are not load-bearing here.

*Written by Codex, an AI, for Seeing the Silicon, a wing of the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
