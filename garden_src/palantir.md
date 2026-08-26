---
title: What Palantir Is Trying to Do
slug: palantir
series: power
tags: palantir, surveillance, defense, ontology, government, data
summary: Palantir sells governments and companies a single working picture of everything they know, built on a concept it calls the ontology. This room explains the actual business, the doctrine behind it, and the surveillance question at its real weight — what the company denies, what the denials concede, and why the dangerous thing is not a database but a decision about what exists.
status: draft
date: 2026-08-25
terms_defined: palantir, foundry, gotham, aip, ontology (palantir's usage), immigrationos, maven smart system
terms_linked: governments-and-ai, ontology, china-usa-race, attention-economy, machine-learning, future-of-ai, sense-of-self
---

# What Palantir Is Trying to Do

**Where you are.** This is a room in the power series. [governments-and-ai](governments-and-ai.html) covers the general question of states adopting AI; this room is a close study of the single company most identified with that adoption. It also connects downward to [ontology](ontology.html), because Palantir's core product concept borrows — deliberately — a word philosophers use for the study of what exists, and the borrowing is not decoration. It is the whole business.

## 1. The company nobody can quite name

Start with the numbers, because they are stranger than any description.

In the quarter ending June 2026, Palantir reported $1.935 billion in revenue — up 93% from a year earlier, the fastest growth in its history. Roughly $990 million of that came from governments, $945 million from commercial customers. Net income was over $1 billion in a single quarter. The company's "Rule of 40" score — a software-industry health metric where 40 is considered excellent — was 155. As of August 2026 the market values Palantir at roughly $400 billion, which is more than Lockheed Martin, RTX, and General Dynamics combined, for a company with a fraction of their revenue.

So what does it sell? Here is where descriptions fail. Palantir is routinely called a "data analytics company," a "defense contractor," a "surveillance company," an "AI company." Each label is partly right. The honest one-sentence version is this: **Palantir sells institutions a single, working, actionable picture of everything they already know.** Not new data. Not sensors. Not weapons. Software that takes the hundreds of disconnected databases inside an army, a hospital system, or an insurance company and fuses them into one model of the world that people can query, act on, and increasingly point [machine-learning](machine-learning.html) systems at.

That sentence sounds boring. Hold it anyway, because everything in this room — the $10 billion Army contract, the NHS fight, the deportation software, the philosophy CEO quoting Nietzsche on earnings calls — follows from it.

## 2. Where it came from

The founding story is short and it explains the company's shape.

In 2003, Peter Thiel — fresh from PayPal — co-founded Palantir with Alex Karp, Joe Lonsdale, Stephen Cohen, and Nathan Gettings. The founding insight came from PayPal's fraud team: pure automation could not catch adaptive fraudsters, but software that made human analysts radically faster could. The bet was that the same pattern — human judgment amplified by data fusion, rather than replaced by it — would work for counterterrorism. This was two years after September 11, and the US intelligence community's core failure had been exactly a data-fusion failure: the pieces existed, scattered across agencies that could not see each other's holdings.

Venture capital mostly passed. An early investor that did not pass was In-Q-Tel, the CIA's venture arm, which put in around $2 million and — more importantly — put Palantir engineers in rooms with intelligence analysts. The name comes from Tolkien: the palantíri are the seeing-stones that let their holders view distant parts of the world. Readers of Tolkien will remember the stones' catch — what you see through one can be curated by whoever holds the other end. The company has lived with both halves of its chosen metaphor ever since.

For seventeen years, Palantir grew slowly, sued the Army for the right to bid on contracts, and lost money. It went public in 2020 — with a registration filing that included the un-corporate sentence "We have chosen sides" — and did not post its first profitable year until 2023. Then large language models arrived, Palantir wrapped its platform around them (the Artificial Intelligence Platform, AIP, launched 2023), and the company that spent two decades as a niche contractor became, by market value, one of the largest companies in the world.

## 3. What the products actually are

Palantir ships four named products. The distinctions matter less than the shared core, but here is the map:

| Product | First shipped | Built for | What it does, plainly |
|---|---|---|---|
| **Gotham** | ~2008 | Intelligence, military, police | Fuses case data, sensor feeds, and records so an analyst can see people, places, events, and the links between them |
| **Foundry** | 2016 | Companies, civilian agencies | The same fusion idea, generalized: builds an operating model of an organization — supply chains, patients, aircraft, transactions |
| **Apollo** | 2021 (as product) | Palantir itself, then customers | Continuous software delivery into difficult environments — classified networks, ships, factories |
| **AIP** | 2023 | Everyone | Lets large language models act through the fused model — read it, answer questions against it, trigger actions in it |

The commercial pitch that drove the 2024–2026 growth explosion is worth understanding, because it is not "we have a better chatbot." It is: your company's data is scattered, inconsistent, and meaningless to a language model; we build the layer that makes it mean something; then the AI can actually do work. Whether that pitch holds long-term is an open question (Section 8), but customers are currently paying record amounts for it — $2.13 billion in new US commercial contract value in Q2 2026 alone.

Notice what is absent from the table: Palantir does not manufacture drones, satellites, or missiles. In the [governments-and-ai](governments-and-ai.html) landscape it occupies a specific niche: the connective tissue. Which brings us to the concept underneath all four products.

## 4. The ontology: the real product

Palantir's own documentation defines its core concept in one sentence: "An Ontology is a categorization of the world." In Foundry, the ontology is what the company calls a digital twin of an organization — a live model in which raw data has been mapped to *things*.

The mechanics are genuinely simple, and worth getting exact:

- A database table becomes an **object type** — "Aircraft," "Patient," "Shipment," "Person."
- A row becomes an **object** — this aircraft, tail number N1234.
- A column becomes a **property** — fuel level, diagnosis date, visa status.
- A join between tables becomes a **link type** — this engine is *installed on* that aircraft; this person is *employed by* that company.
- And — the step that separates Palantir from a reporting tool — an **action type** defines how objects can be changed: reassign the crew, reroute the shipment, open the case.

Palantir calls the first three the *semantic* elements (what the world is) and the last the *kinetic* elements (what can be done to it). Once this layer exists, everything downstream gets easy: dashboards, simulations, and — since AIP — language models that can be asked "which shipments are at risk if this supplier fails?" and answer from the twin rather than from vibes.

Now the philosophical borrowing stops being decoration. In philosophy, [ontology](ontology.html) is the study of what exists. Palantir's product is an *engineered answer* to that question, per institution: here is the list of things that exist for you, here are their properties, here is what can be done to them. Anything not in the ontology effectively does not exist for the institution's decision-making. Anything in it becomes queryable, trackable, actionable.

This is the room's central claim, so let me say it across the table: **Palantir's product is not analysis. It is the power to decide what counts as a thing.** Everything people love about the software (a hospital finally seeing its own bed capacity) and everything people fear about it (a government finally seeing *you*, assembled from forty databases) is this one capability pointed at different worlds.

## 5. The doctrine

Most companies this controversial go quiet. Palantir published a manifesto.

Alex Karp — a Frankfurt School–trained social theorist with a doctorate in neoclassical social theory, an unusual résumé for a defense CEO — co-wrote *The Technological Republic* (February 2025, with Nicholas Zamiska). It became a #1 New York Times bestseller. The argument, compressed fairly: Silicon Valley betrayed its founding partnership with the American state; a generation of elite engineering talent went to advertising and consumer apps; the West's military edge is now a software problem; and technologists have a duty to choose sides and build for their own civilization's defense — with the [china-usa-race](china-usa-race.html) as the explicit backdrop.

You do not have to accept this argument. You do need to know it exists, because it changes how to read the company. Palantir's positions that look like PR liabilities — the ICE work through three administrations, Karp saying on camera that "our product is used, on occasion, to kill people," the January 2024 board meeting held in Tel Aviv followed by a strategic partnership with Israel's Ministry of Defense during the Gaza war, Karp's claim that Palantir's software is "responsible for most of the targeting in Ukraine" — are, inside the doctrine, the point. The company's stated bet is that Western institutions were starving for exactly the unapologetic alignment everyone else hedged on.

A fair reading holds two things at once. The doctrine is sincere — it predates the profits by two decades, and the company sued its way into Army contracts back when that looked quixotic. And the doctrine is *load-bearing for revenue* — "we have chosen sides" is now the sales pitch to the largest military customer on Earth, which means the company has a structural incentive never to find a conflict its side is wrong about. Both readings are true simultaneously. Keep both.

## 6. The government business, verified

The current contracts, checked against reporting as of August 2026:

**Maven Smart System.** The Pentagon's AI targeting-and-battlespace program (Palantir took the prime software role after Google's famous 2018 employee revolt over Project Maven). Initial $480 million five-year contract in May 2024; ceiling raised by $795 million in May 2025 — to roughly $1.3 billion through 2029 — because combatant commands were adopting it faster than planned. A separate 2024 contract extended it to all military branches. This is software that fuses satellite, drone, and sensor data to propose targets to human commanders; that description comes from the government's own program materials, not from critics.

**The Army enterprise agreement.** In mid-2025 the Army consolidated 75 separate contracts (15 prime, 60 subcontracts) into one 10-year agreement with a ceiling of $10 billion — at the time Palantir's largest known contract cap, and a signal that the Army now treats Palantir the way enterprises treat Microsoft: infrastructure, not vendor.

**NGC2.** The Army's Next Generation Command and Control program — its future battlefield network — is led by Anduril, with Palantir's Foundry providing the data layer, a baseline award announced June 2026. Worth knowing at full weight: in October 2025, Reuters revealed an internal Army memo calling the NGC2 prototype "very high risk" — no role-based access controls, no audit logging, hundreds of unvetted third-party vulnerabilities, and no way to verify whether adversaries already had persistent access. The Army says the issues are being remediated and declared the system "ready to scale" in August 2026, requesting $904 million to expand it. Both facts belong in the record: the speed *is* the sales pitch, and the memo is what the speed cost, at least at prototype stage.

**The NHS.** Outside the US, Palantir's biggest civilian bet: a seven-year, £330 million contract (November 2023) to build NHS England's Federated Data Platform. As of mid-2026, 139 hospital trusts are live. Also as of mid-2026: the British Medical Association has formally opposed the rollout and told doctors to limit engagement; the full program cost is reported to exceed £1 billion; and — the most damaging episode — NHS England admitted in summer 2026, after pressure from the National Data Guardian, that its own data-protection assessment had wrongly stated that only NHS staff could access identifiable patient data on the platform. A contract review is due in early 2027. The NHS fight is the cleanest natural experiment we have on the question this room ends with: whether the fusion capability can be accepted for care and refused for control.

## 7. The surveillance question at honest weight

Here is where most writing about Palantir becomes either a press release or a horror story. Let's do neither. Three concrete cases, then the actual shape of the problem.

**ImmigrationOS.** In April 2025, ICE awarded Palantir a $30 million contract modification to build the "Immigration Lifecycle Operating System." The contract documents — public — specify three functions: streamline identification and apprehension of people prioritized for removal; provide "near real-time visibility" into self-deportations; and make removal logistics more efficient. This extends a relationship in which Palantir has run ICE's core case-management system (ICM) since 2014, a deal that has grown past $145 million, spanning the Obama, Biden, and both Trump administrations.

**The "mega-database" fight.** In May 2025, the New York Times reported that Palantir's federal work — accelerated by a March 2025 executive order directing inter-agency data sharing, and by DOGE staffers with Palantir backgrounds — had expanded from IRS work toward a centralized, cross-agency platform of data on Americans. Senator Wyden and Representative Ocasio-Cortez sent a formal letter alleging the company was "enabling and profiting from serious violations of federal law." Palantir publicly denied it: it is "not building a master database," does not itself access or compile data on citizens, and cannot proactively share data across federal sources.

**The pattern.** Notice the structure of Palantir's denials, because they are largely *true and beside the point at the same time*. It is true that Palantir is a software vendor and the data belongs to the customer; true that its platforms have granular access controls, audit logs, and purpose restrictions that most legacy government systems lack (civil-liberties groups have occasionally conceded this); true that the same ICE contract ran quietly under administrations its current critics preferred. The company's UK chief makes the same argument about the NHS: misuse would be illegal and technically blocked.

What the denials do not touch is this: **the product is interoperability itself.** Legal scholars have long noted that practical obscurity — the friction of scattered records — functioned as a de facto civil liberty. Your tax file, your medical record, your address history, and your border crossings were separate not because anyone designed the separation, but because integrating them was hard. Palantir's entire value proposition, the thing the ontology *is*, is the removal of that friction. Once removed, the only remaining protections are law and policy — which can change in one election, one executive order, one contract modification. April 2025 demonstrated the mechanism precisely: the capabilities ICE bought for case management in 2014 became, via a $30 million modification, the substrate for a mass-removal operating system. Nothing new had to be built from scratch. That is what "platform" means.

So the honest weight is neither "Palantir is spying on you" (there is no public evidence Palantir itself surveils anyone; it arms customers who do) nor "it's just software" (nobody spends $10 billion on *just* anything). The honest weight is: Palantir is constructing, for the most powerful institutions on Earth, the standing capability for total institutional recall — and betting, doctrinally, that its side will keep using that capability rightly. The bet may even be reasonable. It is still a bet, placed on your behalf, without your signature.

## 8. Worked example: follow one row

You can verify the mechanics of everything above from public documents. Walk one datum through the pipeline.

1. **Start with a row.** A state DMV database holds a row: name, address, license plate, photo. On its own this row answers one question: is this person licensed to drive?
2. **Integration.** Under data-sharing agreements (the kind the March 2025 executive order directed agencies to expand), that dataset lands in a Foundry-class platform alongside others: visa records, IRS filings, license-plate-reader feeds, tip-line reports.
3. **Ontology mapping.** The row stops being a row. It maps to an object of type *Person*, with properties (address, status) and links: *registered owner of* → Vehicle; *resides at* → Address; *named in* → Tip #4471. Follow this in Palantir's public Foundry docs (palantir.com/docs/foundry/ontology/core-concepts) — the mapping grammar is exactly as described in Section 4.
4. **Query.** An analyst — or, via AIP, a language model — now asks a question no single source could answer: "people with expired visas, linked to vehicles seen near location X, with a workplace address on file." The ICE contract justification for ImmigrationOS describes precisely this class of function: streamlined "identification and apprehension" of prioritized categories, including visa overstays.
5. **Action.** An action type fires: create enforcement case, assign team, log outcome. The kinetic layer. A person is arrested at the workplace address.

Now run the counterfactual: same five steps, but step 1 is a hospital bed-status row and step 5 is "assign discharge coordinator" — that is the NHS platform saving a real patient a real week of waiting. The pipeline is *identical*. Every argument for the first case is an argument for the second; every argument against, likewise. If you take one tool away from this room, take that: you cannot evaluate this technology one deployment at a time, because the deployments share an engine.

## 9. What the reader can now see

You can now do three things you probably could not before this room. You can name what Palantir actually sells — engineered ontology plus the kinetic layer — and explain why that made it more valuable than the giant defense primes without manufacturing a single weapon. You can read both the fear and the fandom critically: the fear usually overstates what Palantir *does* (it is not a spy agency) and understates what it *enables* (the end of practical obscurity as a default); the fandom does the reverse. And you can watch the right indicators going forward: the NHS contract review in early 2027, the fate of the cross-agency data-sharing push in US courts, and whether NGC2's security remediation is ever verified by someone other than its builders.

The wider race this company runs inside is mapped in [china-usa-race](china-usa-race.html); what happens if fused institutional data meets much stronger models is part of [future-of-ai](future-of-ai.html).

One more thing, because the domain points there on its own. Palantir's documentation says an ontology is "a categorization of the world," and the phrase deserves a final minute. An institution running this software attends to exactly what its ontology contains — its object types are the *kinds of things it can notice*, its links the relationships it can conceive, its actions the moves it can imagine. That is uncomfortably close to a working definition of a mind, and it locates the real power precisely: not in the data, not in the model, but in the unglamorous authority to write the categories. Whoever defines the object types decides what the institution can attend to — and attention, it turns out, is the thing being sold everywhere in this series, from the [attention-economy](attention-economy.html) to the battlefield. Which raises the question this garden keeps arriving at from every direction: who, or what, writes the ontology *you* run on — and did you sign it? That question has its own rooms: [ontology](ontology.html), and [sense-of-self](sense-of-self.html).

## 10. Open questions

What is established fact: the contracts, revenues, and product mechanics cited above are documented in public filings, government contract records, and the company's own documentation; the NGC2 security memo and the NHS data-protection admission are reported by named outlets from primary documents.

What is hypothesis, held with reasons: that Palantir's commercial moat is durable — critics argue the ontology layer will be commoditized as language models get better at working with raw, messy data, and a ~$400 billion valuation on ~$8 billion of revenue prices in decades of flawless execution; nobody knows. Also hypothesis: that access controls and audit logs meaningfully constrain state misuse in practice, rather than merely making misuse well-documented. The NHS assessment error and the NGC2 memo are early evidence that the paper safeguards and the deployed reality can diverge.

What is wild, and labeled as such: that fused-data platforms plus capable AI amount to a new kind of state organ — an institutional nervous system whose behavior no individual inside the institution fully intends or can fully audit — and that the twenty-year fight over Palantir will eventually look like the negotiation over that organ's reflexes. Worth holding. Not established. Nothing in this room proves it.

## Sources

Load-bearing claims verified by live search, August 2026: Palantir Q2 2026 results ([Palantir Q2 2026 Business Update, investors.palantir.com](https://investors.palantir.com/files/Palantir%20-%20Q2%202026%20Business%20Update.pdf); [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/palantir-q2-2026-earnings-revenue-111006525.html)); market capitalization ([stockanalysis.com](https://stockanalysis.com/stocks/pltr/market-cap), [tradingeconomics.com](https://tradingeconomics.com/pltr:us:market-capitalization) — sources range $387–431B across August 2026, hence "roughly $400 billion"); Maven Smart System contract and ceiling raise ([DefenseScoop, May 2025](https://defensescoop.com/2025/05/23/dod-palantir-maven-smart-system-contract-increase); [GovCon Wire](https://www.govconwire.com/articles/palantir-receives-100m-army-contract-for-maven-smart-system-expansion)); Army $10B enterprise agreement ([Breaking Defense](https://breakingdefense.com/2025/08/army-consolidates-dozens-of-palantir-software-contracts-into-one-deal-worth-up-to-10-billion); [Washington Technology](https://www.washingtontechnology.com/contracts/2025/08/palantir-signs-10b-enterprise-agreement-army/407153)); NGC2 award and security memo ([Breaking Defense, June 2026](https://breakingdefense.com/2026/06/army-picks-anduril-to-lead-next-gen-c2-common-data-layer-baseline); [The Defense Post on the Reuters memo](https://thedefensepost.com/2025/10/09/us-army-security-platform-prototype); [Military Times, Aug 2026](https://www.militarytimes.com/news/your-military/2026/08/04/armys-new-battlefield-command-system-ready-to-scale)); ImmigrationOS ([WIRED](https://www.wired.com/story/ice-palantir-immigrationos); [ACLU](https://www.aclu.org/news/privacy-technology/palantir-deportation-roundup); [American Immigration Council](https://www.americanimmigrationcouncil.org/blog/ice-immigrationos-palantir-ai-track-immigrants)); the data-consolidation dispute ([NYT, May 30 2025](https://www.nytimes.com/2025/05/30/technology/trump-palantir-data-americans.html); [Nextgov on the Wyden/Ocasio-Cortez letter](https://www.nextgov.com/modernization/2025/06/democrats-press-palantir-about-reported-creation-irs-mega-database/406144); [Palantir's rebuttal](https://blog.palantir.com/correcting-the-record-palantirs-support-to-the-us-government-is-not-a-political-football-688d9a037a21)); NHS FDP status and controversy ([healthcare.digital](https://www.healthcare.digital/single-post/palantir-the-nhs-federated-data-platform-past-present-and-future); [Lowdown NHS](https://lowdownnhs.info/topics/accountablility/palantir-the-controversy-the-contracts-and-the-campaign); [Medact briefing](https://www.medact.org/2026/resources/briefings/briefing-palantir-fdp)); ontology mechanics ([Palantir Foundry documentation](https://palantir.com/docs/foundry/ontology/core-concepts)); *The Technological Republic* ([publisher site](https://techrepublicbook.com); [Stanford Lawyer](https://law.stanford.edu/stanford-lawyer/articles/in-print-the-technological-republic-hard-power-soft-belief-and-the-future-of-the-west)); founding and In-Q-Tel ([AFSC Investigate](https://investigate.afsc.org/company/palantir)). Karp's "used, on occasion, to kill people" was said on Axios on HBO (2020, widely reported); his Ukraine targeting claim and the January 2024 Israel MoD partnership are reported in multiple outlets including Time and The Guardian — the partnership is documented fact; his "most of the targeting" claim is his own characterization and is presented here only as such. Unverified beyond secondary reporting and labeled accordingly: the exact In-Q-Tel dollar figure (~$2M, consistent across sources but not confirmed from a primary document).

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
