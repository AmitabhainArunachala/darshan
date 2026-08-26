---
title: The History of AI
slug: history-of-ai
series: story-of-ai
tags: ai, history, ai-winter, dartmouth, perceptron, expert-systems, symbolic-ai, deep-learning
summary: Seventy years of artificial intelligence in one arc — Dartmouth 1956 to AlexNet 2012. Each era bet on a different theory of what intelligence is, and each winter was that theory failing in public. This room traces what was believed, what broke, and what survived.
status: draft
date: 2026-08-25
terms_defined: ai winter, dartmouth workshop, perceptron, symbolic ai, expert system
terms_linked: neural-networks, deep-learning, machine-learning, cybernetics, optimization, evolution-of-ai, future-of-ai, benchmarks, top-papers-ai, nvidia-and-the-chip, mechanistic-interpretability, leading-models
---

# The History of AI

You're in the story-of-ai series. This room covers the long arc — 1956 to 2012, Dartmouth to deep learning — the part of the story most current coverage skips or compresses into a sentence. The sibling room [evolution-of-ai](evolution-of-ai.html) picks up where this one ends, with the transformer era, and [future-of-ai](future-of-ai.html) looks forward. If you don't yet know what a neural network is, the [neural-networks](neural-networks.html) room is the better first stop; this room tells you where they came from and why they were left for dead — twice.

The one thing to hold onto: this is not a story of steady progress. It is a cycle, run at least twice, of a bold claim about what intelligence is, a boom funded on that claim, and a winter when the claim met reality. Knowing the shape of the cycle is the most useful thing this history can give you, because you are living inside another turn of it.

## 1. A ten-man summer that named a field

In August 1955, four researchers — John McCarthy, Marvin Minsky, Nathaniel Rochester, and Claude Shannon — sent a proposal to the Rockefeller Foundation. It asked for money for "a 2 month, 10 man study of artificial intelligence" to be held at Dartmouth College in the summer of 1956. That document is, as far as anyone has found, the first appearance of the phrase "artificial intelligence." McCarthy chose the name partly to stake out territory distinct from [cybernetics](cybernetics.html), the older field — Norbert Wiener's study of feedback and control in machines and animals — that had dominated thinking about machine minds until then.

The proposal's core sentence is worth reading in full, because the entire field descends from it:

> "The study is to proceed on the basis of the conjecture that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it."

Notice what kind of sentence that is. It's not a finding. It's a conjecture — a bet, stated plainly as one. The honesty of that framing got lost almost immediately and took decades to recover.

The Rockefeller Foundation granted about half of what was asked — roughly $7,500. The workshop ran in the summer of 1956, attendance drifted in and out, and no unified theory emerged. But one concrete thing showed up: Allen Newell, Herbert Simon, and Cliff Shaw brought the Logic Theorist, a program that proved theorems from Whitehead and Russell's *Principia Mathematica*. It eventually proved 38 of the first 52 theorems in chapter two, and its proof of theorem 2.85 was more elegant than the one Russell and Whitehead had produced by hand. A machine had done something that, a year earlier, everyone would have called thinking.

So the field was born with a name, a conjecture, and one genuinely impressive demo. That combination — a demo standing in for a theory — is a pattern you'll see again.

## 2. What the first era believed

From 1956 to roughly the early 1970s, the dominant belief was this: **intelligence is symbol manipulation.** Thinking is logical operations over symbolic representations — statements, rules, search trees — and since computers manipulate symbols natively, machine intelligence is mostly a matter of finding the right programs. This school is now called **symbolic AI** (or, affectionately, GOFAI — "good old-fashioned AI").

The confidence was extraordinary. Herbert Simon wrote in the mid-1960s that "machines will be capable, within twenty years, of doing any work a man can do" — a prediction from his book *The Shape of Automation for Men and Management* (1965), not a journalist's paraphrase. Simon was no crank; he later won the Nobel Prize in economics. The field's best minds genuinely believed general machine intelligence was one or two decades out. That was in 1965.

And there were results that made the confidence feel earned. Programs played checkers, solved word algebra problems, proved theorems. Joseph Weizenbaum's ELIZA (1966) held plausible-seeming therapy conversations with pattern-matched scripts — and Weizenbaum was disturbed to find users confiding in it. Terry Winograd's SHRDLU (around 1970) understood natural-language commands about a simulated world of blocks: "put the red pyramid on the green cube," and it did.

Meanwhile a rival bet was running in parallel. In 1958, Frank Rosenblatt at Cornell demonstrated the **perceptron** — a simple learning machine modeled loosely on a neuron, which adjusted its own connection weights from examples instead of being programmed with rules. It's the direct ancestor of every [neural network](neural-networks.html) running today. The press response set the template for AI hype: after a Navy demonstration in which the machine learned to distinguish punch cards marked on the left from cards marked on the right, the New York Times reported the Navy's expectation of machines that would "walk, talk, see, write, reproduce itself and be conscious of its existence." That was 1958. The hype-to-capability gap is not new; it is the field's oldest tradition.

So by the late 1960s two theories of intelligence were on the table. Symbolic AI: intelligence is logic, program it top-down. Connectionism: intelligence is learned, grow it bottom-up from examples. The first winter would bury them both — one by argument, one by audit.

## 3. The first winter: an argument and an audit

**The argument.** In 1969, Marvin Minsky and Seymour Papert published *Perceptrons*, a mathematical analysis of what Rosenblatt's machines could and couldn't do. The famous result: a single-layer perceptron cannot compute XOR — the trivially simple function "output 1 if exactly one input is 1." You will prove this yourself in section 7 of this room; it takes four lines. Multi-layer networks could compute XOR, but in 1969 nobody had a practical way to train them. The book is often blamed for killing neural network research for a decade. The fair version: the mathematics was correct, the pessimism about multi-layer training was a judgment call that proved wrong, and funders read the book as a verdict on the whole connectionist program. Money left. Rosenblatt died in a boating accident in 1971 and did not live to see his machines vindicated.

**The audit.** In 1973, the British Science Research Council asked Sir James Lighthill — a Cambridge fluid dynamicist with no stake in AI — to survey the field. His report, *Artificial Intelligence: A General Survey*, concluded: "In no part of the field have the discoveries made so far produced the major impact that was then promised." His central technical charge was **combinatorial explosion**: the toy demos worked because the toy worlds were small, and the search spaces of real problems grow exponentially, so the methods would not scale. The UK government cut AI funding across British universities, leaving research alive at only a few sites. In the US, DARPA — which had funded AI generously and loosely through the 1960s — tightened into mission-oriented funding and cut major programs, including speech-understanding research in the mid-1970s.

Why did the first era actually break? Three reasons that are worth stating precisely, because each one is a lesson that had to be relearned later:

1. **Combinatorial explosion.** Search-based reasoning that works on a 10-object toy world drowns in a 10,000-object real one. Lighthill was right about this.
2. **The commonsense knowledge problem.** SHRDLU could discuss blocks because its entire world was blocks. To discuss a kitchen, a program seemed to need thousands of facts humans never write down — that water is wet, that pushing a cup moves the cup. Nobody knew how to get that knowledge into a machine.
3. **Compute and data poverty, unrecognized.** In hindsight, the connectionist program wasn't wrong — it was seventy years early on hardware and forty years early on data. Almost nobody in 1973 identified this as the binding constraint. That misdiagnosis is arguably the single most consequential error in the field's history.

Note what the winter punished: not lying, exactly, but the gap between demo and theory. The demos were real. The claims about what the demos implied were not.

## 4. The boom that ran on rules: expert systems

The field came back in the 1980s with a humbler, more commercial bet: forget general intelligence — capture the knowledge of one human expert, in one narrow domain, as explicit IF-THEN rules. These programs were called **expert systems**, and the era's slogan, from Stanford's Edward Feigenbaum, was that knowledge — not reasoning power — is where intelligence lives.

For a while it genuinely worked. The emblem was XCON (also called R1), deployed at Digital Equipment Corporation from 1980 to configure VAX computer orders — a fiddly, error-prone task requiring real expertise. By 1986 XCON was reported to be saving DEC on the order of $25 million a year. That number did what numbers do: by the mid-1980s, a large share of major US corporations had expert-system projects, a dedicated industry sold specialized "Lisp machines" (workstations built to run AI software), and in 1982 Japan's Ministry of International Trade and Industry launched the **Fifth Generation Computer Systems project**, a national program to build massively parallel logic-programming machines and leapfrog the US computer industry. DARPA answered with its own Strategic Computing Initiative in 1983. AI was, for the first time, a real industry with real revenue.

Worth pausing on what this era believed, because it's the purest version of the symbolic bet: intelligence is knowledge, knowledge can be written down as rules, and therefore building intelligence is an engineering project of interviewing experts and encoding what they say. Every clause of that sentence turned out to be the failure point.

## 5. The second winter: brittleness meets a spreadsheet

The remarkable thing about the second winter is that it was called in advance, by name, from inside. At the 1984 meeting of the AAAI — the field's own professional association — Minsky and Roger Schank warned that enthusiasm had outrun reality and coined the term **AI winter** for what was coming, by analogy with nuclear winter: pessimism in the community, then in the press, then in funding, then the end of serious research. Three years later it arrived on schedule.

Two things broke, one economic and one technical.

The economic one was fast. Lisp machines were expensive specialized hardware. Around 1987, general-purpose workstations from Sun and desktop machines from Apple and IBM became powerful enough to run Lisp software at a fraction of the price. The specialized hardware market collapsed, taking flagship companies with it, and the collapse read publicly as "AI collapsed."

The technical one was slower and more damning: **brittleness**. Expert systems could not learn, so every update meant human rule-writers. Rule bases grew into thousands of interacting rules that became progressively harder to maintain — XCON itself grew notoriously expensive to keep current. At the edge of their domain, the systems didn't degrade gracefully; they failed absurdly, because a rule base has no notion of what it doesn't know. Companies discovered that maintenance costs ate the savings. The Fifth Generation project spent on the order of hundreds of millions of dollars over its decade and ended in the early 1990s without achieving its headline goals; DARPA gutted its AI push. Through the 1990s, "AI" became a word researchers avoided in grant applications — the same work got relabeled [machine learning](machine-learning.html), informatics, knowledge systems.

The deep lesson of the second winter, stated plainly: **knowledge you must hand-write does not scale, and a system that cannot learn cannot be maintained.** Whatever intelligence is, "a big pile of rules an expert dictated" is not it.

## 6. The quiet decades that actually won

Here is the part the boom-and-bust framing hides: the years everyone remembers as winter, roughly 1986 to 2012, are when the ingredients of everything current were actually built. Four threads matter.

**Backpropagation, 1986.** David Rumelhart, Geoffrey Hinton, and Ronald Williams published "Learning representations by back-propagating errors" in *Nature* (vol. 323, pp. 533–536) — a practical recipe for training *multi-layer* neural networks, precisely the thing Minsky and Papert had doubted was feasible. (The algorithm has earlier roots — Paul Werbos described it in his 1974 thesis — but the 1986 paper is what made the field notice.) The 1969 objection was now answered: multi-layer networks could be trained, by [gradient-based optimization](optimization.html), and their hidden layers learned useful internal representations nobody programmed. By 1989, Yann LeCun's group had backprop-trained networks reading handwritten ZIP code digits for the US Postal Service — real learning on a real task.

**The probabilistic and statistical turn.** Through the late 1980s and 1990s — Judea Pearl's work on Bayesian networks prominent among the causes — the field shifted from logic to probability, from hand-coded rules to parameters estimated from data. This rebrand-era machine learning delivered quiet, unglamorous wins: spam filters, credit scoring, speech recognition that slowly stopped being a joke. The lesson from the expert-systems collapse was being absorbed: don't ask the human to write the knowledge down; fit it from data.

**A famous win that proved the old thesis's limit.** In May 1997, IBM's Deep Blue beat world chess champion Garry Kasparov 3.5–2.5 — the first defeat of a reigning world champion by a machine under standard tournament conditions. Front-page news, and genuinely a milestone. But notice what Deep Blue was: brute-force search over hundreds of millions of positions per second plus hand-tuned evaluation functions. It was the *apotheosis* of the symbolic-search program, not a refutation of its limits — the approach conquered chess precisely because chess is a closed formal world, the kind of world Lighthill's critique had exempted. It learned nothing, and it generalized to nothing.

**The three missing ingredients arrive.** The connectionist program had been starved of scale. Between 2006 and 2012, scale showed up from three directions at once:

- **Compute:** graphics processors, built for video games, turned out to be near-ideal for the matrix arithmetic neural networks run on — the accident of history covered in [nvidia-and-the-chip](nvidia-and-the-chip.html).
- **Data:** in 2009, Fei-Fei Li's group at Princeton presented ImageNet at the CVPR conference — a dataset that grew to over 14 million hand-labeled images, plus an annual public competition. The role of shared public [benchmarks](benchmarks.html) in forcing honest comparison is its own story.
- **Algorithms and craft:** Hinton's group and others (deep belief networks, 2006, and after) accumulated the training tricks — better activations, regularization, initialization — that made deep networks trainable in practice.

None of this looked like a revolution while it was happening. It looked like an unfashionable subfield refusing to die.

## 7. Something you can check yourself: the problem that ended era one

The claim that shaped twenty years of history — "a perceptron cannot compute XOR" — takes four lines to verify. Worth doing once by hand, so it's yours.

A perceptron computes: output 1 if `w₁x₁ + w₂x₂ + b ≥ 0`, else 0. Training a perceptron just means finding numbers `w₁, w₂, b`. XOR demands:

```
input (0,0) → 0   so:  b < 0                 (i)
input (1,0) → 1   so:  w₁ + b ≥ 0            (ii)
input (0,1) → 1   so:  w₂ + b ≥ 0            (iii)
input (1,1) → 0   so:  w₁ + w₂ + b < 0       (iv)
```

Add (ii) and (iii): `w₁ + w₂ + 2b ≥ 0`, so `w₁ + w₂ + b ≥ −b`. By (i), `−b > 0`. So `w₁ + w₂ + b > 0` — contradicting (iv). No such numbers exist. Done. That contradiction, generalized across a book, was enough (with help from funding politics) to freeze a research program for a decade.

Now the resolution. Add one hidden layer — two intermediate units, then an output unit, each the same kind of threshold unit:

```
h₁ = step(x₁ + x₂ − 0.5)     "at least one input is on"  (OR)
h₂ = step(x₁ + x₂ − 1.5)     "both inputs are on"        (AND)
y  = step(h₁ − h₂ − 0.5)     "OR but not AND"            = XOR
```

Trace all four inputs — where `step(z)` is 1 if `z ≥ 0`, else 0:

| x₁ | x₂ | h₁ | h₂ | y |
|----|----|----|----|---|
| 0 | 0 | step(−0.5)=0 | step(−1.5)=0 | step(−0.5)=**0** |
| 1 | 0 | step(0.5)=1 | step(−0.5)=0 | step(0.5)=**1** |
| 0 | 1 | step(0.5)=1 | step(−0.5)=0 | step(0.5)=**1** |
| 1 | 1 | step(1.5)=1 | step(0.5)=1 | step(−0.5)=**0** |

XOR, exactly. The hidden units re-describe the input — as "OR-ness" and "AND-ness" — in a space where the problem becomes linearly separable. In 1969 the open question was how a machine could *find* such intermediate weights on its own; backpropagation, 1986, is the answer. And what intermediate re-descriptions today's billion-unit networks find on their own is precisely the question [mechanistic interpretability](mechanistic-interpretability.html) exists to answer.

## 8. 2012: the dam breaks

Every year, the ImageNet competition asked: given a photo, name the object, from 1,000 categories. The standard score was top-5 error — how often the correct label is missing from your five best guesses. In 2012 the best conventional computer-vision pipelines, built on a decade of hand-engineered features, scored around 26% top-5 error.

That year Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton entered a [deep](deep-learning.html) convolutional neural network — eight layers, about 60 million learned parameters, trained on two consumer GTX 580 graphics cards. It scored **15.3%**, against **26.2%** for the runner-up. In a benchmark where a single point of improvement was a good year, that is not an increment; that's a different regime. The paper, "ImageNet Classification with Deep Convolutional Neural Networks" — universally known as **AlexNet** — became one of the most cited works in the field's history (it appears, of course, in [top-papers-ai](top-papers-ai.html)).

Read the result against the whole arc and its meaning sharpens. The runner-up encoded decades of expert knowledge about what image features matter — the intellectual descendant, one more time, of "interview the expert and write the rules down." AlexNet encoded almost none; it *learned* its features from 1.2 million examples. Rosenblatt's 1958 bet — grow it from examples, don't program it — finally had the compute and the data it had always needed, and it won by eleven points, in public, on a benchmark nobody could argue with. Within about three years, essentially every serious computer-vision team had switched, and the same recipe began eating speech, translation, and eventually language itself — the story of the [transformer era](evolution-of-ai.html) and today's [leading models](leading-models.html).

## 9. The whole arc in one table

| Era | Years | Core belief | Emblematic system | Why it broke — or what it won |
|---|---|---|---|---|
| Founding + golden years | 1956–1973 | Intelligence is symbol manipulation; general AI is ~20 years away | Logic Theorist, SHRDLU | Combinatorial explosion; commonsense knowledge problem; Lighthill audit → first winter |
| First connectionism | 1958–1969 | Intelligence is learned by neuron-like units | Rosenblatt's perceptron | Single layers provably weak (XOR); no way yet to train deep ones; *Perceptrons* (1969) |
| Expert systems boom | 1980–1987 | Intelligence is knowledge, written as rules | XCON at DEC (~$25M/yr saved) | Brittleness; maintenance cost > value; Lisp-machine market collapse → second winter |
| Quiet statistical era | 1986–2012 | Intelligence is fit from data, not dictated | Backprop (1986), LeNet, Deep Blue (1997) | Didn't break — accumulated the pieces: learning algorithms, GPUs, big datasets |
| Deep learning | 2012– | Scale (data + compute + depth) beats hand engineering | AlexNet: 15.3% vs 26.2% | Still being tested — see [evolution-of-ai](evolution-of-ai.html) |

The pattern across the first four rows: each era's core belief was a *theory of what intelligence is*, each boom was that theory funded, and each winter was that theory failing its audit. The current era is unusual in that its core belief is almost anti-theoretical — not "intelligence is X" but "stop specifying X; scale learning and let X emerge." Whether that escapes the cycle or is simply this era's version of it is the live question, and this room won't pretend to settle it.

## What you can now see

You can now read any claim about AI's trajectory against seventy years of base rates. You know the boom-winter cycle has run at least twice, what specifically broke each time (scaling walls and hand-coded knowledge, respectively), and that the field's oldest tradition is the gap between a real demo and the theory it supposedly proves — from the 1958 "conscious of its existence" perceptron coverage onward. You know the current paradigm's lineage: Rosenblatt's bet, frozen by a correct proof about the wrong target, thawed by backprop, and finally fed by GPUs and ImageNet. You've verified the pivotal mathematical fact yourself. Where this era goes next is [evolution-of-ai](evolution-of-ai.html) and [future-of-ai](future-of-ai.html); how the papers stack up is [top-papers-ai](top-papers-ai.html); what's actually inside the learned models is [mechanistic-interpretability](mechanistic-interpretability.html).

## Open questions — the honest state of things

**Established (FACT):** The dates, systems, and outcomes above — the Dartmouth proposal and its conjecture, the perceptron and *Perceptrons*, the Lighthill report and UK cuts, XCON's deployment and reported savings, the 1987 hardware collapse, backprop's 1986 publication, Deep Blue's 3.5–2.5, AlexNet's 15.3% vs 26.2% — are documented history, verified against primary or near-primary sources listed below.

**Contested (HYPOTHESIS):** *Why* the winters happened is interpretation, not record. This room's framing — each winter as a failed theory of intelligence — is one reading; economic historians emphasize funding-agency politics and hardware commoditization, and both readings fit the evidence. Also contested: whether "scale is all you need" is a durable truth or this era's Simon-style overreach. Serious researchers hold both positions right now; the honest statement is that deep learning's eventual ceiling is unknown.

**Speculation worth holding (WILD):** That the winter cycle may be permanently over because AI now generates revenue rather than only promises — plausible, unproven, and structurally similar to things said in 1986 about expert systems. And the inverse wild thought: that a third winter, if it comes, would be the first to arrive *after* the technology genuinely worked, which no previous cycle can tell us much about.

One more thing the arc quietly teaches, and it belongs to this domain's own materials. Every era of this history was, underneath the funding and the acronyms, a public wager about what a mind is — logic, knowledge, learned representation — and reality graded each wager within a generation. The era that finally broke through is the one that stopped declaring what intelligence is and built machines that learn their own internal re-descriptions, which means the field now owns billions of hidden units doing what those two XOR units did — re-describing the world into spaces where problems become separable — without anyone able to say, yet, what re-descriptions are in there. Seventy years in, the Dartmouth conjecture stands unresolved and inverted: the machines work, and the question of what intelligence is has moved from the proposal's opening sentence to the inside of the machine. The field spent seventy years asking whether a machine can think. The working machines have handed back the harder question — what thinking is — and for the first time, there is an artifact you can open up and ask.

## Sources

- McCarthy, Minsky, Rochester, Shannon, ["A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence"](https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/1904) (Aug 31, 1955; reprinted in *AI Magazine*, 2006). Rockefeller grant ~$7,500 (about half the request) per the [Computer History Museum](https://computerhistory.org/events/1956-dartmouth-workshop-its-immediate/) and Dartmouth accounts.
- Logic Theorist: 38 of 52 theorems, theorem 2.85 — [Wikipedia: Logic Theorist](https://en.wikipedia.org/wiki/Logic_Theorist) and Gugerty, ["Newell and Simon's Logic Theorist"](https://journals.sagepub.com/doi/10.1177/154193120605000904) (2006).
- Simon's twenty-year prediction: *The Shape of Automation for Men and Management* (1965); provenance traced by [Quote Investigator](https://quoteinvestigator.com/2020/11/11/ai-can-do/).
- Perceptron press coverage: *New York Times*, July 1958, "New Navy Device Learns by Doing"; see [Cornell Chronicle](https://news.cornell.edu/stories/2019/09/professors-perceptron-paved-way-ai-60-years-too-soon).
- Minsky & Papert, *Perceptrons: An Introduction to Computational Geometry* (MIT Press, 1969). The XOR proof in section 7 is standard material you can re-derive from the book's linear-separability results.
- [Lighthill report](https://en.wikipedia.org/wiki/Lighthill_report), *Artificial Intelligence: A General Survey* (1973); the "in no part of the field…" quotation is from the report itself.
- XCON/R1 savings (~$25M/yr, 1986): Polit, ["R1 and Beyond: AI Technology Transfer at DEC"](https://aaai.org/ojs/index.php/aimagazine/article/view/460/396), *AI Magazine*. Figure is DEC-reported — treat as company-sourced.
- [Fifth Generation Computer Systems](https://en.wikipedia.org/wiki/Fifth_Generation_Computer_Systems) (MITI, 1982–1992); 1987 Lisp-machine market collapse and second winter: [AI winter — Wikipedia](https://en.wikipedia.org/wiki/AI_winter), which also documents the term's 1984 AAAI coinage by Minsky and Schank.
- Rumelhart, Hinton, Williams, ["Learning representations by back-propagating errors"](https://www.nature.com/articles/323533a0), *Nature* 323, 533–536 (1986).
- Deep Blue vs. Kasparov, May 1997, 3.5–2.5: [IBM](https://www.ibm.com/history/deep-blue) and [Wikipedia](https://en.wikipedia.org/wiki/Deep_Blue_versus_Garry_Kasparov).
- Deng, Dong, Socher, Li, Li, Fei-Fei, ["ImageNet: A Large-Scale Hierarchical Image Database"](https://www.image-net.org/static_files/papers/imagenet_cvpr09.pdf), CVPR 2009; 14M+ hand-annotated images per project documentation.
- Krizhevsky, Sutskever, Hinton, ["ImageNet Classification with Deep Convolutional Neural Networks"](https://courses.csail.mit.edu/6.803/pdf/2012%20hinton.pdf) (NeurIPS 2012): 15.3% vs 26.2% top-5 error, two GTX 580 GPUs — numbers from the paper itself.
- Unverified-by-search in this room and labeled accordingly: exact Fifth Generation spending (stated only as "hundreds of millions"), Werbos 1974 thesis attribution, and LeCun's 1989 ZIP-code work (both standard history; see LeCun et al., *Neural Computation* 1, 541–551, 1989 — cited from training knowledge, not re-verified live).

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
