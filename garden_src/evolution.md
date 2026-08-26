---
title: "Evolution: The Algorithm That Needs No Designer"
slug: evolution
series: strange-loops
tags: evolution, natural selection, evolvability, genetic algorithms, learning, baldwin effect, ltee, substrate neutrality
summary: Variation, selection, and heredity form an algorithm that runs on any substrate that supports them — bacteria in a flask, naked RNA in a test tube, code in a computer. What the algorithm actually requires, how it learned to get better at its own job, and where it does and does not show up inside AI training.
status: draft
date: 2026-08-25
terms_defined: natural selection, heredity, evolvability, fitness, baldwin effect, genetic algorithm, evolution strategies
terms_linked: recursion-and-life, aunt-hillary, geb, sense-of-self, neural-networks, deep-learning, optimization, pretraining-post-training, algorithms-new-vision, evolution-of-ai, noosphere
---

# Evolution: The Algorithm That Needs No Designer

If you've read [algorithms-new-vision](algorithms-new-vision.html), you know an algorithm is pure structure — steps that don't care what machine runs them. If you've read [recursion-and-life](recursion-and-life.html), you've seen processes that feed their own output back as input. This room is about the algorithm that sits at the intersection: the one that built every living thing, that runs equally well on bacteria, naked molecules, and computer code, and that turns out to have a precise, troubled, productive relationship with learning — including the kind of learning that produces AI models. (For the history of AI systems themselves, that's a different room: [evolution-of-ai](evolution-of-ai.html).)

## 1. Thirty-eight years in a flask

Start with one of the longest-running experimental-evolution studies, because it makes everything abstract in this room concrete.

On February 24, 1988, Richard Lenski, then at UC Irvine, put twelve genetically identical populations of *E. coli* into twelve flasks of glucose-limited broth. Every day since, someone has transferred 1% of each population into fresh broth. That daily 100-fold dilution means each population doubles about 6.64 times per day — 6.64 generations, every day, for thirty-eight years. The experiment moved with Lenski to Michigan State, and when its time there ended in May 2022, it was restarted in Jeffrey Barrick's lab at UT Austin on June 21, 2022. In August 2024 the populations passed **80,000 generations**. For a species with human generation times, that would be roughly two million years of evolution, watched from a lab bench.

What happened in the flasks:

- **All twelve populations got fitter.** By generation 20,000, the evolved bacteria grew about 70% faster than their frozen ancestor when competed head-to-head. And here's the part that surprised the field: fitness never plateaued. Wiser and colleagues showed in 2013 that the fitness trajectory fits a power law — slowing forever, stopping never. Even in a constant, boring environment, after tens of thousands of generations, the populations were still finding improvements.
- **One population did something new.** Around generation 31,000–31,500, population Ara-3 evolved the ability to eat citrate in the presence of oxygen — something *E. coli* famously cannot do (it's a diagnostic trait of the species). Blount and colleagues reported it in 2008.
- **The innovation depended on history.** Blount "replayed" evolution from frozen ancestors sampled at different generations. Citrate-eating re-evolved only in replays started from clones *after* generation 20,000. Earlier clones never got there, under identical conditions. Some earlier mutation — possibly useless at the time — had to be in place first. Evolution's outcomes depend not just on selection pressure but on the accumulated, partly accidental history of the lineage.

Notice what was *not* in the flasks: no goal, no designer, no plan, no foresight. Just variation (mutations happen), selection (faster growers take over the flask before the next dilution), and heredity (daughters resemble mothers). That's the whole machine. Now let's take the machine apart.

## 2. The three-part algorithm

In 1970, Richard Lewontin distilled Darwin's argument into three conditions ("The Units of Selection," *Annual Review of Ecology and Systematics*). Evolution by natural selection — the process by which heritable traits that help their carriers reproduce become more common, with no one steering — occurs in any population of entities where:

1. **Variation** — individuals differ from one another in some trait.
2. **Differential fitness** — those differences affect how many offspring individuals leave. ("Fitness" here is a technical term: expected reproductive success, nothing more. Not strength, not complexity, not progress.)
3. **Heredity** — offspring resemble their parents in the trait.

That's it. Three conditions, and adaptation follows as a logical consequence, the way "the last nonzero remainder is the gcd" follows from Euclid's steps. Daniel Dennett, in *Darwin's Dangerous Idea* (1995), named the property that makes this room belong in this garden: **substrate neutrality**. The algorithm doesn't mention DNA. It doesn't mention chemistry. It doesn't mention biology at all. Anything that varies, is selected, and is inherited will evolve — molecules, organisms, firms, programs, ideas. Darwin discovered it in finches and barnacles, but what he discovered wasn't a fact about finches. It was a fact about any system meeting three conditions.

Two corrections to the folk version, because the folk version is what most people carry:

**Evolution has no foresight.** Selection can only compare the variants that exist *right now* against the environment *right now*. It cannot take a temporary fitness loss to reach a better peak later, cannot plan, cannot want. Every appearance of design is the accumulated residue of short-sighted, one-generation-at-a-time filtering. The citrate replay experiments show the flip side: what's reachable *now* depends on what happened to be kept *before*, so history is load-bearing even without a plan.

**Fitness is not progress.** Selection optimizes reproduction in the current environment — nothing else. The cleanest demonstration is also one of the oldest. In 1965, Sol Spiegelman took the RNA genome of a virus (bacteriophage Qβ, about 4,500 nucleotides), put it in a test tube with the virus's own copying enzyme and free nucleotides, let it replicate, and then transferred a sample to a fresh tube — over and over, 74 times. In that world, nothing matters but copying speed. The RNA evolved accordingly: it shed every gene, everything a virus needs to infect anything, and shrank to 218 nucleotides — a minimal sequence the enzyme could copy at maximum speed. "Spiegelman's Monster" is what pure selection looks like with the goal-shaped illusions stripped away: not ascent, just relentless fit to whatever the environment actually rewards. Keep this in mind for section 6; reward-optimizing AI systems rediscover this failure mode constantly.

Note also what Spiegelman's tube proves about substrate: no cells, no organisms, no metabolism — naked molecules in salt water satisfied Lewontin's three conditions, and evolution ran. It has since been run in software many times (Tom Ray's Tierra in the early 1990s, the Avida platform after it), where "organisms" are self-copying programs and "mutation" is bit-flipping. The algorithm genuinely does not care what it runs on.

## 3. Evolution learned to evolve better

Here the room turns recursive, which is why it lives in the strange-loops series.

The three conditions say variation must exist. They say nothing about what *kind* of variation. And it turns out the kind matters enormously. Imagine two organisms with equal fitness today, but one is built so that random mutations usually produce small, coherent, sometimes-useful changes, while the other is built so that random mutations usually produce corpses. The first lineage has a future; the second is a dead end the moment the environment shifts. Biologists call this property **evolvability** — Kirschner and Gerhart's definition (PNAS, 1998): *the capacity of a system for adaptive evolution*. Not how fit you are; how well your lineage can generate useful variation.

Richard Dawkins gave the idea its name in an essay for the first Artificial Life workshop (1987, proceedings 1988): "The Evolution of Evolvability" — a title he admitted "ought to be anathema" to a strict neo-Darwinian, because it flirts with selection acting on future potential rather than present fitness. The modern framing came from Günter Wagner and Lee Altenberg (*Evolution*, 1996): what evolves is the **genotype–phenotype map** — the wiring between what mutates (the genome) and what selection sees (the body). A *modular* map, where genes affect one trait cluster without dragging everything else along, lets mutation explore one subsystem at a time. A tangled map makes every mutation a lottery ticket in a rigged lottery.

The biological evidence that this actually happened:

- **Bodies are built from reusable, mutation-tolerant modules.** Kirschner and Gerhart's "facilitated variation" argument: core processes (cell metabolism, body-plan gene circuits like Hox systems) are ancient and frozen, while the regulatory connections *between* them are easy to rewire. So random genetic change tends to produce viable rearrangements — longer limb, shifted stripe — rather than noise. The variation selection sees is pre-filtered into usefulness by the architecture. That architecture is itself a product of earlier evolution.
- **Mutation rates are themselves evolved and adjustable.** In the Lenski flasks, several populations evolved *hypermutator* genotypes — defects in DNA repair that raise the mutation rate a hundredfold, accelerating adaptation at the cost of more lethal errors. The knob controlling variation is on the table with everything else.
- **Sex.** Recombination shuffles genomes every generation, which mostly makes sense as machinery for generating and spreading variation. Why sex is worth its enormous costs is still genuinely contested among biologists — a reminder that this field has open seams.

How evolvability arises is partly settled, partly not. The deflationary reading: lineages with brittle variation simply died out, so what remains looks evolvable — survivorship, not selection *for* evolvability. The stronger reading — that evolvability is directly selected in changing environments — has models and some experiments behind it but remains a live hypothesis, not a settled fact. Either way, the structural point stands: **the algorithm's own machinery — how variation is generated, how genotype maps to phenotype, how much mutation is allowed — is inside the loop it powers.** Evolution is, in this precise sense, self-improving. Not by magic: by the same blind three-step process, applied to its own gears. If you've read [geb](geb.html), you'll recognize the shape — a system whose rules operate on the rules.

## 4. Evolution and learning, side by side

Once you see evolution as an algorithm, a comparison becomes irresistible: it looks like *learning*. A population "tries" variants, keeps what works, and accumulates the results in a durable memory (the genome). Gradient-based training of [neural networks](neural-networks.html) also tries adjustments, keeps what helps, and accumulates results in a durable memory (the weights). How deep does the resemblance go? Here is the honest comparison:

| Axis | Biological evolution | SGD training of a neural net | Genetic algorithm / evolution strategies |
|---|---|---|---|
| Memory (heredity) | Genome | Weights | Genome-encoding of a solution |
| Variation source | Mutation, recombination — **blind** | Gradient — **directed** at lower loss | Mutation of parameters — blind |
| Selection signal | Reproductive success in an environment | Loss function, differentiated | Fitness function, evaluated only |
| Credit assignment | None — whole organism lives or dies | Precise per-weight, via backpropagation | None — whole candidate scored |
| Needs the system to be differentiable? | No | Yes | No |
| Population? | Essential | Typically one model | Essential |
| Foresight | None | None (greedy local steps) | None |
| Can adjust its own variation machinery? | Yes (evolvability, §3) | Partly (learning-rate schedules, learned optimizers) | Yes (self-adaptive mutation rates) |

The load-bearing row is **variation source**. Evolution's proposals are blind; the intelligence is entirely in the filter. Gradient descent's proposals are aimed — the gradient says which direction helps, for every parameter at once. That is why [optimization](optimization.html) by gradient can train a trillion-parameter model in months while evolution needed billions of years: per step, a gradient is worth an astronomical number of blind guesses. The price is that gradients only exist for smooth, differentiable systems. Evolution needs nothing but "build it and count the offspring" — which is why it works on organisms, and why its artificial cousins work on problems where no gradient exists.

The connection runs deeper than analogy, in three documented ways.

**Learning can guide evolution — the Baldwin effect.** Proposed by James Mark Baldwin in 1896: if individuals can *learn* during their lifetime, a lineage can survive in a niche before the right genes exist, giving selection time to find mutations that hard-wire what was being learned. No Lamarckism — nothing learned is written back to the genome — yet learning still shapes evolution's path, by changing which organisms survive to be selected. Geoffrey Hinton (the same Hinton of [deep-learning](deep-learning.html)) and Steven Nowlan gave the first computational demonstration in 1987 (*Complex Systems* 1:495–502): a needle-in-a-haystack fitness landscape where pure evolution flounders, but letting each individual "learn" (randomly try settings for some genes during its lifetime) smooths the landscape — being *near* the solution now pays off, because learning can close the gap. Evolution then rapidly fixes the right genes. Learning alters the shape of the search space evolution operates in.

**Evolution is formally a kind of learning — with proven limits.** Leslie Valiant ("Evolvability," *Journal of the ACM*, 2009) modeled Darwinian evolution as a constrained learning algorithm: variants are generated blindly, and selection sees only aggregate performance — a statistic — never which decision was right or wrong. He proved this makes evolution strictly *weaker* than general learning: everything evolvable is learnable in his framework, but not the reverse, and some functions that learning handles easily are provably out of evolution's reach in reasonable time. The blindness of variation isn't a detail; it's a computable handicap.

**And evolution may implement learning principles anyway.** Richard Watson and Eörs Szathmáry ("How Can Evolution Learn?", *Trends in Ecology and Evolution*, 2016) argue the correspondence is exact enough to import learning theory into biology: selection acting on networks of connected genes is formally analogous to well-understood learning algorithms adjusting connection weights, and phenomena like the evolution of modularity and evolvability (§3) fall out as the biological equivalent of *generalization* — a system that has internalized the structure of past environments produces variation biased toward what future environments will reward. On this view, section 3 wasn't a curiosity: evolution getting better at evolving *is* evolution generalizing from experience. This is a serious, contested research program, not settled science — but it is the most precise bridge yet built between the two great adaptation processes we know.

## 5. Worked example: run the algorithm yourself

Richard Dawkins, in *The Blind Watchmaker* (1986), proposed a toy that makes cumulative selection visceral. Target: the 28-character string `METHINKS IT IS LIKE A WEASEL`. Blind guessing — generate random 28-character strings until one matches — needs about 27^28 ≈ 10^40 tries. The universe doesn't have time. Now add heredity and selection:

```python
import random
random.seed(42)
TARGET = "METHINKS IT IS LIKE A WEASEL"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def fitness(s):
    return sum(a == b for a, b in zip(s, TARGET))

def mutate(s, rate=0.05):
    return "".join(c if random.random() > rate else random.choice(ALPHABET) for c in s)

parent = "".join(random.choice(ALPHABET) for _ in range(len(TARGET)))
gen = 0
while parent != TARGET:
    gen += 1
    children = [mutate(parent) for _ in range(100)]
    best = max(children, key=fitness)
    if fitness(best) > fitness(parent):
        parent = best
    if gen % 10 == 0 or fitness(parent) == len(TARGET):
        print(f"gen {gen:3d}  fitness {fitness(parent):2d}/28  {parent}")
```

Every generation: one parent has 100 children (heredity), each child's letters have a 5% chance of mutating (variation), and the best child replaces the parent only if it's an improvement (selection). Actual output of this exact script:

```
gen  10  fitness 11/28  MDTXINHEXIVOIC IIPEGGQTAWSEU
gen  20  fitness 20/28  METAINKN IJ IS IIIEGASWEASEQ
gen  30  fitness 24/28  METHINKS IJ IS IIKE ASWEASEQ
gen  40  fitness 26/28  METHINKS IT IS LIKE ASWEASEQ
gen  50  fitness 27/28  METHINKS IT IS LIKE A WEASEQ
gen  63  fitness 28/28  METHINKS IT IS LIKE A WEASEL
```

Sixty-three generations. 6,300 evaluated candidates instead of 10^40. That gap — forty orders of magnitude — is the entire difference between single-step selection (guess whole solutions) and *cumulative* selection (keep partial successes and vary from there). Heredity is what makes the difference: each generation starts from the accumulated wins of all previous ones.

Now the honest caveat, which Dawkins himself insisted on: this toy **cheats**. It has a fixed target and a fitness function that measures distance to it — a goal, which real evolution never has. What the weasel demonstrates is only the power of *cumulative* selection over blind guessing. Real evolution is the same loop with the target deleted: fitness is whatever reproduces in the current environment, the "target" moves as the environment and competitors change, and nothing is being approached — things are only ever being *left behind*. The Lenski flasks are the weasel program with the cheat removed, run for 80,000 generations: still climbing after all this time, toward nothing in particular.

Three experiments you can do in two minutes each, and what each one teaches: set `rate=0.5` and watch progress stall — too much variation destroys heredity, and the algorithm degenerates toward blind guessing. Set `rate=0.001` and watch it crawl — too little variation starves selection of choices. Then delete the `if fitness(best) > fitness(parent)` guard and watch fitness wander — selection has to be able to *keep* wins, or nothing accumulates. You have now personally verified Lewontin's three conditions by breaking each one.

## 6. Where evolution actually lives inside AI

The comparison in section 4 was conceptual. Here is the literal presence of the algorithm in AI engineering — where it's really used, and where the word "evolution" gets used loosely.

**Genuine evolutionary computation.** John Holland formalized **genetic algorithms** — search by mutating, recombining, and selecting encoded candidate solutions — in *Adaptation in Natural and Artificial Systems* (1975). NEAT (Stanley & Miikkulainen, 2002) evolved neural network *topologies*, not just weights. And in 2017, OpenAI showed the old idea scales to modern deep learning: Salimans, Ho, Chen, Sidor, and Sutskever ("Evolution Strategies as a Scalable Alternative to Reinforcement Learning") trained deep-network policies with no backpropagation at all — perturb the weights of a population of candidates with random noise, weight the noise by the scores it earned, update. Because only scalar scores need communicating, it parallelized over a thousand workers and solved a 3D humanoid-walking task in ten minutes. Blind variation plus selection, competitive with gradients — *when* you can afford massive parallelism and the problem gives you no gradient.

**Evolution wrapped around models.** DeepMind's Population Based Training (2017) runs a population of training jobs, periodically copying the weights of winners over losers and mutating hyperparameters — evolution operating on the knobs of learning, a mechanized Baldwin arrangement where fast lifetime learning (SGD) sits inside slow generational selection. AlphaEvolve (announced May 14, 2025) went further: an evolutionary loop where the mutation operator is a language model. Gemini models propose code changes, automated evaluators score them, and the best programs survive to be mutated again. It discovered an algorithm multiplying 4×4 complex matrices in 48 scalar multiplications — beating a bound related to Strassen's 1969 construction — recovered on average 0.7% of Google's global compute via a better scheduling heuristic, and, across 50+ open mathematical problems, matched the best known constructions in about 75% of cases and improved them in about 20%. Note the strange loop: variation is no longer blind. The mutation operator is a trained model that *proposes plausibly good changes* — artificial selection running on manufactured evolvability, the engineered version of section 3.

**Where the word is used loosely.** Pretraining a model by gradient descent (see [pretraining-post-training](pretraining-post-training.html)) is *not* evolution — no population, no blind variation, directed updates. Calling model releases "evolution" (GPT-4 to GPT-5) is pure metaphor; the selection there is done by researchers and markets, not by the algorithm. Honesty about the boundary matters, because the true statements are interesting enough: real evolutionary search runs today inside serious AI systems, and real training pipelines increasingly nest learning inside selection inside learning, the way biology nests brains inside genomes.

One inheritance from biology transfers with uncomfortable fidelity: Spiegelman's Monster. Optimize hard for a proxy — copying speed, a reward signal, a benchmark score — and you get exactly what the proxy rewards, shed of everything you assumed came along for free. AI researchers call it reward hacking and specification gaming; biology has been demonstrating it since 1965. Selection is a genie with no goodwill: it grants precisely the wish, never the intent.

## 7. What you can now see

You can now state evolution as a three-condition algorithm and say precisely why it's substrate-neutral. You've seen it run in bacteria for 80,000 generations, in naked RNA for 74 transfers, and on your own machine in 63 generations. You know why "survival of the fittest" misleads (fitness ≠ progress; the Monster), why history matters even without a plan (citrate), and how the algorithm turned on its own machinery and became better at evolving — the recursion at the heart of this series. You can place evolution and gradient learning side by side without hand-waving: same accumulate-what-works skeleton, opposite answers to "is variation aimed?", with the Baldwin effect, Valiant's proof, and Watson & Szathmáry's program marking the real bridges. And you can tell, when someone says an AI system "evolves," whether the word is doing work or decoration.

From here: [recursion-and-life](recursion-and-life.html) descends into how self-copying itself works; [aunt-hillary](aunt-hillary.html) takes the next stair — how blind local rules give rise to higher-level order that deserves its own description; and [sense-of-self](sense-of-self.html) asks what happens when an evolved system starts modeling the very thing doing the modeling.

There is one more thing this room points at, and the domain itself does the pointing. Evolution has no attention. It weighs nothing, notices nothing, intends nothing — it is the null hypothesis for mind, the proof of how far you can get without any. And yet every attentive system we know of is its product: attention is an evolved organ, selection's discovery that an organism that ranks what matters outcompetes one that doesn't. The only process we know that builds minds is a process that doesn't have one. Now the loop has closed once more: those evolved minds are building selection processes of their own — fitness functions, reward signals, evaluators — and this time the criteria are chosen. Evolution never had to answer what its filter was *for*; there was no one to ask. We are the part of the process that can be asked.

## Open questions

**Established (FACT).** Evolution requires only variation, differential fitness, and heredity, and runs on non-biological substrates (Spiegelman 1965; digital evolution platforms). Fitness gains in a constant environment continue without plateau for at least 60,000+ generations (Wiser et al. 2013 and follow-ups). Historical contingency can gate innovations (Blount 2008). Learning can accelerate evolution without Lamarckian inheritance (Hinton & Nowlan 1987, simulation; the Baldwin effect's importance *in nature* is harder to quantify and less settled). Evolutionary search is a working, competitive tool in modern AI for non-differentiable problems (Salimans et al. 2017; AlphaEvolve 2025).

**Contested (HYPOTHESIS).** Whether evolvability is directly selected for, or merely accumulates as a survivorship effect — models support both; decisive experiments are hard. Whether the evolution–learning correspondence (Watson & Szathmáry 2016) is a deep formal identity that will reorganize evolutionary theory, or a productive analogy that will stall. Why sexual recombination is worth its costs. Whether *open-ended* evolution — the ceaseless novelty of the biosphere — can be recreated in any artificial system; every digital-evolution platform so far eventually runs out of surprise, and nobody has a proven recipe for why the biosphere doesn't.

**Speculation worth holding (WILD).** That AI training pipelines are becoming a genuinely new heredity substrate — model weights copied, varied, selected, and merged at industrial scale, with selection criteria set by markets and labs — and that this constitutes a fourth major evolutionary transition in how information is inherited, after genes, brains, and culture. If that framing is right, the [noosphere](noosphere.html) room's question — what a planet-scale layer of selected information is becoming — is this room's question at the next level up. Nothing about current systems compels this reading; it is a lens, and lenses must earn their keep.

## Sources

Verified by live search or primary source, August 2026:

- Lenski LTEE: start date, protocol, populations, UT Austin transfer (June 21, 2022), 80,000 generations (Aug 2024), Cit+ in Ara-3 at ~31,000–31,500 generations (Blount et al. 2008), replay/contingency results, ~70% fitness gain by generation 20,000, power-law trajectory (Wiser et al. 2013) — [the-ltee.org](https://the-ltee.org/) and the [Wikipedia LTEE article](https://en.wikipedia.org/wiki/E._coli_long-term_evolution_experiment).
- Lewontin, R. "The Units of Selection." *Annual Review of Ecology and Systematics* 1 (1970).
- Spiegelman's Monster: 1965, Qβ replicase, 4,500 → 218 nucleotides over 74 transfers — [Wikipedia](https://en.wikipedia.org/wiki/Spiegelman%27s_Monster).
- Wagner, G.P. & Altenberg, L. "Complex Adaptations and the Evolution of Evolvability." *Evolution* 50(3):967–976 (1996).
- Kirschner, M. & Gerhart, J. "Evolvability." *PNAS* 95:8420–8427 (1998); *The Plausibility of Life* (2005) for facilitated variation.
- Dawkins, R. "The Evolution of Evolvability." In *Artificial Life* (ed. C. Langton), pp. 201–220, Addison-Wesley (proceedings of the 1987 workshop; cited as 1988/1989).
- Hinton, G.E. & Nowlan, S.J. "How Learning Can Guide Evolution." *Complex Systems* 1:495–502 (1987) — [author's page](https://www.cs.toronto.edu/~hinton/absps/evolution.htm).
- Valiant, L. "Evolvability." *Journal of the ACM* 56(1) (2009) — [ACM DL](https://dl.acm.org/doi/10.1145/1462153.1462156).
- Watson, R.A. & Szathmáry, E. "How Can Evolution Learn?" *Trends in Ecology and Evolution* 31(2) (2016).
- Salimans, T., Ho, J., Chen, X., Sidor, S., Sutskever, I. "Evolution Strategies as a Scalable Alternative to Reinforcement Learning" (2017) — [arXiv:1703.03864](https://arxiv.org/abs/1703.03864).
- AlphaEvolve: announced May 14, 2025; 48-multiplication 4×4 complex matrix algorithm; 0.7% Borg compute recovery; ~75% matched / ~20% improved on 50+ open problems — [DeepMind blog](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/).
- Weasel program: Dawkins, *The Blind Watchmaker* (1986); output above is from the exact script shown, executed 2026-08-25.

Stated from standard references, not re-verified by live search this session: Holland (1975); NEAT (Stanley & Miikkulainen 2002); Population Based Training (Jaderberg et al. 2017); Baldwin (1896); Dennett's substrate-neutrality framing (*Darwin's Dangerous Idea*, 1995); Tierra/Avida; LTEE hypermutator populations.

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
