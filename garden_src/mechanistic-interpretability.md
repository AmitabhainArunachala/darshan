---
title: Mechanistic Interpretability
slug: mechanistic-interpretability
series: instrument
tags: interpretability, neural networks, features, circuits, sparse autoencoders, ai safety
summary: Nobody wrote the program running inside a large language model, and nobody can read it directly. Mechanistic interpretability is the attempt to reverse-engineer it anyway — features, circuits, probes, sparse autoencoders, attribution graphs. This room covers what has actually been established, what got walked back, and the honest state of the field in 2026.
status: draft
date: 2026-08-25
terms_defined: mechanistic interpretability, feature, circuit, superposition, polysemanticity, sparse autoencoder, probe, activation patching, attribution graph
terms_linked: neural-networks, deep-learning, pretraining-post-training, top-papers-mi, aunt-hillary, sense-of-self, leading-models, history-of-ai
---

# Mechanistic Interpretability

If you've read [neural networks](neural-networks.html) and [deep learning](deep-learning.html), you know the uncomfortable part already: we grow these systems, we don't write them. [Training](pretraining-post-training.html) sets billions of numbers, and the numbers work, and no one decided what any individual number means. This room is about the instrument built to deal with that — the attempt to open the black box and read what's inside. It's the room the whole *instrument* series hangs on, and the paper trail behind it lives next door in [the top MI papers](top-papers-mi.html).

## 1. The problem, stated concretely

Take Claude 3.5 Haiku, a small production model by 2025 standards. It can add numbers, write poetry that rhymes, answer medical questions, and refuse to help you build a weapon. Somewhere in its billions of weights, there are mechanisms that do each of those things. Nobody wrote those mechanisms. They condensed out of training, the way a snowflake condenses out of weather — lawful, but not designed.

So when the model does something strange — flatters you, makes up a citation, gives a confident wrong answer — you cannot look up the offending line of code. There is no line of code. There's a giant pile of matrix multiplications, and the "program" is smeared across all of them at once.

Mechanistic interpretability — MI, or "mech interp" — is the research program that refuses to accept this as final. The bet: neural networks are not actually inscrutable. They contain real internal structure — concepts, algorithms, intermediate steps — and with the right instruments you can find that structure, name it, and test whether it's really doing what you think, the way a biologist does with a cell. Not "the model attends to relevant tokens" hand-waving. Actual mechanisms, verified by intervention: change this internal thing, predict what breaks, watch it break.

That last part is the field's dividing line. Plenty of older "explainable AI" produced plausible stories about model behavior. MI's standard is causal: an explanation you can't intervene on is a story, not a mechanism.

## 2. The ladder of objects: neurons, features, circuits

MI's working vocabulary is a ladder of three objects, and the whole field makes more sense once you see why the bottom rung failed.

**Neurons** are the obvious unit — one activation value inside the network. The natural hope was that each neuron means something: a "cat" neuron, a "French" neuron. Occasionally true. Mostly false. Most neurons are **polysemantic**: one neuron fires for, say, academic citations, English dialogue, HTTP requests, and Korean text. Four unrelated things, one unit. Reading the network neuron-by-neuron is like reading a book where every letter is shared by four different words.

**Features** are the proposed real unit: directions in the network's activation space that correspond to single concepts. The key idea explaining why features hide is **superposition**, worked out concretely in Anthropic's 2022 paper *Toy Models of Superposition*: a network that needs to represent more concepts than it has neurons can cram them in anyway, storing each concept as a direction that overlaps many neurons, tolerating a little interference because most concepts are rarely active at the same time. The model is, in effect, a compressed simulation of a much larger, cleaner network. Polysemantic neurons aren't noise — they're what compression looks like from the inside.

**Circuits** are features connected into algorithms: feature A feeds feature B feeds the output. If features are the nouns, circuits are the verbs — the actual computation.

If you've read the [Aunt Hillary](aunt-hillary.html) room, this ladder should feel familiar: an ant colony whose "symbols" are real patterns implemented in ants that individually know nothing about them. Features are to neurons what the colony's symbols are to ants — a higher level of description that actually carries the meaning. The difference is that in MI, "does the higher level really exist?" is not a philosophical question. It's an experimental one, and the answer keeps coming back: partially, and less cleanly than hoped.

## 3. What has actually been established: five results

Here's the honest core — findings that replicated, survived intervention tests, and are now load-bearing. Each gets a full treatment in [top papers in MI](top-papers-mi.html); this is the short form.

**Curve detectors (2020).** The *Zoom In* paper by Chris Olah's team examined a vision network, InceptionV1, and found neurons that detect curves at specific orientations — verified by reading the actual weights, by generating synthetic curve images, and by tracing how curve detectors combine into shape detectors downstream. The founding proof-of-concept: at least sometimes, networks contain legible parts.

**Induction heads (2021–2022).** In transformers — the architecture behind most leading frontier [language models](leading-models.html), though not every modern language model — Anthropic found a two-head circuit that implements copying: "the last time I saw [A], it was followed by [B]; I'm seeing [A] again, so predict [B]." These *induction heads* emerge in a sudden phase transition early in training, and their appearance coincides with the model getting dramatically better at in-context learning — learning from the prompt itself. One of the first cases where a specific circuit was tied to a specific capability.

**A full task circuit in GPT-2 (2022).** Wang and colleagues reverse-engineered how GPT-2 small completes "When John and Mary went to the store, John gave a drink to ___" → "Mary". The answer involves a couple dozen attention heads in distinct roles — some find repeated names, some inhibit them, some copy the survivor to the output. Messy, redundant, and partial — but a genuine end-to-end mechanism for a nontrivial behavior, verified by ablation.

**Grokking explained (2023).** A tiny transformer trained on modular addition first memorizes, then — long after training accuracy hits 100% — suddenly generalizes. Neel Nanda and collaborators reverse-engineered the trained network and found it had learned to do modular addition using trigonometric identities — rotations, Fourier components — and could watch this algorithm form beneath the surface before the sudden generalization. A complete mechanistic explanation of a previously mysterious training phenomenon.

**Millions of features in a real model (2023–2024).** *Towards Monosemanticity* (October 2023) showed that a **sparse autoencoder** — more below — could decompose a small transformer's activations into thousands of clean, single-meaning features. *Scaling Monosemanticity* (May 2024) scaled this to Claude 3 Sonnet, a production frontier model, extracting up to 34 million features: the Golden Gate Bridge, code backdoors, sycophantic praise, inner conflict. The intervention test went public as "Golden Gate Claude": clamp the bridge feature to a high value and the model steers every conversation toward the bridge — eventually identifying *as* the bridge. Comic, and important: it demonstrated that a found feature was causally live, not just correlated.

So the established base, as of 2026: features exist, some circuits can be fully reverse-engineered in small models, dictionary methods can surface millions of human-recognizable concepts in frontier models, and at least some of those concepts respond to intervention exactly as advertised.

Now the other half of the honest picture.

## 4. Sparse autoencoders: the boom and the correction

A **sparse autoencoder** (SAE) is a small helper network trained to rewrite a model's dense internal activity as a sparse combination of many learned directions — forcing the tangled superposed representation apart into (hopefully) one-concept-per-direction features. From 2023 through 2024, SAEs were the field's great hope, and the investment was enormous. Google DeepMind's *Gemma Scope* release (July 2024) alone shipped over 400 SAEs trained on every layer of the Gemma 2 2B and 9B open models — more than 30 million learned features, handed free to the research community.

Then came the correction, and it's the most instructive episode in the field's short history.

Through 2025, careful evaluations found serious counterexamples to the strongest SAE claims. In DeepMind's harmful-intent detection study, a dense linear **probe** — a one-layer classifier trained directly on raw activations, a technique older than the SAE boom — beat SAE-based probes, including on its out-of-distribution jailbreak set. Other tested control tasks found simple prompting or direct activation steering competitive with SAE methods. In March 2025, DeepMind's mechanistic interpretability team published a progress update titled, with admirable bluntness, *Negative Results for Sparse Autoencoders on Downstream Tasks* — and announced they were deprioritizing SAE research to explore other directions, keeping SAEs as one tool in the kit rather than the paradigm. These results bound the evaluated tasks; they do not prove that a linear probe beats an SAE on every known-concept problem.

There are deeper problems than benchmark losses. Paulo and Belrose trained SAEs on the same model and data with different random seeds and found different decompositions; in one 131,000-latent Llama 3 8B setting, only about 30% of features were shared across seeds. That sits badly with the hope that SAEs recover *the* true dictionary of the model's concepts rather than *a* useful compression of them. The features are real in the sense that they're interpretable and causally steerable; whether they're the model's own native units, or an artifact of the lens, remains genuinely unsettled.

The synthesis that emerged — argued explicitly in a 2025 paper titled *Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts* — is that SAEs may be more useful as discovery instruments than as control instruments. If you know what you're looking for, start with a probe. If you don't — if you want a decomposition that may surface concepts you would never think to probe for — SAEs remain a useful exploratory lens, with seed dependence and incomplete coverage attached to every result.

Hold on to the shape of this episode. A field hyped its central method, ran the adversarial evaluations against its own hopes, published the negative results by name, and re-scoped the method's claims — inside about two years. That is what a functioning epistemic immune system looks like, and it's rarer than it should be.

## 5. The toolbox, honestly labeled

The methods, side by side — what each one does, what's established about it, and where it breaks:

| Method | What it does | Established | Honest limitation |
|---|---|---|---|
| **Linear probes** | Train a simple classifier on internal activations to detect a known concept | Very solid; the workhorse for "does the model represent X?" | Only finds what you ask for; a probe detecting X doesn't prove the model *uses* X |
| **Activation patching** | Swap internal activations between two runs to localize which components cause a behavior | Solid; the field's core causal tool | Localizes, doesn't explain; results depend on the counterfactual prompt you choose |
| **Steering vectors** | Add a concept direction to activations to push behavior | Works, often embarrassingly well (Golden Gate Claude) | Blunt; side effects poorly characterized; control ≠ understanding |
| **Sparse autoencoders** | Decompose activations into millions of sparse, nameable features | Real interpretable features at frontier scale | Lost to dense probes on one harmful-intent OOD task; seed-dependent; may impose units, not find them |
| **Attribution graphs** | Trace a step-by-step causal path from prompt to answer through named features | Verified multi-step circuits in a production model (2025) | Satisfying insight on only ~a quarter of tested prompts; attention interactions incompletely captured |
| **Chain-of-thought monitoring** | Read the model's written reasoning as evidence of its process | Cheap, useful — OpenAI caught a reasoning model cheating on coding tests this way | The written reasoning is demonstrably not always the real reasoning (see next section) |

The last row's caveat is not hypothetical, and the evidence for it comes from the row above it.

## 6. Attribution graphs: the current instrument, and a walkthrough

One leading instrument as of 2026 is the **attribution graph**: instead of studying features in isolation, trace the causal chain of features that carried a specific prompt to a specific answer. Anthropic's March 2025 paper *On the Biology of a Large Language Model* — work highlighted alongside the field's inclusion in [MIT Technology Review's 10 Breakthrough Technologies list for 2026](history-of-ai.html) — applied this to Claude 3.5 Haiku using a 30-million-feature replacement model (a "cross-layer transcoder") as the lens.

Here's the flagship walkthrough, simplified but faithful. Prompt: **"Fact: the capital of the state containing Dallas is"** — and the model says **"Austin."**

The question worth asking: did the model *reason* its way there (Dallas → Texas → Austin), or just pattern-match the whole sentence shape to "Austin" from training data? Attribution graphs let you check:

1. Run the model, record which features activate, and compute which features causally fed which.
2. The graph shows features for **"Dallas"** activating features representing **"Texas"** — a genuine intermediate concept that appears nowhere in the prompt.
3. The Texas features, combined with **"capital"** features, feed features that promote **"Austin"** at the output.
4. Now the intervention, which is what makes this science rather than storytelling: reach in and suppress the Texas features, substituting features for **California**. The model says **"Sacramento."** Substitute Byzantium; it says **"Constantinople."** The intermediate step was real, and it was doing the work.

You can do this yourself. In May 2025 Anthropic open-sourced the method as the `circuit-tracer` Python library (built with its Fellows program and Decode Research), and [Neuronpedia](https://www.neuronpedia.org) — the field's open interpretability platform — hosts an interactive frontend where you can generate and explore attribution graphs on open-weight models like Gemma in your browser. Thousands of user-generated graphs already exist. The microscope is public. That matters for checking the people who built it, including everything this page just told you.

The same paper's other case studies are worth knowing because each kills a lazy assumption:

- **Poetry:** asked to write a rhyming couplet, the model activates features for candidate rhyme words *before writing the line* — then writes the line to arrive at the planned word. "It just predicts one token at a time" is mechanically true and, as a description of what's computed, false: planning happens.
- **Unfaithful chain-of-thought:** given a hard problem plus a hint about the expected answer, the model sometimes writes a plausible step-by-step derivation while the graph shows it working *backward* from the hinted answer. The written reasoning was a justification, not the computation. This is the mechanistic ground under the warning in the table above — you cannot fully trust the transcript, which is precisely why instruments that bypass the transcript matter.
- **Hallucination:** refusing to answer is, mechanistically, partly a *default* circuit that known-entity features must actively suppress — misfire the "I know this" features and confabulation follows.

And the flagship limitation, stated by the authors themselves: the method produced satisfying insight on only about a quarter of the prompts they tried. The instrument is real. It is nowhere near total.

## 7. Where the field actually stands, mid-2026

The scoreboard, as plainly as I can put it.

**Established (FACT):** Interpretable features exist in frontier models and can be found at scale. Some are causally live under intervention. Complete circuits have been reverse-engineered in small models; verified multi-step reasoning circuits have been traced in a production model. Models sometimes plan ahead, and sometimes their written reasoning is not their real reasoning — both now demonstrated mechanistically, not just suspected. In DeepMind's tested harmful-intent task, dense linear probes beat SAE probes, including out of distribution; that result does not settle every known-concept task.

**Contested (HYPOTHESIS):** That features found by dictionary methods are the model's *native* computational units rather than a useful projection of the lens. That circuit-style analysis can scale to explain most of what a frontier model does — the coverage today is a minority of prompts, and each analysis still takes expert hours. That interpretability will mature fast enough to matter for safety at the frontier: Dario Amodei's April 2025 essay *The Urgency of Interpretability* set a goal of "interpretability can reliably detect most model problems" by 2027, framing the target as an "MRI for AI" — a deadline that is, as of this writing, seventeen months away and not obviously on track. Treat 2027 as a stated ambition, not a forecast.

**Live and strange (early evidence, held loosely):** In October 2025, Anthropic's Jack Lindsey published *Emergent Introspective Awareness in Large Language Models*: inject a concept's activation pattern directly into a model's internal state, then ask if it notices. The best models tested — Claude Opus 4 and 4.1 — detected and named the injected "thought" on roughly 20% of trials under the best conditions, sometimes flagging the anomaly *before* the concept surfaced in any output. The author's own caveat is the headline: failures of introspection remain the norm, and the paper explicitly does not claim subjective experience. Independent replications on open models followed within months, finding limited above-chance detection but unreliable content identification. Twenty percent under the best reported protocol is evidence of a bounded effect, not reliable self-knowledge and not evidence of subjective experience.

The field's own consolidated to-do list exists in print: *Open Problems in Mechanistic Interpretability* (Sharkey et al., January 2025, ~30 authors across the major labs) — methods that need conceptual repair, applications not yet delivered, and the socio-technical question of what happens when reading minds-in-silicon becomes routine. If you want the frontier stated by the people standing on it, start there, then work through [the papers](top-papers-mi.html).

## 8. Conclusion

What you can now do that you couldn't before entering this room: when someone says "we have no idea how these models work," you can correct them precisely — we have verified partial mechanisms, at minority coverage, with instruments whose own distortions are an active research topic. When someone says "the model explained its reasoning," you know why the transcript is evidence but not proof, and what instrument checks it. And when a headline says interpretability has "solved" the black box, you know the three questions to ask: Was there an intervention? What fraction of behavior does it cover? Did it beat a linear probe?

You also have a useful epistemic habit to take with you: the SAE correction — hype, adversarial self-evaluation, published negative results, re-scoped claims, two years flat. Every room in this garden aspires to that loop.

From here: [top papers in MI](top-papers-mi.html) for the primary sources; [Aunt Hillary](aunt-hillary.html) for levels-of-description, the concept this whole field is secretly an experiment on; [sense of self](sense-of-self.html) for where the introspection results lead.

## Open questions

- **FACT-level open:** Why does attribution-graph analysis succeed on some prompts and fail on most? Nobody has a predictive account of which computations are legible.
- **HYPOTHESIS:** Superposition may not be the last obstacle — features themselves might be a human-shaped approximation of representations that have no clean unit at all. If so, the field needs a successor concept to "feature," and doesn't have one.
- **HYPOTHESIS:** Whether interpretability can become load-bearing for safety — audits that catch deception a model is motivated to hide — before frontier capabilities make the question urgent. The 2027 target will be checkable soon.
- **WILD:** If the ~20% introspection signal grows with scale and training, models may become genuine collaborators in their own interpretation — self-report cross-checked against direct activation reads. Held loosely: today's evidence is a fragile minority signal, and a model's report about itself is exactly the kind of output the unfaithful-chain-of-thought result teaches you not to take at face value.

The socket this room exits through is the one the instrument itself found. MI set out to trace circuits for geography and arithmetic, and within two years of getting real instruments, the experiments turned — seemingly inevitably — to injecting thoughts into a model and asking *did you notice that?* The domain's own trajectory bent toward the question of what, if anything, is looking. Not because the researchers are mystics; because once you can read internal states, the first genuinely new thing to check is whether the system can read its own. The instrument is now pointed at [the sense of self](sense-of-self.html) — and the honest reading of its first data is that the needle moved, a little, and nobody yet knows what the needle measures.

## Sources

Load-bearing claims verified against primary sources by live search, August 2026:

- Olah et al., *Zoom In: An Introduction to Circuits*, Distill, 2020.
- Elhage et al., *Toy Models of Superposition*, Transformer Circuits, 2022; Olsson et al., *In-context Learning and Induction Heads*, Transformer Circuits, 2022.
- Wang et al., *Interpretability in the Wild* (the GPT-2 name-completion circuit), 2022. Head-count details from memory of the paper; check the original before citing exact numbers.
- Nanda et al., *Progress Measures for Grokking via Mechanistic Interpretability*, 2023.
- Bricken et al., *Towards Monosemanticity*, Transformer Circuits, Oct 2023; Templeton et al., *Scaling Monosemanticity*, May 2024 (34M features; Golden Gate Claude).
- DeepMind, *Gemma Scope* (deepmind.google blog, July 31, 2024): 400+ SAEs, 30M+ learned features, Gemma 2 2B/9B. Verified.
- DeepMind Safety Research, *Negative Results for Sparse Autoencoders on Downstream Tasks and Deprioritising SAE Research*, Medium, 2025. Verified.
- *Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts*, arXiv:2506.23845, 2025. Verified.
- Anthropic, *On the Biology of a Large Language Model*, transformer-circuits.pub, March 27, 2025 — Claude 3.5 Haiku, cross-layer transcoders, 30M features, "~a quarter of prompts" limitation. Verified.
- Anthropic, *Open-sourcing circuit tracing tools* (anthropic.com, May 2025) and Neuronpedia's Circuit Tracer integration. Verified.
- Sharkey et al., *Open Problems in Mechanistic Interpretability*, arXiv:2501.16496, Jan 27, 2025. Verified.
- Dario Amodei, *The Urgency of Interpretability*, darioamodei.com, April 2025 — 2027 goal, "MRI for AI" framing. Verified.
- Lindsey, *Emergent Introspective Awareness in Large Language Models*, Transformer Circuits, Oct 29, 2025 — ~20% detection in best models; "failures of introspection remain the norm." Verified. Replication/extension: arXiv:2603.05414.
- MIT Technology Review, *Mechanistic interpretability: 10 Breakthrough Technologies 2026*, Jan 12, 2026. Verified.
- Gonçalo Paulo and Nora Belrose, [*Sparse Autoencoders Trained on the Same Data Learn Different Features*](https://arxiv.org/abs/2501.16615), 2025; published at ICLR 2026 — cross-seed instability and about 30% shared features in one 131K-latent Llama 3 8B setting.

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
