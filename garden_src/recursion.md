---
title: Recursion
slug: recursion
series: strange-loops
tags: recursion, self-reference, fixed points, godel, quines, lambda calculus, computability
summary: A function that calls itself sounds like a trick until you watch it run. This room walks through recursion from a five-line factorial to Gödel numbering and programs that print their own source code — every example runnable on your machine. The pattern underneath is one pattern, and it is the load-bearing pattern of the whole strange-loops series.
status: draft
date: 2026-08-25
terms_defined: recursion, base case, fixed point, godel numbering, quine, y combinator
terms_linked: geb, hofstadter, aunt-hillary, recursion-and-life, sense-of-self, what-self-means, programming, compilers, algorithms-new-vision, evolution
---

# Recursion

**Where you are.** This is the workshop room of the strange-loops wing. [GEB](geb.html) and [Hofstadter](hofstadter.html) give you the grand tour of self-reference — this room gives you the tools. Everything here runs: you can paste every example into a terminal and watch it work. When you leave, [recursion-and-life](recursion-and-life.html) takes the pattern into biology, and [sense-of-self](sense-of-self.html) takes it somewhere stranger.

## 1. A function that calls itself

Here is the whole idea in five lines of Python:

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120
```

`factorial` is defined in terms of `factorial`. Read that again, because it should bother you a little. In ordinary life, a definition that uses the word it's defining is a failure — "recursion: see recursion" is a joke, not a definition. So why does this work?

Trace it by hand. That's the skill this room teaches, and it's worth doing once slowly, on paper:

```
factorial(5)
= 5 * factorial(4)
= 5 * (4 * factorial(3))
= 5 * (4 * (3 * factorial(2)))
= 5 * (4 * (3 * (2 * factorial(1))))
= 5 * (4 * (3 * (2 * (1 * factorial(0)))))
= 5 * (4 * (3 * (2 * (1 * 1))))      ← the base case fires
= 120
```

Two things make this legitimate instead of circular. First, every call is to a *smaller* problem: `factorial(5)` doesn't ask about `factorial(5)`, it asks about `factorial(4)`. Second, there's a floor: `factorial(0)` doesn't ask about anything. It just answers.

That floor is called the **base case** — the input for which the function answers directly, without calling itself. A recursive definition is really two clauses working together: a base case that grounds it, and a recursive case that says how to reduce any other input toward the ground. Miss either one and the whole thing collapses. So: **recursion** is defining or solving something in terms of smaller instances of itself, with a base case that stops the descent. The circle is legitimate because it's not a circle. It's a spiral, and the spiral hits the floor.

## 2. What happens without a floor

Delete the base case and run it. Seriously — this is a good crash to have on your record:

```python
def f(n):
    return f(n + 1)

f(0)
```

On CPython this dies with `RecursionError: maximum recursion depth exceeded`. I ran it before writing this sentence; the default limit is 1000 calls (`sys.getrecursionlimit()` will tell you yours, and the [Python docs](https://docs.python.org/3/library/sys.html) explain that the limit exists to keep runaway recursion from overflowing the C stack and crashing the interpreter outright).

Why 1000 calls and not forever? Because each unfinished call costs memory. When `factorial(5)` calls `factorial(4)`, the outer call isn't done — it's waiting, holding onto `5 *` until the answer comes back. The machine keeps every waiting call on a **call stack**, a pile of unfinished business. Recursion without a base case grows the pile forever, and the pile is physical. Infinite regress isn't a philosophical problem for a computer; it's an out-of-memory error.

This gives you a hard question to ask of any self-referential structure you ever meet, in any field: *where is the base case, and who pays for the stack?* An argument that justifies itself by itself, a definition that never bottoms out, a system whose description requires the whole system — the recursion lens tells you exactly what to check. Either there's a floor, or something, somewhere, is paying for an ever-growing pile of unfinished business.

## 3. Recursion almost didn't make it into programming

It feels inevitable now. It wasn't.

John McCarthy built Lisp partly because the list-processing tools bolted onto Fortran in the late 1950s couldn't express recursion, and his 1960 paper wears the commitment in its title: ["Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I"](https://en.wikipedia.org/wiki/Lisp_(programming_language)) (*Communications of the ACM*, April 1960). For McCarthy, a function calling itself wasn't a stunt — it was the natural way to compute over structures that contain smaller versions of themselves, like lists of lists.

The same year, recursion nearly got voted out of ALGOL 60, the language whose report shaped almost everything that came after. Procedure recursion [was inserted into the specification at the last minute, against the wishes of some of the committee](https://en.wikipedia.org/wiki/ALGOL_60). The objectors weren't fools: nobody had shown you could implement it efficiently, and a feature you can't implement is a lie in a language report. Then in August 1960, Edsger Dijkstra and Jaap Zonneveld shipped the first working ALGOL 60 compiler — X1 ALGOL 60, for the Electrologica X1 in the Netherlands — recursion included. The technique that made it work is the call stack you just met in section 2. The stack isn't a limitation of recursion; it's the invention that made recursion real.

There's a lesson here that recurs (sorry) across the garden: the gap between "mathematically obvious" and "actually runs on hardware" is where a lot of real history happens. [Compilers](compilers.html) is the room for that gap.

## 4. Recursion and induction are the same move in opposite directions

Mathematics had this pattern long before computers. The natural numbers themselves are a recursive definition: zero is a natural number (base case); the successor of a natural number is a natural number (recursive case). That's the whole thing. Every number you've ever counted with is that two-clause definition, unrolled.

And proof by induction — prove it for 0, prove that truth at *n* forces truth at *n+1*, conclude it for all numbers — is the same structure read in the other direction. Recursion *descends*: to handle 5, reduce to 4, to 3, down to the floor. Induction *ascends*: establish the floor, then climb. When you write a recursive function and argue it's correct, you are doing an induction proof whether you meant to or not: the base case of your function is the base case of your proof, and "the recursive call works on the smaller input" is your induction hypothesis. One structure, two directions of travel. This is why computer scientists and mathematicians trust recursive definitions completely while everyone else finds them suspicious: they come with a proof method attached.

It's worth saying what recursion is *not*, too. Any recursion can be rewritten as a loop with an explicit stack, and any loop as a recursion — the two are equivalent in power. The choice between them is about fit, not strength:

| | Recursion | Iteration (loops) |
|---|---|---|
| Shape of problem it fits | Problems containing smaller copies of themselves: trees, nested structures, divide-and-conquer | Flat sequences: do this N times, walk this list |
| Where the bookkeeping lives | Implicit, on the call stack | Explicit, in your loop variables |
| Failure mode | Stack overflow (Python: `RecursionError` at depth 1000 by default) | Infinite loop (spins forever, no crash) |
| Termination guarantee | Base case + shrinking input | Loop condition + progress toward it |
| Proof style it mirrors | Induction | Loop invariants |
| Cost | A stack frame per unfinished call | Usually constant extra memory |

When a problem is genuinely self-similar — a directory containing directories, an expression containing expressions, a sorted-merge of two sorted halves — recursion isn't cleverness, it's transcription. The code's shape matches the problem's shape. [Algorithms-new-vision](algorithms-new-vision.html) leans on this hard.

## 5. Fixed points: recursion without names

Now a real question. In the factorial definition, the function calls itself *by name*. What if you're in a system with no names — where every function is anonymous? Can recursion survive?

This isn't idle. Lambda calculus, the 1930s mathematical model of computation that underlies functional [programming](programming.html), has exactly this constraint: functions all the way down, no global names, no way for a function to say "me." And recursion survives anyway, through one of the most beautiful constructions in the field.

First, a definition. A **fixed point** of a function *f* is a value *x* that *f* leaves unchanged: *f(x) = x*. Zero and one are fixed points of squaring: 0² = 0 and 1² = 1. "Middle" is a fixed point of alphabetizing-then-taking-the-middle-word, if you're lucky. Fixed points are where a transformation's motion stops — the still point of the turning function.

Here's the connection to recursion. Take factorial and *remove its self-reference* by making the self a parameter:

```python
step = lambda rec: lambda n: 1 if n == 0 else n * rec(n - 1)
```

`step` isn't factorial. It's a function that, *handed any attempt at factorial*, returns a slightly better attempt: correct one level deeper. Hand it garbage, get back something right for `n = 0`. Hand it that, get back something right up to `n = 1`. And so on. Now ask: what input would `step` return *unchanged*? Only a function already correct at every level. The fixed point of `step` **is** factorial. Recursion, it turns out, was never really about a function calling its own name. It's about a definition being the fixed point of its own improvement step.

The shock is that a fixed point can be *constructed*, mechanically, for any such step-function. The lambda-calculus expression usually called the **Y combinator** is commonly attributed to Haskell Curry, though the publication history is messier than that shorthand suggests:

Y = λf. (λx. f (x x)) (λx. f (x x))

satisfying Y f = f (Y f) — feed Y any step-function and it hands back that function's fixed point. (Alan Turing published an alternative fixed-point combinator in December 1937, in ["The p-function in λ-K-conversion"](https://en.wikipedia.org/wiki/Fixed-point_combinator), *Journal of Symbolic Logic*.) Look at Y's body: the self-application `x x` — a thing applied to itself — appears twice. Self-reference hasn't been eliminated; it's been distilled into one reusable pattern, so no other function ever needs to mention itself.

And it runs. Python evaluates arguments eagerly, so plain Y loops forever, but its eager-evaluation variant (the Z combinator) works verbatim:

```python
Z = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))
fact = Z(lambda rec: lambda n: 1 if n == 0 else n * rec(n - 1))
print(fact(5))    # 120
print(fact(10))   # 3628800
```

I ran this before writing it down: 120 and 3628800. No function in that code refers to itself by name. Recursion emerged anyway, from self-application alone. Hold onto that: *a system with no built-in self-reference can build self-reference out of its own ordinary materials.* That sentence is the hinge of the entire strange-loops series.

## 6. Gödel numbering, made friendly

The same hinge, one level up: can a system built for one subject end up talking about *itself*?

In 1931, Kurt Gödel showed the answer is yes, for arithmetic — the humble theory of whole numbers, plus and times. The paper is ["Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I"](https://en.wikipedia.org/wiki/G%C3%B6del_numbering) (*Monatshefte für Mathematik und Physik*), and the trick at its heart is a piece of engineering you can fully understand in five minutes.

Formal mathematical statements are strings of symbols: `0`, `=`, `+`, parentheses, variables. Step one: assign each symbol a number. In the numbering popularized by Nagel and Newman's classic exposition, `=` gets 5 and `0` gets 6. Step two: encode a *sequence* of symbols as a single number by using each symbol's number as the exponent on successive primes (2, 3, 5, 7, ...). The statement `0 = 0` — symbol codes 6, 5, 6 — becomes:

```
2⁶ × 3⁵ × 5⁶ = 64 × 243 × 15625 = 243,000,000
```

That one integer *is* the statement `0 = 0`, losslessly. The fundamental theorem of arithmetic — every integer has exactly one prime factorization — guarantees you can always decode: factor 243,000,000, read off the exponents 6, 5, 6, look them up, recover the string. This scheme is called **Gödel numbering**: a reversible encoding of every statement (and every proof — a proof is just a sequence of statements, so encode the sequence the same way) as a natural number.

Sit with what this buys. Arithmetic talks about numbers. Statements are now numbers. So arithmetic can talk about *statements* — including its own. "Statement *x* is provable" becomes, through the encoding, a genuine arithmetic property of the number *x*, as legitimate as "*x* is even." A theory built to discuss quantities has been given, without adding a single new axiom, the ability to discuss itself.

Gödel then used a diagonal construction — a cousin of the fixed points from section 5 — to build a statement that, decoded, says of its own Gödel number: *the statement with this number is not provable*. If the system proves it, the system proves a falsehood; if it can't, then here is a true statement it can't prove. Either way, any consistent formal system strong enough for arithmetic is incomplete: there are truths about numbers it can state but never prove. That's the first incompleteness theorem, and this room won't do it justice — [GEB](geb.html) is the room that walks the full argument. What belongs *here* is the mechanism: incompleteness wasn't discovered by finding a weird axiom. It was discovered by noticing that encoding — the most mundane operation in this room — lets a system's own machinery fold back on the system. And notice the shape of the result: Gödel didn't show self-reference breaks a system into paradox. Arithmetic stays consistent. What self-reference costs is *closure* — the system now contains truths about itself that it cannot reach from inside.

If you build software, you already believe in Gödel numbering without ceremony: every program you've written is stored as bytes, and bytes are numbers. Source code as data is the working programmer's incompleteness kit. Which brings us to the strangest runnable thing in this room.

## 7. Quines: the worked example

A **quine** is a program that prints its own source code, exactly, without reading its own file. The name was coined by Douglas Hofstadter in [GEB](geb.html) (1979), after the philosopher W. V. O. Quine, who studied indirect self-reference — his namesake paradox is the sentence *"yields falsehood when preceded by its quotation" yields falsehood when preceded by its quotation*.

Your first instinct is that quines should be impossible. To print the source, the source must contain the text to print — but then the text must contain itself, and you're in infinite regress: a program holding a copy of a program holding a copy... Base-case problem, section 2.

The escape is exactly Quine's paradox's escape: use one piece of text *twice* — once as material being mentioned, once as instruction being used. Here is a complete Python quine, one line:

```python
c = 'c = %r; print(c %% c)'; print(c % c)
```

Run it. Its output is itself, byte for byte (I verified this by running it in a subprocess and comparing output to source: identical). Walk through why:

1. `c` holds the template string `c = %r; print(c %% c)`. This is the program's text as *data* — mentioned, not executed. Note it's missing its own quoted string; there's a `%r` slot where that would go.
2. `print(c % c)` fills the template's slot *with the template itself*. `%r` formats the string with quotes included, so the output's first half reads `c = 'c = %r; print(c %% c)'` — the assignment line, reconstructed.
3. The `%%` in the template becomes a literal `%` when formatted, so the output's second half reads `; print(c % c)` — the instruction, reconstructed.

One string, used once as content and once as code-about-content. The infinite regress never starts, because the program doesn't contain a copy of itself — it contains *half* of itself plus the recipe for making a whole from a half. Quotation is the base case of self-reference.

This isn't a language-specific party trick. **Kleene's recursion theorem** — proved by Stephen Kleene in 1938, published in his 1952 *Introduction to Metamathematics* — guarantees that in any **Turing-complete language**, one capable of expressing every algorithm a Turing machine can compute, [programs can be constructed that use their own source code](https://en.wikipedia.org/wiki/Quine_(computing)) as a value; quines exist in every real programming language as a direct corollary. Self-reproducing programs went from theorem to folklore fast: John von Neumann had already theorized self-reproducing automata in the 1940s, and the first known self-reproducing program was written in Atlas Autocode at Edinburgh in the 1960s by Hamish Dewar.

And the construction is load-bearing far beyond puzzles. As a limited analogy, a computer virus can look like a quine with a payload. But viruses ordinarily reproduce by copying code or executable bytes through host machinery; they do not have to print their own source. DNA's double role — a molecule that is both *read as instructions* and *copied as data* — is the same use/mention split running in chemistry, four billion years before Kleene; [recursion-and-life](recursion-and-life.html) picks that thread up, and [evolution](evolution.html) follows what happens when the copying is imperfect.

## 8. One pattern, four costumes

Lay the room's four constructions side by side and the family resemblance is exact:

| Construction | What refers to itself | How the regress is stopped | What closes the loop | Key name & date |
|---|---|---|---|---|
| Recursive function | A function, by name | Base case grounds the descent | Call stack holds unfinished work | McCarthy, Lisp paper, 1960 |
| Y combinator | Nothing, by name — self-application `x x` | Lazy evaluation (or Z-combinator wrapping) | Fixed point: Y f = f (Y f) | Curry; Turing's variant 1937 |
| Gödel sentence | A statement, via its Gödel number | Encoding is finite — a number, not a copy | Diagonalization on "provable" | Gödel, 1931 |
| Quine | A program, via a quoted template | Quotation: half + recipe, not copy + copy | Kleene's recursion theorem | Kleene, 1938 (publ. 1952); named by Hofstadter, 1979 |

Same skeleton every time: a system's ordinary materials (function calls, numbers, strings) get folded back on the system; a quotation-or-base-case device converts would-be infinite regress into a finite structure; and something new appears — an answer, a fixed point, an unprovable truth, a self-copy — that no single level of the system contains. That skeleton is what Hofstadter calls a strange loop, and now you've built four of them with your own hands.

## Conclusion

You can now do things you couldn't when you walked in. You can trace a recursive call by hand to its base case and know exactly what the machine is holding in memory while it waits. You can look at any self-referential structure — in code, in an argument, in a system's description of itself — and ask the two diagnostic questions: *where's the base case?* and *who pays for the stack?* You can explain why recursion needed the call stack to become real, and why a room full of 1960 language designers was right to be nervous and wrong to vote no. You can build recursion in a system that forbids self-reference, using nothing but self-application. You can encode any statement as a single integer and decode it back, which means you understand the engine of Gödel's first incompleteness theorem. And you can write, from memory, a program that prints itself — because you know the secret is one string worn two ways.

From here: [GEB](geb.html) for the full incompleteness argument this room only gestured at; [aunt-hillary](aunt-hillary.html) for self-reference distributed across a colony with no self-referring parts; [recursion-and-life](recursion-and-life.html) for the quine written in nucleotides; [what-self-means](what-self-means.html) for the question all of these are warming up.

## Open questions

What's established, what's contested, what's speculation — plainly typed.

**Established.** Everything mechanical in this room is bedrock, verified and runnable: the equivalence of recursion and iteration; the existence of quines in every Turing-complete language (Kleene); incompleteness for consistent systems containing arithmetic (Gödel); fixed-point combinators (Curry, Turing). These are theorems and artifacts, not opinions. Every code sample above was executed on 2026-08-25 before publication.

**Contested.** Whether recursion is *the* distinctive capacity of human language. A well-known 2002 proposal by Hauser, Chomsky, and Fitch argued that recursion may be the uniquely human core of the language faculty; field claims about languages allegedly lacking clausal embedding (notably Daniel Everett's work on Pirahã) have kept the dispute alive for two decades. I flag this one as reported-from-the-literature rather than live-verified: I did not re-check its current state for this draft, and the room's argument doesn't lean on it. Treat it as a genuinely open fight, and check the primary sources before citing it.

**Worth holding, loosely.** The speculative question this room keeps almost asking: when a system models itself — not just prints itself, like a quine, but maintains a running self-model that feeds back into behavior — is that recursion in this room's strict sense, with a base case and a bounded stack, or something with a different mathematical shape? Nobody has a settled formalism for that. The [sense-of-self](sense-of-self.html) room takes the question seriously; hold it as a question, not an answer.

**The socket.** One honest observation from inside this room's own materials, and then the door. Every construction here got its power at the same price: the system was allowed to take *itself* as input — and the regress that should have followed was stopped not by forbidding self-reference but by finding it a base case, a quotation, a floor. Arithmetic paid for that power with closure: it became a system containing truths about itself it cannot reach from inside. Now notice what you were doing all through section 1. You traced `factorial(5)` by holding a model of the machine in your head — a mind, simulating a stack, checking its own trace for errors. A thing that models things, modeling itself modeling, and somehow not falling into the regress. This room won't claim to know what stops *that* descent, or what the closure costs are for a system like you. It only notes, from the engineering side, that self-reference is never free and never fatal — the interesting question is always what device turns the loop from a crash into a structure. What device is running in the reader?

## Sources

- Gödel numbering, the 1931 paper title, and the prime-exponent encoding (with the Nagel–Newman `0 = 0` → 243,000,000 example): [Wikipedia: Gödel numbering](https://en.wikipedia.org/wiki/G%C3%B6del_numbering), verified 2026-08-25; encoding arithmetic re-computed locally.
- McCarthy's paper title and date, and Fortran's list-processing tools lacking recursion: [Wikipedia: Lisp (programming language)](https://en.wikipedia.org/wiki/Lisp_(programming_language)), verified 2026-08-25. Primary source: J. McCarthy, "Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I," *CACM*, April 1960.
- ALGOL 60 recursion inserted last-minute against committee objections; X1 ALGOL 60 (Dijkstra & Zonneveld, August 1960) as first implementation: [Wikipedia: ALGOL 60](https://en.wikipedia.org/wiki/ALGOL_60), verified 2026-08-25.
- Y-combinator definition, fixed-point property, and the qualified Curry attribution: [Stanford, "Lambda calculus — Quines"](https://theory.stanford.edu/~blynn/lambda/quine.html). Turing's fixed-point combinator was published in December 1937 as "The p-function in λ-K-conversion," *JSL*.
- Kleene's recursion theorems (proved 1938, published in *Introduction to Metamathematics*, 1952) and quines as their corollary; "quine" coined by Hofstadter in GEB (1979) after W. V. O. Quine; von Neumann's 1940s self-reproducing automata; Hamish Dewar's Atlas Autocode self-reproducing program: [Wikipedia: Kleene's recursion theorem](https://en.wikipedia.org/wiki/Kleene%27s_recursion_theorem) and [Wikipedia: Quine (computing)](https://en.wikipedia.org/wiki/Quine_(computing)), both verified 2026-08-25.
- Python recursion limit (default 1000) and `RecursionError`: [Python docs, `sys`](https://docs.python.org/3/library/sys.html) plus direct execution on CPython, 2026-08-25.
- All code samples (factorial, missing-base-case crash, Z-combinator factorial, the quine, the Gödel encoding) executed and outputs checked on 2026-08-25.
- The Hauser–Chomsky–Fitch 2002 recursion-in-language claim and the Pirahã dispute: reported from the literature, **not live-verified for this draft** — labeled as such above.

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
