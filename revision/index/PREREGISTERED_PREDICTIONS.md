# Predictions fixed before the outcome data were analysed

Date of record: 26 October 2026 (before any analysis of the project-level outcome data; the index in `build_index.py` does not use outcome data).

The incentive index scores 12 entry routes (country by activity) on four dimensions from the coded legal texts. The outcome data are project-level records of approved or announced digital and AI investments by country, collected from public sources. The following predictions are stated in advance. A prediction counts as supported only if the direction holds; no significance test with four countries is treated as decisive.

* **P1, scale gate and project size.** Within a country, the median investment of projects is larger in routes with a higher capital-barrier score. Test: Thai routes (software, cloud, GPU hosting, data centre) ordered by capital-barrier score against median approved investment.
* **P2, barrier and domestic share.** The domestic-firm share of projects is lower in routes with a higher composite barrier score, within a country and across countries at the compute layers. Test: Spearman rank correlation across routes with at least five projects.
* **P3, bunching at the threshold.** Where a capacity threshold is stated (Thailand, 2 MW; Malaysia DESAC, 0.85 MW), no or almost no approved data-centre project lies below it, and the size distribution starts at or above it. Test: share of projects with stated IT load below the threshold.
* **P4, friction on low-capital routes.** Routes with no capital barrier but with fixed compliance costs (Thai cloud services, Malaysia Digital) attract fewer domestic entrants than the lowest-friction route in the same country. Test: counts of domestic projects per route.
* **P5, a rule-light system does not guarantee domestic entry.** In Viet Nam and the Philippines, where no capital rule is stated at the compute layers, the observed domestic share is not systematically higher than in Thailand and Malaysia. Test: compare domestic shares; a clearly higher domestic share in the rule-light systems would count against the index as an explanation of entry.

What would count against the index: a negative rank correlation in P1 or P2, projects well below stated thresholds in P3, or a clearly higher domestic share in the rule-light systems in P5.
