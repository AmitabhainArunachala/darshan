---
title: "Bottleneck Migration: What Becomes Scarce Next"
slug: bottleneck-migration
series: silicon
tags: bottlenecks, hbm, advanced-packaging, power, transformers, interconnect, optics, capital-cycle
summary: AI demand does not create one permanent shortage. It moves pressure through memory, packaging, power, and interconnect, while capital and substitution work on each constraint at different speeds.
status: draft
date: 2026-09-02
terms_defined: bottleneck-migration, constraint-half-life, co-binding, optical-metrology, optical-interconnect, photonic-computing
terms_linked: the-memory-wall, advanced-packaging, power-and-cooling, the-capital-cycle, necessity-and-capture, forecasting, attention-economy, semiconductors, nvidia-and-the-chip, taiwan, chip-wars, physical-accounting
---

# Bottleneck Migration: What Becomes Scarce Next

You are standing downstream of [the memory wall](the-memory-wall.html), [advanced packaging](advanced-packaging.html), and [power and cooling](power-and-cooling.html). Each room explains a constraint. This room asks a different question: once money attacks that constraint, where does scarcity move next? The map of who can make the chips lives in [the chip wars](chip-wars.html) and [semiconductors](semiconductors.html); this room is the clock those maps do not keep.

## 1. The scarce thing is a moving target

In ecology, a resource is something organisms need, a niche is the set of conditions in which they can live, and succession is the change in which organisms occupy a place after the conditions change. Those words are useful here if we keep their teeth.

AI demand expands. Accelerator demand follows: the processors described in [Nvidia and the chip](nvidia-and-the-chip.html) are only as numerous as the scarce layer they sit on. High-bandwidth memory, or **HBM**, is stacked DRAM placed beside a processor so data can move across a wide interface, and it becomes scarce. Scarcity raises margins and secures customer commitments. Producers add wafer capacity, packaging lines, and equipment. Supply grows, but the system does not return to its old state. The newly available accelerators now need more advanced packages, more rack power, and more network bandwidth. The niche has changed. A different resource can bind.

Call that **bottleneck migration**: the binding constraint moves because demand, design, capital, and substitution alter the system around it. The move is rarely clean. HBM did not cease to matter when packaging tightened. Packaging did not stop binding when grid access became urgent. Constraints **co-bind** when two or more limited resources jointly cap output and loosening either one alone is not enough.

That distinction protects you from a common story: “HBM was last year; transformers are this year.” The dated record is messier. In December 2023 Micron said HBM3E used roughly twice the die area and more than twice the wafer supply per bit of comparable DDR5. By June 2024 it put the wafer-supply ratio near three times and said its HBM output for calendar 2024 and 2025 was sold out. In April 2026 TSMC still called advanced packaging very tight. In July 2026 it said packaging capacity was limiting customer growth. These resources overlapped.

This is also where the wing's anchor sentence earns its place: **technological importance ≠ economic capture ≠ business quality ≠ investment attractiveness.** A component can bind production while a supplier captures little of the value, perhaps because customers qualify a substitute quickly or because new capacity arrives before the supplier earns back its plant. [Necessity and capture](necessity-and-capture.html) separates those steps. This room supplies the clock.

## 2. The migration, with the receipts left visible

The path below is not a claim that each stage replaced the last. It is a dated account of what management teams could not procure fast enough, and when.

**HBM, 2023–24.** SK hynix said in January 2024 that its planned 2024 HBM volume was already sold out. Micron said in June 2024 that its calendar-2024 and calendar-2025 output was sold out, with most 2025 pricing already contracted. Those are company statements, not an audit of the whole market, but they are stronger than a product launch: both connect scarcity to allocation and contracts. The physical reason matters. HBM consumes more leading-edge DRAM wafer area per delivered bit than ordinary memory, then adds through-silicon vias, thinning, stacking, and yield loss. A “memory bit” is not a fungible unit once the package changes.

Capital responded. SK hynix announced in April 2024 that it would spend more than KRW20 trillion over time on its M15X fab, with completion and early mass production targeted for November 2025. Micron, Samsung, and SK hynix also expanded HBM assembly and base-die capability. The implied half-life looked like 18–24 months. It was too short. Micron's June 2026 remarks still described tight supply during the HBM4 ramp. HBM4 uses a custom logic base die and raises qualification demands, so a new product generation consumed part of the capacity gain.

**Advanced packaging, 2024–25.** CoWoS, TSMC's family for mounting a processor and HBM on a large interposer, became the package-equivalent constraint. In its April 2024 earnings call, TSMC said it expected CoWoS capacity to more than double during 2024 and still be insufficient. In July 2024 it said the combined CoWoS variants had more than doubled from 2023 to 2024 and that it wanted another doubling or more in 2025. The company hoped tightness might ease in 2026.

That hope is a useful failed forecast. In October 2025 TSMC still described both front-end and back-end AI capacity as very tight. In April 2026 it said advanced packaging remained very tight and that it was using outsourced assembly-and-test partners. In July 2026 it said the gap was still constraining customers. Capital did arrive. Demand and package area moved too. TSMC's 2024 annual report says a 3.5-reticle CoWoS-L package entered production that year and development began on a 5.5-reticle version. A reticle is the maximum image field printed in one lithography exposure; larger multiples mean fewer packages from a wafer-equivalent and harder assembly.

**Power and transformers, 2025–26.** Once operators could assemble more accelerators, the scarce unit increasingly became an energized megawatt: not annual electricity in the abstract, but firm power at the required site, date, voltage, and reliability. That megawatt is also a physical account — energy, water, carbon — which [physical accounting](physical-accounting.html) treats as a ledger rather than a slogan. Much of the leading-edge packaging still happens on [Taiwan](taiwan.html), so a site-level power delay there is not a local inconvenience. The IEA's *Energy and AI* report, published in 2025, estimated global data-center electricity use at about 415 TWh in 2024 and around 945 TWh in 2030 under its base case. It also estimated that about 20% of planned data-center capacity risked delay from grid constraints, with new transmission commonly taking four to eight years.

Transformers sit inside that delay. A transformer changes voltage so power can move from a grid into a campus and then into equipment. The US Department of Energy reported in a 2026 webinar, using 2024 evidence, that distribution-transformer lead times had risen from three to six months in 2019 to one to two years or longer in 2024; large power transformers could take three to four years. The same webinar included a manufacturer saying some distribution lead times had recently normalized. There is no honest single “transformer lead time.” Voltage class, core steel, winding, specification, factory, and customer all matter.

**Interconnect, 2025–26 and after.** More processors in a rack are useful only if data can reach them. At short distances, copper is cheap, serviceable, and efficient. Nvidia's 2024 Open Compute contribution for a GB200 NVL72 rack described more than 5,000 copper cables, about 100 pounds of structural reinforcement, and roughly 6,000 pounds of connector mating force. That is copper succeeding so hard that its mechanics become a constraint.

As lane speed rises, reach shrinks. The Optical Internetworking Forum's 224-gigabit electrical specification targets long-reach channels of about one metre, down from roughly two metres for the preceding 112-gigabit class. Retimers, which receive and regenerate an electrical signal, extend the niche at the cost of power and latency. Active electrical cables put that electronics in the cable. Pluggable optical modules move the conversion to the switch face. Co-packaged optics moves optical engines beside the switch silicon. None is “the winner” at every distance.

## 3. Three kinds of optics that should never share a forecast

The word *photonic* makes three industries sound like one. They have different jobs, customers, failure modes, and maturity.

| Industry | What the photons do | Maturity as of Q2 2026 | Evidence that resolves maturity | Hype density |
|---|---|---|---|---|
| **Optical metrology** | Inspect patterns, dimensions, and overlay during manufacturing | Production infrastructure | KLA's FY2025 filing lists optical inspection and metrology product families; ASML's YieldStar tools feed measurements back into volume-production correction | Moderate; shipment and fab-use evidence exist |
| **Optical interconnect** | Transport bits between chips, boards, racks, or buildings | Pluggable optics are mature; linear optics and CPO are emerging by reach and architecture | OIF implementation agreements, Ethernet Alliance plugfests, named operator deployments, field failure rates | High around CPO |
| **Photonic computing** | Perform arithmetic or matrix operations in light | Research and prototype | Peer-reviewed system results including converters, control, memory, precision, and end-to-end energy | Very high; kernel demonstrations often omit system costs |

Optical metrology is photons inspecting. KLA reports commercial optical inspection across wafers, reticles, and advanced packaging. ASML says its YieldStar optical metrology operates in production lines. It is mature without being finished: NIST's August 2026 review of EUV scatterometry says fast, non-destructive optical methods still struggle with sub-10-nanometre and three-dimensional structures, so fabs combine them with electron-beam measurements.

Optical interconnect is photons transporting. Fibre already carries data between buildings and across many racks. The live question is how near the switch or processor to perform electrical-to-optical conversion. The OIF published a 3.2-Tb/s co-packaged module agreement in March 2023 and external-laser agreements in 2023 and 2025. Standards prove that interfaces can be specified. They do not prove mass adoption.

Photonic computing is photons computing. A 2023 *Nature Reviews Physics* review makes the hard point: an optical advantage depends on combining several physical benefits while avoiding conversion, memory, control, noise, and programmability costs. A 2024 review in *Light: Science & Applications* still lists compute density, nonlinearity, scalability, and practical applications as open problems. A photonic multiplier can be real while a useful photonic computer remains absent.

Co-packaged optics, or **CPO**, is the densest marketing environment in this industry in 2026. Broadcom reported in March 2024 that it had delivered its 51.2-Tb/s Bailly CPO system to customers and claimed 70% lower optical-interconnect power. Nvidia announced CPO switches in March 2025 with claims of 3.5 times lower power and ten times higher resiliency; in August 2026 it said systems were “arriving” at AI factories. Those statements corroborate shipment or availability only as the companies define them. They do not disclose fleet volume, named operator acceptance, uptime, repair practice, or independently measured energy. A press release corroborates only itself.

## 4. A bottleneck table with clocks attached

A **constraint half-life** is the date by which capital, learning, or substitution is expected to remove about half the shortage pressure. It is not a law of nature. It is a forecast that must name its resolving evidence. A bottleneck without a half-life is not an analysis.

| Constraint | Binds under which scenario? | Half-life estimate as of Q2 2026 | Substitutes and maturity |
|---|---|---|---|
| HBM wafer area, stacking, and qualification | Accelerator demand grows faster than HBM bits per wafer; HBM4 raises wafer and base-die intensity | **UNKNOWN.** The early 18–24 month estimate was falsified by tightness still reported in June 2026; product intensity and private long-term agreements hide clearing conditions | DDR/LPDDR and GDDR are mature but not bandwidth-equivalent; smaller models and more recomputation are mature workload trade-offs; custom HBM is emerging |
| CoWoS package-equivalent slots | Large GPU-plus-HBM packages grow faster than usable interposer, bonding, substrate, and test output | **UNKNOWN.** Two announced doubling cycles did not close the gap by July 2026; TSMC withholds absolute variant-level output and package size keeps changing | CoWoS-L/R are product-specific; OSAT split processing is ramping; Intel EMIB is mature for compatible designs; panel-scale CoPoS is a pilot with production described by TSMC as years away |
| Energized power, grid connection, transformers | Large campuses cluster in regions where firm capacity and equipment cannot arrive at the requested date | Transformers plausibly ease **2027–29** where factory expansion lands; site-specific grid half-life **UNKNOWN**, often 2030+ when new transmission is required | Powered-site relocation is mature but scarce; onsite generation and flexible load use mature components with fuel and regulatory limits; storage shifts time but does not create annual energy |
| Copper reach and signal integrity | 224G and later lanes must cross longer board, rack, or row distances than passive copper can support | The physical reach limit **does not dissolve**. The architecture migrates. CPO adoption half-life is **UNKNOWN** until field volume, reliability, and interoperability appear | Retimers, active electrical cable, and pluggable optics are mature; linear pluggable optics are emerging; CPO is early deployment by vendor report |

Notice the discipline in the last row. Capital cannot repeal channel loss. It can fund a different medium, shorter traces, better encoding, or more regeneration. Sometimes the bottleneck's half-life is really the time required to redesign the system around it.

## 5. A decision tree: which world are you in?

Start with observed delivery, not a theme.

1. **Is HBM allocation still fixed before the production year begins?** Read the three memory makers' quarterly filings and transcripts. If all three report sold-out output or multiyear allocation through 2027, you are still in the HBM-constrained world. If contract duration shortens, inventory rises, and bit shipments grow faster than accelerator demand for two quarters, move one branch down.
2. **Do package-equivalent slots, not HBM stacks, limit shipments?** Read TSMC's calls and the assembly-and-test firms' utilization. “Capacity doubled” is not enough. Look for the demand gap closing, lead times falling, and large-package utilization below full load. If TSMC still says packaging limits customer growth, packaging co-binds.
3. **Can a customer energize the rack on the requested date?** A utility service agreement and transformer delivery matter more than national annual generation. If projects possess chips but delay commissioning for substations, transmission, or turbines, you are in the power world.
4. **Is network scale-up performance degrading before compute is full?** Compare job completion and collective-communication time across cluster size, then inspect cable reach and switch power. If active copper and pluggable optics meet the distance and serviceability budget, CPO is not yet required. If operators accept CPO in named fleets with measured uptime and lower wall-plug energy, the branch changes.

Put dates beside the signposts. The July 2024 TSMC statement “tightness may ease in 2026” looked reasonable then. The April and July 2026 statements falsified it. A decision tree becomes useful only when it is allowed to embarrass its earlier branch.

## 6. Worked example: can published CoWoS capacity cover accelerator demand?

Here is a check you can rerun in a spreadsheet. It does not produce a magic capacity number. It shows exactly which unknown controls the answer.

KGI's May 27, 2024 hardware report estimated TSMC CoWoS capacity at 13,000 wafer starts per month in Q4 2023 and 40,000 in Q4 2024. The same report forecast 4.0 million Nvidia AI-GPU shipments during 2024. These are analyst estimates, not TSMC disclosure. We will use them as scenario inputs.

**Step 1: approximate average 2024 capacity.** Assume a linear ramp from 13,000 to 40,000 wafers per month:

`(13,000 + 40,000) / 2 = 26,500 wafers per month`

`26,500 × 12 = 318,000 wafer-equivalents in 2024`

**Step 2: allocate a share to Nvidia.** JPMorgan research relayed by TrendForce in 2023 estimated Nvidia held about 60% of TSMC's CoWoS allocation. Hold that share constant only for the exercise:

`318,000 × 0.60 = 190,800 Nvidia wafer-equivalents`

**Step 3: solve for the needed output per wafer-equivalent.** Divide the 4.0 million shipment forecast by the capacity allocated to Nvidia:

`4,000,000 / 190,800 = 21.0 good accelerator packages per wafer-equivalent`

**Step 4: test the unknown.** If the mixed production line yields 15 good packages per reported wafer-equivalent, supply is `190,800 × 15 = 2.86 million`. At 20 it is 3.82 million. At 22 it is 4.20 million. The conclusion flips between 20 and 22.

That packages-per-wafer-equivalent number is not public. It bundles interposer area, edge loss, process yield, CoWoS-S/L/R mix, rework, and what the analyst meant by a “wafer.” Blackwell-era packages also use larger interposers than earlier products. A report may count interposer wafer starts, completed packages, or mixed tool capacity without saying which.

So the result is not “TSMC could make 4.20 million units.” The result is: **published data in May 2024 required at least 21 good packages per allocated wafer-equivalent for the two analyst forecasts to coexist.** Anyone claiming a precise surplus or deficit must supply the hidden denominator. You can update the three yellow cells — monthly capacity, allocation share, and good packages per wafer-equivalent — when better evidence arrives.

## 7. Pricing power moves differently from physics

The [capital cycle](the-capital-cycle.html) starts when high returns attract capacity. HBM illustrates why you should follow both the resource and the contract. A memory maker can secure pricing before new supply lands. A packaging foundry can ask customers for long commitments. A transformer maker can carry a large backlog. Those are signals of capture, but the half-lives differ.

Substitution can move capture before it removes scarcity. An outsourced packaging partner may perform only part of the flow while TSMC keeps the scarce integration step. A retimer vendor may earn more because copper remains in the rack, even if optical headlines dominate. A utility may possess generation capacity yet lack a transmission path to the site. “Exposure to the bottleneck” is not one economic position.

This is research and education, not advice. The practical exercise is to write four columns before you form a company view: physical constraint, measurable signpost, half-life, and capture mechanism. If one is blank, the story is incomplete. If the half-life says UNKNOWN, name what would make it known.

## 8. What you can now see

You can now read a shortage claim as a dated state, not a permanent identity. HBM tightened because stacked memory consumed unusually large wafer and packaging resources. CoWoS expanded twice and still co-bound because packages grew and demand outran the ramp. Power then exposed a different clock measured in transformers and transmission, while faster lanes shortened copper's usable reach.

You can also keep three optical industries apart. Optical metrology already measures production. Optical interconnect already transports data, though CPO's place inside the switch is still being tested. Photonic computing remains a systems research question. A single word does not give them a shared maturity.

From here, [the memory wall](the-memory-wall.html) explains why bandwidth has value, [advanced packaging](advanced-packaging.html) shows what those wafer-equivalents physically contain, and [power and cooling](power-and-cooling.html) follows the energized megawatt into racks and grids. [Physical accounting](physical-accounting.html) asks what that megawatt, and the chip it feeds, costs in energy, water, carbon, and materials. [Forecasting](forecasting.html) gives you the scoring discipline for the dates in the table. The [attention economy](attention-economy.html) is why shortage stories travel faster than half-lives.

## Open questions

**Established (FACT):** HBM consumed materially more wafer supply per delivered bit than conventional DRAM in Micron's 2023–24 disclosures. TSMC more than doubled CoWoS capacity in 2024, targeted another doubling in 2025, and still reported a gap in July 2026. Electrical-channel reach falls as lane rates rise; retimers and optics trade reach against power, cost, and serviceability. These are dated observations, not forecasts.

**Contested (HYPOTHESIS):** The next dominant constraint is energized power rather than HBM or packaging. Three falsifiers resolve it: if Micron, Samsung, and SK hynix still allocate substantially all HBM output more than a year ahead in their **Q2 2027** filings, memory still co-binds; if TSMC says in its **Q4 2027** call that large-package capacity no longer limits customer growth and OSAT utilization confirms it, packaging has weakened; if the IEA's **2027 update** and named utility interconnection data show planned data-center capacity commissioning without grid delay, the power hypothesis weakens. The resolving sources are producer filings, TSMC transcripts, utility service records, and IEA updates, not component launch releases.

**Speculation worth holding (WILD):** CPO becomes the binding integration layer rather than a broad substitute. Treat it as false unless, by **December 2027**, at least two independent operators disclose named production fleets, unit scale, twelve-month uptime, repair practice, and measured wall-plug energy against pluggable optics. Treat the opposite speculation — copper plus retimers keeps most in-rack links — as false if OIF's **2027–28** interoperability events show multi-vendor CPO at production error rates and operators remove rather than add service spares. Broadcom and Nvidia releases can nominate systems for checking; they cannot resolve the claim.

---

An ecology is not a list of organisms. It is a record of who can use which resource, what arrives after disturbance, and what the changed environment permits next. Capital systems deserve the same attention. The revealing object is not the component with the loudest shortage story. It is the moving edge where a physical limit, a production niche, and a human decision about what to build meet. Follow that edge long enough and you see what industrial attention really is: the choice of which constraint receives years of work, land, material, and power, and which desired uses wait outside it.

## Sources

Load-bearing claims were opened and checked live on September 2, 2026. Company releases are identified as company reports; their performance claims are not independent corroboration.

- HBM supply intensity and allocation: [Micron FYQ1 2024 prepared remarks, December 20, 2023](https://investors.micron.com/static-files/4e2b9359-c174-49b6-9c68-2b938b3c33d2); [Micron FYQ3 2024 remarks, June 26, 2024](https://investors.micron.com/static-files/4550f98c-1054-4847-a929-c17d520a0564); [Micron FYQ3 2026 remarks, June 24, 2026](https://investors.micron.com/static-files/631b1a32-5537-46ae-8f40-82e42fc79dfe); [SK hynix HBM interview, January 2024](https://news.skhynix.com/en/new-leadership-spotlight-vice-president-kitae-kim-head-of-hbm-sales-marketing/); [SK hynix M15X announcement, April 24, 2024](https://news.skhynix.com/en/sk-hynix-to-produce-dram-from-m15x-in-cheongju/).
- TSMC's relative CoWoS expansions and persistent gap: [Q1 2024 transcript](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2024-04/34ff75e23e53246302ce3a8d90d0423c57c6b120/TSMC%201Q24%20Transcript.pdf); [Q2 2024 transcript](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2024-08/5122725a56670882d777a8e8bfe0ed247cc55330/TSMC%202Q24%20Transcript.pdf); [Q1 2025 transcript](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-04/7630274eecc1197a4e3ea6a415f44a47204fe10a/TSMC%201Q25%20Transcript.pdf); [Q3 2025 transcript](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-10/6860312f04fd291d0f26b46c1234f84e6332717e/TSMC%203Q25%20Transcript.pdf); [Q1 2026 transcript](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-04/3cef85204275f94fd111485cfdf4adb3c0263c45/TSMC%201Q26%20Transcript.pdf); [Q2 2026 transcript](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/547d1696765e05ce3adb81c108ce1c8c1682b80c/TSMC%202Q26%20Transcript.pdf); [TSMC 2024 annual report](https://investor.tsmc.com/sites/ir/annual-report/2024/2024-Annual%20Report-E.pdf).
- The worked example uses analyst estimates, not TSMC disclosure: [KGI Taiwan IT Hardware, May 27, 2024](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/2024/01/it-hardware_27052024.pdf) and [TrendForce's relay of the allocation estimate, July 24, 2023](https://www.trendforce.com/news/2023/07/24/news-nvidia-reportedly-expands-cowos-orders-by-20-with-tsmc-expected-to-double-capacity-by-year-end/). TSMC discloses relative growth but not the absolute package-equivalent denominator.
- Power and grid timing: [IEA, *Energy and AI*, 2025 executive summary](https://www.iea.org/reports/energy-and-ai/executive-summary) and [AI and energy security chapter](https://www.iea.org/reports/energy-and-ai/ai-and-energy-security); [LBNL, *2024 United States Data Center Energy Usage Report*](https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report.pdf); [US DOE distribution-transformer webinar transcript, 2026](https://www.energy.gov/oe/distribution-transformer-webinar-text-alternative); [US DOE large power transformer report, July 2024](https://www.energy.gov/sites/default/files/2024-10/EXEC-2022-001242%20-%20Large%20Power%20Transformer%20Resilience%20Report%20signed%20by%20Secretary%20Granholm%20on%207-10-24.pdf).
- Copper and interoperability: [Nvidia's GB200 NVL72 Open Compute contribution, 2024](https://developer.nvidia.com/blog/nvidia-contributes-nvidia-gb200-nvl72-designs-to-open-compute-project/); [OIF implementation agreements](https://www.oiforum.com/technical-work/implementation-agreements-ias/); [OIF CEI-224G framework](https://www.oiforum.com/wp-content/uploads/OIF-FD-CEI-224G-01.0.pdf); [Ethernet Alliance 2025 high-speed networking plugfest results, March 31, 2026](https://ethernetalliance.org/blog/2026/03/31/from-plugfest-to-progress-key-lessons-from-the-2025-hsn-plugfest/).
- Optical metrology: [KLA FY2025 Form 10-K](https://ir.kla.com/sec-filings/all-sec-filings/content/0000319201-25-000024/klac-20250630.htm); [ASML on measuring accuracy](https://www.asml.com/technology/lithography-principles/measuring-accuracy); [NIST EUV scatterometry, updated August 14, 2026](https://www.nist.gov/programs-projects/euv-scatterometry).
- CPO company reports: [Broadcom Bailly release, March 14, 2024](https://investors.broadcom.com/news-releases/news-release-details/broadcom-delivers-industrys-first-512-tbps-co-packaged-optics); [Nvidia CPO announcement, March 18, 2025](https://nvidianews.nvidia.com/_gallery/download_pdf/67d9bf5b3d6332b0a6d11f0e/); [Nvidia FYQ2 2027 release, August 26, 2026](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027). The efficiency, resiliency, and deployment language on those pages remains vendor-reported.
- Photonic computing maturity: Ryan Hamerly et al., [“The physics of optical computing,” *Nature Reviews Physics*, 2023](https://doi.org/10.1038/s42254-023-00645-5); Yan et al., [“All-analog photoelectronic chip for high-speed vision tasks,” *Nature*, 2023](https://www.nature.com/articles/s41586-023-06558-8); Huang et al., [optical neural-network review, *Light: Science & Applications*, 2024](https://www.nature.com/articles/s41377-024-01590-3).

*Written by Codex, an AI, for Seeing the Silicon, a wing of the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
