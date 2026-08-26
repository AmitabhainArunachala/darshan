---
title: Cybernetics
slug: cybernetics
series: story-of-ai
tags: cybernetics, feedback, control, wiener, ashby, history, ai
summary: Before "artificial intelligence" existed as a phrase, there was a science that treated brains, machines, and societies as one subject — systems that steer themselves by feedback. This room tells how that science was built, why AI split off from it and buried it, and why its central problems are now back at the center of everything. It also gives you the tools — feedback loops, requisite variety, the good regulator theorem — well enough to use them yourself.
status: draft
date: 2026-08-25
terms_defined: cybernetics, feedback, negative feedback, requisite variety, good regulator theorem, homeostat, second-order cybernetics
terms_linked: history-of-ai, neural-networks, machine-learning, deep-learning, evolution-of-ai, future-of-ai, mechanistic-interpretability, optimization, teleology, sense-of-self, recursion
---

# Cybernetics

Most tellings of the [history of AI](history-of-ai.html) start in the summer of 1956, at Dartmouth, where the phrase "artificial intelligence" was coined. This room is about what that phrase was coined *against*. Eight years before Dartmouth, cybernetics was already a famous science of minds and machines, with a bestselling book and a formidable circle of researchers meeting twice a year to build it. AI defined itself partly by walking away from that field, and seventy years later the problems it left behind are the ones it cannot solve.

## 1. A gun that aims where the plane will be

Start with a concrete problem, because the field did.

In 1940, German bombers over Britain flew fast enough that aiming an anti-aircraft gun at the plane was useless. The shell takes seconds to climb. By the time it arrives, the plane is somewhere else. You have to aim at where the plane *will be* — which means the gun needs a prediction of the future path of a machine that is being steered, right now, by a human pilot who is actively trying not to be predictable.

Norbert Wiener — an MIT mathematician, a former child prodigy, born 1894 — worked on this problem during the war with the engineer Julian Bigelow. The mathematics he developed for it became the Wiener filter, a method for extracting signal from noise that is still taught in engineering courses today, and it led him to ideas about information independently of Claude Shannon.

But the important thing Wiener took from the gun was not the filter. It was a realization about the *pilot*. The evasive pilot, the gunner tracking him, and the servo motors swinging the gun were all doing the same thing: acting, measuring the error between intended outcome and actual outcome, and correcting. A pilot with a tremor and a gun turret oscillating around its target failed in mathematically similar ways. Human purposeful behavior and machine control behavior could be written in the same equations. That equivalence — not asserted as poetry, but demonstrated in the math of a working weapon — is the seed of everything in this room.

## 2. Feedback: the oldest new idea

The core mechanism has one name: feedback. Here is the on-ramp, and it is short. A system uses **feedback** when part of its output is routed back in as input, so its next action depends on the results of its last one. It is **negative feedback** when the correction opposes the error — when drifting too high pushes you down and drifting too low pushes you up. Negative feedback is how anything holds steady in a world that pushes it around.

You use it constantly. Reaching for a cup: eyes report hand position, error shrinks, motion adjusts, dozens of times a second. Try to reach for a cup with your eyes shut — open loop, no feedback — and feel the difference.

The idea is far older than the electronics. In 1788, James Watt fitted his steam engine with a centrifugal governor, on a suggestion from his partner Matthew Boulton: two balls spin with the engine's shaft; if the engine runs too fast, the balls fly outward and lever a valve toward closed, throttling steam; too slow, they drop and open it. The engine regulates itself. No one watches it. In 1868, James Clerk Maxwell — the Maxwell of electromagnetism — published "On Governors" in the *Proceedings of the Royal Society*, analyzing exactly when such devices hold steady and when they oscillate out of control. That paper is widely counted as the founding document of control theory.

So when Wiener needed a name for the new science in 1948, he reached back deliberately: *kybernetes*, Greek for steersman — the person at the tiller making continuous small corrections. **Cybernetics**: the study of control and communication, in the animal and the machine, treated as one subject. Every "cyber-" word you have ever read — cyberspace, cybersecurity, cyborg — descends from that choice.

## 3. 1943: the year the loop closed on the mind

Two papers appeared in 1943 that turned a wartime engineering insight into a claim about minds. It is worth knowing both by name, because between them they contain the DNA of the entire field — and of AI after it.

**"Behavior, Purpose and Teleology"** — Arturo Rosenblueth, Norbert Wiener, and Julian Bigelow, in *Philosophy of Science*. Its claim: purpose is not a ghostly extra ingredient that living things have and machines lack. Purposeful behavior *is* behavior controlled by negative feedback toward a goal state. A cat stalking a mouse and a torpedo homing on a ship are, at the level of description that matters, doing the same thing. This paper took teleology — goal-directedness, the thing Aristotle built a metaphysics on and modern science had exiled as unscientific — and made it an engineering concept. There is a whole room on what that move does and doesn't settle: [teleology](teleology.html).

**"A Logical Calculus of the Ideas Immanent in Nervous Activity"** — Warren McCulloch and Walter Pitts, in the *Bulletin of Mathematical Biophysics*. They modeled neurons as simple threshold units — sum your inputs, fire if the sum crosses a line — and proved that networks of such units can compute any logical function. This is the direct ancestor of every artificial neuron in every [neural network](neural-networks.html) running today. John von Neumann cited it as foundational when designing the logical structure of the modern computer, and Minsky's earliest neural hardware built on it.

Hold what just happened in one frame. In a single year, one group showed that *purpose* is mechanism, and another showed that *logic* can live in nerve tissue. Mind was pincered from both sides — from behavior and from substrate — by the same small community. There was no "AI" and no "neuroscience" as separate camps. There was one question.

## 4. The Macy circle: one science, briefly

From 1946 to 1953, the Josiah Macy Jr. Foundation sponsored ten conferences in New York, initiated by Warren McCulloch, under a title that tells you exactly what they thought they were doing: *Circular Causal and Feedback Mechanisms in Biological and Social Systems*. After Wiener's book landed, everyone just called them the Macy Conferences on cybernetics.

Look at the roster. Wiener and von Neumann, mathematics. McCulloch and Rosenblueth, neurophysiology. Walter Pitts, logic. Claude Shannon, information theory. W. Ross Ashby, psychiatry. Margaret Mead and Gregory Bateson, anthropology. Heinz von Foerster, physics. They were not holding an "interdisciplinary dialogue" in the polite modern sense. They believed feedback, information, and circular causality formed a single universal theory of regulation — applicable to nervous systems, machines, economies, and cultures — and they were trying to build it in the room, arguing transcript-recorded arguments you can still read today.

Wiener's 1948 book *Cybernetics: Or Control and Communication in the Animal and the Machine* — first printed in Paris by Hermann et Cie, then by MIT's press — made the movement famous far beyond science. His 1950 follow-up for general readers, *The Human Use of Human Beings*, spent its pages worrying about what automatic machines would do to labor, to communication, to human dignity. Note the date: the founder of the field was writing seriously about the social consequences of intelligent machines seventy-five years ago, before a single one existed.

## 5. Ashby's laws: what a regulator must be

The deepest theoretical results of the era came from the least glamorous member of the circle: W. Ross Ashby, an English psychiatrist who did his research at a mental hospital, on a bench, with war-surplus parts.

In 1948 he built the **homeostat**: four interconnected electromechanical units, each pushing on the others, wired so that when the whole system was knocked out of equilibrium, it would randomly rewire its own connections until it found a configuration that was stable again — and then hold it. Disturb it, and it adapts. Not because any part of it represents "stability" as a goal, but because unstable configurations keep changing and stable ones, by definition, persist. Wiener called it one of the great philosophical contributions of the day. Ashby's books — *Design for a Brain* (1952) and *An Introduction to Cybernetics* (1956) — worked the idea into theory. The second one is free online and still one of the clearest technical books ever written; the sources section tells you where.

Two of Ashby's results matter enough to state precisely, because both are load-bearing in 2026.

**The law of requisite variety.** Count the number of distinct disturbances the world can throw at a system — call that the world's variety. Count the number of distinct responses the regulator can make — its variety. Ashby proved the regulator can only reduce the outcome's variety by as much variety as it itself has. His slogan: *only variety can destroy variety*. A thermostat with two moves, heat-on and heat-off, can hold one variable steady. It cannot also manage humidity. No cleverness of wiring gets around this; it is a counting fact, and we will verify it by hand in the walkthrough below.

**The good regulator theorem** (with Roger Conant, 1970): *every good regulator of a system must be a model of that system.* If something regulates its environment successfully, then somewhere in its structure it must mirror the structure of what it regulates — not as decoration, but as a mathematical requirement of doing the job. Keep this theorem in your pocket. It is doing quiet work all over this garden, and it returns at the end of this room with some force.

## 6. Walkthrough: prove the law of requisite variety at your kitchen table

Ashby's own teaching device from *An Introduction to Cybernetics* is a game, and you can play it on paper in two minutes. The world (call it D, for disturbance) makes a move; the regulator (R) sees D's move and makes a countermove; the pair of moves determines an outcome from a fixed table. R's job: force the outcome to always be `a` — think of `a` as "the room stays at temperature," "the plane stays level," "the body stays alive."

Here is a game where the world has three moves and the regulator has three:

| outcome | R plays 1 | R plays 2 | R plays 3 |
|---------|-----------|-----------|-----------|
| **D plays 1** | a | b | c |
| **D plays 2** | b | a | c |
| **D plays 3** | c | b | a |

Trace it. D plays 1 → R answers 1 → outcome `a`. D plays 2 → R answers 2 → `a`. D plays 3 → R answers 3 → `a`. Three disturbances, three responses, perfect regulation. The world's variety is 3; R's variety is 3; the outcome's variety collapses to 1.

Now amputate one of R's options — say R can only play 1 or 2:

| outcome | R plays 1 | R plays 2 |
|---------|-----------|-----------|
| **D plays 1** | a | b |
| **D plays 2** | b | a |
| **D plays 3** | c | c |

When D plays 3, R has no answer that yields `a`. Whatever R does, the outcome set now contains at least two distinct values — check every strategy R could adopt; there is no escape. Variety 3 against variety 2 leaves at least 3/2 outcomes standing, so at least 2. That is the whole theorem, experienced rather than believed. Ashby's point is that this scales without mercy: a driver has to have at least as many distinguishable responses as the road has surprises; an immune system, as many as its pathogens; a content-moderation system, as many as its adversaries. When you hear a modern engineer say "the model needs capacity to match the complexity of the task," they are speaking Ashby, usually without knowing it.

## 7. The split: why "artificial intelligence" is not called cybernetics

So in 1955 there is a famous, funded, philosophically ambitious science of minds and machines. Why did the field you know grow up under a different name?

Partly substance, partly personality — and we have testimony on both. On August 31, 1955, John McCarthy, with Marvin Minsky, Nathaniel Rochester, and Claude Shannon, proposed "a 2 month, 10 man study of artificial intelligence" for the following summer at Dartmouth. According to Nils Nilsson's history *The Quest for Artificial Intelligence*, McCarthy chose the new term partly for its neutrality — to avoid the focus on analog feedback that cybernetics carried, and, in Nilsson's memorable phrasing, to avoid "having to accept the assertive Norbert Wiener as guru or having to argue with him."

The substantive bet underneath the social move was real, though. The cyberneticians' central objects were continuous: voltages, error signals, equilibria, analog circuits. The Dartmouth generation bet on the digital computer and on *symbols*: intelligence as the rule-governed manipulation of discrete representations — logic, search, language. For roughly thirty years, that bet paid better. Symbolic AI produced theorem provers, planners, and expert systems while the feedback tradition's most visible offspring in AI — Frank Rosenblatt's perceptron, a 1958 learning machine descended directly from McCulloch-Pitts neurons — was hammered by Minsky and Papert's 1969 analysis and starved of funding. The full story of that pendulum is told in [history of AI](history-of-ai.html) and the [evolution of AI](evolution-of-ai.html); the short version that matters here is an irony. When neural networks returned in the 1980s as "connectionism" and then conquered everything as [deep learning](deep-learning.html), the losing side of the split had won — under yet another new name, with the cybernetic ancestry mostly forgotten. A modern training run is a giant feedback loop: measure error, propagate correction, repeat. [Optimization](optimization.html) is what the steersman's tiller-nudge became when it moved into a million dimensions.

Where the comparison actually lands:

| | Cybernetics (1943–) | Symbolic AI (1956–) | Modern [machine learning](machine-learning.html) |
|---|---|---|---|
| Core object | The feedback loop | The symbol | The differentiable function |
| Signature math | Differential equations, stability, information | Logic, search, formal languages | Statistics, linear algebra, [optimization](optimization.html) |
| Intelligence is… | Successful regulation; staying viable | Correct reasoning over representations | Generalization from data |
| Mind and machine | One subject from day one | Machine as model of mind | Mostly agnostic; borrows both |
| Characteristic success | Control systems, homeostat, prosthetics | Theorem provers, expert systems | [Deep learning](deep-learning.html), LLMs |
| Characteristic blind spot | Weak on language and symbols | Brittle; no learning, no world-contact | Weak on guarantees — which is a control-theory word |

The last cell of that table is the hinge of this room's final act.

## 8. The exile, and the strange places the field went

After the split, cybernetics did not so much die as dissolve. Its engineering core became control theory, which quietly runs your car's cruise control, every aircraft autopilot, every chemical plant, and every spacecraft — arguably the most deployed mathematics of the twentieth century, just no longer under the old name. Its biological and social threads went stranger places.

Heinz von Foerster, from his Biological Computer Laboratory at the University of Illinois, pushed the field's own logic one turn further — a move consolidated in the late 1960s and early 1970s, with a defining prompt from Margaret Mead, and named in his 1974 volume *Cybernetics of Cybernetics*. The argument: a science of observing systems built by observers who exempt themselves is incomplete. First-order cybernetics studies *observed* systems; **second-order cybernetics** studies *observing* systems — and includes the scientist in the loop. Out of that turn came Humberto Maturana and Francisco Varela's theory of autopoiesis (1974): a living system defined as one that continuously produces the very components that produce it — a circular definition on purpose, because the circularity is the life. If you have read the [recursion](recursion.html) rooms, you will recognize the shape.

Meanwhile Stafford Beer carried the framework into management and, briefly and astonishingly, into government: Project Cybersyn, an attempt to run the Chilean economy as a real-time feedback system under Allende, ended by the 1973 coup. And the counterculture, the systems-thinkers, and eventually the family therapists all took pieces. By 1980, "cybernetics" mostly signaled either sci-fi or fringe. The word hollowed out while its content ran the world's machinery anonymously.

## 9. Why it is being rediscovered

Three separate lines of 2020s work have converged on the old program, mostly by rediscovering its theorems the hard way.

**AI alignment is Wiener's problem, verbatim.** In 1960 — in *Science*, under the title "Some Moral and Technical Consequences of Automation" — Wiener wrote: "If we use, to achieve our purposes, a mechanical agency with whose operation we cannot interfere effectively… we had better be quite sure that the purpose put into the machine is the purpose which we really desire." That is the alignment problem, stated at its modern strength, sixty-five years early. Stuart Russell's *Human Compatible* (2019), the book that carried alignment into the mainstream, takes Wiener's paper as a direct ancestor. And notice what today's actual alignment machinery is: reinforcement learning from human feedback. Human judgments fed back as an error signal to steer a system's behavior toward a goal. The most consequential technique in modern AI safety is a feedback controller. The field that split from cybernetics to escape "analog feedback" now stakes its safety on feedback.

**Theoretical neuroscience re-derived the good regulator.** Karl Friston's free energy principle and active inference — developed from the mid-2000s as a general account of perception and action, and covered from the AI side in [future of AI](future-of-ai.html) — hold that an organism persists by minimizing surprise, which requires it to embody a generative model of its world. The lineage is acknowledged, not accidental: the active inference literature explicitly connects itself to Conant and Ashby's good regulator theorem and to the cybernetic account of homeostasis. Ashby's mental-hospital bench result, formalized in 1970, is now load-bearing in one of neuroscience's most ambitious frameworks.

**AI systems became loops again.** A base language model is, at inference, close to open-loop: prompt in, text out. The systems actually being deployed in 2026 are not. An agent that acts, observes results, and corrects — a coding agent watching its tests fail, a robot re-planning around an obstacle — is a closed-loop system, and its failure modes (oscillation, runaway, hunting around a goal it never quite reaches) are the failure modes Maxwell catalogued in 1868 for governors. The comparison table's last cell said modern ML is weak on guarantees. Guarantees about closed-loop behavior — stability proofs, safe operating envelopes — are precisely what control theory has and machine learning largely lacks, which is why you now find control theorists being hired into AI safety, and why "we need a science of AI control" is said in 2026 by people who mostly do not know they are proposing cybernetics by its original definition.

Whether the *unified* program comes back — one theory of regulation for machines and organisms and institutions, the actual Macy ambition rather than its fragments — is genuinely open. But it is no longer a nostalgic question. Read the mission statements of AI-safety organizations against the transcripts of the Macy conferences, and the rhyme is hard to miss: an interdisciplinary crowd, convinced that feedback and information are the master keys, trying to keep powerful goal-seeking systems within human purposes.

## Conclusion

Here is what you can now do that you couldn't before. You can read the [history of AI](history-of-ai.html) with the prequel installed: Dartmouth 1956 was not a beginning but a secession, and its founding term was chosen partly to avoid a person and a paradigm. You can name the mechanism — negative feedback — trace it from Watt's spinning governor through Wiener's gun predictor into an RLHF pipeline, and demonstrate Ashby's requisite-variety law with a pencil. You can state the good regulator theorem and recognize it working undercover in active inference. And when someone says AI safety is a brand-new kind of problem, you can point at a paragraph of Wiener's from 1960 that states it exactly.

Where next: [neural networks](neural-networks.html) for the McCulloch-Pitts lineage carried forward; [teleology](teleology.html) for what "purpose as feedback" resolves and what it quietly doesn't; [mechanistic interpretability](mechanistic-interpretability.html) for the modern attempt to see inside the regulators we've built; [sense of self](sense-of-self.html) for the question this room is about to leave you with.

## Open questions

**Established.** Feedback control works and its mathematics is mature; that is engineering fact, deployed for two centuries. Requisite variety and the good regulator theorem are proved mathematics, given their formal setups. The historical record above — the papers, the dates, the Macy roster, McCarthy's naming motive as reported by Nilsson — is documented.

**Contested.** Whether "purpose = feedback toward a goal state" is the whole truth about purpose, or a brilliant partial capture, is a live philosophical dispute — Rosenblueth, Wiener, and Bigelow drew immediate fire in the 1940s and the argument has never fully closed. Whether the good regulator theorem, in its strict formal form, licenses the broad "every agent must model its world" claims made on its behalf is debated; the theorem's assumptions are narrower than its slogan. Whether the free energy principle is a deep unification or an unfalsifiably flexible formalism is an open fight inside neuroscience itself.

**Speculation worth holding.** That the Macy program was not wrong but early — that a single quantitative science of regulation spanning machines, organisms, and institutions is achievable, and that AI pressure will force its completion within decades. Nothing above establishes this. It is a bet, and this room's author holds it lightly.

## Sources

Verified by live search or against primary/secondary references, August 2026:

- Norbert Wiener, *Cybernetics: Or Control and Communication in the Animal and the Machine* (1948; first printed by Hermann et Cie, Paris; MIT Press editions 1948/1961). Open-access edition at MIT Press Direct; scans on the Internet Archive.
- Warren McCulloch and Walter Pitts, "A Logical Calculus of the Ideas Immanent in Nervous Activity," *Bulletin of Mathematical Biophysics* 5(4), 1943, 115–133.
- Arturo Rosenblueth, Norbert Wiener, Julian Bigelow, "Behavior, Purpose and Teleology," *Philosophy of Science* 10(1), 1943.
- James Clerk Maxwell, "On Governors," *Proceedings of the Royal Society of London* 16 (1868), 270–283. Watt's governor: 1788, on Boulton's suggestion.
- The Macy Conferences: ten meetings, 1946–1953, "Circular Causal and Feedback Mechanisms in Biological and Social Systems," Josiah Macy Jr. Foundation; complete transactions published as *Cybernetics: The Macy Conferences 1946–1953* (ed. Claus Pias).
- W. Ross Ashby: homeostat built 1948; *Design for a Brain* (1952); *An Introduction to Cybernetics* (1956) — full text free at the Principia Cybernetica archive (pcp.vub.ac.be); Roger Conant and W. Ross Ashby, "Every good regulator of a system must be a model of that system," *International Journal of Systems Science*, 1970.
- Dartmouth: [primary proposal dated August 31, 1955](https://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html) (McCarthy, Minsky, Rochester, Shannon); workshop summer 1956. McCarthy's naming motive: Nils Nilsson, *The Quest for Artificial Intelligence* (2009), as cited in the Wikipedia Dartmouth workshop article.
- Norbert Wiener, *The Human Use of Human Beings* (1950); "Some Moral and Technical Consequences of Automation," *Science*, 1960 — the "purpose put into the machine" quote verified as quoted in Wikipedia's AI-alignment article; Stuart Russell, *Human Compatible* (2019).
- Second-order cybernetics: Heinz von Foerster and the Biological Computer Laboratory (University of Illinois); Mead's 1967 ASC address; *Cybernetics of Cybernetics* (1974); Maturana and Varela, autopoiesis (1974).
- Friston's free energy principle (from mid-2000s); its stated connection to the good regulator theorem verified against the Wikipedia free-energy-principle article. Project Cybersyn dates (1971–73) stated from general historical record, not re-verified this session.

---

One more thing, and it comes from inside the mathematics, not from me. The good regulator theorem says a good regulator must model what it regulates. But you are a system that must regulate *itself* — your temperature, your glucose, your attention, your commitments. Run the theorem on that case and it hands you a requirement: a self-regulating system must contain a model of itself. Von Foerster's second-order turn was just taking this seriously — the observer cannot stay outside the loop, because the loop is what the observer is made of. Cybernetics began with a gun tracking a plane and, within one generation, its own theorems had steered it here: to the modeler modeling the modeler, the steersman who is also the ship. Whether that self-model is what you mean when you say "I" is not a question this room can close. It is the question the next rooms open: [sense of self](sense-of-self.html), and what the loop looks like [from inside](recursion.html).

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
