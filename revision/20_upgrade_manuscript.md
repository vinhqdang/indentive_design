---
title: "Entry Barriers in AI Investment Incentives: An Index and Evidence from Four Southeast Asian Economies"
---

## Abstract

Governments in Southeast Asia use investment incentives to attract artificial intelligence (AI) infrastructure, but we do not know whether the rules shape who enters. We code 29 instruments in Malaysia, the Philippines, Thailand and Viet Nam and build a transparent index of entry barriers for 11 routes, with four dimensions: capital, fixed compliance cost, reliance on revenue history, and delivery through profit-based tax relief. We check the index against Thai approval statistics, GPU cluster records and 62 project records, using predictions fixed beforehand. Barriers at facility scale are high only in Thailand and Malaysia. Project size rises with the index in Thailand, and domestic GPU clusters appear on the low-capital cloud route at about 1 MW. Capacity thresholds are not where projects cluster. The evidence is small-sample and descriptive.

**Keywords:** artificial intelligence; entry barriers; incentive design; investment incentives; Southeast Asia

## 1. Introduction

Whether domestic firms can build AI computing capacity, and not only buy it, matters for economies that want to move from middle to high income. If they can only adopt what foreign providers supply, more of the gains from AI are likely to accrue elsewhere (Cerutti et al., 2025). Building capacity depends on what investment incentive systems let in, because incentives are the main tool host governments use to attract investors and they write the eligibility rules. Yet we know little about those rules for AI. Studies describe aggregate spending, access scenarios and the geography of compute (Lehdonvirta et al., 2024). We found no systematic, measurable account of how incentive rules treat firms of different scale and age across the layers of the AI stack, or of whether such rules relate to who actually enters.

This paper makes that comparison for Malaysia, the Philippines, Thailand and Viet Nam. It does three things. First, it codes 29 instruments from primary legal texts and turns the codes into a transparent index of entry barriers for 11 entry routes. Second, it tests a viability assumption: whether a small provider of AI computing can survive at all, because a barrier only matters if entry at that scale would otherwise be viable. Third, it checks the index against outcome evidence, using five predictions that we recorded before analysing the outcome data: official Thai approval statistics by activity, a public dataset of GPU clusters, and 62 project records collected from public sources.

We find that barriers at facility scale are high only in Thailand and Malaysia, where capital or capacity gates lie two to three orders of magnitude above the capital to host one server, and that no system aims an instrument at providers below facility scale. In Thailand, mean project size rises with the index and the Thai-held share of capital falls with it, with one exception, the cloud route, where Thai-owned GPU clusters of about 1 MW operate without meeting any capital gate. Stated capacity thresholds are not where projects cluster: approved data-centre projects are 10 to 300 MW, six or more times the stated minima. We read this as evidence that cost, not only design, shapes thresholds at facility scale, and that the screen that matters for smaller domestic providers is fixed compliance cost and reliance on revenue history. The evidence is a small-sample, descriptive linkage and does not identify causal effects.

Section 2 sets out the framework and predictions. Section 3 describes the data and the index. Section 4 reports results. Section 5 discusses implications and limits, and Section 6 concludes.

## 2. Framework and predictions

### 2.1 Why entry at small scale matters

Two literatures motivate the question. The first concerns middle-income growth. Slowdowns in middle-income economies are mainly slowdowns in total factor productivity (Eichengreen et al., 2014), and relative productivity does not converge to the frontier as capital intensity and human capital do (Imam & Temple, 2026). A technological version of the argument says that firms in the ASEAN middle-income economies kept to mature technology while multinationals held the core (Ke, 2024), and that incentives delivered through indirect tax credits favour large profitable incumbents (Bahar et al., 2026). The second literature concerns the effect of fiscal incentives on firm behaviour. Tax incentives change research spending (Bloom et al., 2002), so eligibility rules decide who responds.

For AI, the economic mechanism we have in mind is learning by operating. Hausmann and Rodrik (2003) argue that discovering what an economy can produce at competitive cost is valuable because others can imitate the discovery, and that firms underinvest in it. If domestic firms cannot operate compute at a scale that lets them learn the costs of running it, the knowledge stays with foreign operators, and domestic AI developers become price takers on imported capacity. This is a hypothesis about a channel from entry rules to productivity, and we do not test it. We test the earlier link, from incentive rules to who enters.

### 2.2 The stack and three dimensions of accessibility

We code four layers of the AI stack: (i) applications and models; (ii) cloud and compute services, the provision of computing capacity as a service; (iii) physical data-centre capacity; and (iv) hardware manufacture. Where one instrument covers both (ii) and (iii) without distinguishing them we code "(ii)+(iii)", and we call these the compute layers. Our coding concentrates on supply of compute, because entry by domestic providers is a supply question.

A high threshold is not the same as a barrier to new firms, since a capital-rich startup can meet a high capital requirement. We therefore keep three dimensions apart: layer (which activities the instrument covers), scale (the minimum capital, revenue or staffing it requires) and vintage (whether it accommodates new firms or presupposes a revenue base or profit). A fixed compliance cost is neither a scale nor a vintage rule. We record it separately, as a recurring burden that falls more heavily on small firms.

### 2.3 Three explanations and the viability assumption

The pattern of thresholds can have three kinds of explanation. **Cost necessity** (H1): conditions follow the technical cost of each layer, so thresholds rise with capital intensity and impose no costs unrelated to capital need. **Scale-favouring design** (H2): the architecture raises entry costs for smaller or newer firms beyond what the technology requires, whatever the intent, for example through fixed costs or conditions that presuppose a revenue base. This is the mechanism that Bahar et al. (2026) identify for research tax credits in Japan, through indirect instruments that presuppose profit. **Administrative habit** (H3): instruments reuse templates from generic or pre-AI schemes, such as scale tiers common to all activities.

The assumption **A1** is that a commercially viable scale of AI compute provision exists below facility scale. If A1 fails, the absence of instruments below facility scale is what H1 predicts. We test A1 in Section 4.3. We measure scale by the rung distance: the base-10 logarithm of the ratio between an instrument's threshold and the capital needed at the smallest viable scale of provision.

### 2.4 Predictions

We fixed five directional predictions before analysing the outcome data, and committed them to the project repository on 26 October 2026. **P1:** within a country, mean project investment is higher in routes with a higher capital barrier. **P2:** the domestic share of capital or projects is lower in routes with a higher composite index. **P3:** where a capacity threshold is stated, projects cluster at or just above it, and none lie below. **P4:** routes with no capital barrier but fixed compliance costs attract fewer domestic entrants than the lowest-friction route in the same country. **P5:** systems with no stated capital rule at the compute layers do not show a systematically higher domestic share than systems with one. Results that run against a prediction count against the index as an explanation of entry.

## 3. Data and methods

### 3.1 Instruments, coding and reliability

We code primary legal texts, not strategy documents: Thailand's Board of Investment (BOI) Investment Promotion Guide 2026 and announcements; Viet Nam's Decree 260/2026 and Decision 21/2026; Malaysia's Malaysia Digital and Digital Ecosystem Acceleration (DESAC) guidelines; and the Philippines' CREATE MORE Act, its implementing rules and the 2026 Strategic Investment Priority Plan (SIPP). The unit of analysis is the instrument. Twenty-nine instruments are coded (Supplementary Table S1) on five dimensions: layer; delivery (indirect, tax-based support that presupposes taxable profit, or direct grants, equity and fee waivers); threshold and its basis; explicit new-firm accommodation; and recurring compliance burden. Currency figures are converted at about 35.7 baht, 4.55 ringgit and 57.7 pesos to the dollar, as approximations for comparison.

One author coded all rows and checked them against the texts. A separate instance of a generative AI model then coded all 29 instruments blind, from the codebook and texts alone. Agreement before adjudication was 69% on layer (Cohen's kappa 0.60), 83% on delivery (0.73) and 76% on accommodation (0.57), and 28 of 29 threshold figures matched. Disagreements were resolved against the text and are logged in Supplementary Table S6. An AI coder shares the first coder's blind spots, so a human check remains desirable. The Vietnamese texts were read through a commercial legal database, and the Thai originals, Vietnamese circulars and SIPP guidelines are unread.

### 3.2 The entry-barrier index

We group instruments into 11 entry routes, each the lowest-barrier way for a firm of a given kind to obtain support in a country and layer: software (Thailand), cloud services, GPU hosting and data centres (Thailand); the startup track and cloud-platform listing (Viet Nam); Malaysia Digital and DESAC (Malaysia); and software and hyperscaler, AI and data-science, and data-centre listings (the Philippines). Each route is scored from 0 (open) to 1 (restrictive) on four dimensions, using rules fixed in advance.

*Capital barrier (CB).* The base-10 logarithm of the capital threshold over US$0.28 million, the capital to host one eight-accelerator server, divided by three and bounded between 0 and 1. Capacity thresholds are converted to capital to host. Routes with no stated capital condition score 0.

*Compliance friction (CC).* The number of fixed-cost obligations among five (external certification; external audit at the firm's own cost; mandated certified or third-party location; annual report with inspection; application documentation and annual claim), capped at three and divided by three.

*Vintage barrier (VB).* 0 if the route has an explicit new-firm accommodation, 1 if eligibility presupposes prior revenue, and 0.5 otherwise.

*Delivery (DL).* 1 if support is indirect only, 0.5 if both indirect and direct, 0 if direct only.

The composite is the equal-weight mean. We report five alternative weightings, a version with the capital barrier measured against the viable fleet, and a simulation with random weights. The full scoring is in Supplementary Table S7 and the code is in the replication files.

### 3.3 The viability benchmark

To test A1, we compute the break-even utilisation of a provider of eight-GPU H100 servers. Server capital is US$250,000 to US$320,000, the price runs from US$1.70 to US$3.85 per GPU-hour (the one-year contract index to the on-demand list price of specialist clouds), colocation costs US$200 to US$475 per kW a month, metered power US$0.11 per kWh, and capital is charged as an annuity at 10% over three to five years. A scale provider has wholesale colocation, cheaper hardware and capital at 8%. Provider overhead of US$50,000 to US$300,000 a year is varied because it is not observed. All market inputs come from vendor, reseller and trade sources and are indicative.

### 3.4 Outcome data

We use three sources. First, official BOI statistics for January to December 2025: for the software activity (8.1.1), 96 approved projects with THB 933.0 million of investment, for data centres (8.2.1), 24 projects with THB 457,999.8 million, and for data hosting (8.2.4), one project with THB 126,793.0 million, with the Thai-held share of registered capital in each (BOI, 2026b). Second, the Epoch AI dataset of GPU clusters, from which we take the clusters in the four economies with owner, size and date (Epoch AI, 2025). Third, 62 project records for the four economies, collected from public sources on 26 October 2026, each with a source and quotation. They are indicative: owner nationality is stated for only 26 of the 62, almost all are large data centres, and many primary sources could not be accessed. We use them only for project size against stated thresholds, not for domestic shares.

## 4. Results

### 4.1 Four incentive architectures

The four systems differ in how they set eligibility (Table 1). Thailand sets capital and capacity conditions by activity: software needs THB 1.5 million a year of Thai IT salaries (about US$42,000); data centres need at least 2 MW of IT load; GPU-based data hosting needs THB 5,000 million of capital (about US$140 million); and cloud services carry no capital minimum but require location in two certified data centres and ISO/IEC 27001 and 20000-1 certification (BOI, 2026a). Malaysia runs two schemes: Malaysia Digital, which covers cloud and AI activities at RM50,000 of paid-up capital (about US$11,000) and requires an auditor-verified annual declaration at the firm's cost, and DESAC for data-centre and cloud operators, whose smallest recognised data-centre category is 0.85 MW and whose ten-year option needs RM1 billion of cumulative capital expenditure (Malaysia Digital Economy Corporation, 2025; Malaysian Investment Development Authority, 2024). Viet Nam lists strategic technologies and products in two unranked groups, with no capital rule; the benefits run through Decree 260, whose startup track gives direct support and whose strategic-technology enterprise criteria require 80% of revenue from listed products (Vietnam, 2026a, 2026b). The Philippines lists activities by tier, with software and hyperscalers and grid-reliant data centres in Tier I and AI services and own-power data centres in Tier III, states no size condition, and applies one firm-scale boundary of PHP 15 billion (about US$260 million) that routes projects to the Fiscal Incentives Review Board (Philippines, 2024; Philippines, Office of the President, 2026).

**Table 1: Four Incentive Architectures**

| Architecture | Country | Where the screen sits |
|---|---|---|
| Capital-gated activities | Thailand | Capacity (2 MW) and capital (US$140 million) at data-centre and GPU hosting; certification at cloud |
| Two parallel tracks | Malaysia | Audit cost (Malaysia Digital); categories from 0.85 MW and facility-oriented conditions (DESAC) |
| Strategic-technology list | Viet Nam | Designation and enterprise criteria, not capital |
| Activity tiers with a common boundary | Philippines | Listing and firm scale; for data centres, power source |

*Source:* Authors' compilation from the primary legal texts listed in Supplementary Table S2.

Across the coded instruments, no instrument is aimed at compute provision below facility scale. Where small cloud providers can enter on paper, in Thailand and Malaysia, the screen is a fixed compliance cost, certification in Thailand and audit in Malaysia.

### 4.2 The index

Table 2 gives the index. Entry barriers at the application layer are low everywhere (composite scores of 0.21 to 0.54). At the compute layers the lowest-barrier route scores 0.46 in Malaysia and Viet Nam and 0.54 in the Philippines and Thailand. The highest scores are for facility-scale routes: DESAC (0.69), Thai GPU hosting (0.68) and Thai data centres (0.64). The Philippine routes score alike (0.54) because the Philippine rules state no size condition and our dimensions do not capture the tier.

**Table 2: Entry-Barrier Index by Route**

| Route | Layer | Capital barrier | Compliance friction | Vintage barrier | Delivery | Composite |
|---|---|---|---|---|---|---|
| Thailand, software (8.1.1) | (i) | 0.00 | 0.00 | 0.5 | 1.0 | 0.38 |
| Thailand, cloud (8.2.2) | (ii) | 0.00 | 0.67 | 0.5 | 1.0 | 0.54 |
| Thailand, GPU hosting (8.2.4.1) | (ii) | 0.90 | 0.33 | 0.5 | 1.0 | 0.68 |
| Thailand, data centres (8.2.1) | (iii) | 0.72 | 0.33 | 0.5 | 1.0 | 0.64 |
| Viet Nam, startup track | (i) | 0.00 | 0.33 | 0.0 | 0.5 | 0.21 |
| Viet Nam, cloud platforms | (ii) | 0.00 | 0.33 | 1.0 | 0.5 | 0.46 |
| Malaysia, Malaysia Digital | (i)+(ii) | 0.00 | 0.33 | 0.5 | 1.0 | 0.46 |
| Malaysia, DESAC | (ii)+(iii) | 0.59 | 0.67 | 0.5 | 1.0 | 0.69 |
| Philippines, software and hyperscalers | (i)+(ii) | 0.00 | 0.67 | 0.5 | 1.0 | 0.54 |
| Philippines, AI and data science | (i) | 0.00 | 0.67 | 0.5 | 1.0 | 0.54 |
| Philippines, data centres | (iii) | 0.00 | 0.67 | 0.5 | 1.0 | 0.54 |

*Notes:* Scores run from 0 (open) to 1 (restrictive). The composite is the equal-weight mean. The capital barrier is the base-10 logarithm of the threshold over US$0.28 million, divided by three. *Source:* Authors' calculations from Supplementary Table S7.

The ranking is stable to the weighting. Rank correlations with the equal-weight ranking are 0.99 when capital counts double, 0.88 when delivery is dropped, 1.00 when friction counts double, and 0.77 for capital alone. Measuring capital against the viable fleet of Section 4.3 gives 0.70, because it removes most of the capital barrier of the facility routes. With random weights, Malaysia and Viet Nam each have the lowest compute-entry score in half of the draws, Thailand and the Philippines never, and Thailand's score is higher than at least one of Malaysia and Viet Nam in all draws.

The index does not discriminate well among the lowest-barrier routes, and its dimensions are scored by rules we set. We do not claim it as a final measure, only as a transparent one that others can recode.

### 4.3 Viability of small providers

The benchmark shows that a single server is not a viable provider, and that viability turns on price. At the contract-index price of about US$2.35 per GPU-hour, a small provider on leased colocation cannot break even at any utilisation below 100% in the central case (break-even 1.01). At US$3.00 it breaks even at 79% utilisation, and at the on-demand list price of US$3.85 at 62%. A scale provider breaks even at 56% and 43% at the same prices, about 20 percentage points lower, through cheaper colocation, capital and hardware.

The fleet needed to cover overhead depends on the same price. At US$3.00 and 80% utilisation, 45 to 270 servers (US$13 million to US$80 million of hardware) cover an overhead of US$50,000 to US$300,000 a year. At US$3.85 a few servers suffice, and at US$2.35 or below no fleet size does. Table 3 places each capital threshold against two baselines, one server and this viable fleet. Measured from one server, Thailand's GPU-hosting gate is 2.5 to 3.0 orders of magnitude away and its data-centre condition 1.7 to 2.8. Measured from the viable fleet of the central case, they are 0.2 to 1.0 and −0.6 to 0.8, so the facility-scale thresholds lie within or close to the viable range. A1 therefore holds only conditionally.

**Table 3: Capital Thresholds against Two Baselines**

| Threshold | Basis | US$ million | Orders from one server | Orders from viable fleet |
|---|---|---|---|---|
| Thailand, GPU hosting (8.2.4.1) | Minimum capital | 140 | 2.5 to 3.0 | 0.2 to 1.0 |
| Thailand, data centres (8.2.1) | 2 MW of IT load | 21 to 76 to host | 1.7 to 2.8 | −0.6 to 0.8 |
| Malaysia, DESAC smallest category | 0.85 MW | 9 to 32 to host | 1.3 to 2.4 | −0.9 to 0.4 |
| Malaysia, DESAC ten-year condition | Cumulative capital expenditure | 220 | 2.7 to 3.2 | 0.4 to 1.2 |
| Philippines, firm-scale boundary | Investment capital; routes to FIRB | 260 | 2.8 to 3.3 | 0.5 to 1.3 |
| Philippines, presidential package | Capital, or 10,000 jobs | 865 | 3.3 to 3.8 | 1.0 to 1.8 |

*Notes:* The one-server baseline is US$0.13 million to US$0.46 million. The viable-fleet baseline is US$13 million to US$80 million, at US$3.00 per GPU-hour. FIRB = Fiscal Incentives Review Board. Negative values mean the threshold lies inside the viable range. *Source:* Authors' calculations (Supplementary Table S5).


![**Figure 1: Eligibility Thresholds against Cost Benchmarks.** US$ million, log scale. Shaded bands show the capital to host the stated capacity, from construction cost (US$10.7 million per MW; Turner & Townsend, 2025) to fully equipped AI capacity (US$38 million per MW; Epoch AI, 2026). Thailand's software figure is annual salary spend (hollow marker); Malaysia's paid-up capital figures are company capital, not project scale; the 0.85 MW bar shows the capital to host the smallest DESAC category. Viet Nam states no capital threshold.](fig1_threshold_ladder.png)


### 4.4 The index against outcomes

**Thailand, by route.** Table 4 sets the index against BOI approvals for 2025. Mean project investment rises with the index across the four routes (rank correlation 1.00): THB 9.7 million for software, THB 3,250 million for cloud, THB 19,083 million for data centres and THB 126,793 million for the one data-hosting project. The Thai-held share of registered capital falls with the index (rank correlation −0.80): 46% for software, 15% for data centres and none for data hosting. The exception is the cloud route, where Siam AI, a Thai company and NVIDIA cloud partner, received BOI promotion for a THB 3.25 billion (about US$91 million) project in January 2025, classed as cloud services and not data hosting (BOI, 2025). Two of the four routes rest on one project each, and with four points no significance test is meaningful.

**Table 4: Index and Thai Approvals by Route, 2025**

| Route | Composite index | Projects | Mean investment (THB million) | Thai-held share of capital (%) |
|---|---|---|---|---|
| Software (8.1.1) | 0.38 | 96 | 9.7 | 46 |
| Cloud (8.2.2), Siam AI project only | 0.54 | 1 | 3,250 | 100 |
| Data centres (8.2.1) | 0.64 | 24 | 19,083 | 15 |
| Data hosting (8.2.4), one project | 0.68 | 1 | 126,793 | 0 |

*Source:* BOI (2025, 2026b); authors' calculations.

**GPU clusters.** The Epoch dataset lists five clusters in Thailand and one each in Viet Nam, Malaysia and the Philippines (Epoch AI, 2025). In Thailand, two private clusters of 1,024 H100 equivalents (128 servers, 1.46 MW), SIAM AI's and GreenNode's (owned by VNG of Viet Nam), began operation in 2024, and a public cluster of 222 H100 equivalents has run since 2022. Both private clusters are below the 2 MW data-centre condition and inside the viable range of Section 4.3, and neither had to meet the THB 5,000 million gate. In Viet Nam the only entry is a 2021 Vingroup cluster of 50 H100 equivalents. Malaysia and the Philippines have only Alibaba Cloud entries. The dataset covers large clusters only, so smaller providers are not represented.

**Project size against thresholds.** In public records, 18 Thai data-centre projects with a stated IT load range from 12 to 300 MW against the 2 MW minimum, three Malaysian projects from 120 to 256 MW against 0.85 MW, and six Vietnamese and six Philippine projects from 10 to 140 MW. None lies below a stated threshold, and none lies near it.

**Table 5: Predictions Fixed in Advance and Results**

| Prediction | Result |
|---|---|
| P1: project size rises with the capital barrier | Supported (rank correlation 1.00, four Thai routes) |
| P2: domestic share falls with the index | Partly supported (−0.80); the cloud route is an exception |
| P3: projects cluster at stated capacity thresholds | Not supported: projects start six or more times above the minima |
| P4: friction on low-capital routes limits domestic entry | Inconclusive: BOI approvals for cloud services not obtained |
| P5: rule-light systems do not guarantee domestic entry | Consistent: domestic private clusters are Thailand 2, Viet Nam 1, Malaysia 0, Philippines 0 |

*Source:* Authors' analysis (Supplementary Table S8).

## 5. Discussion

The evidence supports four readings. First, cost shapes thresholds at facility scale. Capital to host the stated capacities is large (US$21 million to US$76 million for 2 MW) and the projects that appear in public records are far larger, so capacity thresholds are not binding on them. This favours H1 as the explanation of why gates sit near facility scale, and it is the opposite of the design reading for those thresholds.

Second, what matters for smaller domestic providers is not the capital gate but the fixed cost of compliance and, in Viet Nam, reliance on revenue history. The Thai cloud route has no capital minimum and has admitted Thai-owned clusters of about 1 MW, but its certification and location conditions are the screen, and it is the route with the highest compliance friction (0.67) of the Thai low-capital routes. This is the pattern H2 predicts through fixed costs, and it is consistent with the finding of Bahar et al. (2026) that instruments that presuppose profit or scale favour larger firms, through a different channel.

Third, the viability benchmark limits the claim that rungs are missing. If viable providers sell near the on-demand price, a few servers suffice and the facility thresholds are a long way above viable scale. If prices are nearer US$3.00, the viable fleet is 45 to 270 servers and the thresholds are close to it. We cannot choose between these cases without data on the prices small regional providers obtain.

Fourth, a rule-light system does not produce more domestic entry. Viet Nam and the Philippines state no capital rule at the compute layers, yet their outcome records show no more domestic AI clusters than Thailand. Their screens lie in listing, designation and discretion, which our legal coding records but our outcome data cannot observe.

The economic implication is limited and conditional. If learning by operating matters, a route that admits domestic providers at about 1 MW, as the Thai cloud route does, supplies the entry that the self-discovery argument requires, and the thresholds at facility scale matter less than the fixed costs on that route. If viable scale is instead at or above facility scale, because prices fall toward contract levels, the case for a sub-facility route weakens. Our evidence cannot say which holds, nor whether domestic entry raises productivity, which needs firm-level data on output, prices and AI adoption.

The linkage has strong limits. There are four countries and 11 routes, two of the Thai route outcomes rest on one project each, and the project records have partial ownership information and cover large projects. The index dimensions are coded by rules we set, and the second coder is an AI. The comparison is a consistency check against predictions, not a test of causal effects, and a firm-level study with data on applications and rejections would be the natural next step.

For policy, three implications follow. Because capital gates sit near the scale at which projects occur, lowering them is unlikely to change entry by itself. A better target is the fixed compliance cost that falls on low-capital routes: certification, audit and mandated location. Governments could also publish approvals by activity, firm size and owner nationality, as only Thailand does, so that the link between rules and entry can be studied. Third, where a government wants domestic providers at the 1 MW scale, the Thai experience suggests that a route without a capital gate works, but its fixed costs should be proportionate to firm size. Because host countries compete for the same investors, any one country that lowers a threshold also lowers it for foreign entrants, so pilots with published take-up data should come before wider change.

## 6. Conclusion

We built a transparent index of entry barriers in AI investment incentives for four Southeast Asian economies and checked it against outcome evidence, using predictions fixed in advance. Barriers at facility scale are high only in Thailand and Malaysia, and no system targets providers below that scale. In Thailand, project size rises and the Thai-held share falls with the index, except on the cloud route, where Thai-owned clusters of about 1 MW operate without a capital gate. Capacity thresholds are not where projects cluster, which favours cost as the explanation of why they sit at facility scale, and the screen that matters for smaller domestic providers is fixed compliance cost. These results are small-sample and descriptive. Their value is a measurable index and a set of pre-stated predictions that larger data can test.

## Data availability

The instrument-level coding, index scoring, viability model, analysis code and collected project records are provided as supplementary material and replication files.

## References

Bahar, D., Gadgin Matha, S., Hausmann, R., & Segovia, S. (2026). *Japan's innovation challenge: Escaping the middle-technology trap* (Growth Lab Working Paper No. 269). Harvard University.

Bloom, N., Griffith, R., & Van Reenen, J. (2002). Do R&D tax credits work? Evidence from a panel of countries 1979-1997. *Journal of Public Economics, 85*(1), 1-31. https://doi.org/10.1016/S0047-2727(01)00086-X

Board of Investment of Thailand. (2025, January 29). *Thailand BOI approves investments worth a total of US$5 billion, including TikTok's data hosting project*. https://osos.boi.go.th/EN/news/2163

Board of Investment of Thailand. (2026a). *Investment promotion guide 2026*. Office of the Board of Investment.

Board of Investment of Thailand. (2026b). *Investment promotion statistics: Approvals by sub-activity, January to December 2025*. Investment Services Center.

Cerutti, E., Garcia Pascual, A. I., Kido, Y., Li, L., Melina, G., Mendes Tavares, M., & Wingender, P. (2025). *The global impact of AI: Mind the gap* (IMF Working Paper No. 25/76). International Monetary Fund.

Eichengreen, B., Park, D., & Shin, K. (2014). Growth slowdowns redux: New evidence on the middle-income trap. *Japan and the World Economy, 32*, 65-84. https://doi.org/10.1016/j.japwor.2014.07.003

Epoch AI. (2025). *GPU clusters* [Dataset]. https://epoch.ai/data/gpu-clusters

Epoch AI. (2026). *Total cost of ownership of a one-gigawatt AI data center*. https://epoch.ai/data-insights/ai-datacenter-cost-breakdown

Hausmann, R., & Rodrik, D. (2003). Economic development as self-discovery. *Journal of Development Economics, 72*(2), 603-633. https://doi.org/10.1016/S0304-3878(03)00124-X

Imam, P. A., & Temple, J. R. W. (2026). At the threshold: The increasing relevance of the middle-income trap. *Scandinavian Journal of Economics*. https://doi.org/10.1111/sjoe.70036

Ke, Y. (2024). ASEAN Four's middle income trap dilemma: Evidence of the middle technology trap. *Asian Review of Political Economy, 3*(1), 1-29. https://doi.org/10.1007/s44216-024-00033-5

Lehdonvirta, V., Wú, B., & Hawkins, Z. (2024). Compute North vs. Compute South: The uneven possibilities of compute-based AI governance around the globe. *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, 7*(1).

Malaysia Digital Economy Corporation. (2025). *Guidelines on Malaysia Digital (MD) tax incentive (new investment incentive)* (revised 22 July 2025). MDEC.

Malaysian Investment Development Authority. (2024). *Guidelines and procedures for the application of the Digital Ecosystem Acceleration (DESAC) scheme*. MIDA.

Philippines, Office of the President. (2026). *Memorandum Order No. 47: Approving the 2026 Strategic Investment Priority Plan*. Malacañang.

Philippines. (2024). *Republic Act No. 12066: Corporate Recovery and Tax Incentives for Enterprises to Maximize Opportunities for Reinvigorating the Economy (CREATE MORE) Act*. Congress of the Philippines.

Turner & Townsend. (2025). *Data centre construction cost index 2025-2026*. Turner & Townsend.

Viet Nam. (2026a). *Decree No. 260/2026/ND-CP detailing the implementation of the Law on High Technology*. Government of Viet Nam.

Viet Nam. (2026b). *Decision No. 21/2026/QD-TTg promulgating the list of strategic technologies and strategic technology products*. Prime Minister of Viet Nam.
