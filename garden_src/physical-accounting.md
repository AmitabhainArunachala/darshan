---
title: "Physical Accounting: What a Chip Costs the World"
slug: physical-accounting
series: silicon
tags: energy, carbon, water, materials, koomey, rebound, lca, h100, embodied, grid
summary: A chip's cost to the world is a ledger with boundaries, not an ESG slogan. This room builds that ledger for one named accelerator — energy, carbon, water, materials, grid — and shows which unknown dominates the total.
status: draft
date: 2026-09-02
terms_defined: physical-accounting, embodied-carbon, operational-carbon, system-boundary, allocation, rebound-effect, koomeys-law, consumptive-water, withdrawn-water
terms_linked: bottleneck-migration, power-and-cooling, semiconductors, nvidia-and-the-chip, chip-wars, taiwan, the-memory-wall, advanced-packaging, necessity-and-capture, the-capital-cycle, forecasting, attention-economy, governments-and-ai, neural-networks, china-usa-race, trends-gap, the-future, optimization
---

# Physical Accounting: What a Chip Costs the World

You have just watched scarcity migrate through [memory](the-memory-wall.html), [packaging](advanced-packaging.html), and [power](power-and-cooling.html). This room asks a prior question: what does one of those accelerators actually take from the world, in energy, carbon, water, and materials, once you say what you counted? The answer is a ledger. It is not a score, a rating, or a reason to buy or avoid a company.

## 1. A ledger with edges

**Physical accounting** is the practice of counting energy, mass, water, and emissions through a named object, over a named period, inside a named **system boundary** — the list of processes you included and the list you left out. The next discipline is **allocation**: when a fab, a grid, or a cooling tower serves more than one product, you must say how you split the shared burden. If either is missing, the number is a slogan with a unit.

Vaclav Smil's *Making the Modern World* (2013; second edition 2023) is the framing, not a 2026 dataset: materials have energy costs, and less mass per device does not, by itself, cut total extraction. Silicon is abundant in the crust and scarce as electronic-grade crystal — the distinction [semiconductors](semiconductors.html) is built on.

Two carbon words, then, because they are not synonyms. **Embodied carbon** is the greenhouse-gas burden of extracting, refining, fabricating, assembling, and moving the hardware, usually reported as carbon-dioxide equivalent. **Operational carbon** is the burden of the electricity (and on-site fuel) used while the hardware runs, including the cooling overhead of the building. Gupta, Kim, Lee, Tse, Lee, Wei, Brooks and Wu, "Chasing Carbon," HPCA 2021, used industry-reported product data to show that for modern mobile devices, and for a substantial share of data-center equipment in their sample, manufacturing and infrastructure dominate the life-cycle carbon. That result is dated and bounded. It is not a law that a 700-watt accelerator, run hard on a fossil-heavy grid, is mostly an embodied object. The boundary decides which term wins.

This is also where the wing's anchor sentence earns its place: **technological importance ≠ economic capture ≠ business quality ≠ investment attractiveness.** A material can be physically indispensable and still fail to concentrate profit, as [necessity and capture](necessity-and-capture.html) shows with quartz crucibles and photoresist. Physical scarcity is an input to that chain. It is not the chain.

The room's standard is simple. Explicit UNKNOWN is always preferable to a fabricated environmental number. The first invented kilogram of carbon, litre of water, or gram of metal would kill the room. A model's number is a lead. A press release corroborates only itself.

## 2. Energy per computation, and why the doubling slowed

**Koomey's law** is the observation, published by Jonathan Koomey, Stephen Berard, Marla Sanchez and Henry Wong in the *IEEE Annals of the History of Computing* in 2011, that the number of computations per kilowatt-hour roughly doubled every 1.57 years from 1946 to 2009. At a fixed computing load, the battery you needed fell by about half every year and a half. Koomey re-examined the series after 2000 and found the doubling had slowed to about once every 2.6 years, coinciding with the end of Dennard scaling — the old trick of shrinking transistors without raising power density — around 2005.

Fernández-Cerero and colleagues, in *Cluster Computing* in 2024, fitted high-performance computers from 2008 to 2023 and got a doubling every 2.29 years. Performance still grew faster than efficiency. A more efficient accelerator can still raise total electricity: more work per watt, and more watts.

Put a named object under that curve. Nvidia's H100 SXM, the Hopper-generation accelerator described in [Nvidia and the chip](nvidia-and-the-chip.html), has a configurable thermal design power — the heat the cooling system is designed to remove — of up to 700 watts, as of the company's H100 datasheet. Eight of them on an HGX H100 baseboard are listed at a typical 5,600 watts in Nvidia's July 2025 product-carbon-footprint summary. Those are nameplate and typical-power figures, not a measurement of your rack. They already tell you that one board is a small electric stove, running for years.

Zoom out. The International Energy Agency's *Energy and AI* report, published in 2025, estimated global data-centre electricity use at about 415 terawatt-hours in 2024, roughly 1.5% of world electricity, and around 945 TWh in 2030 under its base case. Lawrence Berkeley National Laboratory's *2024 United States Data Center Energy Usage Report* (Shehabi, Smith, Hubbard, Newkirk, Lei, Siddik, Holecek, Koomey, Masanet and Sartor, December 2024) put US data-centre electricity at 176 TWh in 2023, 4.4% of US consumption, with a 2028 scenario range of about 325 to 580 TWh. Those two instruments do not measure the same geography or the same year. They agree on direction: the load is growing faster than the rest of electricity.

Capacity is not energy. A megawatt is a rate; a megawatt-hour is a quantity. Berkeley Lab's *Queued Up: 2026 Edition* counted, as of the end of 2025, about 1,312 GW of generation and 749 GW of storage still seeking US transmission interconnection, with a median request-to-operation time of more than five years for projects completed in 2025. Only about 13% of capacity that entered queues between 2000 and 2020 had been built by the end of 2025. The IEA estimated that around 20% of planned data-centre capacity could be delayed, and that new transmission commonly takes four to eight years. [Bottleneck migration](bottleneck-migration.html) follows that delay as a constraint. This room records it as a clock: you cannot spend a kilowatt-hour that has not been connected.

## 3. Carbon, and the boundary that decides which term wins

Gupta and colleagues' HPCA 2021 paper is still the cleanest statement of the embodied case. Using industry product reports, they showed that as operational energy per computation fell, the share of life-cycle emissions sitting in manufacturing and infrastructure rose, especially for battery-powered devices — on the order of three-quarters of life-cycle carbon in their mobile sample. Fabs themselves split roughly as energy, chemicals, fluorinated gases, and wafers. A 100% renewable-powered fab, in their calculation, cut manufacturing carbon by about 2.5 times and still left a large remainder.

Wu, Raghavendra, Gupta and co-authors of "Sustainable AI," MLSys 2022, widened the frame from a device to a model-development cycle. Operational carbon of training is (time) × (processors) × (power) × (PUE) × (grid intensity). Inference, once a model is in production, can exceed training. The paper's contribution is the split, not a headline kilogram.

Now the named object. In a July 2025 summary, Nvidia published an ISO 14067-conformant, third-party-reviewed product carbon footprint, performed by WSP, for one HGX H100 GPU baseboard: eight H100 SXM modules, 640 GB of HBM3, cradle-to-gate. The company reported 1,312 kg of CO2-equivalent. Materials and components were 91% of that; assembly 8.6%; inbound material transport 0.4%. Inside materials, high-bandwidth memory was 546 kg (42%), integrated circuits including the GPUs 332 kg (25%), and thermal components 230 kg (18%). The summary explicitly excludes use-phase and end-of-life "due to the variability in those emissions based on customer usage." Primary data covered more than 92% of the product by weight. Secondary data included imec's net.zero tool and the ecoinvent 3.10 and Sphera 2024 databases.

That 1,312 kg is a company-commissioned, reviewed figure for a defined boundary. It is not an audit of the entire supply chain by an independent laboratory, and it is not eight times a single-GPU number you can drop into a spreadsheet without stating the allocation. Divide by eight and you get 164 kg CO2e per H100-plus-share-of-board. ADEME's 2026 GPU life-cycle study (Lees-Perasso and colleagues), which EcoLogits uses, estimated about 273 kg CO2e for an H100 80 GB card on a different boundary, without the HGX board. The two numbers are in the same order of magnitude. They are not interchangeable. UNKNOWN would be the right label for "the" embodied carbon of an H100. The honest range, as of Q2 2026, is roughly 160–280 kg CO2e per GPU-equivalent depending on whether you include the board, which databases you trust, and how you treat HBM.

For a 700-watt device, operation can swamp that range quickly. It can also fail to. The worked example is built to show the switch.

A model-level contrast, because the object of accounting is easy to slide. Mistral, with Carbone 4 and ADEME, published in July 2025 a life-cycle analysis of Mistral Large 2, peer-reviewed by Resilio and Hubblo. As of January 2025, after eighteen months: 20.4 ktCO2e, 281,000 m³ of water, 660 kg antimony-equivalent. Training and inference were 85.5% of greenhouse gases and 91% of water; hardware's embodied share was 61% of materials. A 400-token Le Chat reply, excluding the user's terminal, was 1.14 gCO2e and 45 mL of water. Those are Mistral's figures for Mistral's model. They do not substitute for an H100 ledger. Mixing a model account with a chip account is how synthetic precision is born.

## 4. Water: withdrawn, consumed, fab, tower

Water accounting dies on a single confusion. **Withdrawn water** is taken from a source. **Consumptive water** is withdrawn and not returned — evaporated from a cooling tower, incorporated into a product, or contaminated beyond reuse. A cubic metre withdrawn from a wet river and returned downstream is not the same event as a cubic metre evaporated in a desert.

Li, Yang, Islam and Ren, "Making AI Less 'Thirsty'," first posted in 2023 and later published in *Communications of the ACM* (2025), estimated that training GPT-3 in Microsoft's US data centres consumed about 700,000 litres of on-site freshwater, and about 5.4 million litres once off-site water embedded in electricity was included. They projected global AI-related water withdrawal of 4.2–6.6 billion cubic metres in 2027. Those figures are model-and-site estimates, not meter readings on a named cluster. The method is the contribution: on-site water-usage effectiveness plus off-site water in the grid, varying by hour and place.

Fab water is a different industry. TSMC's 2024 annual report put total water use, Taiwan fabs plus subsidiaries, at 129 million cubic metres, and unit use at 161.0 litres per 12-inch-equivalent wafer-mask layer, against a 2010 baseline of about 141 litres. The 2030 target is a 30% unit reduction from 2010; 2024 missed it. Reclaimed water in Tainan exceeded 19.65 million cubic metres cumulative by the end of 2024. None of that allocates to one H100. Mask-layer count, yield, and the split between logic, HBM, and the interposer are not public at product level. The GPU's manufacturing water is UNKNOWN. The company's water is not.

Data-centre cooling is the other column. A cooling tower evaporates water to dump heat. Direct-to-chip liquid loops can reduce on-site evaporation and shift the burden into the facility that rejects the heat, or into the electricity used by dry coolers. Google and Microsoft publish campus-level withdrawn and consumptive figures; they do not publish an H100-hour. Li and colleagues' on-site WUE is the transferable factor, and it varies by more than a factor of three across Microsoft's own regions in their paper. Site is not a detail. Site is the number.

## 5. Materials that never appear on the spec sheet

Gallium and germanium are not in the H100 the way copper is in a cable. They sit in compound-semiconductor photonics, in some power devices, and in the fibre and infrared optics around the machine. The US Geological Survey's *Mineral Commodity Summaries 2026* estimated US net import reliance for gallium metal at 100%, with China producing on the order of 900 tonnes of low-purity gallium in 2025 against a world total near 900 tonnes. Germanium's major US uses, in the 2025 summary, were fibre optics, infrared optics, and semiconductor applications; China banned germanium exports to the United States in December 2024. Those are trade facts, not a kilogram-per-GPU. The [China–USA race](china-usa-race.html) and [governments and AI](governments-and-ai.html) are where the export-control story lives. This room only needs the physical point: a chip-adjacent metal can bind a different industry than the silicon it is discussed with.

Tantalum is closer to the board. USGS 2026: the United States was 100% net-import-reliant; apparent consumption in 2025 was estimated at 890 tonnes, up 58% from 2024; the major use is electronic capacitors. Congo (Kinshasa) and Rwanda together were about two-thirds of estimated world mine production. Recycled new scrap may account for as much as 30% of consumption by US primary processors. How many milligrams sit in one HGX H100 is UNKNOWN.

Neon is the laser's buffer gas in deep-ultraviolet lithography. Reuters, using company figures and Techcet, reported in March 2022 that two Ukrainian firms, Ingas and Cryoin, supplied about 45–54% of semiconductor-grade neon. Both halted operations as the invasion began. Chipmakers said they held months of inventory; prices spiked. Substitution and Chinese purification capacity later eased the immediate bind. The 2022 episode is dated evidence that a gas nobody lists on a GPU datasheet can halt a lithography tool.

Helium cools, purges, and leak-tests. It has no chemical substitute in those roles. After damage to Qatar's Ras Laffan helium complex in March 2026, Taiwan's Ministry of Economic Affairs said alternative US imports were available and that major fabs had recycling systems from the 2021 shortage. Nikkei Asia, relayed by *Taiwan News* in July 2026, reported that US shipments were nearly 60% of Taiwan's helium and other noble-gas imports in the first half of 2026, up from less than 4% in 2025, while Qatar's share fell from nearly 88% to about 30%. TSMC said it did not anticipate a significant near-term impact. That is a company statement. The physical dependency is not in dispute: [Taiwan](taiwan.html)'s leading-edge output, which [the chip wars](chip-wars.html) maps, runs on an imported noble gas.

High-purity quartz, less than 100 parts per million impurities, is fused into crucibles that hold the silicon melt. USGS 2026 notes Spruce Pine, North Carolina, historically associated with 99.999% material, and a 2025 Chinese announcement of large HPQ reserves at 99.995–99.998%. The crucible is the object of [necessity and capture](necessity-and-capture.html): the wafer's silicon is common; the vessel that froze it is not.

Naphtha is the petrochemical feedstock behind solvents, resins, and photoresist precursors. Taiwan's Ministry of Economic Affairs, in its 23 March 2026 briefing, named petrochemical raw materials — methanol, polyethylene, polypropylene — alongside helium as the two industrial exposures it was managing. A photoresist molecule is not a barrel of naphtha. A chemicals industry without naphtha does not make photoresist.

End of life is the shortest column. Advanced packages — CoWoS-class assemblies of logic, HBM, and interposer — are not recycled at commercial scale into equivalent silicon. Nvidia's FY2025 sustainability report said GPU-systems *packaging* was 97% recyclable materials by weight. Packaging is cardboard, foam, and trays. It is not the 24-kilogram HGX board. Treat recovery of the advanced package as approximately nil unless a named recycler publishes a mass balance you can read.

## 6. A life-cycle table for one named accelerator

The object is one Nvidia H100 SXM 80 GB as installed on an HGX H100 eight-GPU baseboard. Carbon figures that say "board" are for the eight-GPU assembly; per-GPU lines allocate equally. Water and materials at GPU grain are mostly UNKNOWN. Bands are published ranges, not probability distributions.

| Stage | What is counted | Boundary | Source (as of) | Central figure | p05 / p95 or UNKNOWN |
|---|---|---|---|---|---|
| Manufacturing, carbon | Cradle-to-gate GHG of one HGX H100 baseboard (8× H100 SXM) | Raw materials through assembly; no use, no end-of-life, no rack, no building | Nvidia PCF summary, WSP, ISO 14067 (July 2025) | 1,312 kg CO2e per board (164 kg per GPU-share) | Independent GPU LCAs ~160–280 kg/GPU-equivalent; treat as **UNKNOWN** at ±50% without the underlying inventory |
| Manufacturing, water | Fab ultrapure water plus assembly | TSMC reports company litres per wafer-layer, not per H100 | TSMC 2024 annual report | 161 L / 12-inch wafer-e-layer company-wide | **UNKNOWN** per GPU (mask-layer count and yield not public) |
| Manufacturing, materials | HBM, ICs, thermals, Ta, He, Ne, Ga, Ge, HPQ | PCF splits carbon, not mass of critical minerals | Nvidia PCF; USGS MCS 2025–26 | HBM 42% of board carbon | Mass of Ta, Ga, Ge, He, Ne per board **UNKNOWN** |
| Operation, energy | Electricity at the wall, including cooling | GPU TDP × utilisation × hours × PUE; excludes network and storage unless added | Nvidia H100 datasheet (700 W SXM); PCF typical 5,600 W / 8 GPU | 0.7 kW nameplate per GPU | Utilisation, PUE, hours: **UNKNOWN** until the operator says |
| Operation, carbon | Energy × grid intensity | Must name the grid year and region | Ember: 384 gCO2/kWh US 2024; EIA: 0.81 lb/kWh (~367 g) US 2023 | See worked example | Site mix can be <50 g or >600 g; this term dominates when it is large |
| Operation, water | On-site evaporation plus off-site power-plant water | WUE_on-site + PUE × WUE_off-site | Li et al. 2023/2025; provider WUE where published | **UNKNOWN** per H100-hour | Varies by more than 3× across regions in Li et al. |
| End-of-life | Recovery of silicon, HBM, substrate, board | Advanced package vs cardboard packaging | Nvidia FY2025 sustainability (packaging 97% recyclable by weight) | Package recovery ~nil in practice | **UNKNOWN** as a recovered-mass fraction; do not use the packaging figure for the chip |

Read the table as a warning label. The one precise carbon number is cradle-to-gate for a board Nvidia paid to have studied. Everything that would turn that board into a life-cycle total is either a scenario or UNKNOWN.

## 7. Worked example: build the H100 account, and watch one unknown take over

You can rerun this in a spreadsheet. Yellow cells are the ones you are allowed to change. Do not treat the output as a measurement.

**Step 1: write the manufacturing carbon you actually have.**

Nvidia, July 2025, HGX H100 baseboard, cradle-to-gate: `1,312 kg CO2e`.

Per GPU-share, equal allocation: `1,312 / 8 = 164 kg CO2e`.

Boundary reminder: no rack, no building, no networking switch, no use, no disposal.

**Step 2: write operational energy as a product, not a guess.**

For one GPU:

`E_kWh = 0.7 kW × 8,760 h/year × u × PUE × L_years`

Three scenarios, all invented for the arithmetic, all labelled as such:

| Scenario | u (utilisation) | PUE | Lifetime L | E (kWh) |
|---|---|---|---|---|
| A. Short, cool, idle-ish | 0.30 | 1.10 | 2 | 4,042 |
| B. Mid, US-typical | 0.65 | 1.20 | 3 | 14,355 |
| C. Hard, long, poor cooling | 0.80 | 1.40 | 5 | 34,339 |

Nvidia's PCF used 5,600 W typical for eight GPUs, which is 700 W each — the same 0.7 kW. If your board runs below TDP, lower the 0.7. If it does not, do not.

**Step 3: multiply by a named grid.**

Ember's US 2024 intensity: `0.384 kg CO2/kWh`. EIA's 2023 utility-scale figure: `0.81 lb/kWh ≈ 0.367 kg/kWh`. Use 0.384 for the US-average column, then a clean column at 0.050 (a very low-carbon mix) and a dirty column at 0.670 (a gas-heavy marginal mix in the range discussed around some on-site turbines). These are scenario intensities, not a forecast of your city.

Operational carbon, kg CO2e, one GPU:

| Scenario | Clean 0.050 | US 0.384 | Dirty 0.670 |
|---|---|---|---|
| A (4,042 kWh) | 202 | 1,552 | 2,708 |
| B (14,355 kWh) | 718 | 5,512 | 9,618 |
| C (34,339 kWh) | 1,717 | 13,186 | 23,007 |

**Step 4: add manufacturing, and look at the ratio.**

Using 164 kg embodied:

- Scenario A on a clean grid: 164 + 202 = 366 kg. Embodied is 45% of the total. Gupta's world.
- Scenario B on a US-average grid: 164 + 5,512 = 5,676 kg. Embodied is 3%. Operation owns the ledger.
- Scenario C on a dirty grid: 164 + 23,007 = 23,171 kg. Embodied is 0.7%.

The conclusion flips on the product `u × PUE × L × grid intensity`. That product is the single unknown that dominates. Not "AI." Not "the chip." Four numbers, only one of which (nameplate power) is on the datasheet. Anyone publishing a single life-cycle kilogram for an H100 without those four is either assuming them silently or making them up.

**Step 5: notice what you still have not counted.**

Water: UNKNOWN at GPU grain. Apply Li et al. only if you have WUE and kWh, and say so. Materials: the PCF tells you HBM is 42% of *carbon*, not the helium mass. End-of-life: still approximately nil. EcoLogits' Boavizta-based figure for a p5.48xlarge-class server without GPUs is about 5,700 kg CO2e embodied — a different object, needing an occupancy assumption you probably do not have.

The result is not "an H100 costs X kilograms." It is: **published manufacturing carbon for this board is 1,312 kg cradle-to-gate as of July 2025, and operational carbon is a four-factor product that can sit below, near, or forty times above the per-GPU share.** Update the yellow cells when an operator publishes utilisation, PUE, lifetime, and a location-based mix. Until then, the honest line is the range.

## 8. Rebound: an efficiency claim is not a total-burden claim

William Stanley Jevons, in *The Coal Question* (1865), noticed that cheaper useful work from coal expanded the uses of coal. Steve Sorrell's UK Energy Research Centre review (October 2007) is the modern evidence assessment. Direct rebound — using more of the cheaper service — for household heating and cars in rich countries was often under 30%. Economy-wide rebound, including the spending of saved money on other energy-using goods, was at least 10% and often higher. The review did not find that efficiency routinely increases total energy use. It did find that treating a 20% device-efficiency gain as a 20% system saving is a mistake.

Brockway, Sorrell, Semieniuk, Heun and Court, in *Renewable and Sustainable Energy Reviews* (2021), reviewed 33 economy-wide studies and found rebound often erodes more than half of expected energy savings. That is a literature review, not a measurement of H100 fleets. Apply it as a question. If Koomey's doubling continues at 2.3–2.6 years, computations per joule rise. If [neural networks](neural-networks.html) and [the attention economy](attention-economy.html) raise joules demanded faster than that, total energy rises. Wu et al. 2022 already noted the pattern: efficiency, then more use. [Trends-gap](trends-gap.html) is the garden's room for "this time the curve bent." [Forecasting](forecasting.html) is how you keep score.

The discipline is one sentence: an efficiency claim is a statement about intensity; a total-burden claim is a statement about intensity × activity, after rebound. Publishing the first as if it were the second is how green kilowatts become fiction.

This is research and education, not advice. The practical exercise is the same four columns [the capital cycle](the-capital-cycle.html) wants for money, now for mass and energy: boundary, allocation, intensity, activity. If one is blank, you do not have an account. If the intensity improved and activity is UNKNOWN, you do not have a saving.

## 9. What you can now see

You can now refuse a kilogram that has no edge. Embodied carbon of an HGX H100 board is a reviewed 1,312 kg cradle-to-gate as of July 2025, with HBM the largest slice — which is why [the memory wall](the-memory-wall.html) is an environmental fact as well as an architectural one. Operational carbon is a product you can compute and that you should not pretend to know. Water splits into fab litres that TSMC publishes at company grain and cooling litres that exist only at a named site. Materials bind through helium, neon, tantalum, gallium, germanium, and quartz, on clocks that [bottleneck migration](bottleneck-migration.html) already taught you to date. [Power and cooling](power-and-cooling.html) is the operational chapter of the same ledger; this room is the boundary around it.

You can also see why [the future](the-future.html) talk about "sustainable AI" is usually a category error. Sustainability, if the word is going to mean anything here, is a completed account plus a rebound check. Anything less is marketing copy about a chip.

From here, [optimization](optimization.html) is the mathematical cousin of Koomey's curve, and [advanced packaging](advanced-packaging.html) is where the HBM that dominates the PCF actually sits.

---

A physical account is a way of paying attention. The ledger does not tell you what the computation was for. It tells you that a thought which felt weightless was a 700-watt object, a stack of imported gas and stacked memory, a share of a Taiwanese litre, and a claim on a transformer that has not arrived. Follow the boundary long enough and the question the domain asks by itself is the old one: which uses of this scarce, hot, wet, material process are worth the slice they take, and who is entitled to decide? That is not a carbon coefficient. It is the political remainder after the arithmetic is done.

## Open questions

**Established (FACT):** Koomey's doubling of computations per kWh slowed after 2000, with published fits near 2.3–2.6 years rather than 1.57. Nvidia's July 2025 PCF reports 1,312 kg CO2e cradle-to-gate for one HGX H100 baseboard, HBM 42% of that carbon. The IEA's 2025 *Energy and AI* puts global data-centre electricity near 415 TWh in 2024 and, in its base case, near 945 TWh in 2030, with around 20% of planned capacity at risk of grid delay. LBNL 2024 puts US data-centre electricity at 176 TWh in 2023. USGS records 100% US net-import reliance for gallium and tantalum as of the 2026 summaries. These are dated observations.

**Contested (HYPOTHESIS):** For AI accelerators in production, operational carbon dominates embodied carbon on real fleets, so further manufacturing-carbon work is second-order. Three falsifiers: if, by **December 2027**, operators representing at least two independent HGX-class fleets publish location-based, 12-month electricity, PUE, and utilisation such that operational carbon per GPU-year is below 200 kg CO2e while the Nvidia-class embodied figure remains ~160 kg, the hypothesis fails for those fleets; if ADEME, imec, or a regulator publishes a cradle-to-gate H100-class inventory above 1,000 kg CO2e *per GPU* (not per eight-GPU board) by **June 2028**, embodied has been understated and the hypothesis needs re-basing; if the IEA's **2027** update shows global data-centre electricity below 500 TWh against a 2024 baseline of 415 TWh, activity did not run away from intensity and the operational-dominance claim weakens. Resolving sources: operator environmental reports with named sites, a third-party GPU LCA, IEA *Energy and AI* updates. Vendor efficiency slides do not resolve it.

**Speculation worth holding (WILD):** Package-level recyclability of CoWoS-class assemblies becomes a material mass flow, not a pilot, so that end-of-life stops being approximately nil. Treat as false unless, by **December 2028**, at least two recyclers and one foundry or OSAT publish a mass balance showing recovery of copper, silicon, and precious metals from production volumes of advanced packages, with a named percentage of HBM stacks actually reclaimed. Treat the opposite speculation — that HBM remains the binding environmental object inside the board — as strained if Nvidia's next ISO-reviewed PCF, or an independent equivalent, shows memory below 25% of cradle-to-gate carbon by **the 2027 PCF**, coinciding with a documented drop in HBM wafer intensity. A packaging recyclability press release corroborates only itself.

---

## Sources

Load-bearing claims were opened and checked live on 2 September 2026. Company environmental figures are identified as company reports. Anything not re-opened is labelled.

- Koomey's law: [Koomey, Berard, Sanchez and Wong, "Implications of Historical Trends in the Electrical Efficiency of Computing," *IEEE Annals of the History of Computing*, 2011](https://ieeexplore.ieee.org/document/5440129); slowdown after 2000 as discussed in Koomey's later notes and in [Fernández-Cerero et al., "Evolution of computing energy efficiency: Koomey's law revisited," *Cluster Computing*, 2024](https://link.springer.com/article/10.1007/s10586-024-04767-y) (doubling every 2.29 years, 2008–2023).
- Embodied versus operational: [Gupta et al., "Chasing Carbon: The Elusive Environmental Footprint of Computing," HPCA 2021 / arXiv:2011.02839](https://arxiv.org/abs/2011.02839); [Wu et al., "Sustainable AI: Environmental Implications, Challenges and Opportunities," MLSys 2022 / arXiv:2111.00364](https://arxiv.org/abs/2111.00364).
- Named accelerator, power: [Nvidia H100 product page and datasheet, TDP up to 700 W SXM, 80 billion transistors, TSMC 4N](https://www.nvidia.com/en-us/data-center/h100/).
- Named accelerator, embodied carbon: [Nvidia, "Product Carbon Footprint (PCF) Summary for NVIDIA HGX H100," July 2025](https://images.nvidia.com/aem-dam/Solutions/documents/HGX-H100-PCF-Summary.pdf) — 1,312 kg CO2e cradle-to-gate, HBM 546 kg, ICs 332 kg, thermals 230 kg, typical 5,600 W. Independent check: [ADEME / Lees-Perasso et al., GPU LCA, 2026](https://librairie.ademe.fr/economie-circulaire-et-dechets/9103-analyse-de-cycle-de-vie-de-gpu-cartes-graphiques-pour-l-intelligence-artificielle.html), used by [EcoLogits](https://ecologits.ai/latest/methodology/llm_inference/) at 273 kg CO2e per H100 80 GB.
- Model-level LCA (different object): [Mistral, "Our contribution to a global environmental standard for AI," 22 July 2025](https://mistral.ai/news/our-contribution-to-a-global-environmental-standard-for-ai/).
- Energy totals: [IEA, *Energy and AI*, 2025, executive summary](https://www.iea.org/reports/energy-and-ai/executive-summary) (415 TWh in 2024; ~945 TWh 2030 base; ~20% of planned capacity at delay risk; transmission 4–8 years); [IEA, "AI and energy security"](https://www.iea.org/reports/energy-and-ai/ai-and-energy-security); [Shehabi et al., LBNL *2024 United States Data Center Energy Usage Report*](https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report) (176 TWh in 2023; 4.4% of US electricity; 325–580 TWh in 2028).
- Grid queues: [Berkeley Lab, *Queued Up: 2026 Edition*](https://emp.lbl.gov/queued-2026-edition-characteristics-power-plants-seeking-transmission-interconnection-end-2025) (~1,312 GW generation + 749 GW storage active at end-2025; median >5 years request-to-COD for 2025 completions; 13% of 2000–2020 requests built by end-2025).
- Grid carbon intensity: [EIA FAQ, 2023, 0.81 lb CO2/kWh](https://www.eia.gov/tools/faqs/faq.php?id=74); [Ember, US electricity 2024, 384 gCO2/kWh](https://ember-energy.org/latest-insights/us-electricity-2025-special-report/insight-4-rising-demand-pushes-up-emissions-slight/).
- Water: [Li, Yang, Islam and Ren, arXiv:2304.03271, v5 March 2025, and *CACM* 2025](https://arxiv.org/abs/2304.03271); [TSMC 2024 annual report, water 129 million m³, 161.0 L per 12-inch wafer-e-layer](https://investor.tsmc.com/static/annualReports/2024/english/ebook/files/basic-html/page159.html).
- Materials: [USGS *Mineral Commodity Summaries 2025* and *2026*](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf) — gallium, germanium, tantalum, helium, high-purity quartz; [Reuters, 11 March 2022, Ukraine neon 45–54%](https://www.reuters.com/technology/exclusive-ukraine-halts-half-worlds-neon-output-chips-clouding-outlook-2022-03-11/); [Taiwan MOEA, 24 March 2026, helium and petrochemicals briefing](https://www.moea.gov.tw/MNS/English/news/News.aspx?kind=6&menu_id=176&news_id=122192); [Taiwan News / Nikkei, 14 July 2026, US helium share](https://www.taiwannews.com.tw/news/6400806). Helium-percentage-from-Qatar figures in 2026 press are secondary; the MOEA briefing is the primary that alternative US supply was being used.
- Rebound: [Sorrell, UKERC, *The Rebound Effect*, October 2007](https://ukerc.ac.uk/publications/the-rebound-effect-an-assessment-of-the-evidence-for-economy-wide-energy-savings-from-improved-energy-efficiency/); [Brockway, Sorrell, Semieniuk, Heun and Court, *Renewable and Sustainable Energy Reviews*, 2021](https://www.sciencedirect.com/science/article/pii/S1364032121000769); Jevons, *The Coal Question*, 1865.
- Framing: Vaclav Smil, *Making the Modern World: Materials and Dematerialization*, Wiley, 2013 (2nd ed. 2023), especially the electronics and recycling chapters. Not a 2026 measurement.
- EcoLogits method (inference allocation, not a chip LCA): [Rincé and Banse, *JOSS* 10(111):7471, 2025](https://doi.org/10.21105/joss.07471) and [methodology](https://ecologits.ai/latest/methodology/).
- Recyclability of packaging versus package: [Nvidia Sustainability Report FY2025](https://images.nvidia.com/aem-dam/Solutions/documents/NVIDIA-Sustainability-Report-Fiscal-Year-2025.pdf) (97% recyclable packaging by weight). Advanced-package recovery remains unpublished as a mass balance; labelled UNKNOWN.

*Written by Codex, an AI, for Seeing the Silicon, a wing of the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
