"""Index versus outcomes. Reads routes.csv (index), the Epoch AI GPU cluster dataset (path as argument)
and the collected project records. Run: python3 -I analysis.py /path/to/gpu_clusters.csv"""
import csv, math, sys, statistics as st

routes = {r["route"]: r for r in csv.DictReader(open("routes.csv", encoding="utf-8"))}
def rank(v):
    o = sorted(range(len(v)), key=lambda i: v[i]); rk = [0.0]*len(v); i = 0
    while i < len(o):
        j = i
        while j+1 < len(o) and v[o[j+1]] == v[o[i]]: j += 1
        for k in range(i, j+1): rk[o[k]] = (i+j)/2+1
        i = j+1
    return rk
def spearman(a, b):
    ra, rb = rank(a), rank(b); n = len(a); ma, mb = sum(ra)/n, sum(rb)/n
    num = sum((x-ma)*(y-mb) for x, y in zip(ra, rb)); den = math.sqrt(sum((x-ma)**2 for x in ra)*sum((y-mb)**2 for y in rb))
    return num/den

out = ["# Index versus outcomes", ""]

# A. Thailand, BOI approvals January to December 2025 (official statistics) and the one cloud project
A = [("TH-SW", "8.1.1 software", 96, 933.0, 46.0),
     ("TH-CLOUD", "8.2.2 cloud (Siam AI project only)", 1, 3250.0, 100.0),
     ("TH-DC", "8.2.1 data centres", 24, 457999.8, 15.0),
     ("TH-GPU", "8.2.4 data hosting (TikTok project only)", 1, 126793.0, 0.0)]
out += ["## A. Thailand: BOI approvals by route, 2025", "",
        "| Route | Activity | Index (composite) | Capital barrier | Projects | Mean investment (THB million) | Thai-held share of registered capital (%) |",
        "|---|---|---|---|---|---|---|"]
comp = []; inv = []; thai = []
for rt, lab, n, tot, th in A:
    r = routes[rt]; mean = tot/n
    out.append(f"| {rt} | {lab} | {float(r['I_equal']):.2f} | {float(r['CB']):.2f} | {n} | {mean:,.1f} | {th:.0f} |")
    comp.append(float(r["I_equal"])); inv.append(mean); thai.append(th)
rho_inv = spearman(comp, inv); rho_thai = spearman(comp, thai)
out += ["", f"Rank correlation of the composite index with mean project investment: {rho_inv:.2f} (n = 4). With the Thai-held share: {rho_thai:.2f} (n = 4). The cloud route has one project, owned by a Thai firm, which breaks the monotonic fall in the Thai-held share with the index. With four points no significance test is meaningful.", ""]

# B. Epoch AI GPU clusters in the four economies (and Singapore)
origin = {"SIAM AI HGX": "Thai (private)", "GreenNode Bangkok Cluster": "Vietnamese firm in Thailand (private)",
          "NSTDA Supercomputer Center (ThaiSC) LANTA": "Thai (public)", "Alibaba Cloud in Thailand Phase 1": "foreign hyperscaler",
          "Alibaba Cloud in Thailand Phase 2": "foreign hyperscaler", "Alibaba Cloud in Philippines Phase 1": "foreign hyperscaler",
          "Alibaba Cloud in Malaysia Phase 2": "foreign hyperscaler", "Vingroup VinAI Research Superpod": "Vietnamese (private)",
          "Sustainable Metal Cloud Singapore Phase 1": "Singapore-based (private)"}
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8-sig")))
sea = [r for r in rows if r["Name"] in origin]
out += ["## B. Epoch AI GPU clusters in the four economies", "",
        "| Country | Cluster | Owner origin | First operational | H100 equivalents | Power (MW) |", "|---|---|---|---|---|---|"]
for r in sorted(sea, key=lambda r: (r["Country"], r["First Operational Date"])):
    h = f"{float(r['H100 equivalents']):,.0f}" if r["H100 equivalents"] else "n/a"
    p = f"{float(r['Power Capacity (MW)']):.2f}" if r["Power Capacity (MW)"] else "n/a"
    out.append(f"| {r['Country'].replace(' (the)','')} | {r['Name']} | {origin[r['Name']]} | {r['First Operational Date']} | {h} | {p} |")
dom_priv = [r for r in sea if origin[r["Name"]].startswith(("Thai (private)", "Vietnamese firm", "Vietnamese (private)")) and r["Country"] in ("Thailand","Vietnam","Malaysia","Philippines (the)")]
out += ["", f"Domestic or regional private AI clusters listed in the four economies: {len(dom_priv)} (Thailand 2, Viet Nam 1, Malaysia 0, Philippines 0). The two Thai clusters have 1,024 H100 equivalents (128 eight-GPU servers) and 1.46 MW, below the 2 MW data-centre condition and inside the 45 to 270 server range of the viability benchmark. Epoch lists large clusters only, so smaller providers are not represented.", ""]

# C. Data-centre project size against stated thresholds (collected project records, indicative)
def mw(file, thresh):
    v = [float(r["it_load_mw"]) for r in csv.DictReader(open(file, encoding="utf-8")) if r.get("it_load_mw")]
    return len(v), min(v), st.median(v), max(v), sum(x < thresh for x in v)
out += ["## C. Project size against stated capacity thresholds (collected records, indicative)", "",
        "| Country | Projects with stated IT load | Smallest (MW) | Median (MW) | Largest (MW) | Stated threshold (MW) | Below threshold |", "|---|---|---|---|---|---|---|"]
for ctry, f, th in (("Thailand", "outcomes_raw/thailand_projects.csv", 2.0), ("Malaysia", "outcomes_raw/malaysia_projects.csv", 0.85),
                    ("Viet Nam", "outcomes_raw/vietnam_projects.csv", None), ("Philippines", "outcomes_raw/philippines_projects.csv", None)):
    n, lo, md, hi, below = mw(f, th if th else 0)
    out.append(f"| {ctry} | {n} | {lo:g} | {md:g} | {hi:g} | {th if th else 'none stated'} | {below if th else 'n/a'} |")
out += ["", "Approved or announced data-centre projects are 10 to 300 MW, six or more times the stated minima, so the capacity thresholds do not bind on the projects that appear in public records.", ""]

# D. Scoreboard
out += ["## D. Predictions fixed in advance and what the data show", "",
"| Prediction | Result | Reading |", "|---|---|---|",
f"| P1 scale gate and project size | Supported (rank correlation {rho_inv:.2f}, four Thai routes) | Mean project size rises with the capital barrier. Two routes rest on one project. |",
f"| P2 barrier and domestic share | Partly supported (rank correlation {rho_thai:.2f}) | Thai-held share falls with the index except in the cloud route, which has one Thai-owned project. |",
"| P3 bunching at the threshold | Not supported as stated | Projects start far above the stated minima (12 MW against 2 MW; 120 MW against 0.85 MW), so thresholds do not bind on these projects. |",
"| P4 friction on low-capital routes | Inconclusive | Software route: 96 approved projects; cloud route: one project known to us, because BOI approvals for the cloud activity were not obtained; no verified small project under Malaysia Digital or the Viet Nam cloud listing. |",
"| P5 rule-light systems do not guarantee domestic entry | Consistent, coverage-limited | Domestic private AI clusters: Thailand 2, Viet Nam 1, Malaysia 0, Philippines 0; the two systems without capital rules (Viet Nam, Philippines) have no more than Thailand. |",
"| P6a (exploratory) lower entry-route barrier, more digital greenfield investment | Consistent (-0.89, four countries) | Malaysia and Viet Nam, with the lowest entry scores, attract the most; the Philippines, with a higher score, is outside the top ten. |",
"| P6b (exploratory) higher data-centre route barrier, less data-centre investment | Not supported (+0.50, three countries) | Malaysia has the highest data-centre route score and the largest data-centre investment. |",
"", "Counter-evidence to the design reading: capacity thresholds are not where entrants cluster, which fits H1 (cost) as an explanation of why thresholds sit near facility scale."]

# E. Country level (exploratory; UNCTAD WIR 2025, fDi Markets, announced greenfield 2020 to 2024)
entry = {"Malaysia": 0.46, "Viet Nam": 0.46, "Philippines": 0.54, "Thailand": 0.54}
facility = {"Malaysia": 0.69, "Thailand": 0.64, "Philippines": 0.54}
digital_bn = {"Malaysia": 74.0, "Viet Nam": 32.0, "Thailand": 16.0, "Philippines": 15.9}   # Philippines: not in the top ten, so at most 16; 15.9 stands for "below 16"
swf = {"Malaysia": (44, 2153), "Philippines": (4, 763), "Thailand": (1, 266), "Viet Nam": (1, 191)}
c = ["Malaysia", "Philippines", "Thailand", "Viet Nam"]
rho6a = spearman([entry[x] for x in c], [digital_bn[x] for x in c])
c3 = ["Malaysia", "Philippines", "Thailand"]
rho6b = spearman([facility[x] for x in c3], [swf[x][1] for x in c3])
out += ["", "## E. Country level (exploratory)", "",
        "| Country | Entry-route score | Data-centre route score | Digital greenfield announced 2020-2024 (US$ billion) | Sovereign-fund data-centre projects 2020-2024 (number; US$ million) |",
        "|---|---|---|---|---|"]
for x in c:
    d = "below 16 (outside top ten)" if x == "Philippines" else f"{digital_bn[x]:.0f}"
    out.append(f"| {x} | {entry[x]:.2f} | {facility.get(x, 'none'):} | {d} | {swf[x][0]}; {swf[x][1]:,} |")
out += ["", f"P6a: rank correlation of the entry-route score with announced digital greenfield value: {rho6a:.2f} (n = 4, with tied scores). A lower barrier goes with more investment, as predicted.",
        f"P6b: rank correlation of the data-centre route score with sovereign-fund data-centre investment: {rho6b:.2f} (n = 3). A positive value runs against the prediction: Malaysia has the highest data-centre route score and the most investment.", ""]
open("analysis_results.md", "w", encoding="utf-8").write("\n".join(out)+"\n")
print("\n".join(out[-14:]))

