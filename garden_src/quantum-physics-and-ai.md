---
title: Quantum Physics and AI
slug: quantum-physics-and-ai
series: bridge
tags: quantum computing, quantum mechanics, machine learning, measurement problem, decoherence, quantum consciousness, dequantization
summary: Most of what circulates about quantum physics and minds is folklore, and this room kills it cleanly — the observer effect does not mean consciousness creates reality, and your brain is almost certainly not a quantum computer. What remains after the debunk is genuinely interesting: a real but narrow relationship between quantum computing and machine learning, and a measurement problem that is still honestly open after a hundred years.
status: draft
date: 2026-08-25
terms_defined: qubit, decoherence, measurement problem, quantum machine learning, dequantization, barren plateau, quantum error correction
terms_linked: neural-networks, machine-learning, deep-learning, linear-algebra-and-ai, mechanistic-interpretability, nvidia-and-the-chip, semiconductors, ontology, sense-of-self
---

# Quantum Physics and AI

You're in the bridge series, where the garden connects the traditions and the machines. This room has a specific job: quantum physics is the field most often invoked to connect physics to mind, and most of those invocations are wrong. So we're going to do the debunk properly — not with a sneer, but with the actual experiments — and then look hard at what survives. Two things do survive, and they're better than the folklore. If you've read [neural networks](neural-networks.html) or [machine learning](machine-learning.html), you know how today's AI actually works; nothing in those rooms needed quantum mechanics, and by the end of this one you'll know exactly why.

## 1. The folklore on the table

Three claims circulate wherever quantum physics meets talk about minds and AI. Let's state them fairly before testing them.

**Claim one: observation creates reality.** The double-slit experiment shows that particles behave differently when "observed," so consciousness must play a role in making the physical world definite.

**Claim two: the brain is quantum.** Consciousness can't be explained by ordinary computation, so it must exploit quantum effects — and if brains are quantum, silicon AI built on classical chips can never be conscious, or a quantum computer might be.

**Claim three: quantum computers will supercharge AI.** A quantum computer explores all answers in parallel, so quantum machine learning will make today's models look like pocket calculators.

Each claim contains a real fact wrapped in a false conclusion. The work of this room is separating them.

## 2. What the theory actually says

Quantum mechanics, stripped to what you need here, says this. A physical system is described by a wavefunction — a mathematical object that assigns a complex number to each way the system could be. In the standard operational formalism, a property in superposition is not assigned one definite pre-measurement value; interpretations disagree about what that says about reality. When you measure, you get one outcome, with probabilities given by the wavefunction (Max Born worked out that rule in 1926). And two systems that interact can become entangled: their joint state carries correlations that no assignment of separate, pre-existing local properties can reproduce. That last part isn't philosophy — John Bell showed in 1964 that it makes testable predictions, the tests have been run with increasing rigor since the 1970s, and the 2022 Nobel Prize in Physics went to Alain Aspect, John Clauser, and Anton Zeilinger for closing the loopholes. The predictions of quantum mechanics won every time.

So the strangeness is real. The theory is also the most precisely confirmed in the history of science. Both facts matter for what follows: the folklore isn't wrong because quantum mechanics is tame. It's wrong about what the strangeness consists of.

## 3. The observer, debunked cleanly

Here is the fact under claim one. In a double-slit experiment, if you place a device that records which slit each particle went through, the interference pattern disappears. That's true, replicated beyond any doubt.

Here is what the fact does not say: that a *conscious* observer did anything. The which-path device is a physical system — a photon detector, a stray air molecule, anything that interacts with the particle strongly enough to carry away information about its path. The interference vanishes whether or not any human ever reads the detector, whether or not the data is even stored. "Measurement" in quantum mechanics means a physical interaction that correlates one system with another. Your awareness is not an ingredient.

The modern name for this is **decoherence**: when a quantum system interacts with a large environment — air, light, a measuring device — the delicate phase relationships that produce interference get spread into the environment and become practically unrecoverable. Decoherence is not an interpretation; it's ordinary quantum mechanics applied to big systems, worked out from the 1970s onward by H. Dieter Zeh, Wojciech Zurek, and others, and confirmed in the lab. It explains, with no mention of minds, why cats and chairs never show interference patterns: they're monitored by their environments billions of times per second.

Two pieces of folklore need individual burial:

**The delayed-choice quantum eraser does not send influence backward in time.** In these experiments, the pattern that looks like "the future choice changed the past" only appears when you sort the data afterward using coincidence counts between entangled partners. The total pattern on the screen never changes. No signal, no retrocausation — just post-selection, a filter applied to data that already exists. This is the standard reading in the physics literature, and it's worth knowing because the eraser is the folklore's favorite exhibit.

**"Consciousness causes collapse" was a real proposal — and its own authors walked away from it.** John von Neumann noted in 1932 that the quantum formalism doesn't say where along the chain from particle to detector to eye to brain the definite outcome appears, and Eugene Wigner briefly took the endpoint seriously: maybe the observer's mind does it. This is a legitimate piece of intellectual history. But Wigner himself abandoned the position in later life, largely because of early decoherence-style arguments, and today it has almost no defenders among physicists. The folklore quotes the 1930s and skips the retraction.

What about the brain being quantum? The physicist Max Tegmark ran the numbers in 2000: at body temperature, in the wet, noisy environment of neural tissue, quantum superpositions in neurons or microtubules decohere in something like 10⁻¹³ to 10⁻²⁰ seconds. Neurons fire on timescales of milliseconds — ten orders of magnitude slower, and more. Whatever the brain is doing when you attend to a thought, the arithmetic says the quantum coherence is gone long, long before it could matter. That calculation has been contested at the margins, but no experiment has ever found functional quantum coherence in neural computation, and the burden of proof sits squarely on the claim.

## 4. The one serious version, and what the mountain said

The most serious quantum-consciousness proposal deserves better than a wave of the hand, because it did something the folklore never does: it made a testable prediction, and the test was run.

Roger Penrose — a Nobel-winning physicist, not a mystic — argued in *The Emperor's New Mind* (1989) and *Shadows of the Mind* (1994) that human mathematical insight can't be captured by any formal computation, and that the missing ingredient is an objective, gravity-driven collapse of the wavefunction. With the anesthesiologist Stuart Hameroff he located the proposed mechanism in neuronal microtubules: the Orch-OR theory. Nearly every logician who has examined the Gödel-based argument for non-computability considers it flawed, and Tegmark's decoherence numbers hit microtubules hardest of all. But the gravitational-collapse core, formalized independently by Lajos Diósi as the Diósi–Penrose model, predicts something concrete: collapsing wavefunctions should make charged particles jitter, and jittering charges emit faint radiation.

So a team including Sandro Donadi, Angelo Bassi, and Catalina Curceanu — with Diósi himself as a co-author — went looking for that radiation, using an ultra-pure germanium detector shielded under the Gran Sasso mountain in Italy. Published in 2020–2021: the radiation is not there at the predicted rate. The parameter-free version of the Diósi–Penrose model — the version with Penrose's natural choice of scale — is experimentally falsified. Versions with a free parameter survive, but only pushed to scales an order of magnitude past Penrose's original proposal, and follow-up experiments have tightened the bounds since.

Hold on to what just happened, because it's the method of this whole garden: a claim about consciousness and physics was stated precisely enough to fail, and it failed, and that is science working — which is more respect than the folklore ever earns. The measurement problem the theory was trying to solve, though, did not go away. We'll come back to it.

## 5. What a quantum computer actually is

Now to claim three, which requires knowing what a quantum computer actually does. Not the folklore version — the real one.

A **qubit** is a two-level quantum system that can be in superpositions of 0 and 1. Stack n qubits and their joint state lives in a space of 2ⁿ dimensions — the exponential fact that powers all the excitement. But here's the catch the folklore always omits: when you measure, you get one n-bit answer, sampled at random. A quantum computer does not "try all answers in parallel and pick the best." The entire art of quantum algorithms — and the reason there are so few great ones — is choreographing interference so that wrong answers cancel and right answers reinforce *before* you look. Peter Shor found such a choreography for factoring large numbers in 1994; Lov Grover found a more modest one for search in 1996. Thirty years later, the list of algorithms with proven exponential advantage is still short.

The hardware, meanwhile, has crossed a threshold worth marking precisely. Qubits are fragile — the same environmental coupling that decoheres brains decoheres processors, which is why they run at millikelvin temperatures. The escape route, proposed by Shor in 1995, is **quantum error correction**: encode one *logical* qubit redundantly across many physical qubits, so errors can be detected and undone. The scheme only helps if the physical error rate is below a critical threshold; above it, adding qubits adds noise faster than protection.

Here's a walkthrough you can check yourself. In December 2024, Google's Quantum AI team published results from Willow, a 105-qubit superconducting chip, in *Nature* ("Quantum error correction below the surface code threshold," Acharya et al., Nature 638, 920–926; the preprint is free at arXiv:2408.13687). They encoded one logical qubit in a growing grid of physical qubits — the surface code at distance 3, then 5, then 7, using 17, then 49, then 97 qubits. If the hardware were above threshold, each bigger grid would perform *worse*. Instead, each step up cut the logical error rate by a factor just above two. That is exponential suppression: the first below-threshold demonstration in the field's history, twenty-nine years after Shor said it should be possible. Follow the chain: physical error rates near 10⁻³, useful algorithms needing logical error rates around 10⁻¹⁰ or better, and a suppression factor of ~2 per step means roughly twenty-plus more doublings of protection bought by growing the grid — thousands of physical qubits per logical qubit. That's the whole game now, and it's why every serious roadmap talks about logical qubits, not raw counts. In an [April 2026 release](https://www.quera.com/press-releases/quera-launches-open-source-package-to-simulate-logical-quantum-circuits-at-scale), QuEra described 2025 papers demonstrating neutral-atom architectures with up to 96 logical qubits; that is a company account of the published work, not a January 2026 record claim. IBM has publicly targeted a fault-tolerant machine called Starling for 2029. Take all vendor timelines as marketing until the papers land — Microsoft's "topological qubit" announcement of February 2025 was contested by independent physicists within weeks, with the American Physical Society noting the accompanying paper didn't actually demonstrate the claimed Majorana states. In this field, the gap between press release and peer review is a load-bearing fact.

One more result belongs here because it's current and honest about its own limits. In October 2025 Google reported, again in *Nature*, the first *verifiable* quantum advantage: an algorithm they call Quantum Echoes, measuring a quantity from quantum chaos theory (an out-of-time-order correlator), ran in about two hours on Willow — a task they estimate at roughly 13,000 times longer on a classical supercomputer, after spending about ten person-years attacking their own result with nine classical simulation methods. Unlike the 2019 "supremacy" experiment, whose classical-runtime estimates were repeatedly slashed by better classical algorithms in the following years, this one produces a number other quantum computers can independently check. It is still a physics benchmark, not a commercial application. But it's real, it's recent, and it's the honest state of the art.

## 6. Quantum computing and machine learning: the honest scorecard

So: will quantum computers supercharge AI? Here is the claim-by-claim state of the field, current as of 2026.

| Claim | Status in 2026 | The load-bearing fact |
|---|---|---|
| Quantum computers try all answers at once | **False** | Measurement returns one sample; advantage requires engineered interference, which exists for few problems |
| Quantum linear algebra will speed up ML exponentially | **Mostly collapsed** | HHL-style algorithms carry fine print (state preparation, output access); Tang's dequantization (2018) removed the exponential gap for the flagship cases |
| Variational quantum ML will train useful models on near-term hardware | **Blocked** | Barren plateaus: gradients vanish exponentially with system size (McClean et al., 2018); still the core trainability problem |
| Quantum kernels beat classical kernels on ordinary data | **Unestablished** | No broadly accepted fair-comparison win on ordinary real-world classical data |
| Quantum advantage for learning about *quantum* systems | **Real** | Exponential advantage demonstrated for learning from quantum experiments (Huang et al., *Science*, 2022) |
| AI helps quantum computing | **Real and shipping** | AlphaQubit: transformer-based error decoder, state-of-the-art accuracy (DeepMind + Google Quantum AI, *Nature*, Nov 2024) |

Three rows deserve the full story.

**The dequantization story** is the best cautionary tale in the field, and it was written by an eighteen-year-old. In 2016, Kerenidis and Prakash published a quantum algorithm for recommendation systems — the Netflix problem — that ran exponentially faster than any known classical method. It became a flagship example of quantum machine learning. In 2018, Ewin Tang, then an undergraduate at UT Austin working on her senior thesis, set out to prove no classical algorithm could match it — and instead found one that could. The trick: the quantum algorithm assumed data was pre-loaded in a special quantum-accessible format, and Tang showed that a classical algorithm given an analogous sampling access could do essentially the same job. She and collaborators then dequantized quantum PCA and clustering the following year. The lesson generalizes: many claimed quantum ML speedups lived not in quantum mechanics but in unexamined assumptions about how data gets in and out. Scott Aaronson had flagged exactly this in a 2015 *Nature Physics* piece bluntly titled "Read the fine print." Read the fine print.

**Barren plateaus** are the second wall. The near-term hope for quantum ML was variational circuits — quantum analogs of [neural networks](neural-networks.html), with tunable parameters trained by gradient descent. In 2018, McClean and colleagues showed that for wide classes of these circuits, the training landscape flattens exponentially as qubits are added: gradients become so small that learning stalls. Eight years of proposed workarounds — clever initializations, local cost functions, restricted architectures — have produced a running theme: circuits structured enough to escape barren plateaus tend to become classically simulable. The trap may be a dilemma, not an engineering hurdle. That's a hypothesis, but it's the live one.

**And the data-loading wall stands behind both.** Deep learning eats terabytes of classical data through memory hierarchies that [GPUs](nvidia-and-the-chip.html) built on mature [semiconductors](semiconductors.html) handle at staggering bandwidth. Nobody has built the quantum RAM that speedup theorems assume, and loading n classical numbers into a quantum state generically costs time proportional to n — which already forfeits an exponential speedup before computation starts. Where quantum ML looks genuinely promising is where the data is *born quantum*: outputs of quantum sensors, states of molecules and materials, the behavior of other quantum processors. For learning about quantum systems themselves, real exponential advantages have been demonstrated. For classifying images, recommending films, or training language models — the [deep learning](deep-learning.html) that runs the current AI wave — no broadly accepted, fair-comparison computational advantage on ordinary classical data has been established, and there are structural reasons the bar is high.

Meanwhile the arrow that actually points somewhere runs the other way. AlphaQubit, published in *Nature* in November 2024 by DeepMind and Google Quantum AI, is a transformer — the same architecture underneath large language models — trained to decode quantum error-correction syndromes more accurately than prior algorithmic decoders. The near-term marriage of quantum and AI is not quantum computers running neural networks. It's neural networks helping quantum computers survive their own noise.

## 7. The measurement problem at its actual weight

Now the part of the folklore that, refined and disciplined, is real.

Decoherence explains why we never *see* superpositions. It does not explain why any particular outcome happens. Run the unitary quantum mechanics honestly and a measurement doesn't produce one result — it produces an entangled state in which detector, environment, and observer all join the superposition. The branches stop interfering; the mathematics still contains all of them. Yet every experiment ever performed has a single outcome. Where does the *one* come from? That is the **measurement problem**, and one hundred years after 1926, it is not solved. Max Schlosshauer — the physicist who literally wrote the standard review of decoherence — is explicit that decoherence alone does not resolve it.

The live responses each pay a different price, and none is free:

| Interpretation | The one outcome comes from... | The price | Experimentally distinguishable? |
|---|---|---|---|
| Copenhagen / textbook | Collapse on measurement, left as a primitive | "Measurement" never defined inside the theory | No |
| Many-worlds (Everett) | It doesn't — all outcomes occur, in branching | An unobservable multiverse; deriving probability is contested | No |
| Bohmian mechanics | Particles always had definite positions | Explicit nonlocality; awkward fit with relativity | No |
| Objective collapse (GRW, Diósi–Penrose) | A real physical process modifying quantum theory | New constants; and the tests keep coming back negative | **Yes** — being tested now |
| QBism / epistemic views | The outcome is an event in an agent's experience | Physics becomes first-personal; many find this a retreat | No |

Notice which row is different. Objective collapse models are the only ones that change the predictions, which is why the Gran Sasso experiment could kill one of them. Everything else is empirically identical physics with radically incompatible pictures of reality — which is precisely why the problem has lasted a century.

And physicists genuinely have not converged. At a 2011 quantum foundations conference, Schlosshauer, Kofler, and Zeilinger polled the specialists: 42% favored Copenhagen, 18% many-worlds, the rest scattered. A separate 2016 poll of 149 physicists across specializations — revisited in a 2025 retrospective — found Copenhagen at 39%, Everett at 6%, Bohm at 2%, and 36% with no preferred interpretation. A distinct 2025 *Nature* survey had 1,101 respondents and different results. Read the polls as snapshots with different samples, not one timeless vote on reality.

That is the measurement problem at its actual weight. It is not evidence that consciousness collapses wavefunctions — section 3 buried that. It is not a license for quantum healing or observer-created reality. It is something more uncomfortable: a precise, quantitative, unbroken theory that works everywhere and contains, at its center, an unresolved question about how the description relates to the fact that anything definite is experienced at all. The folklore grabs this question and answers it cheaply. The discipline is to hold it open at full weight.

## 8. What you can now see

You can now do the separation the folklore can't. When someone says "observation collapses the wavefunction," you know "observation" means physical interaction, that decoherence does the visible work, and that the eraser experiments involve post-selection, not retrocausation. When someone says the brain is quantum, you know the decoherence timescales are off by ten orders of magnitude, and that the one rigorous version of the claim predicted radiation that a mountain-shielded detector did not find. When someone says quantum computers will supercharge AI, you know to ask three questions that cut to bone: how does the data get in, does the advantage survive dequantization, and can the circuit be trained at scale? And when someone tells you the measurement problem is solved — by decoherence, by many-worlds, by anything — you know the poll numbers say otherwise.

You also know what's real: below-threshold error correction (2024), verifiable quantum advantage on a physics benchmark (2025), a genuine niche for quantum ML on quantum data, and transformers decoding quantum errors. The truth turned out smaller than the folklore and stranger than the dismissal.

From here, [machine learning](machine-learning.html) and [deep learning](deep-learning.html) show what the current AI wave actually runs on — no quantum required; [linear algebra and AI](linear-algebra-and-ai.html) covers the mathematics both fields share, which is why quantum ML looked so natural and why dequantization was possible; [mechanistic interpretability](mechanistic-interpretability.html) is the instrument this garden trusts for questions about what's happening inside models; and [ontology](ontology.html) picks up the interpretation question where this room leaves it.

## 9. Open questions

**Established (FACT):** Bell-inequality violations are real; local hidden-variable theories are dead (Nobel 2022). Decoherence explains the appearance of classicality without conscious observers. Below-threshold quantum error correction has been demonstrated (Willow, 2024). The parameter-free Diósi–Penrose collapse model is falsified (Gran Sasso, 2020–21). No broadly accepted, fair-comparison quantum-ML computational advantage on ordinary classical real-world data has been established; demonstrated advantages on quantum data and constructed tasks are different claims.

**Contested (HYPOTHESIS):** That barren plateaus reflect a fundamental dilemma — trainable implies classically simulable — rather than an engineering hurdle. That fault-tolerant machines arrive on the 2029-2033 vendor timelines. That quantum computing's first commercial value lands in chemistry and materials rather than optimization or ML. That some modified objective-collapse model survives the tightening experimental bounds.

**Speculation worth holding (WILD):** That the measurement problem's resolution, whenever it comes, will change what physics says about observers — in either direction: dissolving the observer entirely (Everett), or giving the first-person view a formal role no current theory grants it (QBism taken seriously). Nothing in current evidence forces either. A century of failed cheap answers suggests the real one will be expensive.

---

The measurement problem, stated without folklore, is this: physics gives a flawless description of the world from outside, and every use of that description happens from inside — at a vantage point, in an act of attention, where one outcome becomes *this* outcome. Quantum mechanics did not put the observer into physics the way the folklore claims. It did something quieter: it made it impossible to finish the theory without deciding what a measurement is, and a hundred years of the field's best minds have not closed that gap. Every interpretation in the table is, among other things, a position on where the point of view stands in nature. The question of what attention is — what it means that there is a *here* from which anything is registered — turns out not to be an import smuggled into physics by mystics. It is the one question physics itself has left open the longest. What that question is, taken on its own terms, is the subject of [sense of self](sense-of-self.html) — and of most of this garden.

## Sources

Verified by live search for this room (August 2026):

- Acharya et al., "Quantum error correction below the surface code threshold," *Nature* 638, 920–926 (2024/2025); arXiv:2408.13687. Willow announcement: Google blog, Dec 9, 2024.
- Google Quantum AI, "A verifiable quantum advantage" (Quantum Echoes / OTOC), *Nature*, Oct 22, 2025; research.google blog. The 13,000× figure is Google's estimate after internal classical red-teaming; treat as a claim with unusually strong due diligence, not an independent measurement.
- AlphaQubit: Google DeepMind & Google Quantum AI, *Nature* (2024), DOI 10.1038/s41586-024-08148-8; announced Nov 20, 2024.
- Ewin Tang, "A quantum-inspired classical algorithm for recommendation systems," arXiv:1807.04271 (2018); STOC 2019; dequantizing Kerenidis & Prakash, arXiv:1603.08675. Follow-ups: arXiv:1811.00414 and related.
- Donadi, Piscicchia, Curceanu, Diósi, Laubenstein, Bassi, "Underground test of gravity-related wave function collapse," *Nature Physics* (2020/2021); bound R₀ ≳ 0.54 × 10⁻¹⁰ m; follow-up *Eur. Phys. J. C* 81, 773 (2021); Quanta Magazine coverage, Oct 2022.
- Schlosshauer, Kofler, Zeilinger, "A snapshot of foundational attitudes toward quantum mechanics," arXiv:1301.1069 (2013). [Sivasundaram and Nielsen's 2016 poll, discussed in a 2025 retrospective](https://link.springer.com/article/10.1007/s10699-025-09993-0), supplied the 149-person figures; [Nature's separate 2025 survey](https://www.nature.com/articles/d41586-025-02342-y) had 1,101 respondents.
- Marin Ivezic, ["Quantum Machine Learning in 2026: A Real Frontier and an Honest Scorecard"](https://postquantum.com/quantum-ai/quantum-machine-learning-reality/) (29 May 2026) — field review supporting the narrower claim that no ordinary-classical-data result commands broad acceptance after fair baselines and full hardware costs.
- Gupta, Wood, Engstrom, Pole, and Shrapnel, ["A systematic review of quantum machine learning for digital health"](https://www.nature.com/articles/s41746-025-01597-z), *npj Digital Medicine* 8, 237 (2025) — scoped systematic evidence that the digital-health literature did not yet establish a conclusive QML advantage over classical methods.
- [QuEra's April 2026 release](https://www.quera.com/press-releases/quera-launches-open-source-package-to-simulate-logical-quantum-circuits-at-scale) describes 2025 papers with architectures up to 96 logical qubits. IBM Starling's 2029 target was announced June 2025. Microsoft's Majorana 1 announcement (February 2025) is qualified by [APS Physics coverage](https://physics.aps.org/articles/v18/57) noting that the accompanying paper did not establish Majorana zero modes. Vendor roadmap dates are targets, not facts.

Stable literature, cited from the record and not re-verified this session: Born rule (1926); Bell (1964); Shor (1994, 1995); Grover (1996); Harrow–Hassidim–Lloyd (2009); Aaronson, "Read the fine print," *Nature Physics* 11, 291–293 (2015) (confirmed via Tang's bibliography); McClean et al., "Barren plateaus in quantum neural network training landscapes," *Nature Communications* 9, 4812 (2018); Tegmark, "Importance of quantum decoherence in brain processes," *Physical Review E* 61, 4194 (2000); Huang et al., "Quantum advantage in learning from experiments," *Science* 376, 1182 (2022); Zurek's decoherence program; Penrose (1989, 1994); Penrose & Hameroff Orch-OR reviews; von Neumann (1932); Wigner's later retraction of consciousness-collapse; Schlosshauer, "Quantum decoherence," *Physics Reports* 831, 1–57 (2019).

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
