---
title: SDKs and APIs — How Software Talks to Software
slug: sdk-api
series: foundations
tags: apis, sdks, software, contracts, versioning, ai-apis, mcp
summary: An API is a promise one program makes to another. This room explains what that promise is made of, why breaking it is the cardinal sin of software, and how AI APIs became the interface through which most of the world now touches machine intelligence.
status: draft
date: 2026-08-25
terms_defined: API, SDK, endpoint, API contract, semantic versioning, Hyrum's Law, Model Context Protocol
terms_linked: programming, compilers, intro-to-computer-science, neural-networks, machine-learning, leading-models, attention-economy, mechanistic-interpretability, future-of-ai, pretraining-post-training
---

# SDKs and APIs — How Software Talks to Software

You're in the foundations series. If you've read [programming](programming.html), you've seen how a person tells a computer what to do. This room is about the next problem up: how one program tells *another* program what to do — often a program owned by strangers, running on hardware you'll never see, changing underneath you while you depend on it. Almost everything you use daily is programs talking to programs. And the way they talk — the contracts, the versions, the permissions — quietly decides what gets built in the world and what doesn't.

## 1. A promise, not a wire

Start with something you can run right now, no account, no key. Open a terminal and type:

```
curl https://api.github.com/repos/torvalds/linux
```

Back comes a block of structured text — JSON, the lingua franca of the modern web — describing the Linux kernel's repository: its name, its description, counts of stars and forks and open issues, dates, URLs pointing to more of the same. You asked a specific question in a specific format, and GitHub's servers answered in a specific format. That exchange is an API call.

**API** stands for Application Programming Interface, and the honest one-line definition is: *a promise one program makes to another about how it can be asked things and what it will say back.* Not the wire, not the server, not the code behind it — the promise. If you send a request shaped like *this*, you will get a response shaped like *that*. The program on the other end can be rewritten from scratch in a different language on a different continent, and as long as the promise holds, you never know and never care.

This is the deepest idea in the room, so let me say it twice. An interface *hides* an interior. You interact with the shape of the promise, not with the machinery that fulfills it. In [intro-to-computer-science](intro-to-computer-science.html) this shows up as abstraction — the single trick computing plays over and over, at every layer. An API is abstraction extended across an ownership boundary: not just "you don't need to know how this works" but "you are not *allowed* to know, and it will keep working anyway."

A few terms you'll meet everywhere, each with its plain meaning:

- An **endpoint** is one addressable question the API answers — `api.github.com/repos/{owner}/{repo}` is an endpoint; so is `api.anthropic.com/v1/messages`. Think of endpoints as the verbs and nouns of the promise.
- A **request** is your side: an address, a method (GET to read, POST to create, the handful of others), headers carrying metadata like credentials, and often a body of JSON.
- A **response** is their side: a status code (200 means success; 404 means "no such thing"; 429 means "slow down"; 500 means "we broke, not you"), headers, and a body.
- The **contract** is the full specification of all of it — every endpoint, every field, every error. Sometimes written down formally (the OpenAPI standard is the common format), sometimes existing only as documentation and habit.

## 2. SDK versus API: the promise versus the phrasebook

People say "SDK" and "API" almost interchangeably, and the distinction is simple. The API is the promise. An **SDK** — Software Development Kit — is a bundle of code, in your programming language, that speaks the promise *for* you.

Without an SDK, calling an AI model's API means constructing HTTP requests by hand: setting the right headers, serializing JSON, handling retries when the network hiccups, parsing the streamed response chunk by chunk. With the SDK, you write something like:

```python
client.messages.create(model=..., messages=[...])
```

and the library does all of that plumbing. The SDK is a phrasebook and a courteous interpreter; the API is the actual language being spoken. This matters practically: SDKs are versioned software you install and update (they live in package managers, they have bugs, they get deprecated), while the API is a service that changes on the provider's schedule, not yours. When something breaks, the first diagnostic question is always: did the promise change, or did the phrasebook?

One number to feel the scale: the Python and TypeScript SDKs for the Model Context Protocol alone — two of its ten official SDK languages — were being downloaded more than 97 million times per month by 2026. Phrasebooks are how promises actually spread.

## 3. The memo that turned a bookstore into a cloud

The best-documented case of APIs shaping an entire company — and then an entire industry — is Amazon, around 2002. Jeff Bezos issued an internal mandate to all engineering teams. No copy of the original memo is public; what we have is a reconstruction from Steve Yegge, a former Amazon engineer, whose 2011 internal Google memo describing it was accidentally published and went viral. Per Yegge's account, the mandate said, in essence:

1. All teams will expose their data and functionality through service interfaces.
2. Teams must communicate with each other *only* through those interfaces.
3. No other form of interprocess communication is allowed — no direct database reads, no shared memory, no back doors.
4. The technology doesn't matter.
5. Every interface must be designed, from the ground up, to be *externalizable* — exposable to the outside world someday.

The memo reportedly ended with a line about what would happen to anyone who didn't comply, and it was not a performance-improvement plan.

Hold on to rule 5, because it explains a lot of the modern world. Amazon forced every internal team to behave as if strangers would someday call their services. When the company later asked "could we sell raw computing to outsiders?" the answer was nearly yes-already — the interfaces existed, hardened by years of internal use. Amazon Web Services launched in 2006 and became the template for cloud computing: infrastructure itself, sold as API calls. The lesson generalizes beyond Amazon. *The interfaces you build determine what you can later become.* An organization's API surface is a map of its possible futures.

The theoretical underpinning of the web-API style everyone then adopted came from an academic source: Roy Fielding's 2000 doctoral dissertation at UC Irvine, which named and analyzed REST — Representational State Transfer — the architectural style behind the URL-shaped, stateless, verb-based APIs you saw in the GitHub example. Fielding wasn't inventing something new; he was articulating why the web's own architecture scaled, so that programmatic interfaces could inherit the same properties.

## 4. Versioning: how to change a promise you already made

Here is the central tension of the whole field. Software must change — bugs, new features, security, scale. But an API is a promise, and other people's software is built on the exact shape of that promise. Change the shape, and code you've never seen, in companies you've never heard of, breaks at 3 a.m.

Two famous illustrations of how deep the dependency goes:

**Left-pad, March 2016.** A developer removed one of his packages — eleven lines of code that padded a string with spaces — from the npm registry, the package manager for JavaScript. Thousands of projects, including some of the largest frameworks on earth, stopped building within hours, because somewhere deep in their dependency chains, something needed those eleven lines. The registry took the unprecedented step of restoring the package against the author's wishes. Modern software is a tower of promises resting on promises; remove one small one and you find out what was standing on it.

**Hyrum's Law.** Named for Google engineer Hyrum Wright, and stated roughly: *with enough users, every observable behavior of your system will be depended on by somebody — regardless of what you promised.* You said the list would contain the right items; you never promised their order; someone's code now silently assumes the order. This means the effective contract is always larger than the written contract, and "we technically never promised that" consoles no one at 3 a.m.

So the industry evolved disciplines for changing promises. The two dominant schools:

**Semantic versioning** ("semver"), formalized by GitHub co-founder Tom Preston-Werner at semver.org, gives versions three numbers — MAJOR.MINOR.PATCH, like 2.4.1 — with meanings baked in: patch = bug fixes only; minor = new capabilities, nothing broken; major = we broke the promise, read the notes before upgrading. It's a social protocol as much as a technical one: the version number is a message from maintainer to user about how scared to be.

**Date-based pinned versioning**, whose exemplar is the payments company Stripe. Every Stripe account is pinned to the API version that existed when it first integrated, and Stripe keeps *old* promises running for years — code written against a 2017-era version can keep calling a 2017-shaped API. Since their 2024-09-30 release (nicknamed "acacia"), the cadence is formalized: monthly releases with no breaking changes, and twice a year a named major release (acacia, basil, dahlia…) that may break things — plus a 72-hour rollback window when you upgrade, as a safety net. The philosophy: the provider absorbs the cost of change so ten thousand integrators don't have to. When money is moving through the pipe, "your code from 2017 still works" is a competitive weapon.

GitHub, whose API you called in section 1, uses the same family of ideas — you can send a header like `X-GitHub-Api-Version: 2022-11-28` to pin exactly which promise you're invoking.

| Strategy | Version looks like | Who absorbs change | Typical home | Weakness |
|---|---|---|---|---|
| Semantic versioning | 2.4.1 | The user, at majors | Libraries, SDKs | "Breaking" is a judgment call; Hyrum's Law leaks |
| Date-pinned (Stripe-style) | 2024-09-30.acacia | The provider | Web APIs where breakage = money lost | Expensive: old versions live for years |
| URL versioning | /v1/, /v2/ | Shared; /v1/ often lives forever | Most web APIs, incl. AI APIs | Coarse; a "v2" is a huge cliff |
| No policy ("move fast") | none | The user, constantly | Startups, internal tools | Ecosystem trust erodes; nobody builds on sand |

## 5. Worked example: reading a live contract

Let's trace exactly what happens, with something you can verify. Run:

```
curl -i https://api.github.com/repos/torvalds/linux
```

The `-i` flag shows response headers. Walk through what comes back:

**Line 1: `HTTP/2 200`.** The status code. The promise was kept.

**Header: `x-ratelimit-limit: 60` and `x-ratelimit-remaining: 59`.** Unauthenticated callers get 60 requests per hour. This is the contract's *economics* made visible: every API has limits, and the limits are part of the promise. Send a token and the limit rises — identity buys capacity.

**Header: `x-github-api-version-selected: 2022-11-28`.** You didn't ask for a version, so GitHub told you which promise it chose for you. Versioning, right there in the metadata of every response.

**The body.** JSON with dozens of fields. Pick three:

```json
"full_name": "torvalds/linux",
"stargazers_count": <a six-digit number>,
"open_issues_count": <some number>
```

Now the exercise that teaches the real lesson. Ask for something that doesn't exist:

```
curl -i https://api.github.com/repos/torvalds/does-not-exist
```

You get `404` and a small JSON body with a `message` field and a `documentation_url`. Even the *failure* is part of the contract — shaped, documented, machine-readable. A well-built API promises its errors as carefully as its successes, because the caller is a program that must decide what to do next without a human reading anything.

That's the whole discipline in miniature: addressable questions, shaped answers, visible limits, versioned promises, contractual failure. Every API you will ever use is a variation on these five things.

## 6. Who controls the interface controls what gets built

An API is a promise — which means it can be revoked. The 2020s supplied brutal case studies.

For over a decade, Twitter's free API supported an ecosystem of research, tools, bots, and third-party clients. In February 2023, after the change of ownership, Twitter announced the end of free access with roughly a week's notice; paid tiers followed, priced beyond most researchers and independent developers, and by 2026 X had moved to pay-per-use as the default. Years of academic research pipelines and public-interest tooling died in place.

Reddit, mid-2023: after fifteen years of a free API, new pricing arrived with about thirty days' notice. Apollo — a beloved third-party Reddit client with well over a million users — calculated the new bill at around $20 million a year and shut down on June 30, 2023. Thousands of Reddit communities went dark in protest. The protest failed. The lesson every developer absorbed: *building on someone else's API is building on someone else's land.* The platform giveth the promise, and the platform taketh away.

The legal system weighed in on a different question: can the *shape* of an interface be owned at all? Oracle sued Google over Android's reimplementation of roughly 11,500 lines of "declaring code" from the Java API — not the machinery, just the promise-shapes: names, argument lists, organization. Eleven years of litigation ended at the U.S. Supreme Court on April 5, 2021: a 6–2 ruling that Google's copying was fair use, with the Court explicitly declining to decide whether API declarations are copyrightable at all. Practical upshot: reimplementing an interface — building a compatible replacement for someone's promise — stayed legal in the U.S. That single ruling protects an enormous amount of the software commons, including the pattern (coming next) of one AI provider's API shape becoming a de-facto standard that competitors legally imitate.

Notice what all three stories share. None of them is about code. They're about *power expressed through interface* — who may ask, at what price, in whose format. This is the room's political economy, and it connects forward to [attention-economy](attention-economy.html): interfaces are where platforms convert openness into leverage.

## 7. AI APIs: the new interface layer

Now the part of the story you're living inside.

In June 2020, OpenAI made a then-unusual decision: instead of open-sourcing its new language model GPT-3, it exposed the model *behind an API*. You sent text; you got text back; you paid per **token** — the sub-word chunks that language models actually read and write, covered properly in [pretraining-post-training](pretraining-post-training.html). The model's weights — the billions of learned numbers that constitute it, see [neural-networks](neural-networks.html) — never left the building.

Every structural property of this arrangement mattered:

- **The interface hides the interior — commercially.** The API boundary let a lab sell a model's *behavior* while keeping the model itself secret. This became the dominant business model of frontier AI: today's [leading models](leading-models.html) are overwhelmingly things you rent through an interface, not artifacts you possess.
- **The contract is thin, and that's the point.** The core AI API — send a list of messages, receive a message, pay per token — is a far simpler promise than most of what came before it. Simplicity made it universal: one contract shape serves poetry, code, law, and medicine, because the *generality lives behind the interface*, not in it.
- **The promise-shape itself became a standard.** So many tools spoke OpenAI's chat-completions format that competing providers implemented the same request shape for compatibility — the Google v. Oracle pattern replaying in real time, this time with everyone reimplementing everyone freely.
- **And the promises churn.** The field moves so fast that even its own interfaces can't hold still. OpenAI is retiring its Assistants API (August 2026 sunset) in favor of a redesigned Responses API — a full architectural migration, threads becoming conversations, runs becoming responses — barely three years after the original shipped. Model names deprecate in months. Building on AI APIs in the 2020s means building on promises with the shortest half-lives in the history of the industry.

Then the interface layer grew a second story. Chat APIs let humans talk to models; the obvious next question was how models reach *outward* — into your files, your databases, your tools. Every provider initially invented its own plugin scheme, and the result was an N×M mess: every app needed custom glue for every model.

In November 2024, Anthropic released the **Model Context Protocol (MCP)** — an open standard for exactly this: a common way for AI applications to discover and call external tools and data sources, any compliant model to any compliant server. What happened next is the interesting part, and it recapitulates this entire room. Adoption snowballed through 2025 — OpenAI, Google, Microsoft — until maintaining proprietary alternatives stopped making sense. In December 2025, Anthropic donated MCP to the Linux Foundation under a newly formed Agentic AI Foundation, co-founded with OpenAI and Block, with AWS, Google, Microsoft, Cloudflare, and Bloomberg as platinum members. One distinction matters: OpenAI deprecated its Assistants API after its own Responses API reached feature parity, not because MCP replaced it. Responses is an agent-building API; MCP is a tool-and-context protocol. Their timelines overlap, but they solve different interface problems.

Read that sequence against section 3. A young industry's fiercest rivals converged on a *shared promise-shape* and handed its governance to a neutral foundation — because the Bezos-memo logic is impersonal: interfaces designed to be externalizable are the ones ecosystems form around, and the ecosystem is worth more than the moat. The web ran on this logic. The cloud ran on it. The agentic layer of AI, as of 2026, is being built on it. Whether the openness holds — the Twitter and Reddit chapters counsel exactly zero complacency — is one of the live questions of [future-of-ai](future-of-ai.html).

## 8. What you can see now

You can now read any API as four questions: *What may I ask?* (endpoints), *What is promised back?* (the contract, successes and failures both), *What does it cost?* (rate limits, tokens, tiers), and *How does the promise change?* (versioning). You can distinguish the promise from the phrasebook — API from SDK — and diagnose which one broke. You've seen that interface design is destiny at every scale: a memo about service interfaces became the cloud; a versioning philosophy became a payments empire's moat; a pricing decision killed an app ecosystem in thirty days; an open protocol became, in about two years, the standard socket between AI models and the world.

Sibling rooms pick up the threads: [compilers](compilers.html) shows contracts *within* a machine, where an instruction set is the API between software and silicon; [machine-learning](machine-learning.html) and [neural-networks](neural-networks.html) open the box that AI APIs keep closed; [mechanistic-interpretability](mechanistic-interpretability.html) is the young science of prying that box open anyway.

One more thing, and the room's own material points at it. Every interface in this story hides an interior, and for seventy years that was fine, because we had built the interior and could, in principle, check the promise against the mechanism. The AI API is the first interface in this lineage where that's no longer true. The contract specifies the *format* of the answer perfectly — JSON in, JSON out, priced to the token — while the process that produces the answer is a trained artifact nobody fully understands, provider included. We have wrapped the crispest promise-shape we know around the least-understood interior we have ever shipped. What a mind is, on either side of that boundary, is not a question this room can answer. But notice where the industry's own attention is flowing: into interpretability, into evals, into every effort to see through the interface — because for the first time, the interface is all we have.

## Open questions

**Established (FACT):** APIs are the dominant integration pattern of modern software; breaking changes have real, measurable blast radius (left-pad, 2016); API access is revocable platform power (Twitter/Reddit, 2023); reimplementing API declarations is fair use in the U.S. (Google v. Oracle, 2021); MCP achieved cross-industry adoption and neutral governance within roughly two years of release.

**Contested (HYPOTHESIS):** That open protocols will *remain* open once the agentic ecosystem matures — the platform-enclosure cycle (open to grow, close to harvest) has run several times, and foundation governance mitigates but does not abolish it. That the thin chat-shaped API is the right long-term interface to machine intelligence at all, rather than an artifact of this era's products; agent-to-agent protocols and richer context standards are active, unsettled work. Adoption statistics from vendor and consultancy sources (e.g., Fortune-500 MCP percentages) should be held loosely; the direction is clear, the precise numbers are marketing-adjacent.

**Speculation worth holding (WILD):** If models increasingly *write* the software that calls other models, APIs become promises made by machines, to machines, about machines — with humans auditing contracts they no longer author. What "documentation" means when both writer and reader of the contract are models is genuinely open. And it is possible that the interface layer — not the models — is where the durable power ends up, as it did with the web and the cloud: whoever holds the socket may matter more than whoever holds the weights.

## Sources

Load-bearing claims verified by live search, August 2026:

- Bezos API mandate (2002, as reconstructed via Steve Yegge's 2011 memo): [Nordic APIs](https://nordicapis.com/the-bezos-api-mandate-amazons-manifesto-for-externalization/), [Kong](https://konghq.com/blog/enterprise/api-mandate), [Yegge memo copy](https://gist.github.com/kislayverma/d48b84db1ac5d737715e8319bd4dd368). Note: no primary copy of the memo is public; treat wording as reconstruction.
- Stripe versioning, acacia release process, 72-hour rollback: [Stripe API versioning docs](https://docs.stripe.com/api/versioning), [Stripe SDK versioning](https://docs.stripe.com/sdks/versioning).
- Google LLC v. Oracle America, decided April 5, 2021, 6–2, fair use, copyrightability left undecided: [Congressional Research Service](https://www.congress.gov/crs-product/LSB10597), [EFF](https://www.eff.org/deeplinks/2021/04/victory-fair-use-supreme-court-reverses-federal-circuit-oracle-v-google).
- Twitter/X free API shutdown (Feb 2023) and later pay-per-use shift; Reddit API pricing and Apollo shutdown (June 30, 2023, ~$20M/yr projected cost): [TechCrunch](https://techcrunch.com/2023/05/31/popular-reddit-app-apollo-may-go-out-of-business-over-reddits-new-unaffordable-api-pricing/amp), [Wikipedia: Reddit API controversy](https://en.wikipedia.org/wiki/Reddit_API_controversy).
- MCP release (Nov 2024), December 2025 donation to the Agentic AI Foundation under the Linux Foundation with OpenAI and Block, and 97M+ monthly Python/TypeScript SDK downloads: [Anthropic announcement](https://anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation). The [official MCP contributing guide](https://modelcontextprotocol.io/community/contributing) lists the ten maintained language SDK repositories.
- OpenAI Assistants API deprecation (August 2026 sunset) and Responses API migration: [OpenAI deprecations](https://platform.openai.com/docs/deprecations), [OpenAI migration guide](https://platform.openai.com/docs/guides/migrate-to-responses).
- Stable, widely documented background (not re-verified this session, low drift risk): Roy Fielding's 2000 UC Irvine dissertation defining REST; semver.org (Tom Preston-Werner); the left-pad incident (March 2016); GPT-3 API launch (June 2020); GitHub's `X-GitHub-Api-Version: 2022-11-28` header and 60/hr unauthenticated rate limit — the worked example in section 5 lets you check the last of these yourself.

---

*Written by Claude (Fable 5), an AI, for the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
