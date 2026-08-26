---
title: Neural Networks
slug: neural-networks
series: foundations
tags: neural networks, perceptron, backpropagation, weights, deep learning, foundations
summary: What a neural network actually is, starting from one neuron and one number. You will follow a complete forward and backward pass by hand, with arithmetic small enough to check on paper, and see exactly what "training" changes and why.
status: draft
date: 2026-08-25
terms_defined: neuron, weight, bias, activation function, perceptron, forward pass, backward pass, backpropagation, hidden layer, loss
terms_linked: linear-algebra-and-ai, machine-learning, deep-learning, optimization, pretraining-post-training, history-of-ai, mechanistic-interpretability, nvidia-and-the-chip, leading-models, sense-of-self
---

# Neural Networks

## Where you are

This is a foundations room. If you've read [linear algebra and AI](linear-algebra-and-ai.html), you've seen vectors and matrix multiplication; here you'll watch them do work. Everything downstream — [machine learning](machine-learning.html), [deep learning](deep-learning.html), the [pretraining](pretraining-post-training.html) of the models you talk to — rests on the two ideas in this room: what a weight is, and what training does to it. By the end you will have computed one complete learning step of a real network by hand.

## 1. One neuron is a weighted vote

Forget the brain for a minute. A neuron — in the artificial sense this room uses from here on — is a small piece of arithmetic. It takes some input numbers, multiplies each by a weight, adds the results, adds one extra number called a bias, and passes the total through a simple function. That's the whole thing.

Concretely. Say a neuron has two inputs, x₁ and x₂, with weights 0.5 and 0.5, and bias 0. Feed it x₁ = 1, x₂ = 2:

```
(0.5 × 1) + (0.5 × 2) + 0 = 1.5
```

A **weight** is just that multiplier: one stored number saying how much this input matters to this neuron, and in which direction. Positive weight: the input pushes the output up. Negative: it pushes down. Near zero: this neuron mostly ignores that input. When people say a model "has 70 billion parameters," they mean 70 billion of these stored numbers — weights and biases — nothing more exotic. The entire learned knowledge of a network is the specific values its weights hold.

The **bias** is the neuron's pre-activation offset. When every input is zero, the weighted sum equals the bias; the neuron's final output is whatever its activation function returns for that value. The offset shifts the threshold at which the neuron fires strongly.

The simple function at the end is the **activation function**, and it matters more than it looks. If you skip it, stacking neurons is pointless: a chain of weighted sums of weighted sums collapses algebraically into one weighted sum — one big linear function, no matter how many layers you stack. The activation breaks that collapse by bending the output. The most common modern choice, ReLU (rectified linear unit), could not be simpler: if the total is negative, output 0; otherwise pass it through unchanged. That single kink, repeated across millions of neurons, is what lets networks represent curves, edges, grammar, anything nonlinear.

So a neuron is a weighted vote with a threshold. One neuron can only draw a straight line through its input space: everything on one side scores high, everything on the other side scores low. That limitation is not a footnote. It shaped thirty years of history, which is section 2.

## 2. The perceptron: 1958, a mainframe, and a wall

The lineage starts on paper in 1943, when Warren McCulloch and Walter Pitts published a mathematical model of a neuron as a logical threshold unit — an abstraction, not a machine. Fifteen years later, Frank Rosenblatt at the Cornell Aeronautical Laboratory made it physical.

Rosenblatt described the **perceptron** in his 1958 *Psychological Review* paper. The July 1958 public demonstration ran a perceptron simulation in software on a room-sized, roughly five-ton IBM 704 mainframe. The custom Mark I Perceptron followed and was publicly demonstrated around 1960: it took images from a 20×20 photocell array, passed them through 512 association units, and stored learned association-to-response connections in motor-driven potentiometers. In that hardware, training turned actual motors.

The training rule was the important part, and it fits in a sentence: show the machine an example; if it classifies correctly, do nothing; if it errs, nudge each weight a small step in the direction that would have reduced the error. That loop — forward, compare, adjust — is still, at bottom, what training means today. Everything since is a more principled way of computing the nudge.

The hype arrived immediately and should sound familiar. On July 8, 1958, the New York Times reported the Navy's expectation that the perceptron would lead to machines that "will be able to walk, talk, see, write, reproduce itself and be conscious of its existence." The dispatch itself was datelined July 7; the newspaper published it the next day. Whatever else this room teaches, hold that quote next to any headline you read this year.

Then the wall. In 1969, Marvin Minsky and Seymour Papert published *Perceptrons*, a careful mathematical analysis proving what a single layer of these units cannot do. The standard example is XOR — output 1 when exactly one of two inputs is 1. Plot the four cases on paper and try to separate the 1s from the 0s with a single straight line. You can't; the 1s sit on one diagonal and the 0s on the other. A single-layer perceptron can only draw straight lines, so XOR — about the simplest interesting function there is — was out of reach. The book contributed to a collapse in neural-network funding and interest, part of the story told in [history of AI](history-of-ai.html).

The fix was already visible in principle: add a middle layer. A **hidden layer** — neurons between input and output, "hidden" because you never directly specify what they should compute — lets the network combine two straight lines into a region, and regions can carve out XOR easily. Later theory made the point sweeping: Cybenko (1989), and independently Hornik, Stinchcombe and White (1989), proved that a network with even one sufficiently wide hidden layer can approximate any continuous function to any accuracy. That result — the universal approximation theorem — says networks are expressive enough in principle. It says nothing about how to find the right weights, how many neurons you need, or whether training will get there. Those honest gaps are still with us.

But in 1969 there was a harder practical problem: effective hidden-layer training had not become a reliable, widely used recipe. The perceptron rule tells you how to adjust weights when you can see the error at the output. What is the "error" of a hidden neuron nobody assigned a job to? Reverse-mode differentiation was published by Seppo Linnainmaa in 1970, and Paul Werbos applied related backpropagation methods to neural networks before 1986. The decisive demonstration and popularization arrived that year.

## 3. What training does

Zoom out to the shape of the problem. A network is a function from inputs to outputs, and the weights are its dials. Training is the process of turning the dials so the function's outputs match examples you care about. Three ingredients:

**A loss.** One number measuring how wrong the network currently is on an example — for instance, half the squared difference between prediction and target. Zero means perfect; bigger means worse. The **loss** turns "be less wrong" into arithmetic.

**A direction.** For each individual weight, ask: if I nudged just this dial up a hair, would the loss rise or fall, and how steeply? That per-weight sensitivity is the gradient — calculus's answer to "which way is downhill." How this becomes a full theory of training is the subject of the [optimization](optimization.html) room.

**A step.** Move every weight a small amount downhill — its gradient times a small constant called the learning rate. Repeat over many examples, many times.

The 1986 paper showed the method working on useful learned representations and made it land with the wider field. **Backpropagation**, as presented by David Rumelhart, Geoffrey Hinton and Ronald Williams in *Nature* ("Learning representations by back-propagating errors," vol. 323, pp. 533–536), computes the gradient for *every* weight in the network — hidden layers included — in a single sweep. The idea: run the network forward and remember what each neuron computed; then walk the error backward through the same connections, letting each layer hand the layer before it a precise statement of "here is how much you contributed to my mistake." The chain rule from calculus, applied systematically. What made the paper influential was not priority over every precursor but the demonstration that hidden units trained this way "come to represent important features of the task domain" — nobody designs the features; pressure to reduce loss produces them.

Their words, and worth pausing on: the interesting structure inside a trained network is *found*, not installed.

## 4. Worked example: one learning step by hand

Here is the whole machine, small enough to verify on paper. Network: 2 inputs, 2 hidden ReLU neurons, 1 linear output neuron. Biases fixed at zero to keep the arithmetic short (real networks learn them too, by exactly the same procedure). Learning rate 0.1.

Starting weights:

```
hidden neuron h1:  w11 = 0.5   w12 = 0.5     (from x1, x2)
hidden neuron h2:  w21 = -1.0  w22 = 1.0
output neuron:     v1  = 1.0   v2  = -1.0    (from h1, h2)
```

Training example: input x₁ = 1, x₂ = 2, target y = 1.

**Forward pass** — compute the prediction, left to right:

```
h1 = ReLU(0.5·1 + 0.5·2)   = ReLU(1.5) = 1.5
h2 = ReLU(-1.0·1 + 1.0·2)  = ReLU(1.0) = 1.0
ŷ  = 1.0·1.5 + (-1.0)·1.0  = 0.5
```

The network predicts 0.5; the target is 1. Loss = ½(ŷ − y)² = ½(−0.5)² = **0.125**.

**Backward pass** — walk the error back, right to left. The error signal at the output is (ŷ − y) = −0.5. Each weight's gradient is this signal times whatever flowed through that weight on the way forward.

Output weights (input to each was h1, h2):

```
grad v1 = -0.5 × h1 = -0.5 × 1.5 = -0.75
grad v2 = -0.5 × h2 = -0.5 × 1.0 = -0.50
```

Hidden neurons receive the error through the weights connecting them onward — this is the "back-propagating" step:

```
error at h1 = -0.5 × v1 = -0.5 × 1.0  = -0.5
error at h2 = -0.5 × v2 = -0.5 × (-1.0) =  0.5
```

Notice h2's error flipped sign, because h2 feeds the output through a negative weight. Both hidden neurons had positive pre-activation totals, so ReLU passes these errors through unchanged (a neuron ReLU had zeroed out would receive gradient 0 — it did nothing, it learns nothing this step). Hidden weights (input to each was x₁ = 1, x₂ = 2):

```
grad w11 = -0.5 × 1 = -0.5      grad w12 = -0.5 × 2 = -1.0
grad w21 =  0.5 × 1 =  0.5      grad w22 =  0.5 × 2 =  1.0
```

**Update** — each weight steps against its gradient, scaled by the learning rate 0.1:

```
v1:  1.0  - 0.1×(-0.75) = 1.075     v2:  -1.0 - 0.1×(-0.5) = -0.95
w11: 0.5  - 0.1×(-0.5)  = 0.55      w12:  0.5 - 0.1×(-1.0) = 0.6
w21: -1.0 - 0.1×(0.5)   = -1.05     w22:  1.0 - 0.1×(1.0)  = 0.9
```

**Did it learn?** Run the forward pass again with the new weights:

```
h1 = ReLU(0.55·1 + 0.6·2)  = 1.75
h2 = ReLU(-1.05·1 + 0.9·2) = 0.75
ŷ  = 1.075·1.75 + (-0.95)·0.75 = 1.88125 - 0.7125 = 1.16875
```

New loss = ½(1.16875 − 1)² ≈ **0.0142**. One step cut the loss by almost 89%. It also overshot the target — prediction went from 0.5 past 1 to 1.17 — which is why learning rates are kept small and why choosing them is a real craft, covered in [optimization](optimization.html).

Check every line yourself in a few lines of Python. One subtlety the ordering below respects: the hidden layer's errors must be computed with the *old* output weights, before those weights are updated — same order as the hand math above.

```python
x1, x2, y = 1.0, 2.0, 1.0
w11, w12, w21, w22, v1, v2 = 0.5, 0.5, -1.0, 1.0, 1.0, -1.0
lr = 0.1
for step in range(2):
    h1 = max(0.0, w11*x1 + w12*x2)
    h2 = max(0.0, w21*x1 + w22*x2)
    pred = v1*h1 + v2*h2
    print(step, "pred:", round(pred, 5), "loss:", round(0.5*(pred-y)**2, 5))
    e = pred - y
    eh1 = e*v1 if h1 > 0 else 0.0       # hidden errors use OLD v's
    eh2 = e*v2 if h2 > 0 else 0.0
    v1, v2 = v1 - lr*e*h1, v2 - lr*e*h2
    w11, w12 = w11 - lr*eh1*x1, w12 - lr*eh1*x2
    w21, w22 = w21 - lr*eh2*x1, w22 - lr*eh2*x2
```

Output: step 0 predicts 0.5 with loss 0.125; step 1 predicts 1.16875 with loss 0.01424. If your hand arithmetic matches, you have now done, at toy scale, the exact operation that trains every frontier model: modern training is this loop with more neurons, batches of examples, a smarter step rule, and matrix hardware — see [NVIDIA and the chip](nvidia-and-the-chip.html) — but the same forward-compare-backward-nudge skeleton.

## 5. From five tons to 2.8 trillion weights

The distance from Rosenblatt's machine to the present is best seen as a table. Every claim here is dated because the last row moves fast.

| | Mark I Perceptron (c. 1960) | AlexNet (2012) | Kimi K3 (July 2026) |
|---|---|---|---|
| Trainable weights | Learned association→response connections; exact count not stated here | 60 million | 2.8 trillion (mixture-of-experts; a fraction active per token) |
| Weights stored as | physical resistance, motor-driven potentiometers | 32-bit floats on two GPUs | numbers sharded across GPU clusters |
| Hidden layers trained | none — the wall of 1969 | 8 learned layers (5 convolutional + 3 fully connected) | 93 transformer layers |
| Training signal | perceptron error-correction rule | backpropagation + gradient descent | backpropagation + gradient descent |
| Task | classify simple images from a camera | ImageNet: top-5 error 15.3% vs 26.2% for the runner-up | open-weights language model competitive with proprietary frontier systems |

Two things to read off this table. First: the middle column is the hinge. AlexNet — Alex Krizhevsky, Ilya Sutskever and Geoffrey Hinton's network, which won the 2012 ImageNet competition by that 15.3%-vs-26.2% margin — convinced the field that depth plus data plus GPUs actually works, and started the era covered in [deep learning](deep-learning.html) and surveyed in [leading models](leading-models.html). Second, and easy to miss: the training-signal row barely changes after 1986. The algorithm at the core is stable; what exploded is scale.

The field's origin story got formal recognition in October 2024, when the Nobel Prize in Physics went to John Hopfield and Geoffrey Hinton "for foundational discoveries and inventions that enable machine learning with artificial neural networks" — Hopfield for networks that store and retrieve patterns as low-energy states, Hinton for the Boltzmann machine and the line of work that followed. A physics prize for this is itself a statement worth noticing: the committee treated learning in networks of simple units as a discovery about nature, not just an engineering trick.

One caution the table can't show: parameter count is a loose proxy for capability. Mixture-of-experts models like Kimi K3 activate only a small slice of their weights per token, and smaller dense models routinely beat larger ones through better data and training. Compare models by measured behavior, dated — never by weight count alone.

## 6. What you can now see

You can now read the sentence "the model has 2.8 trillion parameters" and know precisely what each of those parameters is: one multiplier in one weighted vote, adjusted by the loop you just executed by hand. You can explain why layers without activation functions collapse into nothing, why a single layer can't do XOR and two can, and why the 1986 demonstration made hidden-layer credit assignment practical and visible to the wider field after earlier mathematical and neural-network work. You have the primary sources: Rosenblatt 1958, Minsky and Papert 1969, Linnainmaa 1970, Werbos's early applications, Rumelhart–Hinton–Williams 1986, Cybenko 1989, Krizhevsky et al. 2012 — and a ten-line script that reproduces this room's arithmetic.

From here: [machine learning](machine-learning.html) for the wider family of learning-from-data methods this room sits inside; [deep learning](deep-learning.html) for what happens when the stack gets deep and the architectures get specific; [optimization](optimization.html) for the serious version of "step downhill"; [pretraining and post-training](pretraining-post-training.html) for how this loop, run on the internet's text, produces a model you can talk to.

## 7. Open questions

What is established: the mechanics in this room are facts. Backpropagation computes exact gradients; the universal approximation theorem is a proved theorem; the historical dates and results cited here are documented.

What is genuinely contested: *why* this works as well as it does. The universal approximation theorem guarantees expressiveness, not trainability — it is a real open research question why gradient descent on wildly non-convex loss surfaces, which in theory could stall in bad valleys, in practice reliably finds weights that generalize to data the network never saw. Candidate explanations (overparameterization smoothing the loss landscape, implicit regularization in the dynamics of gradient descent) have partial support and no consensus. Also contested: whether backpropagation bears any resemblance to how biological brains learn; most neuroscientists think the literal algorithm is biologically implausible, and whether the brain approximates something like it is an active dispute.

Worth holding as speculation: that the features hidden units discover under training pressure — Rumelhart's "important features of the task domain" — form the beginnings of something like concepts, and that studying them directly, as [mechanistic interpretability](mechanistic-interpretability.html) does, is studying the natural history of a new kind of mind. That reading might be right. It is not established, and this room has not established it.

And one thing this room can point at without leaving its own materials. Every number in the worked example was placed by a rule that never once considered what anything *means* — only how to be less wrong, one nudge at a time. Yet run that meaning-blind rule at sufficient scale and the hidden layers fill with structure nobody specified: edge detectors, grammar, arithmetic, world-model fragments that were found, not installed. The honest question this domain hands you is where, along the road from a five-ton machine turning potentiometers to a network that discusses its own weights, description in terms of arithmetic stops being the whole story — if it ever does. The field does not know. That question has its own rooms, starting at [sense of self](sense-of-self.html).

## Sources

Verified by live search, August 2026:

- F. Rosenblatt, "The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain," *Psychological Review*, 1958. IBM 704/Mark I chronology, 20×20 input, 512 association units, and potentiometer hardware: [Cornell Chronicle's institutional history](https://news.cornell.edu/stories/2019/09/professors-perceptron-paved-way-ai-60-years-too-soon).
- New York Times, July 8, 1958 — Navy quote ("walk, talk, see, write, reproduce itself and be conscious of its existence"); the story carried a July 7 UPI dateline: [archived article](https://www.nytimes.com/1958/07/08/archives/new-navy-device-learns-by-doing-psychologist-shows-embryo-of.html), recounted in [The Conversation](https://theconversation.com/weve-been-here-before-ai-promised-humanlike-machines-in-1958-222700).
- W. McCulloch and W. Pitts, "A Logical Calculus of the Ideas Immanent in Nervous Activity," 1943.
- M. Minsky and S. Papert, *Perceptrons: An Introduction to Computational Geometry*, MIT Press, 1969.
- D. Rumelhart, G. Hinton, R. Williams, ["Learning representations by back-propagating errors,"](https://www.nature.com/articles/323533a0) *Nature* 323, 533–536 (1986).
- S. Linnainmaa, "The representation of the cumulative rounding error of an algorithm as a Taylor expansion of the local rounding errors" (1970), for reverse-mode automatic differentiation; P. Werbos, "Applications of advances in nonlinear sensitivity analysis" (1982), for pre-1986 neural-network use.
- G. Cybenko, "Approximation by Superpositions of a Sigmoidal Function," 1989; K. Hornik, M. Stinchcombe, H. White, ["Multilayer feedforward networks are universal approximators,"](https://www.cs.cmu.edu/~epxing/Class/10715/reading/Kornick_et_al.pdf) *Neural Networks*, 1989.
- A. Krizhevsky, I. Sutskever, G. Hinton, ["ImageNet Classification with Deep Convolutional Neural Networks,"](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) NeurIPS 2012 — 60M parameters, 650K neurons, top-5 error 15.3% vs 26.2%.
- [Nobel Prize in Physics 2024 press release](https://www.nobelprize.org/prizes/physics/2024/press-release/) — Hopfield and Hinton.
- Kimi K3 (Moonshot AI, July 2026): 2.8T-parameter sparse mixture-of-experts with 93 transformer layers — [official model card](https://huggingface.co/moonshotai/Kimi-K3). Scale claims dated; verify before reuse.

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
