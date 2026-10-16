#!/usr/bin/env python3
"""Biology diagrams, part 3: blood, kidney, nervous system."""
import math, textwrap
from bio_lib import *

RED_ = "#b3211b"


def arrow(x1, y1, x2, y2, c="#333", w=1.8):
    return L(x1, y1, x2, y2, c, w, None, True)


def loop(cx, cy, r, side, c="#333"):
    """small self-loop arc above/below a circle"""
    if side == "up":
        return P(f"M{cx-9},{cy-r+1} C{cx-22},{cy-r-22} {cx+22},{cy-r-22} {cx+9},{cy-r+1}", "none", c, 1.5) + f'<path d="M{cx+9},{cy-r+1} l-2,-7 l8,3 z" fill="{c}"/>'
    if side == "down":
        return P(f"M{cx-9},{cy+r-1} C{cx-22},{cy+r+22} {cx+22},{cy+r+22} {cx+9},{cy+r-1}", "none", c, 1.5) + f'<path d="M{cx+9},{cy+r-1} l-2,7 l8,-3 z" fill="{c}"/>'
    if side == "left":
        return P(f"M{cx-r+1},{cy-9} C{cx-r-24},{cy-22} {cx-r-24},{cy+22} {cx-r+1},{cy+9}", "none", c, 1.5) + f'<path d="M{cx-r+1},{cy+9} l7,-1 l-3,-7 z" fill="{c}"/>'
    return P(f"M{cx+r-1},{cy-9} C{cx+r+24},{cy-22} {cx+r+24},{cy+22} {cx+r-1},{cy+9}", "none", c, 1.5) + f'<path d="M{cx+r-1},{cy+9} l-7,-1 l3,-7 z" fill="{c}"/>'


def blood_chart():
    b = [T(235, 12, "Who can give blood to whom (ABO system)", 9.5, fill=NAVY, weight="bold")]
    pos = {"O": (62, 118), "A": (235, 56), "B": (235, 180), "AB": (408, 118)}
    cols = {"O": "#ffd6d6", "A": "#ffe9b8", "B": "#d6e8ff", "AB": "#e6d6ff"}
    # arrows first
    def edge(a, b_):
        (x1, y1), (x2, y2) = pos[a], pos[b_]
        d = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / d, (y2 - y1) / d
        return arrow(x1 + ux * 24, y1 + uy * 24, x2 - ux * 26, y2 - uy * 26, "#444", 1.8)
    for a, b_ in [("O", "A"), ("O", "B"), ("O", "AB"), ("A", "AB"), ("B", "AB")]:
        b += [edge(a, b_)]
    b += [loop(62, 118, 22, "left"), loop(235, 56, 22, "up"), loop(235, 180, 22, "down"), loop(408, 118, 22, "right")]
    for k, (x, y) in pos.items():
        b += [C(x, y, 22, cols[k], "#555", 1.6), T(x, y + 5, k, 14, fill="#111", weight="bold")]
    b += [R(4, 24, 126, 42, "#fff", RED_, 1.2, 4), TL(67, 38, ["X = O: universal donor", "no A or B antigen on RBC", "has anti-A and anti-B"], 6.4, "middle", RED_, "bold", 9)]
    b += [R(334, 24, 132, 42, "#fff", "#5b3a8a", 1.2, 4), TL(400, 38, ["Y = AB: universal recipient", "no antibodies in plasma", "has A and B antigens"], 6.4, "middle", "#5b3a8a", "bold", 9)]
    b += [T(262, 60, "antigen A, anti-B", 6.4, "start", "#555"), T(262, 184, "antigen B, anti-A", 6.4, "start", "#555")]
    b += [TL(235, 226, textwrap.wrap("Arrow = can donate to; loop = can donate to its own group.  Rh− donors are safe for Rh− and Rh+; Rh+ blood must only go to Rh+.", 88), 6.2, "middle", "#444")]
    save("b_blood_chart", 470, 246, "".join(b))


def blood_test():
    b = [T(235, 12, "Blood typing with anti-A and anti-B (P23 Q3c)", 9.5, fill=NAVY, weight="bold")]
    b += [panel(6, 18, 250, 176, "Blood X tested")]
    for k, (x, title, clump) in enumerate([(50, "Test tube A\n+ antibody A", False), (160, "Test tube B\n+ antibody B", True)]):
        b += [R(x, 62, 40, 100, "#fff", "#555", 1.6, 8), Q(x + 1.5, 112, 37, 48, "#d9544a", "#d9544a", 0)]
        if clump:
            b += [Q(x + 1.5, 112, 37, 48, "#f4d6d2", "#f4d6d2", 0)]
            for (dx, dy) in [(8, 138), (20, 148), (30, 140), (14, 126), (26, 130), (10, 152)]:
                b += [E(x + dx, dy, 5, 4, "#9a2a20", "#7a1a12", 0.8)]
        lines = title.split("\n")
        b += [TL(x + 20, 44, lines, 7, "middle", "#111", "bold")]
        b += [T(x + 20, 178, "clumping" if clump else "no clumping", 7.2, "middle", RED_ if clump else "#2a7a3a", "bold")]
    b += [R(266, 18, 198, 176, "#f4f8fd", "#9db7d4", 1, 4), T(365, 31, "Results for each blood group", 8, fill=NAVY, weight="bold")]
    rows = [("Group", "Anti-A", "Anti-B"), ("A", "clumps", "no"), ("B", "no", "clumps"), ("AB", "clumps", "clumps"), ("O", "no", "no")]
    for i, (g, a, c) in enumerate(rows):
        y = 40 + i * 22
        fill = "#d6e5f4" if i == 0 else ("#fff7d6" if g == "B" else "#fff")
        b += [R(276, y, 56, 20, fill, "#444", 0.8, 0), R(332, y, 62, 20, fill, "#444", 0.8, 0), R(394, y, 62, 20, fill, "#444", 0.8, 0)]
        b += [T(304, y + 13, g, 7.6, weight="bold"), T(363, y + 13, a, 7.4, fill=RED_ if a == "clumps" else "#111"), T(425, y + 13, c, 7.4, fill=RED_ if c == "clumps" else "#111")]
    b += [T(365, 164, "X: no clumping with A, clumping with B", 6.8, fill=RED_, weight="bold"), T(365, 176, "→ X has B antigen = blood group B", 6.8, fill=RED_, weight="bold")]
    b += [T(365, 188, "can receive from B and O; give to B and AB", 6.4, fill="#444")]
    save("b_blood_test", 470, 200, "".join(b))


def nephron():
    b = [T(235, 12, "The nephron (draw and label)", 9.5, fill=NAVY, weight="bold")]
    # capsule + glomerulus
    b += [C(104, 66, 25, "#fff6e6", "#8a5a1a", 2)]
    b += [P("M96,56 C104,48 116,54 110,62 C104,70 96,64 104,58 C112,70 100,78 94,70 C90,64 96,58 96,56 Z", "#ff9a8a", "#b3211b", 1.2)]
    b += [P("M40,50 L88,60", "none", "#d9544a", 5), P("M40,82 L88,74", "none", "#7a9ad9", 4)]
    b += [T(30, 48, "afferent", 6.2, "end", "#b3211b"), T(30, 56, "arteriole", 6.2, "end", "#b3211b"), T(30, 90, "efferent", 6.2, "end", "#4a6ac0"), T(30, 98, "arteriole", 6.2, "end", "#4a6ac0")]
    tube = "#c28a2a"
    # PCT (coiled) then descending limb, U, ascending limb, DCT, collecting duct
    b += [P("M104,91 C92,98 118,100 104,108 C92,114 118,118 104,126 L104,132", "none", tube, 5)]
    b += [P("M104,132 L104,246 C104,262 140,262 140,246 L140,150", "none", tube, 5)]
    b += [P("M140,150 C150,140 150,160 160,150 C172,140 172,160 182,150 L214,150", "none", tube, 5)]
    b += [P("M214,150 L214,60 L250,60 L250,100 L250,258", "none", tube, 5)]
    b += [P("M104,132 L104,246", "none", "#e6c07a", 1.4, "3 3")]
    # labels
    b += [lab(122, 38, 110, 52, "glomerulus", "start", 7.2, RED_, "bold")]
    b += [lab(30, 126, 104, 68, "", "start")] if False else []
    b += [lab(176, 96, 126, 66, "Bowman’s capsule", "start", 7.4, "#8a5a1a", "bold")]
    b += [lab(52, 112, 95, 108, "PCT", "end", 7.4, "#111", "bold")]
    b += [lab(86, 190, 104, 190, "descending limb", "end", 7.2)]
    b += [lab(160, 208, 140, 208, "ascending limb", "start", 7.2)]
    b += [lab(130, 276, 122, 262, "Loop of Henle", "middle", 7.6, "#111", "bold")]
    b += [lab(160, 138, 160, 148, "DCT", "middle", 7.4, "#111", "bold")]
    b += [lab(262, 100, 252, 100, "Collecting duct", "start", 7.4, "#111", "bold")]
    b += [arrow(250, 232, 250, 270, "#333", 2), T(258, 266, "urine to ureter", 6.8, "start", "#333")]
    # function notes
    notes = [(270, 150, "Filtration: water, glucose, urea, salts"), (270, 160, "pass into capsule (cells and proteins stay)")]
    b += [R(298, 150, 168, 100, "#f4f8fd", "#9db7d4", 1, 4), TL(382, 178, ["Glomerulus + capsule: filtration", "PCT: glucose, amino acids, Na⁺,", "most water reabsorbed", "Loop of Henle: salt gradient;", "water leaves descending limb", "DCT: Na⁺ (aldosterone), water (ADH);", "urea, K⁺ secreted"], 6.4, "middle", "#111", "normal", 11)]
    b += [T(382, 164, "What each part does", 7.4, fill=NAVY, weight="bold")]
    save("b_nephron", 470, 290, "".join(b))


def urine_flow():
    b = [T(235, 12, "How urine is formed", 9.5, fill=NAVY, weight="bold")]
    steps = [("BLOOD in glomerulus", "high pressure", "#b3211b", "#ffe8e8"), ("1 FILTRATION", "water, glucose, urea, salts → capsule", "#1f5fa8", "#eaf3ff"), ("PRIMARY URINE", "glomerular filtrate", "#555", "#f4f4f4"),
             ("2 REABSORPTION", "PCT: glucose, amino acids, Na⁺, water", "#2a7a3a", "#eaf6ec"), ("LOOP OF HENLE", "water + salt reabsorbed", "#2a7a3a", "#eaf6ec"), ("3 DCT", "Na⁺ (aldosterone), water (ADH) in;", "#a05a00", "#fff4e0")]
    x0, y0, w, h = 8, 24, 146, 40
    pos = [(8, 24), (164, 24), (320, 24), (320, 84), (164, 84), (8, 84)]
    for i, ((t, s, c, f), (x, y)) in enumerate(zip(steps, pos)):
        b += [R(x, y, 142, 44, f, c, 1.5, 4), T(x + 71, y + 15, t, 7.6, fill=c, weight="bold"), TL(x + 71, y + 27, [s], 6.2, "middle", "#222")]
    b += [arrow(150, 46, 162, 46), arrow(306, 46, 318, 46), arrow(391, 70, 391, 82), arrow(318, 106, 308, 106), arrow(162, 106, 152, 106)]
    b += [R(8, 140, 142, 44, "#fff4e0", "#a05a00", 1.5, 4), TL(79, 155, ["secretion into tubule:", "urea, uric acid, creatinine, K⁺"], 6.4, "middle", "#a05a00", "bold", 9.5)]
    b += [R(164, 140, 142, 44, "#fffbe0", "#b3a000", 1.5, 4), TL(235, 155, ["COLLECTING DUCT", "ADH: more water back to blood"], 6.4, "middle", "#7a6a00", "bold", 9.5)]
    b += [R(320, 140, 142, 44, "#fff3b0", "#b3a000", 1.8, 4), TL(391, 158, ["URINE", "ureter → bladder → urethra"], 7, "middle", "#7a6a00", "bold", 10)]
    b += [arrow(79, 128, 79, 138), arrow(150, 162, 162, 162), arrow(306, 162, 318, 162), L(79, 128, 79, 116, "#333", 1.5)]
    b += [TL(235, 200, textwrap.wrap("Little water in the body → more ADH → more water reabsorbed → small volume of concentrated urine (P23 Q5a)", 80), 6.6, "middle", RED_, "bold")]
    save("b_urine_flow", 470, 222, "".join(b))


def reflex():
    b = [T(235, 12, "Reflex arc: pulling the hand from a hot stove", 9.5, fill=NAVY, weight="bold")]
    items = [("STIMULUS", "hot stove", "#b3211b", "#ffe8e8"), ("RECEPTOR", "pain / heat\nreceptor in skin", "#1f5fa8", "#eaf3ff"), ("SENSORY\nNEURON", "carries signal\nto spinal cord", "#1f5fa8", "#eaf3ff"),
             ("INTER-\nNEURON", "(relay neuron) in\nspinal cord", "#7a3b9b", "#f3eaff"), ("MOTOR\nNEURON", "carries signal\nto muscle", "#2a7a3a", "#eaf6ec"), ("EFFECTOR", "arm muscle\ncontracts", "#2a7a3a", "#eaf6ec")]
    n = len(items)
    w, gap = 66, 11.4
    for i, (t, s, c, f) in enumerate(items):
        x = 4 + i * (w + gap)
        b += [R(x, 40, w, 74, f, c, 1.6, 5)]
        b += [TL(x + w / 2, 55 if "\n" in t else 62, t.split("\n"), 7.4, "middle", c, "bold", 9), TL(x + w / 2, 90, s.split("\n"), 6.2, "middle", "#222", "normal", 8.5)]
        if i < n - 1:
            b += [arrow(x + w + 1, 77, x + w + gap - 1, 77, "#333", 1.8)]
    b += [T(462, 134, "RESPONSE: the hand is pulled away", 8.2, "end", "#2a7a3a", "bold")]
    b += [R(184, 150, 170, 34, "#fffbe9", "#b3a000", 1.2, 4), TL(269, 163, ["BRAIN is told afterwards (dotted line):", "you feel the pain → the reflex itself is faster, brain not in the first pathway"], 6.2, "middle", "#444", "normal", 9)]
    b += [L(269, 150, 269, 116, "#b3a000", 1.4, "3 2", True)]
    b += [T(235, 200, "Receptor → sensory neuron → interneuron → motor neuron → effector  (P25 Q1a(xxi): option C)", 6.8, fill=RED_, weight="bold")]
    save("b_reflex", 470, 208, "".join(b))


def computer():
    b = [T(235, 12, "The nervous system works like a computer", 9.5, fill=NAVY, weight="bold")]
    b += [T(10, 34, "COMPUTER", 8, "start", "#555", "bold"), T(10, 118, "HUMAN BODY", 8, "start", "#555", "bold")]
    top = [("INPUT", "keyboard, mouse,\nsensors", 10), ("CPU", "processing", 170), ("OUTPUT", "monitor, speaker", 330)]
    bot = [("RECEPTORS", "eye, ear, skin, nose,\ntongue (+ sensory neurons)", 10), ("BRAIN + SPINAL CORD", "processing (CNS)", 170), ("EFFECTORS", "muscles, glands\n(via motor neurons)", 330)]
    for (t, s, x), (t2, s2, x2) in zip(top, bot):
        b += [R(x, 40, 130, 50, "#eaf3ff", "#1f5fa8", 1.6, 5), T(x + 65, 55, t, 8, fill="#1f5fa8", weight="bold"), TL(x + 65, 67, s.split("\n"), 6.4, "middle", "#222", "normal", 8.5)]
        b += [R(x2, 124, 130, 50, "#eaf6ec", "#2a7a3a", 1.6, 5), T(x2 + 65, 139, t2, 7.4, fill="#2a7a3a", weight="bold"), TL(x2 + 65, 151, s2.split("\n"), 6.4, "middle", "#222", "normal", 8.5)]
        b += [L(x + 65, 90, x2 + 65, 124, "#999", 1.2, "3 2")]
    b += [arrow(141, 65, 169, 65, "#1f5fa8"), arrow(301, 65, 329, 65, "#1f5fa8"), arrow(141, 149, 169, 149, "#2a7a3a"), arrow(301, 149, 329, 149, "#2a7a3a")]
    b += [R(170, 94, 130, 22, "#fff4e0", "#a05a00", 1.2, 4), T(235, 108, "Hard disk = memory in the brain", 6.8, fill="#a05a00", weight="bold")]
    b += [T(235, 192, "Both use electrical signals.  A computer cannot make its own decisions; it follows a program.", 6.8, fill="#444")]
    save("b_computer", 470, 200, "".join(b))


if __name__ == "__main__":
    blood_chart(); blood_test(); nephron(); urine_flow(); reflex(); computer()
