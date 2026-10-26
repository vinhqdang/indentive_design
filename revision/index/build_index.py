"""Incentive-barrier index for AI-related entry routes.

Input: the hand-coded routes below (each traced to rows of Supporting Information
Table S1 and to the primary texts). Output: routes.csv, index_results.md.
No outcome data are used. Run: python3 -I build_index.py
"""
import csv, math, itertools, random

T0 = 0.28      # US$m: capital to host one eight-accelerator server (midpoint of 0.13 and 0.46)
TV = 32.0      # US$m: viable fleet, central case (geometric mean of 13 and 80)
SPAN = 3.0     # orders of magnitude that map to a score of 1

# route, country, layer, entry capital threshold in US$m (None = none stated), capital basis,
# obligations (a certification, b external audit at own cost, c mandated certified or third-party location,
# d annual report with inspection, e application documentation package and annual claim),
# vintage score, delivery score, SI rows
ROUTES = [
 ("TH-SW",     "Thailand",    "(i)",         0.042, "annual salary spend (not capital)", [],            0.5, 1.0, "1"),
 ("TH-CLOUD",  "Thailand",    "(ii)",        None,  "none stated",                          ["a","c"],   0.5, 1.0, "21"),
 ("TH-GPU",    "Thailand",    "(ii)",        140.0, "minimum capital",                      ["c"],       0.5, 1.0, "4"),
 ("TH-DC",     "Thailand",    "(iii)",       40.3,  "capital to host 2 MW (21.4 to 76)",    ["a"],       0.5, 1.0, "22"),
 ("VN-START",  "Viet Nam",    "(i)",         None,  "none stated",                          ["d"],       0.0, 0.5, "8, 9"),
 ("VN-CLOUD",  "Viet Nam",    "(ii)",        None,  "none stated",                          ["d"],       1.0, 0.5, "11, 25"),
 ("MY-MD",     "Malaysia",    "(i)+(ii)",    0.011, "paid-up capital",                      ["b"],       0.5, 1.0, "14"),
 ("MY-DESAC",  "Malaysia",    "(ii)+(iii)",  17.1,  "capital to host 0.85 MW (9.1 to 32.3)",["b","d"],   0.5, 1.0, "15, 16, 17, 23"),
 ("PH-SW",     "Philippines", "(i)+(ii)",    None,  "none stated",                          ["d","e"],   0.5, 1.0, "18, 27"),
 ("PH-AI",     "Philippines", "(i)",         None,  "none stated",                          ["d","e"],   0.5, 1.0, "18, 28"),
 ("PH-DC",     "Philippines", "(iii)",       None,  "none stated",                          ["d","e"],   0.5, 1.0, "18, 29"),
]
COMPUTE = {"TH-CLOUD","TH-GPU","TH-DC","VN-CLOUD","MY-MD","MY-DESAC","PH-SW","PH-DC"}

def cb(T, base):
    if T is None: return 0.0
    return max(0.0, min(1.0, math.log10(T/base)/SPAN))

rows=[]
for r in ROUTES:
    route,ctry,layer,T,basis,obl,vb,dl,si = r
    cc = min(len(obl),3)/3
    rows.append(dict(route=route,country=ctry,layer=layer,threshold_usd_m=T if T is not None else "",basis=basis,
        CB=round(cb(T,T0),3),CB_viable=round(cb(T,TV),3),CC=round(cc,3),VB=vb,DL=dl,SI_rows=si))

W = {"equal":(1,1,1,1),"capital x2":(2,1,1,1),"no delivery":(1,1,1,0),"capital only":(1,0,0,0),"friction x2":(1,2,1,1),"viable-fleet capital":None}
def comp(row,w,viable=False):
    c = row["CB_viable"] if viable else row["CB"]
    v=(c,row["CC"],row["VB"],row["DL"]); s=sum(w)
    return sum(a*b for a,b in zip(w,v))/s
for row in rows:
    for name,w in W.items():
        row["I_"+name]= round(comp(row,(1,1,1,1),True) if w is None else comp(row,w),3)
with open("routes.csv","w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

# country compute-entry score: lowest composite among compute routes; facility score: data-centre route
def best(country,key):
    c=[r[key] for r in rows if r["country"]==country and r["route"] in COMPUTE]; return min(c)
country_rows=[]
for ctry in ["Malaysia","Philippines","Thailand","Viet Nam"]:
    entry=best(ctry,"I_equal"); 
    fac=[r["I_equal"] for r in rows if r["country"]==ctry and r["layer"] in ("(iii)","(ii)+(iii)")]
    country_rows.append((ctry,entry,fac[0] if fac else None))

# rank robustness: random weights
def rank_order(weights):
    vals={}
    for ctry in ["Malaysia","Philippines","Thailand","Viet Nam"]:
        vals[ctry]=min(comp(r,weights) for r in rows if r["country"]==ctry and r["route"] in COMPUTE)
    return vals
random.seed(1)
N=20000; wins={c:0 for c in ["Malaysia","Philippines","Thailand","Viet Nam"]}; low_th=0; th_not_lowest=0
for _ in range(N):
    g=[random.gammavariate(1,1) for _ in range(4)]; s=sum(g); wts=[x/s for x in g]
    v=rank_order(wts); lowest=min(v,key=v.get); wins[lowest]+=1
    if v["Thailand"]>min(v["Viet Nam"],v["Malaysia"]): th_not_lowest+=1
lines=["# Incentive-barrier index: results","",
"Scores run from 0 (open) to 1 (restrictive). Dimensions: CB capital barrier, CC compliance friction, VB vintage barrier, DL delivery that presupposes profit. Composite is the equal-weight mean.",""]
lines+=["| Route | Country | Layer | Threshold (US$m) | CB | CC | VB | DL | Composite | Composite, viable-fleet capital |","|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    lines.append(f"| {r['route']} | {r['country']} | {r['layer']} | {r['threshold_usd_m'] if r['threshold_usd_m']!='' else 'none'} | {r['CB']:.2f} | {r['CC']:.2f} | {r['VB']:.1f} | {r['DL']:.1f} | {r['I_equal']:.2f} | {r['I_viable-fleet capital']:.2f} |")
lines+=["","## Country compute-entry score (lowest composite among compute routes)","","| Country | Entry score | Facility-route score |","|---|---|---|"]
for c,e,f in country_rows: lines.append(f"| {c} | {e:.2f} | {'' if f is None else f'{f:.2f}'} |")
lines+=["","## Sensitivity of the route ranking to weights","",
"| Weighting | "+" | ".join(r['route'] for r in rows)+" |","|---|"+"---|"*len(rows)]
def ranks(vals):
    order=sorted(range(len(vals)),key=lambda i:vals[i]); rk=[0]*len(vals)
    i=0
    while i<len(order):
        j=i
        while j+1<len(order) and vals[order[j+1]]==vals[order[i]]: j+=1
        for k in range(i,j+1): rk[order[k]]=(i+j)/2+1
        i=j+1
    return rk
base=[r["I_equal"] for r in rows]; 
def spearman(a,b):
    ra,rb=ranks(a),ranks(b); n=len(a); ma=sum(ra)/n; mb=sum(rb)/n
    num=sum((x-ma)*(y-mb) for x,y in zip(ra,rb)); den=math.sqrt(sum((x-ma)**2 for x in ra)*sum((y-mb)**2 for y in rb))
    return num/den
for name in W:
    vals=[r["I_"+name] for r in rows]
    lines.append(f"| {name} (rho with equal weights {spearman(base,vals):.2f}) | "+" | ".join(f"{v:.2f}" for v in vals)+" |")
lines+=["",f"Random weights (Dirichlet(1,1,1,1), {N} draws): share of draws in which each country has the lowest compute-entry score: "+", ".join(f"{c} {wins[c]/N:.0%}" for c in wins)+f". Thailand's entry score is higher than at least one of Malaysia and Viet Nam in {th_not_lowest/N:.0%} of draws."]
open("index_results.md","w",encoding="utf-8").write("\n".join(lines)+"\n")
print("\n".join(lines))
