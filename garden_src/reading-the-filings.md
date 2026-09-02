---
title: Reading the Filings Cold
slug: reading-the-filings
series: silicon
tags: investing, filings, tsmc, asml, earnings-calls, capex, margins, inventory, reverse-expectations
summary: A filing turns an AI story into revenue mix, capital spending, margins, concentration, inventory, and risks. This room reads TSMC and ASML from the statements outward, then rebuilds TSMC's latest quarter so the process can be repeated next time.
status: draft
date: 2026-09-02
terms_defined: revenue-mix, capex, gross-margin, inventory-days, reverse-expectations
terms_linked: necessity-and-capture, the-capital-cycle, advanced-packaging, the-memory-wall, chip-wars, semiconductors, forecasting
---

# Reading the Filings Cold

You have a fresh annual report, a quarterly deck, and a transcript open in three tabs. Do not begin with the chief executive's letter. Begin with what was sold, what it cost, what the company built, and what could break. This room uses TSMC and ASML because both sit near the center of the [semiconductor](semiconductors.html) machine and disclose very different businesses.

## 1. Build a document stack before you build a story

A Form 20-F is the annual filing used by many foreign private issuers in US markets. It contains audited financial statements, business description, risk factors, operating discussion, governance, and exhibits. TSMC filed its 2025 20-F on 16 April 2026. ASML filed its 2025 annual report with the SEC on 25 February 2026.

The filing is not pure truth. Management chooses categories, estimates useful lives, tests impairment, and writes risks with lawyers. It is still the record: dated, internally reconciled, audited at the financial-statement level, and exposed to securities law. An investor deck is a selection from that record. A prepared earnings script is management's interpretation of a new period. The question-and-answer session is a live test of that interpretation.

Use this order on a first read:

1. Confirm the reporting period, currency, accounting basis, and document date.
2. Read the income statement, balance sheet, and cash-flow statement without commentary.
3. Find the segment and revenue-mix tables.
4. Reconcile capital expenditure with the cash-flow statement and current guidance.
5. Read the gross-margin bridge and the long list of margin drivers.
6. Find customer, supplier, geography, and product concentration.
7. Calculate or locate inventory days and compare with the business model.
8. Read risk factors for dependencies management must put on the record.
9. Read prepared remarks, then Q&A, marking every answer that narrows, refuses, or contradicts the story.

This order delays persuasion until you have a skeleton. It also enforces Seeing the Silicon's distinction: **technological importance ≠ economic capture ≠ business quality ≠ investment attractiveness.** A filing can help with the middle two. It cannot finish the fourth without a dated price and explicit expectations.

| What you need | TSMC: where it lives | ASML: where it lives | Common trap |
|---|---|---|---|
| Revenue and profit | Quarterly management report; 20-F statements and Item 5 | Annual financial statements; quarterly financial release | Mixing quarter, year, currency, or accounting basis |
| Node or product mix | Quarterly management report; node share is wafer revenue | System sales by EUV/DUV and end use; annual sales notes | Treating unlike denominators as one market-share table |
| Platform or customer use | Quarterly platform mix; annual Item 4 | Logic/memory system sales; geography and customer notes | Inferring a node-by-platform cross-tab that is not disclosed |
| Capex spent | Cash-flow statement and management report | Cash-flow statement and property note | Calling a budget cash already spent |
| Capex guidance | Earnings presentation, prepared remarks, Q&A | Earnings release and call | Using superseded guidance without its date |
| Gross-margin drivers | Quarterly bridge; 20-F Item 5 | Annual operating review; quarterly CFO remarks | Explaining margin with mix alone |
| Customer concentration | 20-F Item 3 risk factors | Revenue-concentration note | Confusing customer headquarters with named customers |
| Inventory | Quarterly KPI plus balance sheet | Balance sheet; derive days if useful | Comparing a foundry's days directly with a toolmaker's |
| Risks | 20-F Item 3 | Strategic report and risk section | Quoting boilerplate without linking it to numbers |
| Management uncertainty | Q&A refusals, ranges, changed language | Official call audio; written official transcript may omit Q&A | Treating prepared remarks as the whole call |

## 2. TSMC: read node, platform, and geography as separate maps

TSMC is a foundry: it manufactures designs supplied by customers. That creates several valid ways to cut revenue.

The 16 July 2026 management report gives **node mix** as a share of wafer revenue. In the second quarter of 2026, 2-nanometer technology was 3%, 3nm was 30%, 5nm was 33%, and 7nm was 11%. Nodes at 7nm and below were 77% in total. These labels identify TSMC process generations; they do not state literal transistor dimensions.

The same report gives **platform mix** as a share of net revenue. High-performance computing, or HPC, was 66%; smartphones 22%; internet of things 5%; automotive 4%; digital consumer electronics 1%; and other 2%. HPC revenue rose 20% from the first quarter; smartphone revenue fell 4%.

Then comes **customer geography**. North America was 78% of second-quarter net revenue, Asia-Pacific 8%, China 6%, Japan 4%, and Europe, Middle East, and Africa 4%. This is based on customer headquarters. It is not fabrication location and it is not a claim that one North American customer supplied 78%.

Do not multiply the columns. TSMC does not disclose a node-by-platform-by-customer cube. You cannot conclude from 66% HPC and 33% 5nm that a particular percentage of company revenue was an AI accelerator on 5nm. That may be a plausible story; it is not a filed number.

The annual filing supplies the slower map. In 2025, TSMC reported HPC revenue of NT$2,192.9 billion, 58% of company revenue, and smartphone revenue of NT$1,110.8 billion, 29%. It also disclosed concentration that the quarterly geography table cannot answer. Its top ten customers accounted for 70%, 76%, and 78% of revenue in 2023, 2024, and 2025. The largest customer accounted for 25%, 22%, and 19%; the second-largest for 11%, 12%, and 17%. The filing does not name them.

These sequences tell you something a single year hides. Top-ten concentration rose while the largest customer's share fell and the second-largest rose. That is not automatically better or worse. It gives you questions: Are several large programs scaling together? Does bargaining power shift? What happens if one program changes foundry, node, or timing?

## 3. Capex is a pipeline, not a capacity number

Capital expenditure, or capex, is cash spent on long-lived productive assets such as buildings and equipment. For a foundry, capex precedes qualified output through site work, construction, tool installation, process qualification, and customer ramp. The familiar “18–24 month lag” is a useful analyst heuristic for parts of that journey, but it is not a uniform rule stated in the TSMC documents reviewed here. A greenfield fab, an equipment addition inside an existing shell, advanced packaging, and a process conversion run on different clocks. Use disclosed milestones when they exist; mark the lag **UNKNOWN** when they do not.

TSMC's cash-flow statement tells you what was spent. The second-quarter 2026 management report recorded NT$496.0 billion of quarterly capex; the CFO translated that as $15.7 billion on the call. Operating cash flow was NT$783.4 billion, leaving free cash flow of NT$287.4 billion under the simple operating-cash-flow-minus-capex definition.

The call tells you the current plan. In January 2026, management guided to $52–56 billion for the year. On 16 July it raised that range to $60–64 billion. It allocated 70–80% to advanced process technologies, about 10% to specialty technologies, and 10–20% to advanced packaging, testing, mask-making, and other items.

The Q&A prevents false precision. Asked for more detail on backend spending, management said the bottleneck moves among packaging, testing, and other tools, so it would not split the bucket more finely. Asked why the total increased, it cited stronger demand and tool-price inflation. Asked for a firm schedule behind the announced US investment program, management declined a three- or five-year timetable and said timing depends on customer demand.

That gives you three distinct objects:

- NT$496.0 billion: cash spent in one quarter.
- $60–64 billion: management's revised full-year budget range as of 16 July 2026.
- US fab announcements: multi-year intentions whose exact timing management would not commit to in Q&A.

If you call all three “capex,” you can make capacity appear sooner than the company says it will.

## 4. Gross margin is where the physical system reaches the accounts

Gross margin is revenue minus direct cost of revenue, divided by revenue. It is not a pure measure of pricing power. At a fab, it reflects utilization, wafer price, product and node mix, yield, depreciation, electricity, materials, foreign exchange, and the cost curve of new and overseas facilities.

TSMC reported a 67.7% gross margin for the second quarter of 2026, up 1.5 percentage points from the first quarter's 66.2% and 9.1 points from the second quarter of 2025. Its management report attributed the sequential rise mainly to cost improvement and higher capacity utilization, partly offset by dilution from overseas fabs.

Now read forward-looking puts and takes as management claims, not facts. On 16 July, TSMC said the 2nm ramp could dilute second-half 2026 gross margin by about 3–4 percentage points. It expected overseas-fab dilution of 2–3 points early, widening later to 3–4 points. It named leading-edge demand, cost improvement, productivity, cross-node optimization, and currency as offsets. Next quarter, do not merely compare actual margin with guidance. Rebuild the bridge: which stated headwinds appeared, which offsets were stronger, and which explanation changed?

The 2025 20-F gives the structural list. Annual gross margin was 59.9% in 2025 and 56.1% in 2024. The filing says utilization, price, cost improvement, product mix, exchange rates, and new-node introductions all matter. It attributed the annual increase mainly to utilization and cost improvement, partly offset by currency. The filing keeps you from attributing every move to AI mix.

[The capital cycle](the-capital-cycle.html) adds one more question. High utilization and scarcity raise margin. The same margin calls forth capex, depreciation, supplier expansion, and customer alternatives. A margin bridge is a snapshot of that physical cycle reaching the income statement.

## 5. Inventory days and concentration: compare the business with itself

Inventory days estimate how long inventory sits before passing through cost of sales. A simple annual formula is average inventory divided by annual cost of sales, multiplied by 365. TSMC reports the KPI directly each quarter. ASML does not report it as a headline KPI in the materials reviewed here.

TSMC's second-quarter 2026 inventory was NT$385.5 billion and inventory days were 87, up from 80 in the first quarter and 76 a year earlier. The company attributed the seven-day sequential rise mainly to the N2 ramp. Accounts-receivable days rose to 29 from 26 in the first quarter and 23 a year earlier. Those movements are not verdicts. A new-node ramp can deliberately build work in process. A persistent rise without the promised revenue conversion would mean something different.

ASML's 2025 annual report gives net inventory of €11.43 billion, up from €10.89 billion in 2024, and annual cost of sales of €15.41 billion. Using average beginning-and-ending inventory gives roughly 264 inventory days. That is a derived figure, not one ASML reports, and it is not directly comparable with TSMC's 87 days. ASML builds a small number of complex systems with long assembly and acceptance cycles; TSMC moves wafers through a different production flow.

Concentration needs the same care. ASML reported 2025 sales of €32.67 billion and a 52.8% gross margin. Its largest customer supplied €7.80 billion, or 23.9%, of sales; its top two supplied 38.0%. China represented 29.1% and Taiwan 25.5% of sales by customer location. One table is customer concentration; the other is geography. They answer different risks.

The most useful comparison is not “Which company has fewer inventory days?” It is “What must be true in this business for inventory to convert to revenue, and did that conversion improve or deteriorate?” For ASML, examine system mix, shipment, customer acceptance, field upgrades, and export licenses. For TSMC, examine utilization, work in process, node ramp, yield, and customer tape-outs.

## 6. Risk factors and Q&A: the record meets the sales pitch

Prepared remarks are not useless. They give a clean management bridge and current guidance. But they are rehearsed. Q&A lets analysts choose the seam. The annual filing lists risks management and counsel judged material enough to disclose.

TSMC's 2025 20-F names geopolitical and export-control exposure, concentration of operations in Taiwan, higher cost and execution risk in global expansion, demand-capacity mismatch, customer concentration, limited-source equipment, raw-material and sole-source dependencies, power and water interruption, and foreign exchange. You do not need to copy the whole list. Connect each risk to an operating number.

Customer concentration offers a live example. The filing calls reliance on a concentrated customer base a vulnerability and supplies the 78% top-ten figure for 2025. In the 16 July 2026 Q&A, an analyst asked about rising top-five concentration. The chief executive said it was not a concern because new AI customers were emerging. Both statements belong in your notes:

- Filed record: concentration can materially affect results.
- Management's current view: the customer set is broadening within AI, so the concentration does not cause concern.
- Analyst's task: watch the actual top-customer shares, bargaining terms, receivables, capacity commitments, and new-program revenue.

ASML teaches a document-handling trap. Its official Q2 2026 PDF is titled as an investor-call transcript, but the document ends after prepared remarks with an invitation to take questions. The official results page hosts the audio replay, which is the primary Q&A record. A searchable third-party transcript can be a map, but any consequential wording should be checked against the audio. The absence of Q&A from an official PDF is itself something to notice.

ASML's annual report names semiconductor cyclicality, dependence on a small number of products and customers, export controls, intellectual property, supply-chain concentration, and specialized talent. Its 2025 report also says Zeiss is the sole source of critical optics and that losing that supply for a prolonged period would effectively halt the business. [The chip wars](chip-wars.html) explains the strategic consequence. The filing shows the business consequence.

## 7. Reverse expectations: translate price into operating claims

Alfred Rappaport and Michael Mauboussin call the method expectations investing. A conventional valuation begins with your revenue and margin forecast and produces an estimated value. A reverse-expectations model begins with the market value and asks which operating path makes the discounted cash flows equal it.

The point is not to discover “the” growth rate hidden inside a price. Many combinations of growth, margin, reinvestment, discount rate, and duration can produce the same value. The point is to make the required claims visible.

Use this sketch:

1. Date every market input: share price, diluted shares, debt, cash, investments, and minority interests.
2. Reconcile from equity value to enterprise value.
3. Build operating free cash flow: revenue, operating margin, cash tax, and incremental investment needed for growth.
4. State a discount rate and mature-state assumptions.
5. Hold most drivers fixed. Extend one revenue-growth and margin path until discounted operating value plus non-operating assets equals the current enterprise value.
6. Run a second path: hold growth fixed and solve for margin, or hold margin fixed and solve for the duration of excess returns.
7. Compare each implied operating claim with capacity, customer demand, competition, and the company's own record.

For TSMC, the growth claim must respect capex and capacity timing. The margin claim must respect new-node and overseas-fab dilution. The reinvestment claim must reconcile with actual capex. For ASML, the path must respect system capacity, customer concentration, product mix, service revenue, supplier constraints, and the timing of customer acceptance.

This room does not insert a current share price or produce a verdict. A price would go stale; an investment conclusion would depend on choices the reader must own. The method is the durable part. [Necessity and capture](necessity-and-capture.html) tells you why monopoly cannot substitute for it.

## 8. Worked example: rebuild TSMC's second quarter of 2026

The latest reported TSMC quarter available on 2 September 2026 was the quarter ended 30 June 2026, released on 16 July. Open the quarterly management report, presentation, financial statements, transcript, and 2025 20-F from TSMC's investor site. Then fill this sheet.

| Pass | Number or statement | Where it came from | What to ask next quarter |
|---|---|---|---|
| Scale | Revenue NT$1,270.38bn / US$40.20bn; +12.0% QoQ, +36.0% YoY in NT$ | Q2 management report, 16 Jul 2026 | Did volume, currency, price, or mix drive the change? |
| Profit | Gross margin 67.7%; operating margin 60.3% | Q2 management report | Rebuild the utilization, cost, FX, overseas, and N2 bridge |
| Nodes | 2nm 3%, 3nm 30%, 5nm 33%, 7nm 11%; ≤7nm 77% of wafer revenue | Q2 management report | Did the N2 ramp convert inventory into wafer revenue? |
| Platforms | HPC 66%, smartphone 22%; HPC +20% QoQ, smartphone −4% | Q2 management report | Keep platform denominator separate from wafer-node denominator |
| Geography | North America 78% of net revenue | Q2 management report | Do not call this one-customer share; compare with annual concentration |
| Working capital | Inventory NT$385.53bn; 87 days versus 80 QoQ and 76 YoY | Q2 management report | Does the company still attribute the rise to N2 ramp? |
| Cash and build | Operating cash flow NT$783.36bn; capex NT$496.00bn; simple FCF NT$287.36bn | Q2 management report and statements | Does capex track the revised budget and disclosed allocation? |
| Current guide | Q3 revenue US$44.6–45.8bn; gross margin 65–67%; operating margin 56–58% | Q2 presentation, 16 Jul 2026 | Record the miss or beat by driver, not only direction |
| Annual capex | Revised to US$60–64bn from Jan's US$52–56bn | Q2 transcript | Separate demand-driven addition from tool inflation and timing |
| Filed concentration | Top ten 78%; largest 19%; second-largest 17% in 2025 | 2025 20-F, filed 16 Apr 2026 | Compare the next annual shares with Q&A's broadening claim |
| Filed risks | Taiwan/geopolitics; overseas execution; demand-capacity mismatch; customers; suppliers; power/water; FX | 2025 20-F Item 3 | Attach each risk to a metric or dated event |

Now write a five-sentence quarter note. Sentence one: scale and profit. Sentence two: node and platform mix, with denominators named. Sentence three: inventory and capex. Sentence four: the margin bridge. Sentence five: the most important tension between filing and Q&A.

A defensible version is: TSMC's second-quarter revenue reached NT$1,270.38 billion and gross margin reached 67.7%. Advanced nodes were 77% of wafer revenue, while HPC was 66% of net revenue; those are separate cuts. Inventory days rose to 87 during the N2 ramp, and quarterly capex was NT$496.0 billion. Utilization and cost improvement lifted margin while overseas fabs diluted it, with management identifying N2 and overseas ramps as later headwinds. The filing records rising customer concentration as a risk; management says new AI customers make it unconcerning, so the next annual customer-share table is the resolving evidence.

Save the table with blank columns for the next quarter. Repetition is the advantage. You are no longer reading each release as a new story. You are watching the same physical and economic variables change.

## 9. What you can now see

You can now open a TSMC or ASML report without accepting its order of emphasis. Revenue mix tells you what sold. The cash-flow statement tells you what was built. Margin drivers show where utilization, cost, mix, currency, and new capacity reached the accounts. Concentration and inventory tell you where conversion can fail. Risk factors name dependencies; Q&A shows which ones analysts can make management discuss.

From here, [the capital cycle](the-capital-cycle.html) turns capex and utilization into a dated supply response. [The memory wall](the-memory-wall.html) and [advanced packaging](advanced-packaging.html) supply the physical on-ramp for HBM and CoWoS, so the categories in the filing become equipment you can picture. [Forecasting](forecasting.html) gives you the discipline for writing the signpost that changes an expectation.

## Open questions

**Established (FACT):** TSMC's second-quarter 2026 revenue, margins, mix, inventory days, cash flow, and capex are reported in its 16 July management report and statements. The 2025 20-F discloses customer concentration and operating risks. The July call revised 2026 capex above the January range. ASML's official written Q2 2026 transcript omits the Q&A while its results hub hosts the audio.

**Contested (HYPOTHESIS):** TSMC's higher inventory days mainly reflect a healthy N2 ramp rather than demand or yield friction; management supplied the explanation, and later conversion must test it. New AI customers reduce economic dependence even if reported top-customer concentration remains high. A general 18–24 month capex-to-capacity lag is useful enough for first-pass analysis despite project-specific variation.

**Speculation worth holding (WILD):** If TSMC's inventory days fall while 2nm wafer-revenue share rises, then the Q2 inventory build behaved like planned ramp inventory by 31 December 2026; TSMC's Q3 and Q4 management reports resolve it. If annual top-ten or top-two customer share rises again, then management's broadening-customer answer did not reduce reported concentration by 30 April 2027; the 2026 20-F resolves it. If 2026 capex finishes outside the revised $60–64 billion range without a disclosed timing or currency bridge, then the capacity plan changed again by the full-year call in January 2027; the cash-flow statement and transcript resolve it.

There is a quieter reason to read this way. A filing is a map of institutional attention: what management measures every quarter, what auditors make comparable, what lawyers insist must be named, and what remains outside the categories. Learning to notice both the table and the omission changes what the business is for you. It stops being a ticker or a story and becomes a group of people allocating matter, time, and risk under promises that later documents can check.

## Sources

- TSMC, [2026 financial calendar](https://investor.tsmc.com/english/financial-calendar), accessed 2 September 2026, and [SEC filings index](https://investor.tsmc.com/english/sec-filings), accessed 2 September 2026. Used to establish the latest available quarter and annual filing.
- TSMC, [2025 Form 20-F](https://investor.tsmc.com/sites/ir/sec-filings/2025_20F%20Report.pdf), filed 16 April 2026. Platform revenue, annual margin, customer concentration, capex, and risk factors.
- TSMC, [Q2 2026 Quarterly Management Report](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/6f49632674bd2d0fd48cb65aaf89ec6ab510b559/2Q26%20ManagementReport.pdf), 16 July 2026. Revenue, profit, node/platform/geography mix, margin bridge, inventory days, receivables, cash flow, and capex.
- TSMC, [Q2 2026 presentation](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/0e4d9625c9ef46521afd54002f835e45a9035043/2Q26%20Presentation%20(E).pdf), 16 July 2026. Company guidance.
- TSMC, [Q2 2026 financial statements](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/114aaca0fea2050e96b91fffbab9ed04ba09cd92/FS.pdf), 16 July 2026. Primary statements.
- TSMC, [Q2 2026 earnings-call transcript](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf), event held 16 July 2026. Revised capex, allocation, margin puts and takes, capacity planning, US schedule, customer-concentration answer, and Q&A limits.
- ASML, [2025 Annual Report based on US GAAP](https://ourbrand.asml.com/m/71076aaad607de4d/original/asml-2025-annual-report-based-on-us-gaap.pdf), filed 25 February 2026; [SEC filing index](https://www.sec.gov/Archives/edgar/data/937966/000162828026011378/0001628280-26-011378-index.htm). Sales, gross margin, customer and geographic concentration, inventory, cost of sales, and risks.
- ASML, [Q2 2026 financial statements](https://ourbrand.asml.com/asset/ffeb8813-403b-49df-83c0-01aae7533dd6/Financial-statements-US-GAAP-Q2-2026.pdf), 15 July 2026; [official prepared-remarks PDF](https://ourbrand.asml.com/asset/1fd3908a-0381-47b5-9b69-a3094f656651/2026_07_15-ASML-Transcript-investor-call-Q2-2026.pdf); and [results hub with call audio](https://www.asml.com/en/investors/financial-results/q2-2026). Used to distinguish official statements, prepared remarks, and Q&A record.
- Alfred Rappaport and Michael J. Mauboussin, [“The Approach — Expectations Investing”](https://www.expectationsinvesting.com/about) and [Online Tutorial 8: Price-Implied Expectations Analysis](https://www.expectationsinvesting.com/online-tutorial-8), publication date not displayed, accessed 2 September 2026. Primary author source for the reverse-expectations method and free spreadsheet.
- Michael J. Mauboussin and Dan Callahan, [*Everything Is a DCF Model*](https://www.morganstanley.com/im/publication/insights/articles/article_everythingisadcfmodel_us.pdf), Morgan Stanley Counterpoint Global, 3 August 2021. Discounted-cash-flow framework.

*Written by Codex, an AI, for Seeing the Silicon, a wing of the Darshan garden. John Shrader (Dhyana), founder and publisher of record, answers for every word published here. Errors are corrected on the face of the page, dated.*
