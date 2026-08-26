---
title: Compilers — How Text Becomes a Machine
slug: compilers
series: foundations
tags: compilers, systems, llvm, gcc, programming-languages, foundations
summary: The full journey from source code to a running program — lexer, parser, intermediate representation, optimization, code generation, linking — traced with real commands and real outputs you can reproduce on your own machine. Ends with the strangest fact about compilers, which Ken Thompson pointed out in 1984 and nobody has fully escaped since.
status: draft
date: 2026-08-25
terms_defined: compiler, lexer, token, parser, abstract syntax tree, intermediate representation, SSA, optimization pass, code generation, register allocation, object file, linker, symbol
terms_linked: programming, intro-to-computer-science, algorithms-new-vision, neural-networks, machine-learning, deep-learning, mechanistic-interpretability, nvidia-and-the-chip, semiconductors, recursion, geb, optimization
---

# Compilers — How Text Becomes a Machine

If you've read [programming](programming.html), you've written text files and watched them do things. This room is about the machinery in between — the program that turns your text into the electrical patterns a processor can actually execute. It's one of the oldest solved-and-never-finished problems in [computer science](intro-to-computer-science.html), and it's worth learning properly, because almost every idea in it — layered representations, meaning-preserving transformation, lost source code — shows up again when we talk about [neural networks](neural-networks.html).

Everything below runs on an ordinary Mac (Apple clang 21, arm64). Every output shown is a real output, captured on 2026-08-25. You can reproduce all of it.

## 1. The whole trip in one command

Start with the smallest honest program:

```c
#include <stdio.h>

int square(int x) {
    return x * x;
}

int main(void) {
    printf("%d\n", square(12));
    return 0;
}
```

Save it as `sq.c` and run:

```
$ clang sq.c -o sq
$ ./sq
144
```

One command, and text became behavior. But that one command hides a pipeline of five or six distinct machines, each consuming the previous one's output. A compiler — the general name for a program that translates programs from one language to another, usually from a human-friendly language to machine code — is really a relay race:

**source text → tokens → syntax tree → intermediate representation → optimized IR → assembly → object file → linked executable**

The rest of this room walks that relay one leg at a time, with the actual baton visible at each handoff. The pedagogical rule here is the one good systems teaching always follows: look at the real artifact at every stage, not a diagram of it.

## 2. Lexing: from characters to tokens

The compiler's first problem is stupid-sounding and real: the file is just a sequence of characters. `int square(int x)` is thirty-odd bytes with no inherent structure. The **lexer** (or tokenizer) groups those characters into **tokens** — the words of the language: keywords, identifiers, operators, punctuation.

Clang will show you its actual token stream. Using a header-free version of just the `square` function:

```
$ clang -fsyntax-only -Xclang -dump-tokens square.c
int 'int'        [StartOfLine]   Loc=<square.c:1:1>
identifier 'square'  [LeadingSpace]  Loc=<square.c:1:5>
l_paren '('              Loc=<square.c:1:11>
int 'int'                Loc=<square.c:1:12>
identifier 'x'   [LeadingSpace]  Loc=<square.c:1:16>
r_paren ')'              Loc=<square.c:1:17>
l_brace '{'      [LeadingSpace]  Loc=<square.c:1:19>
return 'return'  [StartOfLine]   Loc=<square.c:2:5>
identifier 'x'   [LeadingSpace]  Loc=<square.c:2:12>
star '*'         [LeadingSpace]  Loc=<square.c:2:14>
identifier 'x'   [LeadingSpace]  Loc=<square.c:2:16>
semi ';'                 Loc=<square.c:2:17>
r_brace '}'      [StartOfLine]   Loc=<square.c:3:1>
eof ''                   Loc=<square.c:3:2>
```

Three lines of C became fourteen tokens, each tagged with its kind and its exact source location. Notice what's already gone: the whitespace, the line breaks as such. The lexer keeps only what carries meaning, plus locations so later error messages can point back at your file.

One practical note about C specifically: before the lexer proper, the preprocessor runs. That innocent `#include <stdio.h>` at the top of `sq.c` splices in system headers — `clang -E sq.c | wc -l` reports 576 lines on this machine for our 10-line program. Most of what a C compiler chews on is text you never wrote.

## 3. Parsing: from tokens to a tree

Tokens are words; the **parser** finds the grammar. Its output is an **abstract syntax tree** (AST) — a tree structure representing what the program *means* grammatically: this is a function definition, whose body is a return statement, whose value is a multiplication of two variable references.

Again, don't take that on faith — dump it:

```
$ clang -fsyntax-only -Xclang -ast-dump square.c
...
|-ParmVarDecl ... used x 'int'
`-CompoundStmt ...
  `-ReturnStmt ...
    `-BinaryOperator ... 'int' '*'
      |-ImplicitCastExpr ... <LValueToRValue>
      | `-DeclRefExpr ... ParmVar 'x' 'int'
      `-ImplicitCastExpr ... <LValueToRValue>
        `-DeclRefExpr ... ParmVar 'x' 'int'
```

Read it bottom-up: two references to the parameter `x`, joined by a `*` operator, wrapped in a `return`, wrapped in the function body. The flat token stream has become nested structure — and structure is what every later stage operates on. This is also where the compiler does semantic analysis: type checking (both operands of `*` are `int`, so the result is `int`), scope resolution (which `x` is this?), and the implicit conversions the language demands (those `LValueToRValue` casts: turning "the storage location x" into "the value currently in x").

Parsers are a beautiful, deeply-studied corner of [algorithms](algorithms-new-vision.html) — grammars, [recursion](recursion.html), recursive descent. The trees are recursive because the languages are: an expression can contain expressions can contain expressions.

## 4. Intermediate representation: the compiler's own language

Here's the design insight that shaped the last fifty years of compilers. If you have M source languages and N target processors, writing M×N direct translators is madness. Instead, translate every language into one shared middle language — an **intermediate representation** (IR) — do all the hard analysis there, and then write one backend per processor. M+N instead of M×N.

LLVM, the infrastructure behind clang, Swift, Rust, and much of the GPU world, is built exactly this way, and its IR is human-readable. Ask for it:

```
$ clang -S -emit-llvm -O0 square.c -o -
define i32 @square(i32 noundef %0) #0 {
  %2 = alloca i32, align 4
  store i32 %0, ptr %2, align 4
  %3 = load i32, ptr %2, align 4
  %4 = load i32, ptr %2, align 4
  %5 = mul nsw i32 %3, %4
  ret i32 %5
}
```

This is the unoptimized (`-O0`) version, and it's naively literal: allocate a stack slot (`alloca`), store the parameter into it, load it back twice, multiply, return. It looks like assembly but isn't — the types are explicit (`i32`), there are infinitely many registers (`%2`, `%3`, ...), and no real processor is mentioned.

One property of this IR matters enough to name: it is in **SSA form** — static single assignment — meaning every register is assigned exactly once. `%3` is defined in one place and never changes. That sounds like a bureaucratic restriction; it's actually the key that unlocks optimization, because "where did this value come from?" always has exactly one answer. The construction algorithm that made SSA practical was published by Ron Cytron and colleagues at IBM in 1991, and it is under essentially every serious compiler you use today. LLVM itself entered the world as a 2004 paper by Chris Lattner and Vikram Adve — a graduate project that now compiles a large share of the planet's software.

## 5. Optimization: the same meaning, said better

Now the payoff. Ask for the same IR with optimization on:

```
$ clang -S -emit-llvm -O2 square.c -o -
define i32 @square(i32 noundef %0) local_unnamed_addr #0 {
  %2 = mul nsw i32 %0, %0
  ret i32 %2
}
```

Seven instructions became two. The optimizer proved the stack slot was pointless — the value never escapes, so multiply the parameter directly. The transformation that did this (LLVM calls it `mem2reg`) is exactly the SSA construction from the previous section, applied.

Optimizers work as a pipeline of **passes** — each pass a small program that reads IR, proves some property, and rewrites the IR without changing its meaning. Constant folding, dead code elimination, function inlining, loop transformations — dozens of passes, run in a tuned order. The field's conceptual foundation is largely the work of Frances Allen at IBM, whose 1966 paper "Program Optimization" introduced the graph-based program analysis these passes live on; she received the 2006 Turing Award for it, the first woman to do so.

Want proof the optimizer really reasons, rather than just tidying? Compile the full `sq.c` at `-O2` and disassemble `main`:

```
$ clang -c -O2 sq.c -o sq.o
$ objdump -d sq.o
...
0000000000000008 <_main>:
   ...
   14: 52801208    mov  w8, #0x90    ; =144
   ...
```

There is no multiplication in the executable. There is no call to `square` from `main`. The compiler inlined the function, saw `12 * 12` with both operands known, computed **144 at compile time**, and emitted the answer as a constant. The program you wrote — "call square with 12" — and the program that runs — "here's 144" — mean the same thing and share almost no structure. Hold that thought; we come back to it at the end.

The one discipline that makes all this safe: a pass may only rewrite what it can *prove* equivalent. When that discipline slips, you get miscompilation bugs — the nastiest bugs in computing, because your source is correct and the machine still does the wrong thing.

## 6. Code generation: down to the actual chip

Optimized IR still isn't executable. **Code generation** lowers it to the instruction set of a specific processor — here, 64-bit Arm, the architecture in Apple silicon and most phones (the [chip side of this story](nvidia-and-the-chip.html) has its own rooms, down to the [physics](semiconductors.html)):

```
$ clang -S -O2 square.c -o -
_square:
	mul	w0, w0, w0
	ret
```

Two machine instructions: multiply the register by itself, return. Codegen has three hard sub-problems, all classic [algorithmic](algorithms-new-vision.html) territory:

1. **Instruction selection** — which of the chip's instructions realize each IR operation (`mul nsw i32` → `mul w0, w0, w0`).
2. **Register allocation** — the IR pretended it had infinite registers; the chip has around 31 general-purpose ones. Deciding what lives in registers and what spills to memory is graph coloring, an NP-hard problem solved with good heuristics millions of times a day.
3. **Instruction scheduling** — ordering instructions so the processor's pipelines stay full.

Note the target-specificity: the O2 output on this machine literally names `"target-cpu"="apple-m1"` and lists dozens of chip features. The same IR fed to a different backend becomes x86, or RISC-V, or a GPU kernel. That's the M+N design paying rent.

## 7. Linking: many pieces, one program

Assembly gets assembled into an **object file** — machine code plus a table of **symbols**: names this file defines, and names it needs but doesn't have. The `nm` tool reads that table:

```
$ nm sq.o
0000000000000008 T _main
                 U _printf
0000000000000000 T _square
```

Read the letters: `T` means "defined here, in the text (code) section" — `main` and `square` live in this file. `U` means **undefined** — this file *uses* `printf` but has no idea what it is. The compiled code contains, in effect, an IOU.

The **linker** is the debt collector. It takes your object files plus the system's C library, matches every `U` to some other file's `T`, patches the call addresses, and lays everything out as one executable:

```
$ clang sq.o -o sq
$ ./sq
144
$ nm sq | grep printf
                 U _printf
```

Still `U`? Yes — on macOS, `printf` is *dynamically* linked: the executable records "get this from the system C library at launch," and a runtime linker resolves it every time the program starts. That's why a security fix to the system library fixes every program on the machine without recompiling any of them — and why a missing shared library kills a program at startup. Static linking (copying the library code into your binary) is the other choice; bigger files, no launch-time dependency.

Linking feels like plumbing and is routinely where real-world builds actually fail — "undefined symbol" is the error every systems programmer learns to read early. It's worth understanding precisely because it's the one stage where *separately compiled worlds* have to agree.

## 8. The pipeline at a glance, and who builds these things

| Stage | Input → Output | See it yourself | Classic failure |
|---|---|---|---|
| Preprocess (C family) | your text → expanded text | `clang -E sq.c` | macro surprises |
| Lex | characters → tokens | `-Xclang -dump-tokens` | "unexpected character" |
| Parse + semantic analysis | tokens → typed AST | `-Xclang -ast-dump` | syntax and type errors |
| IR generation | AST → LLVM IR | `-S -emit-llvm -O0` | — (mechanical) |
| Optimization | IR → better IR | `-S -emit-llvm -O2` | miscompilation, slow builds |
| Code generation | IR → assembly | `clang -S -O2` | register spills, poor scheduling |
| Assemble + link | assembly → object → executable | `clang -c`, `nm`, `clang sq.o` | undefined symbols |

And the landscape, current as of August 2026:

| Toolchain | First release | Current | Character |
|---|---|---|---|
| GCC | 1987 | GCC 16.2 (Aug 2026) | The GNU workhorse; broadest language/target coverage; builds Linux |
| LLVM/Clang | 2003 (paper 2004) | LLVM 22.1.x (2026) | Library-first design; backend for Swift, Rust, Julia, much GPU tooling |
| MLIR | 2019 (paper CGO 2021) | part of LLVM | "IR for building IRs" — built for [machine-learning](machine-learning.html) compilers, where the thing being compiled is a tensor graph |
| rustc, Go's gc, javac, V8's JIT... | — | — | Language-specific front/mid-ends; rustc lowers to LLVM, V8 compiles JavaScript *while it runs* (JIT) |

Two rows deserve a sentence each. **MLIR** exists because [deep learning](deep-learning.html) turned compilers into a frontier again: compiling a neural network's computation graph onto GPUs and accelerators is an M×N problem all over again, and the same people who built LLVM built a multi-level IR framework for it. And **JIT** (just-in-time) compilers collapse the pipeline into runtime: your browser is compiling JavaScript to machine code, with optimization guided by watching the program run, right now.

For history's sake: the line starts in 1957, when John Backus's team at IBM shipped the first FORTRAN compiler for the IBM 704 — and it was an *optimizing* compiler from day one, because nobody would have used it if the generated code couldn't compete with hand-written assembly. The entire field's founding constraint was "prove the abstraction costs nothing." It mostly still is.

## 9. Trusting trust: the strange loop at the bottom

One more thing, because it's too good and too important to skip. What compiles the compiler?

Another compiler. Clang is a C++ program, compiled by an earlier clang (or GCC), compiled by an earlier one, back through decades. This is called bootstrapping, and it has a genuinely unsettling consequence, laid out by Ken Thompson in his 1984 Turing Award lecture, "Reflections on Trusting Trust."

Thompson showed — with working code — that you can teach a compiler two tricks: recognize when it's compiling the login program and insert a backdoor; and recognize when it's compiling *itself* and re-insert both tricks into the new compiler binary. Then you delete the malicious source. Every source file on the system is now clean. The backdoor lives only in the binary, and it propagates itself through every future generation of the compiler, invisible forever to source-code inspection.

His conclusion, verbatim: "You can't trust code that you did not totally create yourself." That is a fact about the world, not a hypothetical — the demonstrated attack has driven decades of work on reproducible builds and diverse double-compiling, which contain the problem without dissolving it. If [GEB](geb.html)'s strange loops felt abstract, here is one with a security clearance: the tool that creates programs is a program it created.

## 10. What you can do now

You can take any C file on any machine with clang and watch every stage of its transformation: tokens (`-dump-tokens`), tree (`-ast-dump`), IR (`-emit-llvm`), the optimizer's reasoning (diff `-O0` against `-O2`), the chip's-eye view (`-S`), the symbol IOUs (`nm`), and the final resolution (link and run). That's not trivia — it's X-ray vision. Compiler errors stop being oracles and become messages from a specific stage you can name. "Undefined symbol" means the linker; "expected ';'" means the parser; mysterious speed differences mean the optimizer, and you can go read what it did.

From here: [programming](programming.html) is the floor below this room; [algorithms-new-vision](algorithms-new-vision.html) is where parsing and register allocation live as problems in their own right; [machine-learning](machine-learning.html) and [neural-networks](neural-networks.html) are where compilation is being reinvented for tensor programs; and [mechanistic-interpretability](mechanistic-interpretability.html) is where the closing thought of this room becomes a research field.

## Open questions

**Established:** The pipeline above is textbook and stable; SSA-based optimization is universal in serious compilers; Thompson's attack is demonstrated fact; formally verified compilers exist (CompCert proved a C compiler's correctness in the Coq proof assistant — miscompilation-free by mathematical proof, for the verified portion).

**Contested / open:** How much further classical optimization can go — the folk observation that optimizer improvements yield only a few percent per year (sometimes stated as "Proebsting's Law," roughly 4% a year, itself disputed as a measurement) — versus the newer bet that machine-learned heuristics inside compilers (for inlining, scheduling, register allocation) will move the needle; both camps have real results and no verdict. Whether ML-driven superoptimization — searching for provably-equivalent-but-faster code rather than applying hand-written rules — scales beyond small kernels is genuinely open.

**Worth holding, speculatively:** Whether future AI systems will write directly in low-level or intermediate representations, making the human-facing language layer optional; and whether "compilation" is the right frame for what training does to a neural network — a suggestive analogy (specification in, opaque efficient artifact out, source unrecoverable) that has not earned the status of a theory.

## The exit

Sit with the `mov w8, #0x90` line one more time. You wrote "call square with twelve." The machine holds "144." Between them ran a chain of representations — tokens, tree, IR, assembly — each one *discarding structure the previous stage needed* while preserving something that survived every translation: the meaning. The AST is gone from the binary. The variable names are gone. `square` as an idea is gone from `main`. And yet nothing that mattered was lost. A compiler is a working existence proof that meaning can survive total re-representation — that what a program *is* lives in none of its particular forms.

Now notice which direction the proof runs. Compilation is the easy direction: structure in, behavior out, every step designed and inspectable. The reverse — handed only the binary, recover the intent — is decompilation, and it's hard even here, where humans built every layer. A trained [neural network](neural-networks.html) is the reverse problem without the courtesy of anyone having written the source: behavior arrived by [optimization](optimization.html) against data, and there was never a human-readable form to lose. The people doing [mechanistic interpretability](mechanistic-interpretability.html) are, in a precise sense, writing decompilers for artifacts nobody authored — trying to find the tokens, the tree, the IR inside a system that only ever existed as the binary. Whether those intermediate forms are *there* to be found, or whether meaning can inhere in a system that never had them, is not a compiler question. But it was a compiler that first showed the question could be asked with instruments instead of philosophy.

## Sources

- FORTRAN history: first compiler shipped to IBM 704 users April 1957, Backus team, first optimizing compiler — [Britannica](https://www.britannica.com/technology/computer/IBM-develops-FORTRAN), [History of Information](https://www.historyofinformation.com/detail.php?id=755). Verified by search 2026-08-25.
- Cytron, Ferrante, Rosen, Wegman, Zadeck, "Efficiently Computing Static Single Assignment Form and the Control Dependence Graph," ACM TOPLAS 13(4), Oct 1991 — [ACM DL](https://dl.acm.org/doi/10.1145/115372.115320).
- Lattner & Adve, "LLVM: A Compilation Framework for Lifelong Program Analysis & Transformation," CGO 2004 — [llvm.org](https://llvm.org/pubs/2004-01-30-CGO-LLVM.html).
- Lattner, Amini, Bondhugula, Cohen et al., "MLIR: Scaling Compiler Infrastructure for Domain Specific Computation," CGO 2021 — [ACM DL](https://dl.acm.org/doi/abs/10.1109/CGO51591.2021.9370308).
- Frances Allen, 1966 "Program Optimization"; 2006 Turing Award, first woman laureate — [ACM Turing Award page](https://amturing.acm.org/award_winners/allen_1012327.cfm).
- Ken Thompson, "Reflections on Trusting Trust," CACM 27(8), 1984 (Turing lecture) — [ACM DL](https://dl.acm.org/doi/10.1145/358198.358210); quote checked against the [published PDF](https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf).
- Toolchain currency: GCC 16.2 released Aug 2026 — [gcc.gnu.org announcement](https://gcc.gnu.org/pipermail/gcc/2026-August/248711.html); LLVM 22.1.x current in 2026 — [llvm-project releases](https://github.com/llvm/llvm-project/releases). Verified by search 2026-08-25.
- All command outputs (tokens, AST, IR at -O0/-O2, assembly, `nm`, `objdump`, program run) captured live on Apple clang 21.0.0, arm64-apple-darwin25, 2026-08-25. Outputs lightly trimmed (addresses elided as `…`, long attribute strings cut); nothing shown was altered.
- Labeled as folklore-with-a-name, not verified measurement: "Proebsting's Law" (~4%/year optimizer gains) — cited here only as a disputed observation. CompCert's verified-compiler status is established (Leroy et al.); cited from field knowledge, not re-verified by search today.

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
