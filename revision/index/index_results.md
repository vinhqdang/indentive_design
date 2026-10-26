# Incentive-barrier index: results

Scores run from 0 (open) to 1 (restrictive). Dimensions: CB capital barrier, CC compliance friction, VB vintage barrier, DL delivery that presupposes profit. Composite is the equal-weight mean.

| Route | Country | Layer | Threshold (US$m) | CB | CC | VB | DL | Composite | Composite, viable-fleet capital |
|---|---|---|---|---|---|---|---|---|---|
| TH-SW | Thailand | (i) | 0.042 | 0.00 | 0.00 | 0.5 | 1.0 | 0.38 | 0.38 |
| TH-CLOUD | Thailand | (ii) | none | 0.00 | 0.67 | 0.5 | 1.0 | 0.54 | 0.54 |
| TH-GPU | Thailand | (ii) | 140.0 | 0.90 | 0.33 | 0.5 | 1.0 | 0.68 | 0.51 |
| TH-DC | Thailand | (iii) | 40.3 | 0.72 | 0.33 | 0.5 | 1.0 | 0.64 | 0.47 |
| VN-START | Viet Nam | (i) | none | 0.00 | 0.33 | 0.0 | 0.5 | 0.21 | 0.21 |
| VN-CLOUD | Viet Nam | (ii) | none | 0.00 | 0.33 | 1.0 | 0.5 | 0.46 | 0.46 |
| MY-MD | Malaysia | (i)+(ii) | 0.011 | 0.00 | 0.33 | 0.5 | 1.0 | 0.46 | 0.46 |
| MY-DESAC | Malaysia | (ii)+(iii) | 17.1 | 0.59 | 0.67 | 0.5 | 1.0 | 0.69 | 0.54 |
| PH-SW | Philippines | (i)+(ii) | none | 0.00 | 0.67 | 0.5 | 1.0 | 0.54 | 0.54 |
| PH-AI | Philippines | (i) | none | 0.00 | 0.67 | 0.5 | 1.0 | 0.54 | 0.54 |
| PH-DC | Philippines | (iii) | none | 0.00 | 0.67 | 0.5 | 1.0 | 0.54 | 0.54 |

## Country compute-entry score (lowest composite among compute routes)

| Country | Entry score | Facility-route score |
|---|---|---|
| Malaysia | 0.46 | 0.69 |
| Philippines | 0.54 | 0.54 |
| Thailand | 0.54 | 0.64 |
| Viet Nam | 0.46 |  |

## Sensitivity of the route ranking to weights

| Weighting | TH-SW | TH-CLOUD | TH-GPU | TH-DC | VN-START | VN-CLOUD | MY-MD | MY-DESAC | PH-SW | PH-AI | PH-DC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| equal (rho with equal weights 1.00) | 0.38 | 0.54 | 0.68 | 0.64 | 0.21 | 0.46 | 0.46 | 0.69 | 0.54 | 0.54 | 0.54 |
| capital x2 (rho with equal weights 0.99) | 0.30 | 0.43 | 0.73 | 0.65 | 0.17 | 0.37 | 0.37 | 0.67 | 0.43 | 0.43 | 0.43 |
| no delivery (rho with equal weights 0.88) | 0.17 | 0.39 | 0.58 | 0.52 | 0.11 | 0.44 | 0.28 | 0.59 | 0.39 | 0.39 | 0.39 |
| capital only (rho with equal weights 0.77) | 0.00 | 0.00 | 0.90 | 0.72 | 0.00 | 0.00 | 0.00 | 0.59 | 0.00 | 0.00 | 0.00 |
| friction x2 (rho with equal weights 1.00) | 0.30 | 0.57 | 0.61 | 0.58 | 0.23 | 0.43 | 0.43 | 0.69 | 0.57 | 0.57 | 0.57 |
| viable-fleet capital (rho with equal weights 0.70) | 0.38 | 0.54 | 0.51 | 0.47 | 0.21 | 0.46 | 0.46 | 0.54 | 0.54 | 0.54 | 0.54 |

Random weights (Dirichlet(1,1,1,1), 20000 draws): share of draws in which each country has the lowest compute-entry score: Malaysia 50%, Philippines 0%, Thailand 0%, Viet Nam 50%. Thailand's entry score is higher than at least one of Malaysia and Viet Nam in 100% of draws.
