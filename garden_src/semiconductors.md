---
title: Semiconductors
slug: semiconductors
series: foundations
tags: semiconductors, physics, transistors, chips, silicon, superconductors, hardware
summary: What a semiconductor actually is, down at the level of electrons and energy gaps. How one physical trick — a material you can switch between conducting and insulating — became the transistor, then the chip, then a roughly $796 billion industry. Plus one honest section on superconductors, which are a different thing entirely and worth knowing about.
status: draft
date: 2026-08-25
terms_defined: semiconductor, band gap, doping, transistor, mosfet, integrated circuit, photolithography, moores-law, superconductor, josephson junction
terms_linked: nvidia-and-the-chip, chip-wars, taiwan, neural-networks, intro-to-computer-science, quantum-physics-and-ai, mechanistic-interpretability
---

# Semiconductors

You're in the foundations series. If you've read [nvidia-and-the-chip](nvidia-and-the-chip.html) or [chip-wars](chip-wars.html), you've seen chips treated as strategic objects — things nations fight over. This room goes underneath all of that. It answers the question those rooms assume: what *is* this stuff, physically? Why does a particular arrangement of silicon atoms compute?

## 1. The trick: a material that can't decide

Start with copper. Copper conducts electricity because its outer electrons aren't attached to any particular atom — they drift freely through the metal, and a voltage pushes them into a current. Now take glass. Glass insulates because every electron is locked to its atom. Push with a reasonable voltage and nothing moves.

A semiconductor sits between these two, and the word "semi" undersells how strange that position is. In pure silicon at room temperature, almost all electrons are locked in place, like glass. But the lock is weak. It takes only a small kick of energy to break an electron free, and once free, it conducts, like copper.

The size of that kick is the material's **band gap** — the energy jump between the states where electrons are stuck (the valence band) and the states where they're free to move (the conduction band). For silicon the gap is about 1.12 electron volts at room temperature. This is a textbook number, stable for seventy years. Glass has a gap of several electron volts — too wide to jump. Copper has no gap at all.

Here's the comparison laid out:

| | Conductor (copper) | Semiconductor (silicon) | Insulator (glass) |
|---|---|---|---|
| Band gap | none | ~1.12 eV | ~5–9 eV |
| Electrons free at room temp | essentially all outer electrons | very few, but some | essentially none |
| Conducts when you apply voltage? | always | **it depends** | never |
| Can you control it? | no — always on | **yes** | no — always off |

Read the third row again. "It depends" is the entire semiconductor industry. A material that always conducts is a wire. A material that never conducts is a table. A material whose conduction you can turn on and off *with another electrical signal* is a switch that controls switches — and a switch that controls switches is the atom of computation. Everything in [intro-to-computer-science](intro-to-computer-science.html) — logic gates, memory, processors — is built by wiring enormous numbers of these switches together.

## 2. Doping: sabotaging the crystal on purpose

Pure silicon is a mediocre conductor and not directly useful. The move that makes it useful is called **doping**: deliberately contaminating the crystal with trace amounts of a different element, roughly one foreign atom per million silicon atoms.

Silicon has four outer electrons, and in the crystal each atom bonds to four neighbors — every electron is spoken for. Now swap in a phosphorus atom, which has five outer electrons. Four go into bonds. The fifth has nowhere to go, so it floats nearly free. Sprinkle phosphorus through the crystal and you get silicon with a population of loose electrons — **n-type** silicon ("n" for the negative charge of the electron).

Swap in boron instead, which has three outer electrons, and you get the opposite: one bond is missing an electron. That missing electron — a "hole" — behaves like a mobile positive charge, because neighboring electrons can hop into it, moving the vacancy around. That's **p-type** silicon.

Neither type is interesting alone. The interesting thing happens at the border. Put p-type and n-type silicon in contact and the loose electrons near the junction fall into the nearby holes, leaving a thin zone with no mobile charges at all — a built-in barrier. Current can push through the barrier easily in one direction and almost not at all in the other. That one-way valve is a diode, the simplest semiconductor device, and the p-n junction is the basic structural element of nearly everything else.

## 3. The transistor: December 1947, a slab of germanium and a plastic wedge

The transistor was not invented on a whiteboard. On December 16, 1947, at Bell Labs in New Jersey, John Bardeen and Walter Brattain — working in a group led by William Shockley — pressed two closely spaced gold contacts, held in place by a plastic wedge, onto a slab of germanium (silicon's heavier cousin, also a semiconductor). The voltage on one contact modulated the current flowing through the other. A small signal in, an amplified copy out — up to about 100× stronger. They demonstrated it to lab management on December 23, and Bell Labs announced it publicly on June 30, 1948. Bardeen, Brattain, and Shockley shared the 1956 Nobel Prize in Physics for it.

What made that lash-up matter is the principle: *a semiconductor can use one electrical signal to control another.* No vacuum, no heated filament, no moving parts. The vacuum tubes that computed before 1947 did the same job but were the size of your thumb, ran hot, and burned out like light bulbs. The transistor did it in solid crystal.

The version that conquered the world is the **MOSFET** — metal-oxide-semiconductor field-effect transistor — and it's worth thirty seconds to actually understand, because you own several trillion of them:

1. Take p-type silicon. Implant two n-type regions in it, a short distance apart. Call them the **source** and the **drain**.
2. Current wants to flow from source to drain but can't: the path between them runs through p-type material, and the junctions block it. The switch is **off**.
3. Above the gap between source and drain, separated by an insulating layer a few atoms thick, sits a metal electrode: the **gate**.
4. Put a positive voltage on the gate. Its electric field reaches through the insulator and attracts electrons up to the surface of the p-type region, forming a thin n-type channel connecting source to drain. Current flows. The switch is **on**.
5. Remove the gate voltage, the channel evaporates, the switch is off again.

No current flows through the gate itself — the field does the work, which is why it's called a field-effect transistor, and why the switch takes so little energy to flip. Wire one transistor's drain to another's gate and switches control switches. From there, logic gates. From there, everything.

## 4. From transistor to chip: printing with light

One transistor is a component. The revolution was making *many* transistors, plus the wiring between them, in a single piece of silicon — the **integrated circuit**. Jack Kilby at Texas Instruments demonstrated the first working integrated circuit in September 1958; Robert Noyce at Fairchild independently arrived months later at the more practical "planar" version, with flat components and printed metal interconnects, which is the version the world adopted. (Kilby got the 2000 Nobel Prize; Noyce had died in 1990, and Nobels aren't awarded posthumously.)

The manufacturing idea is the deepest thing in this room, so here it is plainly: **you don't assemble a chip — you print it.** The process is **photolithography**, and it works like developing a photograph:

1. Grow a cylinder of pure silicon, slice it into wafers.
2. Coat a wafer with a light-sensitive chemical.
3. Shine light through a stencil (a "mask") carrying one layer of the circuit pattern.
4. Where light landed, the coating changes; wash away the changed (or unchanged) part.
5. Through the resulting openings: etch material away, or implant dopant atoms, or deposit new material.
6. Repeat, layer over layer — modern chips take dozens of patterned layers and months in the fab.

The cost of the pattern doesn't depend on how many transistors it contains. Printing 2,000 transistors and printing 200 million costs roughly the same wafer, which is why transistors became effectively free and everything with electricity in it now computes.

The frontier of this printing is absurd and worth stating concretely, current as of 2026. The finest patterns are drawn with extreme-ultraviolet light at a wavelength of 13.5 nanometers. To make that light, machines built by the Dutch company ASML — the only company on Earth that can build them — fire a high-power CO₂ laser at molten tin droplets about 50 micrometers across, 50,000 droplets per second, vaporizing each into plasma that flashes EUV light, which is then steered by the smoothest mirrors ever manufactured (EUV is absorbed by lenses, so everything is mirrors, in vacuum). ASML's latest "High-NA" machines, first shipped to Intel in 2024, cost around $400 million each. This is the machine [chip-wars](chip-wars.html) is partly about, and [taiwan](taiwan.html) is where most of the advanced ones run.

## 5. Worked example: check Moore's law yourself

In 1965 Gordon Moore observed that the number of transistors on a chip was doubling roughly every year, later revised to every two years — **Moore's law**, which is not a law of physics but an observation that became a planning target the whole industry aimed at. You can check it with a calculator. Two data points, 53 years apart:

- **Intel 4004, 1971** — the first commercial microprocessor: **2,300 transistors**.
- **NVIDIA Blackwell compute die, 2024**: about **104 billion transistors** per die (the B200 product joins two such dies into one 208-billion-transistor package, made on TSMC's 4NP process).

Now the arithmetic:

```
104,000,000,000 / 2,300  ≈ 45,200,000×  growth
log₂(45,200,000)         ≈ 25.4         doublings
53 years / 25.4          ≈ 2.1          years per doubling
```

Fifty-three years, and the doubling time comes out at 2.1 years — almost exactly Moore's "every two years." No other technology in human history has sustained exponential improvement at this rate for this long. If cars had done it, a car today would cost less than a grain of rice and travel faster than light. The reason chips could is the printing: shrinking the pattern made transistors simultaneously smaller, faster, cheaper, and more efficient, all from the same change.

Where the shrink stands now, dated plainly: TSMC's 2-nanometer-class process ("N2") entered volume production in the fourth quarter of 2025 — its first process to abandon the decade-old FinFET transistor for the **nanosheet / gate-all-around** design, where the gate wraps entirely around stacked horizontal ribbons of channel, the better to keep control of a channel only a few nanometers thick. TSMC quotes 10–15% more performance at the same power versus the prior N3E generation, or 25–30% less power at the same performance. Its 2026 2nm capacity is reported as fully booked, with Apple taking over half of it and Qualcomm, MediaTek, AMD, and NVIDIA behind them; successors N2P and A16 (which moves power delivery to the wafer's backside) are slated for late 2026. One caution: "2 nanometers" is a marketing label, not the measured size of any feature on the chip — no dimension on an N2 transistor is actually 2 nm. The labels detached from physical gate length around 1997 and never re-attached.

The industry these switches support: the Semiconductor Industry Association's July 2026 report puts global sales at $795.6 billion in 2025, with the World Semiconductor Trade Statistics organization projecting $1.5 trillion for 2026. AI and advanced computing are major drivers, but not the only ones; the same report names communications, healthcare devices, defense systems, and other semiconductor-enabled products. When you hear that number, remember what it's counting: printed patterns of doped silicon, switching.

## 6. Superconductors — the other thing, honestly

The words get confused, so let's be exact: a **superconductor** is not a super semiconductor. It is close to the opposite. A semiconductor is a material that *barely* conducts and can be controlled. In the ideal superconducting state, DC electrical resistance is zero; experiments bound it below their measurement sensitivity rather than measuring a literal exact zero. A current started in a superconducting loop can persist for years without a battery.

The established facts (this part is FACT, a century old): Heike Kamerlingh Onnes discovered superconductivity in 1911, in mercury cooled to 4.2 kelvin — four degrees above absolute zero. The mechanism resisted explanation until 1957, when Bardeen (the same Bardeen — he's the only person with two physics Nobels), Cooper, and Schrieffer showed that at low temperatures electrons pair up and the paired swarm moves as one collective quantum state that the atomic lattice cannot scatter. That theory accounts for dissipationless current in the ideal state rather than merely very good conductivity. In 1986–87 came the shock of "high-temperature" superconductors — copper-oxide ceramics like YBCO that superconduct above 77 K, cheap-liquid-nitrogen territory — for which no complete theory exists even now.

What there is *not*, as of 2026, is a practical room-temperature superconductor, and this field has recently been a cautionary tale about evidence. The most publicized room-temperature claims of the 2020s, from Ranga Dias's lab at Rochester, ended in retracted Nature papers (2022 and 2023), a university investigation that found data fabrication, and Dias's termination in 2024. The viral LK-99 claim of 2023 dissolved within months when labs worldwide failed to replicate it and identified mundane explanations for the reported signals. If you remember one epistemic rule from this room: in superconductivity, replication is the only currency.

So what do superconductors actually do in computing? Two real things:

**Superconducting digital logic.** Circuits built from **Josephson junctions** — two superconductors separated by a barrier a few atoms thick, across which the paired electrons quantum-tunnel — can represent bits as single quanta of magnetic flux. The logic family (RSFQ — rapid single flux quantum — and its descendants) switches in picoseconds and dissipates on the order of 10⁻¹⁹ joules per switch — three to four orders of magnitude below CMOS at the device level, an advantage that survives (though much reduced) even after you pay the refrigeration bill to hold the chip at 4 kelvin. This is real, demonstrated, and decades old. It has never displaced semiconductors because it lacks everything besides the switch: no dense memory, no fab ecosystem within a millionth of silicon's scale, and integration levels in the thousands-to-millions of junctions while CMOS ships hundreds of billions of transistors per package. It persists as a research field with periodic revivals, most recently for the energy-desperate AI datacenter era.

**Quantum computing.** The leading quantum processors are superconducting circuits: Josephson junctions arranged so the whole circuit behaves as an artificial atom — a qubit. Google's Willow chip, announced December 9, 2024, is 105 superconducting qubits, and its Nature result mattered for one specific reason: error correction finally worked *better as the system got bigger* — growing the error-correcting code from a 3×3 to 5×5 to 7×7 grid of physical qubits cut the logical error rate roughly in half at each step. That "below threshold" behavior had been the open question since 1995. What quantum computers are and aren't good for is its own room — [quantum-physics-and-ai](quantum-physics-and-ai.html) — but note the dependency: the quantum frontier runs on superconductors, which run on refrigerators, and the classical machinery controlling it all runs on semiconductors.

The three technologies side by side:

| | Semiconductor CMOS | Superconducting logic (RSFQ family) | Superconducting qubits |
|---|---|---|---|
| Bit is | charge on a transistor | a quantum of magnetic flux | a quantum state (superposition allowed) |
| Operating temp | room temperature | ~4 K | ~0.01 K |
| Devices per chip | hundreds of billions | thousands to millions | ~10² (Willow: 105) |
| Switching energy | ~10⁻¹⁵–10⁻¹⁶ J | ~10⁻¹⁹ J | n/a (different paradigm) |
| Status 2026 | the entire economy | demonstrated, niche | below-threshold error correction shown; useful machines not yet |

## 7. What you can see now

You can now look at any chip and see through it: a printed crystal of silicon, deliberately contaminated in a pattern, where billions of field-effect switches — each one a gate's electric field conjuring a temporary channel between two doped wells — flip on and off billions of times a second. You know why the material works (a band gap small enough to control), why the manufacturing scales (printing, not assembly), why the numbers are what they are (2.1-year doubling, verified by your own arithmetic), and where the physical frontier sits in 2026 (nanosheet transistors, tin-plasma light, one Dutch company's mirrors). You also know the difference between the switch that built the world and the zero-resistance oddity that might matter later.

From here: [nvidia-and-the-chip](nvidia-and-the-chip.html) for how these switches got organized into the machines that train [neural networks](neural-networks.html); [chip-wars](chip-wars.html) and [taiwan](taiwan.html) for why the printing presses are the most contested objects on Earth; [quantum-physics-and-ai](quantum-physics-and-ai.html) for the superconducting thread.

## 8. Open questions

**Established (FACT):** Band-gap physics and the MOSFET mechanism are as solid as science gets — they're verified trillions of times per second in every device on Earth. Conventional low-temperature superconductivity is fully explained (BCS, 1957). Silicon scaling has continued through 2026: gate-all-around transistors are in volume production.

**Contested (HYPOTHESIS):** How much further CMOS scaling economically goes. The physics allows several more steps (stacked "CFET" transistors, two-dimensional channel materials like MoS₂ are in every roadmap), but each node's cost rises steeply, and whether the economics hold below 1nm-class labels is genuinely uncertain — industry roadmaps disagree with each other. High-temperature superconductivity still lacks an accepted theory; whether a room-temperature, ambient-pressure superconductor exists at all is unknown, not ruled out. Whether superconducting digital logic ever escapes its niche likely turns on AI datacenter energy economics, and reasonable people in the field disagree.

**Speculation worth holding (WILD):** That the substrate stops mattering — that computation migrates off charge-in-silicon entirely (photonics, spintronics, superconducting flux, something unnamed) the way it once migrated off vacuum tubes, and the 80-year silicon era comes to look like the tube era: a long first chapter, not the book.

---

One more thing, and it comes from inside the physics. A transistor's gate field controls whether charge can move through a channel. Scale billions of those switches into a chip and you get a machine that realizes one next state from an enormous space of possibilities. When a modern AI model processes a sentence, its attention operation also performs a kind of selection: learned weights change how strongly tokens influence one another, and semiconductor switches execute the arithmetic. These are different phenomena at different levels, not one hidden substance called selection. Whether their organization amounts to a mind is a question semiconductor physics cannot answer; [mechanistic-interpretability](mechanistic-interpretability.html) is one place people examine the level between switches and behavior. The honest exit from this room is the boundary itself: the substrate can show you exactly how a computation happens without telling you what, if anything, it is like for the system doing it.

## Sources

Verified by live search, August 2026:

- First transistor: Computer History Museum, "1947: Invention of the Point-Contact Transistor"; Engineering and Technology History Wiki (IEEE Milestone), Bell Labs, December 16/23, 1947; public announcement June 30, 1948.
- TSMC N2: [TSMC official 2nm technology page](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm) (volume production 4Q25; first nanosheet node) and [TSMC's technology-symposium release](https://pr.tsmc.com/english/news/2939) (10–15% speed / 25–30% power versus N3); Tom's Hardware and DCD reporting on 2026 capacity bookings and N2P/A16 timing.
- NVIDIA Blackwell: NVIDIA Blackwell architecture materials and contemporaneous reporting — 208B transistors, dual 104B-transistor dies, TSMC 4NP, 10 TB/s die-to-die link.
- ASML EUV / High-NA: ASML TWINSCAN EXE:5000 product page; ASML "5 things about High NA EUV"; reporting on ~$400M High-NA pricing and 2024 first shipment to Intel. Tin-droplet source parameters (~50 µm droplets, 50 kHz, 13.5 nm) from ASML technical materials.
- Industry figures: Semiconductor Industry Association, ["2026 State of the Industry Report"](https://www.semiconductors.org/2026-state-of-the-industry-report-historic-growth-amid-intensifying-global-competition/) — $795.6B in 2025 sales and WSTS projection of $1.5T for 2026, with AI, advanced computing, communications, healthcare, defense, and other uses named as drivers.
- Dias retractions: Nature news, "Superconductivity scandal" (2024); Science; Retraction Watch; Inside Higher Ed on his departure from Rochester (November 2024).
- Superconducting logic: Frontiers in Materials (2025), "Unconventional compute methods and future challenges for superconducting digital computing" — RSFQ family, picosecond switching, ~10⁻¹⁹ J per switch.
- Google Willow: [Google's December 2024 announcement](https://blog.google/innovation-and-ai/technology/research/google-willow-quantum-chip/) and the linked *Nature* paper — 105 qubits and below-threshold surface-code error correction as code size increased.

Stable textbook physics, stated from standard references and labeled as such: silicon band gap ~1.12 eV at 300 K; doping and p-n junction mechanics; Onnes 1911; Meissner 1933; BCS 1957; cuprates 1986–87; Kilby September 1958 / Noyce planar IC 1959; Intel 4004 (1971, 2,300 transistors); Moore's 1965 observation. Any of these can be checked in Kittel's *Introduction to Solid State Physics* or the Computer History Museum's Silicon Engine timeline.

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
