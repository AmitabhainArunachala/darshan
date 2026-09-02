---
title: "The Memory Wall and Why HBM Exists"
slug: the-memory-wall
series: silicon
tags: hbm, memory, bandwidth, roofline, dram, energy, sk-hynix, micron, samsung
summary: Moving data can cost far more energy than doing arithmetic, and a fast accelerator is useful only when its memory system can feed it. This room connects the memory wall and roofline model to HBM's physical design, difficult yields, and the value captured by memory and packaging suppliers from 2023 through 2026.
status: draft
date: 2026-09-02
terms_defined: memory-wall, roofline-model, arithmetic-intensity, high-bandwidth-memory, through-silicon-via
terms_linked: semiconductors, optimization, nvidia-and-the-chip, advanced-packaging, bottleneck-migration, reading-the-filings, physical-accounting, what-are-those-rings
---

# The Memory Wall and Why HBM Exists

An accelerator can contain more arithmetic units than it knows how to keep busy. The missing work is often waiting in memory, across wires that take time and energy to cross. This room follows that delay from a 1995 paper to the stacks of memory beside an AI processor, then follows the money that moved when those stacks became scarce.

## 1. The expensive part is fetching the number

Start with one addition. In Mark Horowitz's ISSCC paper from February 2014, a 32-bit integer add in a 45-nanometer process was a rough **0.1 picojoule** operation. A 32-bit floating-point add was **0.9 pJ**, and a 32-bit floating-point multiply was about **3.7 pJ**. These are old-process estimates, not measurements of a 2026 accelerator. Their value is the ratio.

Now fetch the operands. Horowitz's original chart priced a **64-bit access** to an 8 KB on-chip SRAM at about **10 pJ**, to a 32 KB SRAM at **20 pJ**, and to a 1 MB SRAM at **100 pJ**. An off-chip DRAM access was roughly **1.3–2.6 nanojoules**, or **1,300–2,600 pJ**. Fetching from the smallest SRAM cost around one hundred 32-bit integer adds. Reaching DRAM cost tens of thousands.

You will often see a second version of this table: 5 pJ for a 32-bit 8 KB SRAM read and 640 pJ for a 32-bit DRAM read. Those are useful 32-bit normalizations of the same rough energy hierarchy, but they are not the bit widths printed on Horowitz's original slide. Keeping the versions separate matters because a tidy table can otherwise turn an estimate into false precision.

**SRAM**, or static random-access memory, is the fast memory built from transistor cells that a processor can place on its own die. **DRAM**, or dynamic random-access memory, stores charge in denser cells and must be refreshed; most capacity sits outside the processor package. Distance is not the only cost. Larger memories need longer wires, more decoding, and more capacitance to charge and discharge. But distance gives you the right first picture: arithmetic happens in a small neighborhood; memory traffic keeps leaving it.

This is why [optimization](optimization.html) in machine learning is also a physical problem. A mathematical operation count tells you how much arithmetic exists. It does not tell you where the operands are, how often they move, or whether the machine can supply them quickly enough.

## 2. The wall and the roof

William Wulf and Sally McKee named the **memory wall** in *Computer Architecture News* in March 1995. Processor speed and DRAM speed were both improving, they wrote, but processor performance was improving along a steeper exponential curve. The gap therefore widened. A faster processor spent a growing share of its time waiting for memory.

Their paper was mainly about latency and performance, not Horowitz's later energy table. The two arguments now reinforce each other. A long trip to memory both stalls the arithmetic and costs more energy than the arithmetic it serves.

Samuel Williams, Andrew Waterman, and David Patterson gave engineers a compact way to see the limit in 2009. The **roofline model** plots attainable performance against **operational intensity**, the number of useful operations performed for each byte transferred to DRAM after the cache has filtered traffic. People now often call this **arithmetic intensity**, measured in FLOPs per byte. The original paper kept a subtle distinction between the two terms; this room uses the modern shorthand while stating the memory boundary.

The basic roof is:

`attainable FLOP/s = min(peak FLOP/s, memory bandwidth × FLOPs/byte)`

The horizontal part is the compute ceiling. The rising part is the bandwidth ceiling. Their intersection is the **ridge point**: peak compute divided by peak memory bandwidth. A kernel to the left cannot reach the advertised FLOP rate even in the ideal model. It does not reuse each fetched byte enough times. A kernel to the right may be compute-bound, though instruction mix, occupancy, caches, and software can put lower ceilings underneath the simple roof.

This gives you a cleaner way to read an accelerator specification. Peak FLOPs are not a speed. They are one ceiling. Memory bandwidth is another. The program chooses which one it hits.

## 3. HBM makes the path short and very wide

**High-bandwidth memory**, or HBM, is DRAM reorganized for a short, wide connection to a nearby processor. Instead of driving a relatively narrow interface at extreme clock speed through long board traces, an HBM stack exposes thousands of connections at lower per-pin speeds. Several thin DRAM dies sit on a base die. **Through-silicon vias**, or TSVs, are vertical metal connections drilled and filled through those dies. The stack sits next to the logic die on an interposer, a finely wired layer inside the package.

The phrase to keep is **wide and slow**. HBM3 has a 1,024-bit external interface. HBM4 doubles that to 2,048 bits. Conventional memory modules use far fewer data pins driven faster and farther. Short, lower-capacitance connections let HBM move more bits per second with less energy per bit. That is the physical answer to the roofline's sloping side.

It is also a manufacturing wager. Each memory wafer is thinned. TSVs must line up. Dies must be bonded without trapping defects. The completed stack must survive heat, warpage, molding, and package test. If the known-good probability of one DRAM die is `q`, an eight-die stack has a raw die-survival probability of `q^8` before base-die, TSV, bonding, and final-test losses. At 95% per die, that is only 66.3%. At 99%, it is 92.3%.

That multiplication is illustrative, not a reported supplier yield. Real manufacturers test dies before stacking and repair some memory faults, so they do not blindly assemble random dies. But known-good-die screening does not repeal multiplication. It moves effort and cost earlier in the process. TrendForce estimated in May 2024 that HBM consumed roughly 60% more wafer area than conventional DRAM for an equivalent comparison and reported HBM yields around 50–60%, without publishing the exact denominator. Treat those figures as an industry estimate, not a universal process law.

HBM therefore solves one scarcity by creating several others: advanced DRAM wafer starts, TSV capacity, thinning and bonding tools, package substrates, silicon interposers, thermal materials, and test time. The DRAM in those stacks is the same family of devices described in [semiconductors](semiconductors.html); HBM rearranges it. [Advanced packaging](advanced-packaging.html) is where those dependencies meet.

## 4. Four generations, four dated states

The table separates standards from shipping products. Maximum standard bandwidth is not the same as the bandwidth of every product, and a supplier announcement proves only that supplier's claim.

| Generation | Stack height | Bandwidth per stack | Suppliers and dated status |
|---|---:|---:|---|
| **HBM2E** (JESD235C) | Commercial 4-high and 8-high; some roadmaps included 12-high | JEDEC-class 3.2 Gb/s per pin gives 409.6 GB/s; SK hynix shipped 3.6 Gb/s, or 460.8 GB/s | Samsung launched 8-high 16 GB Flashbolt on Feb. 4, 2020; SK hynix announced 16 GB HBM2E in August 2019; Micron documented 8 GB and 16 GB HBM2E. |
| **HBM3** (JESD238) | Original standard supported up to 12-high, with 16-high described as an extension; 8-high and 12-high shipped | 6.4 Gb/s × 1,024 bits = **819.2 GB/s** | SK hynix reported mass production in June 2022; Samsung reported 8-high and 12-high production in October 2023. No public Micron HBM3 product was verified; Micron moved from HBM2E to HBM3E. |
| **HBM3E** (commercial extension of HBM3) | 8-high and 12-high in volume; 16-high appeared as samples or demonstrations | Roughly **1.18–1.28 TB/s** at vendor rates of 9.2–10 Gb/s over 1,024 bits | Micron announced H200-bound 8-high volume production Feb. 26, 2024. SK hynix shipped 8-high in March and began 12-high volume production Sept. 26, 2024. Samsung's own October 2024 disclosure confirmed a major-customer delay; by Q3 2025 it said HBM3E was in mass production for all related customers. |
| **HBM4** (JESD270-4) | Standard supports 4-, 8-, 12-, and 16-high with 24 Gb or 32 Gb dies | JEDEC: 8 Gb/s × 2,048 bits = **2.048 TB/s**; 2026 vendor products claimed more | JEDEC published the standard Apr. 16, 2025. Samsung reported commercial shipments Feb. 12, 2026; Micron reported high-volume production Mar. 16; SK hynix reported Q2 mass shipments July 29. Customer-specific qualification and allocated volume remained uneven and disputed as of Sept. 2, 2026. |

HBM3E is not a separately numbered JEDEC architecture. It is the industry's extended HBM3 product class. HBM4 changes more: twice the interface width and, in many designs, a custom logic base die made on a foundry process. That change pulls memory suppliers deeper into logic design and foundry coordination.

Notice also what the table cannot tell you. Supplier names are public; exact customer allocations, yields, and contractual prices usually are not. In June 2026 TrendForce reported that the three large suppliers' HBM wafer input would rise from about 18% of their DRAM input at the end of 2025 to 22% in 2026 and 30% in 2027. Those are estimates of allocation, not audited shipments.

## 5. Worked example: put a matrix multiply on the roofline

Take an NVIDIA H100 SXM, using NVIDIA's posted ceilings as accessed on Sept. 2, 2026: **67 FP32 TFLOP/s** and **3.35 TB/s** of HBM bandwidth. Now multiply two deliberately skinny FP32 matrices:

- `A` is 4,096 × 16.
- `B` is 16 × 4,096.
- `C = A × B` is 4,096 × 4,096.
- Count one multiply and one add for every inner-dimension step.

The arithmetic is:

`2 × 4096 × 4096 × 16 = 536,870,912 FLOPs`

For the kindest possible HBM traffic count, read each input once and write the output once:

- `A`: `4096 × 16 × 4` = 262,144 bytes.
- `B`: `16 × 4096 × 4` = 262,144 bytes.
- `C` write: `4096 × 4096 × 4` = 67,108,864 bytes.
- Total: 67,633,152 bytes.

Arithmetic intensity is therefore:

`536,870,912 / 67,633,152 = 7.94 FLOPs/byte`

The H100's ridge point is:

`67 TFLOP/s / 3.35 TB/s = 20 FLOPs/byte`

Our 7.94 FLOPs/byte falls to the left. The bandwidth roof is `3.35 × 7.94 = 26.6 TFLOP/s`, far below the 67 TFLOP/s compute ceiling. The ideal memory time is about 20.2 microseconds; the ideal arithmetic time is 8.0 microseconds. Bandwidth binds first.

This is a theoretical lower bound, not a benchmark. Kernel launch overhead, tiling, cache behavior, and occupancy can all make it slower. The traffic estimate is unusually generous. If the operation reads the old value of `C` before accumulating into it, traffic rises and intensity falls. A large square matrix multiply can reuse inputs many times and become compute-bound. The point is sharper than “matrix multiplication needs bandwidth”: shape and reuse decide which roof you hit.

## 6. The 2023–2025 race was a qualification race

SK hynix entered the generative-AI demand shock with the practical lead. TrendForce said on March 13, 2024 that SK hynix was the primary HBM3 supplier for NVIDIA's H100 and led HBM3E validation. SK hynix then reported that 2024 HBM sales grew more than 4.5 times and that HBM exceeded 40% of its DRAM revenue in the fourth quarter.

Micron turned HBM3E into an entry point. On Feb. 26, 2024 it announced volume production of a 24 GB, eight-high part for NVIDIA's H200, with more than 1.2 TB/s of bandwidth. In September 2024, Micron said its HBM was sold out for calendar 2024 and 2025, with most 2025 pricing already contracted. It also said HBM margins were above both DRAM and company averages. That is company testimony, but it is unusually direct testimony about economic capture.

Samsung's difficulty shows why “three companies can make DRAM” did not mean three interchangeable HBM suppliers. TrendForce forecast in March 2024 that Samsung would complete HBM3E qualification in the first quarter. In May it moved the expectation to the second quarter with midyear delivery. By Sept. 30, its 12-high product was still under validation. Samsung itself disclosed on Oct. 8 that HBM3E business with a major customer had begun later than expected, and its Oct. 31 call said commercialization was below guidance.

Reuters reported heat and power issues in May and an eight-high qualification pass in August, based on unnamed sources. Those reports conflict at the edges with Samsung's later disclosure. The defensible statement is narrower: customer-specific qualification was private, outside reports disagreed, and Samsung's own filings confirm that the important 2024 commercialization arrived late. By the third quarter of 2025, Samsung said HBM3E was in mass production and sold to all related customers.

This sequence is a useful case for [reading the filings](reading-the-filings.html). A product announcement says a device exists. Qualification says a customer trusts it inside a costly package. Shipment says it passed enough tests at enough volume. Revenue and margin show whether the supplier captured value. Those are four different events.

## 7. Where the value went

The financial turn was large. SK hynix moved from the memory downturn into 2024 revenue of **66.193 trillion won**, operating profit of **23.467 trillion won**, and a **35% operating margin**, reported Jan. 23, 2025. Its fourth-quarter margin was 41%. The company credited AI memory including HBM and enterprise SSDs, but it does not publish an HBM-only operating margin. Do not assign the whole recovery to one product.

Micron's fiscal 2025 gross margin rose to **39.8%** from **22.4%** in fiscal 2024, while revenue rose from $25.1 billion to $37.4 billion. Its filing said revenue from HBM, high-capacity DIMMs, and low-power server DRAM reached $10 billion, more than five times the prior year. Again, this is a bundle, not an HBM segment. Still, the company's earlier statement that HBM margins were accretive connects the product to the improvement more directly than an outside estimate can.

TrendForce estimated in September 2024 that HBM would represent only about 10% of 2025 DRAM bit output but more than 30% of DRAM revenue. That gap is the scarcity rent in one line. Yet the rent did not belong permanently to memory. In June 2026 TrendForce argued that annual HBM contracts had stopped prices from immediately matching a sharp rise in ordinary server DRAM. The relative attractiveness of capacity had moved again. [Bottleneck migration](bottleneck-migration.html) is not a metaphor; it is a change in which wafer start earns the best next dollar.

The packaging chain received work and capital. SK hynix put its M15X fab beside an expanding TSV line. Micron broke ground on a dedicated HBM advanced-packaging plant in Singapore on Jan. 8, 2025. TrendForce estimated that TSV expansion required nine to twelve months and that CoWoS scarcity, combined with HBM's production cycle of more than two quarters, constrained accelerator output in 2024. Public documents do not isolate the margin captured by each TSV toolmaker, molding-material supplier, tester, or outsourced assembly house. It is honest to say the orders moved outward; it is not honest to assign profits without filings.

This is where the wing's equation earns its place: **technological importance ≠ economic capture ≠ business quality ≠ investment attractiveness.** HBM was technologically necessary. SK hynix and Micron showed economic capture in reported mix and margins. That still says nothing by itself about durability, capital intensity, customer concentration, or any security's attractiveness. Those are separate questions.

## 8. What you can now see

You can now read peak FLOPs as one roof rather than a promise. You can calculate a kernel's arithmetic intensity, compare it with a machine's ridge point, and tell whether more arithmetic or more bandwidth would matter first. You can also see why HBM is not “faster DRAM” in the simple sense. It is a stack, a TSV process, an interposer, a test problem, and a yield multiplication placed beside a processor.

Follow the package into [advanced packaging](advanced-packaging.html), or follow one etch-chamber object in [what are those rings](what-are-those-rings.html). Follow the constraint as it shifts through [bottleneck migration](bottleneck-migration.html). [Nvidia and the chip](nvidia-and-the-chip.html) explains the accelerator above the memory interface. [Physical accounting](physical-accounting.html) follows the energy and materials that specification sheets leave outside their boundary.

## Open questions

**Established (FACT):** Data movement carried a much larger energy cost than simple arithmetic in Horowitz's 45 nm comparison. Wulf and McKee documented the widening processor-memory performance gap in 1995. Roofline bounds performance by the lower of compute and bandwidth ceilings. HBM uses stacked DRAM, TSVs, and wide nearby interfaces. SK hynix led HBM3/HBM3E supply entering 2024; Micron shipped HBM3E for H200; Samsung disclosed a major-customer delay.

**Contested (HYPOTHESIS):** HBM4 announcements do not settle 2026 supplier ranking. All three vendors reported production or shipments by the second quarter, while TrendForce described uneven customer qualification and allocation. The amount of HBM scarcity rent that survives once packaging and ordinary DRAM tighten is also contested because contracts, denominators, and capacity accounting differ.

**Speculation worth holding (WILD):** If customer-qualified HBM4 volume from all three suppliers reaches disclosed accelerator ramps, then no single supplier should retain a majority of HBM4 shipments by **Q4 2027**; quarterly supplier filings and TrendForce's dated HBM share reports can resolve it. If hybrid bonding becomes necessary for mainstream HBM rather than selected products, then at least two memory vendors should name volume hybrid-bonded HBM in filings by **Dec. 31, 2028**; their annual reports and JEDEC product disclosures can resolve it.

The machine spends energy according to where its data lives, and an engineering team spends attention the same way: on the thing it must fetch next. HBM moves a working set closer to arithmetic. The larger design question is which memories deserve to be made close, wide, and expensive in the first place—what the machine is being built to keep present, and what it can afford to forget.

## Sources

- Mark Horowitz, [“Computing's Energy Problem (and What We Can Do About It)”](https://doi.org/10.1109/ISSCC.2014.6757323), IEEE ISSCC, Feb. 2014, pp. 10–14. Original 45 nm energy figures verified from the paper; accessed Sept. 2, 2026.
- William A. Wulf and Sally A. McKee, [“Hitting the Memory Wall: Implications of the Obvious”](https://doi.org/10.1145/216585.216588), *ACM SIGARCH Computer Architecture News* 23(1), Mar. 1995. University of Virginia report dated Dec. 1994.
- Samuel Williams, Andrew Waterman, and David Patterson, [“Roofline: An Insightful Visual Performance Model for Multicore Architectures”](https://doi.org/10.1145/1498765.1498785), *Communications of the ACM* 52(4), Apr. 2009.
- JEDEC, HBM3 release mirrored with specifications by [Phoronix, Jan. 27, 2022](https://www.phoronix.com/news/JEDEC-HBM3), and [HBM4 JESD270-4 release, Apr. 16, 2025](https://www.businesswire.com/news/home/20250416843598/en/). JEDEC's site blocked automated access; the HBM4 release is a distributed copy of JEDEC's announcement.
- SK hynix, [HBM2E architecture explainer](https://news.skhynix.com/en/hbm2e-opens-the-era-of-ultra-speed-memory-semiconductors/), Oct. 25, 2019; [HBM3 mass-production account](https://news.skhynix.com/en/meet-the-engineers-leading-the-worlds-first-mass-production-of-hbm3/), June 22, 2022; [12-layer HBM3E volume production](https://news.skhynix.com/en/sk-hynix-begins-volume-production-of-the-world-first-12-layer-hbm3e/), Sept. 26, 2024.
- SK hynix, [2024 results](https://news.skhynix.com/en/sk-hynix-announces-4q24-financial-results/), Jan. 23, 2025, and [Q2 2026 results](https://news.skhynix.com/en/q2-2026-business-results/), July 29, 2026.
- Micron, [HBM2E technical brief](https://www.micron.com/content/dam/micron/global/public/products/technical-marketing-brief/micron-hbm2e-memory-wp.pdf); [HBM3E volume-production release](https://investors.micron.com/news/press-release/2024/Micron-Commences-Volume-Production-of-Industry-Leading-HBM3E-Solution-to-Accelerate-the-Growth-of-AI-02-26-2024/default.aspx), Feb. 26, 2024; [fiscal Q4 2024 prepared remarks](https://investors.micron.com/static-files/5890f96b-bf35-4c4d-b8b8-b9d0f9ed63e4), Sept. 25, 2024; [fiscal 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/723125/000072312525000038/mu-20251125.htm), filed Nov. 25, 2025.
- Samsung, [HBM2E launch](https://news.samsung.com/global/samsung-to-advance-high-performance-computing-systems-with-launch-of-industrys-first-3rd-generation-16gb-hbm2e), Feb. 4, 2020; [Memory Tech Day 2023](https://news.samsung.com/global/samsung-electronics-holds-memory-tech-day-2023-unveiling-new-innovations-to-lead-the-hyperscale-ai-era), Oct. 20, 2023; [Q3 2024 earnings-call script](https://irsvc.teletogether.com/sec/pdf/2024Q3_script_eng.pdf?1=), Oct. 31, 2024; [Q3 2025 results](https://news.samsung.com/global/samsung-electronics-announces-third-quarter-2025-results), Oct. 30, 2025.
- TrendForce, [HBM supply and qualification](https://www.trendforce.com/presscenter/news/20240313-12075.html), Mar. 13, 2024; [wafer input and yield estimates](https://www.trendforce.com/presscenter/news/20240520-12143.html), May 20, 2024; [12-high qualification and revenue-mix estimate](https://www.trendforce.com/presscenter/news/20240930-12319.html), Sept. 30, 2024; [2026–27 pricing and wafer allocation](https://www.trendforce.com/presscenter/news/20260602-13074.html), June 2, 2026.
- NVIDIA, [H100 specifications](https://www.nvidia.com/en-sg/data-center/h100/), accessed Sept. 2, 2026. The worked example uses posted theoretical ceilings, not measured application performance.
- Packaging investment: SK hynix [M15X announcement](https://news.skhynix.com/en/sk-hynix-to-produce-dram-from-m15x-in-cheongju/), Apr. 24, 2024; Micron [Singapore HBM packaging plant](https://investors.micron.com/news/press-release/2025/Micron-Breaks-Ground-on-New-HBM-Advanced-Packaging-Facility-in-Singapore-01-08-2025/default.aspx), Jan. 8, 2025.

*Written by Codex, an AI, for Seeing the Silicon, a wing of the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
