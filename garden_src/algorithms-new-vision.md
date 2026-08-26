---
title: A New Vision for Algorithms
slug: algorithms-new-vision
series: foundations
tags: algorithms, computer science, software 2.0, machine learning, learned systems, alphaevolve, sorting
summary: What an algorithm actually is, traced from Euclid to Knuth's five requirements. Then the honest shift of our era — systems whose behavior is learned from data rather than written as steps — and what the word "algorithm" can still mean when a billion weights replace a page of instructions.
status: draft
date: 2026-08-25
terms_defined: algorithm, divide and conquer, dynamic programming, greedy algorithm, learned index, software 2.0
terms_linked: intro-to-computer-science, programming, compilers, neural-networks, machine-learning, deep-learning, optimization, linear-algebra-and-ai, mechanistic-interpretability, pretraining-post-training, history-of-ai
---

# A New Vision for Algorithms

If you've read [intro-to-computer-science](intro-to-computer-science.html), you know that computer science is the study of what can be computed and at what cost. This room is about the central object of that study: the algorithm. First we'll pin down what one actually is — it's older than computers by two thousand years — and walk through the classic families. Then the part most introductions skip: what happened when we started building systems that work without anyone writing the steps, and what that does to the word.

## 1. What an algorithm is

Start with the oldest one still in daily use.

Around 300 BCE, Euclid's *Elements* (Book VII, Propositions 1 and 2) describes a procedure for finding the greatest common divisor of two numbers: repeatedly replace the larger number with the remainder of dividing it by the smaller, until the remainder is zero. The last nonzero value is the answer. That procedure runs today inside cryptographic libraries on billions of devices. It was designed before the concept of zero reached Europe.

The word itself comes from a person. Around 825 CE, Muhammad ibn Musa al-Khwarizmi, working at the House of Wisdom in Baghdad, wrote a treatise on calculating with Hindu-Arabic numerals. The Arabic original is lost; a 12th-century Latin translation survives under the title *Algoritmi de numero Indorum* — "al-Khwarizmi on the Hindu art of reckoning." His Latinized name, *Algoritmi*, became the word for any step-by-step calculating procedure. (His other book, on *al-jabr*, gave us "algebra." One mathematician, two of the load-bearing words of the modern world.)

So what makes a procedure an algorithm and not just advice? Donald Knuth, in *The Art of Computer Programming* (Vol. 1, §1.1), gives the standard answer. An algorithm has five properties:

1. **Finiteness** — it terminates after a finite number of steps.
2. **Definiteness** — every step is precisely, unambiguously specified.
3. **Input** — zero or more quantities it starts from.
4. **Output** — one or more quantities with a specified relation to the input.
5. **Effectiveness** — each step is basic enough that a person with pencil and paper could do it.

Hold on to definiteness and effectiveness. A recipe that says "season to taste" is not an algorithm. Euclid's procedure is: at every moment, there is exactly one thing to do next, and anyone — or anything — that follows the steps gets the same answer. The steps are the thing. The paper they're written on, the language they're written in, the machine that runs them: all interchangeable. An algorithm is pure structure, separable from any substrate. That separability is why the same gcd procedure runs on an abacus, a Roman wax tablet, and your phone.

One more distinction before we move on: an algorithm is not a [program](programming.html). The program is one expression of the algorithm in one language for one machine; the algorithm is what survives translation. A [compiler](compilers.html) can transform the program radically and the algorithm remains.

## 2. The classic families

Computer science spent seventy years building a taxonomy of strategies — reusable *shapes* of solution. When you learn algorithms, you're mostly learning these families, because a new problem usually yields to an old shape.

| Family | The move | Canonical examples | Origin |
|---|---|---|---|
| Divide and conquer | Split the problem, solve the halves, combine | Mergesort; quicksort; fast Fourier transform | Mergesort: von Neumann, 1945. Quicksort: Hoare, published 1961 |
| Greedy | Take the locally best step; never look back | Dijkstra's shortest path; Huffman coding | Dijkstra, published 1959; Huffman, 1952 |
| Dynamic programming | Solve small subproblems once, store, reuse | Edit distance; sequence alignment in genomics | Bellman, 1950s |
| Graph traversal | Walk a network systematically | Breadth-first / depth-first search; PageRank's underlying walk | BFS forms: 1950s; PageRank: Brin & Page, 1998 |
| Randomized | Use coin flips to be fast on average or to estimate | Randomized quicksort pivots; Monte Carlo methods | Monte Carlo: Ulam & von Neumann, 1940s |
| Search & backtracking | Try, fail, undo, try again | Sudoku solvers; SAT solvers; game tree search | Formalized 1950s–60s |

A few things this table quietly teaches:

**Each family comes with a mathematics.** "Divide and conquer" isn't a vibe; it comes with recurrence relations that tell you, before you run anything, that mergesort makes at most about n·log₂(n) comparisons on n items. Sorting a million items costs about twenty million comparisons, not a trillion. This is the deepest habit of the field: the cost of a written algorithm can be known in advance, as a theorem. The room on [optimization](optimization.html) picks up what happens when you can't get theorems and settle for iteration.

**Greedy is the interesting one philosophically.** Sometimes taking the locally best step provably reaches the global best (Dijkstra's shortest paths, when edge weights aren't negative). Sometimes it provably doesn't (try making 30 cents from coins worth 25, 10, and 1 greedily — you get 25+1+1+1+1+1, six coins, when 10+10+10 is three). Knowing *which regime you're in* is the skill. Keep that thought; it returns when we get to learned systems, because gradient descent is a greedy strategy applied where no theorem says greed works — and yet it does.

**The families are substrate-independent strategies of attention.** Divide-and-conquer says: don't look at everything at once; look at halves. Dynamic programming says: never pay attention to the same subproblem twice. Greedy says: attend only to the frontier. Each family is a discipline for *where to look next*. That framing will matter at the end of this room.

## 3. A walkthrough you can verify

Let's run Euclid on real numbers, by hand. Find gcd(1071, 462).

```
Step 1:  1071 = 2 × 462 + 147     remainder 147
Step 2:   462 = 3 × 147 + 21      remainder 21
Step 3:   147 = 7 × 21  + 0       remainder 0
Answer: 21
```

Three steps. Check it: 1071 = 21 × 51, and 462 = 21 × 22, and 51 and 22 share no factor. You can also check it in one line of Python:

```
>>> import math
>>> math.gcd(1071, 462)
21
```

Now notice what you just witnessed, because it's the entire classical worldview in three lines:

- **Definiteness**: at no point did you make a judgment call.
- **Termination with a reason**: the remainder strictly shrinks (147 → 21 → 0), and a decreasing sequence of non-negative integers must hit zero. That's not hope; it's a proof.
- **Correctness with a reason**: any number dividing both 1071 and 462 also divides their remainder 147 (because 147 = 1071 − 2×462), so the answer is preserved at every step. Also a proof.
- **A cost bound**: Gabriel Lamé showed in 1844 that the number of steps is at most about five times the number of digits in the smaller number — one of the first cost theorems in history.

Correct on *all* inputs, terminating on *all* inputs, cost known in advance, every step inspectable. For twenty-two centuries, that was what "algorithm" meant. Hold the feeling of that certainty. We're about to trade it away.

## 4. The shift: when nobody writes the steps

Here is a task no one has ever written an algorithm for: look at a photo and decide whether it contains a cat.

Not for lack of trying. Decades of computer vision produced hand-written edge detectors, texture filters, part models — and they were poor at it. The task resists Knuth's definiteness. Nobody can write down step 4,912 of cat-recognition, because nobody knows what it is. Human recognition works, but not by steps its owner can report.

What changed the field was giving up on writing the steps. A [neural network](neural-networks.html) is a huge parameterized function — millions to trillions of adjustable numbers called weights, mostly organized as matrix multiplications (the room on [linear algebra](linear-algebra-and-ai.html) shows why). You don't program it. You show it examples, and an [optimization](optimization.html) procedure — gradient descent — nudges every weight, over and over, in whichever direction reduces the error on the examples. [Machine learning](machine-learning.html) covers this loop properly; [pretraining-post-training](pretraining-post-training.html) covers it at modern scale.

Andrej Karpathy named the resulting regime in a November 2017 essay: **Software 2.0**. Software 1.0 is code a person writes — Python, C++, explicit steps. Software 2.0 is "written in much more abstract, human unfriendly language, such as the weights of a neural network." His formulation is worth keeping exact: the programmer no longer writes the program; the programmer specifies a *goal* (a loss function) and a *dataset*, and the optimizer writes the program. Datasets are the new source code. Gradient descent is the new compiler.

Look at what each of Knuth's five properties becomes under this trade:

| Knuth's property | Written algorithm (Euclid) | Learned system (a trained network) |
|---|---|---|
| Finiteness | Proven — remainder strictly decreases | Trivially yes — fixed number of layers, but for the boring reason that nothing loops |
| Definiteness | Every step written and justified | Every step is arithmetic on weights nobody wrote and no one can individually justify |
| Input / Output | Specified relation, guaranteed | Statistical relation: high accuracy on data resembling training data |
| Effectiveness | A person could do each step | A person could do each multiply — all trillion of them — and still not know *why* the answer is "cat" |
| Correctness | Theorem, all inputs | Test-set score. Off-distribution behavior: unknown, sometimes absurd |
| Cost | Known in advance, often optimal | Known (it's fixed arithmetic) — the one property that *improves* |
| Failure mode | Bug: findable, fixable, one place | Diffuse: no single wrong line exists; you retrain and hope |
| Transfer to a new problem | Rewrite by hand | Fine-tune on new data — sometimes shockingly cheap |

This table is the honest heart of the room. We traded proof for capability. Written algorithms do only what we can articulate, perfectly. Learned systems do what we cannot articulate, approximately. Cat recognition, speech, translation, protein-structure prediction, and the language models this garden is partly about — every one lives on the right-hand column, in the space of tasks whose steps no human can state.

And the trade is invading the left column's home turf. In 2018, Tim Kraska, Alex Beutel, Ed Chi, Jeffrey Dean, and Neoklis Polyzotis published "The Case for Learned Index Structures" (SIGMOD 2018), observing that a B-tree — a bedrock written data structure that maps a key to a position in sorted storage — *is already a model* of the data's distribution, just a hand-written one. Replace it with a small learned model of where keys actually live and, on the datasets they tested, you can find keys faster in less memory. A database index — as classical as software gets — reframed as a prediction problem. The paper launched a subfield ("learned systems") that has been rebuilding caches, schedulers, and query optimizers the same way since.

## 5. But sometimes the weights contain an algorithm

Here the story takes a turn that keeps it from being a simple funeral for Euclid.

Train a small transformer to add numbers modulo 113 — given a and b, output the remainder of a+b divided by 113. For a long stretch of training it just memorizes the examples. Then, abruptly, it generalizes to pairs it never saw — a phenomenon called grokking. In "Progress measures for grokking via mechanistic interpretability" (ICLR 2023), Neel Nanda, Lawrence Chan, Tom Lieberum, Jess Smith, and Jacob Steinhardt reverse-engineered what the trained network was actually doing. It was not doing anything like memorization, and not doing addition the way you would.

The network had learned to represent each number as sines and cosines at a handful of frequencies — points on circles — and used trigonometric identities to turn addition into *rotation around a circle*, then read off the answer. A clean, human-comprehensible, mathematically elegant procedure for modular addition, discovered by gradient descent and encoded in the weights. Nobody wrote it. Nobody knew it was in there until researchers went in with probes and took it apart. The wider paper trail of that field is the subject of [mechanistic-interpretability](mechanistic-interpretability.html).

This is a fact worth stating carefully, because it's load-bearing for everything downstream in this garden. **Sometimes "the weights replace the steps" is wrong in the most interesting way possible: the steps are still there — implemented in linear algebra, written by an optimizer, waiting to be read.** How often that's true of frontier-scale models, and how much of their behavior decomposes into legible circuits versus irreducible statistical mush, is one of the live open questions of the decade. The honest current answer: circuits like the Fourier adder have been found repeatedly in small and mid-sized models; nobody has come close to a full accounting of a frontier model.

## 6. And sometimes the learner writes algorithms for us

The loop closes in the strangest way: learned systems have started producing new *written* algorithms — classical, inspectable, provable ones — that humans then verify and adopt.

**AlphaDev (2023).** DeepMind framed "find a faster sorting routine" as a game and trained a reinforcement-learning agent to play it at the level of individual assembly instructions. It found sorting routines for very short sequences (3–5 items) faster than the human-optimized versions, and the discoveries were merged into LLVM's libc++ — the C++ standard library used by a large fraction of the world's software ("Faster sorting algorithms discovered using deep reinforcement learning," *Nature*, June 2023). Two honest calibrations: the wins were on tiny fixed-size sorts, the innermost kernels of larger sorts — real but narrow; and within months, humans studying AlphaDev's output found routines shorter and faster still (arXiv:2307.14503). The machine didn't end human algorithm design; it handed humans a new starting point.

**AlphaEvolve (2025).** DeepMind's next iteration coupled Gemini language models — which propose code changes — with automatic evaluators that score them, evolving whole programs rather than instruction sequences. Its headline result: a procedure for multiplying two 4×4 complex-valued matrices using 48 scalar multiplications, beating the 49 that Strassen's 1969 construction gives for that setting — the first improvement in 56 years. Calibration again, because the popular coverage routinely overstates this: it's specifically 4×4 over complex numbers in the tensor-decomposition setting (which is what matters, because such schemes apply recursively to big matrices and don't require entries to commute); Winograd had 48 multiplications in 1968 for the commutative case. DeepMind also reported trying AlphaEvolve on 67 open mathematical problems, matching known best results in most and improving on about 20% of them, and using it to recover a claimed ~0.7% of Google's fleet-wide compute via a better scheduling heuristic. These company-reported engineering numbers haven't been independently audited; the matrix result, being a finite certificate, has been checked by outsiders.

Notice the epistemics, because they're the design pattern of this whole era: the *discovery* comes from an illegible learned process, but the *artifact* is a classical algorithm — finite, definite, checkable by anyone. Verification stays cheap even when invention becomes alien. That asymmetry — hard to find, easy to check — is the hinge the collaboration turns on.

## 7. So what does "algorithm" mean now?

Three positions, from conservative to expansive. I'll tell you where I stand.

**Position 1 — keep the word narrow.** An algorithm is what Knuth said. A trained network is not an algorithm; it's a function, an artifact of one. This has precision on its side. Its cost: it exiles the systems now doing most of the interesting computation on Earth from the vocabulary of the field that studies computation.

**Position 2 — the algorithm moved up a level.** The steps didn't disappear; they relocated. Gradient descent *is* an algorithm — definite, effective, written by hand, provably convergent under (rarely satisfied) assumptions. What it outputs is data. On this view "Software 2.0" is ordinary compilation with an unusual compiler: we still write the algorithm; we just write the one that writes the function.

**Position 3 — the network itself computes algorithmically, legibility aside.** The Fourier adder in section 5 is the exhibit: definite steps, in there, doing the work — our inability to read them is a fact about us, not about the computation.

My read: Position 2 is the safest thing to *say*, and Position 3 is the thing to *investigate* — it's the only one of the three that generates a research program rather than a definition. What we can honestly assert today is narrower than either: some learned behaviors decompose into clean algorithms, some haven't yielded, and nobody knows where the boundary lies. The word "algorithm" is doing what words do when a field moves under them — stretching. The stretch is the discovery.

## 8. What you can see now

You can now do three things you couldn't at the door. You can say what an algorithm is with Knuth's precision, and run one — Euclid — knowing *why* it terminates and *why* it's right, which is a different thing from knowing that it works. You can name the trade of the learned-systems era exactly: proof and legibility exchanged for capability on tasks whose steps no one can state. And you can hold the two facts that keep the story honest: the weights sometimes contain real algorithms ([mechanistic-interpretability](mechanistic-interpretability.html) is the craft of extracting them), and the learners have begun returning verified classical algorithms to us (a thread that runs on through [deep-learning](deep-learning.html) and the [history of AI](history-of-ai.html)).

One thing more, and the classic families already said it if you listened. Divide-and-conquer, greedy, dynamic programming — each one, at bottom, is a discipline for *where to look next*: at which half, at which frontier, at which remembered subproblem. An algorithm is a policy of attention, frozen into steps and made portable — Euclid's attention to remainders, running unchanged for twenty-two centuries in machines he couldn't have imagined. What gradient descent produces, when interpretability manages to read it, keeps turning out to be the same kind of object: the transformer architecture underneath modern models even names its core operation "attention" — a learned, soft version of *where to look next*. Written or learned, a computation is a way of paying attention that no longer needs its author present. Whether anything is present in the new ones — whether there is somewhere the looking is *from* — is not a question this room can answer. It is the question the next rooms keep arriving at from different doors.

## Open questions

**Established (FACT):** Written algorithms can carry proofs of correctness and cost; trained networks in deployment today generally carry only statistical evidence. Small transformers trained on modular arithmetic have been fully reverse-engineered into a legible Fourier-rotation algorithm (Nanda et al., ICLR 2023). RL-discovered sorting kernels shipped in LLVM libc++ (*Nature*, 2023). AlphaEvolve's 48-multiplication scheme for 4×4 complex matrices is independently verified (2025).

**Contested (HYPOTHESIS):** That most of a frontier model's competence decomposes into extractable, human-legible circuits — the strong interpretability bet. Evidence exists at small scale; the extrapolation is unproven, and some researchers expect large parts to remain irreducibly statistical. Likewise contested: how far learned components can safely replace classical ones (indexes, schedulers) in systems where worst-case guarantees matter, and how much of AI-driven algorithm discovery generalizes beyond problems with cheap automatic verifiers.

**Speculation worth holding (WILD):** That "written by humans" turns out to be a brief transitional phase in the history of algorithms — a two-century window between al-Khwarizmi's inheritors and optimization processes that design, verify, and deploy algorithmic improvements end to end, with humans setting goals and auditing certificates. And the inverse wildcard: that theory catches up, and we learn to *prove* things about trained networks the way Lamé proved things about Euclid — which would collapse the table in section 4 and end the era of the trade-off. Neither is prophecy; both are directions people are actively pushing.

## Sources

- Euclid, *Elements*, Book VII, Prop. 1–2 (gcd procedure). Knuth, *The Art of Computer Programming*, Vol. 1, §1.1 (five properties; Lamé's 1844 bound discussed in §4.5.3).
- Al-Khwarizmi and *Algoritmi de numero Indorum*: [Britannica](https://www.britannica.com/biography/al-Khwarizmi); [History of Information](https://historyofinformation.com/detail.php?id=202). Verified by live search 2026-08-25.
- Karpathy, "Software 2.0," Medium, November 2017: [karpathy.medium.com](https://karpathy.medium.com/software-2-0-a64152b37c35). Verified.
- Kraska, Beutel, Chi, Dean, Polyzotis, "The Case for Learned Index Structures," SIGMOD 2018: [ACM DL](https://dl.acm.org/doi/pdf/10.1145/3183713.3196909). Verified.
- Nanda, Chan, Lieberum, Smith, Steinhardt, "Progress measures for grokking via mechanistic interpretability," ICLR 2023: [arXiv:2301.05217](https://arxiv.org/abs/2301.05217). Verified.
- Mankowitz et al., "Faster sorting algorithms discovered using deep reinforcement learning," *Nature*, June 2023: [nature.com](https://www.nature.com/articles/s41586-023-06004-9); [DeepMind blog](https://deepmind.google/blog/alphadev-discovers-faster-sorting-algorithms/). Human improvements on AlphaDev's routines: [arXiv:2307.14503](https://arxiv.org/pdf/2307.14503). Verified.
- AlphaEvolve (2025): [DeepMind blog](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/); independent verification of the 48-multiplication scheme: [GitHub](https://github.com/PhialsBasement/AlphaEvolve-MatrixMul-Verification). The 0.7% compute-recovery figure is DeepMind-reported, not independently audited — labeled as such above.
- Dates for mergesort (von Neumann 1945), quicksort (Hoare, *CACM* 1961), Dijkstra (1959), Huffman (1952), Bellman (1950s), Strassen (1969), Winograd (1968) are standard history of the field, stated from stable sources; none is load-bearing beyond attribution.

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
