#!/usr/bin/env python3
"""Biology diagrams, part 1: cells, transport, photosynthesis, plant transport, digestion."""
from bio_lib import *

RED_ = "#b3211b"


def cells():
    b = [T(235, 12, "Prokaryotic cell and eukaryotic cell", 9.5, fill=NAVY, weight="bold")]
    # ---- bacterium (left)
    b += [panel(6, 18, 228, 214, "Prokaryotic cell (bacterium)")]
    b += [R(18, 78, 130, 70, "#fff7d6", "#8a7a3a", 1.2, 35)]            # capsule
    b += [R(22, 82, 122, 62, "#fffbe9", "#6b5a1e", 1.6, 31)]             # cell wall
    b += [R(26, 86, 114, 54, "#fffdf3", "#333", 1.1, 27)]                # membrane
    b += [P("M62,104 C66,96 74,98 78,104 C84,100 92,106 88,114 C94,120 84,128 78,122 C72,128 62,124 66,116 C58,112 60,108 62,104 Z", "#d9ecff", "#1f5fa8", 1.4)]
    b += [P("M66,108 C72,104 78,110 72,114 M72,118 C78,114 84,120 80,122", "none", "#1f5fa8", 0.9)]
    b += [C(108, 104, 4.5, "#fff", "#7a3b9b", 1.2), C(46, 118, 4.5, "#fff", "#7a3b9b", 1.2)]
    for (x, y) in [(40, 98), (50, 108), (98, 92), (108, 120), (118, 108), (126, 96), (54, 128), (98, 130), (118, 128), (36, 108), (126, 120)]:
        b += [C(x, y, 1.5, "#444", "#444", 0)]
    b += [P("M144,113 C158,96 170,132 184,110 C196,92 206,118 218,100", "none", "#555", 2)]   # flagellum
    for k in range(6):
        x = 34 + k * 20
        b += [L(x, 80, x - 1, 73, "#666", 0.8), L(x, 148, x - 1, 155, "#666", 0.8)]          # pili
    b += [lab(34, 54, 36, 79, "Capsule"), lab(78, 54, 78, 83, "Cell wall"), lab(150, 54, 128, 87, "Cell membrane")]
    b += [lab(203, 64, 203, 104, "Flagellum")]
    b += [lab(42, 178, 42, 135, "Pili"), lab(78, 178, 78, 118, "NUCLEOID", "middle", 8, RED_, "bold"), T(78, 188, "(DNA, no nuclear membrane)", 6.2, fill=RED_), lab(120, 168, 108, 108, "Plasmid"), lab(176, 168, 120, 130, "Ribosomes")]
    b += [T(120, 218, "unique to prokaryotes: nucleoid, plasmid", 6.8, fill="#444", style="italic")]
    # ---- animal cell (right)
    b += [panel(240, 18, 224, 214, "Eukaryotic cell (animal)")]
    b += [E(352, 125, 100, 62, "#fff1ee", "#9b3b2a", 1.8)]
    b += [C(330, 120, 27, "#d9ecff", "#1f5fa8", 1.6), C(336, 118, 8, "#8fb8e8", "#1f5fa8", 1)]
    b += [P("M366,112 C376,104 392,106 398,116", "none", "#6b5a1e", 1.2), P("M368,124 C378,132 392,130 398,124", "none", "#6b5a1e", 1.2)]  # ER lines
    b += [E(386, 148, 14, 8, "#ffd9a8", "#a05a00", 1.2, -20), P("M378,150 L384,146 L390,152 L396,146", "none", "#a05a00", 0.9)]
    b += [E(304, 148, 12, 7, "#ffd9a8", "#a05a00", 1.2, 15), P("M297,148 L302,145 L306,150 L311,146", "none", "#a05a00", 0.9)]
    b += [P("M356,150 C366,146 378,146 388,150 M358,156 C368,152 380,152 390,156 M360,162 C370,158 382,158 392,162", "none", "#2a7a3a", 1.3)]  # Golgi
    for (x, y) in [(300, 100), (312, 92), (354, 94), (340, 150), (410, 120), (292, 126), (420, 130), (330, 168)]:
        b += [C(x, y, 1.6, "#444", "#444", 0)]
    b += [lab(290, 54, 275, 100, "Cell membrane"), lab(352, 54, 352, 80, "Cytoplasm"), lab(414, 54, 396, 108, "Rough ER")]
    b += [lab(268, 196, 304, 152, "Mitochondrion"), lab(352, 204, 332, 140, "NUCLEUS (with membrane)", "middle", 7.4, "#1f5fa8", "bold"), lab(430, 196, 382, 158, "Golgi body")]
    save("b_cells", 470, 236, "".join(b))


def transport():
    W = 470
    b = [T(235, 12, "Types of membrane transport", 9.5, fill=NAVY, weight="bold")]
    xs = [8, 125, 242, 359]
    titles = ["Simple diffusion", "Facilitated diffusion", "Osmosis (water)", "Active transport"]
    subs = ["high → low, no energy", "through a protein, no ATP", "low solute → high solute", "low → high, uses ATP"]
    for i, x in enumerate(xs):
        b += [panel(x, 18, 103, 196, titles[i], NAVY), T(x + 51.5, 39, subs[i], 6.2, fill="#444", style="italic")]
        # membrane (bilayer) horizontal at y=110
        mx0, mx1 = x + 6, x + 97
        for k in range(8):
            cx = mx0 + 6 + k * 11.2
            if i in (1, 3) and 3 <= k <= 4:
                continue
            b += [C(cx, 106, 3.4, "#fde3a7", "#a05a00", 0.8), C(cx, 116, 3.4, "#fde3a7", "#a05a00", 0.8)]
        if i == 1:
            b += [R(x + 38, 98, 28, 26, "#cfe3ff", "#1f5fa8", 1.2, 6), T(x + 52, 114, "carrier", 6, fill="#1f5fa8")]
        if i == 3:
            b += [R(x + 36, 96, 32, 30, "#d9f2dc", "#2a7a3a", 1.2, 6), T(x + 52, 112, "pump", 6.2, fill="#2a7a3a"), R(x + 70, 134, 24, 11, "#fff2b3", "#a05a00", 1, 3), T(x + 82, 142.5, "ATP", 6.6, fill="#a05a00", weight="bold")]
    # panel 1 dots
    for (px, py) in [(20, 50), (40, 60), (30, 78), (62, 52), (78, 70), (86, 46)]:
        b += [C(xs[0] + px, py + 8, 3.2, "#c33", "#822", 0.6)]
    for (px, py) in [(40, 150), (70, 170)]:
        b += [C(xs[0] + px, py + 10, 3.2, "#c33", "#822", 0.6)]
    b += [L(xs[0] + 52, 78, xs[0] + 52, 100, RED_, 1.6, None, True), L(xs[0] + 52, 126, xs[0] + 52, 160, RED_, 1.6, None, True)]
    b += [T(xs[0] + 20, 207, "High conc.", 6.4, fill="#444"), T(xs[0] + 82, 207, "Low conc.", 6.4, fill="#444")]
    # panel 2
    for (px, py) in [(20, 52), (40, 64), (30, 80), (64, 54), (80, 74), (88, 50), (50, 40)]:
        b += [C(xs[1] + px, py + 8, 3.2, "#c33", "#822", 0.6)]
    b += [C(xs[1] + 52, 150, 3.2, "#c33", "#822", 0.6), C(xs[1] + 30, 172, 3.2, "#c33", "#822", 0.6)]
    b += [L(xs[1] + 52, 82, xs[1] + 52, 98, RED_, 1.6, None, True), L(xs[1] + 52, 126, xs[1] + 52, 160, RED_, 1.6, None, True)]
    # panel 3 : water blue dots, solute big dots
    for (px, py) in [(18, 160), (30, 172), (44, 160), (62, 170), (76, 160), (86, 174), (24, 186), (52, 188), (70, 190)]:
        b += [C(xs[2] + px, py, 2.4, "#4aa3e0", "#1f5fa8", 0.5)]
    for (px, py) in [(26, 54), (50, 48), (70, 58), (40, 72), (84, 76), (58, 90)]:
        b += [C(xs[2] + px, py + 4, 4.2, "#c33", "#822", 0.6)]
    for (px, py) in [(20, 66), (74, 46), (90, 62)]:
        b += [C(xs[2] + px, py + 4, 2.4, "#4aa3e0", "#1f5fa8", 0.5)]
    b += [L(xs[2] + 52, 150, xs[2] + 52, 126, "#1f5fa8", 1.8, None, True), T(xs[2] + 52, 205, "water in (more solute above)", 6, fill="#1f5fa8")]
    # panel 4
    for (px, py) in [(20, 160), (34, 172), (50, 160), (64, 176), (82, 162), (26, 186), (74, 190), (46, 190), (90, 182)]:
        b += [C(xs[3] + px, py, 3.2, "#c33", "#822", 0.6)]
    for (px, py) in [(26, 56), (50, 48), (74, 60)]:
        b += [C(xs[3] + px, py + 6, 3.2, "#c33", "#822", 0.6)]
    b += [L(xs[3] + 52, 150, xs[3] + 52, 126, RED_, 1.8, None, True), T(xs[3] + 20, 207, "Low conc.", 6.4, fill="#444"), T(xs[3] + 82, 207, "High conc.", 6.4, fill="#444")]
    b += [TL(235, 228, textwrap.wrap("Passive (no energy): diffusion, facilitated diffusion, osmosis  •  Active: needs ATP and carrier protein, moves against the gradient", 88), 6.8, "middle", "#444")]
    save("b_transport", W, 246, "".join(b))


def tonicity():
    b = [T(235, 12, "Effect of the outside solution on animal and plant cells", 9.5, fill=NAVY, weight="bold")]
    cols = [("Hypotonic", "(more dilute outside)", "water IN"), ("Isotonic", "(same concentration)", "no net movement"), ("Hypertonic", "(more concentrated outside)", "water OUT")]
    for i, (t, s, w) in enumerate(cols):
        x = 8 + i * 154
        b += [panel(x, 18, 148, 200, t), T(x + 74, 39, s, 6.4, fill="#444", style="italic")]
        cx = x + 74
        # animal cell
        if i == 0:
            b += [C(cx, 70, 26, "#ffe3e0", "#9b3b2a", 1.8), C(cx, 70, 8, "#d9ecff", "#1f5fa8", 1)]
            b += [T(cx, 108, "swells, may burst (lysis)", 6.8, fill=RED_)]
        elif i == 1:
            b += [C(cx, 70, 20, "#ffe3e0", "#9b3b2a", 1.8), C(cx, 70, 6, "#d9ecff", "#1f5fa8", 1)]
            b += [T(cx, 108, "normal", 6.8, fill="#2a7a3a")]
        else:
            b += [P(f"M{cx-16},70 C{cx-12},56 {cx-6},52 {cx},58 C{cx+6},50 {cx+14},56 {cx+16},68 C{cx+20},78 {cx+8},86 {cx+2},82 C{cx-4},90 {cx-14},84 {cx-16},70 Z", "#ffe3e0", "#9b3b2a", 1.8), C(cx, 70, 4, "#d9ecff", "#1f5fa8", 1)]
            b += [T(cx, 108, "shrinks (crenation)", 6.8, fill=RED_)]
        b += [T(x + 20, 50, "Animal", 6.8, "start", "#444", "bold")]
        # plant cell
        b += [T(x + 20, 130, "Plant", 6.8, "start", "#444", "bold")]
        wall = R(cx - 28, 138, 56, 42, "#fff", "#2a7a3a", 2.4, 5) if i != 2 else R(cx - 28, 138, 56, 42, "#fff", "#2a7a3a", 2.4, 5)
        b += [wall]
        if i == 0:
            b += [R(cx - 26, 140, 52, 38, "#c9efc9", "#2a7a3a", 1, 4), T(cx, 200, "turgid (firm)", 6.8, fill="#2a7a3a")]
        elif i == 1:
            b += [R(cx - 23, 143, 46, 32, "#c9efc9", "#2a7a3a", 1, 4), T(cx, 200, "flaccid / normal", 6.8, fill="#444")]
        else:
            b += [R(cx - 14, 150, 28, 20, "#c9efc9", "#2a7a3a", 1, 6), T(cx, 200, "plasmolysed (wilts)", 6.8, fill=RED_)]
        b += [T(cx, 213, w, 6.6, fill="#1f5fa8", weight="bold")]
    save("b_tonicity", 470, 224, "".join(b))


def osmoscope():
    b = [T(235, 12, "Potato osmoscope", 9.5, fill=NAVY, weight="bold")]
    for k, (x, lvl, title) in enumerate([(10, 120, "(A) Before"), (250, 96, "(B) After 1 hour")]):
        b += [panel(x, 18, 216, 190, title)]
        bx = x + 50
        b += [R(bx, 52, 116, 130, "#eaf6ff", "#555", 1.5, 6)]                      # beaker
        b += [Q(bx + 1.5, 142, 113, 38, "#bfe0f7", "#bfe0f7", 0)]                  # water in beaker
        b += [P(f"M{bx+22},182 L{bx+22},92 Q{bx+22},84 {bx+30},84 L{bx+86},84 Q{bx+94},84 {bx+94},92 L{bx+94},182 Z", "#e6c98a", "#8a6a2a", 1.6)]   # potato
        b += [Q(bx + 46, 108, 24, 74, "#fff", "#8a6a2a", 1.2)]                       # cavity
        b += [Q(bx + 47, lvl, 22, 182 - lvl, "#f5b9b9", "#f5b9b9", 0)]               # sugar solution
        b += [L(bx + 20, lvl, bx + 80, lvl, "#c00", 1, "3 2")]
        b += [L(bx + 66, 62, bx + 52, lvl - 2, "#333", 1.8)]                         # pin
        b += [T(bx + 76, 60, "pin", 6.6, "start")]
    b += [lab(16, 134, 106, 120, "initial level", "start", 6.6, "#c00"), lab(16, 46, 62, 76, "beaker", "start", 6.8), lab(176, 78, 150, 100, "potato", "start", 6.8)]
    b += [lab(45, 200, 70, 168, "Y: water", "middle", 7, RED_, "bold"), lab(158, 200, 120, 162, "X: sugar (salt) solution", "middle", 7, RED_, "bold")]
    b += [lab(256, 134, 346, 96, "initial level", "start", 6.6, "#c00"), T(358, 202, "level rises: water enters by osmosis", 7, fill="#1f5fa8", weight="bold")]
    save("b_osmoscope", 470, 214, "".join(b))


def potato_graph():
    W, H = 470, 200
    b = [T(235, 12, "Potato cubes in sugar solutions (P25 Q4b)", 9.5, fill=NAVY, weight="bold")]
    ox, oy, gw, gh = 60, 170, 250, 130
    # grid
    for k in range(0, 8):
        y = oy - k * gh / 7
        b += [L(ox, y, ox + gw, y, "#ddd", 0.6), T(ox - 6, y + 2.5, str(k), 6.8, "end")]
    for k, c in enumerate([5, 10, 15, 20, 25, 30]):
        x = ox + 22 + k * 42
        b += [L(x, oy, x, oy - gh, "#eee", 0.6), T(x, oy + 11, str(c), 6.8)]
    b += [L(ox, oy, ox, oy - gh, "#222", 1.3), L(ox, oy, ox + gw, oy, "#222", 1.3)]
    pts = [(ox + 22 + k * 42, oy - v * gh / 7) for k, v in enumerate([6, 5, 4, 3, 2, 1])]
    b += [L(*pts[0], *pts[-1], "#1f5fa8", 1.8)]
    for (x, y) in pts:
        b += [T(x, y + 3, "×", 10, fill="#1f5fa8", weight="bold")]
    b += [L(ox, oy - 4 * gh / 7, pts[2][0], pts[2][1], RED_, 1, "3 2"), L(pts[2][0], pts[2][1], pts[2][0], oy, RED_, 1, "3 2")]
    b += [T(pts[2][0] + 6, pts[2][1] - 6, "isotonic: 4 cm³, 15 g/100 ml", 7, "start", RED_, "bold")]
    b += [T(ox + gw / 2, oy + 24, "Concentration of sugar solution (g/100 ml)", 7.4), T(16, oy - gh / 2, "Final size (cm³)", 7.4)]
    b = b[:-1] + ['<text x="16" y="%s" font-size="7.4" text-anchor="middle" transform="rotate(-90 16 %s)">Final size of potato cube (cm³)</text>' % (oy - gh / 2, oy - gh / 2)]
    b += [R(330, 40, 132, 112, "#f4f8fd", "#9db7d4", 1, 4)]
    b += [TL(396, 70, ["Above 4 cm³: cube gained water", "(hypotonic solution)", "Equal to 4 cm³: isotonic", "(no net movement)", "Below 4 cm³: cube lost water", "(hypertonic solution)"], 7, "middle", "#111", "normal", 10.5)]
    b += [T(396, 56, "Reading the graph", 7.6, fill=NAVY, weight="bold")]
    save("b_potato_graph", W, H, "".join(b))


if __name__ == "__main__":
    cells(); transport(); tonicity(); osmoscope(); potato_graph()
