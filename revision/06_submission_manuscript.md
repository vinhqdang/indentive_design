---
title: "Where the Screen Falls: Incentive Architecture and Domestic Firms' Entry into the AI Stack in Southeast Asia"
---

## Abstract

Southeast Asian governments have made artificial intelligence (AI) a pillar of industrial policy, but little is known about which domestic firms their incentive rules admit to the AI stack. We code 29 instruments from the legal texts of Thailand, Vietnam, Malaysia and the Philippines, place their capital thresholds on a common cost scale, and test three explanations: cost necessity, scale-favouring design and administrative habit. The four systems use different architectures: capital-gated activities, two parallel tracks, a strategic-technology list and activity tiers with a common firm-scale boundary. All make application-layer support accessible to small firms. At the compute layers, Thailand's gates lie two to three orders of magnitude above the capital to host one server but about one order or less above the fleet a provider-economics benchmark finds viable, and Malaysia's data-centre track starts at 0.85 MW. Where small cloud providers can enter on paper, the screen is a fixed compliance cost. Vietnam and the Philippines state no capital rule. No instrument is aimed at provision below facility scale. Cost largely explains Thailand's gate but not the pattern across countries. The evidence concerns eligibility, not realised access, and does not show a middle-technology trap.

**Keywords:** AI industrial policy; investment incentives; incentive design; middle-income trap; middle-technology trap; Southeast Asia

## 1. Introduction

A middle-income country that wants to keep growing needs domestic firms able to build, not only to adopt, new technology. AI tests this requirement anew. It is a general-purpose technology whose productivity gains depend on who builds and controls it. If domestic firms can build models, applications and compute capacity, AI can raise total factor productivity, the variable on which middle-income slowdowns turn (Eichengreen, Park and Shin, 2014; Imam and Temple, 2026). If they can only adopt, more of the gain is likely to accrue elsewhere. Cerutti et al. (2025) model such a limited-access scenario, and Lehdonvirta, Wú and Hawkins (2024) show how unevenly compute capacity is distributed.

Governments in the region have taken up the question. Vietnam and the Philippines entered the upper-middle-income group on 1 July 2026 (Ang, 2026), and all four countries have written AI into or alongside their investment incentive systems. Their eligibility rules decide which firms can take part in which part of the AI industry: Thailand's capital threshold for GPU-based data hosting, about US$140 million, admits some firms and excludes others. The literature we review studies aggregate spending, access scenarios and the geography of compute. We found no instrument-level study of eligibility across the AI stack in these economies.

This paper studies who can qualify. Its questions are:

* **RQ1.** Where in the AI stack does each country's incentive system screen entrants, along three dimensions: the layer an instrument covers, the scale it requires, and whether it accommodates new firms or presupposes an existing revenue base?
* **RQ2.** How far above the capital needed to host a single server is the smallest scale that each system makes eligible at the compute layers, and can a small compute provider use any instrument?
* **RQ3.** Is the pattern better explained by cost necessity, scale-favouring design or administrative habit?

The paper makes four contributions. It provides a four-layer coding of AI incentive instruments that separates layer, scale and firm vintage. It classifies the four systems into incentive architectures and states what each implies for a small entrant. It places thresholds on a common cost scale and measures the distance between the smallest viable and the smallest eligible provider, a quantity other countries and technologies can reuse. And it sets out an evidence matrix that separates observations that discriminate between explanations from those that do not.

## 2. Framework and hypotheses

### 2.1 Middle-income trap and middle-technology trap

The middle-income trap names a pattern in aggregate income. Eichengreen, Park and Shin (2014) attribute growth slowdowns in middle-income economies mainly to falling total factor productivity. Imam and Temple (2026) find that relative productivity, unlike capital intensity and human capital, does not converge to the frontier. Bianchi, Isabella, Martinis and Picasso (2024) classify trapped economies by the trajectory of export complexity.

The middle-technology trap concerns the technological composition of an economy and has two lineages. Ke (2024), with Zheng (2024), covers Malaysia, Thailand, Indonesia and the Philippines and attributes stagnation to FDI-led industrialisation in which multinationals keep core technology at home. Fuest et al. (2024) argue that the European Union over-invests in mature mid-technology sectors. Bahar, Gadgin Matha, Hausmann and Segovia (2026) apply the idea to Japan, where research intensity is near the top of the OECD but productivity growth has been flat since 2000, which they attribute to indirect tax credits that presuppose taxable profit and scale and so favour large incumbents.

We treat the middle-technology trap as a mechanism that can contribute to a middle-income trap, through productivity, and not as a synonym for it. We follow the second lineage because its mechanism, incentive design, needs no foreign actor. We also note the political-economy account of Doner and Schneider (2016), in which business fragmented by firm size and ownership explains the trap. We do not test coalitions (Section 5.2).

**What this paper measures.** The literature identifies a middle-technology trap by outcomes, such as low research intensity or research spending concentrated in mature sectors. We observe none of these and do not measure a trap. We identify *features of incentive design that could contribute to one*: a large distance between the smallest scale at which a compute provider could operate and the smallest scale at which an instrument admits it, with no instrument aimed at the scales between. Whether this structure leads to a trap depends on firm behaviour we do not observe.

### 2.2 AI and the gap in the literature

Two readings of AI compete. Lee (2019) argues that latecomers advance fastest where knowledge becomes obsolete quickly, and AI plausibly fits. The sceptical reading holds that AI favours economies that already hold digital infrastructure, data and skills (Abdurohman and Huang, 2026). Cerutti et al. (2025) find that AI gains concentrate in advanced economies and that under limited access emerging-market output growth falls by about one percentage point, and Lehdonvirta et al. (2024) divide the world into a "Compute North", a "Compute South" with inference capacity and a "Compute Desert".

These literatures yield predictions but not a policy mechanism. The macro models assume an access scenario without examining the instruments behind it, and the compute-geography work measures where capacity sits, not which policies shape domestic supply. Bahar et al. (2026) examine incentive design, but for research tax credits in one advanced economy, not for AI or the layers of a stack. An instrument-level account of eligibility across the AI stack in middle-income economies is missing.

### 2.3 The stack and three dimensions of accessibility

We code four layers: (i) applications and models; (ii) cloud and compute services, the provision of computing capacity as a service from owned or leased facilities; (iii) physical data-centre capacity, the construction and operation of facilities; and (iv) hardware manufacture. Where one instrument covers both (ii) and (iii) without distinguishing them we code "(ii)+(iii)", and call these the compute layers. A country can treat the compute layers as generously as layer (i) while restricting hardware, or the reverse, and a binary split would class these as the same. Our coding concentrates on supply of compute.

A high threshold is not the same as a barrier to new firms, since a capital-rich startup can meet a high capital requirement, and a low priority is not blocked access. We therefore keep three dimensions apart: **layer** (which activities the instrument covers), **scale** (the minimum capital, revenue or staffing it requires) and **vintage** (whether it accommodates new firms or presupposes a revenue base or profit). A fixed compliance cost is neither a scale nor a vintage rule. We code it separately as a recurring burden that falls more heavily on small firms.

### 2.4 Three explanations and one assumption

Each hypothesis concerns one country's AI-related incentive design.

* **H1, cost necessity.** Conditions follow the technical cost of each layer. P1a: where thresholds exist, their height rises with capital intensity. P1b: the most capital-intensive layers carry the strictest capital conditions. P1c: eligibility does not depend on firm age or revenue beyond what capital need implies. P1d: the system imposes no costs unrelated to capital need, such as fixed compliance costs at low capital tiers.
* **H2, scale-favouring design.** The architecture raises entry costs for smaller or newer firms beyond what the technology requires, whatever the intent. P2a: no instrument lies between the smallest viable and the smallest eligible provider. P2b: conditions presuppose a revenue base or impose fixed costs on small firms in layers with low capital need. P2c: there is little explicit accommodation for new firms.
* **H3, administrative habit.** Instruments reuse templates from generic or pre-AI schemes. P3a: eligibility follows a template such as scale tiers common to all activities. P3b: gaps arise where an activity falls outside inherited categories. P3c: rules show no AI-specific tailoring.

**A1, the viability assumption.** A commercially viable scale of AI compute provision exists far below facility scale. Power draw shows that a server can be hosted, not that a provider can survive on it, so A1 is empirical. If A1 fails, absence of instruments below facility scale is what H1 predicts and P2a does not apply. Every rating on absence is conditional on A1. Legal texts separate H1 from the pair {H2, H3} better than they separate H2 from H3.

**The missing-rung proposition.** Hausmann and Rodrik (2003) argue that discovering the cost of a new activity is socially valuable because others can imitate it, so laissez-faire yields too little investment in new activities. We apply this to compute supply, as our own proposition. Let the *rung distance* be the base-10 logarithm of the ratio between the smallest scale an instrument makes eligible and the smallest viable scale of provision. **M: where learning in compute supply requires hands-on operation, and the rung distance is large (we take two orders of magnitude or more) with no instrument aimed at the scales between, domestic entry into compute supply is limited to firms that can bear facility-scale risk.** M is false for a country if the hypothetical-firm test (Section 3.3) shows a small provider eligible, if viability evidence shows A1 false, or if domestic sub-facility providers operate without incentives.

## 3. Research design

### 3.1 Scope and case selection

The paper studies *legal eligibility*: who may qualify under the rules as written. It does not observe realised access, application costs, screening practice or firm outcomes. We selected middle-income ASEAN economies with AI-related incentives in force and accessible consolidated legal texts, differing in income trajectory. The "trapped" labels refer to the middle-income trap and are used only to select cases. On the classification of Bianchi et al. (2024), Thailand and Malaysia are trapped by duration but show improving export complexity. Vietnam is not classified as trapped by any source we reviewed, and the Philippines has a documented trap history at a lower income band; both reached upper-middle-income status in July 2026. We do not classify any country as middle-technology trapped. We excluded Indonesia, one of the ASEAN Four in Ke (2024), because the criterion of AI-related incentives in force was not met on the sources we found. Its incentives (tax holidays, super deductions, duty exemptions) are general and name neither AI nor data centres, the national AI roadmap and AI-ethics presidential regulations were still pending in mid-2026 (Noer and Putra, 2026), and an official of the communications ministry was still urging data-centre tax incentives in September 2025 (W.Media, 2025). We checked secondary sources, not primary texts, so Indonesia is a natural later comparator once the roadmap is enacted (on purposive selection see Seawright and Gerring, 2008).

Thailand is the primary case because it alone publishes approval statistics by sub-activity and ownership. The other three are coded from legal texts. Four purposive cases support analytic inferences about design, not statistical claims about Southeast Asia.

### 3.2 Coding, sources and the common scale

We code primary legal texts, not strategy documents or commentary: Thailand's Board of Investment (BOI) Investment Promotion Guide 2026 and announcements; Vietnam's Decree 260/2026 and Decision 21/2026; Malaysia's Malaysia Digital and Digital Ecosystem Acceleration (DESAC) guidelines; and the Philippines' CREATE MORE Act, its implementing rules and the 2026 Strategic Investment Priority Plan (SIPP). Supporting Information Table S2 lists each source, date and check. The unit of analysis is the instrument. Twenty-nine instruments are coded (Table S1), fourteen of them cross-cutting rules that apply beyond AI. Each is coded on five dimensions: layer; delivery (indirect tax-based support, which presupposes taxable profit, or direct grants, equity and fee waivers); threshold and its basis; new-firm accommodation, coded Yes only for an explicit provision, so that a low threshold is recorded as a threshold and not as accommodation; and recurring compliance burden. The codebook is in the Supporting Information. We report the matrix and do not aggregate it into an index, since any weighting would be an assumption.

One author coded all rows and checked them against the primary texts. A separate instance of a generative AI model then coded all 29 instruments blind, from the codebook and texts alone. Agreement before adjudication was 69 per cent on layer (Cohen's, 1960, kappa 0.60), 83 per cent on delivery (0.73) and 76 per cent on accommodation (0.57), and 28 of 29 threshold figures matched. We resolved disagreements against the text and log them in Table S6. An AI coder shares the first coder's blind spots, so a human check remains desirable. The Vietnamese texts were read through a commercial legal database. The Thai originals, the Vietnamese circulars and the SIPP guidelines are unread.

**Common scale.** Thresholds have different bases and currencies. We convert each capital figure to US dollars (at about 35.7 baht, 4.55 ringgit and 57.7 pesos to the dollar) and then to the capacity it would host, using two benchmarks: US$10.7 million per megawatt of construction (Turner and Townsend, 2025) and US$38 million per megawatt of fully equipped AI capacity (Epoch AI, 2026). We take one eight-accelerator server of about 12 kW, a planning figure above the 10.2 kW maximum NVIDIA lists for its DGX H100 (NVIDIA, n.d.), as the lower bound of provision, which needs US$0.13 million to US$0.46 million of capital to host, and the viable fleet found by the benchmark of Section 5.1 as the working baseline. The rung distance of an instrument is the base-10 logarithm of its threshold over the baseline's capital, reported as a range. The benchmarks are orders of magnitude, the thresholds have different bases, and the conversion tests plausibility, not equality.

### 3.3 Hypothetical firms and the rating of evidence

Eligibility is easier to judge for a concrete firm. We define **Firm A**, a three-person AI software startup; **Firm B**, a reseller of AI compute with 20 accelerated servers on leased colocation space; and **Firm C**, a colocation operator with one megawatt of capacity. For each country we read the instruments that could apply and record *eligible*, *ineligible* or *unclear*. "Eligible" means the stated conditions are met, not that the benefit is obtained.

With four cases, conventional identification is unavailable. We use process-tracing logic (Collier, 2011) and borrow from Fairfield and Charman (2017) the discipline of asking how probable evidence is under each rival, without numerical priors that four cases cannot support. Each hypothesis is rated for each piece of evidence as expected (E, predicted by a stated prediction), compatible (C), unexpected (U, in tension with a prediction or reconcilable only with an extra assumption) or contradicted (X). The weight for the pair a row separates is *strong* if one hypothesis is E and the other U or X with verified coding and no auxiliary assumption, *moderate* if it depends on A1 or unverified coding, and *weak* if no hypothesis is U or X. Absence claims are limited to AI-related and digital-sector instruments; general SME, startup and research schemes are not coded.

## 4. Findings

### 4.1 Thailand

Thailand's BOI administers AI-relevant incentives through its digital division. Software and digital-content development (Activity 8.1.1) receives an eight-year corporate income tax exemption, capped each year at 100 per cent of qualifying expenditure, on an investment condition of at least THB 1.5 million a year (about US$42,000) of salaries for additionally employed Thai IT staff. A small technical team can reach it. The compute activities (8.2) are screened differently. Data centres (8.2.1) require at least 2 MW of IT load in both tiers, ISO/IEC 27001 certification and Thai personnel in half of executive and expert positions within three years. Cloud services (8.2.2) have no minimum capital, but the project must sit in two certified data centres with 10 Gbps interconnection and hold ISO/IEC 27001 and 20000-1 before using the exemption. GPU-based data hosting (8.2.4.1) requires capital of at least THB 5,000 million (about US$140 million) excluding land. The activity closest to training or serving AI models therefore carries the highest capital condition, while general cloud carries certification and location conditions in its place. In January 2025 BOI promoted a THB 3.25 billion (about US$91 million) project of Siam AI, a Thai company that operates GPU clusters, as cloud services and not as data hosting (Board of Investment of Thailand, 2025). At least one GPU-based provider has therefore used the cloud route without meeting the THB 5,000 million condition, although how BOI would class a smaller one is untested. A cross-sectoral competitiveness measure extends the exemption to at most 13 years where spending reaches 1 per cent of sales (or THB 200 million, if lower) in the first three years. It is proportional to sales but presupposes them, and is a generic template.

In 2025, 96 approved projects under Activity 8.1.1 carried combined investment of THB 933 million, an average of about THB 9.7 million, while 24 data-centre projects under 8.2.1 carried THB 458,000 million, about US$534 million each (Board of Investment of Thailand, 2026b). A single data-hosting project under 8.2.4 carried THB 126,793 million. Thai-held shares of registered capital fall with depth: 46 per cent in software, 15 per cent in data centres and none in the data-hosting project. This describes capital in approved projects, rests on three points, and does not show that Thai firms were excluded, since a cost-based account also predicts it.

### 4.2 Vietnam

Decree 260/2026, in force from 1 July 2026, implements the Law on High Technology (Vietnam, 2026a). Support attaches to research on technologies listed by the Prime Minister, and includes state funding of tasks up to 100 per cent, duty exemption, cost deductions and interest support. The research-centre track demands 60 per cent of workers in research and development, which restricts it to purpose-built institutions. The startup track requires research on listed technology and either revenue growth of at least 20 per cent a year over two years or a commercialisation-ready solution, and offers fee exemptions, controlled testing and priority for venture-fund equity (Article 11). It is the clearest explicit accommodation for new firms in our data. Enterprise criteria carry research ratios that fall as capital rises (Articles 14 and 15). Decree 260 also supports technology infrastructure, including computing and data infrastructure, with no scale threshold, but for research tasks, not commercial supply.

Decision 21/2026, in force from 1 July 2026, lists ten strategic technologies and thirty strategic products in two unranked groups (Vietnam, 2026b). Group 1 includes Vietnamese-language large language models, virtual assistants and specialised AI, edge-processing AI cameras, digital-twin platforms and cloud-computing platforms. Group 2 includes specialised chips. The Decision attaches no benefit to either group. Benefits run through Decree 260, where a strategic-technology enterprise must earn at least 80 per cent of net revenue from strategic products, spend at least 1 per cent of net revenue less inputs on research and development, hold at least 10 per cent of staff in research and development and reach 40 per cent local content (Article 16). These are proportional conditions, not capital thresholds, but the revenue condition presupposes a product already earning revenue. "Cloud-computing platforms" has no definition and may mean platform software, not capacity, so it is weak evidence on compute. Vietnam's coded instruments contain no capital screen at any layer, and designation is not blocked access.

### 4.3 Malaysia

Malaysia runs two parallel schemes. The Malaysia Digital (MD) incentive covers new activities using ten promoted technology enablers, including AI and cloud (Malaysia Digital Economy Corporation, 2025). The applicant needs only RM50,000 of paid-up capital (about US$11,000), the lowest stated entry threshold among the countries that state one, a new activity and adequate staff, and receives a reduced tax rate or allowance for ten years. It must file an annual self-declaration verified by an external auditor at its own cost, a largely fixed cost that weighs more on a small firm. Because "provision of services utilising cloud" is an MD activity, a small compute provider could in principle apply. We have not confirmed that MDEC accepts resale of capacity as an MD activity.

The DESAC scheme serves data-centre and cloud operators (Malaysian Investment Development Authority, 2024). It offers an investment tax allowance of 100 or 60 per cent on qualifying capital expenditure excluding land, or a special tax rate. Both tiers need paid-up capital of RM2.5 million (about US$550,000), which measures company capital, not project scale, and the ten-year option requires cumulative capital expenditure of RM1 billion (about US$220 million) in years six to ten. The sustainability guideline governing data-centre applications has a smallest category of 0.85 MW to under 4.25 MW (Malaysia, Ministry of Investment, Trade and Industry, 2024). DESAC conditions are written for facility operators: vendor programmes cover cooling and power systems, and the allowance applies to capital investment, which a firm that leases space largely lacks. The New Incentive Framework moves incentives towards outcome-based tiers, but DESAC stays available until its window expires (Malaysian Investment Development Authority, 2026).

### 4.4 The Philippines

The CREATE MORE Act (Republic Act 12066) and the 2026 SIPP give the Philippines a different structure (Philippines, 2024; Philippines, Office of the President, 2026). Incentives go only to listed activities, with a cost-benefit analysis at application. Neither the Act nor the implementing rules state a minimum investment, and the investment promotion agency may register any listed project whatever its capital (Philippines, Department of Finance and Department of Trade and Industry, 2025). The rules require audited statements where applicable and projections for the whole period, a fixed documentation cost. The SIPP names AI and data infrastructure and splits them by tier: software and hyperscalers, and data centres that rely on the grid (as telecommunications infrastructure), are in Tier I, while AI and data-science services and data centres with their own power supply are in Tier III. It states no size condition for any of them, and its qualification guidelines are still to come.

The Act sets a firm-scale boundary at PHP 15 billion of investment capital (about US$260 million): the agency grants incentives to listed projects at or below it and larger ones go to the Fiscal Incentives Review Board (FIRB), with availment periods of 24 to 27 years. Beyond this the President may craft a bespoke package for a highly desirable project with minimum capital of PHP 50 billion (about US$865 million) or at least 10,000 direct jobs, with a 40-year cap. The boundary applies to every activity, so the capital rule is generic while the activity tiers are AI-aware. The Philippines therefore encodes no capital screen specific to compute, and a data centre's tier depends on its power source, not its size.

### 4.5 Cross-country synthesis

Table 1 sets out the coded dimensions. The countries differ in where, and by what, they screen entrants.

**Table 1. Coded incentive dimensions by country and layer**

| Dimension | Thailand | Vietnam | Malaysia | Philippines |
|---|---|---|---|---|
| Layer (i) | Accessible: THB 1.5m (US$42,000) a year of Thai IT salaries | Accessible: startup track (any listed technology); Group 1 products | Accessible: RM50,000 (US$11,000) paid-up capital | Accessible: no minimum; listing and cost-benefit evaluation |
| Compute layers | Data centres at least 2 MW. Cloud: no capital minimum, two certified data centres, ISO 27001 and 20000-1. GPU hosting: at least US$140m | Cloud-computing platforms listed, undefined; no capital rule; infrastructure support for research tasks | MD track covers cloud at RM50,000. DESAC: paid-up floor US$0.55m, smallest category 0.85 MW, ten-year condition US$220m | Hyperscalers and grid data centres Tier I; own-power data centres Tier III; no size condition; PHP 15bn routing boundary |
| Aimed at compute below facility scale | None; cloud has no capital minimum | None | None; MD track may admit | None |
| Explicit new-firm accommodation | None | Startup track (Art. 11) | None | None |
| Recurring compliance | ISO certification | Research ratios; startup reports | Audited declaration at own cost | Cost-benefit; FIRB review |
| Where the screen falls | Capacity and capital at data-centre and GPU activities; certification at cloud | Designation, recognition, enterprise criteria | Audit cost (MD); 0.85 MW and outcome conditions (DESAC) | Listing, evaluation, firm-scale routing |

*Note.* Figures are approximate. Source: primary texts (Table S2). Layers (ii) and (iii) are coded together where instruments do not distinguish them. MD = Malaysia Digital; DESAC = Digital Ecosystem Acceleration scheme; FIRB = Fiscal Incentives Review Board.

Entry thresholds at layer (i) are low or absent. At the compute layers the figures have three bases (company capital, project scale, cumulative spending), so we read them as orders of magnitude. Only Vietnam has an explicit startup track, Thailand's deepest tier presupposes sales, and three countries use tax-based instruments that presuppose profit. The Philippine boundary and Thailand's competitiveness measure look like generic templates, consistent with H3 but untested without pre-AI instruments.

The differences group into four architectures (Table 2).

**Table 2. Four incentive architectures**

| Architecture | Country | Where the screen sits | Implication for a small entrant to compute supply |
|---|---|---|---|
| Capital-gated activities | Thailand | Capacity (2 MW) and capital (US$140m) at data-centre and GPU hosting; certification at cloud | A low-capital cloud route exists, screened by certification; GPU rental and data centres are gated |
| Two parallel tracks | Malaysia | MD: audit cost. DESAC: categories from 0.85 MW and facility-oriented conditions | A small cloud provider may use MD; the data-centre track starts at 0.85 MW |
| Strategic-technology list | Vietnam | Designation and enterprise criteria, not capital | No capital barrier; access depends on designation and uncoded instruments |
| Activity tiers with a common boundary | Philippines | Listing and firm scale; for data centres, power source | The same boundary governs software and data centres; no size condition |

Table 3 applies the common scale to each capital threshold, and Figure 1 places them against the cost benchmarks.

**Table 3. Capital thresholds on the common scale**

| Threshold | Basis | US$ million | From one server (orders of magnitude) | From viable fleet, central case (orders) |
|---|---|---|---|---|
| Thailand, GPU hosting (8.2.4.1) | Minimum capital | 140 | 2.5 to 3.0 | 0.2 to 1.0 |
| Thailand, data centres (8.2.1) | 2 MW of IT load | 21 to 76 to host | 1.7 to 2.8 | -0.6 to 0.8 |
| Thailand, cloud (8.2.2) | No capital condition | not defined | not defined | not defined |
| Malaysia, DESAC smallest category | 0.85 MW | 9 to 32 to host | 1.3 to 2.4 | -0.9 to 0.4 |
| Malaysia, DESAC ten-year condition | Cumulative capex | 220 | 2.7 to 3.2 | 0.4 to 1.2 |
| Philippines, firm-scale boundary | Investment capital; routes to FIRB | 260 | 2.8 to 3.3 | 0.5 to 1.3 |
| Philippines, presidential package | Capital, or 10,000 jobs | 865 | 3.3 to 3.8 | 1.0 to 1.8 |
| Vietnam | No capital rule | not defined | not defined | not defined |

*Note.* Distance is log10 of the threshold over a baseline. The one-server baseline is US$0.13m to US$0.46m, the capital to host one eight-accelerator server on the two benchmarks. The viable-fleet baseline is US$13m to US$80m, the fleet of 45 to 270 servers that covers a provider's overhead at US$3.00 per GPU-hour and 80 per cent utilisation (Section 5.1, Table S5); it falls to US$0.3m to US$2m at US$3.85 and does not exist at US$2.35. Malaysia's paid-up capital floors measure company capital and are not placed on the scale. The Philippine figures are a routing boundary and a package condition, not entry rules. Negative values mean the threshold lies inside the viable range.

![**Figure 1.** Explicit eligibility thresholds against cost benchmarks, US$ million, log scale. Shaded bands show the capital to host the stated capacity, from construction cost (US$10.7m per MW) to fully equipped AI capacity (US$38m per MW). Thailand's software figure is annual salary spend (hollow marker); Malaysia's two paid-up capital figures are company capital, not project scale; the 0.85 MW bar shows the capital to host the smallest DESAC category. Vietnam states no capital threshold.](fig1_threshold_ladder.png)

In Thailand the GPU-hosting gate lies two and a half to three orders of magnitude above one server, and the data-centre condition 1.7 to 2.8, while cloud has no capital condition. Measured from the viable fleet of the central case, the GPU-hosting gate is 0.2 to 1.0 orders away and the Thai and Malaysian facility categories lie inside the viable range. In Malaysia the data-centre track starts 1.3 to 2.4 orders above one server while the Digital track admits cloud at RM50,000. Vietnam and the Philippines state no capital threshold at the compute layers. Where a low-capital cloud route exists, the screen is a fixed compliance cost.

**Table 4. Hypothetical-firm eligibility test, provisional reading**

| Country | Firm A: AI software startup | Firm B: reseller, 20 servers on leased colocation | Firm C: 1 MW colocation operator |
|---|---|---|---|
| Thailand | Eligible (8.1.1) | Possibly eligible as cloud (8.2.2, no capital minimum, but two certified data centres and ISO certification, the route Siam AI used); GPU rental as such falls under 8.2.4.1 | Ineligible (8.2.1 needs 2 MW) |
| Vietnam | Eligible (startup track, subject to recognition) | Unclear (cloud platforms listed with no capital rule; capacity resale not addressed) | Unclear (no data-centre category in Decree 260 or Decision 21) |
| Malaysia | Eligible (MD; audited declaration at own cost) | Possibly eligible under MD; unlikely under DESAC | Eligible to apply under DESAC (falls in the 0.85 to 4.25 MW category; RM2.5m paid-up capital; committee approval is discretionary) |
| Philippines | Eligible if listed, subject to cost-benefit evaluation | Unclear (not clearly a hyperscaler or a data centre as the SIPP defines it) | Possibly eligible (colocation fits the SIPP definition; no size condition) |

*Note.* Provisional reading by one reader. "Eligible" means conditions are met, not that the benefit is obtained.

Small providers are excluded by capital or capacity from Thai data centres and GPU hosting (Firm C by the 2 MW condition; Firm B if its service is classed as GPU hosting) and from the Malaysian data-centre track, and are admitted on paper, subject to fixed compliance costs, through Thailand's cloud activity and Malaysia's Digital track. For absence, we distinguish three readings: no instrument is *aimed at* sub-facility compute, none *could be used by* such a provider on software-firm terms, and none has a *tier* below facility scale. Reading one holds on the instruments coded. Reading two fails on paper for generic cloud in Thailand and Malaysia, subject to certification and audit costs, and holds for GPU rental in Thailand and for facility activities. Reading three holds for facility activities.

## 5. Discussion

### 5.1 Cost necessity versus incentive design

The strongest challenge to a design reading is H1: infrastructure thresholds reflect the real cost of data centres. Construction cost reached about US$10.7 million per megawatt in 2025 (Turner and Townsend, 2025), and equipped AI capacity implies about US$38 million per megawatt (Epoch AI, 2026). On these figures Thailand's US$140 million threshold corresponds to 13 megawatts of construction or under 4 megawatts of equipped capacity. Cost therefore explains the height of the Thai threshold (P1a), and the gap between software and infrastructure thresholds is not evidence of bias.

Cost does not by itself explain what lies below the threshold, so we test A1 with a benchmark of provider economics (Table S5). Its inputs are indicative, from vendor, reseller and trade sources. A single server is not a viable provider. Whether a small one is depends on price. At the contract-index price of about US$2.35 per GPU-hour no small provider breaks even. At US$3.00 it needs about 80 per cent utilisation and a fleet of 45 to 270 servers (US$13 million to US$80 million) to cover an overhead of US$50,000 to US$300,000 a year, and at the US$3.85 on-demand list price a few servers suffice. A scale provider breaks even at a utilisation about 20 percentage points lower, through cheaper colocation, capital and hardware. Measured from the central-case fleet, Thailand's GPU-hosting gate is 0.2 to 1.0 orders of magnitude away (Table 3), Thailand's 2 MW and Malaysia's 0.85 MW categories lie inside the viable range, and Siam AI's project lies near its upper end. A1 therefore holds only conditionally. If small providers can sell near US$3.85, the absence of instruments for a few servers is a design outcome and M applies. If prices sit nearer US$3.00 or below, viable scale is close to the thresholds and H1 explains most of the absence. The benchmark cannot choose between these cases without data on the prices small regional providers obtain.

Malaysia is the informative comparison. Its low-capital digital track covers cloud beside a data-centre track written for facility operators. If the MD track admits capacity resale, a small provider can be admitted on paper at the cost of an annual audit, and Thailand's facility threshold is not forced by the same cost structure. If it does not, Malaysia joins Thailand. Vietnam and the Philippines show a different point. Capital intensity is highest at the compute layers, yet neither states a capital condition there. H1 predicts the strictest conditions where intensity is highest, so this is unexpected under H1. It shows that a capital gate is a design choice, not that small firms can enter, because their screen may lie in designation or listing.

### 5.2 Ownership

Foreign capital is a larger share of registered capital in Thailand's infrastructure layers than in software. This does not show that Thai firms were excluded or that Thailand failed to accumulate capability. A cost-based account predicts it, since the most capital-intensive layers attract the deepest-pocketed firms, for data centres global operators (Lehdonvirta, Wú and Hawkins, 2025). The gradient is consistent with the account of Ke (2024) but cannot distinguish it from capital-intensity effects. Vietnam's announced data-centre investment is led by its largest conglomerate, which does not show capture: that would need evidence of restricted entry or discriminatory support (Doner and Schneider, 2016), and the coded rules contain no capital screen at the compute layers.

### 5.3 What the evidence supports

Table 5 rates the main evidence against the predictions of Section 2.4. The full matrix of twelve items, with what would change each rating, is in the Supporting Information (Table S3).

**Table 5. Evidence matrix (selected items)**

| # | Evidence | H1 | H2 | H3 | Pair separated, weight |
|---|---|---|---|---|---|
| E2 | Low-capital digital track covers cloud beside a 0.85 MW data-centre track (Malaysia) | C | U | C | H2 against H1 and H3, moderate and provisional |
| E3 | No instrument aimed at sub-facility compute (Thailand, Vietnam, Philippines) | U if A1 holds | E if A1 holds | E | H1 against {H2, H3}, weak to moderate; A1 holds only above about US$3.00 per GPU-hour |
| E4 | No capital condition at the compute layers despite capital intensity (Vietnam, Philippines) | U | C | C | H1 against {H2, H3}, moderate |
| E5 | Exemption extension tied to spending of 1% of sales (Thailand) | U | E | E | H1 against {H2, H3}, moderate |
| E6 | Fixed certification and audit costs on low-capital cloud routes (Thailand, Malaysia) | U | E | C | H1 against H2, moderate, cost unmeasured |
| E7 | Firm-scale boundary common to all activities (Philippines) | U | C | E | H3 against H1, weak to moderate |
| E8 | Explicit startup track with direct support (Vietnam) | U | U | U | None |

*Note.* E = expected; C = compatible; U = unexpected. Predictions P1a to P3c as in Section 2.4.

Four results follow. First, cost explains the height of Thailand's threshold, and the data cannot separate a design reading from it on that point. Second, thresholds are not forced by cost: Vietnam and the Philippines state none at the compute layers, and Malaysia admits cloud at RM50,000 on a separate track. Third, H1 is unexpected for features that cost cannot generate: a sales-based extension (E5) and fixed certification and audit costs (E6). Fourth, E8 is unexpected under all three hypotheses. A deliberate startup track shows that these governments can and do design for new firms, and limits H2 as a general account. H2 and H3 remain hard to separate: only E7, and only partly, favours H3. We conclude that the pattern is not only cost-driven and that capital gates are a design choice where they occur, without isolating whether design or habit produced them.

**Sensitivity.** Dropping the evidence against H1 one row at a time leaves the case standing, and dropping rows that depend on A1 (E2, E3) leaves E4 to E7. If MDEC does not accept capacity resale, E2 becomes compatible. The claim that rungs are missing in Thailand depends on A1, which holds only at prices near US$3.85, and on the coverage of general instruments. It is falsified if Firm B or Firm C can use a general instrument on the same terms as a software firm, or if viable small providers operate without incentives. A competing reading cannot be excluded: no middle-income economy can compete with hyperscalers, so applications-led specialisation with infrastructure dependence is sound. Separating the readings needs data on domestic small providers, the prices they obtain and application-layer outcomes, which we do not observe.

### 5.4 Relation to the literature

Bahar et al. (2026) show that indirect tax credits favour large profitable firms in Japan. Thailand's deepest tier presupposes sales, three of four countries deliver the accessible tier through indirect instruments, and Malaysia's fixed audit cost is regressive through a different channel. Their problem is misallocation among sectors for established firms, ours is entry to a new stack, and our evidence is rules, not spending. The lesson we take from Fuest et al. (2024) and Bahar et al. (2026) is about method: look at instrument design. For the access scenarios of Cerutti et al. (2025), the rules we code show where entry is open on paper, not what firms do with it. The architectures suggest testable propositions for other countries: capital gates screen on capital stock, list-based designs shift screening to discretion, and the rung distance is larger where one gate is set at facility scale than where a separate low-capital track covers the same activity.

## 6. Policy implications

Each implication follows from a finding and should be read with the limits in Section 7.

**Audit eligibility before building new rungs.** Capital or capacity conditions exclude small providers from Thai GPU hosting and data centres and from Malaysian data centres, while cloud routes admit them subject to certification and audit costs. The benchmark suggests that the rung that matters lies at tens to hundreds of servers, where Thai cloud and Malaysian Digital routes already exist, so fixed costs deserve attention first. An audit with hypothetical firms, as in Section 3.3, would show a government which of its instruments a small provider could use. Where it shows exclusion, the options are extending eligibility to colocation tenancy or modular deployment, lowering fixed certification and audit costs for small providers, or providing subsidised access to public or consortium compute. Tax relief presupposes profit, so small rungs may suit direct support or refundable credits and larger ones milestone-based incentives with compliance proportional to size (Table S4). Vietnam's startup track is an application-layer pathway keyed to technical criteria, not capital. Risks include subsidising resale of foreign-owned capacity and fiscal leakage; we have not costed any option, and a time-limited pilot would show cost and take-up first.

**Review instruments that presuppose profit or impose fixed costs where capital need is low,** such as Thailand's research tier and Malaysia's audited declaration. Verification in proportion to firm size could lower the fixed cost.

**Treat infrastructure dependence as an explicit choice.** If dependence on foreign infrastructure is an acceptable trade-off, it should be stated as one, with attention to data sovereignty. Because we cannot separate it from rational specialisation, evidence on the prices small providers obtain should be collected before thresholds change.

## 7. Limitations

First, legal eligibility is not realised access: firms may be unable to use an eligible instrument, and may reach support through general schemes we have not coded. The findings describe an opportunity structure, not who benefits. Second, one author coded and checked the rows against English or database texts, with only an AI second coder, and the Thai originals, Vietnamese circulars and SIPP guidelines are unread, so findings that depend on a classification are provisional. Third, the central claim depends on A1, which we test only with a stylised benchmark built from vendor prices, and on an absence claim limited to AI-related and digital-sector instruments. Fourth, layers (ii) and (iii) cannot be separated in several instruments, hardware is coded only for Vietnam, and thresholds have different bases, so scale comparisons are order-of-magnitude. Fifth, we code investment incentives only, and public compute programmes may fill part of the gap. Sixth, only Thailand publishes approval data by sub-activity and ownership, and its gradient rests on three points. Seventh, four cases and ordinal ratings cannot separate H2 from H3 or establish causation, and the target is moving.

## 8. Conclusion

This paper asked where four Southeast Asian incentive systems screen entrants to the AI industry. All four make application development accessible on the stated thresholds, and Vietnam adds a startup track with direct equity access. Above that layer they use four architectures. Thailand gates data centres by capacity and GPU hosting by capital, 1.7 to 3.0 orders of magnitude above one server but at most one order above the fleet a benchmark finds viable at central prices, while cloud services carry certification in place of capital. Malaysia runs a low-capital digital track covering cloud beside a data-centre track starting at 0.85 MW. Vietnam lists strategic technologies without ranking them and states no capital rule. The Philippines lists activities by tier and applies one firm-scale boundary to all. No instrument we coded is aimed at compute provision below facility scale. Cost largely explains Thailand's gate, but not why Vietnam and the Philippines need no capital gate, why Malaysia can run a low-capital cloud track or why Thailand's research tier presupposes sales. The evidence concerns eligibility, not access, and does not show that any of the four is in a middle-technology trap. The next steps are to measure the prices and utilisation that small regional providers actually obtain, code the general schemes, and link rules to firm-level take-up.

## Acknowledgments

[AUTHORS TO COMPLETE.]

## Declaration of interest statement

[AUTHORS TO COMPLETE: the authors report no conflict of interest, or state any.]

## Funding

[AUTHORS TO COMPLETE: funding details, or "No funding was obtained for the reported work."]

## Declaration of generative AI use

The authors used generative AI to polish the writing of this manuscript and, as a blind second coder, to check the coding of legal instruments (Section 3.2). The authors reviewed and edited the text and take full responsibility for the content.

## References

Abdurohman, & Huang, X. (2026). *Can ASEAN+3 economies still escape the middle-income trap in the AI era?* ASEAN+3 Macroeconomic Research Office.

Ang, A. (2026, July 3). The World Bank has elevated Vietnam and the Philippines to upper-middle-income status. *Fortune*.

Bahar, D., Gadgin Matha, S., Hausmann, R., & Segovia, S. (2026). *Japan's innovation challenge: Escaping the middle-technology trap* (Growth Lab Working Paper No. 269). Harvard University.

Bianchi, C., Isabella, F., Martinis, A., & Picasso, S. (2024). Varieties of middle-income trap: Heterogeneous trajectories and common determinants. *Structural Change and Economic Dynamics, 71*, 320-336.

Board of Investment of Thailand. (2025, January 29). *Thailand BOI approves investments worth a total of US$5 billion, including TikTok's data hosting project*. https://osos.boi.go.th/EN/news/2163

Board of Investment of Thailand. (2026a). *Investment promotion guide 2026*. Office of the Board of Investment.

Board of Investment of Thailand. (2026b). *Investment promotion statistics: Approvals by sub-activity, January to December 2025*. Investment Services Center.

Cerutti, E., Garcia Pascual, A. I., Kido, Y., Li, L., Melina, G., Mendes Tavares, M., & Wingender, P. (2025). *The global impact of AI: Mind the gap* (IMF Working Paper No. 25/76). International Monetary Fund.

Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement, 20*(1), 37-46.

Collier, D. (2011). Understanding process tracing. *PS: Political Science & Politics, 44*(4), 823-830.

Doner, R. F., & Schneider, B. R. (2016). The middle-income trap: More politics than economics. *World Politics, 68*(4), 608-644.

Eichengreen, B., Park, D., & Shin, K. (2014). Growth slowdowns redux: New evidence on the middle-income trap. *Japan and the World Economy, 32*, 65-84.

Epoch AI. (2026). *Total cost of ownership of a one-gigawatt AI data center*. https://epoch.ai/data-insights/ai-datacenter-cost-breakdown

Fairfield, T., & Charman, A. E. (2017). Explicit Bayesian analysis for process tracing: Guidelines, opportunities, and caveats. *Political Analysis, 25*(3), 363-380.

Fuest, C., Gros, D., Mengel, P.-L., Presidente, G., & Tirole, J. (2024). *EU innovation policy: How to escape the middle technology trap*. EconPol Europe and ifo Institute.

Hausmann, R., & Rodrik, D. (2003). Economic development as self-discovery. *Journal of Development Economics, 72*(2), 603-633.

Imam, P. A., & Temple, J. R. W. (2026). At the threshold: The increasing relevance of the middle-income trap. *Scandinavian Journal of Economics*.

Ke, Y. (2024). ASEAN Four's middle income trap dilemma: Evidence of the middle technology trap. *Asian Review of Political Economy, 3*(1), 1-29.

Lee, K. (2019). *The art of economic catch-up: Barriers, detours and leapfrogging in innovation systems*. Cambridge University Press.

Lehdonvirta, V., Wú, B., & Hawkins, Z. (2024). Compute North vs. Compute South: The uneven possibilities of compute-based AI governance around the globe. *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, 7*(1).

Lehdonvirta, V., Wú, B., & Hawkins, Z. (2025). Weaponised interdependence in a bipolar world: How economic forces and security interests shape the global reach of US and Chinese cloud data centres. *Review of International Political Economy*.

Malaysia Digital Economy Corporation. (2025). *Guidelines on Malaysia Digital (MD) tax incentive (new investment incentive)* (revised 22 July 2025). MDEC.

Malaysia, Ministry of Investment, Trade and Industry. (2024). *Guideline for sustainable development of data centre*. Malaysian Investment Development Authority.

Malaysian Investment Development Authority. (2024). *Guidelines and procedures for the application of the Digital Ecosystem Acceleration (DESAC) scheme*. MIDA.

Malaysian Investment Development Authority. (2026). *New Incentive Framework (NIF): Media release and frequently asked questions*. MIDA.

Noer, H., & Putra, M. I. D. (2026, July 10). *Consolidation without completion: Indonesia's AI developments in 2026*. Tech For Good Institute.

NVIDIA. (n.d.). *NVIDIA DGX H100/H200 user guide: Introduction*. https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html

Philippines, Department of Finance, & Department of Trade and Industry. (2025). *Implementing rules and regulations of Title XIII of the National Internal Revenue Code of 1997, as amended by Republic Act No. 12066*. Fiscal Incentives Review Board.

Philippines, Office of the President. (2026). *Memorandum Order No. 47: Approving the 2026 Strategic Investment Priority Plan*. Malacañang.

Philippines. (2024). *Republic Act No. 12066: Corporate Recovery and Tax Incentives for Enterprises to Maximize Opportunities for Reinvigorating the Economy (CREATE MORE) Act*. Congress of the Philippines.

Seawright, J., & Gerring, J. (2008). Case selection techniques in case study research: A menu of qualitative and quantitative options. *Political Research Quarterly, 61*(2), 294-308.

Turner & Townsend. (2025). *Data centre construction cost index 2025-2026*. Turner & Townsend.

Vietnam. (2026a). *Decree No. 260/2026/ND-CP detailing the implementation of the Law on High Technology*. Government of Vietnam.

Vietnam. (2026b). *Decision No. 21/2026/QD-TTg promulgating the list of strategic technologies and strategic technology products*. Prime Minister of Vietnam.

W.Media. (2025, September 4). Indonesia must simplify rules and offer tax incentives to woo data center investors: Official. *W.Media*. https://w.media/indonesia-must-simplify-rules-and-offer-tax-incentives-to-woo-data-center-investors-official/

Zheng, Y. (2024). The middle technology trap: China in a comparative perspective. *Asian Review of Political Economy, 3*(1), 11.
