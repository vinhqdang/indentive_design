---
title: "Where the Screen Falls: Incentive Architecture and Domestic Firms' Entry into the AI Stack in Southeast Asia"
---

**[DRAFT FOR AUTHOR REVIEW. PENDING marks data or confirmation only the authors can supply. CITATION NEEDED and VERIFY mark a source check required before submission. Search the file for "PENDING", "CITATION NEEDED" and "VERIFY". All such notes must be removed before submission.]**

## Abstract

Southeast Asian governments have made artificial intelligence (AI) a pillar of industrial policy, but little is known about which firms their incentive instruments let in. We code about 20 instruments from the primary legal texts of Thailand, Vietnam, Malaysia and the Philippines on five dimensions, place explicit thresholds on a common cost scale, and ask where each system screens entrants to the AI technology stack and whether cost necessity, scale-favouring design or administrative habit better explains the pattern. The four systems use four architectures: capital-gated activities (Thailand), two parallel tracks (Malaysia), a priority list without capital rules (Vietnam) and uniform firm-scale tiers (the Philippines). On the stated thresholds all four make application-layer support accessible to small firms. Thailand's gate for GPU data hosting lies two and a half to three orders of magnitude above the capital needed to host one server. Malaysia pairs a low-capital digital track that covers cloud services with a data-centre track whose smallest recognised category is 0.85 MW. Vietnam and the Philippines state no capital rule at the compute layers, so their screens lie in designation and discretion. We found no instrument aimed at compute provision below facility scale, but Malaysia's low-capital cloud route shows that small providers are not excluded everywhere on paper. Cost benchmarks explain the height of Thailand's gate, not the pattern across the four. The evidence concerns legal eligibility, not realised access, and does not show that a middle-technology trap exists.

**Keywords:** AI industrial policy; investment incentives; middle-income trap; middle-technology trap; policy design; Southeast Asia

**JEL classification:** O25; O38; O53; H25; L52

## 1. Introduction

A middle-income country that wants to keep growing needs domestic firms able to build, not only to adopt, new technology. AI tests this requirement anew. It bears on the move from middle to high income because it is a general-purpose technology whose productivity gains depend on who builds and controls it. If domestic firms can build models, applications and compute capacity, AI can raise total factor productivity, the variable on which middle-income slowdowns turn (Eichengreen, Park and Shin, 2014; Imam and Temple, 2026). If they can only adopt what foreign providers supply, more of the gain is likely to accrue elsewhere. Cerutti et al. (2025) model such a limited-access scenario, and Lehdonvirta, Wú and Hawkins (2024) show how unevenly compute capacity is distributed.

Governments in the region have taken up the question. Vietnam and the Philippines entered the upper-middle-income group on 1 July 2026 (Ang, 2026) **[VERIFY: cite the World Bank classification itself]**, and Thailand, Vietnam, Malaysia and the Philippines have each written AI into or alongside their investment incentive systems. Each offers tax or other support to firms that meet stated eligibility rules, and those rules decide which firms can take part in which part of the AI industry. Thailand's capital threshold for GPU-based data hosting, about US$140 million, admits some firms and excludes others, whatever the size of the budget behind it. The literature reviewed in Section 2.3 studies aggregate spending, access scenarios and the geography of compute. We found no instrument-level study of eligibility across the AI stack in these economies **[PENDING: document the literature search, with databases, terms and dates]**.

This paper studies who can qualify. Its questions are:

* **RQ1.** Where in the AI technology stack does each country's incentive system screen entrants, along three dimensions: the layer an instrument covers, the scale it requires, and whether it accommodates new firms or presupposes an existing revenue base?
* **RQ2.** How far above the capital needed to host a single server is the smallest scale that each system makes eligible at the compute layers, and can a small compute provider use any instrument?
* **RQ3.** Is the pattern better explained by cost necessity (H1), scale-favouring design (H2) or administrative habit (H3)?

We code the primary legal texts of the four countries and, for Thailand, set the formal rules against published project approvals. Our results are as follows. On the stated thresholds, all four countries make application-layer support accessible to small firms, and Vietnam adds an explicit startup track with direct equity access. The four systems use different architectures: capital-gated activities (Thailand), two parallel tracks (Malaysia), a priority list without capital rules (Vietnam) and uniform firm-scale tiers (the Philippines). In Thailand the gate for GPU data hosting lies two and a half to three orders of magnitude above the capital needed to host one server. Malaysia pairs a low-capital digital track that covers cloud services (RM50,000 of paid-up capital) with a data-centre track whose smallest recognised category is 0.85 MW. Vietnam and the Philippines state no capital rule at the compute layers, so their screens lie elsewhere. No instrument we coded is aimed at compute provision below facility scale. Cost benchmarks explain the height of Thailand's gate, the most visible pattern and a weak test of design bias, but they do not explain why Vietnam and the Philippines need no capital gate or why Malaysia can admit small cloud providers.

The evidence concerns legal eligibility, not realised access or firm outcomes, and does not show that any of the four countries is in a middle-technology trap.

The paper makes four contributions. First, it provides a four-layer coding of AI incentive instruments that distinguishes layer, scale and firm vintage, which a software-versus-hardware split cannot do. Second, it classifies the four systems into four incentive architectures (gate, two-track, list, tier) and states what each implies for a small entrant. Third, it places explicit thresholds on a common cost scale and measures the distance between the smallest viable and the smallest eligible provider, which turns a qualitative impression of a gap into a quantity that other countries and technologies can reuse. Fourth, it sets out an evidence matrix that separates observations that discriminate between explanations from those that do not, so that readers can see which claims rest on which evidence.

Section 2 relates the middle-income and middle-technology traps, reviews the AI literature, and derives the hypotheses. Section 3 describes the design. Section 4 reports the findings. Section 5 assesses the explanations. Section 6 draws policy implications, Section 7 states the limitations, and Section 8 concludes.

## 2. Conceptual framework and hypotheses

### 2.1 Middle-income trap and middle-technology trap

The middle-income trap names a pattern in aggregate income. Gill and Kharas (2007) argued that middle-income economies must shift from diversification to specialisation, from investment-led to innovation-led growth, and from adapting technology to creating it. Eichengreen, Park and Shin (2012, 2014) located growth slowdowns near US$10,000 to 11,000 and US$15,000 to 16,000 per capita (2005 purchasing power) and attributed them mainly to falling total factor productivity. Imam and Temple (2026) find that capital intensity and human capital converge to the frontier over time but relative total factor productivity does not. Bianchi, Isabella, Martinis and Picasso (2024) classify trapped economies by the trajectory of export complexity, placing Thailand and Malaysia in the most favourable of three categories.

The middle-technology trap concerns the technological composition of an economy. It has two lineages. The first, developed by Ke (2024) with reference to Zheng (2024), covers Malaysia, Thailand, Indonesia and the Philippines (the "ASEAN Four") and attributes stagnation to FDI-led industrialisation in which multinationals keep core technology at home and transfer only mature technology. The second begins with the argument that the European Union over-invests in mature mid-technology sectors at the expense of frontier activity (Fuest, Gros, Mengel, Presidente and Tirole, 2024). Bahar, Gadgin Matha, Hausmann and Segovia (2026) apply it to Japan: research intensity is near the top of the OECD, yet labour-productivity growth has been flat since 2000, because more than half of private research spending goes to mature industries while high-technology sectors receive 35 to 40 per cent. They attribute this to incentives delivered mainly through indirect tax credits, which presuppose taxable profit and scale and so favour large incumbents.

We treat the middle-technology trap as a mechanism that can contribute to a middle-income trap, not as a synonym for it. The transmission runs through productivity: if domestic firms cannot move into the technology layers that carry rising returns, total factor productivity growth stalls, and stalled productivity growth is what the income-trap literature identifies as the proximate cause of slowdowns (Eichengreen, Park and Shin, 2014; Imam and Temple, 2026). The reverse does not hold. A country can be income-trapped for institutional reasons without being technologically trapped, and a technology trap can arise at other income levels. Japan was already a high-income economy in the period Bahar et al. (2026) study. It matters here because it shows that incentive design can channel support to mature activity and to firms able to use it without any foreign actor and without low income. If the mechanism persists in a high-income economy with high research intensity, it can also operate earlier, while a middle-income country is still choosing which activities its incentives reach. The question for the four countries is therefore whether their AI incentive design could impede the move from middle to high income by restricting domestic entry into the technology layers that carry rising returns. We follow the second lineage because its mechanism, incentive design, needs no foreign actor. We also record the political-economy account of Doner and Schneider (2016), who argue that the trap reflects coalition failure, with business fragmented along cleavages such as firm size and foreign versus domestic ownership. We do not test coalitions, but their argument tells us what ownership patterns could and could not mean (Section 5.2).

**What this paper measures.** The literature identifies a middle-technology trap by outcomes: persistently low research intensity and limited indigenous capability (Ke, 2024), or the allocation of research spending between mature and high-technology sectors together with flat productivity growth (Bahar et al., 2026). We observe none of these outcomes. We do not measure a trap or estimate the probability of one. We identify *features of incentive design that could contribute to a middle-technology trap*, upstream of those outcomes. The feature of interest is a large distance between the smallest scale at which a compute provider could operate and the smallest scale at which an instrument admits it, together with an absence of instruments aimed at the scales in between. We observe three indicators: (a) an asymmetry in eligibility across layers, (b) that distance, which we call the rung distance and define in Section 3.3, and (c) ownership concentration in approved projects where data exist. Whether this opportunity structure leads to a trap depends on firm behaviour and outcomes that we do not observe. **[VERIFY: check how Ke (2024), Zheng (2024) and Bahar et al. (2026) operationalise the trap against the full texts, and cite the specific indicators they use.]**

### 2.2 AI: short-cycle opportunity or compute concentration

Two readings of AI compete. Lee (2013, 2019) argues that latecomers advance fastest in domains where knowledge becomes obsolete quickly, since such domains reward agility over accumulated advantage; AI plausibly fits. The sceptical reading holds that AI favours economies that already hold digital infrastructure, data and skilled labour (Abdurohman and Huang, 2026). Cerutti et al. (2025) find in a general-equilibrium model that AI productivity gains concentrate in advanced economies' non-tradable sectors, and that under limited access output growth falls by about one percentage point in emerging markets excluding China and in low-income countries. Alonso, Berg, Kothari, Papageorgiou and Rehman (2020) find divergence from labour-substituting automation. For the offshoring route that the Philippines relies on, Schellekens and Skilling (2024) warn of erosion, Ide and Talamàs (2025, 2026) show that the outcome depends on how sophisticated AI becomes, and the OECD (2024) notes that soft-skill requirements limit cross-border substitution. On geography, Lehdonvirta, Wú and Hawkins (2024) divide the world into a "Compute North", a "Compute South" with inference capacity and a "Compute Desert". Lee, Wong, Intarakumnerd and Limapornvanich (2020) pose the same fork, window of opportunity or reinforced trap, for the Fourth Industrial Revolution in Southeast Asia, and Glawe and Wagner (2020) link human capital to the trap in the age of automation. **[VERIFY: check both papers' findings against the full text before characterising them beyond their titles.]**

### 2.3 What the literature leaves open

These literatures yield a prediction but no mechanism at the level of policy. The macro models (Cerutti et al., 2025; Alonso et al., 2020) assume an access scenario and do not examine the instruments that determine it. The compute-geography work (Lehdonvirta et al., 2024, 2025) measures where capacity sits, not which policies shape whether domestic firms can provide it. Bahar et al. (2026) examine incentive design, but for research and development tax credits in one advanced economy, and not for AI or for the layers of a technology stack. Evidence that fiscal incentives change firm behaviour, such as the finding that cutting the cost of research and development raises research spending across OECD countries (Bloom, Griffith and Van Reenen, 2002), makes the question of who is eligible consequential, and the design of tax incentives for business investment in developing countries is a long-standing public-finance concern (Zee, Stotsky and Ley, 2002). What is missing is an instrument-level account of eligibility across the AI stack in middle-income economies.

### 2.4 The four-layer stack and how it structures the analysis

Existing treatments distinguish software from hardware. We code four layers: (i) applications and models, including domain-specific systems and language models; (ii) cloud and compute services, meaning the provision of computing capacity as a service from owned or leased facilities; (iii) physical data-centre capacity, meaning construction and operation of facilities; and (iv) hardware manufacture, mainly semiconductor design and fabrication. Where one instrument covers both (ii) and (iii) and does not distinguish them, we code it "(ii)+(iii)", and we call these the compute layers. A country can treat the compute layers as generously as layer (i) while ranking hardware lower, or can restrict the compute layers while keeping layer (i) open. A binary split would classify these as the same.

Firms also relate to compute in two ways. Some use it (an AI developer renting capacity) and some supply it (a cloud provider or colocation operator). Support for users and support for suppliers are different instruments. Our coding concentrates on supply, because the entry question for domestic compute capacity is a supply question. **[PENDING: use-side instruments such as compute vouchers, and public or sovereign compute programmes, are not yet systematically coded. A gap in supply-side incentives may be partly filled by programmes outside the incentive system we code; list them for each country, for example national supercomputing facilities, cloud-credit schemes and public research compute.]**

### 2.5 Three dimensions of accessibility, three explanations, and one assumption

A high threshold is not the same as a barrier to new firms, since a capital-rich startup can meet a high capital requirement, and a low priority for an activity is not the same as blocked access. We therefore keep three dimensions apart.

* **Layer.** Which activities does the instrument cover or prioritise?
* **Scale.** What minimum capital, revenue or staffing does it require?
* **Vintage.** Does it accommodate new firms (a startup track, direct equity access) or does it presuppose an existing revenue base or profit?

We use "incumbent" only for the third dimension. A fixed compliance cost is neither a scale nor a vintage rule; we code it separately as a recurring burden, and treat it as a relative cost that falls more heavily on small firms.

Each hypothesis is a claim about the pattern in one country's AI-related incentive design. We rate evidence country by country and pool only where the same rating holds in each country.

* **H1, cost necessity.** The conditions follow the technical cost of each layer. P1a: where thresholds exist, their height rises with the capital intensity of the layer. P1b: the layers with the highest capital intensity carry the strictest capital conditions, and layers with low intensity do not. P1c: eligibility does not depend on firm age or revenue history beyond what the capital need implies. P1d: the system imposes no costs unrelated to the technology's capital need, such as fixed compliance costs at low capital tiers.
* **H2, scale-favouring design.** The architecture raises entry costs for smaller or newer firms beyond what the technology requires, whatever the intent. P2a: there is no instrument between the smallest viable provider and the smallest eligible provider (conditional on the assumption A1 below). P2b: conditions presuppose a revenue base or impose fixed costs on small or new firms in layers with low capital need. P2c: there is little explicit accommodation for new firms. This is the mechanism Bahar et al. (2026) identify for Japan, through a different channel.
* **H3, administrative habit.** Instruments reuse templates inherited from generic or pre-AI schemes. P3a: eligibility follows a template such as uniform scale tiers across activities or activity categories fixed before AI. P3b: gaps arise where an activity falls outside the inherited categories. P3c: rules show no AI-specific tailoring.

**A1, the viability assumption.** A commercially viable scale of AI compute provision exists far below facility scale. Power draw shows that a server can be hosted, not that a provider can survive on it, so A1 is an empirical assumption, not a fact. If A1 fails, the absence of instruments below facility scale is what H1 predicts, and P2a does not apply. Every rating of the evidence on absence below facility scale is therefore conditional on A1.

H2 and H3 can generate similar outcomes and differ mainly in origin. Legal texts separate H1 from the pair {H2, H3} better than they separate H2 from H3.

**The missing-rung proposition.** Hausmann and Rodrik (2003) argue that a country does not know in advance what it can produce at competitive cost, and that discovering the cost of a new activity is socially valuable because others can imitate the discovery, so that laissez-faire yields too little investment and entrepreneurship in new activities. We apply this to compute supply. If the cost of supplying compute from inside a middle-income economy is unknown, small-scale provision is how that cost is discovered. We state the application as a proposition that can be wrong. Let the rung distance be the base-10 logarithm of the ratio between the smallest scale an instrument makes eligible and the smallest viable scale of provision. **M: where learning in compute supply requires hands-on operation, and the rung distance is large (we take two or more orders of magnitude as large) with no instrument aimed at the scales between, domestic entry into compute supply is restricted to firms that can bear facility-scale risk.** M is false for a country if (i) the hypothetical-firm test of Section 3.4 shows a small provider eligible, (ii) the viability evidence shows A1 false, or (iii) domestic providers at sub-facility scale operate without incentives. This is our application of their argument, not a result they report.

## 3. Research design

### 3.1 Scope, case selection and nested structure

The paper studies *legal eligibility*, that is, who may qualify under the rules as written. It does not observe realised access, application costs, screening practice or firm outcomes.

**Case selection.** We selected countries that (i) are middle-income ASEAN economies, (ii) have AI-related investment incentives in force in the period studied, (iii) publish consolidated primary legal texts we can access, and (iv) differ in their income trajectories, using Bianchi et al. (2024) where they classify a country and income history where they do not.

*Which trap the classifications refer to.* The labels "trapped" and "not trapped" refer to the **middle-income trap**, not the middle-technology trap, and are taken from Bianchi et al. (2024), who classify economies by the time spent in the middle-income range (duration criteria) and by the trajectory of export complexity. On that basis Thailand and Malaysia are formally trapped by duration but show sustained improvement in complexity, the most favourable of the three categories. Vietnam is not classified as trapped by any source we reviewed, having reached upper-middle-income status only in July 2026, so we place it by income history. The Philippines crossed the same threshold on the same date but carries a documented trap history at a lower income band. **[VERIFY: confirm the duration criteria and each country's placement in Bianchi et al. (2024), and state the criteria numerically.]** The middle-technology trap has been applied separately: Ke (2024) examines it for Malaysia, Thailand, Indonesia and the Philippines, and does not cover Vietnam. We do not classify any of the four countries as middle-technology trapped, and we use neither classification as a result. We use them to choose cases that differ in position relative to the middle-income range, so the question for each differs: whether AI incentive design reinforces or corrects an established pattern (Thailand, Malaysia), whether a previously experienced pattern could recur at a higher threshold (the Philippines), and whether the architecture being built now, while institutions are comparatively malleable, will help Vietnam through the range in which slowdowns cluster.

*How far the findings generalise.* Four purposively chosen cases support analytic inferences about how these four systems are designed. They do not support statistical claims about Southeast Asia. The findings may apply to other middle-income economies that use threshold-based investment promotion, and are less likely to apply where the incentive architecture differs.

*Countries not included.* Singapore is a high-income economy and outside the middle-income focus. **[PENDING, AUTHORS TO COMPLETE: reason for excluding Indonesia, which belongs to the ASEAN Four in Ke (2024). Possible grounds, to be confirmed or replaced: no consolidated AI incentive instrument in force, language access, timing. A hostile reader will ask whether Indonesia was dropped because it did not fit. See Seawright and Gerring (2008) for the logic of purposive case selection.]**

**Nested design.** Thailand is the primary case because it is the only one of the four that publishes approval statistics by sub-activity and by ownership of registered capital, so formal rules can be compared with realised outcomes. Vietnam, Malaysia and the Philippines are shadow cases coded on the same dimensions from legal texts without equivalent outcome data. The design gives a test of whether rules and outcomes line up in at least one country. The cost is that claims about realised ownership rest on one country.

### 3.2 Data sources

We code primary legal and regulatory texts, not strategy documents or commentary: Thailand's Board of Investment announcements and Investment Promotion Guide; Vietnam's Decree 260/2026 implementing the Law on High Technology and Decision 21/2026 on strategic technologies; Malaysia's Malaysia Digital tax-incentive guidelines and the Digital Ecosystem Acceleration (DESAC) scheme guidelines; and the Philippines' CREATE MORE Act with its implementing rules. Table 1 lists each source with its issuing body, date, access route and the amendment check described below.

**Which instruments were selected, and how we established that they are authoritative and current.** An instrument entered the sample if it met two rules: it is in force in the period studied, and it either names AI, cloud, data centres or digital activity as an eligible or prioritised activity or sets eligibility rules for a scheme under which such activity is registered. For each country we built the list by reading the issuing agency's own consolidated list of schemes and the instruments those schemes cite, and we treated the instrument text, not agency summaries or press releases, as authoritative. For each source we then recorded (a) the version in force on the date of coding, (b) any amendment, consolidation or repeal found in the issuing body's own publication record, and (c) any implementing rule or circular that could change how the coded provision is read. Decision 21/2026/QD-TTg shows why this matters: it replaced an earlier 2025 list of strategic technologies (Decision 1131/QD-TTg), and the coding reflects the 2026 decision only. Malaysia's New Incentive Framework (Section 4.3) is replacing sector-list incentives in phases, so currency is a live question for Malaysia in particular. **[PENDING: complete the amendment and supersession check for every row of Table 1, state the date of each check, and name any provision found to have changed. Until then this paragraph describes the intended procedure, not a completed one.]**

**Table 1. Primary sources coded**

| Country | Source | Issuer | Date in force | Language / translation | Accessed | Amendments, repeals and implementing rules checked (date) |
|---|---|---|---|---|---|---|
| Thailand | BOI Announcements 8/2565, 9/2565, 10/2565; Guide to Investment Promotion 2025; approval statistics Jan to Dec 2025 | Board of Investment | **PENDING** | **PENDING** | **PENDING** | **PENDING** |
| Vietnam | Decree 260/2026/ND-CP; Decision 21/2026/QD-TTg (replaces Decision 1131/QD-TTg of 2025) | Government; Prime Minister | 1 July 2026 (VERIFY) | **PENDING** | **PENDING** | **PENDING** |
| Malaysia | Guidelines on Malaysia Digital (MD) Tax Incentive, New Investment Incentive (revised 22 July 2025); Guidelines and Procedures for DESAC (version on MIDA's site, December 2024); Guideline for Sustainable Development of Data Centre (December 2024) | MDEC; MIDA; MITI (hosted by MIDA) | DESAC applications received 1 January 2022 to 31 December 2027; MD guideline July 2025 | English (original) | Read 9 October 2026 for this draft (authors to confirm) | New Incentive Framework (manufacturing from 1 March 2026, services from Q2 2026) does not withdraw DESAC, which stays available until its window expires (MIDA NIF FAQ, question 20); checked 9 October 2026 |
| Philippines | Republic Act 12066 (CREATE MORE); FIRB Advisory 001-2025 | Congress; FIRB | **PENDING** | **PENDING** | **PENDING** | **PENDING** |

Statistical sources for Vietnam are the Ministry of Information and Communications white book (2024) and the General Statistics Office yearbook (2024). Currency figures are converted at the rates implied by the coded values, about 35.7 baht, 4.55 ringgit and 57.7 pesos per US dollar **[PENDING: state the date and source of each rate]**. Some texts were coded from official or unofficial English translations, implementing rules may follow the primary text, and Vietnam's AI-specific regulatory layer is still developing following the 2025 AI law (Vietnam, 2025).

### 3.3 Coding of instruments, the common scale and the rung distance

The unit of analysis is the instrument, a specific exemption, grant or eligibility rule, not the strategy document. Twenty instruments were coded across the four countries (Supporting Information, Table S1); five of them (SI rows 5, 6, 18, 19 and 20) are cross-cutting rules that apply beyond AI. Each is coded on five dimensions: **(1) stack layer**, using the four-layer scheme with the combined code (ii)+(iii); **(2) delivery mechanism**, distinguishing indirect tax-based instruments, which presuppose taxable profit or investment expenditure, from direct grants, equity or fee waivers; **(3) formal threshold**, the minimum capital, revenue or staffing in the source, recorded with its basis (annual spend, paid-up capital, minimum capital, cumulative capex); **(4) new-firm accommodation**, coded Yes only where the source contains an explicit provision easing access for smaller or newer firms; and **(5) recurring compliance burden**, meaning annual or ongoing obligations attached to continued eligibility. The codebook is in Appendix A. A low threshold is recorded as a threshold, not as accommodation. We report the coded dimensions as a matrix (Table 3) and do not aggregate them into an index, since any weighting would be a modelling assumption with no data-derived basis.

**Common scale and rung distance.** Thresholds are stated in different bases and currencies. To compare them we convert each capital figure to US dollars and then to the capacity that capital would host, using two published benchmarks: US$10.7 million per megawatt for construction cost (Turner and Townsend, 2025) and US$38 million per megawatt for fully equipped AI capacity (Epoch AI, 2026). We take the smallest viable unit of provision to be one eight-accelerator server of about 12 kW **[CITATION NEEDED: manufacturer specification]**, which on the two benchmarks needs US$0.13 million to US$0.46 million of capital to host. The *rung distance* of an instrument is the base-10 logarithm of its capital threshold divided by that capital, reported as a range. The benchmarks are order-of-magnitude figures: the construction index is a global average, the equipped-capacity figure is a gigawatt-scale total cost of ownership, and the thresholds have different bases (minimum capital, paid-up capital, cumulative capex), so the conversion tests plausibility, not equality. **[PENDING: replace the global construction figure with local cost where the index reports it, and state a band for exchange-rate movement.]**

**Reliability.** **[PENDING: inter-coder reliability. A second coder will code all 20 instruments independently, blind to the first coder's codes, using Appendix A. We will report percentage agreement and Cohen's kappa (Cohen, 1960) per dimension, with Krippendorff's alpha (Krippendorff, 2018) as a check given the small number of units, report agreement before and after discussion, and log every resolved disagreement. Layer assignment has already changed once (SI row 12) and the accommodation coding in the first matrix did not follow the codebook, so agreement may be low on those two dimensions. Replace this paragraph with the results.]**

**Verification.** **[PENDING: every figure in Table 3 and Supporting Information Table S1 is to be re-checked against the primary text, with the date of checking recorded. At the time of drafting, 14 of the 20 instrument rows were marked as not independently re-verified, including all Thai and Malaysian rows. Replace this paragraph with the result.]**

**Search protocol for absence claims.** Our claim that no instrument is aimed at compute provision below facility scale is a claim about absence. We distinguish three readings: (i) no instrument *is aimed at* sub-facility compute; (ii) no instrument *could be used by* a sub-facility provider on the same terms as a software firm; (iii) no instrument has a *tier* below facility scale. We assert reading (i) only, and test reading (ii) with the hypothetical-firm test below. **[PENDING: document the search for reading (i): which instrument lists were read in full, which terms were searched in the English and national-language texts (for example colocation, cloud service, compute, GPU, shared infrastructure), on what date, and the nearest instrument to sub-facility compute in each country.]**

**General-purpose instruments.** The coding so far covers AI-related and digital-sector incentives. Firms may reach support through general SME, startup or research schemes that do not mention AI, and AI instruments may copy templates from earlier sectors. **[PENDING: code the general SME, startup and research instruments of each country, and two or three pre-AI sector schemes, on the same dimensions. The first tests reading (ii); the second tests P3a and P3b. Until then, absence claims are limited to AI-related and digital-sector instruments.]**

### 3.4 Hypothetical-firm eligibility test

Eligibility on paper is easier to judge for a concrete firm than for a category. We define three hypothetical firms: **Firm A**, a three-person AI software startup; **Firm B**, a reseller of AI compute with 20 accelerated servers on leased colocation space; **Firm C**, a colocation operator running one megawatt of capacity. For each country and firm we read the instruments that could apply and record *eligible*, *ineligible* or *unclear*, with the clause. "Eligible" means the firm meets the stated conditions; it does not mean the firm obtains the benefit. Two readers code independently. Table 6 reports a provisional reading based on the descriptions in Section 4, to be replaced by the clause-level reading. **[PENDING]**

### 3.5 Assessing rival explanations

Because the analysis rests on four documented cases and not on a panel, conventional identification is unavailable. We use process-tracing logic (Collier, 2011; Mahoney, 2012; Van Evera, 1997): each piece of evidence is assessed by how each hypothesis predicts it, and by whether it can discriminate between them. We borrow from Fairfield and Charman (2017) the discipline of asking how probable the evidence would be under each rival, but we do not assign numerical priors or likelihoods. Four cases and ten evidence items cannot support defensible numerical priors, and conclusions would then depend on the priors. We use an ordinal rubric instead, so that every rating traces to a stated prediction.

**Table 2. Rubric for assessing evidence**

| Rating of a hypothesis | Meaning |
|---|---|
| Expected (E) | A stated prediction (P1a to P3c) predicts the evidence |
| Compatible (C) | No stated prediction covers it, and it is not in tension with any |
| Unexpected (U) | It is in tension with a stated prediction, or can be reconciled only with an additional assumption |
| Contradicted (X) | It is inconsistent with the hypothesis as stated |

| Inferential weight for the pair a row separates | Rule |
|---|---|
| Strong | One hypothesis is E and the other U or X, the coding is verified, and no auxiliary assumption is needed |
| Moderate | Same, but the weight depends on an auxiliary assumption (A1) or on coding not yet verified |
| Weak | No hypothesis is U or X, so the row separates nothing |

The most visible pattern in the data, the gap between software and infrastructure thresholds, is a *weak* test, because a cost-based account predicts it as well as a design-based one does. At the time of drafting no row is Strong, because every discriminating row rests on unverified coding or on A1. The ratings can change after the checks in Sections 3.3 and 3.4.

## 4. Findings

### 4.1 Thailand

Thailand's Board of Investment administers AI-relevant incentives through its Digital, Creative Industries and High-Value Service division, established under two 2022 announcements (Board of Investment of Thailand, 2022, 2025). Software and digital-content development (Activity 8.1.1) qualifies for an uncapped corporate income tax exemption at an annual threshold of approximately 1.5 million baht (about US$42,000), calculated from local staff salary expenditure, which a small technical team can reach. GPU-based data hosting (Activity 8.2.4), the activity most directly involved in training or serving models, requires minimum capital of approximately 5,000 million baht (about US$140 million) and an extensive certification regime. The two thresholds are not strictly comparable, since one is an annual expenditure flow and the other a capital stock, so we compare each with the benchmark of Section 3.3, not with each other. GPU-based hosting could be coded as layer (ii) or (iii), and we code it (ii)+(iii). The coding matrix coded it (iii) and described layer (ii) as "not separately provided for" **[PENDING: confirm the layer assignment]**.

Secondary legal summaries add details that bear on the compute layers **[CITATION NEEDED: the BOI notification; VERIFY every item]**. The THB 5,000 million minimum for Activity 8.2.4 excludes land and working capital, the project must provide an electrical system of at least two megawatts, and it must operate at least two ISO/IEC 27001-certified data centres in Thailand. Data centres under Activity 8.2.1 receive the higher tier only with a power usage effectiveness of 1.3 or lower and at least two megawatts of IT load, and cloud services (Activity 8.2.2) are reported to require two such data centres. If these summaries are right, Thailand's compute activities start at about two megawatts or at two certified facilities, and the earlier statement that cloud services are not separately provided for is wrong **[PENDING: correct SI row 4 and Table 3 after reading the notification]**.

The structure is more than a binary. Baseline research and development qualifies at the same accessible threshold as software. A separate competitiveness-enhancement mechanism lets qualifying firms extend the exemption to thirteen years if they make additional investment of at least 200 million baht (about US$5.6 million), representing a specified minimum share of sales over the following three years (Board of Investment of Thailand, 2022). That tier presupposes a revenue base, and it applies to software, where a cost rationale does not apply. **[VERIFY: the minimum share of sales; whether the mechanism is specific to the digital division or cross-sectoral, which bears on H3; and whether it is an optional add-on to the baseline exemption.]**

Realised approvals are consistent with the rules. Approval statistics for January to December 2025 show 96 approved projects under Activity 8.1.1 with combined investment of 933.0 million baht, an average of about 9.7 million baht. Over the same period 24 approved data-centre projects under Activity 8.2.1 carried 457,999.8 million baht, an average of about 19,083 million baht (about US$534 million), and a single data-hosting project under Activity 8.2.4 carried 126,793.0 million baht (Board of Investment of Thailand, 2026). The average data-centre project is about 1,960 times the average software project in approved investment. This compares approved projects, not firms, and the two averages belong to different activities. The coding records the US$140 million threshold only for Activity 8.2.4. If a similar threshold applies to 8.2.1 **[VERIFY]**, the average approved data-centre project sits about 3.8 times above it, so the threshold would not determine realised size.

Ownership of registered capital differs by layer. In Activity 8.1.1 software projects, 46 per cent of registered capital is Thai-held and 54 per cent foreign-held. In data-centre projects the split is 15 per cent Thai and 85 per cent foreign. In the single data-hosting project all registered capital is foreign. The Thai-held share therefore falls from 46 to 15 to 0 per cent with depth into the infrastructure stack. This gradient rests on three points, one of them a single project, and it describes who holds capital in approved projects. It does not show whether Thai firms were excluded, and a cost-based account also predicts it (Section 5.2). Lehdonvirta, Wú and Hawkins (2025) show that the global reach of cloud data centres is shaped by the economic and security interests of a few home states, which is one reason to expect foreign capital in this layer independently of Thai design.

The Trade and Investment Support Office category, which explicitly includes internationally delivered business-process outsourcing, receives the lowest incentive tier in the division, with no corporate income tax exemption. This activity is exposed to AI-driven automation (Section 2.2) and receives the least support.

### 4.2 Vietnam

Decree 260/2026, implementing the Law on High Technology, took effect on 1 July 2026 and sets two tracks (Vietnam, 2026a). The first, for recognised research centres, imposes demanding conditions: at least 60 per cent of staff in research and development (70 per cent for strategically designated technology), and research spending of 65 to 70 per cent of annual operating budget. These conditions restrict the track to purpose-built research institutions. **[VERIFY: percentage thresholds against the decree text.]**

The second track, for recognised startups, requires only demonstrated revenue growth or a commercialisation-ready technology. Qualifying startups receive the full incentive package, fee exemptions for state research facilities, and priority access to the National Venture Capital Fund, a direct equity instrument distinct from the National Technology Innovation Fund, which provides subsidised lending. This is the clearest instance in our data of explicit accommodation for new firms, and part of it is delivered by direct, not tax-based, means. **[VERIFY: Article 11 provisions and the fund distinction.]**

Decision 21/2026, which replaced a 2025 list, groups thirty strategic technology products into two priority tiers (Vietnam, 2026b). The top tier, of market-ready products with large direct economic impact, includes Vietnamese-language large language models, virtual assistants and specialised AI systems, and also cloud-computing platforms as a separate line item. The lower tier, of future and foundational technologies, includes specialised chips, quantum technologies and satellite systems. "Cloud-computing platforms" is a product category and may refer to platform software, not capacity provision, so it is weak evidence on compute provision **[VERIFY: the list entry's definition and the benefits attached to it]**. Edge-processing AI cameras and digital-twin platforms are also top-tier items, but they are application products, and we do not count them as evidence about compute **[PENDING: the first coding placed them in layer (ii); recode them as layer (i) in Table S1]**. Priority ranking is not blocked access (Section 2.5). Vietnam's coded instruments therefore contain no capital screen at any layer; specialised chips are ranked lower, and no instrument we coded excludes a firm from hardware manufacture. Hardware is coded for Vietnam only (SI row 13) and is uncoded for the other three countries, so we do not compare hardware across countries.

Vietnam's design differs from Thailand's in kind. Thailand and Malaysia define eligibility through activity-specific capital thresholds. Vietnam sets priority through a list of strategic technologies that carries no stated capital rule. A list-based design does not generate a capital gradient, which may be why none appears. The same design moves screening to designation and to instruments we have not coded, so this is a hypothesis about origin, not a finding about access.

The Vietnamese data centre announced for Ho Chi Minh City in 2026 and financed by the country's largest conglomerate **[CITATION NEEDED: source for the announcement]** is a market-structure observation, not a product of rules that exclude smaller firms from the compute layer, because the coded rules contain no such exclusion. Government data point the same way: hardware and electronics enterprises are under 10 per cent of Vietnam's information and communication technology enterprises but over 90 per cent of industry revenue, and are overwhelmingly foreign-invested, while software, digital content and services enterprises are predominantly domestic (Vietnam, Ministry of Information and Communications, 2024). That is evidence about manufacturing, not the compute stack. Of 9,348 operating enterprises in computer programming and related activities at the end of 2022, 57.9 per cent employed fewer than five people and 35.7 per cent employed between five and 49 (Vietnam, General Statistics Office, 2024), a base of micro and small firms that the startup track would be expected to serve. **[VERIFY: all three statistical figures against the cited sources.]**

### 4.3 Malaysia

Malaysia runs two parallel schemes with different logics. The Malaysia Digital (MD) New Investment Incentive, administered by MDEC, covers any new activity that uses one of ten promoted technology enablers, which include AI and big-data analytics and cloud (Malaysia Digital Economy Corporation, 2025). The applicant must hold MD Status, be a Malaysian-resident company with minimum paid-up capital of RM50,000 (about US$11,000), the lowest stated entry threshold among the countries that state one, and propose a new activity: it must not have issued a sales invoice for the activity before applying, with a narrow exception for firms with 60 per cent Malaysian equity. The incentive is a reduced tax rate or an investment tax allowance for ten years. Minimum conditions require an adequate number of full-time employees, among them knowledge workers earning at least RM5,000 a month, and adequate annual operating expenditure. The company must also submit an annual self-declaration within seven months of the year end, and the information in it must first be verified by an independent external auditor appointed by the company at its own cost. The cost is largely fixed, so it weighs more heavily on a small firm **[PENDING: the size of the audit cost relative to RM50,000]**. The effect is regressive in firm size, as is the profit-presupposing credit that Bahar et al. (2026) identify for Japan, but it works through a different channel, a fixed cost and not a profit requirement. Because "provision of services utilising cloud" is a Malaysia Digital activity, a small compute provider could in principle apply through this route **[VERIFY with MDEC whether provision of capacity as a service is accepted as an MD activity]**.

The Digital Ecosystem Acceleration (DESAC) scheme, administered by MIDA, serves a different group (Malaysian Investment Development Authority, 2024). Its qualifying activities are submarine cable including cable landing stations, and data centre and cloud computing or data hosting. The applicant must be a Malaysian-incorporated, resident digital infrastructure provider. The incentive is an investment tax allowance of 100 per cent (Tier 1) or 60 per cent (Tier 2) on qualifying capital investment excluding land, for five or ten years, or a special tax rate of 10 or 15 per cent. Tier 2 requires compliance with minimum conditions: paid-up capital of at least RM2.5 million (about US$550,000), capital expenditure as proposed, full-time Malaysian employees earning at least RM5,000 a month making up at least half of total manpower, at least two local vendor development programmes, adoption of Industry 4.0 elements, and at least one green technology. Tier 1 adds outcome conditions, among them high-value jobs of at least RM10,000 a month and at least three local vendor programmes. The ten-year option requires, in its second five years, cumulative capital expenditure of at least RM1 billion (about US$220 million), which exceeds Thailand's threshold in dollar terms. For existing companies expanding, Tier 1 adds capital expenditure of at least RM300 million over five years. An application must reach MIDA before the project begins, a National Committee on Investment approves it, and compliance with the minimum conditions is declared with verification by external auditors. For the special-rate option an annual compliance report is also due. Applications are open from 1 January 2022 to 31 December 2027.

DESAC is therefore not a ladder of capital tiers. Both tiers carry the same capitalisation floor, and the two tiers differ in outcome conditions. The scale of the project is left to the proposal, apart from the RM1 billion condition for the second five years. The sustainability guideline that governs data-centre applications received until 31 December 2027 sets design targets for power usage effectiveness (PUE) and water usage effectiveness (WUE) by category of data centre, and its smallest category is a low-voltage facility of 0.85 MW to under 4.25 MW (Malaysia, Ministry of Investment, Trade and Industry, 2024) **[VERIFY issuer and date of the guideline]**. On the benchmarks of Section 3.3, 0.85 MW is about US$9 million to US$32 million of capital to host, 1.3 to 2.4 orders of magnitude above one server. The paid-up capital floor of US$0.55 million measures how well capitalised the company is. It does not measure the scale of the project, so it is not a rung of project size. DESAC conditions are also written for facility operators: the local vendor programmes cover network infrastructure, cooling, electrical components and power systems, and the tax allowance applies to qualifying capital investment, which a firm that leases its space and equipment largely lacks.

Malaysia's New Incentive Framework, announced in Budget 2026, moves from sector-based qualification and profit-based tax holidays towards tiered, outcome-based assessment against national outcomes. It applied to manufacturing from 1 March 2026 and applies to services from a second-quarter 2026 date still to be announced, and its published FAQ states that existing packages other than those under the Promotion of Investments Act, DESAC among them, remain available until their application windows expire (Malaysian Investment Development Authority, 2026).

In the 2025 budget address, officials indicated that the earlier approach to data-centre incentives was no longer viewed as sustainable, on the grounds that large capital-intensive projects do not reliably translate into substantial high-skilled employment for Malaysian workers, and the government has since begun a formal restructuring **[VERIFY: speaker names, dates and wording, which are listed as unverified; the New Incentive Framework above is the documented change, and we have not confirmed that the remarks led to any change in DESAC]**. This shows that policymakers saw a problem with the existing design. It does not show that firm-size bias is the cause, since low employment per unit of capital is also what a capital-intensive activity produces.

The staffing rule is proportional (at least half of manpower, at RM5,000 a month or more). A proportional requirement is not a scale filter, since a ten-person firm can meet it as readily as a thousand-person firm, and we record it as an exploratory observation outside the central mechanism.

### 4.4 The Philippines

The Philippine architecture, established under the CREATE MORE Act, differs structurally from the other three (Philippines, 2024; Philippines, Fiscal Incentives Review Board, 2025). Standard registration carries no stated minimum investment; eligibility depends on inclusion in the Strategic Investment Priority Plan, on ownership qualifications and on a cost-benefit evaluation, not on firm size directly. Application-layer support is therefore accessible on its stated conditions, but it is subject to a discretionary inclusion and evaluation step.

Above this baseline sits a firm-scale tier at PHP 15 billion (about US$260 million), which defines a high-value domestic market enterprise and determines whether incentives are granted by the investment promotion agency or escalated to the Fiscal Incentives Review Board, with availment periods reaching 24 to 27 years. Beyond this the President may modify the mix, period and manner of availment, or craft a bespoke package, for a project designated highly desirable, with total incentives capped at forty years. This presidential mechanism is discretionary and, in the statutory text we examined, is not tied to a stated investment figure.

These firm-scale tiers apply uniformly regardless of activity type, and the Strategic Investment Priority Plan groups AI and data-centre infrastructure in the same priority tier **[VERIFY: edition and date of the Plan and its exact treatment of AI relative to data-centre infrastructure]**. The Philippines therefore encodes no capital screen specific to the compute layers. The PHP 15 billion tier is a top-up for extended benefits, not an entry rule. Cucio and Hennig (2025) find that roughly one third of Philippine occupations are highly exposed to AI, with around 60 per cent of that exposed employment complementary to AI and not substitutable by it, which suggests augmentation more than displacement for much of the exposed workforce.

### 4.5 Cross-country synthesis

Table 3 sets out the coded dimensions. The countries differ in where, and by what, they screen entrants.

**Table 3. Coded incentive dimensions by country and layer of the AI technology stack**

| Dimension | Thailand | Vietnam | Malaysia | Philippines |
|---|---|---|---|---|
| Layer (i), applications and models | Accessible: about US$42,000 per year in local salary spend | Accessible: named top-tier strategic priority; startup track | Accessible: about US$11,000 paid-up capital | Accessible on stated conditions: no minimum, subject to inclusion and evaluation |
| Compute layers (ii)+(iii) | Minimum capital about US$140 million, excluding land (Activity 8.2.4); about 2 MW electrical capacity and two certified data centres; Activities 8.2.1 and 8.2.2 also exist (**VERIFY**) | Cloud-computing platforms in top tier; no capital rule; scope **VERIFY** | MD track: cloud is a promoted enabler, RM50,000 paid-up capital (capacity resale **VERIFY**). DESAC: paid-up floor about US$550,000, smallest category 0.85 MW, ten-year condition about US$220 million capex | Same priority tier as AI applications; no minimum; PHP 15 billion firm-scale tier for extended benefits |
| Layer (iv), hardware | Uncoded (separate activity divisions) | Specialised chips in lower priority tier | Uncoded (separate schemes) | Uncoded (no distinct treatment) |
| Instrument aimed at compute provision below facility scale | None identified (**PENDING** search protocol) | None identified (**PENDING**) | None aimed at it; the MD track may admit small cloud providers (**VERIFY**) | None identified (**PENDING**) |
| Explicit accommodation for small or new firms | None explicit (low threshold at layer (i)) | Startup track (Decree 260, Art. 11) | None explicit (low entry capital; MD requires a new activity) | None explicit |
| Delivery mechanism at the accessible tier | Indirect (tax exemption) | Tax plus direct equity access | Indirect (tax exemption) | Indirect (tax exemption) |
| Recurring compliance burden | ISO/IEC 27001 certification at the infrastructure activities (**VERIFY**) | R&D staffing and spending ratios (research track) | Annual auditor-verified self-declaration at own cost (MD); auditor-verified declaration and annual report (DESAC) | FIRB escalation above PHP 15 billion |
| Where the screen falls | Capital and capacity gate at the data-hosting activity | No capital screen in coded instruments; designation | Two tracks: low capital floor (MD); facility categories from 0.85 MW, outcome conditions and committee approval (DESAC) | Inclusion, evaluation and firm-scale tier for extended benefits |
| Thai-held share of registered capital by layer | 46% (software), 15% (data centres), 0% (one data-hosting project) | Not published in comparable form | Not published in comparable form | Not published in comparable form |
| Middle-income trap classification (Bianchi et al., 2024; case selection only) | Trapped by duration, structural progress | Threshold-crossing, no trap history | Trapped by duration, same category as Thailand | Threshold-crossing, prior trap at lower band |
| Covered by the middle-technology trap account of Ke (2024) | Yes | No | Yes | Yes |

*Note.* Figures are approximate, converted at the rates in Section 3.2 **[PENDING: dates]**. Constructed from the primary documents in Table 1. Layers (ii) and (iii) are coded together because several instruments do not distinguish them. The coding matrix coded Thai, Malaysian and Philippine accommodation Yes or Implicit where the threshold was low. Appendix A codes only explicit provisions, and SI rows 1, 2, 14 and 18 are to be recoded. DESAC = Digital Ecosystem Acceleration scheme; FIRB = Fiscal Incentives Review Board.

**Layer.** Thailand screens at the infrastructure activity. Malaysia runs two tracks, a low-capital digital track and a data-centre track with facility categories and outcome conditions. Vietnam's coded instruments contain no capital screen and rank hardware lower. The Philippines applies the same inclusion and scale rules to all activities. All four make layer (i) accessible on the stated thresholds.

**Scale.** At layer (i), stated entry thresholds are low (about US$11,000 in Malaysia and US$42,000 in Thailand, on different bases) or absent (Vietnam, the Philippines). At the compute layers the stated figures are of three kinds: company capital (Malaysia's DESAC floor of about US$550,000 in paid-up capital), project scale (Malaysia's smallest data-centre category of 0.85 MW, and Thailand's minimum capital of about US$140 million and about 2 MW), and cumulative spending (Malaysia's ten-year condition of about US$220 million). The bases differ, so we read these as orders of magnitude, not as one scale.

**Vintage.** Only Vietnam has an explicit startup track. Thailand's most generous research tier presupposes a revenue base and the Philippines' escalation tier presupposes scale.

**Compliance.** Malaysia's audited self-declaration in the low-capital track, borne by the company, and Thailand's certification regime at its infrastructure activities are both recurring burdens. They are recorded separately because a fixed cost is neither a scale nor a vintage rule.

**Delivery.** Three of the four deliver the accessible tier entirely through indirect, tax-based instruments, which presuppose taxable profit. Only Vietnam adds a direct instrument.

**Is the pattern specific to AI?** The Philippines' uniform tiers and Thailand's competitiveness mechanism look like generic investment-promotion templates under which AI was placed, a reading consistent with H3. **[PENDING: confirm by comparing each AI-related instrument with the same country's pre-AI instruments, which needs the general-instrument coding in Section 3.3.]**

**Why does Vietnam differ?** The most direct explanation is the instrument type noted in Section 4.2: a priority list without capital rules against activity-specific thresholds. Vietnam's law is also the most recent of the four, written after cloud and AI became explicit policy priorities. We offer these as hypotheses that the present data cannot test.

**Four architectures.** The differences group into four ways of setting eligibility (Table 4).

**Table 4. Four incentive architectures and what they imply for a small entrant to compute supply**

| Architecture | Country | How eligibility is set | Where the screen sits | Implication for a small entrant to compute supply | Main design risk |
|---|---|---|---|---|---|
| Capital-gated activities | Thailand | Activity-specific minimum capital and capacity | A step at the data-hosting activity (about US$140m; about 2 MW) | No coded rung between the software threshold and the data-hosting threshold | A large gap between layers |
| Two parallel tracks | Malaysia | MD: RM50,000 paid-up capital and a new activity. DESAC: RM2.5m paid-up capital, outcome tiers, committee approval | MD: audit cost. DESAC: facility categories from 0.85 MW and facility-oriented conditions | A small cloud provider may use the MD track; the data-centre track starts at 0.85 MW | Fixed audit cost in the low-capital track; discretionary approval in the facility track |
| Priority list | Vietnam | Designation of products in two tiers; no capital rule | Designation, not capital | No capital barrier; access depends on designation and on instruments not yet coded | Discretion and opacity |
| Uniform scale tiers | Philippines | Inclusion and evaluation; firm-scale tier (PHP 15bn) for extended benefits; presidential discretion above | Inclusion step and firm scale, not layer | The same rules govern software and data centres; the system is AI-blind | Scale tiers set without reference to the technology |

*Note.* The thresholds are on different bases (see the note to Figure 1).

**The rung distance.** Table 5 applies the common scale of Section 3.3 to every coded capital threshold.

**Table 5. Capital thresholds on the common scale, and rung distance**

| Threshold | Basis | US$ million | Equivalent capacity: construction cost / fully equipped | Rung distance (orders of magnitude) |
|---|---|---|---|---|
| Thailand, data hosting (8.2.4), minimum capital | Minimum capital excluding land | 140 | 13.1 MW / 3.7 MW | 2.5 to 3.0 |
| Thailand, data hosting (8.2.4), electrical capacity (VERIFY) | Power capacity, 2 MW | 21.4 to 76 (capital to host) | 2 MW | 1.7 to 2.8 |
| Malaysia, DESAC capitalisation floor | Paid-up capital of the company, not project scale | 0.55 | not a project scale | not applicable |
| Malaysia, DESAC smallest data-centre category | Power capacity, 0.85 MW | 9.1 to 32.3 (capital to host) | 0.85 MW | 1.3 to 2.4 |
| Malaysia, DESAC ten-year condition | Cumulative capex | 220 | 20.6 MW / 5.8 MW | 2.7 to 3.2 |
| Philippines, firm-scale tier | Investment capital, extended benefits only | 260 | 24.3 MW / 6.8 MW | 2.8 to 3.3 |
| Vietnam | No capital rule | not defined | not defined | not defined |
| *Memo:* Thai average approved data-centre project | Approved investment | 534 | 49.9 MW / 14.1 MW | 3.1 to 3.6 |

*Note.* Rung distance is log10 of the threshold over US$0.13m to US$0.46m, the capital to host one eight-accelerator server of about 12 kW on the two benchmarks (CITATION NEEDED for the 12 kW figure). The Philippine figure is an extended-benefit tier, not an entry rule. Malaysia's paid-up capital measures how well capitalised the company is, so it has no rung distance. Malaysia Digital (RM50,000 paid-up capital) is a company-capital rule on a digital track and is not placed on the scale. Bases differ, so rows are indicative.

**Figure 1** places the same thresholds against the cost benchmarks.

![**Figure 1.** Explicit eligibility thresholds against cost benchmarks, US$ million, log scale. Shaded bands show the capital needed to host the stated capacity, from construction cost alone (US$10.7m per MW; Turner and Townsend, 2025) to fully equipped AI capacity (US$38m per MW; Epoch AI, 2026); the node band assumes 12 kW per eight-accelerator server (CITATION NEEDED). Thresholds are on different bases: Thailand's software figure is annual salary spend (hollow marker); Thailand's data-hosting figure is minimum capital; Malaysia's two paid-up capital figures are company capital, not project scale (*), the 0.85 MW bar shows the capital to host the smallest DESAC data-centre category (construction to fully equipped), and the right-hand marker is the cumulative capex condition for the second five years; the Philippine figure is a firm-scale tier for extended benefits. The bands are benchmarks, not like-for-like tests. Vietnam states no capital threshold.](fig1_threshold_ladder.png)

Three readings follow. In Thailand a single step of two and a half to three orders of magnitude separates one server from the smallest eligible scale in capital terms, and nothing coded lies between. In Malaysia the facility track starts at a category of 0.85 MW, 1.3 to 2.4 orders of magnitude above one server, while a separate digital track admits new cloud and AI activities at RM50,000 of paid-up capital. The low DESAC capitalisation floor says little about project scale. Vietnam and the Philippines state no capital threshold at the compute layers, so their screens must be sought in designation, inclusion and discretion.

**The hypothetical-firm test.** Table 6 gives a provisional reading of the test of Section 3.4 from the rules described above.

**Table 6. Hypothetical-firm eligibility test, provisional reading**

| Country | Firm A: three-person AI software startup | Firm B: reseller with 20 servers on leased colocation | Firm C: 1 MW colocation operator |
|---|---|---|---|
| Thailand | Eligible (Activity 8.1.1, about US$42,000 annual salary spend) | Likely ineligible on the coded rules (8.2.4 needs US$140m, about 2 MW and two certified data centres; cloud services under 8.2.2 are reported to need two certified data centres); general instruments **PENDING** | Unclear (1 MW is below the 2 MW of the higher tier of 8.2.1 and of 8.2.4; whether a lower tier of 8.2.1 admits it **VERIFY**); general instruments **PENDING** |
| Vietnam | Eligible (startup track; list item) | Unclear (cloud-computing platforms are listed with no capital rule; coverage of capacity resale **VERIFY**) | Unclear (data-centre capacity not named in coded list items) |
| Malaysia | Eligible (MD: RM50,000 paid-up capital; new activity; audited annual declaration at own cost) | Possibly eligible under the MD track, where cloud is a promoted enabler; unlikely under DESAC, which targets data-centre operators and allows relief on qualifying capital investment excluding land (**VERIFY** with MDEC) | Eligible to apply under DESAC on the stated conditions: a 1 MW facility falls in the 0.85 MW to 4.25 MW category; RM2.5m paid-up capital; Malaysian staff at RM5,000 a month making up half of manpower; committee approval is discretionary |
| Philippines | Eligible on stated conditions, subject to inclusion and evaluation | Unclear (Plan treatment of resale **VERIFY**) | Unclear (Plan groups data-centre infrastructure with AI; no stated minimum; **VERIFY**) |

*Note.* Provisional, derived from the descriptions in Sections 4.1 to 4.4. To be replaced by a clause-level reading by two independent readers. "Eligible" means the stated conditions are met, not that benefits are obtained.

On this reading Thailand's rules are the most likely to exclude Firm B, and Malaysia is the one country where a reading of the primary text supports a small provider's eligibility, through the MD track and not through DESAC. In Vietnam and the Philippines the answer depends on clauses not yet read.

**What the evidence supports on absence.** Reading (i) holds on the instruments we coded: no country has an instrument aimed at sub-facility compute provision. Reading (ii) is likely to hold for Thailand and fails provisionally for Malaysia, whose MD track may admit a small cloud provider. It is open for Vietnam and the Philippines. Reading (iii) holds for Malaysia's data-centre track, whose smallest recognised category is 0.85 MW.

## 5. Discussion

### 5.1 Cost necessity versus incentive design

The most serious challenge to a design reading is H1: thresholds at the infrastructure layer reflect the real cost of building data centres. Global average data-centre construction cost reached about US$10.7 million per megawatt in 2025, up from US$6 to 8 million before 2022 (Turner and Townsend, 2025), and estimates that include servers and networking for AI facilities imply far more, about US$38 billion for a one-gigawatt facility (Epoch AI, 2026). On the first figure Thailand's US$140 million threshold corresponds to about 13 megawatts of construction, and on the second to under four megawatts of fully equipped AI capacity. Either way it falls below the 40-megawatt scale commonly used to define hyperscale facilities **[CITATION NEEDED: source for the 40 MW definition]**. Cost explains the height of the Thai threshold (P1a), so the gap between software and infrastructure thresholds is not evidence of bias.

Cost does not by itself explain what lies below the threshold. In Thailand the rung distance is two and a half to three orders of magnitude (Table 5). Whether that distance is a cost constraint depends on A1: whether a commercially viable provider exists at that scale. A server of about twelve kilowatts can be hosted in colocation space **[CITATION NEEDED: manufacturer specification and provider terms]**, but hosting a server is not the same as running a viable provider. **[PENDING, the second most consequential open check: a viability benchmark from published sources, namely rental prices of regional GPU providers, colocation price lists, regional electricity tariffs and Epoch's cost data, to compute the break-even utilisation and minimum fleet size of a small provider relative to a hyperscaler's price.]** If the benchmark shows that viability requires scale, A1 fails and H1 explains the absence. If it shows that small providers can compete, the absence is a design outcome (H2 or H3) and proposition M applies to Thailand.

Malaysia is the informative comparison. It runs a low-capital digital track that covers cloud (RM50,000 of paid-up capital) beside a data-centre track whose smallest recognised category is 0.85 MW, 1.3 to 2.4 orders of magnitude above one server, and whose conditions are written for facility operators. If the MD track admits a small provider of compute as a service **[VERIFY with MDEC]**, Malaysia shows that a small provider can be admitted on paper at a cost, an annual audit at its own expense, and that the facility threshold in Thailand is not forced by the same cost structure. If it does not, Malaysia joins Thailand. DESAC's low paid-up capital floor does not change this, because it measures company capital, not project scale.

Vietnam and the Philippines show a different point. Capital intensity is highest at the compute layers, yet neither state a capital condition there. H1 predicts the strictest capital conditions where capital intensity is highest (P1b), so the absence of any capital condition is unexpected under H1. It shows that a capital gate is a design choice and not forced by cost. It does not show that small firms can enter, because their screen may lie in designation or inclusion.

### 5.2 Ownership: what the data can and cannot show

Foreign capital is a larger share of registered capital in Thailand's infrastructure layers than in its software layer. This is an observation about capital structure. It does not show that Thai firms were excluded, nor that Thailand failed to accumulate technological capability. A cost-based account predicts it, since the layers with the largest capital requirements attract the firms with the deepest capital, which for data centres are global operators (Lehdonvirta et al., 2025). Ke (2024) describes the trap in the ASEAN Four as one in which multinationals retain core capability at home, and the gradient is consistent with that account, but it cannot distinguish it from capital-intensity effects. Neither this account nor the coalition account of Doner and Schneider (2016) is among our three hypotheses, and the evidence matrix does not score them.

Vietnam's announced data-centre investment is domestic and led by its largest conglomerate. This does not show that domestic firms have captured the market or the incentive system. That conclusion would need further evidence of the kind Doner and Schneider (2016) discuss: restrictions on competitor entry, discriminatory distribution of support, or constraints on technology transfer and learning. The coded rules contain no capital screen at the compute layers (Section 4.2), so the rules do not show capture.

The two country patterns are different phenomena and imply different questions. In Thailand the question is whether technology-transfer or local-content conditions attached to foreign investment would change the learning that domestic firms gain. In Vietnam it is whether competition or access conditions for smaller firms matter in a market that one conglomerate leads. Whether Thailand's gradient holds elsewhere requires approval data that these governments do not publish in comparable form.

### 5.3 What the evidence supports

Table 7 rates each item of evidence against the predictions of Section 2.5 under the rubric of Table 2.

**Table 7. Evidence matrix**

| # | Evidence (country) | H1 cost | H2 design | H3 habit | Pair separated and weight | What would change the rating |
|---|---|---|---|---|---|---|
| E1 | Software threshold far below data-hosting threshold (Thailand) | E (P1a) | C | C (E if the activity thresholds pre-date AI; **PENDING**) | None: Weak | Not diagnostic |
| E2 | Malaysia's low-capital digital track covers cloud (RM50,000 paid-up capital), beside a data-centre track whose smallest category is 0.85 MW | C | U (P2a, if the MD track admits capacity resale; **VERIFY**) | C | H2 against H1 and H3: Moderate, provisional | MDEC's reading of MD activities |
| E3 | No instrument aimed at sub-facility compute (Thailand, Vietnam, Philippines; absence on coded instruments) | U if A1 holds, E if A1 fails | E if A1 holds (P2a) | E (P3b) | H1 against {H2, H3}: Moderate, conditional on A1 and on the search protocol | Viability benchmark; applicable general instrument; hypothetical-firm test |
| E4 | No capital condition at the compute layers despite their capital intensity (Vietnam, Philippines) | U (P1b) | C | C | H1 against {H2, H3}: Moderate; rests on the list and Plan readings | The Decision 21/2026 and Plan readings |
| E5 | Most generous tier requires further investment against a sales base (Thailand) | U (P1c) | E (P2b) | C (E if cross-sectoral; **VERIFY**) | H1 against H2: Moderate; unverified row | Verification; whether the mechanism is cross-sectoral |
| E6 | Auditor-verified annual self-declaration at the company's cost in the low-capital track (Malaysia; verified against the July 2025 guideline) | U (P1d) | E (P2b) | C | H1 against H2: Moderate; audit cost unmeasured | Audit cost relative to RM50,000 of capital |
| E7 | Uniform firm-scale tiers for all activities (Philippines) | U (P1a, P1b) | C | E (P3a) | H3 against H1: Moderate; unverified Plan reading | Pre-AI instruments with the same tiers |
| E8 | Explicit startup track with direct equity (Vietnam) | U (P1c) | U (P2c) | U (P3a; a 2026 design with no scale tiers) | All three unexpected: no pair separated | Take-up evidence |
| E9 | Official criticism of data-centre incentives on employment grounds (Malaysia) | C | C | C | None: Weak | Evidence on whether the criticism cited firm size |
| E10 | Thai-held share of capital falls with depth (46, 15, 0 per cent; Thailand) | C | C | C | None: Weak; descriptive; three points | Project-level data |

*Note.* E = expected; C = compatible; U = unexpected; X = contradicted. Ratings follow the predictions P1a to P3c of Section 2.5 and the rubric of Table 2. Rows resting on unverified coding are provisional.

Four results follow. First, cost explains the height of Thailand's threshold (E1), and the data cannot distinguish a design reading from it on that point. Second, thresholds are not forced by cost: Vietnam and the Philippines state none at the compute layers (E4, E7), and Malaysia admits cloud activity at RM50,000 of paid-up capital on a separate track (E2). Third, H1 is also unexpected for two design features that cost cannot generate, a revenue-base tier (E5, on an unverified row) and a fixed compliance cost (E6, verified against the guideline). Fourth, E8 is unexpected under all three hypotheses. A deliberate startup track fits none of them, which shows that these governments can and do design for new firms, and limits H2 as a general account. H2 and H3 remain difficult to separate: E3, E5 and E6 are expected or compatible under both, and only E7 favours H3 clearly.

We conclude that the pattern is not only cost-driven, and that capital gates are a design choice where they occur. We do not isolate whether design or habit produced them.

**Sensitivity.** Dropping evidence against H1 one row at a time (E3 to E7), the case against H1 survives on the others, so no single row decides it. Dropping the rows that rest on unverified coding (E5, E6, E7) leaves E3 and E4, both of which depend on the search protocol and on the list and Plan readings. Dropping the rows that depend on A1 (E2, E3) leaves E4, E5, E6 and E7. Evidence against H2 (E2, E8) is also tested: dropping E2 leaves E8, which is limited to Vietnam's application layer. If MDEC does not accept capacity resale as an MD activity, E2 reverses to compatible, and the claim that Malaysia is a counter-example to Thailand falls. No single row decides the conclusion that capital gates are a design choice, but the claim that rungs are missing in Thailand depends on A1 and on the general-instrument coding.

**Falsification.** The claim that Thailand has no rung for a sub-facility provider is falsified if a general-purpose or AI-specific instrument can be used by Firm B or Firm C on the same terms as a software firm (Table 6), or if viable small providers operate there without incentives. The claim that H1 is insufficient is falsified if the smallest commercially viable AI compute provider is above Thailand's threshold, which is what the viability benchmark tests.

**Competing interpretation.** A reading this paper cannot exclude is that no middle-income economy can compete with hyperscale providers at frontier scale, so that concentrating domestic effort on applications while accepting infrastructure dependence is sound specialisation. The evidence that would separate the readings is (a) whether domestic sub-facility providers exist, grow and serve domestic AI firms without incentives, (b) the price and availability of compute to domestic AI firms, and (c) outcomes for domestic firms in the application layer. We observe none of these, so we do not adjudicate between a design gap and rational specialisation.

### 5.4 Relation to the literature

Bahar et al. (2026) show for Japan that incentives delivered through indirect tax credits favour large profitable firms. We find that Thailand's deepest research tier presupposes a sales base (E5) and that three of four countries deliver the accessible tier through indirect instruments (Table 3). Malaysia's fixed audit cost has a regressive effect through a different channel (E6). The comparison with Japan and the European Union should be drawn carefully. Their problem is misallocation among sectors for established firms. Ours is entry to a new technology stack, and our evidence is rules, not spending shares. The lesson we take from Fuest et al. (2024) and Bahar et al. (2026) is about method: look at instrument design, not aggregate spending.

Doner and Schneider (2016) treat firm size as a cleavage that works through political weakness. We find that capital screens can be set by instrument type (gate, two-track, list, tier) whatever coalitions form around them, but we do not observe coalitions. For the access scenarios of Cerutti et al. (2025), whose macro outcome depends on whether domestic firms can supply compute, the rules we code show where entry is and is not open on paper. They do not show what firms do with it.

The architectures suggest three propositions for future work, each testable with more countries. **PA1:** capital gates screen on capital stock and so exclude firms by size, list-based designs shift screening to discretionary designation, and tiered designs screen only at the extended-benefit margin. **PA2:** the rung distance is larger where a single gate is set at facility scale than where a separate low-capital track covers the same activity. **PA3:** where an instrument type is inherited from generic schemes, the same tiers appear across activities. With four countries these are descriptions of the cases, and Indonesia, India or Latin American economies would be natural comparators.

## 6. Policy implications

Each implication follows from a specific finding and states its condition and risk. They should be read with the limits in Section 7.

**First, audit eligibility before building new rungs.** Finding: the exclusion of small compute providers is shown on the coded rules only for Thailand, and the other three countries depend on clauses not yet read (Table 6). An eligibility audit with hypothetical firms, as in Section 3.4, would show governments which of their own instruments a Firm B or Firm C could use, at low cost. Where the audit shows exclusion, the options are extending eligibility to colocation tenancy, modular deployment or shared-capacity arrangements, or providing subsidised access to public or consortium compute. Existing public compute programmes may already fill part of the gap **[PENDING: list them for each country]**. Vietnam's startup track is an application-layer example of a parallel pathway keyed to technical or commercialisation criteria, not to capital; whether the idea transfers to compute is untested. Risks: subsidising the resale of foreign-owned capacity, and fiscal leakage if eligibility is loose. We have not costed any option. A small, time-limited pilot with defined eligibility would show cost and take-up before scaling.

Table 8 gives an illustrative calibration of a ladder on the same benchmarks as Figure 1. It shows the order of magnitude of each rung and the instrument type each might suit. It is not a recommendation of specific thresholds, each of which would need costing and local validation.

**Table 8. Illustrative eligibility ladder calibrated to cost benchmarks**

| Rung | Capacity | Capital to host: construction only to fully equipped (US$ million) | Instrument type that may suit the rung | Reason |
|---|---|---|---|---|
| 0 | One eight-accelerator server (12 kW) | 0.13 to 0.46 | Direct: compute vouchers for users, matching grants for small providers | Tax relief presupposes taxable profit, which a new provider lacks |
| 1 | 100 kW (about eight servers) | 1.1 to 3.8 | Direct or refundable credit; simple eligibility test | Allows many small trials before any scale up (Hausmann and Rodrik, 2003) |
| 2 | 1 MW | 10.7 to 38 | Milestone-based tax incentive with compliance proportional to size | Avoids the fixed audit cost that weighs on the smallest firms (Section 4.3) |
| 3 | 10 MW | 107 to 380 | Existing facility-scale tax incentive | Comparable to Thailand's threshold (about 13 MW on construction cost) |
| 4 | 40 MW | 428 to 1,520 | Existing facility-scale incentive and negotiated packages | Already served by current designs |

*Note.* Construction cost of US$10.7m per MW (Turner and Townsend, 2025); fully equipped AI capacity of US$38m per MW (Epoch AI, 2026); 12 kW per server **[CITATION NEEDED]**. Figures are products of these benchmarks, not estimates of this paper.

**Second, review instruments whose design presupposes profit or imposes fixed costs in layers with low capital need.** Findings: Thailand's research tier (E5) and Malaysia's audited declaration (E6), both on unverified rows. Bahar et al. (2026) recommend moving from indirect tax-based support towards instruments that do not presuppose profitability or scale. For Malaysia, risk-based sampling or verification in proportion to firm size could lower the fixed cost, if the audit cost is shown to be material **[PENDING]**. Replacing indirect instruments needs a delivery agency able to run direct support, which is a capacity question as well as a fiscal one.

**Third, treat infrastructure dependence as an explicit choice.** If dependence on foreign providers at the infrastructure layer is an acceptable strategic trade-off, it should be stated as a choice, with attention to data sovereignty, and not left as a by-product of where thresholds fall. Because we cannot separate this from rational specialisation (Section 5.3), we recommend collecting the evidence that would decide it, namely domestic compute price and availability and the growth of small providers, before changing thresholds.

## 7. Limitations

We list the limitations in order of their effect on validity.

1. **Legal eligibility is not realised access.** We code rules as written. Firms may be unable to use an eligible instrument because of application costs or screening practice, and may receive support through general schemes the coding does not yet cover. The findings describe an opportunity structure, not who benefits. Linking rules to firm-level take-up, using venture-capital deal flow, patent data by applicant type and approval data by firm size, is the next step.
2. **Reliability, verification and currency are pending.** The coding has not been checked by a second coder, 14 of 20 rows have not been re-verified against the primary text, and the amendment check is incomplete. **[PENDING: replace with results.]** Every finding that depends on a threshold or classification is provisional until then.
3. **The central claim depends on an assumption and on absence.** The claim that rungs are missing depends on A1, which is untested here, and on a search for absence that is not yet documented. The sensitivity analysis shows that the conclusion on Thailand rests on them (Section 5.3).
4. **Layers are not cleanly separable.** Layers (ii) and (iii) cannot be distinguished in several instruments, hardware is coded for Vietnam only, and the thresholds are stated on different bases, so cross-country comparisons of scale are order-of-magnitude comparisons.
5. **Coverage.** We code investment incentives only. Public compute programmes, vouchers and sovereign compute initiatives are not coded and may fill part of the gap **[PENDING]**.
6. **Uneven evidence.** Only Thailand publishes approval data by sub-activity and ownership. The ownership gradient rests on three points, one of them a single project, and does not generalise.
7. **Four cases.** The countries are purposively selected (Section 3.1) and the findings do not support statistical claims about Southeast Asia. The reason for excluding Indonesia must be stated **[PENDING]**.
8. **No causal identification.** We assess explanations by process-tracing logic with ordinal ratings, and cannot separate H2 from H3 with legal texts alone.
9. **A moving target.** Vietnam's AI-specific regulatory layer is still developing following the 2025 AI law (Vietnam, 2025), and Malaysia is phasing in a New Incentive Framework that is moving incentives from sector lists to outcome-based tiers, with the services sector date still to be announced.

## 8. Conclusion

This paper asked where four Southeast Asian incentive systems screen entrants to the AI industry. All four make application development accessible on the stated thresholds, and Vietnam adds a startup track with direct equity access. Above that layer they use four architectures. Thailand gates data hosting by capital and capacity, two and a half to three orders of magnitude above the capital needed to host one server, with nothing coded in between. Malaysia runs a low-capital digital track that covers cloud beside a data-centre track whose smallest recognised category is 0.85 MW. Vietnam ranks technologies by priority and states no capital rule. The Philippines applies the same inclusion and firm-scale rules to every activity. No instrument we coded is aimed at compute provision below facility scale. Cost explains the height of Thailand's gate, but it does not explain why Vietnam and the Philippines need no capital gate, why Malaysia can run a low-capital cloud track, or why Thailand's research tier presupposes a sales base.

The claims are limited by the evidence. We observe eligibility rules, not realised access or outcomes. The Thai result depends on an assumption about the viability of small providers and on a documented search for absence, and for the other three countries it depends on clauses not yet read. The coding awaits an independent check. The data do not distinguish a design gap from rational specialisation and do not show a middle-technology trap. They identify a feature of design that could contribute to one: where a gate sits far above the smallest viable provider and nothing aims at the scales between, domestic entry into compute supply is restricted to firms that can bear facility-scale risk.

The contribution is a primary-source map of four incentive systems, a typology of incentive architectures, a rung-distance measure that other countries and technologies can reuse, and an evidence matrix that shows which observations discriminate between explanations. The next steps are the hypothetical-firm audit, the viability benchmark, and firm-level evidence on whether small compute providers exist and whether these rules shape their entry.

## Appendix A. Coding rules

Stack layer. *Applications and models* if the instrument governs software, models or AI systems as end products. *Cloud and compute services* if it governs the provision of computing capacity as a service, whether from owned or leased facilities. *Physical data-centre capacity* if it governs construction or operation of physical facilities. *(ii)+(iii)* if one instrument covers both and does not distinguish them. *Hardware manufacture* if it governs semiconductor or chip design or fabrication. *Cross-cutting* if it applies across activity types without targeting a layer.

Delivery mechanism. *Indirect* for tax-based instruments (exemptions, holidays, deductions) that presuppose taxable profit or investment expenditure. *Direct* for grants, equity investment or fee waivers that do not presuppose profitability. Combined schemes are coded as separate rows.

Formal threshold. Report the eligibility rule as stated in the source, in local currency with a dated conversion, and record its basis (annual spend, paid-up capital, minimum capital, cumulative capex, firm-scale investment capital). Record "none stated" when the source states no threshold; do not record zero.

New-firm accommodation. *Yes* only where the source contains an explicit provision easing eligibility for smaller or newer firms (for example a startup track or direct equity access). *No* where none exists, even if the general threshold is numerically low. A low threshold is recorded as a threshold. Proportional requirements (for example a percentage of staff) are coded "not scale-based".

Compliance burden. Any recurring (annual or ongoing) obligation attached to continued eligibility, distinct from one-off application requirements. Fixed-cost obligations are noted explicitly.

Ambiguous cases. When a coding decision stays uncertain after reading the source, flag the row, record both candidate codes, and log how it was resolved.


## References

Abdurohman, & Huang, X. (2026, January 28). *Can ASEAN+3 economies still escape the middle-income trap in the AI era?* ASEAN+3 Macroeconomic Research Office. https://amro-asia.org

Alonso, C., Berg, A., Kothari, S., Papageorgiou, C., & Rehman, S. (2020). *Will the AI revolution cause a great divergence?* (IMF Working Paper No. 20/184). International Monetary Fund. https://doi.org/10.5089/9781513556505.001

Ang, A. (2026, July 3). The World Bank has elevated Vietnam and the Philippines to upper-middle-income status, but now they face "a far more demanding phase of development." *Fortune*. https://fortune.com

Bahar, D., Gadgin Matha, S., Hausmann, R., & Segovia, S. (2026). *Japan's innovation challenge: Escaping the middle-technology trap* (Growth Lab Working Paper No. 269). Harvard University.

Bianchi, C., Isabella, F., Martinis, A., & Picasso, S. (2024). Varieties of middle-income trap: Heterogeneous trajectories and common determinants. *Structural Change and Economic Dynamics, 71*, 320-336. https://doi.org/10.1016/j.strueco.2024.08.008

Bloom, N., Griffith, R., & Van Reenen, J. (2002). Do R&D tax credits work? Evidence from a panel of countries 1979-1997. *Journal of Public Economics, 85*(1), 1-31. https://doi.org/10.1016/S0047-2727(01)00086-X

Board of Investment of Thailand. (2022). *Announcements No. 8/2565, 9/2565 and 10/2565 on investment promotion measures*. Office of the Board of Investment.

Board of Investment of Thailand. (2025). *A guide to investment promotion 2025*. Office of the Board of Investment.

Board of Investment of Thailand. (2026). *Investment promotion statistics: Approvals by sub-activity, January to December 2025*. Investment Services Center.

Cerutti, E., Garcia Pascual, A. I., Kido, Y., Li, L., Melina, G., Mendes Tavares, M., & Wingender, P. (2025). *The global impact of AI: Mind the gap* (IMF Working Paper No. 25/76). International Monetary Fund. https://doi.org/10.5089/9798229008570.001

Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement, 20*(1), 37-46.

Collier, D. (2011). Understanding process tracing. *PS: Political Science & Politics, 44*(4), 823-830.

Cucio, M., & Hennig, T. (2025). *Artificial intelligence and the Philippine labor market: Mapping occupational exposure and complementarity* (IMF Working Paper No. 25/43). International Monetary Fund. https://doi.org/10.5089/9798229001977.001

Doner, R. F., & Schneider, B. R. (2016). The middle-income trap: More politics than economics. *World Politics, 68*(4), 608-644. https://doi.org/10.1017/S0043887116000095

Eichengreen, B., Park, D., & Shin, K. (2012). When fast-growing economies slow down: International evidence and implications for China. *Asian Economic Papers, 11*(1), 42-87. https://doi.org/10.1162/ASEP_a_00118

Eichengreen, B., Park, D., & Shin, K. (2014). Growth slowdowns redux: New evidence on the middle-income trap. *Japan and the World Economy, 32*, 65-84. https://doi.org/10.1016/j.japwor.2014.07.003

Epoch AI. (2026). *Total cost of ownership of a one-gigawatt AI data center*. https://epoch.ai/data-insights/ai-datacenter-cost-breakdown

Fairfield, T., & Charman, A. E. (2017). Explicit Bayesian analysis for process tracing: Guidelines, opportunities, and caveats. *Political Analysis, 25*(3), 363-380. https://doi.org/10.1017/pan.2017.14

Fuest, C., Gros, D., Mengel, P.-L., Presidente, G., & Tirole, J. (2024). *EU innovation policy: How to escape the middle technology trap*. EconPol Europe and ifo Institute.

Gill, I., & Kharas, H. (2007). *An East Asian renaissance: Ideas for economic growth*. World Bank.

Glawe, L., & Wagner, H. (2020). The middle-income trap 2.0: The increasing role of human capital in the age of automation and implications for developing Asia. *Asian Economic Papers, 19*(3), 40-58. https://doi.org/10.1162/asep_a_00783

Hausmann, R., & Rodrik, D. (2003). Economic development as self-discovery. *Journal of Development Economics, 72*(2), 603-633.

Ide, E., & Talamàs, E. (2025). Artificial intelligence in the knowledge economy. *Journal of Political Economy, 133*, 3762-3800. https://doi.org/10.1086/737233

Ide, E., & Talamàs, E. (2026). The impact of AI on global knowledge work. *Journal of Monetary Economics, 157*, 103876. https://doi.org/10.1016/j.jmoneco.2025.103876

Imam, P. A., & Temple, J. R. W. (2026). At the threshold: The increasing relevance of the middle-income trap. *Scandinavian Journal of Economics*. Advance online publication. https://doi.org/10.1111/sjoe.70036

Ke, Y. (2024). ASEAN Four's middle income trap dilemma: Evidence of the middle technology trap. *Asian Review of Political Economy, 3*(1), 1-29. https://doi.org/10.1007/s44216-024-00033-5

Krippendorff, K. (2018). *Content analysis: An introduction to its methodology* (4th ed.). SAGE.

Lee, K. (2013). *Schumpeterian analysis of economic catch-up: Knowledge, path-creation, and the middle-income trap*. Cambridge University Press. https://doi.org/10.1017/CBO9781107337244

Lee, K. (2019). *The art of economic catch-up: Barriers, detours and leapfrogging in innovation systems*. Cambridge University Press. https://doi.org/10.1017/9781108588232

Lee, K., Wong, C.-Y., Intarakumnerd, P., & Limapornvanich, C. (2020). Is the Fourth Industrial Revolution a window of opportunity for upgrading or reinforcing the middle-income trap? Asian model of development in Southeast Asia. *Journal of Economic Policy Reform, 23*(4), 408-425. https://doi.org/10.1080/17487870.2019.1565411

Lehdonvirta, V., Wú, B., & Hawkins, Z. (2024). Compute North vs. Compute South: The uneven possibilities of compute-based AI governance around the globe. *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, 7*(1), 828-838. https://doi.org/10.1609/aies.v7i1.31683

Lehdonvirta, V., Wú, B., & Hawkins, Z. (2025). Weaponised interdependence in a bipolar world: How economic forces and security interests shape the global reach of US and Chinese cloud data centres. *Review of International Political Economy, 32*(5), 1442-1467. https://doi.org/10.1080/09692290.2025.2489077

Mahoney, J. (2012). The logic of process tracing tests in the social sciences. *Sociological Methods & Research, 41*(4), 570-597. https://doi.org/10.1177/0049124112437709

Malaysia Digital Economy Corporation. (2025). *Guidelines on Malaysia Digital (MD) tax incentive (new investment incentive)* (revised 22 July 2025; MOF Approval Ref. MOF.TAX(S) 700-2/7/970 JLD.3 (14)). MDEC. https://www.mdec.my/announcement/md-tax-incentive-revised-guidelines

Malaysia, Ministry of Investment, Trade and Industry. (2024). *Guideline for sustainable development of data centre*. Hosted by the Malaysian Investment Development Authority. https://www.mida.gov.my/wp-content/uploads/2024/12/Guideline-for-Sustainable-Development-of-Data-Centre.pdf

Malaysian Investment Development Authority. (2024). *Guidelines and procedures for the application of the Digital Ecosystem Acceleration (DESAC) scheme* (MOF Approval Ref. MOF.TAX(S)700-2/1/208 JLD.2 (7); version on MIDA's website, December 2024). MIDA. https://www.mida.gov.my/wp-content/uploads/2024/12/DESAC-Guideline_MIDA.pdf

Malaysian Investment Development Authority. (2026). *New Incentive Framework (NIF): Media release and frequently asked questions*. MIDA. https://www.mida.gov.my/media-release/new-incentive-framework-nif/

OECD. (2024). *Offshoring, reshoring and the evolving geography of jobs* (OECD Social, Employment and Migration Working Paper). OECD Publishing.

Philippines. (2024). *Republic Act No. 12066: Corporate Recovery and Tax Incentives for Enterprises to Maximize Opportunities for Reinvigorating the Economy (CREATE MORE) Act*. Congress of the Philippines.

Philippines, Fiscal Incentives Review Board. (2025). *Implementing rules and regulations of Title XIII of the National Internal Revenue Code of 1997, as amended by Republic Act No. 12066* (FIRB Advisory No. 001-2025). FIRB.

Schellekens, P., & Skilling, D. (2024). *Three reasons why AI may widen global inequality*. Center for Global Development.

Seawright, J., & Gerring, J. (2008). Case selection techniques in case study research: A menu of qualitative and quantitative options. *Political Research Quarterly, 61*(2), 294-308. https://doi.org/10.1177/1065912907313077

Turner & Townsend. (2025). *Data centre construction cost index 2025-2026*. Turner & Townsend.

Van Evera, S. (1997). *Guide to methods for students of political science*. Cornell University Press.

Vietnam. (2025). *Law on Artificial Intelligence, No. 134/2025/QH15*. National Assembly of Vietnam.

Vietnam. (2026a). *Decree No. 260/2026/ND-CP detailing the implementation of the Law on High Technology*. Government of Vietnam.

Vietnam. (2026b). *Decision No. 21/2026/QD-TTg promulgating the list of strategic technologies and strategic technology products*. Prime Minister of Vietnam.

Vietnam, General Statistics Office. (2024). *Statistical yearbook of Vietnam 2024*. Statistical Publishing House.

Vietnam, Ministry of Information and Communications. (2024). *Vietnam information and communication technology industry white book 2024*. Information and Communications Publishing House.

Zee, H. H., Stotsky, J. G., & Ley, E. (2002). Tax incentives for business investment: A primer for policy makers in developing countries. *World Development, 30*(9), 1497-1516.

Zheng, Y. (2024). The middle technology trap: China in a comparative perspective. *Asian Review of Political Economy, 3*(1), 11. https://doi.org/10.1007/s44216-024-00030-8
