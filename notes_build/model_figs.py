#!/usr/bin/env python3
"""Exam-style (letter-labelled, black/grey) figures for the Biology model papers. Each function returns an inline <svg> string."""
import math
from bio_lib import T, TL, L, R, C, P, E, Q, FONT, DEFS

K, G1, G2, G3 = "#111", "#bbb", "#ddd", "#eee"


def svg(w, h, body, width_mm):
    return f'<svg viewBox="0 0 {w} {h}" width="{width_mm}mm" xmlns="http://www.w3.org/2000/svg" {FONT}>{DEFS}{body}</svg>'


def tag(x, y, s, tx=None, ty=None, size=9):
    """bold letter with optional leader line to (tx,ty)"""
    o = ""
    if tx is not None:
        o += L(x, y, tx, ty, K, 0.9)
    return o + C(x, y, 7, "#fff", K, 1) + T(x, y + 3.2, s, size, weight="bold")


def axes(x0, y0, w, h, xl, yl):
    b = [L(x0, y0, x0 + w, y0, K, 1.4, None, True), L(x0, y0, x0, y0 - h, K, 1.4, None, True), T(x0 + w / 2, y0 + 26, xl, 8.6)]
    b.append(f'<text x="{x0-34}" y="{y0-h/2}" font-size="8.6" text-anchor="middle" transform="rotate(-90 {x0-34} {y0-h/2})">{yl}</text>')
    return b


def anaphase():
    b = [C(110, 70, 55, G3, K, 1.6)]
    b += [L(65, 70, 150, 70, "#999", 0.8, "3 2")]
    for side, x in ((-1, 70), (1, 150)):
        for k, y in enumerate((50, 62, 78, 90)):
            b += [L(x - 5 * side, y, x + 5 * side, y, K, 3.2)]
    b += [L(75, 56, 100, 62, "#999", 0.6), L(145, 56, 120, 62, "#999", 0.6)]
    return svg(220, 140, "".join(b), 52)


def light_graph():
    b = axes(50, 150, 220, 130, "Light intensity (arbitrary units)", "Rate of photosynthesis")
    b += [P("M50,150 C90,90 130,50 170,40 C210,34 240,33 270,33", "none", K, 2.2), L(170, 150, 170, 40, K, 0.8, "3 3"), C(170, 40, 3, K, K, 0), T(170, 30, "X", 10, weight="bold"), T(170, 163, "", 8)]
    return svg(290, 190, "".join(b), 70)


def temp_table_graph_axes():
    return svg(290, 190, "".join(axes(50, 150, 220, 130, "Temperature (°C)", "Rate")), 70)


def nephron():
    b = [C(60, 50, 22, G3, K, 1.6), P("M54,42 C60,35 70,42 64,48 C58,56 52,50 60,45 C68,56 56,62 50,55", "none", K, 1.2)]
    b += [P("M60,72 C48,80 74,82 60,90 C48,96 74,100 60,108 L60,112", "none", K, 5), P("M60,112 L60,200 C60,214 94,214 94,200 L94,130", "none", K, 5), P("M94,130 C104,122 104,138 114,130 C124,122 124,138 134,130 L160,130", "none", K, 5)]
    b += [P("M160,130 L160,60 L190,60 L190,214", "none", K, 5)]
    b += [P("M60,112 L60,200", "none", "#fff", 1.4, "3 3")]
    b += [tag(20, 24, "A", 38, 36), tag(30, 90, "B", 55, 90), tag(112, 205, "C", 94, 190), tag(135, 112, "D", 120, 128), tag(222, 120, "E", 192, 120)]
    return svg(250, 230, "".join(b), 62)


def chloroplast():
    b = [E(130, 100, 112, 62, G3, K, 2), E(130, 100, 104, 55, "#fff", K, 1)]
    for (gx, gy) in [(70, 85), (100, 112), (72, 118)]:
        for k in range(4):
            b += [E(gx, gy + k * 5, 17, 3, "#999", K, 0.8)]
    b += [C(180, 100, 28, "#fff", K, 1.4), TL(180, 98, ["Calvin", "cycle"], 7.6, "middle", K, "bold")]
    b += [L(200, 20, 180, 66, K, 1.6, None, True), T(205, 15, "CO₂", 9, "start"), L(60, 20, 70, 60, K, 1.6, None, True), T(40, 15, "H₂O", 9, "start"), L(120, 88, 120, 20, K, 1.6, None, True)]
    b += [L(180, 128, 180, 172, K, 1.6, None, True), tag(120, 12, "C", None), tag(192, 168, "D", None)]
    b += [tag(30, 150, "A", 62, 123), tag(232, 150, "B", 205, 118)]
    b += [L(100, 85, 100, 40, K, 1.6, None, True)] if False else []
    return svg(260, 190, "".join(b), 66)


def reflex():
    b = []
    b += [P("M110,100 C125,80 145,120 160,100", "none", K, 0.0)]
    b += [Q(98, 72, 84, 56, "#e8e8e8", K, 1.5), T(140, 66, "Spinal cord", 8)]
    b += [P("M140,128 C140,150 140,160 140,172", "none", "none", 0)]
    # arm
    b += [Q(250, 100, 90, 18, G2, K, 1.2), Q(250, 104, 60, 10, "#999", K, 0.8), C(345, 109, 7, "#333", K, 1)]
    # neurons
    b += [P("M345,112 C300,150 230,150 182,112", "none", K, 1.8), P("M182,92 C220,60 290,60 305,102", "none", K, 1.8)]
    b += [P("M152,100 L152,100", "none", K, 1), L(166, 95, 166, 108, K, 3)]
    b += [tag(345, 150, "A", 345, 117), tag(262, 168, "B", 262, 144), tag(140, 150, "C", 140, 128), tag(240, 44, "D", 244, 68), tag(285, 78, "E", 290, 100)]
    return svg(380, 190, "".join(b), 82)


def plasmolysis():
    b = [R(50, 20, 150, 110, "#fff", K, 3.5, 12), P("M64,42 C60,70 62,95 70,115 C100,118 160,118 186,112 C190,90 190,60 182,38 C140,32 100,34 64,42 Z", G3, K, 1.4)]
    b += [E(125, 76, 34, 22, "#fff", K, 1), C(112, 100, 5, "#999", K, 0.8), C(150, 58, 4, "#999", K, 0.8)]
    b += [tag(25, 20, "A", 52, 28), tag(215, 38, "B", 190, 50), tag(125, 144, "C", 125, 98), tag(30, 118, "D", 66, 100)]
    return svg(240, 160, "".join(b), 58)


def tonicity():
    b = []
    for k, (x, label, shape) in enumerate(((60, "X", "shrunk"), (180, "Y", "normal"), (300, "Z", "swollen"))):
        b += [R(x - 48, 20, 96, 78, "#f5fbff", K, 1.4, 6)]
        if shape == "normal":
            b += [E(x, 60, 20, 20, G2, K, 1.4), E(x, 60, 6, 6, "#fff", K, 1)]
        elif shape == "swollen":
            b += [E(x, 60, 30, 30, G2, K, 1.4), E(x, 60, 5, 5, "#fff", K, 1)]
        else:
            b += [P(f"M{x-16},60 C{x-12},44 {x-6},40 {x},46 C{x+6},38 {x+14},44 {x+16},58 C{x+20},70 {x+8},78 {x+2},74 C{x-4},82 {x-14},76 {x-16},60 Z", G2, K, 1.4)]
        b += [T(x, 116, "Beaker " + label, 9, weight="bold")]
    b += [T(180, 10, "Red blood cells placed in three solutions", 8.6)]
    return svg(360, 124, "".join(b), 86)


def metaphase1():
    b = [C(110, 70, 55, G3, K, 1.6), L(55, 70, 165, 70, "#999", 0.8, "3 2")]
    for (x, y, c) in ((98, 52, "#333"), (122, 52, "#777"), (98, 88, "#333"), (122, 88, "#777")):
        b += [L(x - 5, y - 11, x + 5, y + 11, c, 3.6), L(x + 5, y - 11, x - 5, y + 11, c, 3.6)]
    b += [L(20, 70, 98, 52, "#999", 0.6), L(200, 70, 122, 52, "#999", 0.6)]
    return svg(220, 140, "".join(b), 52)


def digestive():
    b = [E(122, 20, 18, 9, "#eee", K, 1.2), P("M122,29 L122,70", "none", "#aaa", 6)]
    b += [P("M85,64 C100,54 135,58 142,68 C144,92 118,100 98,94 C86,88 82,76 85,64 Z", "#bbb", K, 1.4)]          # liver
    b += [P("M138,64 C160,60 175,72 172,90 C168,108 144,112 133,102 C128,92 142,84 148,82 C146,74 138,72 138,64 Z", "#ddd", K, 1.4)]  # stomach
    b += [P("M110,108 C130,102 156,104 172,110 C156,118 130,120 110,114 Z", "#ccc", K, 1.2)]                      # pancreas
    for y in range(124, 160, 8):
        b += [P(f"M98,{y} C110,{y-6} 122,{y+5} 134,{y-1} C146,{y-6} 156,{y+4} 166,{y}", "none", "#888", 4)]
    b += [P("M82,122 L82,170 L182,170 L182,122 L176,122 L176,164 L88,164 L88,122 Z", "#eee", K, 1.2)]
    b += [tag(38, 78, "A", 95, 78), tag(212, 80, "B", 172, 84), tag(212, 112, "C", 168, 112), tag(212, 142, "D", 166, 144), tag(38, 100, "E", 100, 96)]
    return svg(250, 190, "".join(b), 58)


def pedigree():
    b = []
    def sq(x, y, fill="#fff"): return Q(x - 11, y - 11, 22, 22, fill, K, 1.6)
    def ci(x, y, fill="#fff", dot=False): return C(x, y, 11, fill, K, 1.6) + (C(x, y, 3.2, K, K, 0) if dot else "")
    b += [sq(80, 30), ci(160, 30, "#fff", True), L(91, 30, 149, 30, K, 1.4)]
    b += [L(120, 30, 120, 62, K, 1.4), L(50, 62, 190, 62, K, 1.4)]
    kids = [(50, "c", "#fff", False), (100, "c", "#fff", True), (145, "s", "#444", False), (190, "s", "#fff", False)]
    for x, kind, f, d in kids:
        b += [L(x, 62, x, 78, K, 1.4)]
        b += [(ci(x, 89, f, d) if kind == "c" else sq(x, 89, f))]
    for x, lab in ((50, "II-1"), (100, "II-2"), (145, "II-3"), (190, "II-4")):
        b += [T(x, 116, lab, 8)]
    b += [T(80, 52, "", 8), T(80, 12, "I-1", 8), T(160, 12, "I-2", 8)]
    b += [R(220, 18, 130, 74, "#fff", K, 1, 2), Q(228, 28, 11, 11, "#fff", K, 1.2), T(246, 37, "normal male", 7.8, "start"), C(234, 54, 5.5, "#fff", K, 1.2), C(234, 54, 1.6, K, K, 0), T(246, 57, "carrier female", 7.8, "start"), Q(228, 68, 11, 11, "#444", K, 1.2), T(246, 77, "haemophilic male", 7.8, "start")]
    return svg(360, 126, "".join(b), 86)


def foodchain():
    names = [("A", "Grass"), ("B", "Grasshopper"), ("C", "Frog"), ("D", "Snake"), ("E", "Eagle")]
    b = []
    for i, (l, n) in enumerate(names):
        x = 6 + i * 74
        b += [R(x, 28, 62, 38, "#f2f2f2", K, 1.4, 4), T(x + 31, 44, n, 8.4, weight="bold"), T(x + 31, 58, "(" + l + ")", 8.4)]
        if i < 4:
            b += [L(x + 63, 47, x + 73, 47, K, 1.6, None, True)]
    return svg(380, 80, "".join(b), 90)


def bottleneck():
    b = axes(50, 150, 220, 130, "Time (years)", "Population size")
    b += [P("M50,40 L110,42 L130,60 L150,128 L190,124 L230,110 L270,100", "none", K, 2.2), L(150, 150, 150, 128, K, 0.8, "3 3"), T(146, 141, "hunting begins", 8, "end")]
    return svg(290, 190, "".join(b), 70)
