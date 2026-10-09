"""Figure 1: eligibility thresholds against cost benchmarks (log scale, US$ million).

All threshold values are those reported in Table 3 of the manuscript (several are
still marked VERIFY there). Benchmarks are derived from the two cost figures cited
in Section 5.1: US$10.7m per MW (construction) and US$38m per MW (fully equipped AI
capacity), and from the 12 kW per 8-accelerator server assumption (CITATION NEEDED).
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, MUTED, GRID, BAND = "#0b0b0b", "#52514e", "#d9d8d2", "#ecebe6"

CONSTR, EQUIP = 10.7, 38.0          # US$ million per MW
node_mw, hyper_mw = 0.012, 40.0
bands = [
    ("One 8-accelerator\nnode (12 kW)", node_mw * CONSTR, node_mw * EQUIP),
    ("1 MW", 1 * CONSTR, 1 * EQUIP),
    ("40 MW\n(hyperscale)", hyper_mw * CONSTR, hyper_mw * EQUIP),
]

plt.rcParams["font.family"] = "Liberation Sans"
fig, ax = plt.subplots(figsize=(7.4, 4.9), dpi=300)
ax.set_xscale("log")
ax.set_xlim(0.003, 6000)
rows = ["Thailand", "Vietnam", "Malaysia", "Philippines"]
ypos = {r: i for i, r in enumerate(reversed(rows))}
ax.set_ylim(-0.7, 3.95)

for name, lo, hi in bands:
    ax.axvspan(lo, hi, color=BAND, zorder=0, lw=0)
    ax.text((lo * hi) ** 0.5, 3.8, name, ha="center", va="top", fontsize=7, color=MUTED)

for y in ypos.values():
    ax.axhline(y, color=GRID, lw=0.6, zorder=1)

def pt(country, x, layer, label, hollow=False, dx=0, dy=0.2, ha="center"):
    y = ypos[country]
    color, marker = (BLUE, "o") if layer == "app" else (ORANGE, "s")
    ax.scatter([x], [y], s=46, marker=marker, zorder=4,
               facecolor="white" if hollow else color, edgecolor=color, linewidth=1.6)
    ax.text(x * (10 ** dx), y + dy, label, ha=ha, va="bottom", fontsize=7, color=INK, zorder=5)

# Thailand
pt("Thailand", 0.042, "app", "Software\n$0.04m a year in\nlocal salaries", hollow=True)
pt("Thailand", 140, "infra", "GPU data hosting\n$140m minimum capital")
# Malaysia (two parallel tracks)
ym = ypos["Malaysia"]
pt("Malaysia", 0.011, "app", "Malaysia Digital (incl. cloud)\n$0.011m paid-up capital")
pt("Malaysia", 0.55, "infra", "DESAC capitalisation floor\n$0.55m paid-up capital*")
ax.plot([0.85 * CONSTR, 0.85 * EQUIP], [ym, ym], color=ORANGE, lw=6, solid_capstyle="butt", zorder=4)
ax.text((0.85 * CONSTR * 0.85 * EQUIP) ** 0.5, ym - 0.12, "Smallest DESAC data-centre\ncategory: 0.85 MW (capital to host)", ha="center", va="top", fontsize=7, color=INK)
pt("Malaysia", 220, "infra", "DESAC 10-year condition\n$220m cumulative capex")
# Philippines
pt("Philippines", 260, "infra", "PHP 15bn firm-scale boundary\n$260m, all activities", dx=-0.1, ha="right")
pt("Philippines", 865, "infra", "PHP 50bn presidential\npackage condition, $865m", dx=0.08, ha="left")
ax.text(0.011, ypos["Philippines"] + 0.1, "Application layer and data centres: no stated minimum (2026 Plan)",
        fontsize=7, color=MUTED, va="bottom", ha="left")
# Vietnam
ax.text(0.011, ypos["Vietnam"] + 0.1,
        "No capital threshold stated for any AI layer (strategic-technology list, Decision 21/2026)",
        fontsize=7, color=MUTED, va="bottom", ha="left")

ax.set_yticks(list(ypos.values()))
ax.set_yticklabels(list(ypos.keys()), fontsize=8.5, color=INK)
ax.set_xticks([0.01, 0.1, 1, 10, 100, 1000])
ax.set_xticklabels(["0.01", "0.1", "1", "10", "100", "1,000"], fontsize=7.5, color=MUTED)
ax.set_xlabel("US$ million (log scale)", fontsize=8, color=MUTED)
ax.tick_params(length=0)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRID)

handles = [
    Line2D([], [], marker="o", ls="", color=BLUE, markerfacecolor=BLUE, markersize=6, label="Application layer"),
    Line2D([], [], marker="s", ls="", color=ORANGE, markerfacecolor=ORANGE, markersize=6, label="Cloud, data-centre or cross-layer tier"),
    Line2D([], [], marker="o", ls="", color=BLUE, markerfacecolor="white", markersize=6, label="Annual spend, not capital"),
]
ax.legend(handles=handles, loc="upper center", ncol=3, fontsize=7, frameon=False, bbox_to_anchor=(0.5, -0.14))

fig.tight_layout()
fig.savefig("fig1_threshold_ladder.png", facecolor="#fcfcfb")
print("ok")
