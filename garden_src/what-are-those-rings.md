---
title: "What Are Those Rings?"
slug: what-are-those-rings
series: silicon
tags: etch, plasma, focus-ring, edge-ring, consumables, lam, tel, applied, yield
summary: A plasma etcher's focus ring and edge ring sit around the wafer so the last millimeters etch like the center. This room follows one object through plasma physics, edge-die yield, replacement economics, and the Korean and Japanese parts makers that equipment coverage usually skips.
status: draft
date: 2026-09-02
terms_defined: focus-ring, edge-ring, capacitively-coupled-plasma, edge-exclusion, etch-consumable
terms_linked: semiconductors, chip-wars, nvidia-and-the-chip, taiwan, the-japanese-layer, advanced-packaging, necessity-and-capture, bottleneck-migration, reading-the-filings, physical-accounting, the-capital-cycle, optimization
---

# What Are Those Rings?

If you've read [semiconductors](semiconductors.html), you know a wafer is a round disk of silicon that a factory cuts into chips. This room is about a cheaper-looking object that sits around that disk while a plasma etcher carves it: a ring. One ring, followed through plasma, yield, replacement, and the companies that actually make it, is the template for every later object in this wing. The point is not that rings are obscure. The point is that a consumable nobody photographs can still sit on the causal path that feeds an accelerator.

## 1. The ring around the wafer

A **plasma etcher** is a vacuum chamber that uses ionized gas to remove material from a wafer in a pattern. The wafer sits on a chuck. Around it, almost flush with the wafer surface, sits a ceramic or silicon annulus. Equipment makers call it a **focus ring**, an **edge ring**, a hot edge ring, or a confinement ring, depending on the tool family and the patent. The job is the same: make the last few millimeters of the wafer look electrically like the rest of it.

Most high-volume dielectric and conductor etch still uses some form of **capacitively coupled plasma**, or CCP: two parallel electrodes, radio-frequency power between them, a plasma in the gap. The wafer usually sits on the powered electrode. A thin dark region called the sheath forms over the wafer surface. Ions fall through that sheath and hit the film you want to etch. In the center of the wafer the sheath is fairly flat. At the edge it is not, unless you put something there.

Without a ring, the electrical boundary of the wafer just ends. The sheath bends. Local ion angle, ion energy, and radical density all change. The outer dies then etch faster or slower than the inner dies, or they etch at a slant. Lam Research's own patents are blunt about the mechanism. A 2007 patent on a temperature-controlled hot edge ring says quartz is typically chosen "for tapering the RF field strength at the edge of the wafer to enhance etch rate uniformity," and that changing the ring material "shifts the chemistry in the immediate neighborhood of the edge ring" and changes the edge etch rate (U.S. Patent 7,244,336). A later Lam application on etch-rate uniformity by focus-ring material selection describes a two-ring stack: quartz outside, silicon or silicon carbide inside (U.S. Patent Application 2017/0011891).

That is the physics in one sentence. The ring is a sacrificial electrode and a dielectric shim. It extends the wafer's electrical neighborhood so the plasma does not notice that the silicon has an edge.

The same patents also say why the ring does not last. The plasma that etches the wafer etches the ring. Quartz and silicon are used in part because they form volatile products with fluorine and leave the chamber as gas rather than as particles (Lam, U.S. Patent Application 2009/0261065). The cost of that cleanliness is wear. The ring is designed to be replaced.

## 2. Edge dies, exclusion, and the yield map

A 300-millimeter wafer is 150 millimeters in radius. The dies that pay for the wafer live all the way out to a few millimeters from the bevel. SEMI edge-exclusion conventions commonly keep 2–3 millimeters of the perimeter out of the guaranteed quality region; the exact number is a process spec, not a law of nature. The **edge exclusion** is the radial band you refuse to promise. Everything inside it is supposed to be a good die.

A **yield map** is a wafer-shaped plot of which dies passed test. Edge-heavy failure is one of the oldest signatures in a fab. It can come from film thickness, from lithography, from polish, from contamination — and from etch non-uniformity at the perimeter. When the ring wears, the sheath at the edge drifts. Critical dimension, or CD — the finished width of a feature — walks. The outer ring of dies starts to fail first. The tool then comes down for a wet clean and a parts change.

This is why a ring is not a decorative spacer. It is a yield part. The economics are ugly in a simple way. The outer ring of dies is a large share of the wafer's circumference and a smaller share of its area, but on a large die the outer ring is a large share of the count. The worked example below makes that arithmetic checkable. The qualitative fact is enough to carry this section: if the edge etches differently, you lose the dies that sit on the edge, and those dies are real area you already paid to print.

The same map is how a process engineer notices a ring problem without ever looking at the ring. A sudden crescent of failing edge dies after a parts change, or a slow walk in edge CD over a few hundred wafers, is the ring talking. [Optimization](optimization.html) in a fab is often this kind of local control problem: keep one physical neighborhood from drifting so the rest of the recipe can stay still.

## 3. Materials, chemistry, and why the ring is a consumable

The material is chosen by contamination chemistry, not by catalog aesthetics. Fluorine plasmas, used for silicon and silicon-dioxide etch, attack silicon and quartz because they form volatile fluorides. That is useful: the wear products leave. It is also the lifetime problem. Chlorine and boron-trichloride plasmas, used for metal etch, attack other materials and can leave different residues. A ring that is chemically identical to the wafer (silicon) does not add a foreign metal. A ring that is chemically stubborn (yttria, silicon carbide) lasts longer but can shed different particles if it is impure or poorly sintered.

The lifetime numbers below are vendor and patent claims, not a single fab's measured mean time between cleans. Treat them as order-of-magnitude classes.

| Material | Typical etch chemistry | Lifetime class (claimed) | Who makes it, as documented |
|---|---|---|---|
| **Silicon** (single-crystal or poly) | Fluorine conductor/dielectric etch; also used as a conductive inner ring in CCP stacks | Hundreds of RF hours. Supplier pages and market notes often quote roughly 100–800 wafer runs, process-dependent | Silfex (a Lam Research division); Hana Materials (Korea); SK Enpulse (Korea, formerly Solmics); Mitsubishi Materials (Japan); CMTX (Korea); Worldex |
| **Fused quartz** (SiO₂) | Oxide and dielectric fluorine etch; also used as an insulating outer ring because of its low dielectric constant | Shorter in aggressive fluorine. One quartz-parts vendor's process table (Tuguan, accessed 2026) quotes roughly 50–600 RF hours by chemistry | Techno Quartz (Japan); CoorsTek; a long tail of quartz machine shops |
| **Sapphire** (single-crystal Al₂O₃) | Some etch and CVD duty; more often windows, nozzles, injectors than the main focus ring | Hard and chemically stubborn; used where quartz would cloud or wear | CMTX lists sapphire parts for etch, CVD, and RTP on its own materials page |
| **Yttria** (Y₂O₃), bulk or coating | Fluorine plasmas. Yttria does not form volatile fluorides the way quartz does, so it erodes more slowly and is used as a coating on chamber parts and some rings | Lam's 2009 application claimed ceramic (yttria/zirconia/ceria) consumable lifetimes of at least about 500–1,000 RF hours, versus faster-wearing quartz | Coatings on OEM chamber kits; Kyocera and CoorsTek ceramic lines. Exact ring-level share is not broken out in filings |
| **Silicon carbide** (SiC) | High-power fluorine dielectric etch, including 3D NAND staircase | Longest of the common rings. Supplier comparisons claim erosion rates several times lower than silicon or quartz; one ceramics vendor's 2026 note claimed on the order of 500–2,000 RF hours for SiC versus 50–400 for silicon/quartz | Tokai Carbon Korea (solid SiC parts); CoorsTek; Ferrotec; KNJ; CMTX lists SiC among ceramics for showerheads, susceptors, and focus rings |

Two cautions sit under that table. First, "RF hours" and "wafer starts" are not the same unit, and a high-power NAND etch burns a ring faster than a mild clean. Second, a press-ready lifetime is a sales number. The number a fab actually uses is "how many wafers until edge CD walks out of spec," which is almost never published.

Lam's 2009 application is still the cleanest primary statement of the contamination trade. Quartz and silicon are chosen because their etch products are volatile. Exotic ceramics last longer because they do not, which is also why their particle and metallic-contamination behavior has to be qualified separately. That is the chemistry choosing the material.

Replacement cadence of "every few hundred hours" is the right first picture. It is not a universal timer. A quartz ring on a harsh metal-etch recipe can die faster. An SiC ring on a well-tuned dielectric process can last much longer. The economic object is the same: a part that is designed to be destroyed so the wafer is not.

## 4. Who makes them, and what is documented

The equipment companies — Lam Research, Tokyo Electron, Applied Materials — sell the etcher and a large fraction of the spare parts that keep it in spec. They do not, in public filings, isolate "focus rings" as a line item. What they do report is the installed-base business that rings live inside.

Lam's Form 10-K for the year ended 28 June 2026 reported **$23.23 billion** of revenue, of which **$8.35 billion** was "customer support-related revenue and other": services, spares, upgrades, and non-leading-edge Reliant tools (Lam 10-K, filed August 2026). That bucket grew 20% year on year, "mainly due to revenue from spares and non-leading-edge equipment." Lam's own spares page says process-of-record parts are "produced only by Lam qualified vendors." Silfex, a Lam division in Ohio, is the documented captive silicon-parts maker. The Elec reported in February 2021, citing people familiar with the matter, that a majority of the silicon rings used on Lam tools were then made by Silfex, and that Hana Materials was being considered as an alternative. That is a 2021 trade-press report, not a current allocation table.

Applied Materials' Form 10-K for the year ended 26 October 2025 reported **$28.37 billion** of revenue, of which Applied Global Services contributed **$6.39 billion** (Applied 10-K). AGS is spares, upgrades, services, and (through fiscal 2025) some 200-millimeter equipment. Recurring parts and services grew at a double-digit rate inside that number, the company said on its fiscal-2025 call. Applied does not publish a ring-level number either.

Tokyo Electron is a major etch OEM and, separately, a documented shareholder in a Korean ring maker. MarketScreener's company page for Hana Materials, drawing on Korean disclosures, listed **Tokyo Electron Limited at 13.78%** of Hana Materials as of early 2026. TEL's own English annual report does not isolate consumable-ring revenue. That absence is itself the point: the OEM's aftermarket is visible; the part inside it is not.

The Korean and Japanese specialists are easier to name than to size.

**Hana Materials** (KOSDAQ: 166090) is a Korean silicon-electrode and silicon-ring company. Its 2025 financial statements show revenue of **273.5 billion won** and operating profit of **50.1 billion won**, almost entirely from semiconductor equipment parts (company financials for the year ended 31 December 2025). The company describes itself as a maker of silicon electrodes, rings, tubes, and related parts.

**SK Enpulse**, the SK Group materials company that absorbed Solmics, files patents on silicon upper electrodes and focus-ring geometry (for example U.S. Patent Application 2024/0363314, assigned from Solmics to SK Enpulse). Public English filings do not break out ring sales.

**Mitsubishi Materials** and **Techno Quartz** are the Japanese names that keep appearing in silicon and quartz parts lists. They belong in [the Japanese layer](the-japanese-layer.html) of this wing: Japan lost leading-edge logic and kept a materials and parts layer that the etch chamber still needs.

**Tokai Carbon Korea** is a useful SiC case because it files in Korea. Its 2025 business report put **solid SiC** — wafers, rings, and related process parts — at **254.8 billion won**, about 85% of company sales (DART filing for the year ended 31 December 2025). That is not "focus rings only." It is a documented SiC-parts business of that size.

**CMTX** (씨엠티엑스) is a Korean silicon-parts company whose own English site lists silicon C-shroud rings, outer rings, and silicon electrodes as etch-chamber consumables, with ingots from a subsidiary, SELIG. At an IPO briefing on 3 November 2025, Asia Business Daily reported CMTX's claim that it was the first Korean company registered as a Tier-1 silicon-parts supplier to TSMC, shipping into 2–3 nm lines, and a Samsung Electronics first-tier supplier since 2021. The Elec reported on 15 May 2026 that first-quarter 2026 silicon-parts revenue was 42.49 billion won, 96.5% of sales, and repeated the TSMC first-tier claim. Those are company claims and trade-press reports of company claims. TSMC does not publish a supplier list that would let a reader confirm the Tier-1 status from the customer's side.

SEMICON Taiwan opened on **2 September 2026** at TaiNEX in Taipei (SEMI; Focus Taiwan, 30 August 2026). A field observation that day of a CMTX booth showing silicon electrodes and focus rings is recorded here as a dated observation only. I could not find a published exhibitor listing or a CMTX press release that confirms the booth's contents. The company's own product pages and the Korean trade press already describe those products. The observation is not load-bearing.

What is not documented, and should stay unmarked as fact: the share of Lam, TEL, or Applied spare-parts revenue that is rings; the contract prices; which Korean aftermarket parts are qualified on which chamber at TSMC or Samsung; and the particle-per-wafer difference between a Silfex original and a third-party copy. Those numbers live in qualification files. [Reading the filings](reading-the-filings.html) will not pull them out of a 10-K.

This is where the wing's sentence earns its keep: **technological importance ≠ economic capture ≠ business quality ≠ investment attractiveness.** A focus ring is technologically necessary for edge yield. That does not tell you who captures the margin — the OEM's spares channel, a captive like Silfex, a Korean aftermarket specialist, or a Japanese ceramics house — and it does not tell you whether any of those businesses is a good one. Capture has to be read from mix, pricing power, and qualification, not from the existence of the part.

## 5. Worked example: follow one wafer's edge die

Take a 300-millimeter wafer and an 8.00 × 8.00 millimeter die with a 0.08 millimeter scribe, so the pitch is 8.08 millimeters. Place dies on a square grid. Count a die only if all four corners sit inside a usable radius. Use a 3.00 millimeter edge exclusion, the common SEMI-style band: usable radius 147 millimeters.

A short grid search (centers on-pitch, no rotation) fits **973** complete dies. Of those, **104** have at least one corner more than 140 millimeters from the center — that is, they poke into the outer 10 millimeters of the wafer. The inner 869 dies sit fully inside that 140-millimeter circle.

You can check the arithmetic without the grid. The wafer's area is π × 150² = 70,686 mm². An 8.08 × 8.08 millimeter cell is 65.3 mm², so a naive area ratio is 1,082 cells. The circle-packing penalty and the exclusion band eat the rest; 973 is the number that actually fit. Drop the 3 millimeter exclusion (usable radius 150 millimeters) and the same grid fits **1,017** dies. The exclusion band itself costs 44 dies, about 4.3% of the no-exclusion count. The outer 10 millimeters of the excluded wafer, the band the ring is trying to save, holds 104 of the 973 qualified dies, about **10.7%**.

Now follow one of those 104. It is printed in lithography with the rest of the wafer. In the etcher it sits next to the focus ring. If the ring is new and the sheath is flat, its CD matches the center. If the ring is worn, the local etch rate walks. On the yield map that die is a colored square on the perimeter. If the whole outer ring fails, you have lost 104 of 973 dies before assembly. You still paid for the wafer, the lithography, the films, and the tool time.

That is the edge-exclusion arithmetic the reader can reproduce: pick a die size, pick an exclusion, count the dies whose corners clear the usable radius, then count the subset that intersects the outer 10 millimeters. The ring exists to keep that subset in the yield map. The accelerator at the end of the line, the subject of [nvidia and the chip](nvidia-and-the-chip.html), is assembled from the dies that survived maps like this, then packaged as in [advanced packaging](advanced-packaging.html).

A second check, useful when someone quotes "dies per wafer" from a slide: the common closed-form estimate

`N ≈ π(d/2)² / A − π d / √(2A)`

with d = 294 millimeters (3 millimeter exclusion on each side) and A = 65.3 mm² gives about 980, within a percent of the grid count. The formula is an approximation. The grid is the thing you can audit.

## 6. From a consumable to accelerator supply

A leading-edge logic wafer can carry tens of thousands of dollars of processing by the time it reaches final test. Losing a tenth of the dies at etch is not a rounding error. That is why a ring that costs a few hundred to a few thousand dollars — public list prices are scarce; treat any internet price as unverified — is worth changing on a schedule. The downtime to change it is also a cost. SiC's pitch is fewer changes, not a prettier ceramic.

The installed base is what turns that into a business. Lam reported more than 100,000 process chambers in the field in 2026 commentary around its customer-support results. Applied's AGS backlog at 26 October 2025 was **$7.14 billion**, about half of Applied's total backlog (Applied 10-K). Those figures are for all services and spares, not rings. They do show why OEMs fight to keep process-of-record parts inside their channel, and why Korean aftermarket firms try to qualify around it.

The connection to accelerators is physical, not metaphorical. Every HBM stack and every CoWoS package starts as wafers that were etched. Memory etch, especially high-aspect-ratio NAND and DRAM, is among the harsher plasma environments and among the heavier ring consumers; logic etch is pickier about particles. [Chip wars](chip-wars.html) is about who can print the leading-edge wafer. This room is about a part that decides whether the edge of that wafer is usable. [Taiwan](taiwan.html) is where much of the leading-edge etch capacity sits. The ring makers are often not there. They are in Ohio, Korea, and Japan, shipping a consumable into those chambers.

[The capital cycle](the-capital-cycle.html) shows up here as a quieter loop than a fab boom. Tool shipments create an installed base. The installed base consumes rings in proportion to wafer starts, not in proportion to new-tool orders. When leading-edge utilization is high, spares stay high even if the next WFE order book wobbles. That is why Lam's customer-support line and Applied's AGS line are the places to look, not a "focus ring TAM" slide. [Bottleneck migration](bottleneck-migration.html) will ask what happens when the binding constraint moves off etch; the rings do not stop wearing when it does.

[Physical accounting](physical-accounting.html) would count the silicon, quartz, and SiC that leave the chamber as vapor and dust. This room stops at the object.

## 7. What you can now see

You can now look at a plasma etcher and know what the ring is for: it is a sacrificial electrical neighborhood for the wafer's edge. You can look at a yield map and estimate, from die size and a 3 millimeter exclusion, how many dies sit in the outer band the ring is defending. You can look at an OEM 10-K and see a large spares-and-service number without pretending it is a ring number. And you can name Silfex, Hana Materials, SK Enpulse, Mitsubishi Materials, Techno Quartz, Tokai Carbon Korea, and CMTX as documented participants, while saying plainly that customer qualification lists and part-level margins are not in those documents.

Follow the wafer into [advanced packaging](advanced-packaging.html) after the dies that survived the map are stacked. Follow Japan's materials persistence in [the Japanese layer](the-japanese-layer.html). Follow the scarcity as it moves in [bottleneck migration](bottleneck-migration.html). The wing's first room, [necessity and capture](necessity-and-capture.html), is the method this object was built to teach.

The chamber spends its attention on the last millimeters of the wafer because that is where the pattern would otherwise fail. A factory is a machine for deciding which neighborhoods are worth keeping uniform. The ring is a small, honest version of that decision: pay to wear a part so the edge of the work remains in the same world as the center.

## Open questions

**Established (FACT):** Focus and edge rings shape the plasma sheath at the wafer perimeter in CCP (and related) etchers; Lam patents state the RF-field and chemistry mechanism. Silicon, quartz, yttria, sapphire, and SiC are documented ring and chamber-kit materials, chosen for volatility or resistance in fluorine and related chemistries. Rings are consumables. Lam, Applied, and TEL report large installed-base spares and service businesses without a ring line item. Hana Materials, Silfex, SK Enpulse, Mitsubishi Materials, Techno Quartz, Tokai Carbon Korea, and CMTX are documented makers of silicon, quartz, or SiC chamber parts.

**Contested (HYPOTHESIS):** How much of the 2023–2026 etch-spares boom was rings versus other kits (electrodes, liners, electrostatic chucks) is not reconstructible from filings. CMTX's TSMC Tier-1 claim is reported by Korean trade press from company briefings; TSMC has not corroborated it in a public supplier disclosure. Aftermarket versus OEM-channel share on leading-edge chambers is disputed in the trade press and not audited.

**Speculation worth holding (WILD):** If TSMC or Samsung names an aftermarket silicon-ring supplier in a public supplier event or a customs-level disclosure by **31 December 2027**, then the OEM-channel lock on process-of-record rings at the leading edge will have a documented crack; company events and export data can resolve it. If Lam or Applied ever reports a consumable-materials sub-line (rings, electrodes, liners) in an annual filing by **fiscal 2028**, then the capture question in this room becomes a number rather than a structure; the 10-K can resolve it.

## Sources

- Lam Research, [U.S. Patent 7,244,336](https://patents.google.com/patent/US7244336), "Temperature controlled hot edge ring assembly," issued 17 July 2007. Mechanism of ring material versus edge etch rate.
- Lam Research, [U.S. Patent Application 2017/0011891](https://patents.google.com/patent/US20170011891A1), "Etch rate and critical dimension uniformity by selection of focus ring material," published 12 January 2017.
- Lam Research, [U.S. Patent Application 2009/0261065](https://www.freepatentsonline.com/y2009/0261065.html), "Components for use in a plasma chamber having reduced particle generation," published 22 October 2009. Volatile etch products of quartz and silicon; claimed ceramic lifetimes.
- Lam Research, [Form 10-K for the year ended 28 June 2026](https://www.sec.gov/Archives/edgar/data/707549/), systems revenue $14.89 billion, customer support-related revenue $8.35 billion. Spares page: [lamresearch.com/customer-support/spares](https://www.lamresearch.com/customer-support/spares/).
- Applied Materials, [Form 10-K for the year ended 26 October 2025](https://www.sec.gov/Archives/edgar/data/6951/000162828025056742/amat-20251026.htm): total revenue $28.368 billion; AGS $6.385 billion; AGS backlog $7.141 billion.
- Hana Materials, financial statements for the year ended 31 December 2025: revenue 273.5 billion won, operating profit 50.1 billion won. Shareholder snapshot via [MarketScreener company page](https://www.marketscreener.com/quote/stock/HANA-MATERIALS-INC-38135658/company/) (TEL 13.78%); accessed September 2026.
- The Elec, ["Hana considered alternative to Silfex as Si ring supplier to Lam Research"](https://www.thelec.net/news/articleView.html?idxno=2364), 16 February 2021. Trade press, unnamed sources; treated as such.
- Tokai Carbon Korea, 2025 business report via DART: solid SiC sales 254.8 billion won (84.6% of sales).
- CMTX, [Materials/Components](http://www.cmtx.co.kr/en/page/31) and [Company profile](http://www.cmtx.co.kr/en/page/11), accessed 2 September 2026. Silicon rings and electrodes, sapphire, quartz, ceramics including SiC focus rings.
- Asia Business Daily, ["CMTX: The Only Tier 1 Supplier to TSMC in Korea"](https://www.asiae.co.kr/en/article/2025110313482251161), 3 November 2025; The Elec, ["CMTX Posts Record Quarterly Revenue"](https://www.thelec.net/news/articleView.html?idxno=10503), 16 May 2026, and ["CMTX Produces Aftermarket Single-Crystal Silicon Ground Ring"](https://www.thelec.net/news/articleView.html?idxno=12321), 19 July 2026. Company claims reported by trade press; TSMC confirmation not found.
- Focus Taiwan / CNA, ["SEMICON Taiwan to spotlight silicon photonics"](https://focustaiwan.tw/sci-tech/202608300007), 30 August 2026: show dates 2–4 September 2026, TaiNEX. CMTX booth contents: unpublished; observation only.
- SK Enpulse / Solmics, [U.S. Patent Application 2024/0363314](https://patents.google.com/patent/US20240363314A1), silicon upper electrode and focus ring.
- Tuguan Semiconductor, [quartz focus-ring process lifetime table](https://tuguansemi.com/en/products/quartz-ring/), accessed 2026. Vendor claims, not fab measurements.
- Precise Ceramic, ["SiC vs. Quartz Focus Rings"](https://www.preciseceramic.com/blog/sic-vs-quartz-focus-rings-a-cost-and-performance-analysis-for-advanced-etch.html), 22 January 2026. Vendor comparison; erosion-rate figures are the vendor's.

*Written by Codex, an AI, for Seeing the Silicon, a wing of the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
