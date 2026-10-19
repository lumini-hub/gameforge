#!/usr/bin/env python3
"""Economics diagrams -> figs_e/*.svg (matplotlib)."""
import pathlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Wedge

OUT = pathlib.Path(__file__).parent / "figs_e"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"svg.fonttype": "none", "font.family": "DejaVu Sans", "font.size": 8.4, "axes.linewidth": 0.8, "axes.titlesize": 9, "axes.titleweight": "bold", "axes.titlecolor": "#0e3a66"})
NAVY, RED, GREEN, ORANGE, GREY, BLUE, TEAL = "#0e3a66", "#b3211b", "#2a7a3a", "#b36200", "#777", "#1f5fa8", "#0f7b6c"
W = 5.7


def fig(h, ncols=1, **kw):
    return plt.subplots(1, ncols, figsize=(W, h), **kw)


def save(f, name):
    f.tight_layout(pad=0.6)
    f.savefig(OUT / f"{name}.svg", format="svg")
    plt.close(f)


def ds_axes(ax, xl="Quantity", yl="Price", lim=(0, 10)):
    ax.set_xlim(*lim); ax.set_ylim(*lim)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel(xl, fontsize=8.4, labelpad=16); ax.set_ylabel(yl, fontsize=8.4, labelpad=30)
    for s in ("top", "right"): ax.spines[s].set_visible(False)


def drop(ax, x, y, xl=None, yl=None, c="#555"):
    ax.plot([x, x], [0, y], ls="--", color=c, lw=0.9)
    ax.plot([0, x], [y, y], ls="--", color=c, lw=0.9)
    if xl: ax.text(x, -0.55, xl, ha="center", fontsize=8.4)
    if yl: ax.text(-0.25, y, yl, ha="right", va="center", fontsize=8.4)


D = lambda x, s=0: 10.5 - x + s
Sx = lambda x, s=0: x - 0.2 + s


def wage_eq():
    f, ax = fig(3.1)
    ds_axes(ax, "Quantity of labour", "Wage rate")
    x = np.linspace(1, 9.5, 20)
    ax.plot(x, 10.5 - x, color=BLUE, lw=2); ax.plot(x, x - 0.2, color=RED, lw=2)
    ax.text(9.5, 0.7, "D", color=BLUE, fontweight="bold"); ax.text(9.5, 9.5, "S", color=RED, fontweight="bold")
    ax.plot(5.35, 5.15, "o", color="k", ms=5); ax.text(5.5, 5.35, "E", fontweight="bold")
    drop(ax, 5.35, 5.15, "N", "W")
    ax.plot([0, 3.4], [7.1, 7.1], ls="--", color="#555", lw=0.9); ax.text(-0.25, 7.1, "W₁", ha="right", va="center")
    ax.plot([0, 7.3], [3.2, 3.2], ls="--", color="#555", lw=0.9); ax.text(-0.25, 3.2, "W₂", ha="right", va="center")
    ax.text(2.4, 9.0, "Excess supply\n(wage falls)", color=GREEN, fontsize=8)
    ax.text(0.3, 1.6, "Excess demand\n(wage rises)", color=ORANGE, fontsize=8)
    ax.set_title("Wage determination: E = equilibrium", loc="left")
    save(f, "e_wage_eq")


def supply_shift():
    f, ax = fig(2.9)
    ds_axes(ax, "Quantity of labour", "Wage rate")
    x = np.linspace(1, 9.5, 20)
    ax.plot(x, 10.5 - x, color=BLUE, lw=2); ax.plot(x, x - 0.2, color=RED, lw=2)
    ax.plot(x, x - 2.4, color=RED, lw=2, ls="--")
    ax.text(9.4, 0.8, "D", color=BLUE, fontweight="bold"); ax.text(9.0, 9.0, "S", color=RED, fontweight="bold"); ax.text(9.6, 7.3, "S₁", color=RED, fontweight="bold")
    ax.plot(5.35, 5.15, "o", color="k", ms=4); ax.text(5.0, 5.55, "E", fontweight="bold")
    ax.plot(6.45, 4.05, "o", color="k", ms=4); ax.text(6.7, 4.3, "E₁", fontweight="bold")
    drop(ax, 5.35, 5.15, "Q", "W"); drop(ax, 6.45, 4.05, "Q₁", "W₁")
    ax.annotate("", (8.6, 2.6), (7.0, 2.6), arrowprops=dict(arrowstyle="-|>", color=GREEN))
    ax.text(6.7, 1.3, "supply of labour increases", fontsize=7.8, color=GREEN)
    ax.set_title("2025 Q1(x): S shifts right to S₁", loc="left")
    save(f, "e_supply_shift")


def interest():
    f, ax = fig(3.0)
    ax.set_xlim(0, 11); ax.set_ylim(0, 15)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.set_xlabel("Quantity of capital (Nu million)"); ax.set_ylabel("Interest rate (%)")
    ax.set_xticks([3, 6, 9]); ax.set_xticklabels(["300", "600", "900"]); ax.set_yticks([10, 12])
    x = np.linspace(1, 10, 20)
    ax.plot(x, 16 - x, color=BLUE, lw=2)       # D: 12%->300? scaled: x units of 100
    ax.plot(x, x + 4, color=RED, lw=2)
    # at 10%: D=6 (600) ; at 12%: D=4? fix by custom lines below
    ax.cla()
    ax.set_xlim(0, 11); ax.set_ylim(0, 14)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.set_xlabel("Quantity of capital (Nu million)"); ax.set_ylabel("Interest rate (%)")
    ax.set_xticks([3, 6, 9]); ax.set_xticklabels(["300", "600", "900"]); ax.set_yticks([10, 12])
    xs = np.linspace(1.5, 9.8, 20)
    ax.plot(xs, 10 + (6 - xs) * (2 / 3), color=BLUE, lw=2)
    ax.plot(xs, 10 + (xs - 6) * (2 / 3), color=RED, lw=2)
    ax.text(1.4, 13.2, "D", color=BLUE, fontweight="bold"); ax.text(9.7, 13.2, "S", color=RED, fontweight="bold")
    ax.plot(6, 10, "o", color="k", ms=5); ax.text(6.2, 9.4, "E", fontweight="bold")
    for q in (3, 9):
        ax.plot([q, q], [0, 12], ls="--", color="#555", lw=0.9)
    ax.plot([6, 6], [0, 10], color="#555", lw=1.1)
    ax.plot([0, 9], [12, 12], ls="--", color="#555", lw=0.9); ax.plot([0, 6], [10, 10], ls="--", color="#555", lw=0.9)
    ax.annotate("demand 300", (3, 12), (0.6, 8.0), fontsize=7.8, color=BLUE, arrowprops=dict(arrowstyle="-", color=BLUE))
    ax.annotate("supply 900", (9, 12), (8.6, 7.0), fontsize=7.8, color=RED, arrowprops=dict(arrowstyle="-", color=RED))
    ax.text(3.6, 12.5, "at 12%: demand 300 < supply 900 (excess supply)", fontsize=7.6, color=GREEN)
    ax.set_title("2024 Q1(ii): demand for capital falls from 600 to 300 (Nu million)", loc="left")
    save(f, "e_interest")


def demand_shift():
    f, ax = fig(2.9)
    ds_axes(ax, "Quantity of vitamin C foods", "Price")
    x = np.linspace(1, 9.5, 20)
    ax.plot(x, 10.5 - x, color=BLUE, lw=2); ax.plot(x, x - 0.2, color=RED, lw=2); ax.plot(x, 12.5 - x, color=BLUE, lw=2, ls="--")
    ax.text(9.3, 0.9, "D", color=BLUE, fontweight="bold"); ax.text(9.2, 9.0, "S", color=RED, fontweight="bold"); ax.text(9.3, 3.3, "D₁", color=BLUE, fontweight="bold")
    ax.plot(5.35, 5.15, "o", color="k", ms=4); ax.text(4.7, 5.7, "E", fontweight="bold")
    ax.plot(6.35, 6.15, "o", color="k", ms=4); ax.text(6.6, 6.4, "E₁", fontweight="bold")
    drop(ax, 5.35, 5.15, "Q", "P"); drop(ax, 6.35, 6.15, "Q₁", "P₁")
    ax.annotate("", (3.5, 8.8), (2.5, 7.8), arrowprops=dict(arrowstyle="-|>", color=GREEN))
    ax.text(3.7, 8.6, "flu season: demand rises", fontsize=7.8, color=GREEN)
    ax.set_title("2025 Q3(b): D shifts right → price and quantity both rise", loc="left")
    save(f, "e_demand_shift")


def labour_sched():
    f, ax = fig(3.1)
    ax.set_xlim(0, 12); ax.set_ylim(1000, 3000)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.set_xlabel("Number of labour"); ax.set_ylabel("Wage rate (Nu)")
    ax.set_yticks([1500, 1850, 2500]); ax.set_xticks([4, 6, 8, 10]); ax.grid(True, color="#e4e4e4", lw=0.5)
    ax.plot([10, 8, 4], [1500, 1850, 2500], "o-", color=BLUE, lw=2, ms=4, label="Demand (DD)")
    ax.plot([6, 8, 10], [1500, 1850, 2500], "o-", color=RED, lw=2, ms=4, label="Supply (SS)")
    ax.text(8.2, 1900, "E (equilibrium)", fontsize=8, fontweight="bold")
    ax.annotate("Excess demand\n(1500: 10 − 6 = 4)", (8, 1500), (9.2, 1180), fontsize=7.8, color=ORANGE)
    ax.annotate("Excess supply\n(2500: 10 − 4 = 6)", (4, 2500), (0.3, 2740), fontsize=7.8, color=GREEN)
    ax.annotate("D", (4, 2500), (3.4, 2540), color=BLUE, fontweight="bold"); ax.annotate("S", (10, 2500), (10.2, 2540), color=RED, fontweight="bold")
    ax.legend(loc="upper center", fontsize=7.6, frameon=False)
    ax.set_title("2025 Q4(b): labour market from the schedule", loc="left")
    save(f, "e_labour_sched")


def bar_gdp():
    f, ax = fig(2.8)
    yrs = ["2019", "2020", "2021", "2022"]; v = [240756, 230055, 270674, 301289]
    b = ax.bar(yrs, v, color=[BLUE, RED, BLUE, BLUE], width=0.55)
    for r, x in zip(b, v): ax.text(r.get_x() + r.get_width() / 2, x + 4000, f"{x:,}", ha="center", fontsize=8)
    ax.set_ylim(0, 340000); ax.set_ylabel("GDP per capita (Nu)"); ax.set_xlabel("Year")
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: f"{int(x/1000)}k"))
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.set_title("2025 Q5(d): bar graph of GDP per capita, Bhutan", loc="left")
    save(f, "e_bar_gdp")


def pie_exports():
    f, ax = fig(2.8)
    vals = [7147, 7697, 8301]; lab = ["2021", "2022", "2023"]
    tot = sum(vals)
    cols = ["#9bb7d9", BLUE, NAVY]
    w, _ = ax.pie(vals, startangle=90, counterclock=False, colors=cols, wedgeprops=dict(edgecolor="white"))
    import math
    ang = 90
    for v, l, c in zip(vals, lab, cols):
        a = v / tot * 360; mid = math.radians(ang - a / 2)
        ax.text(0.62 * math.cos(mid), 0.62 * math.sin(mid), f"{l}\n{v/tot*100:.1f}%\n{a:.0f}°", ha="center", va="center", fontsize=8, color="white" if c != "#9bb7d9" else "#111")
        ang -= a
    ax.set_title("2024 Q2(d): exports 2021–2023 (total Nu 23,145 million)", loc="left")
    save(f, "e_pie_exports")


def line_gdp():
    f, ax = fig(2.8)
    yrs = [2018, 2019, 2020, 2021, 2022]; v = [3389, 3564, 3181, 3561, 3704]
    ax.plot(yrs, v, "o-", color=BLUE, lw=2)
    for x, y in zip(yrs, v): ax.text(x, y + 25, f"{y:,}", ha="center", fontsize=8)
    ax.set_xticks(yrs); ax.set_ylim(3000, 3850); ax.set_xlabel("Year"); ax.set_ylabel("GDP per capita (USD)")
    ax.grid(True, color="#e4e4e4", lw=0.5)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.set_title("2024 Q5(d): line graph of GDP per capita (USD)", loc="left")
    save(f, "e_line_gdp")


def trade25():
    f, ax = fig(2.9)
    yrs = ["2020", "2021", "2022"]; ex = [20732.24, 33555.48, 34396]; im = [66456.12, 90229, 118792]
    x = np.arange(3); w = 0.36
    ax.bar(x - w / 2, ex, w, color=GREEN, label="Export"); ax.bar(x + w / 2, im, w, color=RED, label="Import")
    for i in range(3):
        ax.text(x[i] - w / 2, ex[i] + 2500, f"{ex[i]:,.0f}", ha="center", fontsize=7.4); ax.text(x[i] + w / 2, im[i] + 2500, f"{im[i]:,.0f}", ha="center", fontsize=7.4)
        ax.text(x[i], -17000, f"deficit {im[i]-ex[i]:,.0f}", ha="center", fontsize=7.6, color=RED, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(yrs); ax.set_ylim(-24000, 135000); ax.legend(frameon=False, fontsize=7.8, loc="upper left")
    ax.axhline(0, color="#222", lw=0.8); ax.set_ylabel("Nu (million)")
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.tick_params(axis="x", pad=14)
    ax.set_title("2025 Q4(d): imports exceed exports every year", loc="left")
    save(f, "e_trade25")


def box(ax, x, y, w, h, s, fc="#eaf1fa", ec=NAVY, fs=8, bold=False):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.12", fc=fc, ec=ec, lw=1.2))
    ax.text(x, y, s, ha="center", va="center", fontsize=fs, fontweight="bold" if bold else "normal")


def arr(ax, p, q, c="#222", style="-|>", ls="-", rad=0.0):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=11, color=c, lw=1.3, linestyle=ls, connectionstyle=f"arc3,rad={rad}"))


def circular():
    f, ax = fig(3.7)
    ax.set_xlim(0, 12); ax.set_ylim(0, 7.4); ax.axis("off")
    box(ax, 2.0, 3.0, 2.8, 1.2, "HOUSEHOLDS\n(own factors of\nproduction)", "#fff3df", ORANGE, 8.2, True)
    box(ax, 10.0, 3.0, 2.8, 1.2, "BUSINESS FIRMS\n(producers)", "#e7f4ea", GREEN, 8.2, True)
    box(ax, 6.0, 0.55, 2.8, 0.8, "CAPITAL MARKET\n(banks)", "#f1e9f7", "#5b3a8a", 8)
    arr(ax, (3.4, 4.0), (8.6, 4.0 + 1.9), c=BLUE, rad=-0.25)
    ax.text(6.0, 6.7, "REAL FLOW: factor services (land, labour, capital, enterprise)", ha="center", fontsize=7.8, color=BLUE)
    arr(ax, (8.6, 3.6), (3.4, 3.6), c=GREEN, ls="--", rad=0)
    ax.text(6.0, 3.8, "MONEY FLOW: consumption expenditure", ha="center", fontsize=7.8, color=GREEN)
    arr(ax, (8.6, 2.4), (3.4, 2.4), c=BLUE, ls="--")
    ax.text(6.0, 2.0, "MONEY FLOW: factor income (wage, rent, interest, profit)", ha="center", fontsize=7.8, color=BLUE)
    arr(ax, (3.4, 2.4 - 0.0), (8.6, 2.4 - 0.0), c="#fff", ls="-")
    arr(ax, (8.6, 3.0 - 2.0), (3.4, 1.2 + 0.0), c="#222", rad=0.0, style="-")
    ax.cla(); ax.set_xlim(0, 12); ax.set_ylim(0, 7.6); ax.axis("off")
    box(ax, 1.9, 3.6, 2.9, 1.3, "HOUSEHOLDS\n(own factors of production)", "#fff3df", ORANGE, 8.2, True)
    box(ax, 10.1, 3.6, 2.9, 1.3, "BUSINESS FIRMS\n(producers)", "#e7f4ea", GREEN, 8.2, True)
    box(ax, 6.0, 0.65, 3.4, 0.9, "CAPITAL MARKET (banks)", "#f1e9f7", "#5b3a8a", 7.6)
    # real flows (solid)
    arr(ax, (3.2, 4.45), (8.8, 4.45), c=BLUE, rad=-0.28); ax.text(6, 6.55, "REAL FLOW: factor services\n(land, labour, capital, enterprise)", ha="center", fontsize=7.6, color=BLUE)
    arr(ax, (8.8, 2.75), (3.2, 2.75), c=GREEN, rad=-0.28); ax.text(6, 1.78, "REAL FLOW: goods and services", ha="center", fontsize=7.6, color=GREEN)
    # money flows (dashed)
    arr(ax, (8.8, 3.95), (3.2, 3.95), c=BLUE, ls="--"); ax.text(6, 4.12, "MONEY: factor income (wage, rent, interest, profit)", ha="center", fontsize=6.3, color=BLUE)
    arr(ax, (3.2, 3.25), (8.8, 3.25), c=GREEN, ls="--"); ax.text(6, 2.98, "MONEY: consumption expenditure", ha="center", fontsize=7.4, color=GREEN)
    # saving / investment
    arr(ax, (2.3, 2.9), (4.6, 0.95), c="#5b3a8a"); ax.text(2.0, 1.5, "Saving", color="#5b3a8a", fontsize=8, fontweight="bold")
    arr(ax, (7.4, 0.95), (9.7, 2.9), c="#5b3a8a"); ax.text(9.2, 1.5, "Investment", color="#5b3a8a", fontsize=8, fontweight="bold")
    ax.set_title("Circular flow of income: two-sector model with saving and investment", loc="left")
    save(f, "e_circular")


def pf_tree():
    f, ax = fig(2.7)
    ax.set_xlim(0, 12); ax.set_ylim(0, 6.2); ax.axis("off")
    box(ax, 6, 5.5, 3.8, 0.8, "PUBLIC FINANCE", "#0e3a66", NAVY, 9, True); ax.texts[-1].set_color("white")
    for x, t in ((2, "Public revenue"), (6, "Budget"), (10, "Public expenditure")):
        box(ax, x, 3.9, 3.2, 0.8, t, "#eaf1fa", NAVY, 8.6, True); arr(ax, (6, 5.1), (x, 4.3), style="-")
    for x, t in ((1.1, "Tax"), (3.4, "Non-tax")):
        box(ax, x, 2.2, 1.9, 0.75, t, "#fff3df", ORANGE, 8.2); arr(ax, (2, 3.5), (x, 2.6), style="-")
    for x, t in ((8.7, "Current"), (10.9, "Capital")):
        box(ax, x, 2.2, 1.9, 0.75, t, "#e7f4ea", GREEN, 8.2); arr(ax, (10, 3.5), (x, 2.6), style="-")
    ax.text(1.1, 1.35, "direct: PIT, CIT, BIT\nindirect: sales tax,\nexcise, customs", ha="center", va="top", fontsize=6.9)
    ax.text(3.4, 1.35, "fees, commercial,\ngrants, borrowing", ha="center", va="top", fontsize=6.9)
    ax.text(6, 3.0, "types: annual and\nsupplementary", ha="center", va="top", fontsize=7.2)
    ax.text(8.7, 1.35, "salaries, defence,\nmedicine, interest,\nsubsidies", ha="center", va="top", fontsize=6.9)
    ax.text(10.9, 1.35, "roads, bridges,\nschools, hospitals,\nhydropower plants", ha="center", va="top", fontsize=6.9)
    save(f, "e_pf_tree")


def gnh():
    f, ax = fig(3.5)
    ax.set_xlim(0, 12); ax.set_ylim(0, 7.4); ax.axis("off")
    box(ax, 6, 6.7, 5.4, 0.8, "GROSS NATIONAL HAPPINESS", NAVY, NAVY, 9, True); ax.texts[-1].set_color("white")
    pil = [("Good\ngovernance", 1.6), ("Sustainable &\nequitable socio-\neconomic dev.", 4.5), ("Preservation &\npromotion of\nculture", 7.5), ("Environmental\nconservation", 10.4)]
    for t, x in pil:
        box(ax, x, 5.0, 2.7, 1.5, t, "#eaf1fa", NAVY, 7.8, True); arr(ax, (6, 6.3), (x, 5.8), style="-")
    ax.text(6, 3.7, "Nine domains of GNH", ha="center", fontsize=9, fontweight="bold", color=NAVY)
    dom = ["Good governance", "Community vitality", "Health", "Education", "Psychological\nwellbeing", "Cultural diversity\n& resilience", "Time use", "Ecological diversity\n& resilience", "Living standards"]
    for i, d in enumerate(dom):
        r, c = divmod(i, 5) if i < 5 else (1, i - 5)
        x = 1.2 + c * 2.4 + (0 if r == 0 else 1.2); y = 2.8 if r == 0 else 1.2
        box(ax, x, y, 2.25, 1.05, d, "#e7f4ea", GREEN, 7.2)
    save(f, "e_gnh")


def bop():
    f, ax = fig(3.2)
    ax.set_xlim(0, 12); ax.set_ylim(0, 6.6); ax.axis("off")
    box(ax, 6, 5.9, 5.6, 0.8, "BALANCE OF PAYMENTS (BoP)", NAVY, NAVY, 9, True); ax.texts[-1].set_color("white")
    cols = [(2.0, "CURRENT ACCOUNT", "goods (visible) and\nservices (invisible),\nincome, current transfers\n→ includes balance of trade", "#fff3df", ORANGE),
            (6.0, "CAPITAL ACCOUNT", "capital transfers,\nnon-produced,\nnon-financial assets", "#eaf1fa", BLUE),
            (10.0, "FINANCIAL ACCOUNT", "direct investment,\nportfolio investment,\nreserve assets", "#e7f4ea", GREEN)]
    for x, t, d, fc, ec in cols:
        box(ax, x, 4.3, 3.4, 0.8, t, fc, ec, 8.2, True); arr(ax, (6, 5.5), (x, 4.7), style="-")
        ax.text(x, 3.6, d, ha="center", va="top", fontsize=7.6)
    box(ax, 3.0, 0.9, 4.8, 1.0, "SURPLUS: receipts > payments\n(credit > debit)  favourable", "#e7f4ea", GREEN, 7.8)
    box(ax, 9.0, 0.9, 4.8, 1.0, "DEFICIT: payments > receipts\n(credit < debit)  unfavourable", "#fbe4e2", RED, 7.8)
    save(f, "e_bop")


if __name__ == "__main__":
    for fn in (wage_eq, supply_shift, interest, demand_shift, labour_sched, bar_gdp, pie_exports, line_gdp, trade25, circular, pf_tree, gnh, bop):
        fn()
    print("ok", len(list(OUT.glob("*.svg"))))
