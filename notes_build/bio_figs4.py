#!/usr/bin/env python3
"""Biology diagrams, part 4: cell division, heredity, evolution, ecology."""
import math, textwrap
from bio_lib import *

RED_ = "#b3211b"
MAT, PAT = "#1f5fa8", "#c0392b"      # maternal (blue) and paternal (red) chromosomes


def arrow(x1, y1, x2, y2, c="#333", w=1.8):
    return L(x1, y1, x2, y2, c, w, None, True)


def chrom(cx, cy, l, col, rot=0, double=True, sw=3.6):
    """chromosome of half-length l centred at (cx,cy). double = two chromatids (X); single = one chromatid."""
    if double:
        a = 16
        d = (L(cx - l * math.sin(math.radians(a)), cy - l * math.cos(math.radians(a)), cx + l * math.sin(math.radians(a)), cy + l * math.cos(math.radians(a)), col, sw) +
             L(cx + l * math.sin(math.radians(a)), cy - l * math.cos(math.radians(a)), cx - l * math.sin(math.radians(a)), cy + l * math.cos(math.radians(a)), col, sw))
    else:
        d = L(cx, cy - l, cx, cy + l, col, sw)
    return f'<g transform="rotate({rot} {cx} {cy})" stroke-linecap="round">{d}</g>'


LONG, SHORT = 11, 7


def cell(cx, cy, r=34, nuc=False):
    s = C(cx, cy, r, "#fffdf6", "#7a6a3a", 1.5)
    if nuc:
        s += C(cx, cy, r - 8, "none", "#7a6a3a", 0.9).replace('stroke-width="0.9"', 'stroke-width="0.9" stroke-dasharray="3 2"')
    return s


def spindle(cx, cy, r=34):
    return L(cx - r + 2, cy, cx - 6, cy, "#aaa", 0.8) + L(cx + r - 2, cy, cx + 6, cy, "#aaa", 0.8)


def divisions():
    b = [T(235, 12, "Mitosis and meiosis for a cell with 4 chromosomes (2n = 4)", 9.5, fill=NAVY, weight="bold")]
    xs = [58, 174, 290, 406]
    rows = [(22, "MITOSIS (body cell): 1 division → 2 identical cells, 2n = 4", "#1f5fa8"),
            (126, "MEIOSIS I (germ cell): homologous chromosomes separate → 2 cells, n = 2", "#7a3b9b"),
            (230, "MEIOSIS II: chromatids separate → 4 different cells, n = 2", "#2a7a3a")]
    for (y0, title, col) in rows:
        b += [R(4, y0, 462, 100, "#fbfcfe", col, 1.1, 4), T(10, y0 + 10, title, 7.2, "start", col, "bold")]
    # ---- mitosis row
    cy = 22 + 48
    names = ["Prophase", "Metaphase", "Anaphase", "Telophase: 2 cells, 2n = 4"]
    cx = xs[0]
    b += [cell(cx, cy, 30, True)]
    for (dx, dy, l, c, r) in [(-10, -12, LONG, MAT, 30), (10, -10, LONG, PAT, -30), (-9, 10, SHORT, MAT, 60), (10, 11, SHORT, PAT, -50)]:
        b += [chrom(cx + dx, cy + dy, l, c, r)]
    cx = xs[1]; b += [cell(cx, cy, 30), spindle(cx, cy, 30)]
    for (dy, l, c) in [(-18, LONG, MAT), (-6, LONG, PAT), (7, SHORT, MAT), (19, SHORT, PAT)]:
        b += [chrom(cx, cy + dy, l, c, 90)]
    cx = xs[2]; b += [cell(cx, cy, 30), spindle(cx, cy, 30)]
    for side in (-1, 1):
        for (dy, l, c) in [(-17, LONG, MAT), (-6, LONG, PAT), (6, SHORT, MAT), (17, SHORT, PAT)]:
            b += [chrom(cx + side * 17, cy + dy, l * 0.7, c, 90, False)]
    b += [arrow(cx - 8, cy - 26, cx - 20, cy - 26, "#888", 1.2), arrow(cx + 8, cy - 26, cx + 20, cy - 26, "#888", 1.2)]
    cx = xs[3]
    b += [C(cx - 15, cy, 22, "#fffdf6", "#7a6a3a", 1.5), C(cx + 15, cy, 22, "#fffdf6", "#7a6a3a", 1.5)]
    for side in (-1, 1):
        for (dx, dy, l, c, r) in [(-6, -8, LONG * .7, MAT, 30), (6, -8, LONG * .7, PAT, -30), (-5, 8, SHORT * .7, MAT, 60), (7, 8, SHORT * .7, PAT, -50)]:
            b += [chrom(cx + side * 15 + dx * .8, cy + dy, l, c, r, False)]
    for i, n in enumerate(names):
        b += [T(xs[i], cy + 42, n, 6.8, fill="#222", weight="bold")]
    
    # ---- meiosis I row
    cy = 126 + 48
    cx = xs[0]; b += [cell(cx, cy, 30, True)]
    for (dx, dy, l, c) in [(-6, -12, LONG, MAT), (6, -12, LONG, PAT), (-6, 11, SHORT, MAT), (6, 11, SHORT, PAT)]:
        b += [chrom(cx + dx, cy + dy, l, c, 0)]
    b += [T(cx, cy - 31, "crossing over", 5.8, fill=RED_)]
    cx = xs[1]; b += [cell(cx, cy, 30), spindle(cx, cy, 30)]
    for (dx, dy, l, c) in [(-5, -13, LONG, MAT), (5, -13, LONG, PAT), (-5, 13, SHORT, MAT), (5, 13, SHORT, PAT)]:
        b += [chrom(cx + dx, cy + dy, l, c, 90)]
    cx = xs[2]; b += [cell(cx, cy, 30), spindle(cx, cy, 30)]
    for (dx, dy, l, c) in [(-16, -9, LONG, MAT), (-16, 11, SHORT, MAT), (16, -9, LONG, PAT), (16, 11, SHORT, PAT)]:
        b += [chrom(cx + dx, cy + dy, l, c, 90)]
    cx = xs[3]
    b += [C(cx - 15, cy, 22, "#fffdf6", "#7a6a3a", 1.5), C(cx + 15, cy, 22, "#fffdf6", "#7a6a3a", 1.5)]
    for (dx, dy, l, c) in [(-15, -6, LONG * .8, MAT), (-15, 10, SHORT * .8, MAT), (15, -6, LONG * .8, PAT), (15, 10, SHORT * .8, PAT)]:
        b += [chrom(cx + dx, cy + dy, l, c, 90)]
    for i, n in enumerate(["Prophase I", "Metaphase I", "Anaphase I: pairs split", "Telophase I: n = 2"]):
        b += [T(xs[i], cy + 42, n, 6.8, fill="#222", weight="bold")]
    
    # ---- meiosis II row
    cy = 230 + 48
    cx = xs[0]
    for sx in (-15, 15):
        b += [C(cx + sx, cy, 22, "#fffdf6", "#7a6a3a", 1.5)]
        b += [chrom(cx + sx, cy - 7, LONG * .8, MAT if sx < 0 else PAT, 90), chrom(cx + sx, cy + 9, SHORT * .8, MAT if sx < 0 else PAT, 90)]
    cx = xs[1]
    for sx in (-15, 15):
        b += [C(cx + sx, cy, 22, "#fffdf6", "#7a6a3a", 1.5)]
        for (dy, l) in [(-9, LONG * .55), (9, SHORT * .55)]:
            b += [chrom(cx + sx - 8, cy + dy, l, MAT if sx < 0 else PAT, 90, False), chrom(cx + sx + 8, cy + dy, l, MAT if sx < 0 else PAT, 90, False)]
    cx = xs[2]
    for sx in (-15, 15):
        b += [C(cx + sx, cy, 22, "#fffdf6", "#7a6a3a", 1.5)]
    for (dx, dy, l, c) in [(-25, -6, LONG * .55, MAT), (-25, 8, SHORT * .55, MAT), (-5, -6, LONG * .55, MAT), (-5, 8, SHORT * .55, MAT), (5, -6, LONG * .55, PAT), (5, 8, SHORT * .55, PAT), (25, -6, LONG * .55, PAT), (25, 8, SHORT * .55, PAT)]:
        b += [chrom(cx + dx, cy + dy, l, c, 90, False)]
    cx = xs[3]
    for (ox, oy) in [(-14, -14), (14, -14), (-14, 14), (14, 14)]:
        b += [C(cx + ox, cy + oy, 14, "#fffdf6", "#7a6a3a", 1.4)]
    for (ox, oy, c1, c2) in [(-14, -14, MAT, MAT), (14, -14, MAT, PAT), (-14, 14, PAT, MAT), (14, 14, PAT, PAT)]:
        b += [chrom(cx + ox, cy + oy - 3, LONG * .5, c1, 90, False), chrom(cx + ox, cy + oy + 5, SHORT * .5, c2, 90, False)]
    for i, n in enumerate(["Metaphase II", "Anaphase II", "Telophase II", "4 gametes (n = 2)"]):
        b += [T(xs[i], cy + 42, n, 6.8, fill="#222", weight="bold")]
    
    save("b_divisions", 470, 336, "".join(b))


def crossing():
    b = [T(235, 12, "Crossing over in prophase I", 9.5, fill=NAVY, weight="bold")]
    def chr2(x, y, cols_left, cols_right, h=64):
        # two chromatids; each given as (top_col, bottom_col)
        s = ""
        for dx, (ct, cb) in ((-5, cols_left), (5, cols_right)):
            s += Q(x + dx - 3, y, 6, h / 2, ct, ct, 0) + Q(x + dx - 3, y + h / 2, 6, h / 2, cb, cb, 0)
        s += C(x, y + h / 2, 3.2, "#222", "#222", 0)
        return s
    for i, (title, desc) in enumerate([("1 Pairing", "homologous chromosomes pair"), ("2 Crossing over", "chromatids swap segments"), ("3 After", "mixed chromatids")]):
        x = 8 + i * 155
        b += [panel(x, 18, 149, 150, title), T(x + 74.5, 38, desc, 5.6, fill="#444", style="italic")]
    # panel 1
    b += [chr2(48, 56, (MAT, MAT), (MAT, MAT)), chr2(88, 56, (PAT, PAT), (PAT, PAT))]
    # panel 2: bars overlapping with crossing marks
    b += [chr2(203, 56, (MAT, MAT), (MAT, MAT)), chr2(223, 56, (PAT, PAT), (PAT, PAT))]
    b += [L(207, 76, 219, 82, RED_, 2), L(207, 82, 219, 76, RED_, 2), T(213, 142, "✕ chiasma", 6.4, fill=RED_, weight="bold")]
    # panel 3
    b += [chr2(358, 56, (MAT, MAT), (MAT, PAT)), chr2(398, 56, (PAT, PAT), (PAT, MAT))]
    b += [T(378, 142, "each chromosome is now a mix", 6.2, fill="#2a7a3a", weight="bold")]
    b += [TL(235, 182, textwrap.wrap("Crossing over, independent assortment and random fertilisation create variation (P23 Q1a(xix): answer B).", 88), 6.8, "middle", "#444")]
    save("b_crossing", 470, 206, "".join(b))


def punnett_box(x, y, title, top, side, cells, res, w=150):
    b = [R(x, y, w, 132, "#fbfcfe", "#b9c7d8", 1, 3), T(x + w / 2, y + 11, title, 7.2, fill=NAVY, weight="bold")]
    gx, gy, cw, ch = x + 36, y + 34, 50, 26
    b += [T(gx - 30, gy - 8, "", 6)]
    for i, t in enumerate(top):
        b += [R(gx + i * cw, gy - 16, cw, 16, "#d6e5f4", "#555", 0.8, 0), T(gx + i * cw + cw / 2, gy - 4.5, t, 7.4, weight="bold")]
    for j, t in enumerate(side):
        b += [R(gx - 24, gy + j * ch, 24, ch, "#fde9c2", "#555", 0.8, 0), T(gx - 12, gy + j * ch + ch / 2 + 2.6, t, 7.4, weight="bold")]
    for k, t in enumerate(cells):
        i, j = k % 2, k // 2
        b += [R(gx + i * cw, gy + j * ch, cw, ch, "#fff", "#555", 0.8, 0), T(gx + i * cw + cw / 2, gy + j * ch + ch / 2 + 2.6, t, 7.6, fill="#111")]
    b += [TL(x + w / 2, y + 100, res, 6.4, "middle", RED_, "bold", 8.6)]
    return b


def punnett():
    b = [T(235, 11, "Punnett squares used in the papers", 9.5, fill=NAVY, weight="bold")]
    sp = [(4, 16, "Tt \u00d7 tt  (P25 Q9d)", ["T", "t"], ["t", "t"], ["Tt", "tt", "Tt", "tt"], ["1 Tt : 1 tt", "1 tall : 1 dwarf"]),
          (160, 16, "Tt \u00d7 Tt", ["T", "t"], ["T", "t"], ["TT", "Tt", "Tt", "tt"], ["1 TT : 2 Tt : 1 tt", "3 tall : 1 dwarf (75% tall)"]),
          (316, 16, "Ee \u00d7 ee  (P24 Q8a)", ["E", "e"], ["e", "e"], ["Ee", "ee", "Ee", "ee"], ["1 Ee : 1 ee", "1 free : 1 attached (50%)"]),
          (4, 154, "EE \u00d7 Ee  (P23 Q7c)", ["E", "e"], ["E", "E"], ["EE", "Ee", "EE", "Ee"], ["1 EE : 1 Ee", "all free earlobes (100%)"]),
          (160, 154, "Carrier \u2640 \u00d7 normal \u2642 (P25 Q8c)", ["XC", "Xc"], ["XC", "Y"], ["XCXC", "XCXc", "XCY", "XcY"], ["normal \u2640, carrier \u2640, normal \u2642,", "colour-blind \u2642 (c = defect): 75% normal"]),
          (316, 154, "Haemophilia (P23 Q1a(xxi))", ["Xh", "Xh"], ["XH", "Y"], ["XHXh", "XHXh", "XhY", "XhY"], ["all \u2640 carriers, all \u2642 haemophilic", "(h = haemophilia allele)"])]
    for (x, y, t, top, side, cells, res) in sp:
        b += punnett_box(x, y, t, top, side, cells, res)
    save("b_punnett", 470, 292, "".join(b))


def flower(cx, cy, col, r=7):
    s = ""
    for k in range(6):
        a = k * math.pi / 3
        s += C(cx + r * 0.8 * math.cos(a), cy + r * 0.8 * math.sin(a), r * 0.55, col, "#555", 0.6)
    return s + C(cx, cy, r * 0.4, "#ffd54a", "#a07000", 0.6)


def dominance():
    b = [T(235, 12, "Complete dominance, incomplete dominance and codominance", 9.5, fill=NAVY, weight="bold")]
    heads = [("COMPLETE DOMINANCE", "red RR × white rr", "#d33", "#fff", "#d33", "F1: all red (Rr)", "red hides white; F2 = 3 red : 1 white"),
             ("INCOMPLETE (A)", "red × white", "#d33", "#fff", "#f6a5b8", "F1: pink (blend)", "F2 = 1 red : 2 pink : 1 white"),
             ("CODOMINANCE (B)", "black × white", "#333", "#fff", None, "F1: both colours shown", "e.g. black-and-white patches, blood group AB")]
    for i, (t, cross, c1, c2, c3, f1, note) in enumerate(heads):
        x = 6 + i * 155
        b += [panel(x, 18, 149, 168, t, NAVY if i != 1 else RED_)]
        cx = x + 74
        b += [T(cx, 38, cross, 6.8, fill="#444"), flower(cx - 28, 58, c1, 9), T(cx, 61, "×", 9), flower(cx + 28, 58, c2, 9), arrow(cx, 72, cx, 92, "#555", 1.4)]
        if c3 is None:
            b += [flower(cx - 9, 108, "#333", 8), flower(cx + 9, 108, "#fff", 8)]
            b += [P(f"M{cx-24},108 C{cx-24},96 {cx},96 {cx},108", "none", "#fff", 0)]
        else:
            b += [flower(cx, 108, c3, 11)]
        b += [T(cx, 134, f1, 7, fill=RED_, weight="bold"), TL(cx, 148, textwrap.wrap(note, 30), 6.2, "middle", "#333", "normal", 8.4)]
        b += [T(cx, 178, "neither hides the other" if i else "dominant hides recessive", 6.2, fill="#2a7a3a", style="italic")]
    save("b_dominance", 470, 194, "".join(b))


def moth(x, y, col, s=1.0, dead=False):
    t = E(x - 5 * s, y, 5 * s, 3 * s, col, "#222", 0.7, -20) + E(x + 5 * s, y, 5 * s, 3 * s, col, "#222", 0.7, 20) + E(x, y + 1 * s, 1.6 * s, 4 * s, "#555", "#222", 0.5)
    if dead:
        t += L(x - 7, y - 6, x + 7, y + 6, RED_, 1.6) + L(x - 7, y + 6, x + 7, y - 6, RED_, 1.6)
    return t


def selection():
    b = [T(235, 12, "Natural selection: the peppered moth", 9.5, fill=NAVY, weight="bold")]
    titles = ["1 Variation", "2 Selection", "3 Survival", "4 Evolution"]
    for i, t in enumerate(titles):
        x = 6 + i * 116
        b += [panel(x, 18, 110, 150, t)]
    # panels with backgrounds
    for i in range(4):
        x = 6 + i * 116
        bg = "#e9e4d6" if i == 0 else "#6b6b6b"
        b += [R(x + 8, 44, 94, 62, bg, "#888", 0.8, 3)]
    pos = [(10, 56), (36, 52), (64, 58), (16, 76), (46, 80), (70, 88), (12, 96), (40, 98)]
    for k, (px, py) in enumerate(pos):
        b += [moth(6 + px + 18, py, "#f4f4f0" if k % 2 == 0 else "#555", 1)]
    for k, (px, py) in enumerate(pos):
        b += [moth(122 + px + 18, py, "#f4f4f0" if k % 2 == 0 else "#555", 1, dead=(k % 2 == 0))]
    for k, (px, py) in enumerate(pos[:5]):
        b += [moth(238 + px + 18, py, "#555", 1)]
    for k, (px, py) in enumerate(pos):
        b += [moth(354 + px + 18, py, "#555" if k != 3 else "#f4f4f0", 1)]
    b += [TL(61, 124, ["moths vary in", "colour (genes)"], 6.4, "middle", "#333", "normal", 8), TL(177, 124, ["soot darkens trees;", "birds eat light moths"], 6.4, "middle", "#333", "normal", 8), TL(293, 124, ["dark moths survive,", "breed, pass on alleles"], 6.4, "middle", "#333", "normal", 8), TL(409, 124, ["dark allele becomes", "common = evolution"], 6.4, "middle", "#b3211b", "bold", 8)]
    for i in range(3):
        b += [arrow(6 + i * 116 + 111, 90, 6 + (i + 1) * 116 - 1, 90, "#555", 1.5)]
    b += [T(235, 186, "Fitness = ability to survive and reproduce. Advantageous alleles increase in frequency.", 6.8, fill="#444")]
    save("b_selection", 470, 194, "".join(b))


def isolation():
    b = [T(235, 12, "Isolation leads to speciation", 9.5, fill=NAVY, weight="bold")]
    # population
    b += [C(48, 80, 30, "#e8f3e0", "#2a7a3a", 1.6), T(48, 44, "ONE POPULATION", 6.4, fill="#2a7a3a", weight="bold"), T(48, 84, "interbreed", 6.4)]
    for (x, y) in [(36, 68), (56, 66), (62, 86), (40, 94), (50, 78)]:
        b += [C(x, y, 3, "#e0a000", "#a07000", 0.5)]
    b += [arrow(80, 80, 112, 80, "#555", 2)]
    # barrier
    b += [R(112, 44, 112, 76, "#fbfcfe", "#999", 1, 3), Q(160, 44, 16, 76, "#9fd0f0", "#4a88c0", 1), T(168, 38, "BARRIER", 6.4, fill=RED_, weight="bold")]
    b += [C(138, 84, 18, "#fff1ee", "#9b3b2a", 1.4), C(198, 84, 18, "#eaf3ff", "#1f5fa8", 1.4)]
    b += [T(138, 87, "A", 8, weight="bold"), T(198, 87, "B", 8, weight="bold")]
    b += [arrow(226, 80, 252, 80, "#555", 2)]
    b += [R(252, 44, 100, 76, "#fff8e8", "#a05a00", 1.2, 3), TL(302, 58, ["no gene flow:", "mutation, natural", "selection and drift", "change A and B", "differently"], 6.6, "middle", "#a05a00", "bold", 9)]
    b += [arrow(354, 80, 380, 80, "#555", 2)]
    b += [R(380, 44, 84, 76, "#eaf6ec", "#2a7a3a", 1.4, 3), TL(422, 62, ["NEW SPECIES", "A and B can no", "longer interbreed"], 6.8, "middle", "#2a7a3a", "bold", 10)]
    types = [("Geographic", "river, mountain, island split by a storm"), ("Ecological (habitat)", "same area, different habitats (trees vs grassland)"), ("Temporal", "breed at different times"), ("Behavioural", "different courtship calls")]
    for i, (t, d) in enumerate(types):
        x = 6 + i * 116
        b += [R(x, 132, 110, 44, "#f4f8fd", "#9db7d4", 1, 3), T(x + 55, 144, t, 7, fill=NAVY, weight="bold"), TL(x + 55, 155, textwrap.wrap(d, 26), 6, "middle", "#333", "normal", 8)]
    b += [T(235, 190, "P25 Q5c: lizards in one desert, different habitats = ecological;  island split by a storm = geographic", 6.6, fill=RED_, weight="bold")]
    save("b_isolation", 470, 198, "".join(b))


def dots(cx, cy, n, cols, r=34, dr=2.6, seed=3):
    import random
    rnd = random.Random(seed)
    s = ""
    for k in range(n):
        a = rnd.random() * 2 * math.pi
        d = r * math.sqrt(rnd.random()) * 0.92
        s += C(cx + d * math.cos(a), cy + d * math.sin(a), dr, rnd.choice(cols), "#444", 0.4)
    return s


def drift():
    b = [T(235, 12, "Genetic drift: bottleneck effect and founder effect", 9.5, fill=NAVY, weight="bold")]
    cols = ["#d33", "#3a7bd5", "#2a9a4a", "#e0a000"]
    b += [panel(6, 18, 226, 140, "Bottleneck effect")]
    b += [C(46, 92, 34, "#fbfcfe", "#999", 1.2), dots(46, 92, 40, cols, 34, 2.8, 1)]
    b += [arrow(84, 92, 108, 92, "#555", 2), TL(96, 74, ["storm,", "flood,", "disease"], 6, "middle", RED_, "bold", 7.5)]
    b += [C(138, 92, 14, "#fbfcfe", "#999", 1.2), dots(138, 92, 5, ["#d33", "#d33", "#3a7bd5"], 14, 2.8, 2)]
    b += [arrow(158, 92, 178, 92, "#555", 2)]
    b += [C(204, 92, 24, "#fbfcfe", "#999", 1.2), dots(204, 92, 18, ["#d33", "#d33", "#d33", "#3a7bd5"], 24, 2.6, 4)]
    b += [TL(46, 142, ["large, varied"], 6.2, "middle", "#333"), TL(138, 142, ["few survivors"], 6.2, "middle", "#333"), TL(204, 142, ["less variation", "(some alleles lost)"], 6.2, "middle", "#b3211b", "bold", 8)]
    b += [panel(238, 18, 226, 140, "Founder effect")]
    b += [P("M246,70 C250,56 290,52 312,64 C330,76 320,112 296,122 C270,132 244,118 244,96 Z", "#e4f3dc", "#2a7a3a", 1.2)]
    b += [dots(282, 92, 34, cols, 28, 2.8, 5)]
    b += [P("M420,56 C440,50 458,64 456,84 C454,108 430,114 412,104 C400,94 404,64 420,56 Z", "#e4f3dc", "#2a7a3a", 1.2)]
    b += [dots(430, 84, 4, ["#3a7bd5"], 14, 2.8, 6), arrow(318, 82, 400, 82, "#555", 2), TL(360, 66, ["small group", "colonises new island"], 6.2, "middle", RED_, "bold", 8)]
    b += [TL(282, 142, ["ancestral population"], 6.2, "middle", "#333"), TL(430, 142, ["colony: few alleles,", "drifts apart"], 6, "middle", "#b3211b", "bold", 8)]
    b += [T(235, 176, "Drift = chance change in allele frequency, strongest in small populations.", 6.8, fill="#444")]
    save("b_drift", 470, 184, "".join(b))


def genetic_eng():
    b = [T(235, 12, "Genetic engineering: making disease-resistant, high-yield cattle", 9.5, fill=NAVY, weight="bold")]
    steps = [("1 Find the gene", "disease-resistance gene\nin the local breed", "#1f5fa8", "#eaf3ff"), ("2 Cut it out", "restriction enzyme\n(molecular scissors)", "#7a3b9b", "#f3eaff"), ("3 Insert in vector", "gene joined into a\nplasmid (recombinant DNA)", "#a05a00", "#fff4e0"),
             ("4 Transfer", "vector carries gene\ninto high-yield hybrid cell", "#2a7a3a", "#eaf6ec"), ("5 Grow", "embryo → GM cattle:\nhigh yield + resistant", "#b3211b", "#ffe8e8")]
    w = 86
    for i, (t, d, c, f) in enumerate(steps):
        x = 4 + i * (w + 8)
        b += [R(x, 28, w, 82, f, c, 1.6, 5), TL(x + w / 2, 42, t.split(" ", 1)[0:1] + [t.split(" ", 1)[1]], 7, "middle", c, "bold", 9), TL(x + w / 2, 70, d.split("\n"), 6, "middle", "#222", "normal", 8)]
        if i < 4:
            b += [arrow(x + w + 1, 70, x + w + 7, 70, "#333", 1.6)]
    # DNA helix glyph
    for k in range(10):
        x = 20 + k * 8
        y1 = 130 + 8 * math.sin(k * 0.9); y2 = 130 - 8 * math.sin(k * 0.9)
        b += [L(x, y1, x, y2, "#aaa", 1), C(x, y1, 1.8, "#3a7bd5", "#3a7bd5", 0), C(x, y2, 1.8, "#d33", "#d33", 0)]
    b += [T(66, 152, "DNA (nucleic acid)", 6.4, fill="#444")]
    b += [R(150, 120, 312, 50, "#fffbe9", "#b3a000", 1, 4), TL(306, 138, ["Genetic engineering changes the DNA (nucleic acid)", "Introducing foreign DNA = genetic modification", "Faster and more precise than natural evolution", "Uses: insulin from bacteria, pest-resistant crops"], 6.4, "middle", "#444", "normal", 10)]
    save("b_genetic_eng", 470, 180, "".join(b))


def ecosystem():
    b = [T(235, 12, "A pond ecosystem: biotic and abiotic components", 9.5, fill=NAVY, weight="bold")]
    b += [Q(6, 22, 458, 132, "#f3f9ff", "#9db7d4", 1)]
    b += [Q(6, 82, 458, 72, "#bfe0f7", "#bfe0f7", 0), Q(6, 138, 458, 16, "#a98a5a", "#a98a5a", 0)]
    b += [C(48, 44, 14, "#ffd54a", "#b36200", 1.4)]
    for k in range(8):
        a = k * math.pi / 4
        b += [L(48 + 18 * math.cos(a), 44 + 18 * math.sin(a), 48 + 24 * math.cos(a), 44 + 24 * math.sin(a), "#b36200", 1.4)]
    # plants
    for x in (150, 170, 330):
        b += [P(f"M{x},138 C{x-6},118 {x+6},104 {x},90", "none", "#2a9a4a", 3)]
    b += [E(250, 108, 20, 8, "#2a9a4a", "#1a6a2a", 1)]
    # fish
    for (x, y) in [(210, 100), (290, 120)]:
        b += [E(x, y, 14, 6, "#f08a4b", "#a03a00", 1), P(f"M{x-14},{y} L{x-22},{y-6} L{x-22},{y+6} Z", "#f08a4b", "#a03a00", 1), C(x + 8, y - 1, 1.2, "#111", "#111", 0)]
    # frog on lily pad, bacteria
    b += [E(380, 84, 22, 4, "#2a9a4a", "#1a6a2a", 1), E(380, 76, 10, 7, "#7fcf5a", "#2a7a3a", 1.2), C(376, 71, 2, "#111", "#111", 0), C(384, 71, 2, "#111", "#111", 0)]
    for (x, y) in [(400, 134), (410, 130), (420, 136), (432, 131)]:
        b += [E(x, y, 3.4, 1.8, "#7a3b9b", "#4a1a6b", 0.6)]
    # bubbles O2
    for (x, y) in [(222, 92), (230, 78), (160, 86), (176, 74)]:
        b += [C(x, y, 1.8, "#fff", "#4a88c0", 0.6)]
    b += [lab(86, 36, 60, 44, "Sunlight (abiotic)", "start", 6.8, "#a05a00", "bold")]
    b += [lab(150, 168, 160, 132, "Water plants / algae (biotic)", "start", 6.6, "#1a6a2a", "bold")]
    b += [lab(300, 28, 290, 114, "Fish (biotic)", "start", 6.6, "#1a6a2a", "bold")]
    b += [lab(375, 50, 380, 70, "Frog (biotic)", "middle", 6.6, "#1a6a2a", "bold")]
    b += [lab(412, 162, 418, 134, "Bacteria (biotic)", "middle", 6.6, "#1a6a2a", "bold")]
    b += [lab(20, 166, 40, 142, "Mud / soil (abiotic)", "start", 6.6, "#a05a00", "bold"), lab(240, 52, 240, 84, "Water, dissolved O₂ and CO₂, temperature (abiotic)", "middle", 6.6, "#a05a00", "bold")]
    b += [TL(235, 186, ["Plants need sunlight, water and CO\u2082; fish and frogs need dissolved oxygen and water;", "bacteria need mud and warmth: every biotic component depends on the abiotic ones (P23 Q9d)."], 6.6, "middle", "#444", "normal", 10)]
    save("b_ecosystem", 470, 212, "".join(b))


def biodiv():
    b = [T(235, 12, "Biodiversity and the health of the ecosystem", 9.5, fill=NAVY, weight="bold")]
    b += [panel(6, 18, 226, 178, "GOOD: a positive cycle", "#2a7a3a"), panel(238, 18, 226, 178, "BAD: a negative cycle", RED_)]
    g = [("HIGH BIODIVERSITY", "many genes, species, habitats", 119, 58), ("STABLE, HEALTHY ECOSYSTEM", "resilient; resists invasive species", 119, 104), ("ECOSYSTEM SERVICES", "food, clean water, pollination, soil", 119, 150)]
    for (t, s, cx, cy) in g:
        b += [R(cx - 90, cy - 16, 180, 34, "#eaf6ec", "#2a7a3a", 1.4, 5), T(cx, cy - 2, t, 7.2, fill="#2a7a3a", weight="bold"), T(cx, cy + 10, s, 6, fill="#333")]
    b += [arrow(119, 74, 119, 86, "#2a7a3a", 1.8), arrow(119, 122, 119, 132, "#2a7a3a", 1.8)]
    b += [P("M209,150 C226,150 226,58 209,58", "none", "#2a7a3a", 1.8), '<path d="M209,58 l8,-3 l0,6 z" fill="#2a7a3a"/>']
    b += [T(119, 184, "services support people and species, so we protect biodiversity", 6, fill="#2a7a3a")]
    r = [("THREATS", "habitat loss, poaching, pollution", 351, 58), ("LOSS OF SPECIES", "food webs break, fewer pollinators", 351, 104), ("UNSTABLE ECOSYSTEM", "invasive species, disease, collapse", 351, 150)]
    for (t, s, cx, cy) in r:
        b += [R(cx - 90, cy - 16, 180, 34, "#ffe8e8", RED_, 1.4, 5), T(cx, cy - 2, t, 7.2, fill=RED_, weight="bold"), T(cx, cy + 10, s, 6, fill="#333")]
    b += [arrow(351, 74, 351, 86, RED_, 1.8), arrow(351, 122, 351, 132, RED_, 1.8)]
    b += [T(351, 184, "poaching is NOT a healthy sign (P24 Q1a(xi))", 6, fill=RED_)]
    save("b_biodiv", 470, 204, "".join(b))


if __name__ == "__main__":
    divisions(); crossing(); punnett(); dominance(); selection(); isolation(); drift(); genetic_eng(); ecosystem(); biodiv()
