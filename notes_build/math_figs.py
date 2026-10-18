#!/usr/bin/env python3
"""Maths diagrams -> figs_m/*.svg (matplotlib, real geometry)."""
import math, pathlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Arc, Rectangle, FancyArrowPatch

OUT = pathlib.Path(__file__).parent / "figs_m"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"svg.fonttype": "none", "font.family": "DejaVu Sans", "font.size": 8.4, "axes.linewidth": 0.8, "axes.titlesize": 9, "axes.titleweight": "bold", "axes.titlecolor": "#0e3a66"})
NAVY, RED, GREEN, ORANGE, GREY, BLUE = "#0e3a66", "#b3211b", "#2a7a3a", "#b36200", "#777", "#1f5fa8"
W = 5.7


def fig(h, ncols=1, **kw):
    f, ax = plt.subplots(1, ncols, figsize=(W, h), **kw)
    return f, ax


def save(f, name):
    f.tight_layout(pad=0.6)
    f.savefig(OUT / f"{name}.svg", format="svg")
    plt.close(f)


def grid_axes(ax, xlim, ylim, xt=None, yt=None, minor=True):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.axhline(0, color="#222", lw=1); ax.axvline(0, color="#222", lw=1)
    ax.grid(True, color="#ddd", lw=0.5)
    if xt is not None: ax.set_xticks(xt)
    if yt is not None: ax.set_yticks(yt)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.spines["left"].set_position("zero"); ax.spines["bottom"].set_position("zero")


def quad_2025_5d():
    f, ax = fig(3.0)
    x = np.linspace(-2.2, 4.2, 300); y = -(x + 1) * (x - 3)
    grid_axes(ax, (-2.5, 4.5), (-3, 5.5), range(-2, 5), range(-3, 6))
    ax.plot(x, y, color=BLUE, lw=2)
    for px, py, t, dx, dy in ((-1, 0, "(-1, 0)", -0.3, -0.7), (3, 0, "(3, 0)", 0.1, -0.7), (1, 4, "vertex (1, 4)", 0.15, 0.2), (0, 3, "y-intercept (0, 3)", 0.15, 0.2)):
        ax.plot(px, py, "o", color=RED, ms=4)
        ax.annotate(t, (px, py), (px + dx, py + dy), fontsize=7.6, color=RED)
    ax.axvline(1, color=GREEN, lw=1, ls="--"); ax.text(1.08, -2.6, "axis of symmetry x = 1", color=GREEN, fontsize=7.4)
    ax.set_title("f(x) = -(x + 1)(x - 3):  opens downward (a = -1)")
    save(f, "m_q25_5d")


def line_2025_6a():
    f, ax = fig(2.9)
    grid_axes(ax, (-1.5, 8.5), (-1, 6.5), range(-1, 9), range(0, 7))
    x = np.array([-1.5, 8.5]); ax.plot(x, 5 - 2 * x / 3, color=BLUE, lw=2)
    ax.plot([0, 6], [5, 1], "o", color=RED, ms=4)
    ax.annotate("y-intercept (0, 5)", (0, 5), (0.4, 5.5), fontsize=8, color=RED)
    ax.plot([0, 6, 6], [5, 5, 1], color=GREEN, lw=1.2, ls="--")
    ax.text(3, 5.12, "run = 6", color=GREEN, ha="center", fontsize=8); ax.text(6.1, 3, "rise = -4", color=GREEN, fontsize=8)
    ax.set_title("Slope = rise / run = -4 / 6 = -2/3;  y-intercept = 5")
    save(f, "m_line_25_6a")


def scatter_2025_8b():
    mx = [37, 65, 18, 76, 38, 40, 66, 93, 52, 75, 48]; en = [75, 45, 85, 19, 85, 69, 54, 34, 29, 32, 56]
    f, ax = fig(3.1)
    ax.scatter(mx, en, color=BLUE, s=22, zorder=3)
    m, c = np.polyfit(mx, en, 1)
    xx = np.array([10, 100]); ax.plot(xx, m * xx + c, color=RED, lw=1.6, label="line of best fit")
    ax.plot([60, 60, 0], [0, m * 60 + c, m * 60 + c], color=GREEN, lw=1, ls="--")
    ax.plot(60, m * 60 + c, "o", color=GREEN, ms=5)
    ax.annotate(f"Maths 60  ->  English about {m*60+c:.0f}", (60, m * 60 + c), (62, 75), fontsize=8, color=GREEN, arrowprops=dict(arrowstyle="->", color=GREEN))
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.set_xlabel("Mathematics mark"); ax.set_ylabel("English mark"); ax.grid(True, color="#ddd", lw=0.5)
    ax.set_title("Strong negative correlation (r about -0.84)"); ax.legend(loc="upper right", fontsize=7.6, frameon=False)
    save(f, "m_scatter_25_8b")


def box_pair(ax, stats, labels, y0=0):
    pass


def box_2025_2c():
    f, ax = fig(2.2)
    A = dict(mn=1, q1=2.9, med=4.4, q3=5.9, mx=8.8); B = dict(mn=2.2, q1=3.5, med=4.4, q3=5.2, mx=6.5)
    for y, d, lab, col in ((2, A, "Source A", BLUE), (0.6, B, "Source B", ORANGE)):
        ax.plot([d["mn"], d["q1"]], [y, y], color=col, lw=1.5); ax.plot([d["q3"], d["mx"]], [y, y], color=col, lw=1.5)
        ax.add_patch(Rectangle((d["q1"], y - 0.35), d["q3"] - d["q1"], 0.7, fc="white", ec=col, lw=1.6))
        ax.plot([d["med"], d["med"]], [y - 0.35, y + 0.35], color=col, lw=2.2)
        for k in ("mn", "mx"): ax.plot([d[k], d[k]], [y - 0.15, y + 0.15], color=col, lw=1.5)
        ax.text(0.2, y, lab, ha="right", va="center", fontsize=8.4, color=col, weight="bold")
    ax.set_xlim(-1.2, 10.5); ax.set_ylim(-0.3, 2.9); ax.set_yticks([]); ax.set_xticks(range(0, 11)); ax.grid(True, axis="x", color="#ddd", lw=0.5)
    for s in ("left", "top", "right"): ax.spines[s].set_visible(False)
    ax.text(5.6, 2.55, "A: range about 8, IQR about 3", fontsize=7.8, color=BLUE); ax.text(5.6, 1.15, "B: range about 4, IQR about 2  (less spread)", fontsize=7.8, color=ORANGE)
    ax.set_title("Income from sources A and B"); save(f, "m_box_25_2c")


def box_2024_7a():
    f, ax = fig(1.9)
    d = dict(mn=32, q1=58, med=65, q3=74, mx=89)
    y = 1
    ax.plot([d["mn"], d["q1"]], [y, y], color=BLUE, lw=1.5); ax.plot([d["q3"], d["mx"]], [y, y], color=BLUE, lw=1.5)
    ax.add_patch(Rectangle((d["q1"], y - 0.4), d["q3"] - d["q1"], 0.8, fc="#c9d7ff", ec=BLUE, lw=1.6)); ax.plot([d["med"]] * 2, [y - 0.4, y + 0.4], color=NAVY, lw=2.4)
    for k in ("mn", "mx"): ax.plot([d[k]] * 2, [y - 0.2, y + 0.2], color=BLUE, lw=1.6)
    for k, lab in (("mn", "min 32"), ("q1", "Q1 58"), ("med", "median 65"), ("q3", "Q3 74"), ("mx", "max 89")):
        ax.text(d[k], y + 0.62 if k != "q1" else y - 0.75, lab, ha="center", fontsize=7.8, color=RED)
    ax.set_xlim(28, 94); ax.set_ylim(0, 2); ax.set_yticks([]); ax.set_xticks(range(30, 95, 5)); ax.grid(True, axis="x", color="#ddd", lw=0.5)
    for s in ("left", "top", "right"): ax.spines[s].set_visible(False)
    ax.set_title("Midterm Mathematics marks (20 students): values read from the plot"); save(f, "m_box_24_7a")


def scatter_2024_9b():
    hrs = [0, 2, 5, 6, 8, 10, 13, 14, 15, 16, 18, 25]; sc = [20, 28, 23, 45, 32, 63, 52, 60, 58, 68, 69, 80]
    f, ax = fig(3.0)
    ax.scatter(hrs, sc, color=BLUE, s=22, zorder=3); m, c = np.polyfit(hrs, sc, 1)
    ax.plot([0, 26], [c, m * 26 + c], color=RED, lw=1.6)
    ax.set_xlim(0, 27); ax.set_ylim(0, 90); ax.set_xlabel("Hours of revision"); ax.set_ylabel("Exam score"); ax.grid(True, color="#ddd", lw=0.5)
    ax.set_title("Strong positive correlation (r about 0.93)"); save(f, "m_scatter_24_9b")


def scatter_2023_6c():
    age = [20, 22, 30, 30, 34, 26, 26, 18, 36, 40]; hr = [15, 11, 6, 7, 6, 14, 8, 16, 3, 3]
    f, ax = fig(3.0)
    ax.scatter(age, hr, color=BLUE, s=22, zorder=3); m, c = np.polyfit(age, hr, 1)
    ax.plot([16, 42], [m * 16 + c, m * 42 + c], color=RED, lw=1.6)
    ax.set_xlim(14, 44); ax.set_ylim(0, 18); ax.set_xlabel("Age (years)"); ax.set_ylabel("Hours of activity per week"); ax.grid(True, color="#ddd", lw=0.5)
    ax.set_title("Strong negative correlation (r about -0.92)"); save(f, "m_scatter_23_6c")


def construct_2025_4b():
    A = np.array([0.0, 0.0]); B = np.array([7.0, 0.0])
    # angle A=45, angle B=60 -> C
    a, b = math.radians(45), math.radians(60)
    # intersection of ray from A at 45 deg and ray from B at 120 deg
    t = 7 * math.sin(b) / math.sin(a + b)
    C = A + t * np.array([math.cos(a), math.sin(a)])
    f, ax = fig(3.6)
    ax.add_patch(Polygon([A, B, C], fill=False, ec=NAVY, lw=2))
    # perpendicular bisectors of AB and AC
    def pb(P, Q, col):
        M = (P + Q) / 2; d = Q - P; n = np.array([-d[1], d[0]]); n = n / np.linalg.norm(n)
        ax.plot([M[0] - 3.2 * n[0], M[0] + 3.2 * n[0]], [M[1] - 3.2 * n[1], M[1] + 3.2 * n[1]], color=col, lw=1, ls="--")
        ax.plot(*M, "s", color=col, ms=3)
        return M, n
    M1, n1 = pb(A, B, GREEN); M2, n2 = pb(A, C, ORANGE)
    sol = np.linalg.solve(np.array([n1, -n2]).T, M2 - M1); O = M1 + sol[0] * n1
    R = np.linalg.norm(O - A)
    ax.add_patch(Circle(O, R, fill=False, ec=RED, lw=1.6)); ax.plot(*O, "o", color=RED, ms=4)
    ax.annotate("O (circumcentre)", O, O + np.array([1.6, 1.0]), fontsize=8, color=RED, arrowprops=dict(arrowstyle="->", color=RED))
    for P, t_, d in ((A, "A", (-0.4, -0.5)), (B, "B", (0.15, -0.5)), (C, "C", (0.15, 0.2))): ax.text(P[0] + d[0], P[1] + d[1], t_, fontsize=10, weight="bold", color=NAVY)
    ax.text(3.5, -0.75, "AB = 7 cm", ha="center", fontsize=8); ax.text(0.8, 0.28, "45°", fontsize=8); ax.text(6.0, 0.22, "60°", fontsize=8)
    ax.text(O[0] + R * 0.1, O[1] - R - 0.4, f"radius = {R:.2f} cm", fontsize=8, color=RED)
    ax.set_aspect("equal"); ax.set_xlim(-1.5, 9.8); ax.set_ylim(O[1] - R - 1, O[1] + R + 0.5); ax.axis("off")
    ax.set_title("Circumcircle through A, B, C: where the perpendicular bisectors meet"); save(f, "m_construct_25_4b")


def construct_2024_4b():
    B = np.array([0.0, 0.0]); C = np.array([5.5, 0.0]); A = 6 * np.array([math.cos(math.radians(120)), math.sin(math.radians(120))])
    f, ax = fig(4.0)
    ax.add_patch(Polygon([A, B, C], fill=False, ec=NAVY, lw=2))
    def pb(P, Q, col, L=4.2):
        M = (P + Q) / 2; d = Q - P; n = np.array([-d[1], d[0]]); n = n / np.linalg.norm(n)
        ax.plot([M[0] - L * n[0], M[0] + L * n[0]], [M[1] - L * n[1], M[1] + L * n[1]], color=col, lw=1, ls="--"); ax.plot(*M, "s", color=col, ms=3); return M, n
    M1, n1 = pb(B, C, GREEN, 6); M2, n2 = pb(A, B, ORANGE, 6)
    sol = np.linalg.solve(np.array([n1, -n2]).T, M2 - M1); O = M1 + sol[0] * n1; R = np.linalg.norm(O - B)
    ax.add_patch(Circle(O, R, fill=False, ec=RED, lw=1.6)); ax.plot(*O, "o", color=RED, ms=4)
    ax.annotate("O is OUTSIDE the triangle\n(angle B = 120° is obtuse)", O, O + np.array([-4.2, -1.2]), fontsize=8, color=RED, arrowprops=dict(arrowstyle="->", color=RED))
    for P, t_, d in ((A, "A", (-0.5, 0.2)), (B, "B", (-0.5, -0.6)), (C, "C", (0.2, -0.5))): ax.text(P[0] + d[0], P[1] + d[1], t_, fontsize=10, weight="bold", color=NAVY)
    ax.text(2.75, -0.5, "BC = 5.5 cm", ha="center", fontsize=8); ax.text(-3.6, 1.8, "AB = 6 cm", fontsize=8); ax.text(0.45, 0.25, "120°", fontsize=8)
    ax.set_aspect("equal"); ax.set_xlim(O[0] - R - 0.5, O[0] + R + 0.5); ax.set_ylim(O[1] - R - 0.5, O[1] + R + 0.5); ax.axis("off")
    ax.set_title(f"Circumcircle of an obtuse triangle (radius {R:.2f} cm)"); save(f, "m_construct_24_4b")


def centroid_2023_3c():
    Y = np.array([0.0, 0.0]); Z = np.array([8.3, 0.0]); X = 6.9 * np.array([math.cos(math.radians(65)), math.sin(math.radians(65))])
    G = (X + Y + Z) / 3
    f, ax = fig(3.2)
    ax.add_patch(Polygon([X, Y, Z], fill=False, ec=NAVY, lw=2))
    for P, Q, col in ((X, (Y + Z) / 2, GREEN), (Y, (X + Z) / 2, ORANGE), (Z, (X + Y) / 2, BLUE)):
        ax.plot([P[0], Q[0]], [P[1], Q[1]], color=col, lw=1.3, ls="--"); ax.plot(*Q, "s", color=col, ms=3)
    ax.plot(*G, "o", color=RED, ms=5); ax.annotate("G (centroid)\n2/3 along each median", G, G + np.array([2.2, 1.6]), fontsize=8, color=RED, arrowprops=dict(arrowstyle="->", color=RED))
    for P, t_, d in ((X, "X", (-0.4, 0.15)), (Y, "Y", (-0.5, -0.5)), (Z, "Z", (0.15, -0.5))): ax.text(P[0] + d[0], P[1] + d[1], t_, fontsize=10, weight="bold", color=NAVY)
    ax.text(4.1, -0.55, "YZ = 8.3 cm", ha="center", fontsize=8); ax.text(0.2, 3.5, "XY = 6.9 cm", fontsize=8, rotation=65); ax.text(0.6, 0.25, "65°", fontsize=8)
    ax.set_aspect("equal"); ax.set_xlim(-1.2, 9.6); ax.set_ylim(-1.2, 7); ax.axis("off")
    ax.set_title("Medians join each vertex to the midpoint of the opposite side"); save(f, "m_centroid_23_3c")


def sales_2024_8c():
    f, ax = fig(3.0)
    x = np.linspace(-5, 55, 300); y = (20 + x) * (50 - x)
    ax.plot(x, y, color=BLUE, lw=2)
    x2 = np.linspace(0, 50, 100); ax.plot(x2, (20 + x2) * (50 - x2), color=RED, lw=2.4)
    for px, py, t, dx, dy in ((15, 1225, "maximum (15, 1225)", 3, 20), (0, 1000, "(0, 1000)", 2, 30), (50, 0, "(50, 0)", -8, 90)):
        ax.plot(px, py, "o", color=RED, ms=4); ax.annotate(t, (px, py), (px + dx, py + dy), fontsize=7.8, color=RED)
    ax.axhline(0, color="#222", lw=1); ax.axvline(0, color="#222", lw=1); ax.grid(True, color="#ddd", lw=0.5)
    ax.set_xlim(-8, 55); ax.set_ylim(-150, 1400); ax.set_xlabel("x = number of Nu 1 increases"); ax.set_ylabel("S(x) (Nu)")
    ax.set_title("S(x) = (20 + x)(50 - x): realistic part drawn in red (0 ≤ x ≤ 50)"); save(f, "m_sales_24_8c")


def line_2024_6a():
    f, ax = fig(2.9)
    grid_axes(ax, (-1.5, 5), (-2, 7.5), range(-1, 6), range(-2, 8))
    x = np.array([-1.2, 4.6]); ax.plot(x, 6 - 2.5 * x, color=BLUE, lw=2)
    ax.plot([0, 2.4], [6, 0], "o", color=RED, ms=4)
    ax.annotate("(0, 6)  y-intercept", (0, 6), (0.3, 6.6), fontsize=8, color=RED); ax.annotate("(2.4, 0)  x-intercept", (2.4, 0), (2.7, 0.9), fontsize=8, color=RED)
    ax.set_title("y = -(5/2)x + 6   (slope -2.5, y-intercept 6)"); save(f, "m_line_24_6a")


def quad_2023_8b():
    f, ax = fig(3.0)
    x = np.linspace(-2.4, 3.4, 300); y = -2 * (x + 1) * (x - 2)
    grid_axes(ax, (-3, 4), (-6, 6), range(-3, 5), range(-6, 7, 2))
    ax.plot(x, y, color=BLUE, lw=2)
    for px, py, t, dx, dy in ((-1, 0, "(-1, 0)", -0.5, 0.5), (2, 0, "(2, 0)", 0.2, 0.5), (0.5, 4.5, "vertex (0.5, 4.5)", 0.2, 0.3), (0, 4, "(0, 4)", -1.1, 0.4)):
        ax.plot(px, py, "o", color=RED, ms=4); ax.annotate(t, (px, py), (px + dx, py + dy), fontsize=7.8, color=RED)
    ax.axvline(0.5, color=GREEN, lw=1, ls="--")
    ax.set_title("f(x) = -2(x + 1)(x - 2):  opens downward (a = -2)"); save(f, "m_q23_8b")


def hexagon_2023_9c():
    f, ax = fig(3.1)
    # hexagon of side 2 made of 24 triangles; centre at origin
    def tri(p, q, r): return np.array([p, q, r])
    s = 1.0
    pts = lambda i, j: np.array([i * s + j * s / 2, j * s * math.sqrt(3) / 2])
    tris = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            for up in (True, False):
                if up: T = [pts(i, j), pts(i + 1, j), pts(i, j + 1)]
                else: T = [pts(i + 1, j), pts(i + 1, j + 1), pts(i, j + 1)]
                c = sum(T) / 3
                # inside hexagon of "radius" 2: check hex distance
                ang = np.degrees(np.arctan2(c[1], c[0])) % 360
                d = max(abs(c[0]) * math.sqrt(3) / 2 + abs(c[1]) / 2, abs(c[1]))
                if d < 1.74: tris.append((np.array(T), c))
    # shade the six triangles touching the centre? use outer ring ones: choose by sector symmetric set: central six
    shaded = []
    for T, c in tris:
        if np.linalg.norm(c) < 0.7: shaded.append(True)
        else: shaded.append(False)
    for (T, c), sh in zip(tris, shaded):
        ax.add_patch(Polygon(T, fc="#9fc3f0" if sh else "white", ec="#444", lw=0.8))
    ax.plot(0, 0, "o", color=RED, ms=4); ax.annotate("centre of rotation", (0, 0), (1.1, 0.05), fontsize=7.8, color=RED, arrowprops=dict(arrowstyle="->", color=RED))
    ax.set_aspect("equal"); ax.set_xlim(-2.3, 2.3); ax.set_ylim(-1.9, 1.9); ax.axis("off")
    ax.set_title("Six triangles round the centre: order of turn symmetry 6 (turn 60°)"); save(f, "m_hex_23_9c")


def star_2025_3d():
    f, axs = fig(2.7, 2)
    ax = axs[0]
    # order 4: square frame made by rotating L-corner
    ax.plot([0, 0, 2], [2, 4, 4], color=NAVY, lw=2.2)
    ax.plot([4, 4, 2], [2, 0, 0], color=BLUE, lw=2, ls="--"); ax.plot([2, 4, 4], [4, 4, 2], color=BLUE, lw=2, ls="--"); ax.plot([0, 0, 2], [2, 0, 0], color=BLUE, lw=2, ls="--")
    ax.plot(2, 2, "o", color=RED, ms=5); ax.text(2.15, 2.15, "centre", color=RED, fontsize=8)
    ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-0.5, 4.5); ax.set_ylim(-0.5, 4.5); ax.set_title("(i) turn 90° three times\n(navy = given part, dashed = added)", fontsize=8.4)
    ax = axs[1]
    n = 9; ang = [math.radians(90 + k * 360 / n) for k in range(n)]
    for k in range(n):
        a = ang[k]; tip = np.array([math.cos(a), math.sin(a)]); l = np.array([math.cos(a - math.radians(20)), math.sin(a - math.radians(20))]) * 0.45; r = np.array([math.cos(a + math.radians(20)), math.sin(a + math.radians(20))]) * 0.45
        shaded = k % 3 in (0, 1)
        ax.add_patch(Polygon([tip, r, l], fc="#9fc3f0" if shaded else "white", ec="#333", lw=1))
        ax.text(tip[0] * 1.17, tip[1] * 1.17, str(k + 1), ha="center", va="center", fontsize=7.6, color=RED)
    ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.4, 1.4); ax.set_title("(ii) shade points 1, 2, 4, 5, 7, 8\n(pairs repeat every 120°): order 3", fontsize=8.4)
    save(f, "m_star_25_3d")


def venn_2025_16():
    f, ax = fig(2.4)
    ax.add_patch(Rectangle((0, 0), 10, 5.5, fill=False, ec="#222", lw=1.2))
    ax.add_patch(Circle((3.9, 2.8), 1.9, fc="#c9d7ff", ec=BLUE, alpha=0.7)); ax.add_patch(Circle((6.0, 2.8), 1.9, fc="#ffd9b0", ec=ORANGE, alpha=0.7))
    ax.text(2.9, 2.8, "12", ha="center", va="center", fontsize=10); ax.text(5.0, 2.8, "25", ha="center", va="center", fontsize=10, weight="bold"); ax.text(7.0, 2.8, "78", ha="center", va="center", fontsize=10)
    ax.text(0.6, 0.6, "25", fontsize=10); ax.text(3.0, 4.9, "M (music)", color=BLUE, fontsize=8.5); ax.text(6.0, 4.9, "S (sport)", color=ORANGE, fontsize=8.5)
    ax.text(10.4, 2.8, "P(M | S) = 25 / (25 + 78)\n= 25/103", fontsize=9, color=RED, va="center")
    ax.set_xlim(0, 16); ax.set_ylim(0, 5.7); ax.axis("off"); ax.set_title("Given S, the sample space is only the S circle (103 students)"); save(f, "m_venn_25_16")


def digraph_2024_3b():
    f, ax = fig(2.9)
    P = {"A": np.array([0.0, 2.2]), "B": np.array([4.0, 2.2]), "C": np.array([2.0, 0.0])}
    for k, v in P.items():
        ax.add_patch(Circle(v, 0.22, fc="white", ec=NAVY, lw=1.6)); ax.text(v[0], v[1], k, ha="center", va="center", weight="bold", color=NAVY)
    def edge(p, q, rad=0.0):
        ax.add_patch(FancyArrowPatch(P[p], P[q], connectionstyle=f"arc3,rad={rad}", arrowstyle="-", lw=1.6, color="#333", shrinkA=9, shrinkB=9))
    edge("A", "B"); edge("A", "C"); edge("B", "C"); edge("A", "C", 0.55); edge("B", "C", -0.55)
    ax.text(2.0, 2.45, "1", color=RED, ha="center", fontsize=9); ax.text(0.55, 1.0, "1", color=RED, fontsize=9); ax.text(3.45, 1.0, "1", color=RED, fontsize=9); ax.text(-0.25, 0.7, "1", color=RED, fontsize=9); ax.text(4.05, 0.7, "1", color=RED, fontsize=9)
    ax.set_xlim(-1, 5.2); ax.set_ylim(-0.7, 3); ax.axis("off")
    ax.text(4.6, 2.9, "no arrowheads in my copy:\nevery link is two-way", fontsize=7.4, color=GREY, ha="right", va="top")
    ax.set_title("A–B: 1 link; A–C: 2 links; B–C: 2 links"); save(f, "m_digraph_24_3b")


def trig_quadrants():
    f, ax = fig(2.9)
    th = np.linspace(0, 2 * np.pi, 200); ax.plot(np.cos(th), np.sin(th), color=NAVY, lw=1.5)
    ax.axhline(0, color="#222", lw=1); ax.axvline(0, color="#222", lw=1)
    txt = {(0.45, 0.45): "I  (0°–90°)\nALL positive", (-0.45, 0.45): "II  (90°–180°)\nSine positive", (-0.45, -0.45): "III  (180°–270°)\nTangent positive", (0.45, -0.45): "IV  (270°–360°)\nCosine positive"}
    for (x, y), t in txt.items(): ax.text(x, y, t, ha="center", va="center", fontsize=8, color=RED if x > 0 and y > 0 else NAVY)
    ang = math.radians(150); ax.plot([0, math.cos(ang)], [0, math.sin(ang)], color=GREEN, lw=2); ax.add_patch(Arc((0, 0), 0.5, 0.5, theta1=0, theta2=150, color=GREEN)); ax.text(0.28, 0.3, "5π/6 = 150°", color=GREEN, fontsize=7.6)
    ax.set_aspect("equal"); ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.2, 1.2); ax.axis("off")
    for t, x, y in (("0°/360°", 1.2, 0.08), ("90°", 0.02, 1.1), ("180°", -1.3, 0.08), ("270°", 0.02, -1.15)): ax.text(x, y, t, fontsize=7.6, ha="center")
    ax.set_title("Signs of trigonometric ratios (ASTC: All, Sin, Tan, Cos)"); save(f, "m_trig_quad")


def trig_graphs():
    f, axs = fig(2.3, 3)
    x = np.linspace(-2 * np.pi, 2 * np.pi, 600)
    for ax, fn, name, ylim in ((axs[0], np.sin, "y = sin x", (-1.6, 1.6)), (axs[1], np.cos, "y = cos x", (-1.6, 1.6)), (axs[2], np.tan, "y = tan x", (-3, 3))):
        y = fn(x)
        if name.endswith("tan x"): y[np.abs(y) > 20] = np.nan
        ax.plot(x, y, color=BLUE, lw=1.8); ax.axhline(0, color="#222", lw=0.8); ax.axvline(0, color="#222", lw=0.8); ax.set_ylim(*ylim); ax.grid(True, color="#ddd", lw=0.5)
        ax.set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi]); ax.set_xticklabels(["-2π", "-π", "0", "π", "2π"], fontsize=7); ax.tick_params(labelsize=7); ax.set_title(name, fontsize=8.4)
    axs[0].text(0.15, -1.4, "through 0;\nmax at π/2", fontsize=6.8, color=RED); axs[1].text(0.15, -1.4, "starts at 1\n(max at 0)", fontsize=6.8, color=RED); axs[2].text(0.15, -2.7, "asymptotes at\n±π/2, ±3π/2", fontsize=6.8, color=RED)
    save(f, "m_trig_graphs")


def cut_box_2025_6d():
    f, axs = fig(2.7, 2)
    ax = axs[0]
    ax.add_patch(Rectangle((0, 0), 9, 9, fill=False, ec=NAVY, lw=2))
    for (cx, cy) in ((0, 0), (7, 0), (0, 7), (7, 7)): ax.add_patch(Rectangle((cx, cy), 2, 2, fc="#ffd9d9", ec=RED, lw=1))
    ax.text(4.5, 4.5, "base (x - 4) by (x - 4)\nwith x = 9: 5 by 5", ha="center", va="center", fontsize=8)
    ax.text(4.5, -0.9, "x = 9 cm", ha="center", fontsize=8.4, color=NAVY); ax.text(1, 1, "2", ha="center", va="center", fontsize=8, color=RED)
    ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-0.5, 9.5); ax.set_ylim(-1.5, 9.5); ax.set_title("Sheet: cut 2 cm squares", fontsize=8.4)
    ax = axs[1]
    ax.text(0.5, 0.78, "Volume = length × width × height", ha="center", fontsize=8.4, transform=ax.transAxes)
    ax.text(0.5, 0.58, "50 = (x - 4)(x - 4)(2)", ha="center", fontsize=9, transform=ax.transAxes, color=NAVY)
    ax.text(0.5, 0.40, "(x - 4)² = 25", ha="center", fontsize=9, transform=ax.transAxes)
    ax.text(0.5, 0.22, "x - 4 = 5  →  x = 9 cm", ha="center", fontsize=9, transform=ax.transAxes, color=RED, weight="bold")
    ax.axis("off"); save(f, "m_box_25_6d")


def altitude_2025_8a():
    f, ax = fig(2.8)
    B = np.array([0.0, 0.0]); C = np.array([5.0, 0.0]); A = np.array([0.0, 3.2])
    AC = C - A; t = np.dot(B - A, AC) / np.dot(AC, AC); D = A + t * AC
    ax.add_patch(Polygon([A, B, C], fill=False, ec=NAVY, lw=2)); ax.plot([B[0], D[0]], [B[1], D[1]], color=RED, lw=1.8)
    ax.add_patch(Rectangle((0, 0), 0.25, 0.25, fill=False, ec=NAVY, lw=1))
    d = (D - A) / np.linalg.norm(D - A); n = np.array([-d[1], d[0]])
    for P, t_, dd in ((A, "A", (-0.35, 0.1)), (B, "B", (-0.4, -0.4)), (C, "C", (0.12, -0.4)), (D, "D", (0.12, 0.1))): ax.text(P[0] + dd[0], P[1] + dd[1], t_, fontsize=10, weight="bold", color=NAVY)
    ax.text(0.45, 0.12, "(3x - 5)°", fontsize=8, color=GREEN); ax.text(3.35, 0.12, "(2x + 15)°", fontsize=8, color=ORANGE)
    ax.text(1.2, 3.0, "∠B = 90°;  BD ⊥ AC  →  triangle BDC has a right angle at D", fontsize=7.6, color=RED)
    ax.set_aspect("equal"); ax.set_xlim(-1, 6); ax.set_ylim(-0.8, 3.9); ax.axis("off"); ax.set_title("(3x - 5) + (2x + 15) = 90  →  x = 16"); save(f, "m_alt_25_8a")


def skew_2025_20():
    f, axs = fig(2.4, 2)
    ax = axs[0]
    x = np.linspace(0, 10, 200); y = x * np.exp(-x / 1.5) * 1.0
    ax.fill_between(x, y, color="#c9d7ff", ec=BLUE); ax.set_title("Right-skewed histogram", fontsize=8.2); ax.set_xticks([]); ax.set_yticks([])
    ax = axs[1]
    ax.plot([1, 2.2], [1, 1], color=BLUE, lw=1.6); ax.plot([4.4, 9.5], [1, 1], color=BLUE, lw=1.6)
    ax.add_patch(Rectangle((2.2, 0.6), 2.2, 0.8, fc="white", ec=BLUE, lw=1.6)); ax.plot([2.8, 2.8], [0.6, 1.4], color=NAVY, lw=2.2)
    ax.text(5.9, 1.0, "right whisker longer", fontsize=7.6, color=RED, ha="center", va="bottom"); ax.text(2.8, 0.25, "median near Q1", fontsize=7.6, color=RED, ha="center")
    ax.set_xlim(0, 10); ax.set_ylim(0, 2); ax.axis("off"); ax.set_title("Box plot of the same data", fontsize=8.2)
    save(f, "m_skew_25_20")


def tent_2025_2():
    f, ax = fig(2.4)
    ax.add_patch(Polygon([[0, 0], [4, 0], [2, 3]], fc="#eaf3ff", ec=NAVY, lw=2))
    ax.plot([2, 2], [0, 3], color=RED, ls="--", lw=1.4); ax.text(2.1, 1.4, "pole h", color=RED, fontsize=8)
    ax.text(2, -0.4, "base 4 m", ha="center", fontsize=8); ax.text(0.5, 1.6, "5 m", fontsize=8, rotation=56); ax.text(3.35, 1.6, "5 m", fontsize=8, rotation=-56)
    ax.text(4.4, 1.4, "tent length 8 m", fontsize=8, color=BLUE)
    ax.text(4.4, 0.6, "SA = 2(½×4×h) + (5+5+4)×8\n136 = 4h + 112  →  h = 6 m", fontsize=8, color=NAVY)
    ax.set_aspect("equal"); ax.set_xlim(-0.4, 9.8); ax.set_ylim(-0.9, 3.4); ax.axis("off"); ax.set_title("2025 Q1(a)(ii): the tent is a triangular prism"); save(f, "m_tent_25_1")


def frustum_2023_6a():
    f, ax = fig(2.6)
    ax.add_patch(Polygon([[-8, 0], [8, 0], [4, 8], [-4, 8]], fc="#eaf3ff", ec=NAVY, lw=2))
    ax.plot([-8, 0, 8], [0, 16, 0], color=GREY, lw=1, ls="--"); ax.plot([0, 0], [0, 16], color=GREY, lw=0.8, ls=":")
    ax.text(0, 4, "frustum\nh = 8", ha="center", fontsize=8); ax.text(4, -1.5, "R = 8", ha="center", fontsize=8, color=RED); ax.text(2, 8.6, "r = 4", ha="center", fontsize=8, color=RED)
    ax.text(10, 12, "big cone: R = 8, h = 16\nsmall cone: r = 4, h = 8\nV = ⅓π(64)(16) - ⅓π(16)(8)\n= (1024π - 128π)/3\n≈ 938.3 cm³", fontsize=8, color=NAVY, va="top")
    ax.set_aspect("equal"); ax.set_xlim(-10, 26); ax.set_ylim(-3, 17); ax.axis("off"); ax.set_title("Frustum = big cone - small cone (similar triangles)"); save(f, "m_frustum_23_6a")


def vertical_line_2024_1():
    f, axs = fig(2.0, 4)
    th = np.linspace(0, 2 * np.pi, 100)
    shapes = [("A", np.cos(th) * 1.0, np.sin(th) * 0.6, "ellipse: fails"), ("B", -np.linspace(0, 1, 60) ** 2, np.linspace(-1, 1, 60), "sideways parabola: fails"), ("C", np.zeros(20), np.linspace(-1, 1, 20), "vertical line: fails"), ("D", np.linspace(-1, 1, 60), -np.linspace(-1, 1, 60) ** 2, "passes: a function")]
    for ax, (lab, x, y, t) in zip(axs, shapes):
        ax.plot(x, y, color=BLUE if lab == "D" else RED, lw=2); ax.axhline(0, color="#222", lw=0.8); ax.axvline(0, color="#222", lw=0.8)
        ax.set_title(f"{lab}: {t}", fontsize=7.2); ax.axis("off"); ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3)
    save(f, "m_vline_24_4")


def greenhouse_2025_7d():
    f, ax = fig(2.2)
    th = np.linspace(0, np.pi, 80); ax.plot(10 * np.cos(th), 10 * np.sin(th), color=NAVY, lw=2); ax.plot([-10, 10], [0, 0], color=NAVY, lw=2)
    ax.text(0, 4, "end view: semicircle\nradius r = 20 ÷ 2 = 10 m", ha="center", fontsize=8); ax.text(0, -2, "diameter 20 m", ha="center", fontsize=8, color=RED)
    ax.text(12.5, 7, "Roof = half of a cylinder's curved surface\n= ½ × 2πr × L = π × 10 × 80\n= 800π ≈ 2513.3 m²\nCost = 2513.3 × 15 ≈ Nu 37 699", fontsize=8, va="top", color=NAVY)
    ax.set_aspect("equal"); ax.set_xlim(-12, 42); ax.set_ylim(-4, 11); ax.axis("off"); ax.set_title("Greenhouse: arch of diameter 20 m, length 80 m"); save(f, "m_greenhouse_25_7d")


if __name__ == "__main__":
    for fn in (quad_2025_5d, line_2025_6a, scatter_2025_8b, box_2025_2c, box_2024_7a, scatter_2024_9b, scatter_2023_6c, construct_2025_4b, construct_2024_4b, centroid_2023_3c, sales_2024_8c, line_2024_6a, quad_2023_8b, hexagon_2023_9c, star_2025_3d, venn_2025_16, digraph_2024_3b, trig_quadrants, trig_graphs, cut_box_2025_6d, altitude_2025_8a, skew_2025_20, tent_2025_2, frustum_2023_6a, vertical_line_2024_1, greenhouse_2025_7d):
        fn()
    print(len(list(OUT.glob("*.svg"))), "figures")
