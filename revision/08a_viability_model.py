"""Viability benchmark for a small AI-compute provider (assumption A1).

Every input is a stated assumption or a figure from the sources in
08_viability_benchmark.md. Run: python3 08a_viability_model.py
"""
import math

H, G = 8760, 8            # hours a year; GPUs per server
KW, LOAD, POWER = 12, 0.7, 0.11   # kW per server; average load factor; US$ per kWh (THB 3.95 at 35.7 THB/US$)
VAR = 0.10                # revenue-proportional costs (payment, support, bandwidth)
PRICES = (1.70, 2.35, 3.00, 3.85)  # US$ per GPU-hour: 1-year contract index (Oct 2025, Mar 2026) to neocloud on-demand list


def crf(rate, life):
    return rate / (1 - (1 + rate) ** -life)


def annual_cost(capex, life, colo, rate, power_included=False):
    """Capital charge plus colocation plus metered power, per server a year."""
    power = 0 if power_included else KW * LOAD * H * POWER
    return crf(rate, life) * capex + colo * KW * 12 + power


def breakeven_util(capex, life, colo, rate, price, power_included=False):
    return annual_cost(capex, life, colo, rate, power_included) / (price * G * H * (1 - VAR))


CASES = {
    "Small provider, favourable inputs (US$250k, 5 years, colocation US$200/kW, 10%)": (250e3, 5, 200, 0.10),
    "Small provider, central inputs (US$300k, 4 years, colocation US$330/kW, 10%)": (300e3, 4, 330, 0.10),
    "Small provider, adverse inputs (US$320k, 3 years, colocation US$475/kW, 10%)": (320e3, 3, 475, 0.10),
    "Scale provider (US$250k, 4 years, wholesale US$150/kW, 8%)": (250e3, 4, 150, 0.08),
}

print("Break-even utilisation (1.00 = every hour sold)")
print(f"{'':80s}" + "".join(f"{p:>8.2f}" for p in PRICES))
for name, (c, l, k, r) in CASES.items():
    print(f"{name:80s}" + "".join(f"{breakeven_util(c, l, k, r, p):8.2f}" for p in PRICES))

print("\nMinimum fleet (servers) to cover provider overhead F, central inputs")
c, l, k, r = CASES["Small provider, central inputs (US$300k, 4 years, colocation US$330/kW, 10%)"]
for F in (50e3, 150e3, 300e3):
    out = []
    for u, p in ((0.8, 3.00), (0.8, 3.85), (0.6, 3.85)):
        margin = p * G * H * u * (1 - VAR) - annual_cost(c, l, k, r)
        out.append(f"util {u:.0%}, US${p}: " + ("none (margin <= 0)" if margin <= 0 else f"{F / margin:6.0f} servers = US${F / margin * c / 1e6:5.1f}m"))
    print(f"F = US${F / 1e3:.0f}k:  " + " | ".join(out))

print("\nDistance of each threshold from a viable fleet of US$13m to US$80m (orders of magnitude)")
LO, HI = 13.0, 80.0
for name, (a, b) in {
    "Thailand GPU hosting, US$140m": (140, 140),
    "Thailand data centres 2 MW, US$21-76m to host": (21, 76),
    "Malaysia DESAC smallest category 0.85 MW, US$9-32m": (9, 32),
    "Malaysia DESAC ten-year condition, US$220m": (220, 220),
    "Philippines boundary, US$260m": (260, 260),
    "Philippines presidential package, US$865m": (865, 865),
    "Siam AI cloud project, THB 3.25bn = US$91m": (91, 91),
}.items():
    print(f"{name:55s} {math.log10(a / HI):5.1f} to {math.log10(b / LO):4.1f}")
