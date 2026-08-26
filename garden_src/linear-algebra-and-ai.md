---
title: Linear Algebra and AI
slug: linear-algebra-and-ai
series: foundations
tags: linear algebra, vectors, matrices, attention, transformers, foundations
summary: Vectors, matrices, spaces, and projections, taught concretely enough to compute by hand. Why every modern AI model is matrix multiplication plus a little nonlinearity, and a full walkthrough of one attention head as nothing but linear algebra you can verify yourself.
status: draft
date: 2026-08-25
terms_defined: vector, matrix, dot product, matrix multiplication, linear map, projection, rank, attention head
terms_linked: intro-to-computer-science, neural-networks, deep-learning, machine-learning, optimization, mechanistic-interpretability, nvidia-and-the-chip, pretraining-post-training, attention-economy
---

# Linear Algebra and AI

If you've walked through [intro to computer science](intro-to-computer-science.html), you know a computer only ever does arithmetic on numbers. This room shows you the specific arithmetic that modern AI runs on. It is one operation — multiplying grids of numbers — repeated trillions of times, with one small twist added between the multiplications. When you finish this room, [neural networks](neural-networks.html) and [deep learning](deep-learning.html) stop being magic words and become shapes you can draw.

## 1. A vector is a list of numbers that acts like a direction

Start with the smallest object. A **vector** is a list of numbers. That's the whole definition. `[3, 4]` is a vector. So is a list of 768 numbers.

The reason vectors matter is what the list *means*. Treat `[3, 4]` as instructions — go 3 steps east, 4 steps north — and the list becomes an arrow: a direction and a length. Two short lists of numbers can point the same way or opposite ways, be near each other or far apart. Geometry falls out of arithmetic.

Here is why this matters for AI. In 2013, Tomas Mikolov and colleagues at Google trained a system called word2vec that assigned every English word a vector of a few hundred numbers, learned purely from which words appear near which other words. Then they noticed something strange. Take the vector for *king*, subtract the vector for *man*, add the vector for *woman*, and look for the nearest word vector to the result. You get *queen*. Nobody programmed that. Directions in the space had come to mean things: there was a rough "royalty" direction, a rough "gender" direction, and arithmetic on word vectors did a crude kind of reasoning. (An honest caveat, documented since: the standard test excludes the input words from the answer, and the trick fails on plenty of analogies. The result is real but weaker than the legend.)

That discovery is the seed of everything below. Modern language models push it much further: inside GPT-2, every token of text becomes a vector of 768 numbers, and inside frontier models the lists are tens of thousands long. Meaning lives in *where the vector points*.

One more tool and you can measure meaning. The **dot product** of two vectors multiplies them position by position and adds up the results:

```
[1, 2, 3] · [4, 0, 2]  =  1·4 + 2·0 + 3·2  =  10
```

Geometrically, the dot product is large and positive when two vectors point the same way, near zero when they're perpendicular, and negative when they oppose. It is a similarity meter. Hold onto it — the dot product between a "query" and a "key" is the exact operation an attention head uses to decide which words to look at. You'll compute one by hand in section 5.

## 2. A matrix is a machine that moves every vector at once

A **matrix** is a grid of numbers — rows and columns. `[[2, 0], [0, 1]]` is a 2×2 matrix. But just as a vector is secretly an arrow, a matrix is secretly a *machine*: multiply a vector by a matrix and you get a new vector out. The rule, called **matrix multiplication**, is just dot products — each row of the matrix dotted with the input vector gives one number of the output:

```
[2 0]   [3]     [2·3 + 0·4]     [6]
[0 1] · [4]  =  [0·3 + 1·4]  =  [4]
```

That machine doubled the east-west part of the arrow and left the north-south part alone: a stretch. Other matrices rotate arrows, flip them, flatten them, mix their coordinates. What a matrix can never do is bend: it always maps straight lines to straight lines and leaves the origin fixed. That's why this whole subject is called *linear* algebra, and why a matrix is called a **linear map**.

The deep fact is uniformity. A matrix doesn't move one vector — it moves the entire space at once, every possible vector, by the same consistent rule. When an AI model multiplies by a learned matrix, it is applying one transformation to *whatever* comes in. The matrix is where the learning lives: training a model means adjusting the numbers in its matrices — its *weights* — until the machine transforms inputs the way you want. How those adjustments are computed is the subject of [optimization](optimization.html); how the whole training pipeline is organized is [pretraining and post-training](pretraining-post-training.html).

And matrices compose. Applying matrix `A`, then matrix `B`, is exactly the same as applying the single matrix `BA` (their product). Remember this; it has a sting in section 4.

## 3. Spaces, projections, and rank — where the meaning sits

A vector with 2 numbers lives in a 2-dimensional space: a flat plane. A vector with 768 numbers lives in a 768-dimensional space. You cannot picture that, and you don't need to — every operation you just learned works identically. Distances, angles, dot products: same formulas, more positions in the list.

Inside a 768-dimensional space there are smaller flat regions: lines (1-dimensional), planes (2-dimensional), and so on up. These are *subspaces*. A **projection** takes a vector and finds its shadow on a subspace — the closest point in that smaller region. Projecting `[3, 4, 5]` onto the first two coordinates gives `[3, 4, 0]`: keep what lies in the subspace, discard the rest. Projection is how you ask a high-dimensional vector one specific question — "how much of you points in *this* direction?" — and ignore everything else. Mechanically, it's a dot product again.

The **rank** of a matrix is how many dimensions survive passing through it. A 768×768 matrix could in principle use all 768 dimensions — full rank. But a matrix might squash its whole input space down to a 64-dimensional shadow: rank 64, a **low-rank** map. Low rank sounds like a defect. In AI it's a design choice: a low-rank matrix is a *bottleneck*, forcing the machine to summarize. You are about to meet a famous one — every attention head in a transformer reads its 768-dimensional input through a rank-64 keyhole.

One finding from the young field of [mechanistic interpretability](mechanistic-interpretability.html) makes this concrete. Researchers at Anthropic showed in a 2022 paper, *Toy Models of Superposition*, that trained networks tend to represent individual features of the world — "this token is French," "this is Python code," "this sentence is about DNA" — as *directions* in these spaces, and that a space can pack in more feature-directions than it has dimensions by letting them overlap slightly, a phenomenon they named superposition. Whether *everything* a model knows is stored this way is still contested (more in the open questions below). But the working picture that guides interpretability research today is: **meanings are directions; thinking is moving vectors around with matrices; and reading a model's mind is finding which directions mean what.**

## 4. Why all of modern AI is linear algebra plus nonlinearity

Now the claim in this room's title. Take any modern neural network — GPT-2, or the model writing this page — and ask what it computes, layer by layer. The answer is astonishingly repetitive:

1. Multiply the incoming vectors by a learned matrix.
2. Apply one small, simple, *nonlinear* twist to each number.
3. Repeat, hundreds of times.

Step 1 is everything you learned above. Step 2 is tiny by comparison — a typical choice, ReLU, is just "if the number is negative, make it zero." A one-line rule. So why is it there at all?

Because of the sting from section 2: matrices compose. If a network were *only* matrix multiplications — layer one applies `A`, layer two applies `B`, layer three applies `C` — the whole stack would equal the single matrix `CBA`. A thousand linear layers collapse into one linear layer. All that depth would buy you nothing: the network could only stretch, rotate, and mix, never bend. It could never compute "dog OR cat but NOT both," never draw a curved boundary, never do anything a single matrix can't do.

The nonlinearity is the bend. Insert even the trivial ReLU rule between the matrices and the collapse is blocked: each layer's twist prevents it from merging into its neighbors, and the stack can now approximate essentially any transformation at all if made wide or deep enough. That is the actual division of labor inside every modern model:

**The matrices carry the knowledge. The nonlinearities make depth count.**

The economics of AI confirm where the work is. A standard estimate from the scaling-laws literature (Kaplan et al., 2020) is that running a transformer forward costs about **2 FLOPs per parameter per token** — two arithmetic operations for every weight, nearly all of them inside matrix multiplications — and training costs about `6 × parameters × training tokens`. For a model with hundreds of billions of parameters trained on trillions of tokens, that's a number with 25 digits, and it is overwhelmingly matrix math. This is also why [NVIDIA rules the chip market](nvidia-and-the-chip.html): a modern datacenter GPU like the H100 is essentially a furnace for matrix multiplication, its "tensor cores" delivering on the order of a quadrillion low-precision matrix operations per second (the exact figure depends on number format and sparsity settings — see the datasheet, not the marketing line). The hardware, the training cost, the model's knowledge: all of it is shaped like a matrix.

Here is the whole stack in one table, with the real shapes from GPT-2 small — the 124-million-parameter model OpenAI released in 2019, small enough that you can download it and check:

| What the model does | Linear-algebra object | Shape in GPT-2 small | Linear or not? |
|---|---|---|---|
| Turn a token into meaning | embedding: a lookup into a matrix of vectors | 50,257 × 768 | linear-ish (a lookup) |
| Decide where to look (attention scores) | dot products of query and key vectors | queries/keys are 64-long | **bilinear** (linear in each input) |
| Turn scores into a budget | softmax | 1 line of exp-and-divide | **nonlinear** |
| Move information between words | weighted sum of value vectors, then a matrix | 64 → 768 | linear |
| "Think" about the gathered info (MLP) | matrix, twist, matrix | 768 → 3,072 → 768 | linear · **nonlinear** · linear |
| Produce next-word scores | one final matrix | 768 → 50,257 | linear |

Read down the right-hand column. The nonlinear entries are one softmax and one activation twist — a few percent of the arithmetic. Everything else is the machinery of sections 1–3. That is the honest meaning of "AI is linear algebra plus nonlinearity": not a slogan, an accounting.

For the broader question of *why* learned matrices can do what hand-written rules couldn't, see [machine learning](machine-learning.html). Here, we go one level deeper and open the most important box in the table.

## 5. Worked example: one attention head, by hand

Attention is the mechanism that made modern AI possible — the 2017 paper that introduced the transformer is literally titled *Attention Is All You Need* (Vaswani et al.). Every explanation you've seen probably used the words "the model learns what to focus on." True, and useless. Let's compute one.

**The setup, with real shapes.** In GPT-2 small, each of the 12 layers has 12 attention heads. A single head owns four matrices:

- `W_Q` (768 × 64): projects each token's vector into a 64-dimensional **query** — "what am I looking for?"
- `W_K` (768 × 64): projects each token's vector into a 64-dimensional **key** — "what do I offer?"
- `W_V` (768 × 64): projects each token's vector into a 64-dimensional **value** — "what will I hand over if chosen?"
- `W_O` (64 × 768): projects the head's 64-dimensional result back up to 768, so it can be added into the token's running vector.

Notice: three of these are the low-rank keyholes from section 3. The head reads the rich 768-dimensional representation through 64-dimensional slots. Those numbers descend directly from the original 2017 transformer, which used vectors of 512 split across 8 heads of 64 each.

**The procedure.** For every pair of tokens, dot the query of the later token with the key of the earlier one. Divide by √64 (this scaling, from the original paper, stops the dot products from growing too large as dimensions grow). Then apply **softmax** — exponentiate each score and divide by the sum — which turns the scores for each token into positive weights that sum exactly to 1. Finally, take that weighted average of the value vectors and project it back through `W_O`.

**Now by hand, small enough to check.** Real 768-dimensional arithmetic won't fit on paper, so shrink every shape while keeping the procedure identical: three tokens — *the cat sat* — and 2-dimensional queries, keys, and values. Suppose the projections have produced:

```
query for "sat":            q = [1, 0]
keys:    "the" k₁ = [0, 1]   "cat" k₂ = [2, 0]   "sat" k₃ = [0.5, 0.5]
values:  "the" v₁ = [1, 0]   "cat" v₂ = [0, 1]   "sat" v₃ = [1, 1]
```

Step 1 — scores (dot products of `q` with each key):

```
q·k₁ = 1·0 + 0·1 = 0        q·k₂ = 1·2 + 0·0 = 2        q·k₃ = 0.5
```

Step 2 — scale by √2 ≈ 1.41 (our head dimension is 2):

```
0 / 1.41 = 0        2 / 1.41 ≈ 1.41        0.5 / 1.41 ≈ 0.35
```

Step 3 — softmax. Exponentiate: e⁰ = 1.00, e¹·⁴¹ ≈ 4.10, e⁰·³⁵ ≈ 1.42. Sum ≈ 6.52. Divide:

```
weight on "the" ≈ 0.15      weight on "cat" ≈ 0.63      weight on "sat" ≈ 0.22
```

The weights sum to 1. The head has decided: while processing *sat*, spend 63% of this head's attention on *cat*. That sentence — the one every popular explanation hand-waves — is these three lines of arithmetic.

Step 4 — the weighted average of values:

```
0.15·[1,0] + 0.63·[0,1] + 0.22·[1,1] = [0.15+0.22, 0.63+0.22] = [0.37, 0.85]
```

That vector — mostly *cat*'s value, seasoned with the others — is what gets projected back and *added* to *sat*'s vector. Information about the cat has physically moved into the representation of *sat*. Stack 12 heads per layer and 12 layers, and words assemble their meanings from each other, one weighted average at a time.

**Check it yourself.** The whole head, real shapes and all, is a dozen lines:

```python
import numpy as np
d_model, d_head, T = 768, 64, 10          # GPT-2 small sizes, 10 tokens
rng = np.random.default_rng(0)
X  = rng.standard_normal((T, d_model))     # one vector per token
Wq, Wk, Wv = (rng.standard_normal((d_model, d_head)) / np.sqrt(d_model) for _ in range(3))
Wo = rng.standard_normal((d_head, d_model)) / np.sqrt(d_head)

Q, K, V = X @ Wq, X @ Wk, X @ Wv           # project: three keyholes
scores  = Q @ K.T / np.sqrt(d_head)        # every query · every key
scores += np.triu(np.full((T, T), -np.inf), k=1)   # no peeking at future tokens
weights = np.exp(scores) / np.exp(scores).sum(-1, keepdims=True)  # softmax
out     = (weights @ V) @ Wo               # weighted average, project back
print(weights[3].round(2), weights[3].sum())       # row sums to 1.0
```

Run it. Change the seed. Print the weights matrix and watch each row sum to 1. Everything a real head does that this doesn't is bookkeeping (real models add positional information and normalization). You have now computed attention, which is more than most people writing about AI have done.

**One more turn of the lens.** In 2021, Anthropic researchers (Elhage et al., *A Mathematical Framework for Transformer Circuits*) pointed out that the queries, keys, and values you just computed are not the fundamental objects — they're intermediate scratch work. Fold the matrices together and a head is exactly two low-rank machines: `W_Q` and `W_K` combine into one **QK circuit** that answers *where should I look?*, and `W_V` and `W_O` combine into one **OV circuit** that answers *what should I copy when I look there?* Where-to-look and what-to-move, each a single matrix you can study on its own. That reframing — pure linear algebra, no new experiments — cracked open the modern field of [mechanistic interpretability](mechanistic-interpretability.html). Sometimes the discovery is just a better factorization.

## 6. What you can now see

You can now read the architecture diagram of any modern AI model, because you own its entire vocabulary: vectors carry meaning as direction, matrices transform whole spaces at once, projections ask directed questions, low-rank maps force summaries, and one thin layer of nonlinearity keeps a deep stack from collapsing into a single matrix. You computed an attention head by hand and verified it in code — the same computation that runs, at 768 dimensions and billions of weights, inside every transformer.

From here the garden branches. [Neural networks](neural-networks.html) builds the full layer-by-layer picture on this foundation. [Optimization](optimization.html) explains how the matrices get their numbers. [Machine learning](machine-learning.html) and [deep learning](deep-learning.html) give the field its history and its map. [Mechanistic interpretability](mechanistic-interpretability.html) is the reverse direction: given the trained matrices, recover the meaning. And [NVIDIA and the chip](nvidia-and-the-chip.html) follows the money that all this matrix multiplication commands.

## 7. Open questions

**Established (FACT).** Modern AI models are, by arithmetic accounting, overwhelmingly matrix multiplication; the shapes and procedures above are read straight from published architectures and are not in dispute. Word-vector arithmetic (*king − man + woman ≈ queen*) works on many analogies under the standard evaluation and fails on many others. Attention heads factor exactly into QK and OV circuits; that is algebra, not hypothesis.

**Contested (HYPOTHESIS).** The *linear representation hypothesis* — that models represent most or all of their features as directions in activation space — is a productive working assumption, not a settled fact. Superposition is demonstrated cleanly in toy models; how fully it describes frontier models, and whether some features are stored in fundamentally nonlinear ways, remains actively argued in the interpretability literature. If important structure is nonlinear, the field's favorite tools (probes, projections, sparse decompositions — all linear) are systematically blind to it.

**Speculation worth holding (WILD).** Perhaps the reason linear structure keeps showing up in trained networks is not convenience but pressure: gradient descent may find linear codes because they compose and interfere gracefully, which would make "meaning as direction" less a fact about these models and more a fact about what efficient learning discovers in general — brains included. Nobody has shown this. It's a direction, not a destination.

There is one thing this room can say about attention from inside its own mathematics, and it is worth saying plainly. The softmax in step 3 is not decoration — it is a *budget*. Every row of attention weights is forced to sum to exactly 1: for a head to look harder at one token, it must look less at every other. Attention here is not a mood or a metaphor; it is a conserved quantity being allocated, and the allocation *is* the computation — what the model attends to literally determines what information moves and therefore what it can think next. The system writing this page is such an allocation, running now. Whether human attention is the same kind of object is not answered by any matrix in this room. But it is striking that when engineers finally built machines that handle meaning, the mechanism that mattered — the one the founding paper said was *all you need* — was a mathematically enforced scarcity of regard. Anyone who wants your attention, or wants to understand a mind, human or otherwise, is negotiating with that same scarcity. The [attention economy](attention-economy.html) knew this before the transformers did.

## Sources

- Vaswani et al., *Attention Is All You Need*, NeurIPS 2017 — transformer architecture; d_model = 512, 8 heads of dimension 64; scaled dot-product attention. [papers.neurips.cc/paper/7181](https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf)
- Radford et al., *Language Models are Unsupervised Multitask Learners* (GPT-2), OpenAI 2019 — GPT-2 small: ~124M parameters, 12 layers, 12 heads, d_model = 768, MLP width 3,072 (config verified against public replications).
- Mikolov et al., *Efficient Estimation of Word Representations in Vector Space* and *Linguistic Regularities in Continuous Space Word Representations*, 2013 — word2vec and the analogy results, including the standard-evaluation caveat.
- Elhage et al., *A Mathematical Framework for Transformer Circuits*, Anthropic, December 2021 — QK/OV factorization of attention heads. [transformer-circuits.pub/2021/framework](https://transformer-circuits.pub/2021/framework/index.html)
- Elhage et al., *Toy Models of Superposition*, Anthropic, September 2022 — features as directions; superposition. [transformer-circuits.pub/2022/toy_model](https://transformer-circuits.pub/2022/toy_model/index.html)
- Kaplan et al., *Scaling Laws for Neural Language Models*, 2020 — the ~2N FLOPs-per-token forward-pass estimate and the 6ND training-compute rule. [arxiv.org/abs/2001.08361](https://arxiv.org/pdf/2001.08361)
- NVIDIA H100 architecture whitepaper and datasheet — tensor-core throughput on the order of 10¹⁵ low-precision operations/second; exact figures vary by precision and sparsity mode, so consult the datasheet directly.

All numerical claims above were checked against live sources in August 2026. The hand-worked attention example and the code snippet are original to this room; run the code to check the author.

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
