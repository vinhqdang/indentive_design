---
title: "Entry Barriers in AI Investment Incentives: An Index and Evidence from Four Southeast Asian Economies"
---

## Abstract

Governments in Southeast Asia use investment incentives to attract artificial intelligence (AI) infrastructure, but we do not know whether the rules shape who enters. We code 29 instruments in Malaysia, the Philippines, Thailand and Viet Nam and build a transparent index of entry barriers for 11 routes. We check it against Thai approval statistics, GPU cluster records, UNCTAD investment data and project records, using predictions fixed beforehand. Project size rises with the index in Thailand, domestic GPU clusters appear on the low-capital cloud route at about 1 MW, and countries with lower entry barriers attract more digital investment. Barriers at facility scale do not predict data-centre investment: Malaysia has the highest and the most. The evidence is small-sample and descriptive.

**Keywords:** entry barriers; incentive design; investment incentives; artificial intelligence; data centres; Southeast Asia

**JEL codes:** F21, F23, H25, L52, O25

## 1. Introduction

Whether domestic firms can build AI computing capacity, and not only buy it, matters for economies that want to move from middle to high income. If they can only adopt what foreign providers supply, more of the gains from AI are likely to accrue elsewhere (Cerutti et al., 2025). Building capacity depends on what investment incentive systems let in, because incentives are the main tool host governments use to attract investors and they write the eligibility rules. Yet we know little about those rules for AI. Studies describe aggregate spending, access scenarios and the geography of compute (Lehdonvirta et al., 2024). We found no systematic, measurable account of how incentive rules treat firms of different scale and age across the layers of the AI stack, or of whether such rules relate to who actually enters.

This paper makes that comparison for Malaysia, the Philippines, Thailand and Viet Nam. It does three things. First, it codes 29 instruments from primary legal texts and turns the codes into a transparent index of entry barriers for 11 entry routes. Second, it tests a viability assumption: whether a small provider of AI computing can survive at all, because a barrier only matters if entry at that scale would otherwise be viable. Third, it checks the index against outcome evidence, using five predictions that we recorded before analysing the outcome data: official Thai approval statistics by activity, a public dataset of GPU clusters, and 62 project records collected from public sources. It adds two exploratory country-level checks against UNCTAD's investment data.

We find that barriers at facility scale are high only in Thailand and Malaysia, where capital or capacity gates lie two to three orders of magnitude above the capital to host one server, and that no system aims an instrument at providers below facility scale. In Thailand, mean project size rises with the index and the Thai-held share of capital falls with it, with one exception, the cloud route, where Thai-owned GPU clusters of about 1 MW operate without meeting any capital gate. Stated capacity thresholds are not where projects cluster: approved data-centre projects are 10 to 300 MW, six or more times the stated minima. Across countries, those with lower entry-route barriers attract more announced digital investment, but barriers at the data-centre route do not predict data-centre investment: Malaysia has the highest barrier and the most investment. We read this as evidence that cost, not only design, shapes thresholds at facility scale, and that the screen that matters for smaller domestic providers is fixed compliance cost and reliance on revenue history. The evidence is a small-sample, descriptive linkage and does not identify causal effects.

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

We fixed five directional predictions before analysing the outcome data, and committed them to the project repository on 26 October 2026. **P1:** within a country, mean project investment is higher in routes with a higher capital barrier. **P2:** the domestic share of capital or projects is lower in routes with a higher composite index. **P3:** where a capacity threshold is stated, projects cluster at or just above it, and none lie below. **P4:** routes with no capital barrier but fixed compliance costs attract fewer domestic entrants than the lowest-friction route in the same country. **P5:** systems with no stated capital rule at the compute layers do not show a systematically higher domestic share than systems with one. Results that run against a prediction count against the index as an explanation of entry. After reading UNCTAD's country data we added two exploratory predictions, labelled as such: **P6a**, countries whose lowest-barrier compute route has a lower score attract more digital greenfield investment; **P6b**, countries whose data-centre route has a higher score attract less data-centre investment.

## 3. Data and methods

### 3.1 Instruments, coding and reliability

We code primary legal texts, not strategy documents: Thailand's Board of Investment (BOI) Investment Promotion Guide 2026 and announcements; Viet Nam's Decree 260/2026 and Decision 21/2026; Malaysia's Malaysia Digital and Digital Ecosystem Acceleration (DESAC) guidelines; and the Philippines' CREATE MORE Act, its implementing rules and the 2026 Strategic Investment Priority Plan (SIPP). The unit of analysis is the instrument. Twenty-nine instruments are coded (Supplementary Table S1) on five dimensions: layer; delivery (indirect, tax-based support that presupposes taxable profit, or direct grants, equity and fee waivers); threshold and its basis; explicit new-firm accommodation; and recurring compliance burden. Currency figures are converted at about 35.7 baht, 4.55 ringgit and 57.7 pesos to the dollar, as approximations for comparison.

One author coded all rows and checked them against the texts. A separate instance of a generative AI model then coded all 29 instruments blind, from the codebook and texts alone. Agreement before adjudication was 69% on layer (Cohen's kappa 0.60), 83% on delivery (0.73) and 76% on accommodation (0.57), and 28 of 29 threshold figures matched. Disagreements were resolved against the text and are logged in Supplementary Table S6. An AI coder shares the first coder's blind spots, so a human check remains desirable. The Vietnamese texts were read through a commercial legal database, and the Thai originals, Vietnamese circulars and SIPP guidelines are unread.

### 3.2 The entry-barrier index

We group instruments into 11 entry routes, each the lowest-barrier way for a firm of a given kind to obtain support in a country and layer: software (Thailand), cloud services, GPU hosting and data centres (Thailand); the startup track and cloud-platform listing (Viet Nam); Malaysia Digital and DESAC (Malaysia); and software and hyperscaler, AI and data-science, and data-centre listings (the Philippines). Each route is scored from 0 (open) to 1 (restrictive) on four dimensions, using rules fixed in advance.

*Capital barrier (CB).* The base-10 logarithm of the capital threshold over \$0.28 million, the capital to host one eight-accelerator server, divided by three and bounded between 0 and 1. Capacity thresholds are converted to capital to host, at \$10.7 million per megawatt of construction (Turner & Townsend, 2025) to \$38 million per megawatt of fully equipped AI capacity.[^1] Routes with no stated capital condition score 0.

*Compliance friction (CC).* The number of fixed-cost obligations among five (external certification; external audit at the firm's own cost; mandated certified or third-party location; annual report with inspection; application documentation and annual claim), capped at three and divided by three.

*Vintage barrier (VB).* 0 if the route has an explicit new-firm accommodation, 1 if eligibility presupposes prior revenue, and 0.5 otherwise.

*Delivery (DL).* 1 if support is indirect only, 0.5 if both indirect and direct, 0 if direct only.

The composite is the equal-weight mean. We report five alternative weightings, a version with the capital barrier measured against the viable fleet, and a simulation with random weights. The full scoring is in Supplementary Table S7 and the code is in the replication files.

### 3.3 The viability benchmark

To test A1, we compute the break-even utilization of a provider of eight-GPU H100 servers. Server capital is \$250,000 to \$320,000, the price runs from \$1.70 to \$3.85 per GPU-hour (the one-year contract index to the on-demand list price of specialist clouds), colocation costs \$200 to \$475 per kW a month, metered power \$0.11 per kWh, and capital is charged as an annuity at 10% over three to five years. A scale provider has wholesale colocation, cheaper hardware and capital at 8%. Provider overhead of \$50,000 to \$300,000 a year is varied because it is not observed. All market inputs come from vendor, reseller and trade sources and are indicative.

### 3.4 Outcome data

We use three sources. First, official BOI statistics for January to December 2025: for the software activity (8.1.1), 96 approved projects with THB 933.0 million of investment, for data centres (8.2.1), 24 projects with THB 457,999.8 million, and for data hosting (8.2.4), one project with THB 126,793.0 million, with the Thai-held share of registered capital in each (Board of Investment of Thailand, 2026b). Second, the Epoch AI dataset of GPU clusters, from which we take the clusters in the four economies with owner, size and date.[^2] Third, 62 project records for the four economies, collected from public sources on 26 October 2026, each with a source and quotation. They are indicative: owner nationality is stated for only 26 of the 62, almost all are large data centres, and many primary sources could not be accessed. We use them only for project size against stated thresholds, not for domestic shares. Fourth, for the exploratory country-level checks, UNCTAD's World Investment Report 2025, which reports announced greenfield projects from fDi Markets for 2020 to 2024: digital-economy projects by host economy (Malaysia \$74 billion, Viet Nam \$32 billion, Thailand \$16 billion, with the Philippines outside the top ten) and data-centre projects of sovereign wealth funds (Malaysia 44 projects and \$2,153 million, the Philippines 4 and \$763 million, Thailand 1 and \$266 million, Viet Nam 1 and \$191 million) (UNCTAD, 2025). The 2026 report gives 2025 growth of FDI inflows (Malaysia +51%, Thailand +30%, Viet Nam +1%) (UNCTAD, 2026).

## 4. Results

### 4.1 Four incentive architectures

The four systems differ in how they set eligibility (Table 1). Thailand sets capital and capacity conditions by activity: software needs THB 1.5 million a year of Thai IT salaries (about \$42,000); data centres need at least 2 MW of IT load; GPU-based data hosting needs THB 5,000 million of capital (about \$140 million); and cloud services carry no capital minimum but require location in two certified data centres and ISO/IEC 27001 and 20000-1 certification (Board of Investment of Thailand, 2026a). Malaysia runs two schemes: Malaysia Digital, which covers cloud and AI activities at RM50,000 of paid-up capital (about \$11,000) and requires an auditor-verified annual declaration at the firm's cost, and DESAC for data-centre and cloud operators, whose smallest recognized data-centre category is 0.85 MW and whose ten-year option needs RM1 billion of cumulative capital expenditure (Malaysia Digital Economy Corporation, 2025; Malaysian Investment Development Authority, 2024). Viet Nam lists strategic technologies and products in two unranked groups, with no capital rule; the benefits run through Decree 260, whose startup track gives direct support and whose strategic-technology enterprise criteria require 80% of revenue from listed products (Vietnam, 2026a, 2026b). The Philippines lists activities by tier, with software and hyperscalers and grid-reliant data centres in Tier I and AI services and own-power data centres in Tier III, states no size condition, and applies one firm-scale boundary of PHP 15 billion (about \$260 million) that routes projects to the Fiscal Incentives Review Board (Philippines, 2024; Philippines, Office of the President, 2026).

*[Put table 1 here]*

Across the coded instruments, no instrument is aimed at compute provision below facility scale. Where small cloud providers can enter on paper, in Thailand and Malaysia, the screen is a fixed compliance cost, certification in Thailand and audit in Malaysia.

### 4.2 The index

Table 2 gives the index. Entry barriers at the application layer are low everywhere (composite scores of 0.21 to 0.54). At the compute layers the lowest-barrier route scores 0.46 in Malaysia and Viet Nam and 0.54 in the Philippines and Thailand. The highest scores are for facility-scale routes: DESAC (0.69), Thai GPU hosting (0.68) and Thai data centres (0.64). The Philippine routes score alike (0.54) because the Philippine rules state no size condition and our dimensions do not capture the tier.

*[Put table 2 here]*

The ranking is stable to the weighting. Rank correlations with the equal-weight ranking are 0.99 when capital counts double, 0.88 when delivery is dropped, 1.00 when friction counts double, and 0.77 for capital alone. Measuring capital against the viable fleet of Section 4.3 gives 0.70, because it removes most of the capital barrier of the facility routes. With random weights, Malaysia and Viet Nam each have the lowest compute-entry score in half of the draws, Thailand and the Philippines never, and Thailand's score is higher than at least one of Malaysia and Viet Nam in all draws.

The index does not discriminate well among the lowest-barrier routes, and its dimensions are scored by rules we set. We do not claim it as a final measure, only as a transparent one that others can recode.

### 4.3 Viability of small providers

The benchmark shows that a single server is not a viable provider, and that viability turns on price. At the contract-index price of about \$2.35 per GPU-hour, a small provider on leased colocation cannot break even at any utilization below 100% in the central case (break-even 1.01). At \$3.00 it breaks even at 79% utilization, and at the on-demand list price of \$3.85 at 62%. A scale provider breaks even at 56% and 43% at the same prices, about 20 percentage points lower, through cheaper colocation, capital and hardware.

The fleet needed to cover overhead depends on the same price. At \$3.00 and 80% utilization, 45 to 270 servers (\$13 million to \$80 million of hardware) cover an overhead of \$50,000 to \$300,000 a year. At \$3.85 a few servers suffice, and at \$2.35 or below no fleet size does. Table 3 places each capital threshold against two baselines, one server and this viable fleet. Measured from one server, Thailand's GPU-hosting gate is 2.5 to 3.0 orders of magnitude away and its data-centre condition 1.7 to 2.8. Measured from the viable fleet of the central case, they are 0.2 to 1.0 and −0.6 to 0.8, so the facility-scale thresholds lie within or close to the viable range. A1 therefore holds only conditionally.

*[Put table 3 here]*


*[Put figure 1 here]*


### 4.4 The index against outcomes

**Thailand, by route.** Table 4 sets the index against BOI approvals for 2025. Mean project investment rises with the index across the four routes (rank correlation 1.00): THB 9.7 million for software, THB 3,250 million for cloud, THB 19,083 million for data centres and THB 126,793 million for the one data-hosting project. The Thai-held share of registered capital falls with the index (rank correlation −0.80): 46% for software, 15% for data centres and none for data hosting. The exception is the cloud route, where Siam AI, a Thai company and NVIDIA cloud partner, received BOI promotion for a THB 3.25 billion (about \$91 million) project in January 2025, classed as cloud services and not data hosting.[^3] Two of the four routes rest on one project each, and with four points no significance test is meaningful.

*[Put table 4 here]*

**GPU clusters.** The Epoch dataset lists five clusters in Thailand and one each in Viet Nam, Malaysia and the Philippines In Thailand, two private clusters of 1,024 H100 equivalents (128 servers, 1.46 MW), SIAM AI's and GreenNode's (owned by VNG of Viet Nam), began operation in 2024, and a public cluster of 222 H100 equivalents has run since 2022. Both private clusters are below the 2 MW data-centre condition and inside the viable range of Section 4.3, and neither had to meet the THB 5,000 million gate. In Viet Nam the only entry is a 2021 Vingroup cluster of 50 H100 equivalents. Malaysia and the Philippines have only Alibaba Cloud entries. The dataset covers large clusters only, so smaller providers are not represented.

**Project size against thresholds.** In public records, 18 Thai data-centre projects with a stated IT load range from 12 to 300 MW against the 2 MW minimum, three Malaysian projects from 120 to 256 MW against 0.85 MW, and six Vietnamese and six Philippine projects from 10 to 140 MW. None lies below a stated threshold, and none lies near it.

*[Put table 5 here]*

**Country level (exploratory).** Table 6 sets the entry-route and data-centre route scores against UNCTAD's country figures. Malaysia and Viet Nam, with the lowest entry-route scores (0.46), attracted the most announced digital greenfield investment from 2020 to 2024 (\$74 billion and \$32 billion), Thailand (0.54) \$16 billion, and the Philippines (0.54) less than that. The rank correlation of the entry score with the value is −0.89, as P6a predicts. The data-centre route does not follow: Malaysia has the highest data-centre route score (0.69) and the largest sovereign-fund data-centre investment (44 projects, \$2,153 million), against 4 projects in the Philippines (score 0.54) and 1 in Thailand (0.64), a rank correlation of +0.50 that runs against P6b. In 2025 FDI inflows rose by 51% in Malaysia, 30% in Thailand and 1% in Viet Nam (UNCTAD, 2026). With four countries, these are descriptions, and market size, power supply and location, such as Johor's position next to Singapore, are obvious alternative explanations.

*[Put table 6 here]*

## 5. Discussion

The evidence supports five readings. First, cost shapes thresholds at facility scale. Capital to host the stated capacities is large (\$21 million to \$76 million for 2 MW) and the projects that appear in public records are far larger, so capacity thresholds are not binding on them. This favours H1 as the explanation of why gates sit near facility scale, and it is the opposite of the design reading for those thresholds.

Second, what matters for smaller domestic providers is not the capital gate but the fixed cost of compliance and, in Viet Nam, reliance on revenue history. The Thai cloud route has no capital minimum and has admitted Thai-owned clusters of about 1 MW, but its certification and location conditions are the screen, and it is the route with the highest compliance friction (0.67) of the Thai low-capital routes. This is the pattern H2 predicts through fixed costs, and it is consistent with the finding of Bahar et al. (2026) that instruments that presuppose profit or scale favour larger firms, through a different channel.

Third, the viability benchmark limits the claim that rungs are missing. If viable providers sell near the on-demand price, a few servers suffice and the facility thresholds are a long way above viable scale. If prices are nearer \$3.00, the viable fleet is 45 to 270 servers and the thresholds are close to it. We cannot choose between these cases without data on the prices small regional providers obtain.

Fourth, for the hyperscale foreign investors that dominate data-centre investment, incentive barriers appear to matter little: Malaysia combines the highest data-centre route barrier with the largest data-centre investment, so power, market and location probably dominate. The index aligns with investment only at the entry route, where smaller and domestic firms operate. Fifth, a rule-light system does not produce more domestic entry. Viet Nam and the Philippines state no capital rule at the compute layers, yet their outcome records show no more domestic AI clusters than Thailand. Their screens lie in listing, designation and discretion, which our legal coding records but our outcome data cannot observe.

The economic implication is limited and conditional. If learning by operating matters, a route that admits domestic providers at about 1 MW, as the Thai cloud route does, supplies the entry that the self-discovery argument requires, and the thresholds at facility scale matter less than the fixed costs on that route. If viable scale is instead at or above facility scale, because prices fall toward contract levels, the case for a sub-facility route weakens. Our evidence cannot say which holds, nor whether domestic entry raises productivity, which needs firm-level data on output, prices and AI adoption.

The linkage has strong limits. There are four countries and 11 routes, two of the Thai route outcomes rest on one project each, and the project records have partial ownership information and cover large projects. The index dimensions are coded by rules we set, and the second coder is an AI. The comparison is a consistency check against predictions, not a test of causal effects, and a firm-level study with data on applications and rejections would be the natural next step.

For policy, three implications follow. Because capital gates sit near the scale at which projects occur, lowering them is unlikely to change entry by itself. A better target is the fixed compliance cost that falls on low-capital routes: certification, audit and mandated location. Governments could also publish approvals by activity, firm size and owner nationality, as only Thailand does, so that the link between rules and entry can be studied. Third, where a government wants domestic providers at the 1 MW scale, the Thai experience suggests that a route without a capital gate works, but its fixed costs should be proportionate to firm size. Because host countries compete for the same investors, any one country that lowers a threshold also lowers it for foreign entrants, so pilots with published take-up data should come before wider change.

## 6. Conclusion

We built a transparent index of entry barriers in AI investment incentives for four Southeast Asian economies and checked it against outcome evidence, using predictions fixed in advance. Barriers at facility scale are high only in Thailand and Malaysia, and no system targets providers below that scale. In Thailand, project size rises and the Thai-held share falls with the index, except on the cloud route, where Thai-owned clusters of about 1 MW operate without a capital gate. Capacity thresholds are not where projects cluster, which favours cost as the explanation of why they sit at facility scale, and the screen that matters for smaller domestic providers is fixed compliance cost. At the country level, lower entry-route barriers go with more digital investment, but data-centre route barriers do not predict data-centre investment. These results are small-sample and descriptive. Their value is a measurable index and a set of pre-stated predictions that larger data can test.

## Data availability

The instrument-level coding, index scoring, viability model, analysis code and collected project records are provided as supplementary material and replication files.

[^3]: Board of Investment of Thailand (2025). Thailand BOI approves investments worth a total of \$5 billion, including TikTok's data hosting project. 29 January 2025. Available at https://osos.boi.go.th/EN/news/2163 (accessed October 2026).

[^2]: Epoch AI (2025). GPU clusters [dataset]. Available at https://epoch.ai/data/gpu-clusters (accessed October 2026).

[^1]: Epoch AI (2026). Total cost of ownership of a one-gigawatt AI data center. Available at https://epoch.ai/data-insights/ai-datacenter-cost-breakdown (accessed October 2026).

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

## References

Bahar D, Gadgin Matha S, Hausmann R and Segovia S (2026). Japan's innovation challenge: Escaping the middle-technology trap. Growth Lab Working Paper No. 269. Harvard University.

Bloom N, Griffith R and Van Reenen J (2002). Do R&D tax credits work? Evidence from a panel of countries 1979–1997. *Journal of Public Economics*. 85(1): 1–31.

Board of Investment of Thailand (2026a). *Investment Promotion Guide 2026*. Bangkok. Office of the Board of Investment.

Board of Investment of Thailand (2026b). Investment promotion statistics: Approvals by sub-activity, January to December 2025. Bangkok. Investment Services Center.

Cerutti E, Garcia Pascual AI, Kido Y, Li L, Melina G, Mendes Tavares M and Wingender P (2025). The global impact of AI: Mind the gap. IMF Working Paper No. 25/76. International Monetary Fund.

Eichengreen B, Park D and Shin K (2014). Growth slowdowns redux: New evidence on the middle-income trap. *Japan and the World Economy*. 32: 65–84.

Hausmann R and Rodrik D (2003). Economic development as self-discovery. *Journal of Development Economics*. 72(2): 603–633.

Imam PA and Temple JRW (2026). At the threshold: The increasing relevance of the middle-income trap. *Scandinavian Journal of Economics*. Online first, doi: 10.1111/sjoe.70036.

Ke Y (2024). ASEAN Four's middle income trap dilemma: Evidence of the middle technology trap. *Asian Review of Political Economy*. 3(1): 1–29.

Lehdonvirta V, Wú B and Hawkins Z (2024). Compute North vs. Compute South: The uneven possibilities of compute-based AI governance around the globe. *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society*. 7(1).

Malaysia Digital Economy Corporation (2025). Guidelines on Malaysia Digital (MD) tax incentive (new investment incentive), revised 22 July 2025. Kuala Lumpur.

Malaysian Investment Development Authority (2024). Guidelines and procedures for the application of the Digital Ecosystem Acceleration (DESAC) scheme. Kuala Lumpur.

Philippines (2024). Republic Act No. 12066: Corporate Recovery and Tax Incentives for Enterprises to Maximize Opportunities for Reinvigorating the Economy (CREATE MORE) Act. Congress of the Philippines.

Philippines, Office of the President (2026). Memorandum Order No. 47: Approving the 2026 Strategic Investment Priority Plan. Manila.

Turner & Townsend (2025). Data centre construction cost index 2025–2026. London.

UNCTAD (2025). *World Investment Report 2025: International Investment in the Digital Economy*. United Nations publication. Geneva.

UNCTAD (2026). *World Investment Report 2026: International Investment in a Turbulent Era*. United Nations publication. Geneva.

Viet Nam (2026a). Decree No. 260/2026/ND-CP detailing the implementation of the Law on High Technology. Government of Viet Nam.

Viet Nam (2026b). Decision No. 21/2026/QD-TTg promulgating the list of strategic technologies and strategic technology products. Prime Minister of Viet Nam.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

**Table 1: Four incentive architectures, 2026**

| Architecture | Country | Where the screen sits |
|---|---|---|
| Capital-gated activities | Thailand | Capacity (2 MW) and capital (\$140 million) at data-centre and GPU hosting; certification at cloud |
| Two parallel tracks | Malaysia | Audit cost (Malaysia Digital); categories from 0.85 MW and facility-oriented conditions (DESAC) |
| Strategic-technology list | Viet Nam | Designation and enterprise criteria, not capital |
| Activity tiers with a common boundary | Philippines | Listing and firm scale; for data centres, power source |

*Source:* Authors' compilation from the primary legal texts listed in Supplementary Table S2.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

**Table 2: Entry-barrier index by route, 2026**

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

*Notes:* Scores run from 0 (open) to 1 (restrictive). The composite is the equal-weight mean. The capital barrier is the base-10 logarithm of the threshold over \$0.28 million, divided by three. *Source:* Authors' calculations from Supplementary Table S7.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

**Table 3: Capital thresholds against two baselines, 2026**

| Threshold | Basis | \$ million | Orders from one server | Orders from viable fleet |
|---|---|---|---|---|
| Thailand, GPU hosting (8.2.4.1) | Minimum capital | 140 | 2.5 to 3.0 | 0.2 to 1.0 |
| Thailand, data centres (8.2.1) | 2 MW of IT load | 21 to 76 to host | 1.7 to 2.8 | −0.6 to 0.8 |
| Malaysia, DESAC smallest category | 0.85 MW | 9 to 32 to host | 1.3 to 2.4 | −0.9 to 0.4 |
| Malaysia, DESAC ten-year condition | Cumulative capital expenditure | 220 | 2.7 to 3.2 | 0.4 to 1.2 |
| Philippines, firm-scale boundary | Investment capital; routes to FIRB | 260 | 2.8 to 3.3 | 0.5 to 1.3 |
| Philippines, presidential package | Capital, or 10,000 jobs | 865 | 3.3 to 3.8 | 1.0 to 1.8 |

*Notes:* The one-server baseline is \$0.13 million to \$0.46 million. The viable-fleet baseline is \$13 million to \$80 million, at \$3.00 per GPU-hour. FIRB = Fiscal Incentives Review Board. Negative values mean the threshold lies inside the viable range. *Source:* Authors' calculations (Supplementary Table S5).

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

**Table 4: Index and Thai approvals by route, 2025**

| Route | Composite index | Projects | Mean investment (THB million) | Thai-held share of capital (%) |
|---|---|---|---|---|
| Software (8.1.1) | 0.38 | 96 | 9.7 | 46 |
| Cloud (8.2.2), Siam AI project only | 0.54 | 1 | 3,250 | 100 |
| Data centres (8.2.1) | 0.64 | 24 | 19,083 | 15 |
| Data hosting (8.2.4), one project | 0.68 | 1 | 126,793 | 0 |

*Source:* Board of Investment of Thailand (2026b), and footnote 3 for the cloud project; authors' calculations.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

**Table 5: Predictions fixed in advance and results, 2025–2026**

| Prediction | Result |
|---|---|
| P1: project size rises with the capital barrier | Supported (rank correlation 1.00, four Thai routes) |
| P2: domestic share falls with the index | Partly supported (−0.80); the cloud route is an exception |
| P3: projects cluster at stated capacity thresholds | Not supported: projects start six or more times above the minima |
| P4: friction on low-capital routes limits domestic entry | Inconclusive: BOI approvals for cloud services not obtained |
| P5: rule-light systems do not guarantee domestic entry | Consistent: domestic private clusters are Thailand 2, Viet Nam 1, Malaysia 0, Philippines 0 |
| P6a (exploratory): lower entry barrier, more digital investment | Consistent (rank correlation −0.89, four countries) |
| P6b (exploratory): higher data-centre barrier, less data-centre investment | Not supported (+0.50, three countries) |

*Source:* Authors' analysis (Supplementary Table S8).

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

**Table 6: Index and country-level investment, 2020–2024 (exploratory)**

| Country | Entry-route score | Data-centre route score | Digital greenfield announced, 2020–2024 (\$ billion) | Sovereign-fund data-centre projects, 2020–2024 (number; \$ million) |
|---|---|---|---|---|
| Malaysia | 0.46 | 0.69 | 74 | 44; 2,153 |
| Philippines | 0.54 | 0.54 | below 16 | 4; 763 |
| Thailand | 0.54 | 0.64 | 16 | 1; 266 |
| Viet Nam | 0.46 | none | 32 | 1; 191 |

*Notes:* Scores from Table 2 (lowest composite among compute routes; data-centre route). The Philippines is outside the top ten developing economies for digital greenfield value, so its value is below Thailand's. Sovereign-fund projects are a small part of data-centre investment. *Source:* UNCTAD (2025), based on fDi Markets; authors' calculations.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

![**Figure 1: Eligibility thresholds against cost benchmarks, 2026.** \$ million, log scale. Shaded bands show the capital to host the stated capacity, from construction cost (\$10.7 million per MW) to fully equipped AI capacity (\$38 million per MW), as described in section 3.2. Thailand's software figure is annual salary spend (hollow marker); Malaysia's paid-up capital figures are company capital, not project scale; the 0.85 MW bar shows the capital to host the smallest DESAC category. Viet Nam states no capital threshold.](fig1_threshold_ladder.png)
