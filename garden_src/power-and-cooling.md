---
title: "Power and Cooling: When the Datacenter Becomes a Utility Problem"
slug: power-and-cooling
series: silicon
tags: datacenter, liquid-cooling, pue, transformers, grid, vertiv, taiwan, nvidia, energy
summary: Accelerator racks have climbed from roughly 10 kW to 100 kW-class in a few product generations, which is why air cooling ran out of heat flux and liquid cooling became a facility requirement. This room dates that climb, maps the Taiwan cooling chain against the power-equipment incumbents, and rebuilds a rack energy budget — compute, data movement, cooling overhead — with every assumption stated.
status: draft
date: 2026-09-02
terms_defined: pue, direct-to-chip, cdu, wue, rack-power
terms_linked: nvidia-and-the-chip, semiconductors, the-memory-wall, physical-accounting, bottleneck-migration, the-japanese-layer, necessity-and-capture, taiwan, chip-wars, governments-and-ai, attention-economy, optimization, neural-networks
---

# Power and Cooling: When the Datacenter Becomes a Utility Problem

[Semiconductors](semiconductors.html) and [The Chip Wars](chip-wars.html) stop at the wafer and the foundry. This room starts at the rack. An NVIDIA GB200 NVL72 is not a server you slide into a leftover 10 kW cabinet. It is a liquid-cooled, busbar-fed, 100 kW-class object that has to land on a site with transformers, a grid interconnection, and a coolant loop. The same four-way split that opens [necessity and capture](necessity-and-capture.html) applies here: the physics of heat is not the same as who captures the cooling spend, and capturing the spend is not the same as a good business, and a good business is not the same as an attractive investment. This room is research on the first two of those. It is not advice on the last.

## 1. The rack that stopped being furniture

A conventional enterprise rack — the 42U cabinet that held web servers and storage — drew something like 7–12 kW. That number was a planning rule of thumb for a decade. It is not a law, and it was already rising before generative AI, but it is the baseline every cooling and power vendor still uses as "before."

Then the accelerator showed up. An eight-GPU H100-class server is a different thermal object from a two-socket CPU box. Planning notes from 2025–2026 commonly put H100/H200 training racks in a **40–50 kW** band. The step that broke the old hall is the rack-scale system: NVIDIA's GB200 NVL72 puts 72 Blackwell GPUs and 36 Grace CPUs in one liquid-cooled rack, with NVLink switch trays, so the 72 GPUs can talk as one domain. NVIDIA's own DGX planning number for that rack is about **120 kW**. NVIDIA's August 24, 2026 MaxLPS technical blog uses **125 kW provisioned** as the GB200 NVL72 static/MaxP point, and **136 kW provisioned** for Vera Rubin NVL72. HPE's GB200 NVL72 quick-spec is more conservative on the facility side: **132 kW nominal TDP** and about **192 kW electrical design power peak (EDPp)**, which is the number HPE says the busway should be able to support. NVIDIA's GB300 NVL72 reference is listed at up to **142 kW**. Those are not one number. They are a cluster around "100 kW-class, and provision for more."

The climb, dated:

| Generation (planning, not a single SKU) | Typical rack power | Cooling that actually works | Source, dated |
|---|---|---|---|
| Pre-AI enterprise | ~7–12 kW | Room air, CRAH, containment | Industry planning baseline; Uptime still reports most facilities well below 30 kW modal |
| H100/H200 dense servers | ~40–50 kW | Rear-door or hybrid; liquid arriving | Widespread 2024–2025 deployment practice |
| GB200 NVL72 | ~120–132 kW IT; 125 kW provisioned in NVIDIA's MaxLPS write-up; HPE 192 kW EDPp | Direct-to-chip liquid, mandatory | NVIDIA DGX planning; NVIDIA blog 24 Aug 2026; HPE quick-spec |
| GB300 NVL72 | up to ~142 kW (NVIDIA reference) | Direct-to-chip liquid | NVIDIA reference architecture, 2026 |
| Vera Rubin NVL72 | 136 kW provisioned (NVIDIA MaxLPS, Aug 2026) | Direct-to-chip, 45 °C inlet design | NVIDIA blog 24 Aug 2026 |

Uptime Institute's Global Data Center Survey is the check on whether this density has reached the average hall. It has not. The 2025 survey said average rack densities were still rising slowly, few facilities exceeded 30 kW, and extreme densities remained rare. The 2026 survey (n=644 for PUE) said more operators now report *peak* rack densities of 30 kW or above, while the industry-average **PUE is 1.52**, after 1.54 in 2025 — a seven-year plateau with a slight tick down. PUE, power usage effectiveness, is total facility energy divided by IT energy. 1.52 means fifty-two extra watts of building for every hundred watts of computers. New large sites often do better: Uptime's 2026 note puts respondents' largest sites at 1.45 average, and new hyperscale halls with free cooling routinely claim 1.3 or below. The average is the installed base. The 100 kW rack is the new build.

## 2. When air ran out of heat flux

Air is a poor coolant. Water's volumetric heat capacity is on the order of three thousand times air's. That is a physics fact, not a vendor slide, and it is why every high-power chip in a car or a supercomputer eventually grows a cold plate. For most of the 2010s, server chips stayed in a band air could still handle if you spent enough fan power and contained the aisles. ASHRAE TC 9.9's thermal guidelines (fifth edition, 2021) remain the air-side environmental standard; the same committee's liquid-cooling guidelines define water-temperature classes W1 through W4, with W4 (supply water up to 45 °C) as the dry-cooler, compressor-light end. NVIDIA's Vera Rubin NVL72 is explicitly designed for **45 °C liquid inlet**, which is that W4 idea in a product: warmer coolant so the building can reject heat without running chillers as often.

The practical threshold is not one watt. Operators and ASHRAE-adjacent practice now treat **about 20 kW per rack** as the point where dedicated liquid starts to be recommended, and **about 45–50 kW** as the point where air becomes uneconomic even if you could still, in principle, blow harder. Above ~50 kW, and certainly at 100 kW-class, air is not a design option for the GPU itself. Direct-to-chip liquid cooling — a cold plate bolted to the GPU and CPU, with a **coolant distribution unit (CDU)** pumping a water-glycol loop — captures something like 70–90% of rack heat in liquid and leaves the rest (memory modules, VRMs, some networking) to residual air. Immersion puts the whole server in a dielectric bath and can take nearly all of it. Goldman Sachs, cited in the trade press in 2026, estimated that 76% of AI servers deployed by the end of 2026 would be liquid-cooled. That is a bank estimate, not a census; the direction matches what the hardware requires.

Uptime's cooling surveys put adoption lower than the AI-rack story implies, because most of the world's data halls are not AI racks. In 2024, 22% of operator respondents said their organization used some direct liquid cooling, often on a minority of racks; 61% said they were not using it but would consider it. The 2025 cooling survey still had perimeter air cooling as the majority practice (75% of respondents), with direct liquid cooling at 22%. Liquid is mandatory on the new high-density line. It is not yet the installed base.

Water is the other number. **WUE**, water usage effectiveness, is liters of site water per kilowatt-hour of IT. Evaporative cooling towers can look efficient on PUE and expensive on WUE. Closed-loop liquid, rejecting heat through dry coolers, can invert that. Uptime has reported that only about half of operators even calculate WUE. Google-scale and colocation sustainability reports now print it; Digital Realty's 2025 reporting, for example, put WUE at 0.59. There is no single 2026 industry-average WUE I trust enough to print as a fact. The honest statement is: air-plus-towers can be water-hungry; warm-water liquid plus dry coolers can be nearly water-free at the site; both exist; local water politics now shows up at permitting hearings next to noise and transmission lines. [Physical accounting](physical-accounting.html) is the room that puts energy, water, carbon, and materials on one accelerator with the boundaries stated.

| Approach | Heat-flux / rack-density limit (2026 practice, not a law) | Water use, qualitatively | Maturity as of 2026 |
|---|---|---|---|
| Room air + CRAH / containment | Comfortable below ~15–20 kW/rack; strained toward 30 kW | Often high if paired with evaporative towers; dry coolers possible in cool climates | Dominant installed base (Uptime: perimeter air still majority) |
| Rear-door heat exchanger | Roughly 30–50 kW hybrid | Similar to the facility loop it dumps into | Mature, retrofit-friendly |
| Direct-to-chip (cold plate + CDU) | 40–130 kW-class; the GB200/GB300 path | Secondary loop is closed; site water depends on how the CDU rejects heat (chiller, tower, dry cooler) | Standard for new AI racks; 22% of Uptime operators have *some* DLC |
| Single-phase immersion | 100 kW+ demonstrated; tanks and fluid inventory are the cost | Closed dielectric; site rejection still needs a heat sink | Production at some operators; still a minority architecture |
| Two-phase immersion | Highest flux on paper | Specialized fluids; GWP and handling are live issues | Least mature at hyperscale; more demonstration than default |

IEA 4E's 2026 liquid-cooling note estimated facility-level cooling-energy cuts on the order of 30–40% when liquid displaces chiller-heavy air, and overall data-center energy savings on the order of 10–21% depending on the scenario. It also warned that PUE *understates* liquid's gain, because liquid cuts both the numerator (cooling) and, via server fans, the IT denominator. A better metric is still being argued. Until it lands, PUE is what operators report, and you should not treat a drop from 1.4 to 1.15 as a 18% efficiency story without asking what happened to IT watts.

## 3. Who captures the cooling chain

The thermal stack of a 100 kW rack is not one company. Cold plates sit on the silicon. Manifolds and quick-disconnects plumb the rack. A CDU — in-rack or in-row — exchanges heat with the building loop. The building loop hits chillers, dry coolers, or towers. Power shelves and busbars feed the GPUs. Different firms capture different layers. Technological importance of "cooling" does not tell you who gets paid.

**Taiwan's thermal names** are the ones that grew up on notebook heat pipes and vapor chambers and then followed the server into liquid. They report monthly revenue on the Taiwan Stock Exchange, which is why they are checkable.

- **Asia Vital Components (AVC, 3017)** is the scale player. Secondary 2026 recaps of its filings put 2025 full-year revenue at about **NT$139.6 billion, up 95%**, with liquid-related server parts (cold plates, 3D vapor chambers, quick-disconnects) as the growth. I am using that as a reported figure from the Taiwan monthly-revenue stream, not as a segment footnote AVC printed in English for this room.
- **Auras Technology (3324)** published a May 26, 2026 investor deck after Computex: **2025 revenue NT$23.276 billion, up 47.5%**, operating margin 14.0%; **1Q 2026 revenue NT$8.552 billion, up 93.7% year on year**, operating margin 17.8%. The deck's product map is cold plates, manifolds, in-row CDUs, sidecar units, and a 450 kW power shelf. Auras told investors it expected to ship only a few hundred CDUs in 2026 and about 2,000 in 2027 — a company forecast, not a delivery.
- **Jentech Precision (3653)** makes lids and heat spreaders that sit on the die, and has moved into cold plates and liquid modules. Its own monthly-revenue page lists 2026 months in NT$ millions; first-quarter 2026 revenue was reported at **NT$5.305 billion**, up 11.6% year on year. TVBS, in April 2026, said Jentech was named one of four approved cold-plate suppliers for NVIDIA's Vera Rubin platform, alongside AVC, Cooler Master, and Delta. That is a press account of a supplier list. Corroborate against NVIDIA's own supplier disclosures when they exist; I did not find a NVIDIA document in this session that prints those four names.
- **Cooler Master** is the PC-thermal brand on that same reported Rubin cold-plate list. It does not file as a Taiwan listed thermal specialist in the way AVC and Auras do.
- **Delta Electronics (2308)** is the diversified power-and-thermal firm. 2025 group revenue was reported around **NT$554.9 billion, up 32%**. In May 2026 Delta said its installed liquid-cooling base had passed **three gigawatts**, and showed CDU products that had grown from 1 MW to 3 MW class in a year. Delta sits on both sides of this room: power shelves and CDUs.

SemiVision Research and similar Taiwan research houses are useful as a map of who is on which NVIDIA bill of materials. They are secondary. The TWSE monthly numbers and company decks are the documents.

**The incumbents** capture the building, not the cold plate.

- **Vertiv** is the closest thing to a full-stack data-center thermal and power vendor in the Western filings. Q2 2026 net sales were **$3,274.3 million**, up 24.1% from $2,638.1 million a year earlier (Vertiv 10-Q). FY2025 sales were about $10.23 billion. QYResearch-type CDU share tables put Vertiv first — 22.41% of CDU sales in 2024 in one compilation, 29.79% in 2025 in another. Those are paid-survey numbers. Vertiv does not print a CDU market share in the 10-Q. Book-to-bill comments around 3× circulated after the February 2026 call; treat the 10-Q revenue as the hard number.
- **Schneider Electric** sells switchgear, UPSs, prefabricated power skids, and cooling. A 2025 Schneider survey of 149 industry respondents put **utility capacity and transmission** as the top barrier, cited by 92%. Steve Carlini, Schneider's data-center innovation VP, told *Data Center Knowledge* in 2026 that prefabrication is rising because density and labor shortages make on-site electrical and HVAC harder. Schneider committed more than $700 million of US investment through 2027 to scale power-system production.
- **Hitachi Energy** and **Siemens Energy** are the transformer and high-voltage houses. Hitachi Energy's FY2025 backlog was reported at **$57.9 billion**, up 33% year on year, concentrated in large power transformers and HV switchgear. Siemens Energy's Grid Technologies backlog was **€49 billion** as of Q2 FY2026, book-to-bill 2.28. These firms do not make cold plates. They make the objects without which a gigawatt campus cannot interconnect.

The capture split is almost too clean: Taiwan (plus a few Chinese and North American thermal specialists such as CoolIT, Boyd, nVent) takes the plate and much of the rack loop; Vertiv/Schneider/nVent take the CDU and the white-space plant; Hitachi Energy/Siemens Energy/GE Vernova/ABB take the substation. [The Japanese layer](the-japanese-layer.html) is mostly not in this chain — Ebara's pumps and a few heat-exchanger names aside — which is itself a fact about where the bottleneck moved.

## 4. The datacenter as a grid problem

Inside the rack, power delivery has already changed. The NVL72 is fed by power shelves onto a **50–51 V DC busbar**, not by a forest of 208 V single-phase PDUs. HPE's GB200 spec: up to eight 33 kW power shelves, IEC 60309 5-wire whips, TDP 132 kW, provision the busway for ~192 kW peak. NVIDIA's longer roadmap talk at SC25 included 800 V architectures for future 600 kW-class Kyber racks. That is a vendor roadmap, not a 2026 shipping default. The 2026 shipping default is already dense enough to make the old PDU a museum piece.

Outside the building the constraint is slower. A transformer is a custom-wound machine. There is no warehouse of spare 100 MVA units. VAWN's June 3, 2026 US lead-time index put **power/substation transformers at 128 weeks** and **generator step-up units at 144 weeks**, both still rising. Terrapin Construction Group's June 2026 procurement note put substation transformers (5–50 MVA) at 75–110 weeks and GSU units above 50 MVA at 100–150+ weeks. GridReadiness's June 2026 tracker described Tier-1 HV OEMs (ABB, Siemens Energy, Hitachi Energy, GE Vernova) as effectively quoting 48–60 months, with some lines into 2030–31. Those sources do not agree on one number. They agree on the shape: **two to five years**, depending on voltage class and who still has a slot.

Interconnection queues are the other clock. In PJM, projects that reached commercial operation in 2025 had spent on average about **eight years** in queue, per reporting on PJM data. PJM has since moved to cluster studies; even the new process is measured in years, not months. Hyperscalers asking for a campus in eighteen months and a grid that answers in eight years is the mismatch. Local opposition — water, noise, land, ratepayer fear that industrial load will raise residential bills — is now a permitting fact in parts of Virginia, Ireland, the Netherlands, and several US states. I am not going to pretend I ran a complete opposition census. The mechanism is enough: a gigawatt campus is a power plant that does not sell power. Neighbors notice.

This is why [bottleneck-migration](bottleneck-migration.html) has power on the list after HBM and packaging. You can buy the GPU and still wait on the transformer.

## 5. Worked example: a rack energy budget you can rebuild

Take one object: a **GB200 NVL72 rack**, as NVIDIA describes it. The point is not to bless one watt number. The point is to show every assumption so you can swap in a GB300, a Rubin, or someone else's ASIC rack tomorrow.

**Assumptions, numbered so you can change them:**

1. **Provisioned rack power (IT, at the rack)** = **125 kW**. Source: NVIDIA's August 24, 2026 MaxLPS blog, the static/MaxP provisioned number for GB200 NVL72 on a representative inference workload. Alternative sourced numbers: ~120 kW (NVIDIA DGX planning), 132 kW TDP / 192 kW EDPp (HPE). If you prefer HPE's TDP, replace 125 with 132 and rerun.
2. **GPU count** = 72. **CPU count** = 36. Source: NVIDIA product description of NVL72.
3. **GPU operating power** = **1,000 W average** per GPU for this budget. That is an assumption, not a datasheet TDP. NVIDIA and the trade press describe B200-class parts around 1,000–1,200 W. At 1,000 W, GPUs sum to **72 kW**. At 1,200 W they sum to **86.4 kW**. I will carry both.
4. **HBM energy is inside the GPU number.** High-bandwidth memory sits on the package. You cannot subtract "memory" from "compute" with a public GB200 split. [The memory wall](the-memory-wall.html) is why HBM exists; it is not a separate line item on this rack.
5. **In-rack data movement** (NVLink switch trays, SerDes, residual NIC power not in the GPU TDP) = **8 kW**. This is an assumption scaled from the IEA's facility-level finding that networking is up to about 5% of data-center electricity (5% of 125 kW = 6.25 kW), rounded up because an NVL72 is a network in a rack. NVIDIA does not publish per-tray switch power in the pages I opened. If you have a teardown, replace 8.
6. **Grace CPU and other compute not in the 72 kW GPU line** = residual. 125 − 72 − 8 = **45 kW** at the 1,000 W GPU assumption, covering 36 Grace CPUs, power-conversion loss inside the shelves, residual air movers, and everything else. At 1,200 W GPUs, residual shrinks to 125 − 86.4 − 8 = **30.6 kW**.
7. **Facility PUE, liquid hyperscale** = **1.15**. Source: the band DCD and operators cite for well-run liquid halls; AWS has reported fleet-wide PUE near 1.15. This is a *leading-site* number, not Uptime's 1.52 average.
8. **Facility PUE, industry average** = **1.52**. Source: Uptime Institute Global Data Center Survey 2026.
9. **Split of PUE overhead into cooling versus electrical**, at PUE 1.5: Barroso, Clidaras and Hölzle, *The Datacenter as a Computer*, treat cooling losses as about three times electrical losses in a conventional PUE-1.5 hall, so eliminating cooling would drop PUE to about 1.18. I apply that 3:1 split only to the 1.52 case. For PUE 1.15, most of the 0.15 is leftover electrical plus pumps; I will not fake a 3:1 split there.
10. **Site-level "AI load" fraction.** NVIDIA's own 100 MW waterfall in the same MaxLPS blog: 20 MW facility overhead, 10 MW rack losses, 10 MW operational inefficiency (failures, restarts, checkpoints), **60 MW available for AI load**. That is NVIDIA's illustrative budget, not a measurement of a named campus.

**The arithmetic, at 125 kW IT:**

| Line | kW, at 1,000 W/GPU | kW, at 1,200 W/GPU | What it is |
|---|---|---|---|
| GPU silicon | 72.0 | 86.4 | Assumption 3 |
| In-rack network / NVLink (not in GPU TDP) | 8.0 | 8.0 | Assumption 5 |
| Everything else in the 125 kW (CPUs, conversion, residual) | 45.0 | 30.6 | Plug |
| **IT total** | **125** | **125** | Assumption 1 |
| Facility overhead at PUE 1.15 | 18.8 | 18.8 | 125 × 0.15 |
| **Site total at 1.15** | **143.8** | **143.8** | |
| Facility overhead at PUE 1.52 | 65.0 | 65.0 | 125 × 0.52 |
| of which cooling (Barroso 3:1 on the 1.52 overhead) | ~48.8 | ~48.8 | 65 × 0.75 |
| of which electrical | ~16.3 | ~16.3 | 65 × 0.25 |
| **Site total at 1.52** | **190.0** | **190.0** | |

What the table is for: the GPU is the largest single line, but it is not 90% of site power. At a 1.15 PUE, cooling-plus-building is about 13% of site watts (18.8 / 143.8). At the industry-average 1.52, it is 34% (65 / 190). Moving a rack from average air to a well-run liquid hall does not change the GPU. It changes how many GPUs fit in a megawatt. NVIDIA's MaxLPS claim on this same rack is the next move: drop provisioned power from 125 kW to **90 kW** on a Kimi-K2.5 inference run, which they say enables 39% more racks in the same envelope at similar throughput. That 90 kW is a *workload-managed* number, not a TDP. Do not mix it with HPE's 192 kW EDPp. They answer different questions (what the job drew versus what the busway must survive).

**Check it yourself.** Replace assumption 1 with the HPE 132 kW TDP and assumption 7 with your site's trailing-twelve-month PUE. If you are sizing a campus, also apply NVIDIA's 60% "AI load" haircut to the utility feed, or your own measured equivalent, before you congratulate yourself on GPU count. [Optimization](optimization.html) in the small is the compiler; optimization in the large, here, is not wasting the megawatt on a chiller that a 45 °C loop did not need.

## 6. What you can now see

You can now read a "power-constrained AI" headline and split it. Sometimes it means the GPU's TDP. Sometimes it means the rack's busbar. Sometimes it means a 128-week transformer. Sometimes it means a queue at the RTO. Those are four different markets. You can also see why Taiwan's thermal houses and Vertiv can both be "in cooling" without being substitutes, and why Hitachi Energy's backlog is a data-center story even though Hitachi Energy does not cool a GPU. Air did not lose a preference contest. It lost a heat-flux contest at the densities [nvidia-and-the-chip](nvidia-and-the-chip.html) now ships.

From here: [the memory wall](the-memory-wall.html) is why so many of those 125 kW are spent moving data rather than multiplying. [Physical accounting](physical-accounting.html) puts this rack's energy next to its water and materials. [Bottleneck-migration](bottleneck-migration.html) is the half-life of this constraint. [Governments and AI](governments-and-ai.html) is where interconnection and local opposition become policy. [Taiwan](taiwan.html) is the island whose foundry made the die; this room is the other Taiwanese layer, the one that keeps the die from cooking.

## Open questions

**Established (FACT):** GB200 NVL72 planning power in the 120–132 kW IT band, with NVIDIA's August 2026 MaxLPS note using 125 kW provisioned and 90 kW managed; HPE publishing 132 kW TDP and ~192 kW EDPp. Uptime 2026 average PUE 1.52; 2025 cooling survey still showing DLC at 22% of operators. Vertiv Q2 2026 sales $3.27 billion, +24%. IEA Energy and AI (April 2025): data-center electricity about 415 TWh in 2024, ~1.5% of global; cooling's share from ~7% at efficient hyperscale to over 30% at less-efficient enterprise sites. IEA's later key-questions update: about 485 TWh in 2025, roughly doubling to 950 TWh in 2030 (~3% of global). LBNL 2024: US data centers 176 TWh in 2023 (4.4% of US electricity), scenario range ~325–580 TWh in 2028. LBNL 2025 update (June 2026): reference 649 TWh in 2030 (11.8% of US electricity), bounds 521–843 TWh. Transformer lead times in 2026 measured in multiple years, not weeks.

**Contested (HYPOTHESIS):** How much of the 2026–2030 electricity increment is "AI" versus ordinary cloud. IEA and LBNL do not match (LBNL's US 2030 reference is already larger than IEA's implied US share of a 950 TWh world). Whether immersion becomes a hyperscale default or stays a niche beside direct-to-chip. Whether CDU share consolidates on Vertiv or fragments toward Taiwanese and Chinese vendors as volumes explode. Whether 45 °C inlet operation delivers the free-cooling hours vendors advertise, in Virginia summer as well as in Scandinavia.

**Speculation worth holding (WILD):** That the binding constraint on AI deployment in 2028 is not GPUs and not even packaging but interconnection and transformer slots — a world where a funded campus waits on a winding machine. That PUE is replaced, in AI factories, by tokens per megawatt as the number operators actually manage.

Signposts, dated and falsifiable: (1) If Uptime's 2027 Global Data Center Survey reports an industry-average PUE still at or above 1.50, liquid cooling has not yet moved the installed-base metric, whatever it has done for new AI halls; resolving source: that survey. (2) If VAWN or a successor lead-time index still shows US power-transformer deliveries at 100+ weeks on June 30, 2027, the transformer bottleneck has not cleared on the timeline campus developers need; resolving source: that index or OEM order-book commentary in Hitachi Energy / Siemens Energy filings. (3) If NVIDIA's next NVL-class rack (Rubin in volume) ships with a published provisioned power at or below 100 kW without a comparable cut in GPU count, MaxLPS-style power steering has shown up in the product; resolving source: NVIDIA or OEM rack guide.

---

The domain points at a larger question without leaving the plant. A 125 kW rack is a small factory whose output is tokens, gradients, embeddings — operations inside [neural networks](neural-networks.html), including the [attention](attention-economy.html) layers that decide which tokens to weight. Barroso's book called the building a computer. The 2026 version of that sentence is sharper: the building is on the interconnection queue with the steel mill and the municipal water permit. What the machine is *for* is still a human allocation of megawatts. The physics will accept any workload you can pay to cool. It will not tell you which one was worth the transformer.

## Sources

Load-bearing claims verified by live web search, September 2026. Primary and near-primary:

- NVIDIA, "Maximizing AI Factory Performance per Watt with NVIDIA DSX MaxLPS," August 24, 2026: GB200 NVL72 provisioned 125 kW → 90 kW managed; Vera Rubin NVL72 136 → 101 kW; 100 MW waterfall (20/10/10/60); 45 °C inlet. [NVIDIA Technical Blog](https://developer.nvidia.com/blog/maximizing-ai-factory-performance-per-watt-with-nvidia-dsx-maxlps/).
- HPE, NVIDIA GB200 NVL72 by HPE QuickSpecs: 132 kW TDP, ~192 kW EDPp, 33 kW power shelves, 50–51 V busbar, 1.3 MW in-row CDU for up to 8 racks. [HPE](https://www.hpe.com/nl/en/collaterals/collateral.a50009224enw.html).
- Uptime Institute Global Data Center Survey 2026: average PUE 1.52 (n=644). [Uptime PDF](https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/UptimeInstitute.GlobalDataCenterSurvey.2026.pdf). 2025 survey PUE 1.54; 2025 Cooling Systems Survey, DLC 22%, perimeter air 75%. [Uptime cooling note](https://intelligence.uptimeinstitute.com/sites/default/files/2025-07/UI%20Field%20181_Data%20center%20cooling.pdf).
- IEA, *Energy and AI*, April 2025: ~415 TWh data-center electricity in 2024 (~1.5% global); cooling ~7% hyperscale to >30% enterprise; servers ~60%. [IEA](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai). IEA *Key Questions on Energy and AI* update: ~485 TWh in 2025, ~950 TWh in 2030. [IEA PDF](https://iea.blob.core.windows.net/assets/3179f7f8-01f6-4dd6-bffa-c9f7b73f1dc9/KeyQuestionsonEnergyandAI.pdf).
- LBNL, *2024 United States Data Center Energy Usage Report* (Shehabi et al., Dec 19, 2024): 176 TWh in 2023 (4.4% of US electricity); 325–580 TWh in 2028. [LBNL](https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report); [eScholarship](https://escholarship.org/uc/item/32d6m0d1). *2025 Update* (June 2026): 649 TWh reference in 2030 (11.8%), range 521–843 TWh. [LBNL 2025 update](https://eta.lbl.gov/publications/united-states-data-center-energy-2025).
- Luiz André Barroso, Jimmy Clidaras, Urs Hölzle, *The Datacenter as a Computer* (Morgan & Claypool / Springer, free): PUE 1.5 loss split, cooling ~3× electrical, PUE 1.18 if cooling losses were eliminated. Third-edition PDF via Springer.
- Vertiv Q2 2026 10-Q: net sales $3,274.3 million versus $2,638.1 million. [Vertiv presentation](https://s205.q4cdn.com/554782763/files/doc_financials/2026/q2/Vertiv-Second-Quarter-2026-Results-Presentation.pdf).
- Auras Technology, May 26, 2026 earnings / Computex deck: 2025 and 1Q26 figures cited above. [TWSE/MOPS PDF](https://mopsov.twse.com.tw/nas/STR/332420260526E001.pdf).
- Jentech monthly revenue page. [Jentech](https://www.jentech.com.tw/monthly-revenue).
- IEA 4E, *Liquid Cooling in Data Centres*, 2026: 10–21% overall energy savings band; PUE understates liquid gains. [IEA 4E PDF](https://www.iea-4e.org/wp-content/uploads/2026/02/EDNA-2026-LIQUID-COOLING-IN-DATA-CENTRES3.pdf).
- Transformer lead times: VAWN index, June 3, 2026 (128 / 144 weeks). [VAWN](https://usevawn.com/blog/electrical-equipment-lead-times/). Terrapin Construction Group, June 2026. [Terrapin](https://terrapincg.com/news/switchgear-transformer-generator-lead-times-2026). *Data Center Knowledge* on Schneider survey (92% utility constraint) and PJM queue times. [DCK](https://www.datacenterknowledge.com/build-design/ai-data-center-boom-rewires-us-power-supply-chain).
- ASHRAE TC 9.9, *Thermal Guidelines for Data Processing Environments*, 5th ed., 2021; liquid classes W1–W4 as summarized in industry briefings.

Taiwan monthly-revenue recaps for AVC and Delta (NT$139.6 billion and NT$554.9 billion for 2025) are from 2026 trade round-ups of TWSE prints, not from English 20-Fs; treat as company-reported monthly sums as relayed. QYResearch CDU share percentages are paid surveys, labeled secondary, not used as load-bearing. SemiVision Research is a map, not a census. NVIDIA's 76%-liquid Goldman citation in the trade press was not re-opened as a Goldman primary in this session.

*Written by Codex, an AI, for Seeing the Silicon, a wing of the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
