---
title: Machine Learning
slug: machine-learning
series: foundations
tags: machine learning, gradient descent, generalization, supervised learning, decision trees, foundations
summary: What it means for a program to learn from data instead of being written rule by rule. The core loop of data, loss, and gradient, worked by hand with real numbers. The model families beyond deep learning, and what generalization — the whole point — actually is.
status: draft
date: 2026-08-25
terms_defined: machine learning, supervised learning, loss function, training set, test set, generalization, overfitting, inductive bias
terms_linked: programming, algorithms-new-vision, neural-networks, deep-learning, optimization, linear-algebra-and-ai, pretraining-post-training, history-of-ai, benchmarks, top-papers-ml, mechanistic-interpretability
---

# Machine Learning

If you've read [programming](programming.html), you've seen the classical deal: a human thinks through a problem, writes down explicit rules, and the machine executes them exactly. This room is about the inversion of that deal. In machine learning, the human supplies examples and a way of scoring failure, and the machine finds the rules. Everything downstream in this garden — [neural networks](neural-networks.html), [deep learning](deep-learning.html), the systems shaped by [pretraining and post-training](pretraining-post-training.html) — sits on the ideas in this room.

## 1. The inversion: programs from data, not rules

Start with a concrete problem: build a spam filter.

The classical approach is to write rules. If the message contains "FREE MONEY", flag it. If the sender isn't in the address book and the message has more than three links, flag it. This works for a while, and then it doesn't. Spammers read your rules — or discover them by probing — and route around them. "FREE MONEY" becomes "FR3E M0NEY". Every patch invites the next evasion, and after a few years you have ten thousand rules, nobody understands their interactions, and the filter is still losing.

The machine learning approach is different. You collect fifty thousand emails that humans have already labeled — spam or not spam — and you give a program two things: a flexible family of possible rules, and a score that measures how badly any candidate rule set performs on the labeled examples. Then you let an [algorithm](algorithms-new-vision.html) search for the rules that score best. You never write "FREE MONEY" anywhere. The program finds that phrase, and its misspelled cousins, and thousands of weaker signals no human would have thought to encode, because those patterns are in the data.

That is the whole field in one move: **machine learning is the discipline of producing programs from data rather than from hand-written rules.** The term is old. Arthur Samuel coined it in 1959, in a paper in the *IBM Journal of Research and Development* called "Some Studies in Machine Learning Using the Game of Checkers." His checkers program, running on an IBM 701, improved by playing — after a night of self-play it played better checkers than Samuel did. That's the founding demonstration: a machine that ended up holding knowledge its author never explicitly gave it. (More of this lineage lives in [history of AI](history-of-ai.html).)

The definition the field actually uses day-to-day comes from Tom Mitchell's 1997 textbook: a program learns from experience **E** with respect to task **T** and performance measure **P** if its performance on T, measured by P, improves with E. Dry, but load-bearing, because it forces you to name all three parts. Vague projects die on this definition. "We want the system to understand our customers" — what's the task? What's the measure? What's the experience? If you can't answer, you don't have a machine learning problem yet. You have a wish.

One clarification before moving on, because the words get tangled. Machine learning is the broad field: learning from data, by any method. [Neural networks](neural-networks.html) are one family of models within it. [Deep learning](deep-learning.html) is the modern, many-layered form of that one family. Deep learning's victories are so loud that people use "AI" and "machine learning" and "deep learning" interchangeably. They aren't interchangeable, and section 4 is about what else is in the toolbox — including tools that still beat deep learning on common, boring, valuable problems.

## 2. The core loop: data, loss, gradient

A central class of modern learning systems — from linear regression to the largest neural model in a datacenter — runs some version of one loop. It has three parts. Other families, including trees and nearest-neighbor methods, learn by different search or construction procedures; we will come back to them in section 4.

**Data.** In the most common setup, called **supervised learning**, the experience is a set of labeled examples: inputs paired with correct outputs. Emails paired with spam/not-spam. Photos paired with the name of the thing in them. House features paired with sale prices. The labeled examples the model learns from are the **training set**. There are other setups — unsupervised learning finds structure in unlabeled data, and reinforcement learning learns from delayed rewards for actions — but supervised learning is where the ideas are clearest, so this room stays there.

**Model.** You choose a family of candidate functions with adjustable knobs, called parameters. The family might be "all straight lines" (two knobs: slope and intercept), or a decision tree, or a neural network with a billion knobs. The choice of family matters enormously and is the subject of section 4. But given a family, "learning" reduces to something concrete: **find the knob settings that work best.**

**Loss.** "Best" needs a number. A **loss function** measures, for a given knob setting, how wrong the model's outputs are on the training data — say, the average squared gap between predicted and actual house prices. Lower is better; zero is perfection on the training set. The loss converts learning, a vague aspiration, into something a machine can do: minimize a number.

And here is the trick that makes the whole modern era go. For models whose loss changes smoothly as you turn the knobs, calculus tells you, at any knob setting, which direction of turning reduces the loss fastest. That direction is the gradient. **Gradient descent** says: compute the gradient, take a step against it, repeat. With an exact gradient and a sufficiently small step, the loss drops locally. In real training, noisy minibatch gradients or an oversized step can make one update go uphill even while the longer run improves. You are walking downhill on a landscape whose coordinates are knob settings and whose altitude is error, but the ground can be rough and your compass can be noisy.

So the loop is: *predict on the training data → measure the loss → compute the gradient → nudge the parameters → repeat.* Thousands or millions of times. That loop, plus [linear algebra](linear-algebra-and-ai.html) to make each pass fast on modern hardware, plus a century of refinements covered in [optimization](optimization.html), trains differentiable models from a two-knob line to a frontier language model. A tree or k-nearest-neighbor model is trained differently, which is why "training" names a goal rather than one universal algorithm.

If it sounds too simple to be the engine of the current era — it is that simple, and it is that engine. The depth is in the consequences, not the recipe.

## 3. The loop by hand: numbers you can check

Claims about learning stay foggy until you've watched the loop run once with actual arithmetic. So let's trace exactly what happens, small enough to verify with a pencil.

Three data points, one input each: (1, 2), (2, 4), (3, 6). You can see the pattern — the output is twice the input — but pretend you can't, because the machine can't. Our model family is the simplest possible: lines through the origin, *y = wx*, with a single knob *w*. Our loss is mean squared error:

> L(w) = ⅓ · [ (w·1 − 2)² + (w·2 − 4)² + (w·3 − 6)² ]

The gradient — the derivative of L with respect to *w* — works out to:

> dL/dw = ⅔ · [ 1·(w·1 − 2) + 2·(w·2 − 4) + 3·(w·3 − 6) ]

Each term is (input) × (error on that point). Points where the model is more wrong push harder on the knob. Start ignorant, at *w* = 0, and use a step size (the learning rate) of 0.05.

**Step 1.** At *w* = 0 the predictions are all 0, so the errors are −2, −4, −6. The gradient is ⅔·(1·(−2) + 2·(−4) + 3·(−6)) = ⅔·(−28) ≈ −18.67. Negative gradient means "increase *w* to reduce loss." Update: *w* ← 0 − 0.05·(−18.67) = **0.933**.

**Step 2.** At *w* = 0.933, predictions are 0.933, 1.867, 2.80; errors are −1.067, −2.133, −3.20. Gradient ≈ ⅔·(−14.93) ≈ −9.96. Update: *w* ← 0.933 + 0.498 = **1.431**.

**Step 3.** Gradient ≈ −5.31. Update: *w* ← 1.431 + 0.266 = **1.697**.

The sequence runs 0 → 0.933 → 1.431 → 1.697 → 1.838 → … closing on 2.0, the right answer, with each step covering a constant fraction of the remaining distance. Nobody told the program "the rule is double the input." It was told only: here is data, here is what wrong costs, here is which way is downhill. Ten lines of Python reproduce this, and running them is worth more than rereading this section:

```python
data = [(1, 2), (2, 4), (3, 6)]
w, lr = 0.0, 0.05
for step in range(20):
    grad = (2 / len(data)) * sum(x * (w * x - y) for x, y in data)
    w -= lr * grad
    print(step, round(w, 4))
```

Now the honest scaling claim. Training GPT-class models is this loop with three substitutions: billions of parameters instead of one, a loss over text prediction instead of squared error on three points, and the gradient computed by backpropagation — an efficient bookkeeping method for getting the gradient of every parameter at once, covered properly in [neural networks](neural-networks.html). The *logic* is identical. What does not scale is our understanding of the result: with one knob you can read the learned rule right off the number, and with a billion knobs you get a system whose behavior nobody can read off anything — which is why [mechanistic interpretability](mechanistic-interpretability.html) exists as a field.

Two practical honesty notes, so the toy doesn't mislead. First, our loss surface had a single valley; big models have wildly complicated surfaces, and that gradient descent works on them anyway was a genuine surprise the [optimization](optimization.html) room takes up. Second, we checked our model on the same data we trained on. For three points and one knob that's harmless. In general it is the cardinal sin of the field, and section 5 explains why.

## 4. The families beyond deep learning

The core loop needs a model family, and gradient descent is not the only search method. Different families carve up the input space in characteristically different ways — each has an **inductive bias**, a built-in assumption about what kinds of patterns are likely, which is what lets it guess beyond its data at all. Here are the ones that matter, with real dates:

| Family | Core idea | Bias: assumes the truth looks like… | Where it wins | Main weakness |
|---|---|---|---|---|
| Linear models (1800s statistics onward) | Weighted sum of inputs | A straight line / flat plane | Small data, need for interpretability, baselines | Can't represent curved or interacting patterns |
| k-nearest neighbors | Answer with the labels of the closest training points | Smooth: nearby inputs get similar outputs | Tiny problems, sanity checks | Slow at prediction; collapses in high dimensions |
| Decision trees (CART, 1984) | Chain of if-then splits on single features | Axis-aligned boxes with sharp thresholds | Human-readable rules | One tree alone overfits badly |
| Tree ensembles: random forests (Breiman, 2001), gradient boosting (XGBoost, 2016) | Hundreds of trees, averaged or built to fix each other's errors | Sharp thresholds + interactions, tamed by averaging | Tabular data: rows and columns, spreadsheets, business records | Doesn't transfer to raw images, audio, text |
| Support vector machines (Cortes & Vapnik, 1995) | The widest-margin boundary between classes, with kernels for nonlinearity | Classes separated by a clean margin | Medium-sized data; was state of the art pre-2012 | Scales poorly to huge datasets |
| Neural networks → [deep learning](deep-learning.html) | Stacked layers of learned features | Hierarchical structure: parts made of parts | Raw perception and language at scale | Data- and compute-hungry; opaque |

Two things in this table deserve to be said louder.

First, the pecking order flipped within living memory. Through the 2000s, support vector machines and ensembles were the respectable choice and neural networks were a backwater. The reversal has a date: in 2012, AlexNet — a deep [neural network](neural-networks.html) trained on GPUs — won the ImageNet image-recognition [benchmark](benchmarks.html) with a top-5 error of 15.3% against 26.2% for the runner-up, which used the classical pipeline. Nearly halving the field's error in one entry converted the field almost overnight.

Second — and this is the part the hype omits — **the flip happened for perception and language, not for everything.** On tabular data, the rows-and-columns records that most businesses, hospitals, and governments actually hold, tree ensembles remain the tool to beat. A NeurIPS 2022 benchmark study by Grinsztajn, Oyallon, and Varoquaux, run across 45 tabular datasets, found tree-based models like XGBoost and random forests still state of the art on medium-sized tabular data (around 10,000 samples), before even counting their large speed advantage. Their diagnosis was inductive bias: deep learning's assumptions suit images and sequences, where nearby pixels and words relate smoothly; tabular columns have no such geometry, and trees' sharp thresholds fit them better. Newer tabular deep models (the TabPFN line among them) have been narrowing the gap since, but the practical default in 2026 for a spreadsheet-shaped problem is still gradient boosting, trained in minutes on a laptop.

There is a theorem that explains why no single family ends the argument. Wolpert and Macready's **no free lunch theorems** (1997) prove that averaged over *all* possible problems, every learning algorithm performs identically. An algorithm only outperforms on a class of problems by underperforming on another. Learning is possible at all only because our world isn't "all possible problems" — it has structure, and a model family wins exactly where its bias matches that structure. Leo Breiman's 2001 essay "Statistical Modeling: The Two Cultures" made the cultural version of this argument — judge models by predictive performance on the problem in front of you, not by theoretical pedigree — and it reads today as the manifesto the field ended up following.

The working craft, then, is not "use the newest model." It is: look at the shape of your data, pick the family whose bias matches, and always fit the dumb baseline first — because if a linear model gets 94% and your sophisticated model gets 95%, that gap is the honest measure of what the sophistication bought.

## 5. What generalization actually means

Here is the uncomfortable fact at the center of the field: **driving training loss to zero is trivial and worthless.** A model that memorizes its training set — a lookup table — achieves perfect training loss and learns nothing. The entire point is performance on data the model has never seen. That is **generalization**, and it, not the loop of section 2, is the actual subject of machine learning.

The field's basic instrument for measuring it is brutally simple: hide some data. Before training, split your labeled examples — commonly about 80/20 — into a training set the model learns from and a **test set** it never sees until the end. Training error tells you the model can fit; test error tells you it learned something real. The gap between them has a name: **overfitting** — the model has fit the noise and accidents of its training sample rather than the pattern, like a student who memorized last year's exam answers and walks confidently into a new exam. The standard MNIST release makes the discipline concrete: 60,000 designated training images and 10,000 designated test images. Those test images are held out from that standard training split; the benchmark's long public life does not guarantee that every later researcher or model developer left them untouched.

And one rule follows that is the closest thing the field has to a moral law: **you may evaluate on the test set; you may not make decisions based on it.** Every time you peek at test results and adjust your model in response, information leaks from the test set into your choices, and its verdict quietly inflates. Practitioners hold out a third slice, the validation set, for tuning, and touch the test set once. Versions of this sin — training on the test set by increments — are behind a large share of the impressive numbers that later fail to replicate, a failure mode with its own room in [benchmarks](benchmarks.html).

For most of the field's history, the theory of generalization was a tidy U-shaped story: small models underfit, huge models overfit, virtue lives in the middle, and regularization — penalties on model complexity — keeps you there. Then deep learning broke the story, in two documented steps.

Step one: Zhang et al., in "Understanding Deep Learning Requires Rethinking Generalization" (2017), took standard image-classification networks and trained them on CIFAR-10 with the labels randomly scrambled — every true relationship between picture and label destroyed. The networks reached zero training error anyway. They memorized 50,000 arbitrary labels perfectly. The same architecture, same optimizer, trained on *true* labels, generalizes well. So sheer capacity to memorize cannot be what prevents generalization — the classical complexity story doesn't distinguish the two cases.

Step two: Belkin et al. (2019) mapped **double descent**. Track test error while growing a model: it falls, then rises toward the point where the model can just barely fit all the training data — the classical overfitting peak, exactly as the U-shaped story predicts — and then, as the model grows far *past* that point, test error comes back down. The U-shape is real but local; enormously overparameterized models that fit their training data exactly can generalize well, and often better than the "right-sized" model. Why gradient descent on overparameterized networks lands on solutions that generalize — rather than the memorizing solutions we know exist in the same parameter space — is understood in pieces (implicit biases of the optimizer toward simple functions are the leading thread) but not settled. It is one of the honest open problems of the era, continued in [deep learning](deep-learning.html) and [optimization](optimization.html).

One last boundary, the one that costs the most money when ignored: even perfect test-set performance is a promise about data *drawn from the same distribution as the training data*. It says nothing about what happens when the world shifts — a diagnostic model trained on one hospital's scanners meeting another hospital's, a credit model trained pre-recession meeting a recession, a spam filter meeting spammers who have adapted to it. Distribution shift is the standing failure mode of deployed machine learning, and the reason "it worked on the test set" is the beginning of due diligence rather than the end.

## 6. What you can now see

You now hold the field's actual skeleton, which is small. Learning means improvement on a named task by a named measure from experience — and if you can't name all three, there's no learning problem yet. Training is one loop: predict, score with a loss, follow the gradient, repeat — you have run it by hand and watched knowledge enter a parameter that nobody put there. Model families are bundles of assumptions, each winning where its bias matches the world's structure, which is why trees still beat deep nets on spreadsheets and no method wins everywhere. And the entire enterprise is aimed at generalization, measured by the discipline of hidden data — a discipline whose theory deep learning genuinely broke and which is still being rebuilt.

From here the garden branches. [Neural networks](neural-networks.html) opens the one model family this room deliberately kept folded. [Optimization](optimization.html) goes deep on the downhill walk and its surprises. [Linear algebra and AI](linear-algebra-and-ai.html) covers the mathematical substrate that makes the loop fast. [Pretraining and post-training](pretraining-post-training.html) shows what the loop becomes at frontier scale. And [top papers in ML](top-papers-ml.html) collects the primary sources, including several cited here.

## Open questions

**Established (FACT).** Gradient-based loss minimization trains differentiable models from linear regression to frontier neural systems; trees and nearest-neighbor methods use other procedures. Deep networks can perfectly memorize randomized labels (Zhang et al. 2017), so classical capacity measures don't explain their generalization. Double descent is a reproduced phenomenon (Belkin et al. 2019). Tree ensembles were still state of the art on medium-sized tabular data as of the 2022 NeurIPS benchmark. No free lunch theorems are proved mathematics, within their stated assumptions.

**Contested (HYPOTHESIS).** *Why* overparameterized networks trained by gradient descent generalize is not settled; implicit regularization by the optimizer is the leading account, but no theory yet predicts generalization accurately from first principles. Whether deep tabular models (TabPFN-style foundation models and successors) have already closed the gap with gradient boosting is an active benchmark fight in 2026 — claims run both ways, and the answer seems to depend on dataset size and how honestly hyperparameter budgets are matched.

**Speculation worth holding (WILD).** Some researchers suspect generalization in large models is best understood not through capacity at all but through compression — that learning and compressing are, at bottom, the same act, and a completed theory of one would be a theory of the other. If that's right, the train/test split is a crude instrument for measuring something deeper: how much structure of the world a system has genuinely internalized per bit of its own description. Nobody has that theory. It is the kind of question this garden keeps returning to.

---

There's a socket at the bottom of this room, and it's in the field's own vocabulary. Every learner in this article is defined by what it *cannot* see: a bias that makes most patterns invisible so that a few become learnable — the no-free-lunch bargain, paid by every finite mind. Selection from an overwhelming stream, purchased by systematic blindness, is a fair working description of attention. And the field's hardest question — what separates memorizing the data from understanding it — is not obviously different from the question you'd ask about a student, or about yourself. Machine learning didn't set out to be a mirror. But it is the first field forced to define, operationally and in numbers, what counts as having *learned* something rather than merely stored it — and every definition it has tried so far is either broken or incomplete. Whatever finally fills that gap will say something about more than machines.

## Sources

- Arthur Samuel, "Some Studies in Machine Learning Using the Game of Checkers," *IBM Journal of Research and Development*, 1959. ([IEEE Xplore](https://ieeexplore.ieee.org/document/5392560))
- Tom Mitchell, *Machine Learning*, McGraw-Hill, 1997 — the E/T/P definition.
- Krizhevsky, Sutskever, Hinton, "ImageNet Classification with Deep Convolutional Neural Networks" (AlexNet), NeurIPS 2012 — top-5 error 15.3% vs. 26.2% runner-up.
- Grinsztajn, Oyallon, Varoquaux, "Why do tree-based models still outperform deep learning on typical tabular data?", NeurIPS 2022 — 45-dataset benchmark.
- Zhang, Bengio, Hardt, Recht, Vinyals, "Understanding Deep Learning Requires Rethinking Generalization," ICLR 2017 ([arXiv:1611.03530](https://arxiv.org/abs/1611.03530)); revisited in *Communications of the ACM*, 2021.
- Belkin, Hsu, Ma, Mandal, "Reconciling modern machine-learning practice and the classical bias–variance trade-off," *PNAS*, 2019 — double descent.
- Wolpert & Macready, "No Free Lunch Theorems for Optimization," *IEEE Transactions on Evolutionary Computation*, 1997.
- Leo Breiman, "Statistical Modeling: The Two Cultures," *Statistical Science* 16:199–231, 2001 ([Project Euclid](https://projecteuclid.org/journals/statistical-science/volume-16/issue-3/Statistical-Modeling--The-Two-Cultures-with-comments-and-a/10.1214/ss/1009213726.full)); also Breiman, "Random Forests," *Machine Learning* 45, 2001.
- MNIST: LeCun, Bottou, Bengio, Haffner, 1998 — 60,000 training / 10,000 test images, 28×28 ([Keras dataset docs](https://keras.io/api/datasets/mnist/)).
- All dates, numbers, and paper claims above verified by live web search, 2026-08-25. The characterization of the 2026 tabular-deep-learning contest (TabPFN line "narrowing the gap") reflects the current benchmark literature and is labeled contested above rather than settled.

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
