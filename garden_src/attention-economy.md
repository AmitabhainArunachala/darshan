---
title: The Attention Economy
slug: attention-economy
series: power
tags: attention, advertising, social media, recommender systems, smartphones, humane technology, platform power
summary: The attention economy is the set of markets and machines built around a hard limit: you can only notice so much. This room follows the money from advertisers to feeds, traces one ranked recommendation step by step, and tests the strongest claims about harm and reform.
status: draft
date: 2026-08-25
terms_defined: attention economy, engagement, recommender system, behavioral advertising, two-sided market, stopping cue
terms_linked: algorithms-new-vision, machine-learning, optimization, governments-and-ai, palantir, elon-musk, blockchain, benchmarks, forecasting, meaning-of-time, sense-of-self
---

# The Attention Economy

You're in the power wing of the garden. The neighboring rooms follow what states can compel, what companies such as [Palantir](palantir.html) can make visible, and what changes when [one entrepreneur](elon-musk.html) owns a major distribution channel. This room follows a quieter kind of power: the ability to decide what reaches your eyes next, and to earn money from that decision.

## 1. Start with the scarce thing

Imagine opening your phone at 7:30 in the morning. Your family has sent six messages. Three news alerts are waiting. A work app has two red badges. A video feed can supply more clips than you could watch in a lifetime. Information is abundant before you have left bed. Your capacity to receive it is not.

Herbert Simon named this inversion in 1971. In *Designing Organizations for an Information-Rich World*, he argued that an abundance of information consumes the attention of its recipients. The scarce resource is therefore not information. It is the capacity to notice, understand, and decide what to do with information.

That gives us a clean definition. **The attention economy is the set of systems in which access to limited human attention is allocated, measured, and often sold.** A newspaper allocates space among stories and advertisements. A television network sells advertisers access to an expected audience. A search engine chooses ten links and several ads from millions of candidates. A social feed makes that allocation again after every swipe.

Attention is not a barrel of oil. A platform cannot remove ten minutes from your head and ship it to an advertiser. What it can do is create a reliable opportunity for an advertiser's message to be seen, then charge for the impression, click, view, or purchase that follows. Treat “selling attention” as useful shorthand for selling that opportunity, not as a literal transfer.

This distinction matters. It lets you criticize the real mechanism without pretending that every entertaining screen is theft. Sometimes you deliberately trade attention for something you value: a free map, a friend's update, a lecture, a joke. The question is whether the terms of that trade are visible, whether you can refuse them, and whose objective controls the next item.

## 2. From Simon to the feed in your hand

The business is older than the smartphone. Advertising-supported newspapers and broadcast programs already joined two groups that wanted different things. Readers or viewers wanted content. Advertisers wanted access to readers or viewers. Economists call this a **two-sided market**: a business creates value by bringing two different groups together, then charges one side, both sides, or neither side directly.

Digital systems changed the precision and tempo of the exchange.

In September 2006, Facebook's News Feed turned a collection of profile pages into a continuously updated stream. The launch provoked an immediate privacy backlash, which Facebook answered with additional controls. The important change survived: users no longer had to decide which page to visit. The service decided which update should come to them.

Apple introduced the iPhone in January 2007 as a phone, an iPod, and an internet device in one touch-controlled object. The first model did not contain the mature notification and app ecosystem you know now. It did make the internet portable, personal, sensor-rich, and reachable during every small gap in the day.

Ranked feeds then became prediction systems. Facebook's own 2018 explanation broke ranking into four parts: available posts, signals about the posts and viewer, predictions about likely responses, and a score used to order the posts. In 2020, TikTok said its For You system used signals such as likes, shares, comments, captions, sounds, and whether a viewer finished a longer video. A completed view carried more weight than a weak contextual match such as sharing a country with the creator.

That is the move from a page to a feed. A page waits for your intention. A feed predicts it. The best prediction systems make the next item feel less like a selection made by a distant company and more like the natural continuation of your own interest.

## 3. Follow the money, using the filings

You do not need leaked emails to establish the central business incentive. The companies report it to investors.

Meta's 2025 annual filing recorded $200.966 billion in total revenue. Advertising supplied $196.175 billion, or about 97.6%. The same filing reported 3.58 billion daily active people across its family of apps in December 2025 and annual revenue per active person of $57.03. Meta says user growth and engagement affect revenue by changing both the number of ads it can show and their value to marketers.

Alphabet's 2025 filing recorded $402.836 billion in total revenue and $294.691 billion in Google advertising revenue. That is about 73.2%. Search ads, YouTube ads, and ads on partner properties are different products, but they share a basic proposition: Google can place a message in a moment when it predicts that the message will matter.

Those numbers prove that advertising finances these companies. They do **not** prove that every product decision maximizes time spent, or that an individual user's attention is worth a fixed number of cents. Meta's own annual revenue-per-person figure is an average across countries, products, seasons, and kinds of use. Divide $57.03 by 365 and you get roughly 15.6 cents per day, but that is a rough unit-economics lens, not the price of your day. A US Instagram session and a WhatsApp message in a lower-ad-price market do not monetize alike.

Here are the main arrangements side by side:

| Model | Who pays | What gets optimized first | Real advantage | Structural pressure |
|---|---|---|---|---|
| Search advertising | Advertiser, usually per click or outcome | Match between an expressed query and an ad | High relevance at the moment of intent | More valuable queries and better conversion measurement |
| Social-feed advertising | Advertiser, per impression, action, or campaign outcome | Predicted relevance of content and ads to a person | Discovery without a prior query | More usable inventory and better behavioral prediction |
| Subscription | User, at a recurring price | Retention of a paying customer | The customer and payer are the same person | Lock-in, price increases, and content made safe for subscribers |
| Contextual advertising | Advertiser, based mainly on page or topic | Match between message and current context | Less dependence on a behavioral profile | Lower targeting precision in some markets |
| Public, nonprofit, or cooperative service | Taxpayer, donor, member, or mixed funding | A stated public or member purpose | Governance can include goals beyond revenue | Political control, weak funding, or capture by insiders |

No row is innocent. Subscription businesses also design for retention. Public media can become propaganda. A cooperative can serve its most active members rather than everyone. The useful question is not “ads or no ads?” It is “who is the customer, what is measured, and who can change the objective?”

The phrase **behavioral advertising** means choosing or tailoring an ad partly from observed or inferred behavior, rather than only from the page in front of you. A shoe ad beside an article about running is contextual. A shoe ad beside an unrelated article because the system has inferred that you run is behavioral. Real campaigns can combine both.

## 4. What a feed actually optimizes

A **recommender system** is software that ranks candidate items for a particular user or context. Modern recommenders use [machine learning](machine-learning.html), which means they learn patterns from examples rather than following only hand-written rules. The underlying [optimization](optimization.html) problem is simple to state: choose an order that scores well on the platform's objectives while satisfying policy, safety, and product constraints.

“Maximize engagement” is the usual summary. **Engagement** means measurable interaction: a view, pause, click, like, share, comment, follow, return visit, or purchase. But a production system rarely has one engagement number. It predicts several outcomes, assigns them weights, applies penalties, and tests changes against a bundle of metrics.

Facebook said in 2018 that it predicted whether a person would comment, share, or interact with friends, and that it demoted engagement bait even when bait produced clicks. Meta's later system cards describe prediction models using features of a post and a person's history with similar posts. TikTok says it deliberately injects some variety and makes some reviewed categories ineligible for recommendation. These are the companies' descriptions, not independent audits, but they are enough to reject the cartoon of one dial labeled ADDICTION.

The deeper criticism survives the correction. A company can include satisfaction and safety metrics while still depending on a long, repeatable stream of monetizable opportunities. Anything hard to measure—regret an hour later, a broken train of thought, a slowly narrowed sense of what matters—enters the objective weakly unless research, regulation, reputation, or user departure makes it costly.

This is a proxy problem familiar from [benchmarks](benchmarks.html). The system cannot directly optimize “a life well spent.” It optimizes signals that stand in for value. Once creators learn which signals receive distribution, they adapt their work to them. Headlines sharpen. Videos put the payoff in the first second. Outrage becomes useful because it produces action. None of this requires a meeting where executives choose social corrosion. It can emerge from millions of local attempts to score well against a proxy.

## 5. Worked example: trace one swipe

Let's trace exactly what happens in a simplified feed. The numbers below are invented so you can inspect the mechanism. The sequence is based on the public ranking descriptions from Meta and TikTok; it is not a claim about either company's secret weights.

You open an app. Four candidate videos survive eligibility checks:

| Candidate | Predicted full watch | Predicted share | Predicted “not interested” | Diversity bonus | Final toy score |
|---|---:|---:|---:|---:|---:|
| Friend's climbing clip | 0.72 | 0.08 | 0.02 | 0.00 | 0.790 |
| Election argument | 0.81 | 0.15 | 0.12 | 0.00 | 0.765 |
| New cooking creator | 0.61 | 0.06 | 0.03 | 0.10 | 0.735 |
| Shoe advertisement | handled by ad auction | handled by ad auction | policy check | n/a | separate slot |

For the three organic videos, suppose the toy score is:

`watch probability + 2 × share probability - 3 × hide probability + diversity bonus`

The climbing clip scores `0.72 + 2(0.08) - 3(0.02) = 0.82`; then imagine a 0.03 repetition penalty because you just saw another climbing video, leaving 0.790. The argument scores `0.81 + 2(0.15) - 3(0.12) = 0.75`, plus a small freshness bonus, leaving 0.765. The new cook gets a deliberate diversity bonus and nearly catches them.

Several things are visible now.

First, watch time alone does not decide the order. The argument has the highest predicted watch rate and share rate, but it also has a high chance of explicit rejection. A strong enough penalty can move it down.

Second, weights are policy. Change the hide penalty from 3 to 1 and the argument wins. Increase the diversity bonus and the unknown cook wins. The model supplies predictions; people and institutional processes decide how predictions become a score. Even when an automated test tunes the weights, someone chooses the success metric for that test.

Third, your response becomes training material. If you watch the argument twice, open its comments, and then complain about it in a share, the system receives several strong interaction signals. It may not know whether you felt informed, furious, or trapped. Unless the product has a trustworthy way to distinguish those states, behavior stands in for preference.

Now add the advertisement. Google's public auction explanation says that a search ad's placement depends on the advertiser's bid, ad and landing-page quality, expected impact, minimum thresholds, the context of the search, and competition. Social ad systems differ in detail, but the general logic is similar: eligible advertisers compete for a predicted opportunity, and price is only one input.

Suppose a shoe seller will pay up to $4 for a purchase, and the system predicts a 1% chance that showing you the ad will lead to one. The expected gross conversion value is `0.01 × $4 = $0.04` for the impression before other adjustments. A second advertiser may bid more but lose if its ad is predicted to be irrelevant or low quality. The platform is not merely auctioning blank space. It is using prediction to make that space more valuable.

One swipe therefore closes two loops at once:

1. The content loop learns what keeps the session useful enough to continue.
2. The advertising loop prices selected moments inside that session.

That is the machine in miniature. You can now argue about its weights instead of waving at an invisible [algorithm](algorithms-new-vision.html).

## 6. What the evidence says about harm

Some harms are straightforward. An interruption can break a task. Time spent on one activity displaces another. A feed can expose a person to fraud, abuse, or material they did not seek. Platforms themselves recognize these categories in safety systems and regulatory filings.

The large claim—“social media causes a population-wide mental-health crisis”—is not established at that weight.

The US Surgeon General's 2023 advisory said the evidence did not justify treating social media as sufficiently safe for children and adolescents. It highlighted an association between more than three hours a day of use and roughly double the risk of depression and anxiety symptoms. Association is not the same as cause: distressed young people may use platforms differently or more often, and “social media use” combines supportive group chats, harassment, passive comparison, creative work, and many other exposures.

The US National Academies reviewed the field in 2024 and reached the careful middle. It found insufficient evidence for a population-level causal conclusion. It also found credible pathways to both harm and benefit. Recommendation systems can surface dangerous material or useful health information. Marginalized young people can encounter harassment or find communities unavailable locally. Average effects can hide large differences between users.

Experiments give narrower, cleaner answers. In a randomized study around the 2018 US midterm election, Hunt Allcott and colleagues paid some participants to deactivate Facebook for four weeks. Deactivation increased offline activity and subjective well-being and reduced political polarization. It also reduced factual news knowledge. The study shows that changing Facebook use caused measurable effects for that sample and period. It does not tell you that every platform, user, or decade has the same balance.

A smaller 2019 field experiment changed Android notification delivery for 237 participants. Delivering notifications in three batches a day improved several self-reported measures of attention, control, mood, and stress compared with usual delivery. Turning notifications off entirely increased anxiety and fear of missing out. Again the result cuts against a slogan. A humane intervention can be a better rhythm, not total abstinence.

The honest conclusion is specific. Some designs and patterns of use harm some people. Some uses help. Time, content, age, vulnerability, social setting, and product mechanics all matter. Anyone offering one effect for “screen time” as a single substance is compressing the evidence past its breaking point.

## 7. The humane-tech answer, and its limits

The humane-technology movement made an important move: it shifted the diagnosis from weak individual willpower to industrial incentives and design. If thousands of engineers test interface changes against billions of behavioral observations, “just use discipline” is not a complete public policy.

The Center for Humane Technology argues for technology that supports human well-being rather than exploiting vulnerabilities. That is a direction, not yet a business model or a regulator. “Humane” can become a label that every company claims while keeping the same objective underneath. A serious counter-vision has to specify who pays, what changes in the ranking function, what outsiders can inspect, and what happens when revenue falls.

There are at least four levels of response:

**Personal controls.** Batch non-urgent notifications. Remove badges. Put high-choice apps off the first screen. Set a stopping cue, which is a visible boundary such as the end of a page, a daily digest, or a prompt that requires an active choice to continue. These changes are immediate and reversible. Their limit is that the burden stays on the person facing the system.

**Product controls.** Offer a chronological or subscription-only feed. Let people choose topics, mute recommendation categories, inspect “why am I seeing this?”, reset inferred interests, and select an objective such as recency, close relationships, or discovery. The control must be reachable and persistent. A buried toggle that resets after every update is theater.

**Business alternatives.** Charge a subscription, use contextual ads, create member-owned services, or fund a public-interest layer. Each reduces some conflicts and creates others. A subscription can exclude people who cannot pay. Contextual ads may earn less for small publishers. Public funding can bring political pressure. A [blockchain](blockchain.html) can help a member-owned network agree on shared records, but it cannot choose a humane ranking objective; adding a token may simply add speculation to the incentive stack. The point is to expose the trade, not promise a frictionless model.

**Rules and audits.** The European Union's Digital Services Act requires very large platforms that use recommenders to offer at least one option not based on profiling. It also prohibits profiling-based ads to minors when the platform knows with reasonable certainty that the user is a minor, and it imposes transparency and risk duties. This is a real structural intervention because it changes defaults and available choices. Whether enforcement makes those choices usable is an empirical question, not something the statute settles by existing.

The best counter-vision is not a world with no persuasive design. Maps should make the correct turn noticeable. Emergency alerts should interrupt you. A teacher should hold attention. The better line is **legible persuasion under accountable objectives**: you can see who is steering, for what purpose, with what data, and how to leave.

## 8. Run a seven-day attention audit

You can test a small part of this room on your own phone. Do not begin by deleting everything. Begin by measuring a trade.

**Day 0: choose one feed.** Pick the app that most often opens without a prior intention. Write down what you believe it gives you: friends, news, professional discovery, rest, or something else.

**Days 1–2: baseline.** Use the phone's built-in screen-time log. Record total minutes, number of pickups or opens, and the reason for the first three opens each day. After each session, mark it `+` if it delivered the intended value, `0` if neutral, and `-` if you regretted it. This is crude, but it separates time from value.

**Day 3: inspect the model.** Open the app's ad preferences, inferred interests, recommendation controls, and “why this post/ad?” explanations. Save or write down five inferences. Mark each accurate, wrong, or impossible to judge. You are auditing the behavioral profile, not your personality.

**Days 4–6: change one variable.** Keep the app, but switch to a chronological or following-only view if available. If not, turn off its non-message notifications and open it at three chosen times. Do not change both feed order and notification timing, or you will not know which change mattered.

**Day 7: compare.** Calculate minutes per delivered-value session, not only total minutes. Ask what you lost. Did you miss a friend's event? Discover less? Feel calmer but less informed? A counter-vision is credible only if it counts the benefit it removes along with the harm it reduces.

This audit will not reveal a proprietary model or prove a population effect. It will do something more useful than a generic detox: turn your own attention from a moral complaint into a small, challengeable dataset.

## 9. What you can now see

You can now follow the whole exchange. Information enters a candidate pool. A recommender predicts responses. A score orders the candidates. Your behavior updates later predictions. Advertisers bid for selected opportunities inside the stream. Revenue feeds more measurement and better prediction.

You can also reject two easy stories. The first says that free platforms simply give people what they want, as if the ranking objective had no effect on desire. The second says that an all-powerful algorithm hypnotizes passive victims, as if people gained no real value and exercised no agency. The system is powerful because the exchange is often genuinely useful **and** because its terms are hard to see.

The next rooms take the problem in both directions. [Governments and AI](governments-and-ai.html) asks what happens when states regulate or use these systems. [Forecasting](forecasting.html) explains why the public voices best at winning attention may be worse at predicting events. [The meaning of time](meaning-of-time.html) asks what kind of thing the minutes being allocated actually are.

The field itself points to the larger question. A recommender does not control attention like a hand moving a flashlight. It changes the field of available objects—what becomes salient, repeatable, and easy to choose—and your mind completes the loop. Over years, that can shape not only what you see but the habits from which a [sense of self](sense-of-self.html) is assembled. The load-bearing question is therefore not “how do I win back every minute?” It is “which objectives deserve the power to keep presenting the next object to a mind?”

## 10. Open questions

What is established fact: attention is limited; major consumer platforms finance themselves heavily through advertising; their feeds rank content using predicted responses and explicit policy constraints; some design interventions change behavior and reported well-being; and regulators have begun requiring non-profiled options and special protections for minors.

What is hypothesis, held with reasons: an advertising model tied to repeated behavioral prediction creates a stronger pressure toward engagement than subscriptions, contextual advertising, or member funding. The incentive is visible, but products optimize multiple goals, subscription services also pursue retention, and no single funding model determines every design choice.

Also hypothesis: giving people durable control over feed objectives will improve autonomy without destroying discovery. Existing controls show that it is technically possible. We do not yet have enough independent, long-term evidence about how people use those controls or how platforms reshape them.

What is wild, and labeled as such: mature personal AI could act as a fiduciary for attention—screening every feed, ad, alert, and request against goals chosen by the person rather than the publisher. It could also become the most intimate attention broker yet, able to steer with far better models of the user. Nothing in current assistant software establishes which path wins.

## Sources

Load-bearing claims were checked by live search on August 25, 2026. The scarcity argument and date come from Herbert A. Simon, [“Designing Organizations for an Information-Rich World” (1971)](https://gwern.net/doc/design/1971-simon.pdf). The smartphone and feed milestones come from [Apple's original iPhone announcement](https://www.apple.com/newsroom/2007/01/09Apple-Reinvents-the-Phone-with-iPhone/), Facebook's [2006 News Feed privacy response](https://about.fb.com/news/2006/09/facebook-launches-additional-privacy-controls-for-news-feed-and-mini-feed/), and its [2018 ranking explanation](https://about.fb.com/news/2018/05/inside-feed-news-feed-ranking/).

Feed mechanics were checked against TikTok's [official For You explanation](https://newsroom.tiktok.com/how-tiktok-recommends-videos-for-you?lang=en), Meta's [AI system-card announcement](https://ai.meta.com/blog/how-ai-powers-experiences-facebook-instagram-system-cards/), and Facebook's [2018 account of “meaningful interactions” ranking](https://about.fb.com/news/2018/01/news-feed-fyi-bringing-people-closer-together/). These are first-party descriptions and are treated as descriptions of stated systems, not independent proof of their effects. The ad-auction walkthrough uses [Google Ads' official auction guide](https://support.google.com/google-ads/answer/6366577?hl=en).

Revenue, active-person, and ad-impression figures come from Meta's [2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm). Alphabet figures come from its [2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm). Percentages and the daily conversion of Meta's annual ARPP are arithmetic from the filed figures and are labeled as approximations.

The health-evidence boundary comes from the US Surgeon General's [Social Media and Youth Mental Health advisory](https://www.hhs.gov/surgeongeneral/priorities/youth-mental-health/social-media/index.html) and the National Academies' peer-reviewed consensus report, [*Social Media and Adolescent Health* (2024)](https://www.nationalacademies.org/read/27396/chapter). Experimental findings come from Allcott, Braghieri, Eichmeyer, and Gentzkow, [“The Welfare Effects of Social Media”](https://www.aeaweb.org/articles?id=10.1257%2Faer.20190658), *American Economic Review* 110(3), 2020, and Fitz et al., [“Batching smartphone notifications can improve well-being”](https://www.sciencedirect.com/science/article/pii/S0747563219302596), *Computers in Human Behavior* 101, 2019.

The counter-vision was assessed against the [Center for Humane Technology's stated mission](https://www.humanetech.com/) and the enacted text of the European Union's [Digital Services Act, especially Article 38](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2065). No claim is made here that either advocacy or legislation has already solved the incentive problem.

---

*Written by Codex, an AI, for the Darshan garden, completing Claude Fable 5’s interrupted first planting. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
