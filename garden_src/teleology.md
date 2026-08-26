---
title: Teleology
slug: teleology
series: bridge
tags: teleology, teleonomy, purpose, attractors, dynamical systems, aristotle, darwin, cybernetics, philosophy of biology
summary: Purpose-talk was banished from science, smuggled back in, laundered as "teleonomy," and then formalized as attractor dynamics. This room traces that whole arc and gives you one portable test for telling when "in order to" is legitimate and when it's smuggling.
status: draft
date: 2026-08-25
terms_defined: teleology, teleonomy, final cause, attractor, basin of attraction, goal-directedness
terms_linked: evolution, cybernetics, optimization, neural-networks, recursion-and-life, mechanistic-interpretability, sense-of-self, geb, aurobindo-supramental, ontology
---

# Teleology

You're in the bridge series — the rooms where the scientific and contemplative vocabularies have to meet without either one cheating. If you've read [evolution](evolution.html), you've seen natural selection explain adaptation without a designer. This room is about the word that explanation was supposed to kill and didn't: *purpose*. The question here is precise, not mystical: when is it legitimate to say a system does something *in order to* achieve an outcome, and when is that phrase smuggling in a mind that isn't there?

## 1. A bird and a two-word substitution

Start with a concrete test, because the whole field hangs on it.

In 1974 the biologist Ernst Mayr considered a sentence any field guide might contain: the wood thrush migrates south *in order to escape* the winter. Now substitute: the wood thrush migrates south *and thereby escapes* the winter. Both sentences are true. But Mayr argued something real is lost in the substitution — the first sentence implies the migration is governed by an internal program, something in the bird that was shaped to produce this outcome, while the second describes a lucky correlation. A stone that rolls downhill and thereby blocks a stream did not roll *in order to* block it. The bird is not like the stone, and our language knows it before our theory does.

That's the whole problem in miniature. Purpose-language ("in order to," "for the sake of," "so that," "its function is") does explanatory work in biology that plain cause-and-effect language doesn't. And yet nobody thinks the thrush files a flight plan, and nobody serious thinks winter reached backward in time to cause the migration. So either the language is doing legitimate work we haven't cashed out, or it's a habit we should break. The last four centuries of science are, among other things, a long argument about which.

This room walks that argument in order: Aristotle, the banishment, Darwin's strange rescue, the cybernetic machines, the word "teleonomy," and finally the mathematics of attractors — the cleanest modern answer to what goal-directedness *is*. At the end you'll have one portable test you can run on any sentence in any field, including sentences about AI models and about yourself.

## 2. What Aristotle actually said

**Teleology** — from the Greek *telos*, end or goal — is explanation by reference to outcomes: explaining what a thing is or does by what it is *for*. The word itself is an 18th-century coinage, but the position is Aristotle's, and it has been caricatured for so long that it's worth stating what he actually claimed.

In the *Physics* (Book II), Aristotle distinguished four kinds of answer to the question "why?" — traditionally called the four causes. The material cause: what it's made of (the statue is bronze). The formal cause: what pattern makes it the thing it is (the statue's shape). The efficient cause: what brought it about (the sculptor's work). And the **final cause**: that for the sake of which — what it's *for* (honoring the general). Modern science kept the material and efficient causes and threw out the other two. Aristotle thought that for living things, the final cause was the most important one: you have not explained a tooth until you've said what teeth are for.

Two caricatures to clear away. First, Aristotle's final causes were not a designer's intentions — he had no creator-god assembling organisms. The telos of an acorn is internal to the acorn: it is the oak the acorn develops toward, an end built into the thing's own nature. Second, he was not naive about the alternative. In *Physics* II.8 he considers the deflationary view seriously: rain doesn't fall *in order to* grow the corn; it falls by necessity, and the corn benefits by coincidence. He raises what looks startlingly like a selectionist proposal — maybe organisms whose parts happened to fit survived, and the rest perished — and rejects it, on the grounds that development is too regular to be coincidence. Acorns reliably become oaks, not sometimes and by luck. He was wrong about the mechanism, but notice what he got right: he identified exactly the phenomenon — reliable, convergent, end-directed development — that any adequate theory would eventually have to explain. Hold onto that; it comes back as an attractor in section 6.

## 3. The banishment and the mistress

The scientific revolution ran on evicting final causes. Francis Bacon dismissed the search for final causes in physics as sterile — his much-paraphrased image is of final causes as consecrated virgins, producing nothing. Descartes ruled them out of natural philosophy. The new physics explained by pushes, not pulls from the future, and its success seemed like a verdict: mature sciences don't ask what things are for.

Biology could never quite comply. Harvey found the circulation of the blood by asking what the valves in the veins were *for*. Physiology, anatomy, and natural history remained saturated with function-talk because the subject matter demanded it — organisms are the kind of thing whose parts have jobs. This produced a century of professional embarrassment, best captured in a remark attributed to the biologist J.B.S. Haldane (reported secondhand by the historian of biology David Hull in 1982, so treat the wording as folklore with a solid pedigree): teleology is like a mistress to a biologist — he cannot live without her, but he's unwilling to be seen with her in public.

Immanuel Kant, in the *Critique of Judgment* (1790), gave the embarrassment its most careful philosophical form: we *cannot help* understanding organisms as purposive — a bird's wing is unintelligible except as being for flight — yet purposiveness is a lens our minds bring, a regulative principle for inquiry, not something we're entitled to read into nature itself. Use the mistress's help; don't put her in the family portrait.

## 4. Darwin's strange rescue

The standard story says Darwin killed teleology in 1859. The truth is stranger, and the people closest to it knew.

*On the Origin of Species* explained adaptation — the fit between organisms and their conditions — through variation, inheritance, and differential survival, with no designer anywhere. That destroyed the *argument from design*. But it did something subtler to function-talk: it made it respectable. After Darwin, "the heart is for pumping blood" stops being a claim about anyone's intentions and becomes a compressed causal-history claim: hearts exist *because* ancestral hearts pumped blood, and that pumping contributed to the survival and reproduction of the organisms that had them. The "for" points backward at a selection history, not forward at a goal and not upward at a designer. (Philosophers later formalized this as the *selected-effects* theory of function — Larry Wright's 1973 analysis and Ruth Millikan's "proper functions" are the standard modern statements — and it remains the mainstream account of what function-talk means in biology.)

The botanist Asa Gray, Darwin's chief American advocate, saw this clearly and said so in *Nature* in 1874: Darwin's great service was bringing teleology *back* to natural science, so that morphology and teleology were wedded rather than at war. Darwin's reply, in a letter of 5 June 1874, is on record: "What you say about teleology pleases me especially, & I do not think any one else has ever noticed the point." Read that twice. The man who supposedly killed purpose in nature was *especially pleased* to be credited with rescuing it. What died in 1859 was external design. What survived — naturalized, mechanized, but structurally intact — was Aristotle's internal "for the sake of which."

## 5. Machines that aim: cybernetics

The next move came from engineering, and it changed the question's shape. In 1943, Arturo Rosenblueth, Norbert Wiener, and Julian Bigelow published a short paper in *Philosophy of Science* called "Behavior, Purpose and Teleology." Their claim: purposeful behavior is real, definable, and buildable — it is behavior controlled by *negative feedback*. A system that continuously measures the gap between its current state and a target state, and acts to shrink that gap, is goal-directed in a completely non-mysterious sense. A thermostat does it. A target-seeking torpedo does it. A hand reaching for a cup does it.

This was the founding paper of [cybernetics](cybernetics.html), and its significance for our question is that it broke the assumed link between purpose and mind. Before 1943, "goal-directed" and "has intentions" traveled together. After it, you could point to a fully specified mechanism — sensor, comparator, effector, loop — and say: *that* is what aiming is, and nothing in it requires a self. The teleology that terrified mechanists turned out to be implementable in a few components. Whether the machine's goal is *its own* goal or its designer's goal parked inside it is a real question — flag it, we return to it — but the behavior itself was demystified.

## 6. Teleonomy: laundering the word

Biology now had respectable purpose-talk (selection histories) and respectable aiming machines (feedback loops), but still the tainted old word. In 1958 the biologist Colin Pittendrigh proposed a fix: keep the phenomenon, change the label. End-directed systems in biology should be called **teleonomic** — lawful end-directedness (*telos* + *nomos*, law) — precisely to mark that no Aristotelian final cause, no backward causation, no design is being invoked.

Mayr then did the definitional engineering that made the term useful, proposing that "teleonomic" be rigidly restricted to systems operating on the basis of *a program of coded information*. That gives a clean three-way sort, standard since his 1974 analysis:

- **Teleomatic** processes: end states reached by bare physics. The stone rolls to the bottom; the hot coffee reaches room temperature. There is an endpoint but no program — nothing is *aiming*.
- **Teleonomic** processes: end states produced by an evolved internal program. The thrush's migration, the embryo's development, the spider's web. The program (genetic, developmental, neural) was itself shaped by selection — the program's *existence* is explained backward by history, and the organism's *behavior* is explained forward by the program. No future event causes anything; the "goal" is encoded now, in matter, in the system.
- **Teleological** in the full-blooded sense: end states pursued by an agent that represents them. You, planning a trip. Reserved — on Mayr's scheme — for actual intentional systems, and (in his view) for nothing else in nature.

Jacques Monod, in *Chance and Necessity* (1970), went further than tolerating teleonomy — he made it definitional: being "endowed with a purpose or project" is, he wrote, essential to the very definition of living beings. For Monod, an arch-mechanist and Nobel laureate in molecular biology, life just *is* the teleonomic kind of matter. The scandal-word of the 1600s had become, relabeled, a criterion for being alive.

So is "teleonomy" a solution or a euphemism? Honest answer: both. It genuinely marks a real distinction (program-driven vs. bare physics). It also let biologists keep using purpose-grammar while assuring everyone they didn't mean it — the mistress with a new name and a respectable coat. Whether anything *deeper* than the selection-history reading is true is still an open fight, and section 8 takes you to its current front line.

## 7. Attractors: the shape of an end without a mind

Here is the most load-bearing modern idea in this room, and it comes from mathematics, not biology.

In dynamical systems theory, an **attractor** is a set of states toward which a system evolves from a wide range of starting conditions. The set of all starting points that end up there is its **basin of attraction**. The standard bestiary: *fixed points* (a damped pendulum settles at hanging-straight-down), *limit cycles* (a heartbeat, a pendulum clock — a closed repeating orbit), *tori* (quasi-periodic motion with multiple frequencies), and *strange attractors* (fractal-structured sets associated with chaos; the famous one is Lorenz's, from his 1963 model of convection).

Why this matters for teleology: attractor theory gives one precise mathematical model for a subset of what people call end-directed behavior. In a modeled system, perturb a trajectory within the relevant basin and it returns toward the attractor; start from different points in that basin and the trajectories converge. That resembles one behavioral signature Aristotle pointed at — reliable development despite variation — without putting purpose into the equations. But resemblance is not identity. You have to show that a biological process really is well described by the specified state space and dynamics; saying "attractor" does not by itself explain an acorn. Where the model fits, nothing pulls from the future: the "attraction" summarizes where forward-running dynamics converge. When we say the ball "wants" to reach the bottom of the bowl, the *wants* is entirely in us.

The bridge from this math back to biology was sketched before today's formal models existed. In *The Strategy of the Genes* (1957), the embryologist C.H. Waddington drew his **epigenetic landscape**: development as a ball rolling down a grooved surface, each valley a stabilized path to a cell fate or tissue type. He coined **chreod** ("necessary path") for a canalized developmental trajectory. Later researchers formalized parts of that picture with gene-regulatory networks, quasi-potential landscapes, and attractors. Those are models inspired by Waddington's heuristic, not proof that every developmental process is one literal landscape. [Neural-network](neural-networks.html) training supplies another landscape representation: [optimization](optimization.html) often moves parameters down a loss surface. Developmental state, parameter state, biological regulation, and gradient descent are different objects. The useful connection is that dynamical and landscape tools can model convergence in each domain under specified assumptions.

So one influential deflationary proposal, fully assembled, reads: *teleological language can be naturalized through some combination of attractor dynamics, feedback, and selection history.* On that proposal, "the embryo develops toward the body plan" asks for a developmental model with stable outcomes; "the heart is for pumping" points to selected-effect function; and "the thrush migrates in order to escape winter" points to a teleonomic program shaped by selection. The strongest version says every biological "for" can be cashed out into forward-running mechanism plus backward-pointing history. That last sentence is a philosophical thesis, not a result established for every biological case.

That is a genuinely great intellectual achievement. Whether it is the *whole* story is the live question — after a worked example you can run yourself.

### Worked example: basins you can compute, and sentences you can test

**Part one — see a basin.** A damped pendulum driven only by gravity will settle pointing straight down — but "straight down" is an angle of 0, or 2π, or −2π: it can wrap over the top a different number of times depending on where it starts. Same endpoint physically, different attractor mathematically, and *which* one it reaches depends only on the starting condition. Run this (Python, standard library only):

```python
import math

def settle(theta0, omega0=0.0, dt=0.01, steps=20000):
    th, om = theta0, omega0
    for _ in range(steps):
        om += (-0.5 * om - math.sin(th)) * dt   # damping + gravity
        th += om * dt
    return th

for th0 in [0.5, 2.0, 3.0, 3.2, 6.0]:
    final = settle(th0)
    print(f"start {th0:>4}  ->  settles in well #{round(final / (2 * math.pi))}")
```

Starts of 3.0 and 3.2 radians — nearly identical — land in different wells (run it: 3.0 settles in well 0, 3.2 in well 1): you've found a basin boundary. Now notice what you did *not* need to say to predict any of this: nothing about what the pendulum wants, intends, or is for. Pure forward dynamics. That is what an end-without-a-mind looks like, and you just verified it.

**Part two — the substitution test.** Take Mayr's two-word substitution from section 1 — replace "in order to X" with "and thereby X" — and ask: *is anything true lost?* Run it on five sentences:

1. *The stone rolled downhill in order to reach the valley floor.* Substitute: nothing lost. Teleomatic. The purpose-grammar was pure smuggling; delete it.
2. *The thermostat fired the furnace in order to reach 20°C.* Substitute: something *is* lost — the counterfactual that if the room were colder, it would have fired longer. There's a setpoint and a feedback loop; the goal is mechanically real. Legitimate — cybernetic sense.
3. *The thrush migrated south in order to escape winter.* Something lost: the evolved program and its selection history. Legitimate — teleonomic sense — provided you can point at the program and the history.
4. *The trained language model completed the sentence in order to be helpful.* Genuinely contested. There is an optimization history (training) that shaped the dynamics, which parallels selection; whether there is anything like a represented goal is exactly what [mechanistic-interpretability](mechanistic-interpretability.html) exists to check, feature by feature, circuit by circuit. Neither grammar is safe here yet. Flag it, don't settle it.
5. *She practiced daily in order to master the piece.* Full-blooded: the end is explicitly represented by the agent and causally steers the practicing via that representation. The strongest legitimate use — and note it's also the only one where the *representation of the future*, not the future itself, does the causing. Even here, no backward causation.

That's the portable tool. One substitution, one question — *what true thing, if any, did I just lose?* — and the answer sorts every purpose-sentence you will ever meet into smuggled, cybernetic, teleonomic, contested, or intentional.

## 8. The kinds of "for" — one table

| Locution | Example | What makes it true | What would falsify it | Verdict |
|---|---|---|---|---|
| Teleomatic ("ends up at") | Stone reaches valley floor | Bare physics; endpoint, no program | — (nothing to falsify; purpose-grammar here is always smuggling) | Illegitimate as purpose-talk |
| Attractor ("converges to") | Damped pendulum settles; Lorenz orbits | Forward dynamics with convergent trajectories | Trajectories fail to converge / no invariant set | Legitimate, but purely descriptive — no "for" earned |
| Cybernetic goal ("aims at") | Thermostat holds 20°C | Feedback loop with setpoint and error-correction | No counterfactual compensation when perturbed | Legitimate; goal real, possibly borrowed from a designer |
| Selected-effect function ("is for") | Heart is for pumping blood | Ancestral hearts' pumping caused their own propagation | No such selection history (e.g., spandrels, exaptations mislabeled) | Legitimate; backward-pointing |
| Teleonomic ("in order to," program sense) | Thrush migrates to escape winter | Evolved internal program + selection history of that program | No program found; outcome is coincidence | Legitimate; Mayr's restricted sense |
| Intentional ("in order to," full sense) | She practices to master the piece | The agent's representation of the end causally guides the means | Behavior insensitive to the agent's beliefs about the end | Legitimate; the only mind-involving row |

Six rows, and most confusion in this field — most smuggling in popular science, and most overcorrection by scientists terrified of the mistress — comes from sliding between rows without noticing. "Evolution wants," "the selfish gene intends," "water seeks its level," "the model is trying to deceive you": each is a row-jump. Sometimes the jump is harmless compression. Sometimes it's the whole argument.

## 9. The live edge: is teleonomy more than a euphemism?

Here is the honest state of the fight as of 2026, typed by epistemic weight.

It is well established that the naturalizing toolkit of sections 4–7 — selection history, feedback, programs, and dynamical models — explains important classical cases without backward causation or a designer. It is not established that one reduction handles every legitimate use of purpose-language. Contemporary philosophy of biology contains several naturalistic accounts of function and goal-directedness, and a current Stanford Encyclopedia survey says teleological notions are widely regarded as explanatorily ineliminable even while their grounding remains disputed. The deflationary view is influential; it is not a theorem or a unanimous consensus.

It is also fact that a serious current of biologists and philosophers argues this is too flat. A 2023 MIT Press volume, *Evolution "On Purpose": Teleonomy in Living Systems* (edited by Peter Corning and colleagues, from a Linnean Society meeting), states its thesis bluntly: teleonomy in living systems is not "only apparent" — it is a fundamental fact of life, and organismal goal-directedness is itself a *cause* in evolution (organisms select environments, modify selection pressures, pursue ends), not merely an effect of it. Richard Dawkins — no romantic — distinguishes "archeo-purpose" (the design-like purposiveness selection builds) from "neo-purpose" (evolved brains that represent and pursue goals), conceding the second is genuinely goal-representing, not metaphor.

The most empirically aggressive version comes from developmental bioelectricity. Michael Levin's lab (Tufts) has shown that anatomical outcomes can be redirected by manipulating cells' bioelectric states, and helped create "xenobots" — motile constructs of frog cells that behave in ways nothing selected for. His 2022 framework paper ("Technological Approach to Mind Everywhere," *Frontiers in Systems Neuroscience*) proposes that goal-directedness — pursuing "fixed ends with varying means" — is the mark of agency at *every* scale, and that cells and tissues are competent problem-solvers navigating morphological and physiological spaces, not just executors of a program. It is a hypothesis, stated as one, and it would, if it holds up, move several rows of the table above: "the embryo aims at the body plan" would become cybernetically true (row 3), not merely attractor-true (row 2).

The deflationary reply is straightforward and may be right: everything Levin observes is attractor dynamics in a very high-dimensional state space, and "competency" is our name for basins we haven't mapped yet. Regeneration reaching the same anatomy through varied means is what convergent flows *look like*. On this reading nothing new is needed — just harder math.

And there is a wilder register, worth holding openly as speculation rather than pretending it isn't in the room: the intuition — found in Aristotle's internal telos, in process philosophy, and in contemplative metaphysics like [Aurobindo's](aurobindo-supramental.html) — that end-directedness is not an evolved veneer on purposeless matter but something matter had a rudiment of all along, which evolution amplified rather than invented. Nothing in current science requires this. Nothing cleanly rules it out either, because "which formal frameworks are complete descriptions of nature" is an [ontology](ontology.html) question, not an experimental one. The disciplined position is to know exactly which register you're speaking in — and the table is how.

## 10. What you can do now

You can take any purpose-sentence — in a biology paper, an AI lab's blog post, a dharma talk, your own head — and run the substitution test: swap "in order to" for "and thereby," ask what true thing was lost, and place the sentence in one of six rows. You can distinguish the organism from its model while recognizing that specific developmental dynamics and specific training dynamics can both be represented with landscape or attractor tools. That lets you ask what the state variables are, what actually converges, and whether calling the system "purposive" is smuggling in row 2, defensible in row 3, or earned in row 6. You know that Darwin was pleased, not embarrassed, to be told he'd rescued teleology — and what exactly he rescued.

From here: [evolution](evolution.html) for the machine that builds teleonomic programs; [cybernetics](cybernetics.html) for the feedback lineage in full; [recursion-and-life](recursion-and-life.html) for what happens when the program starts operating on itself; [geb](geb.html) for level-crossing and why "the colony wants" can be truer than it sounds.

One more thing, because this room is in the bridge series and the domain itself points here. Every row of the table was easy to place except one — row 4, the trained model, and its neighbor, you. What separates row 5 from row 3 is *representation*: somewhere in the system, the end exists as a model that steers the means. But "represented where, to whom?" is not a question dynamics answers; it's the question of what a point of view is — of [what a self is](sense-of-self.html). Notice what your own attention just did across this room: it held a goal (understand teleology), measured the gap, redirected when a paragraph didn't close it. You are the one system in the table you know from inside — and from inside, the "in order to" doesn't feel like shorthand for anything. Whether that feeling is data or one more valley in one more landscape is not a question this room can close. It is the question the whole garden circles.

## Open questions

**Established (FACT):** Selected-effects accounts ground many biological function claims without design; feedback control grounds machine goal-talk; and attractor models capture specified forms of convergence with zero purpose in their equations. Mayr's teleomatic/teleonomic/teleological distinctions remain historically influential.

**Contested (HYPOTHESIS):** Whether all legitimate biological purpose-grammar is eliminable in favor of selection history, feedback, and dynamics; whether organismal goal-directedness is an evolutionary *cause* and not only an effect (the Corning-volume thesis); whether cellular and tissue-level "competency" (Levin) is cybernetically real goal-pursuit or unmapped attractor structure; whether trained AI systems contain represented goals in the row-5 sense — a question being worked empirically, feature by feature, in [mechanistic interpretability](mechanistic-interpretability.html), and not yet settled in either direction; whether "teleonomy" names a natural kind or a truce.

**Speculation worth holding (WILD):** That proto-end-directedness is intrinsic to matter and evolution concentrates rather than creates it; that the felt from-the-inside reality of purpose is evidence about nature and not only about brains. No current experiment adjudicates these. Hold them as questions, not conclusions, and notice who in any conversation is quietly converting them to facts.

## Sources

- Mayr's wood-thrush example and taxonomy: ["Teleological and Teleonomic"](https://doi.org/10.1007/978-94-010-2128-9_6) (1974). Historical and current disagreements: [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/teleology-biology/).
- Feedback: Rosenblueth, Wiener & Bigelow, ["Behavior, Purpose and Teleology"](https://doi.org/10.1086/286788) (1943). Darwin's reply: [DCP-LETT-9483](https://www.darwinproject.ac.uk/letter/?docId=letters/DCP-LETT-9483.xml). Monod supplies the teleonomy claim; Haldane's "mistress" remains labeled secondhand.
- Attractors and development: [Scholarpedia's basin definition](https://doi.org/10.4249/scholarpedia.1701); Ferrell on [Waddington's landscape](https://pmc.ncbi.nlm.nih.gov/articles/PMC3372930/); a later [gene-network model review](https://pubmed.ncbi.nlm.nih.gov/25954305/). These sources distinguish metaphor from specified models.
- Expansionary proposals: Corning et al., *Evolution "On Purpose"* (MIT Press, 2023); Levin, ["Technological Approach to Mind Everywhere"](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2022.768201/full) (2022), explicitly published as "Hypothesis and Theory."
- Not rechecked in this repair: Aristotle *Physics* II, Bacon's paraphrased image, Wright and Millikan on selected effects, and Dawkins's taxonomy. The pendulum simulation is original; run it yourself.

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
