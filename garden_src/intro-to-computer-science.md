---
title: Intro to Computer Science
slug: intro-to-computer-science
series: foundations
tags: computation, abstraction, logic gates, turing machine, layers, foundations
summary: What computation actually is, starting from a physical switch and ending at the idea that makes the whole field learnable. A computer is a tower of layers, each one a machine built out of the layer below it, and meaning enters only at the top. Once you see that, every other room in this garden gets easier.
status: draft
date: 2026-08-25
terms_defined: computation, abstraction layer, bit, logic gate, turing machine, stored program
terms_linked: programming, compilers, algorithms-new-vision, semiconductors, nvidia-and-the-chip, chip-wars, neural-networks, machine-learning, mechanistic-interpretability, geb, aunt-hillary
---

# Intro to Computer Science

This is the first room of the foundations series. Everything else in the garden — [programming](programming.html), [compilers](compilers.html), [neural networks](neural-networks.html), the [chips](semiconductors.html) all of it runs on — sits on top of what this room builds. You need no background. If you can follow a light switch, you can follow this.

## 1. Start with a switch

Here is the whole field in one object: a switch that another switch can flip.

A light switch on your wall is a switch a *finger* flips. Boring. But in 1937, a 21-year-old MIT master's student named Claude Shannon was working with relays — switches flipped not by fingers but by electric current. Current flows into the relay's coil, a small electromagnet pulls a metal arm, and a *second* circuit closes. A switch controlling a switch.

Shannon noticed something that now looks obvious and then looked like nothing at all: circuits of these relays obey the same algebra that the logician George Boole had worked out in the 1850s for *true* and *false*. Wire two relays in series and the output circuit closes only if the first is on AND the second is on. Wire them in parallel and it closes if the first is on OR the second is on. Add a relay arranged to open when its input closes, and you have NOT. Shannon's thesis, "A Symbolic Analysis of Relay and Switching Circuits" (submitted August 1937, published 1938), showed the two systems are the same system: any expression in Boolean logic can be built as a circuit, and any relay circuit can be analyzed as logic. It has been called the most important master's thesis of the twentieth century, and for once the superlative is defensible.

Why does this matter so much? Because logic is something you can *stack*. The output of one logical expression can be the input of another, and another, without limit. The moment circuits became logic, circuits inherited that stackability. That is the seed of everything.

Today the switch is not a relay but a transistor — a sliver of silicon that conducts or doesn't depending on a voltage at its gate, no moving parts, switching billions of times per second. The transistor was demonstrated at Bell Labs in December 1947. Intel's first microprocessor, the 4004 in 1971, had 2,300 of them. Apple's M3 Ultra, released March 2025, has 184 billion. The switch got small and fast beyond metaphor. It never got smarter. It is still just a switch a switch can flip.

## 2. Bits: the honest name for what a computer holds

A **bit** is one switch's worth of state: on or off, written 1 or 0. That's the entire definition. Not "a tiny piece of information" — a bit has no meaning in itself, and this point is load-bearing for the whole room.

Take the pattern `01000001`. Eight bits. What is it?

- Read as a binary number: 65.
- Read as text in the ASCII convention: the letter `A`.
- Read as a machine instruction in legacy 32-bit x86 mode: `inc ecx` — "add one to a counter." In x86-64 long mode, the same byte is instead a REX.B prefix.
- Read as part of an image: a fairly dark gray pixel.

Same switches, same voltages. The pattern doesn't "contain" any of these meanings. The meaning lives entirely in the convention the *reader* of the bits applies — and inside a computer, the reader is always some other circuit, which is itself just switches. Hold onto that. It comes back at the end of this room, and it is one of the deepest facts in the field.

## 3. From switches to arithmetic: nobody in the chip knows math

Logic gates are the standard packaging of Shannon's insight. A **logic gate** is a small transistor circuit implementing one Boolean operation: AND outputs 1 only if both inputs are 1; OR outputs 1 if either is; NOT flips its input.

One gate deserves special attention: NAND — "not-and," outputting 0 only when both inputs are 1. NAND is *universal*: every other gate, and therefore every digital circuit that exists or could exist, can be built from NANDs alone. (Logicians knew a single operation could generate all of logic before the hardware existed — Henry Sheffer published the result in 1913, and Charles Peirce had it decades earlier in unpublished work.) A modern chip is, with no exaggeration, a few hundred billion arrangements of roughly one idea.

Now watch arithmetic fall out of logic, because you can verify this yourself with a pencil. Binary addition of two one-bit numbers has four cases: 0+0=0, 0+1=1, 1+0=1, and 1+1=10 (that's "two" in binary: sum digit 0, carry 1). Look at the two output columns:

- The **sum** digit is 1 when exactly one input is 1. That's a gate called XOR (exclusive-or).
- The **carry** digit is 1 only when both inputs are 1. That's AND.

So two gates wired to the same pair of inputs form a *half adder*: a circuit that adds. Chain these (with a small extension to accept an incoming carry, called a full adder) 64 times and you have the 64-bit adder inside every processor on earth.

Notice what did *not* happen. No component understands addition. XOR doesn't know it's computing a sum digit; it's transistors passing voltage. Arithmetic isn't *in* the circuit — arithmetic is a description that is true *of* the circuit, at a level above it. This pattern — dumb parts below, real behavior describable only at the level above — is the single most repeated structure in computing, and you have now seen it with your own eyes at the bottom of the stack.

## 4. Turing: computation was defined before computers existed

Here is a fact with a date, and the date is the surprise: computation's core formal model and some of its central limits were established in 1936 — a decade before the first general-purpose electronic computers ran.

Alan Turing's paper "On Computable Numbers, with an Application to the Entscheidungsproblem" was submitted to the London Mathematical Society on 28 May 1936 and published that November and December. Turing was answering a question in pure logic (whether mathematics admits a mechanical procedure for deciding every statement — it doesn't), and to answer it he had to pin down what "mechanical procedure" *means*. His answer, now called the **Turing machine**, is almost insultingly simple: an unbounded tape of symbols, a head that reads and writes one symbol at a time, a finite set of internal states, and a fixed table of rules — "in state 3 reading a 1: write 0, move left, enter state 7."

That's it. State plus rules plus memory. Turing argued this captures anything a human following explicit instructions could ever do, and ninety years of trying has produced no counterexample: every programming language, every chip, every [neural network](neural-networks.html) running on ordinary hardware computes exactly the class of things a Turing machine computes. Faster, never *more*. This claim — that Turing's definition captures everything we'd intuitively call computation — is called the Church–Turing thesis, and note the word: *thesis*, not theorem. It's a claim about the informal notion of "computable," so it can't be proven, only endlessly survived. So far it has endlessly survived.

Turing's paper contains a second idea, and this one built the industry. Among all possible machine tables, there is a *universal* one: a machine that reads the description of any other machine from its own tape and then behaves as that machine. One hardware design, infinitely many behaviors, selected by what you feed it. A program, in other words, is data. The machine that runs Fortnite and the machine that runs a spreadsheet are the same machine holding different bits.

That is the **stored program** idea, and it's why your phone is not a phone. It's a universal machine currently *pretending* to be a phone, and will pretend to be a piano, a map, or a darkroom the moment you load different bit patterns into its memory. Once you see this, the software industry stops being mysterious: hardware is built once; everything else is arranging bits.

## 5. Why layers exist: the tower

So we have switches at the bottom and, somehow, video calls at the top. The distance between those two is not crossed by cleverness. It is crossed by **abstraction layers**, and this section is the room's center.

An abstraction layer is a deal with two clauses: *I provide you a clean, simple behavior. You don't look at how.* The adder from section 3 already made this deal — "give me two numbers, I return their sum; ignore the transistors." Computing is that deal, made maybe a dozen times in a stack:

| Layer | What it is | Its promise to the layer above | Who works here |
|---|---|---|---|
| Physics | Electrons in doped silicon | Voltage in this range = reliably distinguishable states | Physicists, [fab engineers](semiconductors.html) |
| Transistor | A voltage-controlled switch | Clean on/off, billions of times a second | Device engineers |
| Logic gate | A few transistors | AND / OR / NOT / NAND, exactly | Circuit designers |
| Circuit | Thousands of gates | Add, compare, store, select | Hardware architects |
| Processor & ISA | Billions of transistors behind a fixed instruction vocabulary | "I execute these ~1,000 documented instructions, in order, forever" | [Chip companies](nvidia-and-the-chip.html) |
| Machine code / assembly | Bit patterns naming instructions | A program the silicon directly runs | Compiler writers, rare humans |
| High-level language | Python, C, Rust | "Say `x = 2 + 3`; I handle everything below" | [Programmers](programming.html) |
| [Algorithm](algorithms-new-vision.html) | A method, independent of language | "This procedure sorts / searches / routes, provably" | Computer scientists |
| Application | The spreadsheet, the browser, the model | "Tap here" | Everyone |

Two things about this tower are true at once, and both matter.

First: **the layers are honest**. Each one really does hide the one below. The [compiler](compilers.html) translating your Python has no model of transistor physics. The person who designed the adder never met the person who wrote your browser, and neither needed the other's knowledge. This is why the tower could be built by millions of people across eighty years, no one of whom understood all of it. Layering isn't an engineering convenience; it's the only known way to build something this large out of human-sized understandings. A person can hold one layer and its two interfaces. Nobody holds the tower.

Second: **the layers are a fiction the layer below continuously maintains**. There is no addition in the chip, no Python in the memory, no image on the disk — there are only switch states, all the way down, and each layer's clean behavior is a hard-won engineering achievement of the layer beneath, not a fact of nature. Mostly you may ignore this. When things break badly — a chip's arithmetic bug, a cosmic ray flipping a bit, an exploit that talks to the memory hardware directly, sidestepping every software layer's assumptions — the fiction tears, and whoever fixes it must climb down the tower in person.

The tower is still growing at both ends. At the bottom, TSMC moved its 2-nanometer-class process into volume production in late 2025, with capacity through 2026 essentially sold out — the switches are still shrinking, though the [economics and geopolitics of that shrinking](chip-wars.html) now shape world politics. At the top, [machine learning](machine-learning.html) has added a genuinely new kind of layer: one whose behavior is trained rather than specified, which is why a new field — [mechanistic interpretability](mechanistic-interpretability.html) — had to be invented just to read what's inside it.

## 6. The one mental model

Everything above compresses into a sentence you can carry for the rest of your life:

**A computer is a tower of layers. Each layer is a machine built out of the layer below. Meaning is never in a layer — it is always assigned from the layer above. And you only ever need to learn one layer at a time.**

The last clause is the practical superpower, so let's make it operational. Whenever you meet anything new in computing — a tool, a language, an error, a buzzword — ask three questions:

1. **What layer is this on?** (Is Docker a chip thing, a language thing, an operating-system thing? Finding the shelf is half the understanding.)
2. **What does the layer below promise it?** (What is it allowed to assume just works?)
3. **What does it promise the layer above?** (What is its own interface — the clean fiction it maintains?)

Confusion in computing is almost always *layer* confusion — an explanation pitched at the wrong floor of the tower, or two floors silently mixed. The beginner who asks "but how does the computer *know* that `if` means if?" is asking a real question whose answer is "it doesn't — a [compiler](compilers.html) translated your `if` into compare-and-jump instructions, and 'knowing' was never involved at any layer." Once you have the tower, you can place every explanation you'll ever hear, notice what it's hiding, and decide whether the hidden part matters for you today. That is what makes the whole field learnable: not that it's simple, but that it was *built by people who could each only learn one layer at a time*, and the seams they left are the handholds you climb with.

## 7. Worked example: ride `2 + 3` down the tower

Let's trace one addition all the way down. You can verify the top layers yourself right now on any Mac or Linux machine.

**Layer: high-level language.** Open a terminal and run:

```
python3 -c "print(2 + 3)"
```

You get `5`. One line of Python. Now let's see under it.

**Layer: bytecode.** Python first compiles your line into instructions for a simpler internal machine. Ask to see them:

```
python3 -c "import dis; dis.dis(compile('2 + 3', '', 'eval'))"
```

You'll see the constant `5` being returned directly (`LOAD_CONST 5` then `RETURN_VALUE` on older Pythons, `RETURN_CONST 5` on 3.12+) — the compiler noticed both numbers were constants and did the addition at compile time. Foil it by making one a variable:

```
python3 -c "import dis; dis.dis(compile('a = 2\nb = a + 3', '', 'exec'))"
```

Now you'll see the machinery: `LOAD_NAME a`, `LOAD_CONST 3`, an add opcode (`BINARY_ADD`, or `BINARY_OP +` on newer Pythons), `STORE_NAME b`. Your one `+` became load-load-operate-store — the universal rhythm of machine computation: fetch operands, apply operation, put the result somewhere.

**Layer: machine code.** The Python interpreter executing `BINARY_OP` is itself a program, written in C, compiled to your processor's instruction set. Somewhere in it, an actual add instruction runs — `add x0, x1, x2` on the ARM chip in a modern Mac. That instruction is a bit pattern in memory, maybe 32 switches wide, and the stored-program idea from section 4 is now literal: your program is sitting *in memory as bits*, being read by the processor the way the universal machine reads its tape.

**Layer: circuit.** The processor routes the two operands — `2` is `0010`, `3` is `0011`, padded to 64 bits — into its adder: the chained full adders from section 3. XOR gates produce sum digits, AND gates produce carries, the carries ripple (real chips use cleverer, faster carry circuits, but the logic is the same), and out comes `0101`. Five. Check the bottom two bits by hand with the rules from section 3: rightmost column 0+1 → sum 1, no carry; next column 1+1 → sum 0, carry 1; carry lands in the third column. `101`. It works on paper because the paper and the silicon are running the same Boolean algebra — Shannon's equivalence, live.

**Layer: transistors and physics.** Each of those gates is a handful of transistors; each transistor either lets charge through or doesn't, according to the voltage on its gate — the switch flipped by a switch, a few nanometers wide now, doing what the relay did in 1937.

The hardware addition itself takes far less than a millisecond. The end-to-end command does not: launching Python and printing to a terminal usually takes milliseconds to tens of milliseconds, depending on the machine and environment. Number of layers that "understood addition": zero. Number of layers that had to work exactly as promised: all of them.

For scale — ENIAC, the room-sized machine unveiled in February 1946 with roughly 17,500 vacuum tubes, managed about 5,000 additions per second and drew around 174 kilowatts. The phone in your pocket does billions of additions per second per core, on milliwatts, because the tower let eighty years of improvements at every layer multiply together without anyone coordinating them.

## 8. Conclusion: what you can now see

You can now do something most people around you cannot: place any piece of computing on its layer. You know what a bit honestly is (a switch, meaning assigned from above), why arithmetic needs no arithmetic in it, why one machine can be every machine (Turing, 1936), and why the field is learnable at all (one layer at a time, against its interfaces). When you hit something confusing in later rooms, come back to the three questions in section 6 — they don't stop working.

From here the foundations series fans out: [programming](programming.html) is life on the high-level-language layer; [compilers](compilers.html) is the layer-crossing machinery itself, the translators that maintain the fictions; [algorithms](algorithms-new-vision.html) is what remains of a program when you abstract away *every* layer; [semiconductors](semiconductors.html) and [nvidia-and-the-chip](nvidia-and-the-chip.html) go down the tower into the physics and the business of the switch; and [neural networks](neural-networks.html) begins the strange new wing of the tower where the top layer is grown rather than written.

One thread from this room runs further than the rest. You saw, at the bottom of the stack, that addition is not in the adder — it is a description true of the adder from one level up, and the meaning of every bit pattern lives in its reader, which is always more switches. [Hofstadter](geb.html) built a whole book around what happens when that pattern — dumb parts, real behavior one level up — stacks high enough to describe *itself*, and his [ant colony](aunt-hillary.html) chapter is the friendliest door into it. The question is not idle anymore: we now have systems at the top of the tower whose inner layers nobody wrote, and a field — [mechanistic interpretability](mechanistic-interpretability.html) — climbing down into them to find where, if anywhere, the meaning sits. Every layer we've examined turned out to be switches wearing a description. What a description would have to be *of*, for there to be someone home reading it — that question the tower does not answer. It only sharpens it.

## 9. Open questions

The honest state of the field, typed plainly:

- Established fact: universality is real mathematics. The universal machine, the equivalence of every proposed general model of computation so far (Turing machines, lambda calculus, ordinary programming languages), and the existence of problems no program can solve (Turing proved the first in the same 1936 paper) are theorems, not opinions.
- Established fact: the layers are physically real engineering, not metaphor — you can buy any layer of the tower separately, from raw wafers to cloud APIs.
- Hypothesis, strongly held but unprovable in principle: the Church–Turing thesis. Everything physically buildable so far computes within Turing's limits, but "computable" as an informal notion can't be captured in a proof. Quantum computers, for the record, do not break it — they change what's *fast*, not what's *possible*.
- Hypothesis, contested: whether physical reality permits any process that outruns Turing computability ("hypercomputation"). No credible candidate has survived scrutiny; the question is not closed, merely undefeated.
- Speculation worth holding loosely: pancomputationalism — the claim that the universe itself *is* a computation. It's a live philosophical position with serious defenders and serious critics, and nothing in this room requires you to take a side. Notice only that the claim inherits this room's central lesson: calling something a computation requires saying who's assigning the meaning.

## Sources

- Claude Shannon, "A Symbolic Analysis of Relay and Switching Circuits," MIT master's thesis, submitted August 1937, published 1938. Thesis dates verified via [History of Information](https://www.historyofinformation.com/detail.php?id=622) and the [Wikipedia article on the thesis](https://en.wikipedia.org/wiki/A_Symbolic_Analysis_of_Relay_and_Switching_Circuits).
- Alan Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem," Proceedings of the London Mathematical Society; received 28 May 1936, published November–December 1936. Dates verified against the [scanned paper](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf) and [History of Information](https://www.historyofinformation.com/detail.php?id=619).
- ENIAC figures (≈17,500 vacuum tubes, ~5,000 additions/second, ~174 kW, February 1946 unveiling): [Britannica](https://www.britannica.com/technology/ENIAC) and the [Computer History Museum](https://www.computerhistory.org/revolution/birth-of-the-computer/4/78). Sources vary slightly on the tube count (17,000–17,468); the number here is rounded accordingly.
- Apple M3 Ultra, 184 billion transistors, released March 2025: [Apple Newsroom](https://www.apple.com/newsroom/2025/03/apple-reveals-m3-ultra-taking-apple-silicon-to-a-new-extreme/).
- TSMC 2nm-class (N2) volume production beginning Q4 2025, 2026 capacity effectively booked out: [Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-begins-quietly-volume-production-of-2nm-class-chips-first-gaa-transistor-for-tsmc-claims-up-to-15-percent-improvement-at-iso-power) and [Data Center Dynamics](https://www.datacenterdynamics.com/en/news/tsmc-secures-15-customers-for-its-2nm-technology-majority-in-hpc-space/).
- Stable historical facts stated from standard references and not separately live-verified: transistor demonstrated at Bell Labs, December 1947; Intel 4004 (1971, ~2,300 transistors); Sheffer's 1913 publication of NAND-universality with Peirce's unpublished precedence; Boole's laws of thought (1850s). These are settled history; if any is wrong, the error is the author's and will be corrected on this page, dated.
- The Python bytecode traces in section 7 are directly runnable and were executed and verified on CPython 3.9.6 while writing this room; opcode names vary slightly by version as noted inline — the layer lesson is unchanged.

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
