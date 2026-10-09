---
title: "Supporting Information"
subtitle: "Instrument-level coding matrix for \"Incentive Design, Ownership, and the Risk of an AI-Era Middle-Technology Trap in Southeast Asia\""
---

## Purpose

This document gives the instrument-level data behind Tables 1 to 5 of the manuscript, so that the coding can be replicated. Each row is one instrument: a specific tax exemption, grant, eligibility rule or compliance requirement. The unit of analysis is the instrument, not the strategy document. A single scheme, such as Thailand's digital division, bundles several instruments, and each is coded in its own row. Table S1 holds 29 instruments, in four blocks by country; Tables S2 to S4 give the sources, the full evidence matrix and an illustrative ladder. Rows 1 to 20 are the first-coded instruments, and rows 21 to 29 were added when the primary texts were read in full for the compute layers.

## How to read Table S1

The columns follow the codebook given below.

- **Layer.** (i) applications and models; (ii) cloud and compute services; (iii) physical data-centre capacity; (ii)+(iii) where one instrument covers both and does not distinguish them; (iv) hardware; or cross-cutting where the instrument applies across activity types without targeting a layer.
- **Delivery.** *Indirect* for tax-based instruments that presuppose taxable profit or investment expenditure. *Direct* for grants, equity, fee waivers and interest support. *Eligibility status* for a rule that confers a status and attaches no benefit itself.
- **Threshold and basis.** The rule as stated in the source, in local currency, with its basis (annual spend, paid-up capital, minimum capital, cumulative capital expenditure, firm-scale investment capital, power capacity, or a proportional ratio). "None stated" means the source states no threshold. It does not mean zero.
- **New-firm accommodation.** *Yes* only for an explicit provision easing access for smaller or newer firms. *No* otherwise, even when the threshold is low. *Not scale-based* for a proportional requirement. *Not applicable* for a designation or discretionary power.
- **Recurring compliance burden.** Annual or ongoing obligations attached to continued eligibility, distinct from one-off application requirements. Fixed-cost obligations are marked as such.
- **Verification.** The text read and the date of the check. All rows were checked against the cited primary text on 9 October 2026 (authors to confirm). A second reading by an independent person is still to be done (see the reliability section).

Converted figures use the rates of the Currency section. A converted figure is an approximation for comparison, not a quotation from the source.

## Table S1. Instrument-level coding matrix

### Thailand (Board of Investment)

| No. | Instrument | Layer | Delivery | Threshold and basis | New-firm accommodation | Recurring compliance | Verification |
|---|---|---|---|---|---|---|---|
| 1 | Software, digital platform and digital-content development (Activity 8.1.1, tier A2) | (i) | Indirect: eight-year corporate income tax exemption, annual cap at 100% of actual qualifying expenditure | At least THB 1.5m a year (about US$42,000), annual spend on salaries of additionally employed Thai IT staff; development must take place in Thailand; retail and wholesale sales excluded | No | Standard BOI reporting | Investment Promotion Guide 2026, Activity 8.1.1 |
| 2 | Research and development (Activity 10.2, tier A1) | (i) | Indirect: corporate income tax exemption | At least THB 1.5m a year of new R&D salaries (about US$42,000, annual spend), **or** capital investment of at least THB 1m (about US$28,000) excluding land, working capital and vehicles | No | Standard BOI reporting | Guide 2026, Activity 10.2 |
| 3 | Competitiveness-enhancement measure (extension of the exemption; Announcement 10/2565) | Cross-cutting (all activity groups) | Indirect: extension by one year, and by up to five years, to a maximum of 13 years | Spending of at least 1% of sales in the first three years, or THB 200m (about US$5.6m), whichever is lower, for one year; 5% of sales or THB 1,000m for the maximum; basis proportional to sales | No: presupposes sales in the first three years | Monitoring of spending against sales | Guide 2026 and Announcement 10/2565 as restated in the Guide |
| 4 | GPU-based data hosting (Activity 8.2.4.1, tier A2); other data hosting (8.2.4.2, tier A3) has the same capital condition | (ii)+(iii) | Indirect: corporate income tax exemption | At least THB 5,000m (about US$140m) of capital investment excluding land and working capital; location in at least two certified data centres | No | Certification regime of the host data centres | Guide 2026, Activity 8.2.4 |
| 5 | Trade and Investment Support Office, including internationally delivered business-process outsourcing (Activity 10.1.1, tier B) | Cross-cutting (services) | None: tier B carries no corporate income tax exemption | At least THB 10m a year (about US$280,000) of selling and administrative expenses | No | Standard registration | Guide 2026, Activity 10.1.1 |
| 6 | Distribution centres with smart systems (Activity 10.11.1, tier A2) | Cross-cutting | Indirect: corporate income tax exemption | Capital investment of at least THB 1,000m (about US$28m) excluding land and working capital; within three years, Thai staff with science or technology degrees (engineering, AI, data science) of at least 20% of employment, use of a data centre or colocation in Thailand, and data-analytics activity | Staffing ratio: not scale-based; the capital condition is scale-linked, so No | Staffing-ratio compliance | Guide 2026, Activity 10.11.1 |
| 21 | Cloud services (Activity 8.2.2, tier A2) | (ii) | Indirect: corporate income tax exemption | **No minimum capital.** Location in at least two ISO/IEC 27001-certified data centres in Thailand, interconnected at 10 Gbps or more with a backup link; ISO/IEC 27001 for cloud security and ISO/IEC 20000-1 held before using the exemption | No | Fixed certification costs (ISO/IEC 27001 and 20000-1) | Guide 2026, Activity 8.2.2 |
| 22 | Data centres (Activity 8.2.1, two tiers) | (ii)+(iii) | Indirect: corporate income tax exemption | Electrical system for at least 2 MW of IT load in both tiers (basis power capacity; no capital minimum stated); four high-speed links; concurrent maintainability; plan of benefits to Thailand; Thai personnel in at least half of executive and expert positions within three years; the higher tier also requires a power usage effectiveness of 1.3 or lower | No | ISO/IEC 27001 certification; power usage effectiveness in the higher tier | Guide 2026, Activity 8.2.1; Announcement Sor. 9/2568 |

### Vietnam

| No. | Instrument | Layer | Delivery | Threshold and basis | New-firm accommodation | Recurring compliance | Verification |
|---|---|---|---|---|---|---|---|
| 7 | Research-centre track (Decree 260/2026, Article 8) | (i) (research institutions) | Direct (funding of tasks up to 100%, interest support, fee waivers) and indirect (duty exemption, cost deduction) | At least 60% of workers in R&D (70% for strategic technology); of these at least 85% with a bachelor's degree and 10% with a master's (20% and 5% doctorates for strategic technology); R&D spending at least 65% of annual operating expenditure (70%); all proportional ratios | No: restricts the track to purpose-built research institutions | Staffing and spending ratios | Decree 260/2026, read in full |
| 8 | Startup track (Decree 260/2026, Article 11) | (i) | Direct: 100% fee exemption for three years then 50% at state research facilities, controlled testing, priority for equity and fundraising support; also indirect | R&D on listed technology; innovative solution with average revenue growth of at least 20% a year over two consecutive years (firms at least three years old), or ready for commercialisation with a feasible plan; capacity to expand the market. Recognition by the provincial People's Committee within 40 days, for five years | Yes: explicit startup track | Annual report; inspection after 12 months and every two years; revocation for false declarations or 12 months of inactivity | Decree 260/2026, Article 11 |
| 9 | National Venture Capital Fund priority consideration (startup track benefit) | (i) | Direct (equity) | Priority consideration for co-investment, investment, guarantees and fundraising support, conditional on startup recognition. NATIF is a separate instrument that supports interest on bank loans and does not lend | Yes | None beyond recognition | Decree 260/2026, Articles 4, 5 and 11 |
| 10 | Strategic technology products, Group 1: Vietnamese-language large language models, virtual assistants and specialised AI (item 1) | (i) | Designation; no benefit attached in the Decision | None stated | Not applicable | None in the Decision | Decision 21/2026/QĐ-TTg, Annex II |
| 11 | Strategic technology products, Group 1: cloud-computing platforms (item 4) | (ii), scope to be confirmed | Designation | None stated; the item has no definition | Not applicable | None in the Decision | Decision 21/2026/QĐ-TTg, Annex II |
| 12 | Strategic technology products, Group 1: edge-processing AI cameras (item 2) and digital-twin platforms (item 3) | (i) | Designation | None stated | Not applicable | None in the Decision | Decision 21/2026/QĐ-TTg, Annex II |
| 13 | Strategic technology products, Group 2: specialised chips | (iv) | Designation | None stated | Not applicable | None in the Decision | Decision 21/2026/QĐ-TTg, Annex II |
| 24 | Technology-infrastructure support, including computing and data infrastructure (Decree 260/2026, Articles 3, 4(6), 5(6)) | (ii)+(iii), for research tasks | Indirect: investment cost deductible for corporate income tax | None stated | Not applicable | None stated | Decree 260/2026; coverage of a small commercial provider not confirmed |
| 25 | Strategic-technology enterprise criteria (Decree 260/2026, Article 16) | Cross-cutting | Eligibility status | At least 80% of annual net revenue from strategic products; R&D spending in Vietnam at least 1% of net revenue less inputs; R&D staff with college degrees or above at least 10% of the workforce; local content at least 40%; all proportional | No: not scale-based, but the revenue condition presupposes a product already earning revenue | Verification and inspection under Article 17 | Decree 260/2026, Article 16 |
| 26 | High-technology enterprise ratios (Decree 260/2026, Articles 14 and 15, Group 2) | Cross-cutting | Eligibility status | R&D spending of at least 0.5% of net revenue less inputs where total capital is VND 6,000bn or more, 1% where it is VND 100bn or more, 2% otherwise; research staff of at least 1%, 2.5% or 5% of the workforce on the same tiers; basis firm size, ratios fall as the firm grows | No | Ratio compliance | Decree 260/2026, Articles 14 and 15 |

### Malaysia

| No. | Instrument | Layer | Delivery | Threshold and basis | New-firm accommodation | Recurring compliance | Verification |
|---|---|---|---|---|---|---|---|
| 14 | Malaysia Digital (MD) New Investment Incentive, covering ten technology enablers including AI and big data and cloud | (i) and (ii) | Indirect: reduced tax rate or investment tax allowance for ten years | Malaysian-resident company with at least RM50,000 paid-up capital (about US$11,000; company capital); new activity with no prior sales invoice; adequate full-time staff, including knowledge workers at RM5,000 a month or more | No: a low capital floor is recorded as a threshold | Annual self-declaration within seven months of year end, verified by an external auditor appointed at the company's own cost (fixed cost) | MDEC guideline, revised July 2025 |
| 15 | Digital Ecosystem Acceleration (DESAC): capitalisation floor, both tiers | (ii)+(iii) | Indirect: investment tax allowance of 100% (Tier 1) or 60% (Tier 2) on qualifying capital expenditure excluding land, for five or ten years, or special tax rate of 10% or 15% | Paid-up capital of at least RM2.5m (about US$550,000; company capital, not project scale) | No | External auditor verification of compliance; annual report for the special-rate option | MIDA DESAC guideline (December 2024) |
| 16 | DESAC ten-year option | (ii)+(iii) | Indirect | Cumulative capital expenditure of at least RM1bn (about US$220m) in years six to ten; for existing companies expanding, Tier 1 adds RM300m over five years | No | As row 15 | MIDA DESAC guideline |
| 17 | DESAC workforce conditions | (ii)+(iii) | Indirect (attached condition) | Tier 2: full-time Malaysian staff earning at least RM5,000 a month making up at least half of manpower; Tier 1 adds high-value jobs of RM10,000 a month or more and at least three local vendor programmes | Not scale-based: proportional requirement | Staffing-ratio compliance | MIDA DESAC guideline |
| 23 | Data-centre categories in the sustainable-development guideline that governs DESAC data-centre applications | (iii) | Design conditions attached to the incentive | Smallest category: low-voltage facility of 0.85 MW to under 4.25 MW (basis power capacity); targets for power usage effectiveness and water usage effectiveness by category | No | Efficiency targets | MITI guideline (December 2024), hosted by MIDA |

### Philippines

| No. | Instrument | Layer | Delivery | Threshold and basis | New-firm accommodation | Recurring compliance | Verification |
|---|---|---|---|---|---|---|---|
| 18 | Standard registration under the CREATE MORE Act and its implementing rules | Cross-cutting | Indirect: income tax holiday followed by special corporate income tax or enhanced deductions | None stated in the Act or the implementing rules. The project must be listed in the Strategic Investment Priority Plan, meet the Plan's qualifications and ownership rules, and be within the corporate powers; the agency registers any listed project regardless of capital | No | Cost-benefit analysis at application; documents including audited financial statements where applicable and projections without incentives for the whole period; FIRB monitoring | RA 12066; implementing rules (signed 17 February 2025) |
| 19 | Firm-scale boundary and high-value domestic market enterprise | Cross-cutting (firm scale) | Indirect: longer availment (up to 14 to 17 years under the agency tier, 24 to 27 years under the FIRB tier) | Investment capital above PHP 15bn (about US$260m) routes the project to the FIRB, which may raise the figure; a high-value domestic market enterprise has more than PHP 15bn in import-substituting sectors or export sales of at least US$100m; extension only with at least 10,000 direct local employees | No | FIRB oversight and reporting | RA 12066; implementing rules |
| 20 | Highly desirable project (Section 301, presidential discretion) | Cross-cutting | Direct or indirect: bespoke package, income-tax incentives capped at 40 years | The FIRB must find benefits clear and convincing and far above cost; sustainable development plan; **minimum investment capital of PHP 50bn (about US$865m) or at least 10,000 direct local jobs within three years**; thresholds reviewed every three years | Not applicable: discretionary | FIRB and presidential oversight; cancellation if targets are missed | RA 12066 Section 301; implementing rules |
| 27 | 2026 Plan, IT-enabled services: software development including software as a service, and hyperscalers (Tier I) | (i) and (ii) | Indirect (through the tier) | None stated | No | As row 18 | Memorandum Order 47 of 21 May 2026 |
| 28 | 2026 Plan, artificial intelligence and data science: development of solutions and provision of services (Tier III) | (i) | Indirect (through the tier) | None stated | No | As row 18 | Memorandum Order 47 |
| 29 | 2026 Plan, data centres: those relying on the grid as upstream telecommunications infrastructure (Tier I); those with their own power supply, listed among science, technology and innovation support facilities (Tier III). The Plan defines a data centre as a purpose-built commercial facility, dedicated or multi-tenant, that provides infrastructure such as colocation | (iii) | Indirect (through the tier) | None stated; the tier depends on the power source, not on size | No | As row 18 | Memorandum Order 47 |

*Notes.* Verification covers the cited primary text only. The Vietnamese texts were read through a commercial legal database, not the official gazette. Rows 7 to 9 and 24 to 26 draw on Decree 260/2026 and rows 10 to 13 on Decision 21/2026. The Thai activity numbers follow the Guide 2026.

## Table S2. Primary sources coded

| Country | Source | Issuer | Date in force | Language / translation | Accessed | Amendments, repeals and implementing rules checked (date) |
|---|---|---|---|---|---|---|
| Thailand | BOI Investment Promotion Guide 2026; BOI Announcements 9/2565 (8 December 2022), 10/2565, Sor. 5/2568 (5 June 2025) and Sor. 9/2568 (14 November 2025); approval statistics January to December 2025 | Board of Investment | Sor. 9/2568 applies to applications from 14 November 2025 | English (BOI unofficial translation) | Read 9 October 2026 | Guide 2026 and Sor. 9/2568 are the current texts and Sor. 5/2568 and 9/2568 amend 9/2565; the Thai original and Royal Gazette text are to be checked (not yet read) |
| Vietnam | Decree 260/2026/ND-CP (30 June 2026; in force 1 July 2026; replaces Decree 10/2024); Decision 21/2026/QD-TTg (replaces Decision 1131/QD-TTg of 2025) | Government; Prime Minister | 1 July 2026 | Vietnamese original, read through the Thu Vien Phap Luat legal database, not the official gazette | Decree 260 and Decision 21/2026 read in full 9 October 2026 | Implementing circulars 38, 40, 42, 48 and 49/2026/TT-BKHCN and Decrees 20/2026 and 264/2025 identified; the circulars (including Circular 34/2025/TT-BKHCN on procurement preference) not yet read (not yet read) |
| Malaysia | Guidelines on Malaysia Digital (MD) Tax Incentive, New Investment Incentive (revised 22 July 2025); Guidelines and Procedures for DESAC (version on MIDA's site, December 2024); Guideline for Sustainable Development of Data Centre (December 2024) | MDEC; MIDA; MITI (hosted by MIDA) | DESAC applications received 1 January 2022 to 31 December 2027; MD guideline July 2025 | English (original) | Read 9 October 2026 | New Incentive Framework (manufacturing from 1 March 2026, services from Q2 2026) does not withdraw DESAC, which stays available until its window expires (MIDA NIF FAQ, question 20); checked 9 October 2026 |
| Philippines | Republic Act 12066 (CREATE MORE), signed 11 November 2024; implementing rules and regulations of Title XIII of the Tax Code (signed 17 February 2025, in force 20 February 2025, circularized by FIRB Advisory 001-2025); Memorandum Order 47 of 21 May 2026 approving the 2026 SIPP | Congress; Department of Finance and Department of Trade and Industry; Office of the President | Act 2024; rules February 2025; SIPP 2026 | English (original) | All three read in full 9 October 2026  | FIRB Advisory 009-2026 circularizing the 2026 SIPP identified; the SIPP qualification guidelines and the FIRB's published amendments not yet read (not yet read) |

*Note.* Currency figures are converted at about 35.7 baht, 4.55 ringgit and 57.7 pesos to the US dollar. The Vietnamese texts were read through a commercial legal database, not the official gazette.

## Table S3. Full evidence matrix

Rating rubric. A hypothesis is rated *expected* (E) when a stated prediction (P1a to P3c, Section 2.4 of the manuscript) predicts the evidence, *compatible* (C) when no prediction covers it and it is not in tension with any, *unexpected* (U) when it is in tension with a prediction or can be reconciled only with an additional assumption, and *contradicted* (X) when it is inconsistent with the hypothesis. The weight for the pair a row separates is *strong* if one hypothesis is E, the other U or X, the coding is verified and no auxiliary assumption is needed; *moderate* if it depends on assumption A1 or on coding not yet verified; and *weak* if no hypothesis is U or X.

| # | Evidence (country) | H1 cost | H2 design | H3 habit | Pair separated and weight | What would change the rating |
|---|---|---|---|---|---|---|
| E1 | Software threshold far below GPU-hosting capital condition (Thailand) | E (P1a) | C | C | None: Weak | Not diagnostic |
| E2 | Malaysia's low-capital digital track covers cloud (RM50,000 paid-up capital), beside a data-centre track whose smallest category is 0.85 MW | C | U (P2a, if the MD track admits capacity resale; to be confirmed) | C | H2 against H1 and H3: Moderate, provisional | MDEC's reading of MD activities |
| E3 | No instrument aimed at sub-facility compute (Thailand, Vietnam, Philippines; absence on coded instruments) | U if A1 holds, E if A1 fails | E if A1 holds (P2a) | E (P3b) | H1 against {H2, H3}: Moderate, conditional on A1 and on the search protocol | Viability benchmark; applicable general instrument; hypothetical-firm test |
| E4 | No capital condition at the compute layers despite their capital intensity (Vietnam, Philippines) | U (P1b) | C | C | H1 against {H2, H3}: Moderate; rests on Decision 21/2026, Decree 260 and the Act and Plan, with the Vietnamese circulars and the Philippine qualification guidelines unread | The circulars and the guidelines |
| E5 | Extension of the exemption tied to spending of at least 1% of sales, or THB 200m if lower, in the first three years (Thailand; cross-sectoral measure, verified) | U (P1c) | E (P2b) | E (P3a) | H1 against {H2, H3}: Moderate | How BOI applies the measure to firms without early sales |
| E6 | Auditor-verified annual self-declaration at the company's cost in the low-capital track (Malaysia; verified against the July 2025 guideline) | U (P1d) | E (P2b) | C | H1 against H2: Moderate; audit cost unmeasured | Audit cost relative to RM50,000 of capital |
| E7 | Common firm-scale boundary for all activities in the Act (Philippines); activity tiers that name AI and data centres | U (P1a, P1b) | C | E (P3a) for the boundary; U for the tiers, which name AI | H3 against H1: Weak to Moderate; Act, implementing rules and Plan read | Pre-AI instruments with the same boundary; Plan guidelines |
| E8 | Explicit startup track with direct support and recognition by the provincial authority (Vietnam; verified against Decree 260/2026, Article 11) | U (P1c) | U (P2c) | U (P3a; a 2026 design with no scale tiers) | All three unexpected: no pair separated | Take-up evidence |
| E9 | Official criticism of data-centre incentives on employment grounds (Malaysia) | C | C | C | None: Weak | Evidence on whether the criticism cited firm size |
| E10 | Thai-held share of capital falls with depth (46, 15, 0 per cent; Thailand) | C | C | C | None: Weak; descriptive; three points | Project-level data |
| E11 | Low-capital cloud routes screened by fixed compliance costs: Thai cloud services (certification, two certified data centres) and the Malaysian Digital track (annual audit) | U (P1d) | E (P2b) | C | H1 against H2: Moderate; verified against the guides, cost size unmeasured | Cost of certification and audit relative to a small provider's capital |
| E12 | Required research ratio falls as total capital rises (VND 100 billion and 6,000 billion tiers) in high-technology enterprise criteria (Vietnam; verified) | U (P1d) | E (P2b) | C | H1 against H2: Moderate; applies to enterprise recognition, not to compute provision | Whether the criteria apply to compute providers |

*Note.* E = expected; C = compatible; U = unexpected; X = contradicted. Ratings follow the predictions P1a to P3c of Section 2.4 and the rubric of Section 3.3 of the manuscript. Rows resting on unverified coding are provisional.

## Table S4. Illustrative eligibility ladder calibrated to cost benchmarks

| Rung | Capacity | Capital to host: construction only to fully equipped (US$ million) | Instrument type that may suit the rung | Reason |
|---|---|---|---|---|
| 0 | One eight-accelerator server (12 kW) | 0.13 to 0.46 | Direct: compute vouchers for users, matching grants for small providers | Tax relief presupposes taxable profit, which a new provider lacks |
| 1 | 100 kW (about eight servers) | 1.1 to 3.8 | Direct or refundable credit; simple eligibility test | Allows many small trials before any scale up (Hausmann and Rodrik, 2003) |
| 2 | 1 MW | 10.7 to 38 | Milestone-based tax incentive with compliance proportional to size | Avoids the fixed audit cost that weighs on the smallest firms (Section 4.3) |
| 3 | 10 MW | 107 to 380 | Existing facility-scale tax incentive | Comparable to Thailand's threshold (about 13 MW on construction cost) |
| 4 | 40 MW | 428 to 1,520 | Existing facility-scale incentive and negotiated packages | Already served by current designs |

*Note.* Construction cost of US$10.7m per MW (Turner and Townsend, 2025); fully equipped AI capacity of US$38m per MW (Epoch AI, 2026); 12 kW per server [citation to be added]. Figures are products of these benchmarks, not estimates of this paper.

## Currency conversion

Thai baht, Malaysian ringgit, Philippine peso and Vietnamese dong figures are converted to US dollars at about 35.7 baht, 4.55 ringgit and 57.7 pesos to the dollar. These rates are those implied by the values first coded. They are approximations used for comparison only. The source and date of each rate are to be recorded before submission, and the local-currency figure is the one to cite.

## Codebook

The coding rules applied are these.

Stack layer. *Applications and models* if the instrument governs software, models or AI systems as end products. *Cloud and compute services* if it governs the provision of computing capacity as a service, whether from owned or leased facilities. *Physical data-centre capacity* if it governs construction or operation of physical facilities. *(ii)+(iii)* if one instrument covers both and does not distinguish them. *Hardware manufacture* if it governs semiconductor or chip design or fabrication. *Cross-cutting* if it applies across activity types without targeting a layer.

Delivery mechanism. *Indirect* for tax-based instruments (exemptions, holidays, deductions) that presuppose taxable profit or investment expenditure. *Direct* for grants, equity investment or fee waivers that do not presuppose profitability. Combined schemes are coded as separate rows.

Formal threshold. Report the eligibility rule as stated in the source, in local currency with a dated conversion, and record its basis (annual spend, paid-up capital, minimum capital, cumulative capex, firm-scale investment capital). Record "none stated" when the source states no threshold; do not record zero.

New-firm accommodation. *Yes* only where the source contains an explicit provision easing eligibility for smaller or newer firms (for example a startup track or direct equity access). *No* where none exists, even if the general threshold is numerically low. A low threshold is recorded as a threshold. Proportional requirements (for example a percentage of staff) are coded "not scale-based".

Compliance burden. Any recurring (annual or ongoing) obligation attached to continued eligibility, distinct from one-off application requirements. Fixed-cost obligations are noted explicitly.

Ambiguous cases. When a coding decision stays uncertain after reading the source, flag the row, record both candidate codes, and log how it was resolved.

Four points matter for replication.

1. **A low threshold is not accommodation.** A low capital floor is recorded in the threshold column. Accommodation is coded Yes only for an explicit provision for small or new firms, such as Vietnam's startup track.
2. **Layers (ii) and (iii).** Where an instrument names data centres and cloud services together without distinguishing them, it is coded (ii)+(iii). Thailand's cloud-services activity (row 21) is coded (ii) because it carries no capacity or capital condition and is defined by certification and location.
3. **Designation is not access.** Rows 10 to 13 record that a technology is named. They state no condition and attach no benefit, and the two groups of Decision 21/2026 are not ranked.
4. **Cross-cutting rows.** Rows 3, 5, 6, 18, 19, 20, 25 and 26 apply beyond AI. They are kept so that the rules that govern an AI firm can be separated from rules written for AI.

## Reliability and outstanding checks

- **Inter-coder reliability.** Not yet done. A second coder will code all 29 instruments independently from the blind sheet, using the codebook, and the manuscript will report percentage agreement, Cohen's kappa per dimension and Krippendorff's alpha. Each resolved disagreement is to be logged.
- **Texts still to be read.** The Thai originals and gazette texts of the BOI announcements; the Vietnamese implementing circulars (including those on procurement preference for listed digital products); and the qualification guidelines of the 2026 Strategic Investment Priority Plan.
- **Open interpretation questions.** Whether BOI would classify a small GPU rental provider under Activity 8.2.2 or 8.2.4.1; whether MDEC accepts resale of compute capacity as a Malaysia Digital activity; what "cloud-computing platforms" means in Decision 21/2026; whether Article 16 of Decree 260 applies to a firm that has not yet earned revenue.
- **Instrument lists not yet coded.** General SME, startup and research schemes, and pre-AI sector schemes, are outside Table S1. Absence claims in the manuscript are limited to AI-related and digital-sector instruments.
