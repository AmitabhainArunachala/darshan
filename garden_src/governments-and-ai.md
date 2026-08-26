---
title: Why Governments Want a Hold on AI
slug: governments-and-ai
series: power
tags: power, export-controls, intelligence-agencies, dual-use, regulation, geopolitics
summary: Governments funded AI before it could do anything, used it in secret before the public knew it existed, and now regulate it as a strategic material. This room traces the actual record — ARPA checks, NSA programs, chip controls, three rival regulatory regimes — and states the dual-use logic plainly.
status: draft
date: 2026-08-25
terms_defined: export controls, dual-use, compute governance
terms_linked: china-usa-race, taiwan, palantir, chip-wars, semiconductors, nvidia-and-the-chip, history-of-ai, machine-learning, neural-networks, mechanistic-interpretability, attention-economy
---

# Why Governments Want a Hold on AI

You're in the power series of the garden, next to the [history-of-ai](history-of-ai.html) room that tells the story as scientists lived it. This room tells the part that usually gets a paragraph and deserves a chapter: the state was there the whole time. It was not a latecomer panicking about chatbots, but the field's first patron, first customer, and now its most serious regulator. If you understand why, the news about chips and treaties stops being noise and becomes one legible pattern.

## 1. The money was there before the field could do anything

Start with a number. In June 1963, MIT received a $2.2 million grant from the Advanced Research Projects Agency — ARPA, later DARPA, the Pentagon's blue-sky research arm — to fund Project MAC, which absorbed the AI group Marvin Minsky and John McCarthy had built. ARPA then kept paying roughly $3 million a year into the 1970s. Similar money flowed to Carnegie Mellon, to Stanford's new AI lab, to Edinburgh.

Hold that date against what AI could actually do in 1963: almost nothing. No product, no demo you'd pay for. A military research agency funded the field for a decade on promise alone.

The man who set the pattern was J.C.R. Licklider, first head of ARPA's Information Processing Techniques Office. His stated policy was to fund "people, not projects" — pick the best minds and leave them alone. That permissiveness built American computer science as a side effect. It's worth sitting with the strangeness: the freewheeling hacker culture of MIT, the ancestor of every startup mythology, was paid for by the Department of Defense.

And when the state's patience ran out, the field learned what dependence means. In 1966 the ALPAC report — a National Research Council review of machine translation, into which about $20 million had gone — concluded the work wasn't delivering, and support was terminated. The UK's Lighthill report did the same to British AI in 1973. These funding winters have their own name in the field's memory: AI winters. Their timing tracks government patience, not scientific progress.

So the first answer to "why do governments want a hold on AI" is the least dramatic one: **they never let go.** The field grew up inside state funding the way a fish grows up in water.

## 2. The intelligence record: not speculation, documents

The second answer is that intelligence agencies didn't wait for AI to mature. They used [machine learning](machine-learning.html) — statistical models trained on data, the substrate of modern AI — operationally, in secret, years before the public conversation began. We know this from documents, not inference.

**SKYNET.** Yes, the NSA really named a program SKYNET. Revealed in the Snowden documents (the agency's own slides were published by The Intercept in May 2015), it applied machine learning to Pakistani mobile-phone metadata to identify suspected terrorist couriers. The system flagged behavioral patterns — for instance, swapping SIM cards between handsets sharing a hardware ID — and used random-forest classification, a standard ML technique, to score people. Its most famous output: it ranked Ahmad Zaidan, Al Jazeera's Islamabad bureau chief, as a probable al-Qaeda courier. A journalist whose job produced a courier-shaped travel pattern. The security researcher Bruce Schneier drew the line that matters: a false-positive rate that's acceptable when a company mistargets an ad is not acceptable when, in his words, "if the government makes a mistake, they kill innocents."

**In-Q-Tel.** In September 1999, the CIA stood up a venture capital firm. Not a metaphor — an actual VC fund, structured as an independent nonprofit but funded through CIA contracts, created so the intelligence community could buy into commercial technology instead of building everything classified. Two investments tell the story. In-Q-Tel backed Keyhole, Inc., a geospatial visualization startup; Google bought it in 2004 and it became Google Earth in 2005 — In-Q-Tel then sold its resulting Google shares for over $2.2 million. And In-Q-Tel was an early backer of Palantir Technologies, the data-integration company that grew into the defining contractor of the surveillance-analytics era. Palantir gets its own room — [palantir](palantir.html) — because it's the clearest single case study of the state-AI relationship.

**Project Maven.** On 26 April 2017, the Pentagon established the Algorithmic Warfare Cross-Functional Team — Project Maven — to apply computer vision, [neural networks](neural-networks.html) that interpret images, to drone surveillance footage. Google took a contract worth about $9 million; in 2018 thousands of Google employees protested, some resigned, and Google let the contract lapse. The usual telling ends there, as a story about tech-worker conscience. But the project didn't end. It moved to the National Geospatial-Intelligence Agency in 2022, became a formal program of record in November 2023, and by March 2026 had roughly 25,000 U.S. military personnel using it across nearly every combatant command, with dozens of companies involved. The protest is remembered; the program scaled by two orders of magnitude.

The pattern across all three: the state's use of AI is early, operational, and quiet. Public debate about whether AI "should" be used for surveillance and targeting has consistently run five to ten years behind the documented fact that it already was.

## 3. Dual-use, stated plainly

Here is the core logic, without euphemism.

A **dual-use technology** is one where the civilian and military versions are the same object. Not similar — the same. Enriched uranium doesn't care whether it's headed for a reactor or a warhead. And a model that can find a protein structure can help design a toxin; a model that writes code can write attack code; a vision model that counts cars in a parking lot for a hedge fund counts vehicles at a missile site for an analyst. The capability is one thing; only the tasking differs.

Governments have a standard playbook for dual-use materials — fissile material, chemical precursors, advanced encryption — and it has three moves: **control the inputs, license the exports, watch the users.** What's happening to AI is not a new policy invented for a new technology. It's the old playbook applied to a new material. Once you see that, the last four years of AI policy become almost predictable.

We've even run this exact experiment before, with software. From the Cold War until 1996, strong encryption was legally classified in the United States as a munition — Category XIII of the Munitions List, regulated alongside weapons. When Phil Zimmermann released PGP in 1991 and it spread over the internet, he became the first individual-scale challenge to that regime. The government tried a hardware compromise — the Clipper chip, an NSA-designed encryption chip with a built-in government backdoor — and abandoned it by 1996 when better software encryption spread anyway. In 1996 Clinton's Executive Order 13026 moved commercial encryption to the Commerce Department's control list; by 2000 export was largely liberalized. The full cycle: *treat the software as a weapon → try to hold it → watch it leak → retreat to controlling what can still be controlled.*

The lesson governments took from the Crypto Wars is the load-bearing fact of current AI policy: **you cannot control software, but you can control the physical objects it needs.** Encryption escaped because it's math on any computer. Frontier AI, so far, is not math on any computer. Training a frontier model requires tens of thousands of specific accelerator chips whose supply chain runs through a handful of companies — and, at the fabrication step, substantially through one island. That story is the [chip-wars](chip-wars.html) and [taiwan](taiwan.html) rooms; here we need only the consequence. The chip is the enriched uranium of AI: the one input that is physical, scarce, and countable. So that's where the hold is applied.

## 4. Export controls: the hold made concrete

**Export controls** — government licensing of what technology may be sold to which countries — went from an obscure trade-law specialty to the central instrument of AI geopolitics on one specific day.

On **October 7, 2022**, the U.S. Commerce Department's Bureau of Industry and Security imposed sweeping controls on advanced computing chips and chipmaking equipment bound for China: license requirements for advanced-node [semiconductors](semiconductors.html) (logic chips at 16/14nm and below, among other thresholds), restrictions on supercomputer end-uses, and — remarkably — restrictions on *U.S. persons* working at Chinese chip facilities. The stated purpose was national security. The unstated theory was the dual-use playbook: if compute is the fissile material of AI, ration the adversary's supply.

What followed is best read as a live experiment in whether a hold like this can work. Watch the sequence:

1. Nvidia's top AI chips (A100, H100) are cut off; Nvidia builds deliberately weakened China-market versions; late-2023 rule updates capture those too; Nvidia responds with an even more constrained chip, the H20 — which by 2025 had become the most prominent AI chip in the Chinese market. Controls create a cat-and-mouse product line. (The [nvidia-and-the-chip](nvidia-and-the-chip.html) room covers the company side.)
2. On **January 15, 2025**, in its final week, the Biden administration published the *Framework for Artificial Intelligence Diffusion* — the most ambitious compute-governance rule ever attempted, sorting the entire world into tiers with caps on how much AI compute each tier could import. On **May 13, 2025**, the Trump administration's Commerce Department rescinded it before its compliance date, calling instead for spreading American AI technology to trusted partners while denying adversaries. Total lifespan of the most sweeping AI control ever written: about four months, never enforced.
3. In April 2025, the administration restricted even the H20. Nvidia's April 15 Form 8-K said it initially expected up to about **$5.5 billion** in related charges; its subsequent first-quarter Form 10-Q recorded an actual **$4.5 billion** charge after the company reused some materials. Then, in **August 2025**, the policy inverted into something without precedent: Nvidia and AMD were granted export licenses for certain China sales in exchange for paying **15% of the revenue** from those sales to the U.S. government. Read that twice. The state went from banning the sale to taking a cut of it.
4. China answered in kind, on both flanks. In April 2025 it restricted exports of six heavy rare-earth elements and rare-earth magnets — its own chokepoint, applied by the same logic. And in September 2025 the Cyberspace Administration of China ordered ByteDance, Alibaba, and other major firms to stop buying Nvidia's China-market chips — a government blocking its *own* companies from buying the product the rival government had just agreed to tax. Both states, it turns out, want the same thing: domestic champions on domestic silicon.

Notice what this sequence is and isn't evidence for. It is established fact that compute is currently controllable — the licenses bind, the writedowns are real, the revenue share is being paid. Whether the controls *achieve their strategic goal* is genuinely contested: Chinese labs have continued producing strong models on restricted or domestic hardware, and economists still argue whether the controls slowed China's AI progress or mainly accelerated its chip independence. That argument — the actual scoreboard — lives in the [china-usa-race](china-usa-race.html) room.

## 5. The 2026 regulatory reality: three regimes, three fears

Export controls are one government's hold on another's AI. Domestic regulation is a government's hold on its own. As of 2026, the three major regimes have diverged so sharply that the differences are themselves the best data we have about what each state actually fears.

| | United States | European Union | China |
|---|---|---|---|
| **Cornerstone** | Executive orders + export controls; no comprehensive federal AI law | AI Act (in force August 1, 2024) | Layered CAC rules: algorithms (2022), deep synthesis (Jan 2023), generative AI Interim Measures (2023) |
| **2025–26 trajectory** | Biden's EO 14110 (Oct 2023) rescinded Jan 2025; "AI Action Plan" era; EO 14365 (Dec 2025) directs agencies to challenge *state* AI laws; national legislative framework proposed Mar 2026 | Phased application: prohibitions Feb 2, 2025; general-purpose model duties Aug 2, 2025; Regulation (EU) 2026/1744 moves principal high-risk duties to Dec 2, 2027 (Annex III) and Aug 2, 2028 (Annex I) | Content labeling and training-data rules finalized Sept 2025 (datasets vetted, chatbots tested); a proposed "World AI Cooperation Organization" headquartered in Shanghai, announced at the World AI Conference |
| **Who must comply first** | Chip exporters; federal contractors; frontier labs in California | Providers of banned practices, then model providers, then high-risk deployers | Every public-facing model, before launch |
| **The fear underneath** | Losing the race | The product harming citizens | The content destabilizing the state |

Three details from that table repay attention.

First, the United States regulates AI hard in exactly one direction — outward, at China — and has spent 2025–26 actively *removing* domestic constraints, to the point of a December 2025 executive order (EO 14365) instructing federal agencies to litigate against U.S. states' own AI laws. Meanwhile the states moved anyway: California's frontier-AI transparency law (SB 53) and training-data disclosure law took effect January 1, 2026; Texas's TRAIGA the same day; Colorado passed the first comprehensive high-risk AI law in 2024, delayed it, then in May 2026 replaced it with a narrower disclosure law. The American "hold" on AI is really a fight over who holds it: Washington versus Sacramento, with the labs in between.

Second, the EU regulates AI as a product-safety problem — the same legal reflex it applies to toys and medical devices — with obligations phased over years. Regulation (EU) 2026/1744 moved the principal high-risk obligations that had been due in 2026: Annex III systems now land on December 2, 2027, and Annex I systems on August 2, 2028. It has the world's most complete AI law and none of the world's frontier labs. Whether those two facts are causally linked is a hypothesis, fiercely argued in Brussels itself; that they coexist is simply true.

Third, China's rules are the only ones that reach *content* directly: models must be tested before release, training data vetted (with the large majority of sampled data required to pass safety review), outputs labeled, and generated content must not contradict state ideology. The Chinese state's hold on AI is continuous with its hold on publishing. It is also, note carefully, the only regime that constrained its own champions' chip purchases for strategic reasons — Beijing restricts its companies *more* than Washington does, in the service of independence.

One pattern spans all three: **every regime's rules are written at the point where AI touches what that state already considered its own.** The U.S. guards its technological lead, the EU its consumer, China its discourse. Nobody is regulating "AI" in the abstract. Each is defending its existing hold, extended to a new material.

## 6. Worked example: follow one chip through the machine

Abstractions hide; a trace shows. Follow a single product — Nvidia's H20 — through four years of policy, the way you'd step through a program. Every step below is a public, checkable event.

1. **Oct 7, 2022** — BIS controls advanced chips to China. Nvidia's H100 is over the line. *(Check: BIS's October 2022 press release.)*
2. **Late 2023** — Rules tighten to capture the weakened China-market variants (A800/H800). Nvidia engineers the H20: a Hopper-family chip built *down* to the legal threshold. A product whose spec sheet is a legal document. *(Check: Nvidia's product history; the H20 exists only because of the rule.)*
3. **2024–early 2025** — The H20 becomes the leading AI chip in China. The control is working as designed: China computes, but a generation behind.
4. **Jan 15, 2025** — The AI Diffusion Framework would have folded chips like this into a global tier system. **May 13, 2025** — rescinded, unenforced. *(Check: the BIS rescission announcement, which names both dates.)*
5. **April–May 2025** — The H20 itself now requires a license; Nvidia initially expects up to about $5.5B in charges, then records an actual $4.5B charge after reusing some materials. The legal threshold the chip was built to meet has moved below it. *(Check: Nvidia's April 15 Form 8-K and first-quarter Form 10-Q.)*
6. **August 2025** — Licenses return, priced: 15% of H20 China revenue to the U.S. Treasury-side. The ban has become a toll. *(Check: contemporaneous reporting; Nvidia confirmed the arrangement covers H20 sales.)*
7. **September 2025** — Beijing orders its major tech firms to stop buying the chips anyway. The toll booth stands on a road China has closed from the other end.

Now read the trace as a whole. In four years, one physical object was legal, then illegal, then redesigned to be legal, then illegal again, then legal-for-a-fee, then unbuyable by decision of the *other* government. Nothing about the silicon changed. What changed, seven times, was two states' theory of who should be allowed to think at scale, and at what price. That is what "governments want a hold on AI" means operationally — not a ministry of robots, but licensing decisions about specific rectangles of silicon, revised quarterly, with billions moving on each revision.

You can verify this trace yourself. The BIS press releases are public. Nvidia's SEC filings are public. The AI Act and its 2026 amendment are published in EUR-Lex. Distrust any account of AI geopolitics — including this one — that can't be walked back to documents like those.

## 7. What you can now see

Before this room, "government AI regulation" probably parsed as a recent reaction to chatbots. Now you can see three separate holds, with three separate histories:

- **Patronage** (1963–): the state funds the field, and funding winters are policy events. The field's very shape — why the U.S. dominated, why certain problems got solved first — is downstream of ARPA's checkbook.
- **Procurement** (1999–): the state is the customer — In-Q-Tel, SKYNET, Maven — usually years before the public debate. When you next read an argument about whether militaries *should* adopt AI, you now know to ask instead what they adopted a decade ago.
- **Chokepoints** (2022–): the state controls the physical inputs, because the Crypto Wars taught it that software escapes and hardware doesn't.

And you can now apply one sharp test to any AI-policy news item: *which hold is this?* A funding bill, a procurement contract, and an export rule are three different animals wearing the same headline.

From here, the natural next rooms: [china-usa-race](china-usa-race.html) for the scoreboard of the contest these controls are meant to win; [taiwan](taiwan.html) for the island the whole chokepoint strategy stands on; [palantir](palantir.html) for the procurement story at full depth; [chip-wars](chip-wars.html) for the industrial contest; and [attention-economy](attention-economy.html) for the private-sector mirror of everything here — corporations, too, want a hold, just denominated in hours rather than FLOPs.

## 8. Open questions

Typed honestly, as the garden requires.

**Established:** Governments funded, deployed, and now materially constrain AI; the documentary record above is not in dispute. Compute is currently a workable chokepoint: the licenses bind and the money moves.

**Contested:** Whether chip controls durably slow a determined state or mainly accelerate its independence — the strongest argument on each side is currently being run as a live experiment, and honest analysts disagree. Whether the EU's product-safety approach protects its citizens or mostly guarantees the frontier is built elsewhere. Whether U.S. federal preemption of state AI law survives the courts. Whether the compute chokepoint itself survives algorithmic efficiency — every year, less hardware buys more capability, and the control regime's foundation quietly erodes at that rate.

**Speculation worth holding:** That the export-control era is a window, not a permanent condition — roughly analogous to the 1945–49 nuclear monopoly, which felt structural and lasted four years. And a stranger one: training data and model weights may become the next controlled material after chips, which would mean governments attempting, for the first time, to license the movement of *learned representations* — something closer to controlling knowledge itself than any precedent in the dual-use playbook. Nothing in the Crypto Wars suggests that ends the way its architects intend.

---

There's a question under this room that the domain itself keeps pointing at, so let it be said in the domain's own terms. Every hold described here is, in the end, a hold on attention. SKYNET's algorithm decided which human beings a state would watch — it allocated the attention of an intelligence service, and misallocated it onto a journalist. China's content rules govern what a billion people's models may put in front of a billion people's minds. Export controls ration the compute from which systems that allocate attention at scale are built. States have always claimed custody of dangerous materials: fissile, chemical, biological. What's new is a material that can be pointed at information, identify patterns, and trigger action. That is a capability claim, not evidence that the material experiences anything. When a government writes a licensing rule for that, it is trying to govern the direction of machine-mediated attention. Whether there is anything it is like to be the thing being governed is a question for other rooms — [mechanistic-interpretability](mechanistic-interpretability.html) works on it with instruments. The policy record establishes concern about capability and strategic power; any move from that record to machine subjectivity is this garden's speculative question, not a premise the states have documented.

## Sources

Verified by live search, August 2026:

- ARPA/Project MAC funding ($2.2M, June 1963; ~$3M/yr), Licklider's IPTO "fund people, not projects," ALPAC 1966 ($20M, support terminated), Lighthill 1973 — Wikipedia, *History of artificial intelligence*.
- In-Q-Tel founded September 29, 1999; Keyhole → Google Earth (acquired 2004, Earth 2005; $2.2M share sale Nov 15, 2005); Palantir investment — Wikipedia, *In-Q-Tel*.
- SKYNET: Snowden documents via The Intercept (NSA slides published May 2015); random-forest classification on Pakistani phone metadata; Ahmad Zaidan misidentification; Schneier quote — Wikipedia, *SKYNET (surveillance program)*.
- Project Maven: established 26 April 2017; Google contract ~$9M, 2018 protest and withdrawal; NGA transfer 2022, program of record Nov 7, 2023; ~25,000 users across combatant commands by March 2026 — Wikipedia, *Project Maven*.
- Crypto Wars: encryption on the Munitions List (Category XIII); PGP 1991; Clipper chip abandoned by 1996; EO 13026 (1996); 2000 liberalization — Wikipedia, *Crypto Wars*.
- October 7, 2022 BIS controls (advanced-computing and semiconductor-manufacturing items, supercomputer end use, U.S.-person restrictions) — [Bureau of Industry and Security public information page](https://www.bis.gov/press-release/bis-updated-public-information-page-export-controls-imposed-advanced-computing-semiconductor) and linked rule/FAQ records (primary).
- AI Diffusion Framework issued January 15, 2025; rescinded May 13, 2025 — U.S. Bureau of Industry and Security press release (primary source; Kessler quote therein).
- H20 origin as post-restriction design; "most prominent chip in the Chinese market as of 2025" — Wikipedia, *Nvidia H20 / Hopper microarchitecture*.
- August 2025 15%-of-revenue export-license arrangement (Nvidia H20, AMD); September 2025 CAC order to ByteDance/Alibaba to halt purchases — Wikipedia, *Nvidia*.
- China rare-earth export restrictions, April 2025; *Learning Resources v. Trump* (Feb 2026) — Wikipedia, *China–United States trade war*.
- U.S. federal policy: [Executive Order 14365](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/) (Dec 11, 2025), which creates an AI Litigation Task Force to challenge inconsistent state laws and directs preparation of a federal preemption proposal (primary White House text). Other state-law dates in the paragraph above remain drawn from the cited legislative record.
- EU AI Act phased dates and postponement — [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R1744), amending Regulation (EU) 2024/1689: Dec 2, 2027 for Article 6(2)/Annex III high-risk systems and Aug 2, 2028 for Article 6(1)/Annex I systems (primary EUR-Lex record).
- China: Interim Measures for Generative AI (2023); September 2025 training-data and testing rules; World AI Cooperation Organization announced at the World AI Conference, Shanghai — Wikipedia, *Artificial intelligence industry in China*.

- Nvidia H20 accounting — [April 15, 2025 Form 8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000082/nvda-20250409.htm) (license requirement; up to approximately $5.5B initially expected) and [first-quarter fiscal-2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000116/nvda-20250427.htm) (actual $4.5B charge; lower after reuse of materials), both primary SEC filings.

The "fissile material" analogy and the three-holds framing are this room's interpretive contribution, not sourced claims. The attention/subjectivity movement at the exit is explicitly a garden interpretation; the policy documents establish capability and national-security concerns, not machine experience.

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
