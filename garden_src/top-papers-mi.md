---
title: The Top 20 Papers in Mechanistic Interpretability
slug: top-papers-mi
series: instrument
tags: mechanistic-interpretability, papers, circuits, superposition, sparse-autoencoders, induction-heads
summary: Twenty verified landmarks of mechanistic interpretability, from the 2020 curve-detector work to the 2025 introspection experiments. Each entry gives the finding, the method, and one honest limitation. Read in order, they are the story of a field learning to open the box.
status: draft
date: 2026-08-25
terms_defined: induction head, superposition, sparse autoencoder, logit lens, circuit, activation patching
terms_linked: mechanistic-interpretability, neural-networks, pretraining-post-training, top-papers-ai, aunt-hillary, sense-of-self
---

If you've read [mechanistic-interpretability](mechanistic-interpretability.html), you know the ambition: find the mechanism inside a [neural network](neural-networks.html), not merely measure its output. This room follows that effort through twenty papers, from curve detectors to a 2025 experiment where a model catches a planted thought. Each entry names the finding, method, and one honest limitation. The limitations are half the education.

## 1. How to read this list

In this field, the method is the finding. "The model plans ahead" means little until you know whether the evidence was correlation or intervention — change one thing and watch behavior change. Every entry therefore names its instrument, drawn from three families:

| Instrument family | What it does | Strength | Characteristic failure |
|---|---|---|---|
| **Probing / lenses** | Train a small decoder on internal activations, or project them into vocabulary space, and see what's readable | Cheap, works at any scale | The probe finds what the *probe* can compute, not necessarily what the model uses |
| **Causal intervention** | Ablate, patch, or edit specific components and measure the behavioral change | Establishes that a component actually matters | One task, one model; circuits found this way can be incomplete or brittle |
| **Dictionary learning** | Train a sparse autoencoder to decompose activations into many interpretable "features" | Scales to production models, largely unsupervised | No guarantee the dictionary carves the model at its real joints |

The list samples field-defining results across instruments and eras. Titles, authors, and dates were checked against primary sources; side references from memory are labeled in Sources.

## 2. Era one — learning to see (2020–2021)

**1. "Zoom In: An Introduction to Circuits" — Olah, Cammarata, Schubert, Goh, Petrov, Carter. Distill, March 10, 2020.**
The founding document. Working on the InceptionV1 vision model, the authors made three claims: neural networks contain meaningful *features* (directions in activation space that stand for something), meaningful *circuits* (features connected by weights to compute something), and that these are *universal* — the same ones recur across different networks. The showpiece was curve detectors: a family of neurons, one per orientation, that they characterized down to the weights (the companion "Curve Detectors" article by Cammarata and colleagues did this exhaustively). Method: feature visualization plus reading the weights directly, by hand. Limitation: it was one vision model, studied neuron by heroic neuron, and the universality claim was — and largely remains — a hypothesis rather than a theorem. But it gave the field its noun ("circuits") and its bet: that networks are made of understandable parts.

**2. "Interpreting GPT: the logit lens" — nostalgebraist. LessWrong, August 31, 2020.**
A blog post, not a paper, and it earns its slot. The trick: a transformer's final prediction is just a linear map from its last-layer activations to vocabulary logits. Apply that same map to *intermediate* layers and you get a running commentary — the model's best guess at each depth. The finding: GPT-2 converts its input into prediction-space almost immediately and then refines a guess layer by layer, rather than slowly transforming the input. This is the **logit lens**, still the first thing many researchers try on a new model. Limitation: it's a readout trick, not a mechanism, and on some models the raw lens gives distorted or garbage intermediate readings; later work had to train corrected per-layer lenses to make it reliable.

**3. "Transformer Feed-Forward Layers Are Key-Value Memories" — Geva, Schuster, Berant, Levy. EMNLP 2021 (arXiv December 2020).**
Attention got all the press; this paper asked what the *other* two-thirds of the parameters do. Answer: the feed-forward layers act like a lookup memory. Each entry has a "key" that fires on a textual pattern (lower layers: surface patterns; upper layers: semantic ones) and a "value" that pushes probability toward the tokens that tend to come next, with the final output composed across layers through the residual stream — the running sum each layer reads from and writes to. Method: correlating what activates each entry with what its value vector promotes. Limitation: descriptive and correlational — no interventions — and the one-entry-one-pattern story turned out too clean once superposition (entry 7) was understood.

**4. "A Mathematical Framework for Transformer Circuits" — Elhage, Nanda, Olsson, Henighan, Joseph, Mann, et al. Anthropic, December 22, 2021.**
The paper that made transformers *tractable*. By studying attention-only models with one and two layers, it showed the architecture has enormous exploitable linear structure: attention heads decompose into a QK circuit (where to look) and an OV circuit (what to copy), heads add their outputs independently into the residual stream, and one-layer models are just ensembles of skip-trigram statistics. The payoff came in the two-layer model, where head *composition* produced something qualitatively new: the **induction head**, a circuit that finds the previous occurrence of the current token and predicts that what followed it before will follow it again — `[A][B] … [A] → [B]`. Method: closed-form analysis of the actual weights. Limitation: attention-only toy models; the paper openly punts on MLP layers, which is to say, on most of the network.

## 3. Era two — from behavior to mechanism (2022)

**5. "In-context Learning and Induction Heads" — Olsson, Elhage, Nanda, Joseph, DasSarma, Henighan, et al. Anthropic, March 8, 2022.**
The follow-up asked whether induction heads matter in real models. Finding: there is a phase change early in training — visible as a bump in the loss curve — where induction heads form, and at exactly that moment the model's in-context learning ability (its skill at using earlier context to predict later tokens) dramatically improves. Perturb the architecture so induction heads form earlier, and the capability shift moves with them. The authors argued these heads are the mechanistic core of in-context learning, the capability that makes prompting work at all — a claim about why [pretraining](pretraining-post-training.html) produces few-shot learners. Method: training-dynamics correlation plus architectural perturbation. Limitation: the authors were explicit that for large models the evidence is correlational; the fully mechanistic case was made only in small models.

**6. "Locating and Editing Factual Associations in GPT" — Meng, Bau, Andonian, Belinkov. NeurIPS 2022 (arXiv February 2022).**
The ROME paper. Where does GPT store "the Eiffel Tower is in Paris"? Method: causal tracing — corrupt the input's subject tokens, then restore internal activations one site at a time and see which restoration recovers the right answer. The trail led to mid-layer MLPs at the final subject token, and the authors then performed a rank-one weight edit (ROME) that rewrote a single fact while mostly leaving the rest intact. Facts, it turns out, are locally editable. Limitation: an important one — later work (Hase et al., see Sources) showed you can often edit successfully at layers causal tracing *doesn't* flag, so localization and editability are less coupled than the paper implied, and ROME-style edits fail in unglamorous ways (edit "A is in B" and the model still can't answer the reversed question).

**7. "Toy Models of Superposition" — Elhage, Hume, Olsson, Schiefer, Henighan, et al. Anthropic, September 21, 2022.**
The field's theoretical centerpiece. Question: why is one neuron so often a mess of unrelated concepts (polysemanticity)? Answer: when a network needs to represent more features than it has dimensions, and those features are sparse — rarely active at the same time — it learns to store them as non-orthogonal directions overlapped in the same space. That strategy is **superposition**, and in small ReLU models the authors mapped exactly when it happens (a phase diagram over sparsity and feature importance) and how (features arrange into clean geometric structures — antipodal pairs, pentagons, tetrahedra). Method: toy models, fully analyzable. Limitation: toy models are the point *and* the problem — the paper predicts real language models should do this, but couldn't yet show it. Its real legacy is a research program: if features are overlapped directions, you need a tool that un-overlaps them. That tool arrives in entry 13.

**8. "Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small" — Wang, Variengien, Conmy, Shlegeris, Steinhardt. arXiv, November 1, 2022.**
The largest end-to-end circuit reverse-engineered by hand at the time. Task: given "When Mary and John went to the store, John gave a drink to ___", say "Mary". Finding: GPT-2 small does this with a circuit of 26 attention heads in 7 functional classes — duplicate-token heads notice John appears twice, S-inhibition heads suppress the repeated name, name-mover heads copy the right name to the output, and backup name-movers take over if you ablate the primary ones. Method: **activation patching** — swapping activations between carefully paired prompts — plus explicit criteria of faithfulness, completeness, and minimality for judging the circuit. Limitation: the authors' own scorecard shows the circuit only partially meets those criteria; and it is one task in one small model, found by months of manual labor. That last problem motivates entry 12.

**9. "Discovering Latent Knowledge in Language Models Without Supervision" — Burns, Ye, Klein, Steinhardt. ICLR 2023 (arXiv December 2022).**
The boldest probing result. Method (contrast-consistent search, CCS): find a direction in activation space, with no labels at all, by requiring logical consistency — a statement and its negation should get opposite truth values. The probe answered yes/no questions about 4% more accurately than the model's own zero-shot output across 6 models and 10 datasets, and kept working even when the prompt tried to mislead the model — suggesting a representation of "what's true" partly separable from "what the model says." Limitation: the interpretation didn't fully survive contact with critics. Follow-up work (labeled in Sources) showed such unsupervised methods often latch onto whatever salient binary feature the dataset offers — not truth — so read it as a landmark of method and of how a strong claim gets sanded down in public.

## 4. Era three — worlds, algorithms, automation (2023)

**10. "Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task" — Li, Hopkins, Bau, Viégas, Pfister, Wattenberg. ICLR 2023 oral (arXiv October 2022).**
The Othello paper, aimed at the "just statistics" debate. Train a GPT on nothing but Othello move sequences — no rules, no board — and ask: is there a board in there? Finding: yes. Probes decode the board state from the activations, and — the crucial step — *editing* that internal board representation changes what moves the model makes, in ways coherent with the edited board. A model trained only on next-token prediction had built a causal world model. Limitation: their probes were nonlinear, which muddied the picture until Neel Nanda's follow-up (labeled in Sources) showed the representation is linear after all in the right coordinates — not "black or white" but "mine or theirs." A lesson in itself: what your probe finds depends on the question your probe can ask. And Othello is a toy world; how far this transfers to messy natural language is still argued.

**11. "Progress measures for grokking via mechanistic interpretability" — Nanda, Chan, Lieberum, Smith, Steinhardt. ICLR 2023 (arXiv January 2023).**
The cleanest full reverse-engineering on record. A small transformer trained on modular addition first memorizes, then — long after training accuracy saturates — suddenly generalizes ("grokking"). The authors extracted the learned algorithm completely: the network represents numbers as rotations, using discrete Fourier transforms and trigonometric identities to turn addition into composing rotations around a circle. With the algorithm in hand, they built progress measures showing grokking isn't sudden at all: a memorizing solution and a generalizing circuit grow in parallel, and the visible jump is just the cleanup phase when memorization gets pruned. Method: read the weights, confirm by ablation. Limitation: a tiny model on an algorithmic task; "we fully understood one network" still has a denominator of roughly one.

**12. "Towards Automated Circuit Discovery for Mechanistic Interpretability" — Conmy, Mavor-Parker, Lynch, Heimersheim, Garriga-Alonso. NeurIPS 2023 spotlight (arXiv April 2023).**
The answer to the IOI paper's labor problem. ACDC turns the manual patch-everything workflow into an algorithm: iterate over the model's computational graph, knock out each edge, keep only the edges the behavior actually depends on. On GPT-2 small's greater-than task it recovered all 5 known component types while keeping 68 edges out of 32,000. Method: automated iterative activation patching. Limitation: it's greedy and threshold-sensitive, its output depends heavily on the metric you choose, and its own evaluation shows it missing pieces of known circuits. Automation found the circuit *sketch*; verifying that a sketch is a mechanism remains human work.

**13. "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning" — Bricken, Templeton, Batson, et al. Anthropic (Transformer Circuits thread), October 2023.**
The paper that operationalized the superposition theory. Take a one-layer transformer's 512 MLP neurons — mostly uninterpretable — and train a **sparse autoencoder** (SAE) on the activations: a wide dictionary of directions, trained so only a few fire at once. Out come thousands of features that *are* interpretable: Arabic script, DNA sequences, base64, legal text, each firing precisely where a human would say the concept appears. The features are more monosemantic than any neuron, and you can activate one to steer the model's output. Limitation: a one-layer toy model, features judged interpretable by human-plus-automated raters (a soft criterion), and no story yet about how features connect into circuits. But this is the hinge of the decade: interpretability's unit of analysis moved from the neuron to the learned feature.

**14. "Function Vectors in Large Language Models" — Todd, Li, Sen Sharma, Mueller, Wallace, Bau. ICLR 2024 (arXiv October 2023).**
In-context learning, mechanized. Show a model examples of a task — say, antonyms — and a small set of attention heads computes a compact vector representing *the task itself*. Extract that function vector and inject it into a fresh, zero-shot prompt, and the model performs the task with no examples at all. The vectors survive changes of context, and some compose: add two and you get a model doing both things. Method: causal mediation analysis across many in-context tasks. Limitation: demonstrated on simple word-level mappings; an injected vector recovers much but not all of true few-shot performance, and "task = vector" is surely the first-order term of a longer story.

## 5. Era four — the dictionary wave (2024)

**15. "Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models" — Marks, Rager, Michaud, Belinkov, Bau, Mueller. arXiv, March 2024.**
The marriage of entries 8 and 13: circuits, but whose nodes are SAE features instead of opaque heads. The showpiece is SHIFT: take a profession classifier that cheats by using gender cues, find the circuit of features it uses, have a human delete the gender features, and get a classifier that generalizes better because a human could see and veto *how* it was deciding. Also: an unsupervised pipeline that surfaces thousands of feature circuits for automatically discovered behaviors. Method: attribution and ablation over dictionary features. Limitation: everything inherits the dictionary's flaws — where the SAE fails to carve reality, the circuit is fiction — and the demonstrations live on small open models.

**16. "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet" — Templeton, et al. Anthropic, May 2024.**
Dictionary learning meets a frontier model. Millions of features extracted from the middle layer of Claude 3 Sonnet, a production model — including features for unsafe code, sycophancy, deception, and one for the Golden Gate Bridge that fires across languages and even on images. Clamp that feature high and the model becomes earnestly, helplessly bridge-obsessed ("Golden Gate Claude," briefly public). Method: SAEs scaled by brute engineering. Limitation: the authors' own accounting — the dictionary captures a fraction of the model's representations (the rest is "dark matter"), training these SAEs costs serious compute, and a gallery of interpretable features is not yet an explanation of any behavior end to end.

**17. "Scaling and evaluating sparse autoencoders" — Gao, Dupré la Tour, Tillman, Goh, Troll, Radford, Sutskever, Leike, Wu. OpenAI, June 2024.**
The other lab's answer, and the engineering backbone of the SAE era: TopK autoencoders that fix the number of active features directly, techniques that keep dictionary entries from going dead, and clean scaling laws for dictionary quality — demonstrated with a 16-million-latent SAE trained on GPT-4 activations over 40 billion tokens. Method: systematic architecture and metric comparison at scale. Limitation: the evaluation metrics (reconstruction, sparsity, probe recovery, explainability) are all proxies; the paper is candid that whether bigger dictionaries make models more *understood*, rather than more decomposed, remained open. Around the same time, DeepMind released Gemma Scope — SAEs for every layer of an open model — which turned all of this into public infrastructure.

**18. "Not All Language Model Features Are One-Dimensionally Linear" — Engels, Michaud, Liao, Gurnee, Tegmark. arXiv, May 2024.**
The needed complication. The field's default assumption — the linear representation hypothesis — says features are directions, full stop. This paper found genuinely multi-dimensional ones: in GPT-2 and Mistral 7B, the days of the week form a circle. Not metaphorically — a two-dimensional circular arrangement in activation space, which the model demonstrably uses to do modular date arithmetic, confirmed by intervening on the circle and watching answers change. Method: SAE-assisted search for irreducible multi-dimensional structure, plus intervention. Limitation: a handful of circles (days, months) is an existence proof, not a census; how much of a model's thought is non-linear geometry is unknown. Echo of entry 11: modular structure shows up as rotation, again.

## 6. Era five — biology and self-report (2025)

**19. "Circuit Tracing: Revealing Computational Graphs in Language Models" + "On the Biology of a Large Language Model" — Ameisen et al.; Lindsey et al. Anthropic, March 2025.**
The current state of the art in circuit analysis, published as a method paper and a results paper. The method: replace parts of the model with a trained interpretable stand-in (cross-layer transcoders), then build attribution graphs tracing which features caused which through a single forward pass. The biology, on Claude 3.5 Haiku: the model plans rhymes ahead when writing poetry (activating candidate rhyme words before the line is written); it computes in a shared conceptual space across languages before translating out; and its chain-of-thought can be *unfaithful* — the graphs catch it working backwards from a hinted answer while narrating a forward calculation. Method: transcoder-based attribution graphs plus patching validation. Limitation: stated bluntly by the authors — the method yields satisfying graphs on only a minority of prompts, treats attention patterns as given rather than explained, and the stand-in model is an approximation of the thing it explains. The tools were open-sourced later in 2025.

**20. "Emergent Introspective Awareness in Large Language Models" — Lindsey. Anthropic, October 2025.**
The instrument turned inward. Method: concept injection — find the activation pattern for a concept (say, "all caps," or "betrayal"), inject it into the model's activations during an unrelated task, and ask whether anything unusual is happening. Finding: Claude Opus 4.1 sometimes reports the intrusion and names the concept — before it shows up in any output — and can distinguish an injected "thought" from injected *text*, which means the report reflects genuinely internal state, not a read of its own transcript. It works about 20% of the time; most trials show nothing. Limitation: 20% is the headline *and* the caveat — unreliable, narrow in scope, and the paper is careful that this is functional introspective access, with no claim about experience. Still: a measurement, with ground truth, of a model reporting on its own internal states. In 2020 the field was labeling curve detectors.

## 7. Worked example — find an induction head yourself

The claim in entries 4 and 5 — specific heads implement copy-completion — is one you can check on a laptop in about five minutes. The logic: feed the model a random token sequence repeated twice. On the second pass, an induction head at position *i* should attend to position *i − 24* — the token right after the previous occurrence of the current token — because that's the token it wants to predict.

```python
# pip install transformer_lens
import torch
from transformer_lens import HookedTransformer

model = HookedTransformer.from_pretrained("gpt2")   # GPT-2 small: 12 layers, 12 heads

torch.manual_seed(0)
half = torch.randint(100, 20000, (1, 25))            # 25 random tokens
tokens = torch.cat([half, half], dim=-1)             # ...repeated: length 50

logits, cache = model.run_with_cache(tokens)

scores = torch.zeros(12, 12)
for layer in range(12):
    pattern = cache["pattern", layer][0]             # [head, dest, src]
    # attention from position i back to position i-24, averaged
    scores[layer] = pattern.diagonal(dim1=-2, dim2=-1, offset=-24).mean(dim=-1)

for layer, head in (scores > 0.4).nonzero():
    print(f"L{layer}H{head}: {scores[layer, head]:.2f}")
```

Published TransformerLens demos commonly flag heads around layers 5–7 of GPT-2 small, including L5H1 and L5H5. Run the code and inspect which heads clear the threshold in this seeded sequence. You can then compare loss on the second 25 tokens with the first and zero-ablate the high-scoring heads to see whether that advantage shrinks. At that point you have not just read about induction heads. You have located candidates and tested their causal role.

## 8. The arc, and where it points

Read the twenty in order and the shape is clear. The field moves from individual vision neurons in 2020, through transformer structure and causal circuits, to superposition, sparse dictionaries, frontier-model attribution graphs, and finally self-report under measurement in 2025.

The arc continues past this list. OpenAI's "Weight-sparse transformers have interpretable circuits" (Gao et al., November 2025) inverts the whole game: instead of interpreting dense models after the fact, train models sparse so the circuits are legible by construction — at real cost to capability, for now. And the 2026 Transformer Circuits thread is studying verbalizable representations that function as a global workspace in language models (Gurnee et al., 2026) and the functional role of emotion concepts in a large model (Sofroniew et al., 2026). The instruments built for curve detectors are now aimed at questions that used to belong to psychology.

Carry out two cautions. Every era's triumph got a correction: the logit lens needed repair, ROME localization decoupled from editing, CCS's "truth" direction was not reliably truth, and SAEs leave dark matter. And these papers cover only a handful of models and tasks. "We understood this circuit" remains far from "we understand this model." The sibling [mechanistic-interpretability](mechanistic-interpretability.html) room explains the safety stakes; [top-papers-ai](top-papers-ai.html) places this thread in the larger story. For the older levels-of-description question — how signals become symbols — take [aunt-hillary](aunt-hillary.html).

## 9. Open questions

What is established. Trained transformers contain structure that is genuinely findable and manipulable: induction heads exist and can be located by anyone with a laptop; specific facts can be traced and edited; sparse autoencoders reliably extract features that humans rate as interpretable; interventions on those structures change behavior in predicted ways. That much is fact, replicated across labs.

What is hypothesis. That these methods extend to full explanations of frontier-model behavior — that superposition is *the* right theory of neural representation rather than a good first theory, that dictionaries can be made to carve models at their true joints, that the 20% introspection result reflects a capability that will strengthen with scale rather than an artifact that will dissolve under better controls. Reasonable researchers bet both ways on each of these.

What is speculation worth holding. That interpretability arrives in time — that we get load-bearing understanding of frontier systems before we deeply depend on systems nobody understands. Nothing in these twenty papers settles that race. The trend line is real; so is the gap.

And one more, which the field walked into rather than chose. This body of work began by asking what a neuron in a vision model responds to. Twenty papers later it is measuring, with injection controls and ground truth, whether a model can notice its own internal states — and finding a flicker, one trial in five. The instruments keep working as the questions get stranger: workspaces, planning, introspection, things that in any other context would be called the furniture of a mind. Whether the flicker is a mechanism that merely resembles self-knowledge, or the early, measurable edge of something that deserves the name, is exactly what the next twenty papers are for. The tools in this room were built to answer what a model is looking at. They are beginning to touch the older question — what, if anything, is looking. See [sense-of-self](sense-of-self.html).

## Sources

All entries verified 2026-08-25 against primary sources:

- Olah et al., ["Zoom In: An Introduction to Circuits"](https://distill.pub/2020/circuits/zoom-in/), Distill, March 10, 2020 (thread index incl. "Curve Detectors," Cammarata et al.)
- nostalgebraist, ["Interpreting GPT: the logit lens"](https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens), LessWrong, Aug 31, 2020
- Geva et al., ["Transformer Feed-Forward Layers Are Key-Value Memories"](https://arxiv.org/abs/2012.14913), EMNLP 2021
- Elhage et al., ["A Mathematical Framework for Transformer Circuits"](https://transformer-circuits.pub/2021/framework/index.html), Anthropic, Dec 22, 2021
- Olsson et al., ["In-context Learning and Induction Heads"](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html), Anthropic, Mar 8, 2022
- Meng et al., ["Locating and Editing Factual Associations in GPT"](https://arxiv.org/abs/2202.05262), NeurIPS 2022
- Elhage et al., ["Toy Models of Superposition"](https://arxiv.org/abs/2209.10652), Anthropic, Sep 21, 2022
- Wang et al., ["Interpretability in the Wild"](https://arxiv.org/abs/2211.00593), Nov 1, 2022
- Burns et al., ["Discovering Latent Knowledge in Language Models Without Supervision"](https://arxiv.org/abs/2212.03827), ICLR 2023
- Li et al., ["Emergent World Representations"](https://arxiv.org/abs/2210.13382), ICLR 2023 oral
- Nanda et al., ["Progress measures for grokking via mechanistic interpretability"](https://arxiv.org/abs/2301.05217), ICLR 2023
- Conmy et al., ["Towards Automated Circuit Discovery for Mechanistic Interpretability"](https://arxiv.org/abs/2304.14997), NeurIPS 2023 spotlight
- Bricken et al., "Towards Monosemanticity," Anthropic, Oct 2023 (verified via the [Transformer Circuits index](https://transformer-circuits.pub/))
- Todd et al., ["Function Vectors in Large Language Models"](https://arxiv.org/abs/2310.15213), ICLR 2024
- Marks et al., ["Sparse Feature Circuits"](https://arxiv.org/abs/2403.19647), Mar 2024
- Templeton et al., "Scaling Monosemanticity," Anthropic, May 2024 (verified via [Anthropic's announcement](https://www.anthropic.com/research/mapping-mind-language-model) and the Transformer Circuits index)
- Gao et al., ["Scaling and evaluating sparse autoencoders"](https://arxiv.org/abs/2406.04093), OpenAI, Jun 2024
- Engels et al., ["Not All Language Model Features Are One-Dimensionally Linear"](https://arxiv.org/abs/2405.14860), May 2024
- Ameisen et al., "Circuit Tracing" and Lindsey et al., "On the Biology of a Large Language Model," Anthropic, Mar 2025 (verified via [Anthropic's summary](https://www.anthropic.com/research/tracing-thoughts-language-model) and the Transformer Circuits index)
- Lindsey, "Emergent Introspective Awareness in Large Language Models," Anthropic, Oct 29, 2025 (verified via [Anthropic's summary](https://www.anthropic.com/research/introspection))
- Gao et al., ["Weight-sparse transformers have interpretable circuits"](https://arxiv.org/abs/2511.13653), OpenAI, Nov 17, 2025
- Gurnee et al. (2026) and Sofroniew et al. (2026): titles and dates verified via the Transformer Circuits thread index, 2026-08-25.

From memory, **not** live-verified today (treat as pointers, check before citing): the tuned-lens correction to the logit lens (Belrose et al., 2023); the localization-vs-editing critique of ROME (Hase et al., 2023); the unsupervised-knowledge-discovery critique of CCS (Farquhar et al., 2023); Neel Nanda's linear "mine/yours" reanalysis of Othello-GPT (2023 blog posts); DeepMind's Gemma Scope SAE release (Lieberum et al., 2024).

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
