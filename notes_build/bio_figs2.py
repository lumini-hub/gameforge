#!/usr/bin/env python3
"""Biology diagrams, part 2: photosynthesis, plant transport, digestion."""
from bio_lib import *

RED_ = "#b3211b"
GRN = "#2a7a3a"


def arrow(x1, y1, x2, y2, c="#333", w=1.8):
    return L(x1, y1, x2, y2, c, w, None, True)


def chloroplast():
    import math
    b = [T(235, 12, "Photosynthesis inside the chloroplast", 9.5, fill=NAVY, weight="bold")]
    b += [E(238, 122, 190, 70, "#eaf7e6", "#2a7a3a", 2.4), E(238, 122, 182, 63, "#f3fbef", "#2a7a3a", 1)]
    for (gx, gy) in [(95, 104), (140, 128), (100, 140), (160, 98)]:
        for k in range(4):
            b += [E(gx, gy + k * 6, 20, 3.4, "#7fcf7f", "#2a7a3a", 1)]
    b += [C(335, 122, 34, "#fff", "#1f5fa8", 1.6)]
    b += [P("M335,88 C361,88 369,122 345,142", "none", "#1f5fa8", 2), P("M335,156 C307,156 299,122 325,102", "none", "#1f5fa8", 2)]
    b += ['<path d="M345,142 l-3,-8 l9,3 z" fill="#1f5fa8"/>', '<path d="M325,102 l3,8 l-9,-3 z" fill="#1f5fa8"/>']
    b += [TL(335, 118, ["Calvin", "cycle"], 8, fill="#1f5fa8", weight="bold")]
    b += [C(40, 40, 11, "#ffd54a", "#b36200", 1.4)]
    for k in range(8):
        a_ = k * math.pi / 4
        b += [L(40 + 14 * math.cos(a_), 40 + 14 * math.sin(a_), 40 + 19 * math.cos(a_), 40 + 19 * math.sin(a_), "#b36200", 1.4)]
    b += [arrow(55, 52, 92, 96, "#d9a200", 2.4), T(36, 66, "light", 7.4, "start", "#b36200", "bold")]
    b += [arrow(150, 30, 150, 86, "#1f5fa8", 2), T(150, 26, "H\u2082O (water)", 7.8, fill="#1f5fa8", weight="bold")]
    b += [arrow(190, 118, 190, 196, "#c33", 2), T(198, 204, "O\u2082 released", 7.8, "start", "#c33", "bold")]
    b += [arrow(335, 30, 335, 86, "#555", 2), T(335, 26, "CO\u2082 (carbon dioxide)", 7.8, fill="#333", weight="bold")]
    b += [arrow(335, 156, 335, 196, GRN, 2), T(346, 205, "GLUCOSE", 8, "start", GRN, "bold")]
    b += [L(190, 96, 296, 108, "#a05a00", 1.8, None, True), T(244, 94, "ATP", 7.8, fill="#a05a00", weight="bold")]
    b += [L(190, 108, 296, 120, "#7a3b9b", 1.8, None, True), T(244, 121, "NADPH", 7.8, fill="#7a3b9b", weight="bold")]
    b += [L(296, 136, 190, 128, "#888", 1.2, "3 2", True), T(244, 146, "ADP, NADP\u207a return", 6.6, fill="#666")]
    b += [T(100, 218, "GRANA (thylakoids) = LIGHT REACTION", 7.6, fill=RED_, weight="bold"), T(335, 218, "STROMA = DARK REACTION", 7.6, fill=RED_, weight="bold")]
    b += [T(100, 228, "needs light + water; makes ATP, NADPH, O\u2082", 6.4, fill="#444"), T(335, 228, "needs CO\u2082 + ATP + NADPH; makes glucose", 6.4, fill="#444")]
    save("b_chloroplast", 470, 236, "".join(b))


def rate_graphs():
    b = [T(235, 12, "Factors limiting the rate of photosynthesis", 9.5, fill=NAVY, weight="bold")]
    specs = [("Light intensity", "M0,0 C20,-48 60,-70 118,-76", "levels off: another factor", "(CO₂ / temperature) is limiting"),
             ("CO₂ concentration", "M0,0 C20,-48 60,-70 118,-76", "levels off: light or", "temperature is limiting"),
             ("Temperature", "M0,0 C40,-20 70,-50 80,-78 C90,-90 96,-60 104,0", "optimum about 35–40 °C", "above it enzymes denature")]
    for i, (t, d, l1, l2) in enumerate(specs):
        x = 8 + i * 154
        b += [panel(x, 18, 148, 168, t)]
        ox, oy = x + 18, 150
        b += [L(ox, oy, ox, oy - 100, "#222", 1.2, None, True), L(ox, oy, ox + 118, oy, "#222", 1.2, None, True)]
        b += [P(d, "none", "#2a7a3a", 2.2).replace('d="', f'transform="translate({ox},{oy})" d="')]
        b += ['<text x="%s" y="%s" font-size="6.6" text-anchor="middle" transform="rotate(-90 %s %s)">Rate of photosynthesis</text>' % (x + 8, oy - 50, x + 8, oy - 50)]
        xl = ["Light intensity →", "CO₂ concentration →", "Temperature (°C) →"][i]
        b += [T(ox + 60, oy + 11, xl, 6.8)]
        b += [TL(x + 74, 40, [l1, l2], 6.4, fill="#b3211b")]
        if i == 2:
            b += [L(ox + 80, oy, ox + 80, oy - 78, RED_, 1, "3 2"), T(ox + 80, oy - 82, "optimum", 6.4, fill=RED_)]
        if i < 2:
            b += [L(ox + 70, oy - 74, ox + 118, oy - 76, RED_, 1, "3 2")]
    save("b_rate_graphs", 470, 192, "".join(b))


def elodea():
    b = [T(235, 12, "Pondweed (Elodea) experiment: bubbles of oxygen per minute", 9.5, fill=NAVY, weight="bold")]
    for k, (x, title, liquid, hasco2) in enumerate([(10, "EXPERIMENT", "water + sodium hydrogen carbonate", True), (240, "CONTROL", "water only", False)]):
        b += [panel(x, 18, 220, 196, title, RED_ if k == 0 else NAVY)]
        bx = x + 40
        b += [R(bx, 76, 100, 112, "#eaf6ff", "#555", 1.5, 5), Q(bx + 1.5, 100, 97, 86, "#cfe8fa", "#cfe8fa", 0)]
        b += [P(f"M{bx+18},170 L{bx+42},120 L{bx+58},120 L{bx+82},170 Z", "#f5f5f5", "#555", 1.4)]                   # funnel
        b += [Q(bx + 44, 70, 12, 52, "#eaf6ff", "#555", 1.4), Q(bx + 45.5, 86, 9, 34, "#fff", "#fff", 0)]            # tube
        b += [P(f"M{bx+30},176 C{bx+34},160 {bx+40},170 {bx+46},156 C{bx+50},170 {bx+58},160 {bx+64},176", "none", GRN, 2)]  # Elodea
        for (px, py) in [(bx + 49, 132), (bx + 51, 118), (bx + 48, 104)] if k == 0 else [(bx + 50, 128)]:
            b += [C(px, py, 2, "#fff", "#4a88c0", 0.8)]
        b += [E(bx + 128, 120, 12, 14, "#ffe9a0", "#b36200", 1.4), Q(bx + 124, 134, 8, 16, "#999", "#555", 1)]       # lamp
        for a in (-1, 0, 1):
            b += [L(bx + 116, 120 + a * 8, bx + 104, 120 + a * 8, "#d9a200", 1.2, None, True)]
        b += [T(bx + 128, 166, "lamp", 6.8)]
        b += [T(x + 110, 202, liquid, 7, fill=RED_ if k == 0 else "#444", weight="bold")]
    b += [lab(150, 48, 66 + 38, 100, "", "start")] if False else []
    b += [lab(78, 56, 100, 85, "test tube (O₂ collects)", "middle", 6.8), lab(36, 66, 52, 160, "", "start")] if False else []
    b += [lab(52, 64, 88, 82, "test tube: O₂", "middle", 6.8), lab(172, 56, 132, 98, "", "start")] if False else []
    b += [lab(36, 52, 88, 80, "test tube (O₂ gas)", "start", 6.6), lab(24, 174, 64, 168, "funnel", "start", 6.6), lab(24, 186, 84, 172, "Elodea", "start", 6.6, GRN, "bold")]
    save("b_elodea", 470, 222, "".join(b))


def vascular():
    W = 470
    b = [T(235, 12, "Conducting (vascular) tissue", 9.5, fill=NAVY, weight="bold")]
    b += [box(175, 20, 120, 24, "CONDUCTING TISSUE", col=NAVY)]
    b += [box(30, 66, 190, 26, "XYLEM: water + minerals (up only)", col="#1f5fa8", fill="#eaf3ff"), box(250, 66, 190, 26, "\u2460 PHLOEM: food (up and down)", col="#b36200", fill="#fff4e0")]
    b += [L(235, 44, 235, 54, "#333", 1.4), L(125, 54, 345, 54, "#333", 1.4), L(125, 54, 125, 66, "#333", 1.4, None, True), L(345, 54, 345, 66, "#333", 1.4, None, True)]
    xs = [["Xylem", "vessel"], ["\u2462 Tracheid"], ["Xylem", "fibre"], ["\u2464 Xylem", "parenchyma"]]
    xd = [["main water", "pipe (dead)"], ["water pipe", "(dead)"], ["support"], ["storage"]]
    ph = [["\u2461 Sieve tube", "element"], ["Companion", "cell"], ["\u2463 Phloem", "fibre"], ["\u2465 Phloem", "parenchyma"]]
    pd = [["conducts food", "(like oesophagus)"], ["controls sieve", "tube, gives ATP"], ["support"], ["stores food,", "conducts"]]
    b += [L(125, 92, 125, 100, "#333", 1.1), L(345, 92, 345, 100, "#333", 1.1), L(33, 100, 204, 100, "#333", 1.1), L(269, 100, 440, 100, "#333", 1.1)]
    for i in range(4):
        x1, x2 = 6 + i * 57, 242 + i * 57
        b += [L(x1 + 27, 100, x1 + 27, 112, "#333", 1.1, None, True), L(x2 + 27, 100, x2 + 27, 112, "#333", 1.1, None, True)]
        b += [R(x1, 112, 54, 60, "#fff", "#1f5fa8", 1.2, 3), TL(x1 + 27, 126, xs[i], 6.4, "middle", "#1f5fa8", "bold"), TL(x1 + 27, 150, xd[i], 5.6, "middle", "#333")]
        b += [R(x2, 112, 54, 60, "#fff", "#b36200", 1.2, 3), TL(x2 + 27, 126, ph[i], 6.4, "middle", "#b36200", "bold"), TL(x2 + 27, 150, pd[i], 5.4, "middle", "#333")]
    b += [TL(235, 190, textwrap.wrap("Numbers \u2460\u2013\u2465 are the blanks of P24 Q7b: 1 phloem, 2 sieve element, 3 tracheid, 4 phloem fibre, 5 xylem parenchyma, 6 phloem parenchyma", 88), 6.2, "middle", "#444")]
    save("b_vascular", W, 212, "".join(b))


def plant(x, y, sink_label=True):
    """simple plant: returns drawing parts"""
    b = [P(f"M{x},{y+140} L{x},{y+10}", "none", "#7a5a2a", 8)]
    b += [E(x - 38, y + 22, 34, 12, "#6fcf6f", "#2a7a3a", 1.3, -20), E(x + 38, y + 30, 34, 12, "#6fcf6f", "#2a7a3a", 1.3, 20), E(x - 30, y + 70, 28, 10, "#6fcf6f", "#2a7a3a", 1.3, -15)]
    b += [C(x + 40, y + 78, 9, "#f08a4b", "#a03a00", 1.3)]
    for dx in (-30, -12, 8, 28):
        b += [P(f"M{x},{y+140} L{x+dx},{y+178}", "none", "#7a5a2a", 2)]
    b += [Q(x - 70, y + 140, 140, 3, "#9b7a3a", "#9b7a3a", 0)]
    return b


def translocation():
    b = [T(235, 12, "Translocation: from source to sink through the phloem", 9.5, fill=NAVY, weight="bold")]
    b += plant(235, 24)
    b += [L(228, 70, 228, 190, "#e08a00", 3, "5 3", True), L(228, 72, 228, 52, "#e08a00", 3, "5 3", True)]
    b += [arrow(244, 170, 244, 70, "#1f5fa8", 2.4)]
    b += [arrow(228, 62, 270, 100, "#e08a00", 2)]
    b += [lab(100, 36, 205, 46, "SOURCE: leaf makes sucrose", "start", 7.6, GRN, "bold")] if False else []
    b += [T(10, 44, "SOURCE", 8.4, "start", GRN, "bold"), TL(10, 55, ["leaf: makes sugar by", "photosynthesis and", "exports sucrose"], 6.8, "start")]
    b += [L(88, 44, 196, 44, GRN, 1, "3 2", True)]
    b += [T(340, 100, "SINK", 8.4, "start", RED_, "bold"), TL(340, 111, ["fruit, seed, growing bud:", "use or store sugar"], 6.8, "start")]
    b += [L(338, 100, 280, 104, RED_, 1, "3 2", True)]
    b += [T(340, 180, "SINK", 8.4, "start", RED_, "bold"), TL(340, 191, ["root, tuber: use or store", "sugar"], 6.8, "start")]
    b += [L(338, 182, 266, 192, RED_, 1, "3 2", True)]
    b += [T(10, 150, "Phloem (orange)", 7.6, "start", "#b36200", "bold"), TL(10, 161, ["carries sucrose up and down;", "needs energy (ATP)", "and water from the xylem"], 6.8, "start")]
    b += [T(10, 205, "Xylem (blue): water + minerals up only", 7.4, "start", "#1f5fa8", "bold")]
    save("b_translocation", 470, 226, "".join(b))


def ring():
    b = [T(235, 12, "Ring (girdling) experiment", 9.5, fill=NAVY, weight="bold")]
    xs = [10, 165, 320]
    titles = ["Start", "After a few months", "Interpretation"]
    for i, x in enumerate(xs):
        b += [panel(x, 18, 148, 200, titles[i])]
        cx = x + 74
        # stem
        top, bot = 50, 200
        b += [Q(cx - 14, top, 28, bot - top, "#c79a5a", "#7a5a2a", 1.4)]
        b += [Q(cx - 8, top, 16, bot - top, "#f2e6c8", "#7a5a2a", 0.8)]   # wood core with xylem
        if i == 0:
            b += [Q(cx - 14, 120, 28, 24, "#fff", "#fff", 0), Q(cx - 8, 120, 16, 24, "#f2e6c8", "#7a5a2a", 0.8)]
            b += [T(x + 8, 108, "ring of bark", 6.6, "start"), T(x + 8, 116, "removed", 6.6, "start"), L(x + 36, 118, cx - 15, 130, "#666", 0.8)]
        if i == 1:
            b += [P(f"M{cx-14},120 C{cx-30},118 {cx-30},96 {cx-14},92 L{cx-14},120 Z", "#c79a5a", "#7a5a2a", 1.2), P(f"M{cx+14},120 C{cx+30},118 {cx+30},96 {cx+14},92 L{cx+14},120 Z", "#c79a5a", "#7a5a2a", 1.2)]
            b += [Q(cx - 14, 120, 28, 24, "#fff", "#fff", 0), Q(cx - 8, 120, 16, 24, "#f2e6c8", "#7a5a2a", 0.8)]
            b += [T(x + 74, 80, "SWELLING", 7, fill=RED_, weight="bold"), TL(x + 36, 170, ["bark below", "ring starves,", "roots die"], 6.4, "middle", "#444")]
        if i == 2:
            b += [Q(cx - 14, 120, 28, 24, "#fff", "#fff", 0), Q(cx - 8, 120, 16, 24, "#f2e6c8", "#7a5a2a", 0.8)]
            b += [L(cx - 22, 66, cx - 22, 112, "#e08a00", 2.4, None, True), T(cx - 26, 90, "sugar", 6.4, "end", "#b36200"), T(cx - 26, 98, "comes down", 6.4, "end", "#b36200")]
            b += [L(cx + 22, 190, cx + 22, 66, "#1f5fa8", 2.4, None, True), T(cx + 26, 130, "water", 6.4, "start", "#1f5fa8"), T(cx + 26, 138, "still rises", 6.4, "start", "#1f5fa8")]
            b += [T(cx - 26, 130, "blocked", 6.8, "end", RED_, "bold"), L(cx - 24, 112, cx - 17, 120, RED_, 1.8)]
            b += [TL(x + 74, 208, ["phloem cut; xylem intact"], 6.4, fill="#444")]
        # leaves & roots
        b += [E(cx - 22, top + 2, 18, 6, "#6fcf6f", "#2a7a3a", 1, -25), E(cx + 22, top + 4, 18, 6, "#6fcf6f", "#2a7a3a", 1, 25)]
    save("b_ring", 470, 224, "".join(b))


def digestive():
    b = [T(235, 12, "The human digestive system", 9.5, fill=NAVY, weight="bold")]
    # body outline faint
    b += [P("M200,28 C170,30 160,60 168,92 C150,130 150,210 170,260 L300,260 C320,210 320,130 302,92 C310,60 300,30 270,28 Z", "#fff8f5", "#e6c9be", 1)]
    # mouth/oesophagus
    b += [E(235, 40, 22, 12, "#f6c0c0", "#a03a3a", 1.2), P("M235,52 L235,120", "none", "#d98080", 7)]
    b += [E(213, 52, 7, 5, "#fde68a", "#a05a00", 1), E(257, 52, 7, 5, "#fde68a", "#a05a00", 1)]   # salivary glands
    # liver
    b += [P("M170,120 C190,106 236,110 244,124 C246,150 214,160 190,152 C174,146 168,134 170,120 Z", "#b0663a", "#6b3a1a", 1.6)]
    b += [E(214, 152, 7, 11, "#78c28a", "#2a7a3a", 1.2)]  # gall bladder
    # stomach
    b += [P("M240,118 C270,112 288,126 284,152 C280,176 250,180 236,166 C230,150 244,140 252,138 C250,130 240,128 240,118 Z", "#f4b18a", "#a0522d", 1.6)]
    # pancreas
    b += [P("M216,170 C236,162 262,164 280,172 C262,180 236,182 216,176 Z", "#f7e08a", "#a07a00", 1.2)]
    # small intestine coil
    for k, y in enumerate(range(186, 236, 9)):
        b += [P(f"M196,{y} C210,{y-8} 224,{y+6} 238,{y-2} C252,{y-8} 264,{y+4} 276,{y}", "none", "#e08aa0", 5)]
    # large intestine frame
    b += [P("M180,188 L180,248 L290,248 L290,188 L282,188 L282,240 L188,240 L188,188 Z", "#cfe8c0", "#4a8a2a", 1.4)]
    b += [P("M235,248 L235,262", "none", "#8a5a3a", 6)]
    labs_l = [("Mouth", 130, 40, 215, 40), ("Salivary glands", 130, 58, 208, 54), ("Oesophagus", 130, 90, 232, 90), ("Liver (makes bile)", 130, 132, 190, 132), ("Gall bladder (stores bile)", 130, 158, 212, 156), ("Large intestine", 130, 215, 183, 215), ("Rectum", 130, 256, 233, 258)]
    for (t, x, y, tx, ty) in labs_l:
        b += [lab(x, y, tx, ty, t, "end", 7.6, "#111", "bold" if "Liver" in t else "normal")]
    labs_r = [("Stomach (HCl, pepsin)", 330, 140, 270, 146), ("Pancreas", 330, 172, 270, 173), ("Small intestine", 330, 205, 270, 205), ("(digestion + absorption)", 330, 215, 330, 215), ("Anus", 330, 262, 236, 262)]
    for (t, x, y, tx, ty) in labs_r:
        if t.startswith("(digestion"):
            b += [T(x, y, t, 6.6, "start", "#555")]
        else:
            b += [lab(x, y, tx, ty, t, "start", 7.6)]
    b += [T(14, 276, "P25 Q2a: A liver, B stomach, C pancreas, D small intestine", 6.6, "start", RED_)]
    save("b_digestive", 470, 284, "".join(b))


def digest_flow():
    b = [T(235, 12, "Digestion: which enzyme, where, end product", 9.5, fill=NAVY, weight="bold")]
    rows = [("CARBOHYDRATE", "#b36200", [("Starch", "salivary amylase", "Maltose", 0), ("Maltose", "maltase (pancreatic amylase)", "GLUCOSE", 2)]),
            ("PROTEIN", "#1f5fa8", [("Protein", "pepsin + HCl", "Peptides", 1), ("Peptides", "trypsin, peptidases", "AMINO ACIDS", 2)]),
            ("FAT", "#a02a2a", [("Fat", "bile emulsifies, then lipase", "FATTY ACIDS + GLYCEROL", 2)])]
    y = 38
    xcol = [10, 150, 300]
    for (name, col, steps) in rows:
        b += [R(4, y, 462, 46, "#fbfcfe", col, 1.2, 4), T(12, y + 12, name, 8, "start", col, "bold")]
        for (a, enz, prod, colidx) in steps:
            pass
        # draw chain
        if name == "CARBOHYDRATE":
            b += [box(14, y + 20, 60, 20, "Starch", col=col), arrow(76, y + 30, 130, y + 30, col), T(103, y + 24, "salivary amylase", 5.8, fill=col), box(132, y + 20, 60, 20, "Maltose", col=col), arrow(194, y + 30, 330, y + 30, col), T(262, y + 24, "maltase (in small intestine)", 5.8, fill=col), box(332, y + 20, 80, 20, "GLUCOSE", col=col, fill="#fff4e0")]
        if name == "PROTEIN":
            b += [box(14, y + 20, 60, 20, "Protein", col=col), arrow(76, y + 30, 190, y + 30, col), T(133, y + 24, "pepsin + HCl (stomach)", 5.8, fill=col), box(192, y + 20, 60, 20, "Peptides", col=col), arrow(254, y + 30, 330, y + 30, col), T(292, y + 24, "trypsin, peptidases", 5.8, fill=col), box(332, y + 20, 100, 20, "AMINO ACIDS", col=col, fill="#eaf3ff")]
        if name == "FAT":
            b += [box(14, y + 20, 60, 20, "Fat", col=col), arrow(76, y + 30, 330, y + 30, col), T(203, y + 24, "bile (liver) emulsifies  →  pancreatic lipase", 5.8, fill=col), box(332, y + 20, 128, 20, "FATTY ACIDS + GLYCEROL", col=col, fill="#fdeaea", tsize=7)]
        y += 52
    b += [T(235, y + 8, "Absorption of the end products happens through the villi of the small intestine; water is absorbed in the large intestine.", 6.6, fill="#444")]
    save("b_digest_flow", 470, y + 16, "".join(b))


if __name__ == "__main__":
    chloroplast(); rate_graphs(); elodea(); vascular(); translocation(); ring(); digestive(); digest_flow()
