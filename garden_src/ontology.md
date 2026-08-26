---
title: What Ontology Means
slug: ontology
series: bridge
tags: ontology, philosophy, knowledge-representation, metaphysics, categories, ai
summary: The word "ontology" lives two lives. In philosophy it names the oldest question there is — what exists? In computing it names an engineered artifact — a formal spec of categories and relations. This room teaches both lives, shows where they meet, and shows why every AI system, whether anyone admits it or not, is forced to make ontological choices.
status: draft
date: 2026-08-25
terms_defined: ontology, ontological commitment, categories, knowledge graph, top-level ontology
terms_linked: mechanistic-interpretability, neural-networks, machine-learning, deep-learning, history-of-ai, leading-models, sense-of-self, what-self-means, teleology, geb, hofstadter, ai-and-the-traditions, cybernetics, top-papers-mi
---

# What Ontology Means

You're in the bridge series — the rooms where the technical garden and the contemplative garden share a wall. Most bridge rooms carry a tradition's map or a big claim. This one carries a single word. "Ontology" is used every day by two communities that barely talk to each other: philosophers, for whom it names the study of what exists, and engineers, for whom it names a file you can download. Both uses are legitimate, both are precise, and the space between them is where AI now lives. If you've read [machine-learning](machine-learning.html) or [mechanistic-interpretability](mechanistic-interpretability.html), you've already been doing ontology without the name.

## 1. Start with a concrete thing: a gene, a label, a war

In May 2000, a consortium of biologists published a short paper in *Nature Genetics* called "Gene ontology: tool for the unification of biology" (Ashburner et al., vol. 25, pp. 25–29). Their problem was mundane and enormous: fly biologists, mouse biologists, and yeast biologists were describing the same molecular machinery in different vocabularies. The same protein activity would be called one thing in a *Drosophila* database and another thing in a yeast database, and no computer could tell they were the same.

Their fix was to build a controlled, structured vocabulary — the Gene Ontology — with three root domains: **molecular function** (what a gene product does at the molecular level, like binding or catalysis), **biological process** (larger operations with a beginning and end), and **cellular component** (where in the cell it happens). Every term gets an ID, a definition, and typed relations to other terms. A curator annotates a gene to `GO:0005739` (mitochondrion) and now every database on Earth agrees on what was just said. The consortium's 2019 resource paper reported roughly 45,000 terms and more than seven million annotations across more than 3,200 species.

Notice what happened. Before anyone could unify the databases, someone had to decide *what kinds of things there are* in molecular biology. Is "binding" a thing? Is a "process" a different kind of thing from a "location"? Is a protein complex a component or a bunch of components? These are not database questions. They are questions about what exists — asked, this time, with a deadline and a budget.

That's the whole shape of this room. The engineering problem keeps running into the philosophical question, because the philosophical question was never optional. It was just deferrable — until you tried to make two systems agree.

## 2. The first life: ontology in philosophy

The philosophical discipline is old; the word is not. "Ontology" was coined in the early 1600s from Greek *ontos* (being) + *logos* (study), but the activity goes back at least to Aristotle's *Categories*, which proposed that everything sayable falls under a small set of highest kinds — substance, quantity, quality, relation, place, time, and a few more. The claim underneath the list is the interesting part: reality has joints, and a finite mind can find them.

The cleanest modern statement of the problem is W.V.O. Quine's 1948 essay "On What There Is" (*Review of Metaphysics*). It opens with what might be the best first paragraph in analytic philosophy:

> "A curious thing about the ontological problem is its simplicity. It can be put in three Anglo-Saxon monosyllables: 'What is there?' It can be answered, moreover, in a word — 'Everything.'"

Everything exists, trivially — and then the fighting starts, because the fight was never about "everything." It's about the inventory. Do numbers exist, or just numerals? Do holes exist, or just perforated things? Does "the average American family" with its 2.5 children exist? Quine's contribution was a *criterion* rather than an answer, usually compressed to the slogan **to be is to be the value of a bound variable**. Unpacked: look at your best theory of the world, write it in logical notation, and see what the theory *quantifies over* — what has to be in the domain of "there exists an x such that…" for the theory's sentences to come out true. Those are your **ontological commitments** (the things your accepted statements require to exist, whether you meant to sign up for them or not). You don't discover what exists by squinting at reality; you discover what your own best descriptions have already committed you to.

Philosophers after Quine split the field into layered questions — the Stanford Encyclopedia of Philosophy's entry on logic and ontology sorts them into four projects: what we're *committed* to, what there *is*, what the most *general features* of what there is are, and the meta-question of what ontology should even be trying to do. You don't need the taxonomy. You need the posture: in philosophy, ontology is a *truth-seeking* enterprise. There is presumed to be one world, and the job is to get its inventory right.

Hold that. It's exactly the property the second life gives up.

## 3. The second life: ontology as an artifact

In 1993, Tom Gruber — then at Stanford's Knowledge Systems Laboratory — needed a word for the shared vocabularies that knowledge-based systems would use to interoperate, and he reached for the philosophers' word. His definition, refined in a 1995 paper in the *International Journal of Human-Computer Studies* ("Toward Principles for the Design of Ontologies Used for Knowledge Sharing"), became the field's standard: **an ontology is an explicit specification of a conceptualization** — a formal, machine-readable declaration of the objects, concepts, and relations presumed to exist in some domain.

Read that definition against Quine and you can see the whole pivot in two words: *presumed to exist*. The engineer doesn't claim the inventory is true. The engineer claims it's *declared* — written down explicitly enough that two programs, or two labs, or two companies can commit to the same one. Gruber was explicit that this is applied engineering, not applied metaphysics: an ontology in this sense is a designed artifact, judged by whether it serves knowledge sharing, not by whether it carves nature at its joints.

The artifact tradition then built real infrastructure:

- **Cyc**, started by Douglas Lenat at MCC in the 1980s, tried to hand-encode common sense itself. Secondary accounts put its later scale at roughly 1.5 million terms and 24.5 million assertions, and a widely repeated 2002 estimate put the investment at $60 million and 600 person-years. Those figures are useful for scale, but I could not verify them against a stable Cyc release record, so treat them as reported rather than audited. The project remains a rare attempt to build a common-sense ontology by sustained manual encoding.
- **OWL**, the Web Ontology Language, became a W3C recommendation in 2004, with OWL 2 following in October 2009. OWL 1 DL drew on the description logic SHOIN(D); OWL 2's direct semantics are tied to SROIQ. In both cases the engineering move is visible: restrict which constructions count as DL ontologies so standard reasoning questions retain useful computational guarantees. Philosophy never had to publish that trade in a conformance specification. Engineering did.
- The **Gene Ontology** you met in section 1 — the artifact tradition's clearest success.
- **Basic Formal Ontology (BFO)**, developed by the philosopher Barry Smith and colleagues from 2001, is a *top-level ontology* (a small set of maximally general categories — like "object" vs. "process" — that domain ontologies plug into so they can interoperate). BFO divides everything into **continuants** (things that persist through time, like a cell) and **occurrents** (things that happen, like a cell division). It became ISO/IEC 21838-2 in 2021. Then a 2024 joint Department of Defense and Intelligence Community memo named BFO as a top-level baseline and the **Common Core Ontologies (CCO)** as a mid-level baseline. CCO is a suite of eleven ontologies built on BFO, bridging its general categories to domain vocabularies. Sit with that for a second: a classification of being, descended from Aristotle's *Categories*, is now an ISO standard and part of a defense-sector ontology stack. The two lives of the word are not as separate as the two communities pretend.
- **Knowledge graphs** (large networks of entities and typed relations, an ontology's categories filled in with millions of instances) took the artifact mainstream. Google launched its Knowledge Graph on May 16, 2012, under the slogan "things, not strings" — search should return the *entity* Taj Mahal, not pages containing the string "taj mahal." Seven months in, it covered 570 million entities and 18 billion facts; by 2020 Google reported 500 billion facts about 5 billion entities.

Here is the comparison the two communities rarely make side by side:

| Axis | Ontology (philosophy) | Ontology (computing) |
|---|---|---|
| Grammatical number | Singular — *ontology*, the discipline | Countable — *an* ontology, *many* ontologies |
| Question asked | What exists? | What shall we treat as existing, for this purpose? |
| Success criterion | Truth | Interoperability, consistency, usefulness |
| How many can be right | At most one inventory of the world | Many, coexisting, per domain |
| Method | Argument, analysis of best theories | Design, curation, formal logic, standards bodies |
| Revision looks like | A philosophical position falls | A version bump (GO releases monthly; BFO 2020 succeeded BFO 2.0) |
| Characteristic failure | Being wrong | Being unusable — too vague to compute or too rigid to fit the domain |
| Exemplary artifact | Quine 1948; Aristotle's *Categories* | Gene Ontology; OWL; BFO; Cyc |

The table is clean; reality is not. BFO is engineering built by a philosopher making genuinely philosophical claims (that continuant/occurrent is a real joint, not a convenience). And Quine's criterion turns out to be a perfectly good *code-review tool* for schemas: look at what your system quantifies over, and that's what you've committed to. The next section does exactly that.

## 4. Worked example: three schemas, three worlds

Take one ordinary fact: *Alice and Bob got married on June 12, 2019.* You're designing a system that must store it. Here are three ways, in RDF Turtle syntax (each line is a triple: subject, predicate, object — read `:alice :marriedTo :bob` as "Alice is married to Bob"). You can paste any of these into a validator like the W3C's online RDF tools and they'll parse.

**Schema A — marriage as a relation:**

```turtle
:alice  :marriedTo  :bob .
```

**Schema B — marriage as an entity:**

```turtle
:m1  a            :Marriage ;
     :partner     :alice, :bob ;
     :startDate   "2019-06-12"^^xsd:date .
```

**Schema C — marriage as an event plus a state:**

```turtle
:w1  a          :WeddingEvent ;      # an occurrent — it happened, then ended
     :date      "2019-06-12"^^xsd:date .
:m1  a          :MarriageState ;     # a continuant — it persists
     :beganWith :w1 ;
     :partner   :alice, :bob .
```

All three store "the same fact." Now apply Quine's criterion — what does each quantify over?

Schema A's world contains two people and no marriage. There is no thing you can point to, date, count, or end; "married" is just a link. The moment your product manager asks "show marriages that lasted under five years," you're stuck: there is no marriage in your ontology to have a duration. Schema B's world contains a third object — the marriage itself, with properties of its own. Now duration queries are trivial, but you've committed to marriages being *things*, and you'll face the classic puzzles of things: if Alice and Bob divorce and remarry each other, is that one marriage or two? Your schema must answer; philosophy would call this an identity-conditions problem, and it's now a ticket in your backlog. Schema C splits the wedding (an event, over in a day) from the marriage (a state, persisting for years) — which is exactly BFO's occurrent/continuant distinction showing up in a customer database, and it's the only schema of the three that can cleanly say "the wedding was in Kyoto but the marriage is governed by California law."

Nobody in this story set out to do metaphysics. But the questions that decided between A, B, and C — is a marriage a thing? is an event the same kind of thing as a state? what makes two marriages two? — are ontological questions, full stop. The database schema is a small formal theory of a domain, and by Quine's own criterion its existence-claims are readable right off its quantifiers. This is what "AI systems force ontological choices" means at the smallest scale. Scale it up and you get the Gene Ontology's decision that functions, processes, and components are three different kinds of being — a decision now baked into six million annotations.

## 5. Why AI forces the question — twice

Symbolic AI forced it openly. Cyc, expert systems, the Semantic Web, every knowledge graph: these systems *are* declared ontologies plus inference, and their builders knew it. When your medical system must decide whether "diabetes" names a disease, a process, or a disposition, you are doing ontology with a compliance deadline. That's the first forcing, and it's forty years old — the [history-of-ai](history-of-ai.html) room covers how this whole program rose and receded.

Deep learning looked like an escape. A [neural network](neural-networks.html) is trained on raw text or pixels; nobody declares categories; the [machine-learning](machine-learning.html) pipeline never asks what exists. For a while it was possible to believe the ontological question had simply been dissolved — [deep-learning](deep-learning.html) systems would learn whatever structure they needed, and no human would have to legislate the world's joints.

That belief hasn't survived contact with the models. Three places the question re-enters:

**Inside the model.** [Mechanistic interpretability](mechanistic-interpretability.html) exists because a trained network clearly *has* internal structure — directions and circuits that behave like a concept of "the Golden Gate Bridge" or "deception" — and we want to know what that structure is. But every interpretability method smuggles in an ontology of the model itself: is the right unit a neuron, a linear direction, a circuit, a "feature"? Researchers who extract features with sparse autoencoders are making a Gruber-style move — an explicit specification of a conceptualization — over the model's activations. Whether those features are the model's real joints or artifacts of the tool is a live dispute, and it is *exactly* the realism-versus-convention dispute philosophy has hosted for centuries, replayed on new terrain. That's stated as fact about the dispute existing; which side is right is open.

**At the interface.** When a [frontier model](leading-models.html) answers questions, retrieves from a knowledge graph, calls tools, or fills a JSON schema, someone chose the entity types. Structured output is a declared ontology; the model is forced into it token by token. The industry's practical stack — LLM for language, knowledge graph for facts — is a running negotiation between learned structure and declared structure, "things, not strings" all the way down.

**In the training data.** A model trained on human text inherits the categories human text uses — including their disagreements. Whether large models thereby *have* an ontology in any strong sense is a hypothesis, not a fact. The deflationary reading — the model has statistical structure that mimics categorical structure, and "ontology" is our projection — deserves the floor first, and it may be the whole story. The stronger reading — that training discovers real joints in the world because those joints are what makes text predictable — is defensible but unproven. Wilder still, and worth holding loosely: if two very different systems (say, a human scientific community and a large model) keep converging on the same categories, that convergence is *evidence about the world*, a probe for which joints are really there. Nobody has built that instrument carefully yet.

The honest summary: AI did not inherit ontology as a quaint philosophical decoration. It re-derived the problem twice — once by building explicit ontologies and hitting their limits, once by avoiding them and finding the question waiting inside the weights.

## 6. What you can do now

You can hear the word "ontology" and know which life it's living: the singular truth-seeking discipline or the countable engineered artifact. You can apply Quine's criterion as a working tool — read any schema, prompt template, or API contract and say precisely what it commits its users to existing. You can look at a design choice like marriage-as-relation versus marriage-as-entity and recognize it as a metaphysical decision with a version number. And you can watch the current fight over what a "feature" is inside a transformer and recognize it as the oldest question in the building, wearing a lab coat.

From here: [mechanistic-interpretability](mechanistic-interpretability.html) is where the ontology-of-the-model question gets its tools; [what-self-means](what-self-means.html) and [sense-of-self](sense-of-self.html) take the hardest single ontological question — what a self is — from both the [contemplative](ai-and-the-traditions.html) and mechanistic sides; [geb](geb.html) and [hofstadter](hofstadter.html) hold the strange-loop answer; [teleology](teleology.html) asks the sibling question — not what exists, but what things are *for*; and [cybernetics](cybernetics.html) is where "system" itself got its modern definition.

One more thing, because this is where the domain itself points. Every ontology in this room — Aristotle's categories, Quine's quantifiers, the Gene Ontology, the features in a sparse autoencoder — is a record of where some mind's attention found a stable joint and stayed. Categories are frozen attention: the marks left where noticing repeated until it hardened into a kind. That's not mysticism; it's visible in the artifacts. GO's three domains are where biologists' attention reliably landed; BFO's continuants and occurrents are where a philosopher found everyone's attention already divided. So the discipline that asks "what exists?" keeps arriving, from inside its own method, at a prior question it never quite states: what is the thing that attends, that carves, that commits? Quine told us to read a theory's ontology off its variables. He didn't say what to make of the fact that there's always a reader.

## Open questions

**Established (FACT):** The two uses of "ontology" are both standardized and both precise — Quine's commitment criterion on the philosophy side; Gruber's definition, OWL's 2004/2009 W3C recommendations, and BFO's 2021 ISO standardization on the engineering side. Schema design decisions provably constrain what a system can represent and query. Trained networks contain non-random internal structure that interpretability methods can partially extract.

**Contested (HYPOTHESIS):** Whether features found by current interpretability tools are the model's real computational joints or artifacts of the extraction method. Whether large language models "have an ontology" in any sense stronger than statistical mimicry of human categories. Whether any top-level ontology (BFO or rival) captures genuine structure of reality versus a usefully standardized convention — the field's own realists and conventionalists disagree.

**Worth holding (WILD):** That convergence between independently built systems — human sciences, different model families, different cultures — could be turned into an actual instrument for detecting reality's joints, making ontology partly an experimental science. And that the recurring arrival of ontological inquiry at the nature of the inquirer is a structural feature of the problem rather than an accident of who's asking. Both are speculation, labeled as such.

## Sources

- Quine, W.V.O., ["On What There Is"](https://rintintin.colorado.edu/~vancecd/phil375/Quine.pdf), *Review of Metaphysics* 2 (1948).
- Hofweber, T., "Logic and Ontology," [*Stanford Encyclopedia of Philosophy*](https://plato.stanford.edu/entries/logic-ontology/) — the four-project division of ontology (O1–O4) and Quine's quantificational criterion.
- Gruber, T., ["A Translation Approach to Portable Ontology Specifications"](https://tomgruber.org/writing/ontolingua-kaj-1993.pdf) (1993) and "Toward Principles for the Design of Ontologies Used for Knowledge Sharing," *Int. J. Human-Computer Studies* 43 (1995), 907–928; Gruber also gives the definition's history on his [author page](https://tomgruber.org/writing/definition-of-ontology).
- Ashburner, M., et al., ["Gene ontology: tool for the unification of biology"](https://doi.org/10.1038/75556), *Nature Genetics* 25 (2000), 25–29. The three domains and 2018-release counts come from the Gene Ontology Consortium's primary 2019 resource paper, ["20 years and still GOing strong"](https://academic.oup.com/nar/article/47/D1/D330/5160994); the consortium's current [ontology](https://geneontology.org/docs/ontology-documentation/) and [annotation](https://geneontology.org/docs/go-annotations/) documentation explains the maintained artifact.
- OWL dates, semantics, and computational tradeoffs: W3C's [OWL standards overview](https://www.w3.org/OWL/) and the [OWL 2 Recommendation overview](https://www.w3.org/TR/2009/REC-owl2-overview-20091027/).
- BFO's status and scope: [ISO/IEC 21838-2:2021](https://www.iso.org/standard/74572.html). CCO's eleven-ontology, BFO-based structure: [National Center for Ontological Research](https://ncor-network.org/wiki/ontologies/common-core-ontologies). The baseline decision is in the joint DoD/IC [2024 memorandum](https://dailynous.com/wp-content/uploads/2024/03/memo-dod-applied-ontology.pdf), which names BFO and CCO separately in a linked top- and mid-level stack.
- Cyc's founding, later scale, and cost figures are retained as claims reported in secondary histories, including the [Cyc overview](https://en.wikipedia.org/wiki/Cyc); the absence of a stable primary release ledger is why the article labels the exact figures unverified.
- Google Knowledge Graph: Google's original [2012 launch post](https://blog.google/products/search/introducing-knowledge-graph-things-not/) and its [2020 first-party account](https://blog.google/products-and-platforms/products/search/about-knowledge-graph-and-knowledge-panels/), which reports more than 500 billion facts about five billion entities.
- The coinage of "ontology" in the early 1600s and the content of Aristotle's *Categories* are standard history of philosophy, stated from general knowledge and not re-verified by live search for this draft. The claims about sparse-autoencoder features and the interpretability dispute summarize the public state of the field as of the author's knowledge; the dispute's existence is documented across the interpretability literature (see [top-papers-mi](top-papers-mi.html)).

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
