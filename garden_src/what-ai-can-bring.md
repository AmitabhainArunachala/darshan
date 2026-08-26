---
title: What AI Can Bring Humanity
slug: what-ai-can-bring
series: time-future
tags: medicine, science, education, access, evidence, forecasting, benefits
summary: The honest positive case for AI, built only from verified 2024–2026 evidence — a Nobel-recognized protein map, an AI-designed drug in patients, a 105,000-woman screening trial, weather models, tutoring RCTs, and open translation. Underneath it all, the gifts arrive under specific conditions, which this room names.
status: draft
date: 2026-08-25
terms_defined: the verified-gift test, conditions of arrival
terms_linked: neural-networks, deep-learning, benchmarks, leading-models, mechanistic-interpretability, forecasting, trends-gap, futurism, the-future, attention-economy, what-self-means
---

# What AI Can Bring Humanity

You're in the [time-future](the-future.html) wing of the garden. The rooms around this one — [forecasting](forecasting.html), [trends-gap](trends-gap.html), [futurism](futurism.html) — deal in what might happen. This room deliberately does not. It collects what AI has already brought, with dates, numbers, and papers you can check, and then asks the harder question hiding inside the good news: under what conditions do the gifts actually arrive?

## 1. The rule of this room

The positive case for AI is usually made badly. It's made with press releases, demo videos, and the word "soon." That style of argument deserves the distrust it gets.

So this room runs on one rule, call it the **verified-gift test**: a claimed benefit counts only if there is a primary source — a peer-reviewed paper, an officially graded result, or a public database you can open yourself — and the claim survives contact with its own caveats. Every claim below is dated. Where the evidence is thin, the sentence says so. Where a headline result got credibly attacked, the attack is in the room too.

One more ground rule on grammar. Nothing here is a prophecy. "AI will cure cancer" is not a sentence this room contains. What it contains is closer to: here is a drug a [deep learning](deep-learning.html) system helped design, here is what happened to the 71 patients who took it, and here is what we still don't know.

## 2. Medicine: the map, and the first drugs off the map

Start with the strongest single piece of evidence that exists.

For about fifty years, working out the 3D shape of a single protein — the thing that determines what it does in your body — was slow, expensive lab work. Over that half-century, the field accumulated roughly 200,000 experimentally solved structures in the Protein Data Bank. In 2022, DeepMind's AlphaFold2, a [neural network](neural-networks.html) trained on those solved structures, released predicted structures for over 200 million proteins — essentially every protein science had a sequence for. The predictions sit in a free public database, and by DeepMind's five-year accounting in 2025 it had been used by more than 3 million researchers in over 190 countries, more than a million of them in low- and middle-income countries. In 2024 the Nobel Prize in Chemistry went half to Demis Hassabis and John Jumper for the work — the first Nobel awarded for an AI system's scientific output. The Nobel committee's press release cited both the accuracy and the openness.

Hold on to that pairing — accuracy *and* openness. It recurs in every real gift in this room.

A structure database is upstream of cures, not a cure. So the next question is what the AI-designed-medicine pipeline has produced in actual patients. In 2025, rentosertib became the first AI-generated drug with results published from a randomized Phase 2a trial. Other AI-discovered or AI-designed candidates had already entered human trials, so this is a publication milestone, not the first human exposure.

The drug is rentosertib, from Insilico Medicine. Generative AI was used both to pick the target — a kinase called TNIK, which no one had clinically validated for lung fibrosis before — and to design the molecule. In 2025, *Nature Medicine* published the Phase 2a trial in idiopathic pulmonary fibrosis, a progressive and ultimately fatal lung disease. Seventy-one patients, randomized, double-blind, 12 weeks. Patients on the highest dose gained a mean 98.4 mL of forced vital capacity — lung function — while the placebo group declined by 20.3 mL. In IPF, where the standard course is decline, a mean *improvement* is striking.

Now the caveats, at full weight: 71 patients is small. Twelve weeks is short. The trial's primary endpoint was safety, not efficacy, and there were real safety signals — the most common reasons for discontinuation were liver toxicity and diarrhea, and 16 of 71 patients stopped early. Quality-of-life measures were inconclusive. None of this is disqualifying for a Phase 2a; all of it means "promising early trial," not "AI cured lung disease." The claim that survives is narrower and still remarkable: an AI-selected target and an AI-designed molecule went through a randomized human trial and produced a dose-dependent signal in the right direction, published in a top journal, in roughly half the time a traditional discovery program typically takes to reach that stage.

The antibiotic story runs parallel. In 2020, an MIT deep learning screen surfaced halicin, a molecule structurally unlike existing antibiotics, active against drug-resistant bacteria. In 2023, the same broad approach found abaucin, narrow-spectrum against *Acinetobacter baumannii* — one of the WHO's priority pathogens. In December 2023, *Nature* published the discovery of an entire new *structural class* of antibiotic candidates active against MRSA, found with an explainable deep learning model — meaning the researchers could see which chemical substructures the model was keying on, a small early win for [mechanistic interpretability](mechanistic-interpretability.html) thinking applied to chemistry. Caveat, again at full weight: none of these AI-discovered antibiotics has yet passed human trials. Bacteria don't care about *Nature* papers. But antibiotic discovery had been nearly dry for decades; candidate molecules with genuinely novel structures are exactly the bottleneck resource.

## 3. Medicine at population scale: the 105,000-woman trial

Drug discovery is glamorous. Screening is where AI may quietly matter first, and here the evidence is unusually good — a real randomized controlled trial, not a retrospective benchmark.

The MASAI trial, run inside Sweden's national breast-screening program, randomized over 105,000 women. In the intervention arm, an AI system (Transpara) supported the reading of mammograms; the control arm got the European standard, two radiologists reading every scan. Interim results in *Lancet Oncology* and *Lancet Digital Health* (2023, 2025): cancer detection up 29%, radiologists' screen-reading workload down 44%, no increase in false positives. The final results, published in *The Lancet* in January 2026, added the number that matters most: interval cancers — the dangerous ones that surface between screenings because a reader missed them — were 12% lower in the AI-supported arm, with 27% fewer of the aggressive subtypes among them.

Read carefully what the trial did *not* show. The AI did not replace anyone. Every scan was still read by at least one human radiologist; the AI flagged and triaged. The study's first author, Jessie Gommers, said it plainly: the results do not support replacing healthcare professionals — they support easing a workload crisis so that radiologist attention goes where it's needed. That design — AI proposes, human disposes, and the combination beats both the old standard and the machine alone — is the recurring shape of AI's verified medical wins so far.

## 4. Science itself: weather, materials, mathematics

**Weather.** In late 2024, *Nature* published GenCast, a DeepMind diffusion model that generates probabilistic 15-day forecasts. Evaluated against ENS — the world-leading physics-based ensemble run by the European Centre for Medium-Range Weather Forecasts — GenCast scored better on 97.2% of 1,320 verification targets, with particular gains on extreme events and tropical cyclone tracks. The practical point is not bragging rights over meteorologists. Traditional ensemble forecasting requires a supercomputer; a trained model generates its ensemble at a small fraction of the computational cost. Cyclone-track accuracy at low cost is, concretely, an early-warning technology for countries that could never afford their own numerical weather infrastructure. Caveat: these models are trained on reanalysis data produced *by* the physics-based pipeline; they currently ride on that infrastructure rather than replacing it, and how they behave as the climate shifts out of the training distribution is an open research question.

**Materials.** Here the room shows you what the honest positive case looks like when a headline partially deflates. In November 2023, *Nature* published GNoME, which predicted 2.2 million new crystal structures, about 381,000 of them computed to be stable — announced as "an order-of-magnitude expansion in stable materials known to humanity," with 736 of the structures independently made in labs. In April 2024, two senior materials scientists at UC Santa Barbara, Anthony Cheetham and Ram Seshadri, published a pointed analysis in *Chemistry of Materials*: sampling the released structures, they found scant evidence of compounds that were simultaneously credible, *novel*, and useful — many were minor variants of known compounds, and some involved elemental orderings unlikely to exist in a real lab. They did not call the work useless; they called the underlying approach sound and the headline oversized. That's the calibrated take this room adopts: GNoME produced a very large, genuinely useful set of computationally screened candidates — and "candidate list" is a different, more modest gift than "new materials." The gap between those two phrasings is where most AI hype lives.

**Mathematics.** In July 2025, an advanced version of Gemini with Deep Think solved five of six problems at the International Mathematical Olympiad — 35 of 42 points, a gold-medal score — and, for the first time, the solutions were officially graded and certified by IMO coordinators using the same criteria applied to students, who found the proofs "clear, precise and most of them easy to follow." (OpenAI reported the same score the same week, self-graded, without official certification — a difference worth noticing if you care about [benchmarks](benchmarks.html) and who verifies them.) A year earlier, DeepMind's systems had scored at silver level using formal proof languages; the 2025 result was in ordinary mathematical English. What this brings humanity is not solved Olympiad problems — those were already solved by teenagers. It's evidence that machine reasoning at elite-human level in a domain with objective verification is real, which matters for every scientific field whose bottleneck is proof and derivation rather than data.

## 5. Education: the two trials that define the whole question

Education is where the largest number of humans could be touched, and where the evidence splits most instructively. Two randomized controlled trials, published within about a year of each other, point in opposite directions — and the difference between them is the entire lesson.

**Nigeria, 2025.** A World Bank team ran an RCT in nine public secondary schools in Edo State: a six-week after-school program where students worked in pairs with GPT-4, guided by teachers and by prompts designed to promote reasoning rather than answer-copying. Learning gains were about 0.3 standard deviations overall — the authors estimate this is equivalent to one and a half to two years of typical learning progress in comparable settings, better than roughly 80% of rigorously evaluated education interventions globally. There was a dose-response relationship (more sessions, more gain), gains extended to end-of-year exams beyond the program's content, and subgroup estimates were larger for girls and, separately, for students with higher initial academic performance. The oldest result in education research is that one-on-one tutoring works and cannot be afforded at scale. This trial is the first strong evidence that an AI tutor, *embedded in structure*, can deliver a real fraction of that at marginal cost.

**Turkey, 2024–2025.** A University of Pennsylvania team ran an RCT with nearly 1,000 high-school students doing math practice. Students with unrestricted GPT-4 access ("GPT Base") solved 48% more practice problems correctly. Then access was removed for the test — and those students scored 17% *worse* than students who never had AI at all. They had used the model as a crutch, copying answers instead of learning. But a second arm ("GPT Tutor"), same model wrapped in prompts that made it teach rather than solve, improved practice performance 127% and showed no harm when access was removed.

Same underlying technology. One design produces two years of learning in six weeks; another produces students who know less than if the tool had never existed. The gift is real and the gift is conditional, and the condition is design — pedagogy, teacher presence, guardrails — not the model. This is the sharpest available answer to "is AI good for education?": wrong question. *Which deployment* is the question.

## 6. Access: the gifts that arrive by being given away

A third category is less about new capability than about who gets existing capability.

**Language.** In 2022 Meta released No Language Left Behind, a single open-sourced model translating directly between 200 languages, 150 of them low-resource languages — Luganda, Asturian, Balinese — that commercial translation had mostly ignored because their speakers aren't lucrative markets. Open weights meant researchers and local builders could use and adapt it without permission.

**Sight.** Be My Eyes, an app connecting blind and low-vision users with sighted volunteers, integrated GPT-4's vision capability in 2023 so that users can point a camera at anything — a medicine label, a train departure board, the contents of a fridge — and get an immediate description, no human volunteer required, free to the end user. The app reports over a million blind and low-vision users across 150+ countries, against an estimated 340 million people worldwide living with blindness or low vision. That last ratio is the honest note: the technology exists; most people who need it don't have it yet.

**Knowledge infrastructure.** The AlphaFold database is free. The GNoME candidate structures were released. NLLB was open-sourced. GenCast's code and weights were published. Notice the pattern: in every case in this room where a gift demonstrably arrived at scale, someone chose to distribute the artifact at marginal cost — which for software and model weights is approximately zero. Where outputs stay proprietary, benefits still exist but pool narrowly. The economics of "near-zero marginal cost" is the single strongest structural reason to believe AI's benefits *can* be broadly shared, and the openness decisions above are evidence it sometimes actually happens — while the [attention-economy](attention-economy.html) room next door documents what the same economics does when the product is your attention instead of your protein structure.

## 7. The conditions under which the gifts arrive

Lay the verified cases side by side and the pattern is hard to miss.

| Gift | Evidence (year) | Cheap objective verification? | Distributed at ~zero marginal cost? | Human institution absorbing it? | Status |
|---|---|---|---|---|---|
| AlphaFold structures | Nobel 2024; 200M+ structures; 3M+ users | Yes — against crystallography | Yes — free database | Yes — structural biology adopted it | Arrived |
| Rentosertib (IPF drug) | *Nat. Med.* Phase 2a, 2025 | Yes — randomized trial | No — proprietary drug | Yes — clinical-trial system | Early; Phase 3 pending |
| AI antibiotic candidates | *Nature* 2023–24 | Partly — in vitro/animal only | Papers open; molecules proprietary | Not yet — no human trials | Promising, unproven |
| MASAI screening | *Lancet* final, 2026; n>105,000 | Yes — RCT, cancer registry | No — commercial product | Yes — radiologists in the loop | Arrived (in trial setting) |
| GenCast weather | *Nature* 2024 | Yes — forecasts verify in days | Yes — open code/weights | Partly — agencies still integrating | Arriving |
| GNoME materials | *Nature* 2023 + 2024 critique | Weak — synthesis is slow | Yes — structures released | Contested — chemists pushed back | Deflated to "candidate list" |
| IMO gold | Officially graded, 2025 | Yes — IMO coordinators | No — frontier model | n/a | Capability proven |
| AI tutoring (Nigeria) | World Bank RCT, 2025 | Yes — tested vs control | Cheap, not free | Yes — teachers facilitating | Arrived (pilot scale) |
| Unguarded AI tutoring (Turkey) | PNAS RCT, 2025 | Yes — tested vs control | Yes | **No — design absent** | Net harm |
| NLLB translation | Released 2022, 200 languages | Partly — FLORES benchmark | Yes — open source | Mixed | Arrived |
| Be My Eyes | 1M+ users, 150+ countries | User adoption, not RCT | Yes — free to users | Yes — existing app community | Arrived |

Three conditions do almost all the work:

1. **Cheap, objective verification.** The gifts land fastest where reality grades the output quickly — a forecast verifies in ten days, a proof is checked by coordinators, a trial has a placebo arm. Where verification is slow or absent (materials synthesis, unguarded tutoring), claims inflate and later deflate. This is the same lesson the [benchmarks](benchmarks.html) room teaches from the other side.
2. **Near-zero-cost distribution, actually chosen.** The marginal cost of copying a model or a database is nearly nothing, but somebody still has to decide to give it away. Every at-scale arrival in the table involved that decision.
3. **A human institution that absorbs the tool.** Radiologists, teachers, structural biologists, forecast agencies. The Turkey trial is the clean negative control: identical model, no absorbing design, negative outcome. The gifts do not arrive *to* humanity; they arrive *through* human institutions or not at all.

None of this is a law of nature. It's an empirical pattern across roughly a dozen verified cases from 2022–2026, and you should hold it as exactly that.

## 8. Worked example: walk the chain yourself

The claim structure of this room — database → target → molecule → trial — is checkable from a laptop in about ten minutes. Here's the trace, using the rentosertib story:

1. **Open the map.** Go to `alphafold.ebi.ac.uk` (the AlphaFold Protein Structure Database). Search for **TNIK** and select the human entry. You're looking at the predicted 3D structure of the kinase that rentosertib inhibits.
2. **Check where the model admits ignorance.** The structure is colored by pLDDT — per-residue confidence. Blue regions are high-confidence; orange/yellow regions are low-confidence, often intrinsically disordered. This is worth seeing with your own eyes: the model publishes its own uncertainty, residue by residue. Ask how many human institutions do that.
3. **Read the trial.** Search PubMed for "generative AI-discovered TNIK inhibitor idiopathic pulmonary fibrosis randomized phase 2a" — the *Nature Medicine* 2025 paper is open-access via PubMed Central. Check the numbers this room quoted: n=71, +98.4 mL vs −20.3 mL, 16 discontinuations, liver-toxicity signal. If this room misquoted them, you'll know in five minutes.
4. **Check the screening claim the same way.** The MASAI final paper is Gommers et al., *The Lancet*, January 31, 2026 (DOI: 10.1016/S0140-6736(25)02464-X); the trial registration is NCT04838756 on clinicaltrials.gov, where the pre-registered endpoints are public — so you can verify the outcome wasn't moved after the fact.

That's the whole method of this room, handed over. You don't need to trust the author, which is the point.

## 9. Conclusion: what you can now see

You can now do three things you couldn't at the door. You can name the strongest verified benefits AI has delivered — a Nobel-recognized protein map used by millions of researchers, an AI-designed drug with a positive randomized-trial signal, a 105,000-person screening trial with fewer missed cancers and 44% less reading workload, weather models that beat the world standard, and a tutoring result worth two years of school in six weeks. You can attach to each one its honest caveat without the caveat destroying the case. And you can run the three-condition test — verification, distribution, absorption — on the next breathless claim you meet, and predict with decent accuracy whether it will arrive or deflate.

Where this goes next: [the-future](the-future.html) room takes up scenarios; [trends-gap](trends-gap.html) examines the space between capability curves and deployed reality — which this room's table is a snapshot of; [forecasting](forecasting.html) covers how to reason about any of it without prophecy. For the systems behind the gifts, start at [deep-learning](deep-learning.html) and [leading-models](leading-models.html).

## 10. Open questions

**Established (FACT):** Everything in the table above, at the stated scope: AlphaFold's database and adoption; rentosertib's status as the first published randomized Phase 2a trial of an AI-generated drug and the trial's reported numbers; MASAI's detection, workload, and interval-cancer results; GenCast's benchmark performance; the IMO 2025 officially graded gold score; both tutoring RCTs, including the separate larger subgroup estimates for girls and for students with higher initial performance; NLLB's release; the GNoME dataset and the published critique of its novelty claims.

**Contested or unknown (HYPOTHESIS):** That AI-discovered drugs will clear Phase 3 at higher rates, or meaningfully faster, than conventionally discovered ones — no AI-designed drug has yet completed Phase 3, so the discovery-speed gains shown so far may or may not survive the most expensive part of the pipeline. That MASAI's results generalize outside Sweden's double-reading system — US-style single-reader screening is a different baseline, and trials there are ongoing. That structured AI tutoring keeps its effect size beyond six-week pilots and dose-response novelty. That ML weather models remain reliable as climate drifts from their training distribution. That the three-condition pattern in Section 7 is causal rather than a description of a dozen early cases.

**Speculation worth holding (WILD):** That cheap elite-level reasoning plus cheap verification could compress decades of ordinary science into years in verification-rich fields — mathematics first, then computational chemistry and biology. Nothing in current evidence establishes this; the IMO result and AlphaFold are consistent with it, and equally consistent with progress that stays narrow, uneven, and institution-bound. Held as a scenario with named assumptions (verification stays cheap, distribution stays open, institutions absorb rather than resist), not as a forecast.

---

There is one more thing to say, and the material of this room says it on its own. Go back through the verified gifts and look at what each one actually redistributes. The radiologists got 44% of their screen-reading attention back, to spend on the cases that need a human. The Nigerian students got what education research has always said matters most and scales worst: something like individual attention, twice a week, for the cost of electricity. The Be My Eyes user gets a description the moment attention is pointed at the fridge shelf. Even the failures fit: the Turkey students were harmed precisely when the tool absorbed their attention's work instead of training it. Strip the domain labels away and every entry in the table is the same transaction — machine attention substituting where human attention was scarce, so that human attention can go where machines' cannot. What exactly is being redistributed, and what a system that pays attention *is*, is the question under every room in this garden; it's taken up directly in [attention-economy](attention-economy.html) and [what-self-means](what-self-means.html). This room only establishes the ledger: the gifts are real, they are conditional, and every one of them is, at bottom, attention.

## Sources

- Nobel Prize in Chemistry 2024, press release — nobelprize.org/prizes/chemistry/2024/press-release (200M structures; 2M+ users at award time).
- DeepMind, "AlphaFold: Five Years of Impact" (2025) — 3M+ researchers, 190+ countries, 1M+ LMIC users.
- AlphaFold Protein Structure Database — alphafold.ebi.ac.uk.
- Insilico Medicine / *Nature Medicine* (2025): ["A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized phase 2a trial"](https://pmc.ncbi.nlm.nih.gov/articles/PMC12353801/) — the first published randomized Phase 2a trial of an AI-generated drug; trial numbers and safety data as quoted.
- Hernström et al., *Lancet Digital Health* 7:e175–e183 (2025); Gommers et al., *The Lancet* 407:505–514 (Jan 31, 2026) — MASAI interim and final results; registration NCT04838756.
- Price et al., "Probabilistic weather forecasting with machine learning," *Nature* (2024), DOI 10.1038/s41586-024-08252-9 — GenCast vs ENS.
- Merchant et al., "Scaling deep learning for materials discovery," *Nature* (2023), DOI 10.1038/s41586-023-06735-9 — GNoME; Cheetham & Seshadri, *Chemistry of Materials* (2024) — the critique, as covered by The Register and 404 Media.
- Google DeepMind blog (July 2025): "Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the International Mathematical Olympiad" — 35/42, officially graded.
- Wong et al., "Discovery of a structural class of antibiotics with explainable deep learning," *Nature* 626:177–185 (2023/2024); Liu et al., abaucin, *Nature Chemical Biology* (2023); Stokes et al., halicin, *Cell* (2020).
- De Simone et al. (2025), World Bank Policy Research Working Paper, ["From Chalkboards to Chatbots: Evaluating the Impact of Generative AI on Learning Outcomes in Nigeria"](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099548105192529324) — overall and subgroup estimates for the Edo State RCT.
- Bastani et al., "Generative AI without guardrails can harm learning," *PNAS* 122 (2025) — Turkey RCT.
- Meta AI, No Language Left Behind (2022) — 200 languages, open-sourced.
- Be My Eyes press (2025): 1M users, 10M volunteers; OpenAI case study (2023).

Claims verified by live web search, August 2025–2026 sources, on 2026-08-25. The Nigeria RCT figures and subgroup statements are drawn from the authors' World Bank policy research working paper.

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
