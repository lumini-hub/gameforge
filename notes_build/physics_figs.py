#!/usr/bin/env python3
"""Generates the physics diagrams as SVG files in figs/ (hand-written SVG, no external libs)."""
import math, pathlib

OUT = pathlib.Path(__file__).parent / "figs"
OUT.mkdir(exist_ok=True)
NAVY, TEAL, GOLD, RED, GREY, GREEN = "#1b3a6b", "#0f6b63", "#8a4b00", "#b3261e", "#666", "#2e7d32"
FONT = 'font-family="Liberation Sans, Arial, sans-serif"'
DEFS = ('<defs>'
        '<marker id="a" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="context-stroke"/></marker>'
        '</defs>')


def save(name, w, h, body):
    (OUT / f"{name}.svg").write_text(f'<svg viewBox="0 0 {w} {h}" width="{w}" xmlns="http://www.w3.org/2000/svg" {FONT}>{DEFS}{body}</svg>', encoding="utf-8")


def T(x, y, s, size=11, anchor="middle", fill="#1d1d1d", weight="normal", style="normal", rot=None):
    tr = f' transform="rotate({rot} {x} {y})"' if rot is not None else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{fill}" font-weight="{weight}" font-style="{style}"{tr}>{s}</text>'


def L(x1, y1, x2, y2, c="#333", w=1.6, dash=None, arrow=False):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = ' marker-end="url(#a)"' if arrow else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}"{d}{m}/>'


def R(x, y, w, h, fill="none", stroke="#333", sw=1.6, rx=0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def C(x, y, r, fill="none", stroke="#333", sw=1.6):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def P(d, fill="none", stroke="#333", sw=1.8, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{da}/>'


def poly(pts, fill="none", stroke="#333", sw=1.8):
    return f'<polygon points="{" ".join(f"{x},{y}" for x, y in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def wave(x0, x1, y, amp, cycles, steps=240, phase=0):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        pts.append(f"{x0 + (x1 - x0) * t:.1f},{y - amp * math.sin(2 * math.pi * cycles * t + phase):.1f}")
    return "M" + " L".join(pts)


# ---------------------------------------------------------------- 1 moment (see-saw)
def fig_moment():
    b = []
    b.append(poly([(300, 150), (280, 185), (320, 185)], "#ddd"))
    b.append(L(60, 150, 540, 150, "#8a4b00", 7))
    b.append(L(60, 185, 540, 185, "#888", 1))
    b.append(L(190, 100, 190, 145, RED, 2.5, arrow=True)); b.append(T(190, 92, "Pema 250 N", 11, fill=RED, weight="bold"))
    b.append(L(480, 100, 480, 145, NAVY, 2.5, arrow=True)); b.append(T(480, 92, "Dema 450 N", 11, fill=NAVY, weight="bold"))
    b.append(L(190, 208, 298, 208, "#555", 1.2, arrow=True)); b.append(L(298, 208, 190, 208, "#555", 1.2, arrow=True)); b.append(T(244, 224, "d = ? (3.6 m)", 11))
    b.append(L(302, 208, 480, 208, "#555", 1.2, arrow=True)); b.append(L(480, 208, 302, 208, "#555", 1.2, arrow=True)); b.append(T(391, 224, "2 m", 11))
    b.append(T(300, 205, "", 10))
    b.append(T(300, 260, "Principle of moments:  clockwise moment = anticlockwise moment", 12, weight="bold", fill=NAVY))
    b.append(T(300, 280, "450 N x 2 m = 250 N x d   =>   d = 900 / 250 = 3.6 m", 12))
    b.append(T(300, 125, "pivot", 10, fill=GREY)); b.append(L(300, 128, 300, 146, GREY, 1, arrow=True))
    save("moment", 600, 295, "".join(b))


# ---------------------------------------------------------------- 2 couple
def fig_couple():
    b = []
    # left: moment of force (spanner on nut)
    b.append(T(150, 22, "Moment of a force", 13, weight="bold", fill=NAVY))
    b.append(C(70, 110, 16, "#bbb"))
    b.append(R(70, 103, 160, 14, "#cfcfcf", "#555", 1.5, 4))
    b.append(L(222, 160, 222, 122, RED, 2.5, arrow=True)); b.append(T(236, 150, "F", 12, fill=RED, weight="bold", anchor="start"))
    b.append(L(70, 150, 222, 150, "#555", 1.2, arrow=True)); b.append(T(146, 168, "perpendicular distance d", 10))
    b.append(T(150, 200, "Moment = F x d (about the nut)", 11, weight="bold"))
    b.append(T(150, 217, "one force: also tends to move the body", 10, fill=GREY))
    # right: couple (steering wheel)
    b.append(T(450, 22, "Moment of a couple", 13, weight="bold", fill=NAVY))
    b.append(C(450, 110, 62, "none", "#555", 5)); b.append(C(450, 110, 7, "#555"))
    b.append(L(450, 48, 450, 172, "#555", 3)); b.append(L(388, 110, 512, 110, "#555", 3))
    b.append(L(388, 135, 388, 85, RED, 2.5, arrow=True)); b.append(T(372, 112, "F", 12, fill=RED, weight="bold"))
    b.append(L(512, 85, 512, 135, RED, 2.5, arrow=True)); b.append(T(528, 112, "F", 12, fill=RED, weight="bold"))
    b.append(L(388, 188, 512, 188, "#555", 1.2, arrow=True)); b.append(L(512, 188, 388, 188, "#555", 1.2, arrow=True)); b.append(T(450, 204, "d", 11))
    b.append(T(450, 226, "Moment of couple = F x d (d = distance between the forces)", 11, weight="bold"))
    b.append(T(450, 243, "two equal, opposite, parallel forces: net force = 0, pure rotation", 10, fill=GREY))
    save("couple", 600, 255, "".join(b))


# ---------------------------------------------------------------- 3 equilibrium
def fig_equilibrium():
    b = []
    xs = [100, 300, 500]
    titles = ["STABLE", "UNSTABLE", "NEUTRAL"]
    notes = ["returns to original position", "falls further away", "stays in the new position"]
    cols = [TEAL, RED, GOLD]
    # bowl
    b.append(P("M30,70 Q100,150 170,70", "none", "#555", 3)); b.append(C(100, 112, 13, "#7aa6d8", NAVY)); b.append(L(70, 108, 52, 92, GREEN, 2, arrow=True)); b.append(L(130, 108, 148, 92, GREEN, 2, arrow=True))
    # hill
    b.append(P("M230,130 Q300,50 370,130", "none", "#555", 3)); b.append(C(300, 63, 13, "#7aa6d8", NAVY)); b.append(L(318, 74, 340, 100, RED, 2, arrow=True)); b.append(L(282, 74, 260, 100, RED, 2, arrow=True))
    # flat
    b.append(L(430, 125, 570, 125, "#555", 3)); b.append(C(500, 112, 13, "#7aa6d8", NAVY)); b.append(C(540, 112, 13, "none", "#999", 1.2)); b.append(L(515, 112, 526, 112, GOLD, 2, arrow=True))
    for x, t, n, c in zip(xs, titles, notes, cols):
        b.append(T(x, 170, t + " equilibrium", 12, weight="bold", fill=c))
        b.append(T(x, 187, n, 10.5))
    b.append(T(100, 205, "C.G. rises when displaced", 10, fill=GREY)); b.append(T(300, 205, "C.G. falls when displaced", 10, fill=GREY)); b.append(T(500, 205, "C.G. stays at the same height", 10, fill=GREY))
    b.append(T(100, 222, "(bottle standing upright)", 10, fill=GREY)); b.append(T(300, 222, "(pencil on its tip)", 10, fill=GREY)); b.append(T(500, 222, "(bottle lying on its side, ball)", 10, fill=GREY))
    save("equilibrium", 600, 235, "".join(b))


# ---------------------------------------------------------------- 4 stability
def fig_stability():
    b = []
    # low wide cone
    b.append(T(110, 20, "More STABLE", 13, weight="bold", fill=TEAL)); b.append(T(110, 36, "low C.G., wide base", 10.5))
    b.append(poly([(40, 170), (180, 170), (110, 90)], "#dbe7f7", NAVY)); b.append(C(110, 148, 4.5, RED, RED)); b.append(T(124, 146, "C.G.", 10, anchor="start", fill=RED))
    b.append(L(110, 148, 110, 188, RED, 1.4, dash="4 3", arrow=True)); b.append(T(110, 202, "line of action falls well inside base", 10))
    # tall narrow
    b.append(T(300, 20, "LESS STABLE", 13, weight="bold", fill=RED)); b.append(T(300, 36, "high C.G., narrow base", 10.5))
    b.append(R(270, 60, 60, 110, "#f7dcdc", NAVY)); b.append(C(300, 90, 4.5, RED, RED)); b.append(T(314, 88, "C.G.", 10, anchor="start", fill=RED))
    b.append(L(300, 90, 300, 188, RED, 1.4, dash="4 3", arrow=True)); b.append(T(300, 202, "close to the edge of the base", 10))
    # tilting
    b.append(T(500, 20, "Toppling", 13, weight="bold", fill=GOLD)); b.append(T(500, 36, "line of action leaves the base", 10.5))
    b.append(poly([(470, 170), (530, 170), (545, 110), (485, 110)], "#fff1d6", NAVY).replace('points="', 'points="').replace("470,170 530,170 545,110 485,110", "470,170 535,150 585,100 520,80"))
    b.append(L(450, 170, 560, 170, "#555", 2)); b.append(C(528, 112, 4.5, RED, RED)); b.append(L(528, 112, 528, 188, RED, 1.4, dash="4 3", arrow=True)); b.append(T(500, 202, "falls outside base -> topples", 10))
    b.append(T(300, 228, "Stability increases with: LOWER centre of gravity  +  LARGER base area", 12, weight="bold", fill=NAVY))
    save("stability", 600, 240, "".join(b))


# ---------------------------------------------------------------- 5 free fall + terminal velocity
def fig_freefall():
    b = []
    labels = [("START", "v = 0", 0, 52), ("SPEEDING UP", "weight > drag", 24, 52), ("TERMINAL VELOCITY", "weight = drag", 52, 52)]
    for i, (t, s, drag, w) in enumerate(labels):
        x = 55 + i * 100
        b.append(T(x, 18, t, 9.5, weight="bold", fill=NAVY)); b.append(T(x, 31, s, 9.5, fill=GREY))
        b.append(C(x, 120, 14, "#ffcc80", GOLD))
        b.append(L(x, 136, x, 136 + w, RED, 2.5, arrow=True)); b.append(T(x + 10, 136 + w, "W", 10, anchor="start", fill=RED, weight="bold"))
        if drag:
            b.append(L(x, 104, x, 104 - drag, NAVY, 2.5, arrow=True)); b.append(T(x + 10, 104 - drag + 6, "Drag", 10, anchor="start", fill=NAVY, weight="bold"))
    b.append(T(155, 214, "net force: W  ->  decreasing  ->  zero", 10, fill=GREY)); b.append(T(155, 228, "acceleration: g  ->  decreasing  ->  zero", 10, fill=GREY))
    # graph
    gx, gy, gw, gh = 380, 30, 200, 150
    b.append(L(gx, gy + gh, gx + gw, gy + gh, "#333", 1.6, arrow=True)); b.append(L(gx, gy + gh, gx, gy - 6, "#333", 1.6, arrow=True))
    b.append(T(gx + gw / 2, gy + gh + 22, "time", 11)); b.append(T(gx - 14, gy + 60, "velocity", 11, rot=-90))
    b.append(L(gx, gy + gh, gx + gw - 10, gy + 15, GREY, 1.6, dash="5 4")); b.append(T(gx + gw - 8, gy + 12, "no air resistance", 9.5, anchor="end", fill=GREY))
    pts = []
    for i in range(0, 101):
        t = i / 100
        v = 1 - math.exp(-3.2 * t)
        pts.append(f"{gx + t * (gw - 10):.1f},{gy + gh - v * (gh - 50):.1f}")
    b.append(P("M" + " L".join(pts), "none", NAVY, 2.6))
    b.append(L(gx, gy + gh - (gh - 50) * 0.97, gx + gw - 10, gy + gh - (gh - 50) * 0.97, TEAL, 1.2, dash="3 3")); b.append(T(gx + gw - 10, gy + gh - (gh - 50) - 4, "terminal velocity", 10, anchor="end", fill=TEAL, weight="bold"))
    b.append(T(gx + 130, gy + gh - 30, "with air resistance", 9.5, anchor="end", fill=NAVY))
    b.append(T(480, 232, "forces on a falling body and its velocity-time graph", 10, fill=GREY, style="italic"))
    save("freefall", 600, 245, "".join(b))


# ---------------------------------------------------------------- 6 energy efficient house (cold place)
def fig_house():
    b = []
    b.append(L(20, 200, 580, 200, "#6b8e23", 4))
    b.append(poly([(150, 90), (300, 30), (450, 90)], "#c9a27a", "#555", 2))
    b.append(R(170, 90, 260, 110, "#f3e3c3", "#555", 2))
    b.append(R(190, 110, 60, 50, "#bfe3f5", NAVY, 2)); b.append(L(220, 110, 220, 160, NAVY, 1.2)); b.append(L(190, 135, 250, 135, NAVY, 1.2))
    b.append(R(350, 110, 60, 50, "#bfe3f5", NAVY, 2)); b.append(L(380, 110, 380, 160, NAVY, 1.2)); b.append(L(350, 135, 410, 135, NAVY, 1.2))
    b.append(R(285, 130, 34, 70, "#8b5a2b", "#555", 2))
    b.append(poly([(236, 56), (236, 20), (262, 20), (262, 70)], "#aaa", "#555", 1.5))
    b.append(R(210, 78, 40, 16, "#2a4d8f", "#222", 1.5)); b.append(R(350, 70, 50, 20, "#2a4d8f", "#222", 1.5))
    for x0, y0, txt, tx, ty, anc in [
        (230, 75, "solar panels / solar water heater", 12, 40, "start"),
        (300, 45, "thick roof insulation", 300, 14, "middle"),
        (180, 150, "double-glazed windows", 20, 120, "start"),
        (170, 175, "thick insulated walls (cavity / wool / foam)", 20, 160, "start"),
        (300, 170, "draught-proofed door + porch", 300, 222, "middle"),
        (400, 135, "large south-facing windows (sunlight heating)", 632, 120, "end"),
        (430, 185, "stone / concrete floor stores heat", 632, 160, "end"),
    ]:
        b.append(L(x0, y0, tx + (8 if anc == "start" else -8 if anc == "end" else 0), ty + 4, "#999", 1))
        b.append(T(tx, ty, txt, 10.5, anchor=anc, fill=NAVY, weight="bold"))
    b.append(T(300, 240, "Also: LED lamps, 5-star appliances, thick curtains, heat-recovery stove", 10.5, fill=GREY))
    save("house", 640, 250, "".join(b))


# ---------------------------------------------------------------- 7 hydraulic press
def fig_hydraulic():
    b = []
    b.append(P("M120,190 L120,120 L170,120 L170,170 L360,170 L360,100 L470,100 L470,190 Z", "#cfe6fb", "#444", 2.5))
    b.append(R(120, 100, 50, 20, "#999", "#333", 1.5)); b.append(L(145, 100, 145, 60, "#333", 4))
    b.append(R(360, 80, 110, 20, "#999", "#333", 1.5)); b.append(L(415, 80, 415, 55, "#333", 6)); b.append(R(350, 40, 130, 15, "#777", "#333", 1.5))
    b.append(L(145, 20, 145, 56, RED, 3, arrow=True)); b.append(T(160, 30, "F1 (small effort)", 11, anchor="start", fill=RED, weight="bold"))
    b.append(L(415, 100, 415, 70, NAVY, 3, arrow=True))
    b.append(T(415, 30, "F2 (large load)", 11, fill=NAVY, weight="bold")); b.append(T(145, 207, "small piston, area A1", 11)); b.append(T(415, 207, "large piston, area A2", 11))
    b.append(T(250, 150, "liquid (incompressible)", 10.5, fill=NAVY, style="italic"))
    b.append(T(300, 232, "Pascal's law:  P1 = P2   =>   F1 / A1 = F2 / A2   =>   F2 = F1 x (A2 / A1)", 12, weight="bold", fill=NAVY))
    b.append(T(300, 250, "A2 > A1  =>  F2 > F1 : the machine is a FORCE MULTIPLIER (work in = work out: F1 d1 = F2 d2)", 10.5, fill=GREY))
    save("hydraulic", 600, 262, "".join(b))


# ---------------------------------------------------------------- 8 heating curve
def fig_heating():
    b = []
    gx, gy, gw, gh = 70, 20, 480, 190
    b.append(L(gx, gy + gh, gx + gw, gy + gh, "#333", 1.6, arrow=True)); b.append(L(gx, gy + gh, gx, gy - 6, "#333", 1.6, arrow=True))
    b.append(T(gx + gw / 2, gy + gh + 28, "heat supplied / time (constant heating rate)", 11)); b.append(T(24, gy + 90, "temperature (C)", 11, rot=-90))
    y0 = gy + gh - 60; y100 = gy + 35
    b.append(L(gx - 4, y0, gx + gw, y0, "#bbb", 1, dash="3 3")); b.append(T(gx - 8, y0 + 4, "0", 10, anchor="end"))
    b.append(L(gx - 4, y100, gx + gw, y100, "#bbb", 1, dash="3 3")); b.append(T(gx - 8, y100 + 4, "100", 10, anchor="end"))
    pts = [(gx, gy + gh - 20), (gx + 80, y0), (gx + 190, y0), (gx + 290, y100), (gx + 420, y100), (gx + 470, y100 - 25)]
    b.append(f'<polyline points="{" ".join(f"{x},{y}" for x, y in pts)}" fill="none" stroke="{NAVY}" stroke-width="3"/>')
    b.append(T(gx + 40, gy + gh - 45, "ice warms", 10, fill=TEAL, weight="bold")); b.append(T(gx + 135, y0 - 8, "ice melts", 10, fill=RED, weight="bold")); b.append(T(gx + 135, y0 + 14, "latent heat of fusion", 10, fill=RED)); b.append(T(gx + 135, y0 + 27, "(temperature constant)", 9.5, fill=GREY))
    b.append(T(gx + 220, gy + 120, "water warms", 10, fill=TEAL, weight="bold")); b.append(T(gx + 355, y100 - 8, "water boils", 10, fill=RED, weight="bold")); b.append(T(gx + 355, y100 + 14, "latent heat of vaporisation", 10, fill=RED)); b.append(T(gx + 355, y100 + 27, "(temperature constant)", 9.5, fill=GREY))
    b.append(T(gx + 470, y100 - 40, "steam", 10, fill=TEAL, weight="bold"))
    save("heating", 600, 260, "".join(b))


# ---------------------------------------------------------------- 9 calorimeter
def fig_calorimeter():
    b = []
    b.append(R(150, 70, 190, 150, "#fff3cd", "#555", 2))
    b.append(R(172, 90, 146, 130, "#ddd", "#555", 2)); b.append(R(184, 118, 122, 100, "#bfe3f5", NAVY, 1.5))
    b.append(L(190, 70, 300, 70, "#555", 6)); b.append(L(245, 60, 262, 200, "#222", 3)); b.append(C(245, 55, 6, "none", "#222", 2.5)); b.append(L(280, 30, 280, 200, "#555", 1.6)); b.append(C(280, 205, 10, "none", "#555", 2))
    for y, txt, ax, ay in [(80, "lid with holes (stops convection / evaporation)", 300, 70), (115, "thermometer", 262, 120), (148, "stirrer (keeps temperature even)", 281, 150), (182, "inner shiny copper vessel (low radiation)", 306, 190)]:
        b.append(L(385, y - 4, ax, ay, "#999", 1)); b.append(T(390, y, txt, 10.5, anchor="start", fill=NAVY, weight="bold"))
    b.append(T(80, 122, "outer jacket", 10.5, fill=NAVY, weight="bold"))
    b.append(T(80, 140, "with insulating", 10.5, fill=NAVY, weight="bold")); b.append(T(80, 153, "lagging (felt /", 10.5, fill=NAVY, weight="bold")); b.append(T(80, 166, "cotton wool)", 10.5, fill=NAVY, weight="bold"))
    b.append(L(150, 160, 118, 160, "#999", 1)); b.append(T(160, 240, "air gap between the vessels (poor conductor)", 10.5, fill=GREY))
    b.append(T(300, 18, "Calorimeter: principle  heat lost by hot body = heat gained by cold body", 12, weight="bold", fill=NAVY))
    save("calorimeter", 640, 255, "".join(b))


# ---------------------------------------------------------------- 10 V-I graphs
def fig_vi():
    b = []
    for i, (title, sub) in enumerate([("OHMIC conductor (e.g. copper wire at constant temperature)", "straight line through origin: V / I = constant"), ("NON-OHMIC conductor (e.g. filament lamp, diode)", "curve: resistance changes with V and I")]):
        ox = 40 + i * 300
        gx, gy, gw, gh = ox + 25, 40, 220, 150
        b.append(L(gx, gy + gh, gx + gw, gy + gh, "#333", 1.5, arrow=True)); b.append(L(gx, gy + gh, gx, gy - 8, "#333", 1.5, arrow=True))
        b.append(T(gx + gw, gy + gh + 16, "I", 12)); b.append(T(gx - 10, gy - 4, "V", 12))
        if i == 0:
            b.append(L(gx, gy + gh, gx + gw - 20, gy + 15, NAVY, 3))
        else:
            b.append(P(f"M{gx},{gy + gh} Q{gx + 150},{gy + gh - 15} {gx + gw - 20},{gy + 15}", "none", NAVY, 3))
        b.append(T(ox + 135, 18, title, 9.5, weight="bold", fill=NAVY)); b.append(T(ox + 135, gy + gh + 36, sub, 10, fill=GREY))
    save("vi", 620, 255, "".join(b))


# ---------------------------------------------------------------- 11 Fleming's rules
def fig_fleming():
    b = []
    for i, (title, th, ff, sf, sub) in enumerate([("Fleming's LEFT-hand rule (MOTOR effect)", "Thumb = FORCE (motion)", "First finger = magnetic FIELD (N to S)", "Second finger = CURRENT", "current-carrying conductor in a field"),
                                                    ("Fleming's RIGHT-hand rule (GENERATOR effect)", "Thumb = MOTION of the conductor", "First finger = magnetic FIELD (N to S)", "Second finger = INDUCED CURRENT", "conductor moved in a field")]):
        ox = 40 + i * 300
        cx, cy = ox + 110, 105
        b.append(T(ox + 130, 16, title, 11.5, weight="bold", fill=NAVY))
        b.append(L(cx, cy, cx, cy - 62, TEAL, 3.5, arrow=True)); b.append(T(cx + 8, cy - 62, "Thumb", 10.5, anchor="start", fill=TEAL, weight="bold"))
        b.append(L(cx, cy, cx + 80, cy, RED, 3.5, arrow=True)); b.append(T(cx + 84, cy + 4, "First finger", 10.5, anchor="start", fill=RED, weight="bold"))
        b.append(L(cx, cy, cx - 52, cy + 50, GOLD, 3.5, arrow=True)); b.append(T(cx - 56, cy + 66, "Second finger", 10.5, anchor="end", fill=GOLD, weight="bold"))
        b.append(T(ox + 130, 188, th, 10.5, fill=TEAL, weight="bold")); b.append(T(ox + 130, 202, ff, 10.5, fill=RED, weight="bold")); b.append(T(ox + 130, 216, sf, 10.5, fill=GOLD, weight="bold"))
        b.append(T(ox + 130, 232, sub, 9, fill=GREY, style="italic"))
    save("fleming", 620, 242, "".join(b))


# ---------------------------------------------------------------- 12 AC generator
def fig_generator():
    b = []
    b.append(R(60, 50, 60, 90, "#cfd8dc", "#455a64", 2)); b.append(T(90, 100, "N", 20, weight="bold", fill=RED))
    b.append(R(260, 50, 60, 90, "#cfd8dc", "#455a64", 2)); b.append(T(290, 100, "S", 20, weight="bold", fill=NAVY))
    b.append(poly([(150, 60), (230, 70), (230, 130), (150, 120)], "none", GOLD, 3))
    b.append(L(190, 38, 190, 160, "#555", 1.5, dash="5 3"))
    b.append(P("M168,18 Q190,2 212,18", "none", RED, 2).replace('/>', ' marker-end="url(#a)"/>'))
    b.append(T(190, 12, "", 8))
    b.append(C(190, 168, 8, "none", "#555", 2.5)); b.append(C(190, 188, 8, "none", "#555", 2.5))
    b.append(R(205, 164, 24, 8, "#999", "#333", 1)); b.append(R(205, 184, 24, 8, "#999", "#333", 1))
    b.append(L(229, 168, 340, 168, "#333", 1.5)); b.append(L(229, 188, 340, 188, "#333", 1.5)); b.append(R(340, 160, 46, 36, "none", "#333", 1.5)); b.append(T(363, 183, "load", 10))
    b.append(T(60, 172, "coil ABCD rotates", 10, anchor="start", fill=GOLD, weight="bold")); b.append(T(60, 186, "in the field", 10, anchor="start", fill=GOLD, weight="bold"))
    b.append(T(246, 214, "slip rings + carbon brushes", 10, fill=NAVY, weight="bold"))
    b.append(T(190, 232, "AC generator", 12, weight="bold", fill=NAVY))
    b.append(T(100, 252, "(a DC generator uses a split-ring commutator instead of slip rings)", 9.5, anchor="start", fill=GREY))
    # waveform
    gx = 430; b.append(L(gx, 120, gx + 160, 120, "#333", 1.4, arrow=True)); b.append(L(gx, 190, gx, 50, "#333", 1.4, arrow=True)); b.append(T(gx + 163, 134, "time", 10, anchor="end")); b.append(T(gx + 8, 52, "emf", 10, anchor="start"))
    b.append(P(wave(gx, gx + 150, 120, 52, 1.5), "none", NAVY, 2.6)); b.append(T(gx + 80, 205, "alternating emf", 10.5, fill=NAVY, weight="bold")); b.append(T(gx + 80, 219, "(max when coil is parallel to field)", 9.5, fill=GREY))
    save("generator", 600, 262, "".join(b))


# ---------------------------------------------------------------- 13 transformers
def fig_transformer():
    b = []

    def tf(ox, title, np_, ns_, col, note):
        s = [T(ox + 130, 18, title, 12, weight="bold", fill=col)]
        s.append(R(ox + 90, 40, 80, 120, "#cfd8dc", "#455a64", 2)); s.append(R(ox + 108, 58, 44, 84, "#fff", "#455a64", 1.5))
        for k in range(np_): s.append(L(ox + 86, 62 + k * (74 / max(np_ - 1, 1)), ox + 114, 62 + k * (74 / max(np_ - 1, 1)) + 3, GOLD, 2.2))
        for k in range(ns_): s.append(L(ox + 146, 62 + k * (74 / max(ns_ - 1, 1)), ox + 174, 62 + k * (74 / max(ns_ - 1, 1)) + 3, TEAL, 2.2))
        s.append(T(ox + 55, 105, "Primary", 10.5, fill=GOLD, weight="bold")); s.append(T(ox + 55, 118, f"{np_} turns (Np)", 9.5)); s.append(T(ox + 205, 105, "Secondary", 10.5, fill=TEAL, weight="bold")); s.append(T(ox + 205, 118, f"{ns_} turns (Ns)", 9.5))
        s.append(T(ox + 130, 180, note, 10.5, weight="bold"))
        return "".join(s)
    b.append(tf(0, "STEP-UP transformer", 4, 9, RED, "Ns > Np  =>  Vs > Vp (current falls)"))
    b.append(tf(300, "STEP-DOWN transformer", 9, 4, NAVY, "Ns < Np  =>  Vs < Vp (current rises)"))
    b.append(T(300, 212, "Vs / Vp = Ns / Np      and, for an ideal (100% efficient) transformer:   Vp Ip = Vs Is", 12, weight="bold", fill=NAVY))
    b.append(T(300, 230, "Works only with AC: a changing current in the primary changes the magnetic flux in the iron core and induces an emf in the secondary.", 9.5, fill=GREY))
    save("transformer", 600, 240, "".join(b))


# ---------------------------------------------------------------- 14 EM spectrum
def fig_em():
    b = []
    names = [("Radio waves", "#ffcdd2"), ("Microwaves", "#ffe0b2"), ("Infrared", "#fff9c4"), ("Visible", "#c8e6c9"), ("Ultraviolet", "#bbdefb"), ("X-rays", "#d1c4e9"), ("Gamma rays", "#f8bbd0")]
    uses = ["radio, TV,\nbroadcasting", "mobile phones,\nWi-Fi, satellite,\noven", "remote control,\nnight vision,\nheating", "seeing,\nphotography", "sterilising,\nfake-note\ndetector", "medical\nimaging,\nsecurity", "cancer therapy,\nsterilising"]
    w = 82
    for i, ((n, c), u) in enumerate(zip(names, uses)):
        x = 10 + i * w
        b.append(R(x, 50, w, 50, c, "#555", 1.4)); b.append(T(x + w / 2, 80, n, 10.5, weight="bold"))
        for j, ln in enumerate(u.split("\n")): b.append(T(x + w / 2, 118 + j * 12, ln, 9, fill="#333"))
    b.append(L(14, 36, 580, 36, RED, 2.2, arrow=True)); b.append(T(14, 28, "frequency and energy INCREASE", 10.5, anchor="start", fill=RED, weight="bold"))
    b.append(L(580, 168, 14, 168, NAVY, 2.2, arrow=True)); b.append(T(580, 184, "wavelength DECREASES", 10.5, anchor="end", fill=NAVY, weight="bold"))
    b.append(T(300, 18, "The electromagnetic spectrum:  c = f x lambda   (all travel at 3 x 10^8 m/s in vacuum)", 11.5, weight="bold", fill=NAVY))
    b.append(T(300, 205, "RADIO (longest wavelength, ~1 m - km)  ->  GAMMA (shortest wavelength, < 10^-11 m)", 10.5, fill=GREY))
    save("em", 600, 215, "".join(b))


# ---------------------------------------------------------------- 15 wave types
def fig_wavetypes():
    b = []
    b.append(T(150, 18, "TRANSVERSE wave (light, X-ray, radio)", 11.5, weight="bold", fill=NAVY))
    b.append(L(20, 90, 285, 90, "#999", 1, dash="3 3")); b.append(P(wave(20, 285, 90, 36, 2), "none", NAVY, 2.8))
    b.append(L(150, 142, 230, 142, TEAL, 2.5, arrow=True)); b.append(T(190, 158, "direction of propagation", 10, fill=TEAL)); b.append(L(250, 60, 250, 90, GOLD, 2, arrow=True)); b.append(T(262, 62, "vibration", 9.5, anchor="start", fill=GOLD)); b.append(T(150, 178, "vibration  PERPENDICULAR  to travel", 10.5, weight="bold"))
    b.append(T(450, 18, "LONGITUDINAL wave (sound)", 11.5, weight="bold", fill=NAVY))
    for k in range(34):
        x = 320 + k * 8 + 6 * math.sin(2 * math.pi * k / 11)
        b.append(L(x, 55, x, 110, NAVY, 1.4))
    b.append(T(345, 128, "compression", 9.5, fill=RED)); b.append(T(430, 128, "rarefaction", 9.5, fill=TEAL)); b.append(T(520, 128, "compression", 9.5, fill=RED))
    b.append(L(380, 142, 460, 142, TEAL, 2.5, arrow=True)); b.append(T(420, 158, "direction of propagation", 10, fill=TEAL)); b.append(T(450, 178, "vibration  PARALLEL  to travel", 10.5, weight="bold"))
    save("wavetypes", 600, 190, "".join(b))


# ---------------------------------------------------------------- 16 propagation
def fig_propagation():
    b = []
    b.append(P("M20,260 Q300,150 580,260 Z", "#a5d6a7", "#2e7d32", 2))
    b.append(P("M25,196 Q300,26 575,196", "none", "#ffb300", 5)); b.append(T(300, 22, "IONOSPHERE (reflects short radio waves)", 11, weight="bold", fill=GOLD))
    b.append(L(80, 232, 80, 214, "#555", 4)); b.append(T(70, 254, "transmitter", 10, anchor="start"))
    b.append(P("M84,225 Q160,205 240,222", "none", NAVY, 2.6))
    b.append(P("M86,214 Q150,90 250,62", "none", RED, 2.6)); b.append(P("M250,62 Q380,120 470,226", "none", RED, 2.6).replace('/>', ' marker-end="url(#a)"/>'))
    b.append(L(86,211,310,6, TEAL, 2.4, arrow=True))
    b.append(L(470, 232, 470, 214, "#555", 4)); b.append(T(470, 254, "receiver", 10))
    b.append(R(360, 40, 215, 62, "#fff", "#bbb", 1)); b.append(L(368, 54, 392, 54, NAVY, 2.6)); b.append(T(398, 58, "ground wave (low frequency)", 9.5, anchor="start"))
    b.append(L(368, 72, 392, 72, RED, 2.6)); b.append(T(398, 76, "sky wave: reflected, long distance", 9.5, anchor="start")); b.append(L(368, 90, 392, 90, TEAL, 2.6)); b.append(T(398, 94, "space wave: passes through (satellite, TV)", 9.5, anchor="start"))
    save("propagation", 600, 262, "".join(b))


# ---------------------------------------------------------------- 17 signals
def fig_signals():
    b = []
    cells = [("ANALOGUE signal", "continuous, any value (sine wave)", lambda: P(wave(20, 270, 80, 38, 2.5), "none", NAVY, 2.8)),
             ("DIGITAL signal", "only two states: 0 and 1 (square wave)", lambda: P("M20,115 L20,45 L60,45 L60,115 L100,115 L100,45 L140,45 L140,115 L180,115 L180,115 L220,115 L220,45 L270,45", "none", RED, 2.8))]
    for i, (t, s, f) in enumerate(cells):
        ox = i * 300
        b.append(T(ox + 145, 16, t, 12, weight="bold", fill=NAVY)); b.append(T(ox + 145, 30, s, 10, fill=GREY))
        b.append(f'<g transform="translate({ox},0)">{f()}</g>'); b.append(L(ox + 12, 120, ox + 280, 120, "#999", 1))
    b.append(T(150, 142, "affected by noise; used in radio/TV broadcast", 10)); b.append(T(450, 142, "noise-free copies, easy to store; computers, phones", 10))
    # modulation
    b.append(T(100, 170, "Carrier wave", 10.5, weight="bold")); b.append(P(wave(20, 180, 195, 12, 14), "none", GREY, 1.6))
    b.append(T(300, 170, "AM: amplitude varies", 10.5, weight="bold", fill=GOLD))
    pts = []
    for i in range(0, 241):
        t = i / 240
        a = 14 * (1 + 0.7 * math.sin(2 * math.pi * 1.5 * t)) / 1.7 * 1.6
        pts.append(f"{200 + t * 160:.1f},{195 - a * math.sin(2 * math.pi * 20 * t):.1f}")
    b.append(P("M" + " L".join(pts), "none", GOLD, 1.6))
    b.append(T(500, 170, "FM: frequency varies", 10.5, weight="bold", fill=TEAL))
    pts = []
    ph = 0
    for i in range(0, 241):
        t = i / 240
        f = 14 + 7 * math.sin(2 * math.pi * 1.5 * t)
        ph += 2 * math.pi * f / 240
        pts.append(f"{400 + t * 180:.1f},{195 - 15 * math.sin(ph):.1f}")
    b.append(P("M" + " L".join(pts), "none", TEAL, 1.6))
    save("signals", 600, 225, "".join(b))


# ---------------------------------------------------------------- 18 radiations
def fig_radiation():
    b = []
    b.append(R(20, 100, 60, 50, "#9e9e9e", "#444", 2)); b.append(R(32, 100, 36, 28, "#e0e0e0", "#444", 1)); b.append(C(50, 140, 6, "#ffee58", "#f57f17")); b.append(T(50, 168, "source in lead", 10, fill=GREY))
    b.append(T(300, 14, "Penetrating power: alpha < beta < gamma", 12, weight="bold", fill=NAVY))
    xs = [(180, "paper", "#fff8e1"), (270, "aluminium (few mm)", "#cfd8dc"), (360, "thick lead / concrete", "#757575")]
    for x, n, c in xs: b.append(R(x, 38, 16 if n != "thick lead / concrete" else 30, 110, c, "#444", 1.6)); b.append(T(x + 8, 164, n, 9.5, anchor="middle"))
    b.append(L(80, 60, 178, 60, RED, 3, arrow=True)); b.append(T(130, 52, "alpha", 10.5, fill=RED, weight="bold"))
    b.append(L(80, 90, 268, 90, GOLD, 3, arrow=True)); b.append(T(160, 84, "beta", 10.5, fill=GOLD, weight="bold"))
    b.append(L(80, 125, 440, 125, TEAL, 3, arrow=True)); b.append(T(120, 119, "gamma (only thick lead reduces it)", 10.5, anchor="start", fill=TEAL, weight="bold"))
    b.append(T(300, 190, "STOPPED by: alpha - paper / skin  |  beta - few mm aluminium  |  gamma - thick lead / concrete", 10.5, fill=NAVY, weight="bold"))
    # deflection panel
    ox = 470
    b.append(T(ox + 60, 32, "In an electric field", 11, weight="bold", fill=NAVY))
    b.append(L(ox + 10, 50, ox + 10, 135, RED, 3)); b.append(T(ox + 10, 46, "+", 13, fill=RED, weight="bold")); b.append(L(ox + 110, 50, ox + 110, 135, NAVY, 3)); b.append(T(ox + 110, 46, "-", 14, fill=NAVY, weight="bold"))
    b.append(P(f"M{ox + 60},150 Q{ox + 58},110 {ox + 14},60", "none", GOLD, 2.4).replace('/>', ' marker-end="url(#a)"/>')); b.append(T(ox + 28, 82, "beta", 9.5, fill=GOLD))
    b.append(L(ox + 60, 150, ox + 60, 55, TEAL, 2.4, arrow=True)); b.append(T(ox + 66, 84, "gamma", 9.5, anchor="start", fill=TEAL))
    b.append(P(f"M{ox + 60},150 Q{ox + 62},110 {ox + 96},60", "none", RED, 2.4).replace('/>', ' marker-end="url(#a)"/>')); b.append(T(ox + 94, 78, "alpha", 9.5, anchor="start", fill=RED))
    b.append(T(ox + 60, 168, "alpha(+) bends to -, beta(-) to +", 9, fill=GREY)); b.append(T(ox + 60, 180, "gamma: no charge, not deflected", 9, fill=GREY))
    save("radiation", 620, 205, "".join(b))


# ---------------------------------------------------------------- 19 R vs I graph (2025 Q3c)
def fig_ri():
    b = []
    gx, gy, gw, gh = 70, 20, 440, 230
    b.append(L(gx, gy + gh, gx + gw, gy + gh, "#333", 1.6, arrow=True)); b.append(L(gx, gy + gh, gx, gy - 8, "#333", 1.6, arrow=True))
    b.append(T(gx + gw / 2, gy + gh + 34, "Resistance R (ohm)", 11.5)); b.append(T(24, gy + gh / 2, "Current I (A)", 11.5, rot=-90))
    for i, R_ in enumerate([0, 10, 20, 30, 40]):
        x = gx + R_ * 10 + 10
        b.append(L(x, gy + gh, x, gy + gh + 5, "#333", 1.2)); b.append(T(x, gy + gh + 18, str(R_), 10))
    for I_ in range(0, 101, 20):
        y = gy + gh - I_ * 2.1
        b.append(L(gx - 5, y, gx, y, "#333", 1.2)); b.append(T(gx - 9, y + 4, str(I_), 10, anchor="end")); b.append(L(gx, y, gx + gw, y, "#e5e5e5", 0.8))
    data = [(0, 100), (10, 80), (20, 60), (30, 40), (40, 20)]
    pts = [(gx + R_ * 10 + 10, gy + gh - I_ * 2.1) for R_, I_ in data]
    b.append(f'<polyline points="{" ".join(f"{x},{y}" for x, y in pts)}" fill="none" stroke="{NAVY}" stroke-width="2.6"/>')
    for (x, y), (R_, I_) in zip(pts, data): b.append(C(x, y, 4.5, RED, RED)); b.append(T(x + 8, y - 8, f"({R_}, {I_})", 9.5, anchor="start", fill=RED))
    b.append(T(330, 70, "straight line, negative slope:  I = 100 - 2R", 11, anchor="start", weight="bold", fill=NAVY)); b.append(T(330, 86, "as R increases, I decreases", 10.5, anchor="start"))
    save("ri", 600, 300, "".join(b))


# ---------------------------------------------------------------- 20 centre of gravity of lamina
def fig_cg():
    b = []
    pts = [(130, 60), (270, 50), (330, 120), (260, 200), (120, 190), (70, 120)]
    b.append(poly(pts, "#fff3cd", "#555", 2));
    for (x, y), n in zip([(130, 60), (330, 120), (120, 190)], ["1", "2", "3"]):
        b.append(C(x + (6 if n != "2" else -6), y + 4, 3.5, "#555", "#555"))
    b.append(L(136, 64, 190, 205, RED, 1.4, dash="5 3")); b.append(L(324, 124, 196, 62, GREEN, 1.4, dash="5 3")); b.append(L(126, 194, 210, 52, NAVY, 1.4, dash="5 3"))
    b.append(C(191, 130, 6, RED, RED)); b.append(T(200, 150, "C.G. = where the plumb lines cross", 10.5, anchor="start", fill=RED, weight="bold"))
    b.append(T(190, 18, "Finding the centre of gravity of an irregular lamina", 12, weight="bold", fill=NAVY))
    b.append(T(190, 225, "hang from hole 1, 2, 3 in turn; draw the plumb-line each time", 10, fill=GREY))
    save("cg", 460, 235, "".join(b))


def fig_laminaflow():
    pass


if __name__ == "__main__":
    for f in (fig_moment, fig_couple, fig_equilibrium, fig_stability, fig_freefall, fig_house, fig_hydraulic, fig_heating, fig_calorimeter, fig_vi,
              fig_fleming, fig_generator, fig_transformer, fig_em, fig_wavetypes, fig_propagation, fig_signals, fig_radiation, fig_ri, fig_cg):
        f()
    print(sorted(p.name for p in OUT.glob("*.svg")))
