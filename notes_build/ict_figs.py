#!/usr/bin/env python3
"""ICT diagrams -> figs_i/*.svg"""
import math, textwrap
from ict_lib import *

BLUE, GREEN, ORANGE, PURPLE, REDC = "#1f5fa8", "#2a7a3a", "#a05a00", "#7a3b9b", "#b3211b"


def arrow(x1, y1, x2, y2, c="#333", w=1.6):
    return L(x1, y1, x2, y2, c, w, None, True)


def cloud_models():
    b = [T(235, 12, "Who manages what? (cloud service models)", 9.5, fill=NAVY, weight="bold")]
    layers = ["Applications", "Data", "Runtime / middleware", "Operating system", "Servers, storage, network"]
    cols = [("On-premises", "#555", [1, 1, 1, 1, 1]), ("IaaS", ORANGE, [1, 1, 1, 1, 0]), ("PaaS", BLUE, [1, 1, 0, 0, 0]), ("SaaS", GREEN, [0, 0, 0, 0, 0])]
    x0 = 130
    for j, (name, c, m) in enumerate(cols):
        x = x0 + j * 86
        b += [R(x, 22, 80, 22, "#fff", c, 1.6, 4), T(x + 40, 37, name, 8.6, fill=c, weight="bold")]
        for i, mine in enumerate(m):
            y = 50 + i * 26
            b += [R(x, y, 80, 22, "#ffe3a8" if mine else "#cfe3ff", "#666", 0.8, 0), T(x + 40, y + 14, "you manage" if mine else "provider", 6.8, fill="#222")]
    for i, l in enumerate(layers):
        b += [T(x0 - 6, 50 + i * 26 + 14, l, 7.6, "end")]
    b += [TL(235, 190, ["Examples: IaaS = virtual servers;  PaaS = app platform;  SaaS = Google Docs, Gmail.", "SaaS = least work for the user;  IaaS = most control;  PaaS = developers manage only the app and data."], 6.6, "middle", "#444", "normal", 11)]
    save("i_cloud_models", 470, 212, "".join(b))


def cloud_types():
    b = [T(235, 12, "Types of cloud (deployment models)", 9.5, fill=NAVY, weight="bold")]
    items = [("PRIVATE", "one organisation only;\nmost control and security", "school or bank data", "#7a3b9b", "#f3eaff"), ("PUBLIC", "shared; provider owns it;\ncheap, pay as you go", "Google Drive, Dropbox", "#1f5fa8", "#eaf3ff"),
             ("HYBRID", "private + public mixed;\nsensitive data kept private", "secure records + public website", "#2a7a3a", "#eaf6ec"), ("COMMUNITY", "shared by several groups\nwith the same needs", "several colleges / hospitals", "#a05a00", "#fff4e0")]
    for i, (t, d, e, c, f) in enumerate(items):
        x = 6 + i * 116
        b += [R(x, 24, 110, 112, f, c, 1.6, 6), T(x + 55, 42, t, 9, fill=c, weight="bold"), TL(x + 55, 62, d.split("\n"), 6.8, "middle", "#222", "normal", 9.5), T(x + 55, 100, "Example:", 6.6, fill="#555", weight="bold"), TL(x + 55, 111, textwrap.wrap(e, 18), 6.4, "middle", "#222", "normal", 9)]
    b += [TL(235, 152, textwrap.wrap("A school that wants high control and security of its own data should choose a PRIVATE cloud (P25 Q1a(vi)).", 80), 6.8, "middle", REDC, "bold")]
    save("i_cloud_types", 470, 168, "".join(b))


def cc_licences():
    b = [T(235, 12, "Creative Commons licences: from most open to most restricted", 9.5, fill=NAVY, weight="bold")]
    rows = [("CC0", "no rights reserved (public domain)", "#2a7a3a"), ("CC BY", "use, share, change, even for money, but give credit", "#3a9a4a"), ("CC BY-SA", "like BY, but share your changes under the same licence", "#6aa02a"),
            ("CC BY-NC", "remix and share, NOT for commercial use (credit needed)", "#c9a000"), ("CC BY-ND", "share only, NO changes (credit needed)", "#e08a00"), ("CC BY-NC-SA", "non-commercial; changes must use the same licence", "#d06a00"), ("CC BY-NC-ND", "most restrictive: share only, no changes, non-commercial", "#b3211b")]
    for i, (n, d, c) in enumerate(rows):
        y = 22 + i * 24
        b += [R(8, y, 92, 20, c, c, 1, 4), T(54, y + 14, n, 8.6, fill="#fff", weight="bold"), R(104, y, 358, 20, "#fff", c, 1.2, 4), T(112, y + 14, d, 7.4, "start", "#222")]
    save("i_cc_licences", 470, 196, "".join(b))


def vlookup():
    b = [T(235, 12, "VLOOKUP anatomy: =VLOOKUP(lookup_value, table_array, col_index, FALSE)", 9, fill=NAVY, weight="bold")]
    hdr = ["", "A", "B", "C"]
    rows = [("1", "Student ID", "Name", "ICT Marks"), ("2", "101", "Karma Wangmo", "85"), ("3", "102", "Dorji Wangchuk", "90"), ("4", "103", "Tashi Dendup", "78"), ("5", "104", "Kelzang Lethro", "88")]
    xs = [10, 38, 108, 208]; ws = [28, 70, 100, 70]
    for j in range(4):
        b += [R(xs[j], 24, ws[j], 18, "#e6e6e6", "#888", 0.8, 0), T(xs[j] + ws[j] / 2, 36, hdr[j], 7.6)]
    for i, r in enumerate(rows):
        y = 42 + i * 18
        for j in range(4):
            fill = "#ffe8a0" if (j in (2, 3) and i >= 1) else ("#e6e6e6" if j == 0 else "#fff")
            b += [R(xs[j], y, ws[j], 18, fill, "#888", 0.8, 0), T(xs[j] + ws[j] / 2, y + 12, r[j], 7.4, weight="bold" if i == 0 else "normal")]
    b += [P("M108,42 L208,42 L208,132 L108,132 Z", "none", REDC, 1.8, "4 3"), T(158, 144, "table_array B2:C5 (lookup column B first)", 6.8, fill=REDC)]
    b += [TL(375, 40, ["=VLOOKUP(\"Tashi Dendup\",", "B2:C5, 2, FALSE)"], 7.4, "middle", "#111", "bold", 12)]
    b += [TL(375, 84, ["1) value to find", "(first column of the table)", "2) table range, starting at that column", "3) column number inside the table", "4) FALSE = exact match"], 6.2, "middle", "#222", "normal", 10)]
    b += [T(375, 64, "result: 78", 8, fill=GREEN, weight="bold")]
    save("i_vlookup", 470, 160, "".join(b))


def chart_choice():
    b = [T(235, 12, "Which chart?", 9.5, fill=NAVY, weight="bold")]
    names = [("Column / bar", "compare amounts\n(modes of transport)"), ("Line", "TREND over time\n(monthly sales)"), ("Pie", "parts of a whole\n(budget share)"), ("Scatter", "relationship between\ntwo numbers")]
    for i, (n, d) in enumerate(names):
        x = 6 + i * 116
        b += [R(x, 20, 110, 130, "#fbfcfe", "#b9c7d8", 1, 4), T(x + 55, 33, n, 8.4, fill=NAVY, weight="bold")]
        gx, gy = x + 16, 112
        if i == 0:
            for k, hgt in enumerate([30, 58, 40, 70]):
                b += [R(gx + k * 20, gy - hgt, 14, hgt, "#4472c4", "#4472c4", 0, 0)]
            b += [L(gx - 4, gy, gx + 80, gy, "#333", 1)]
        if i == 1:
            pts = [(0, 40), (20, 56), (40, 74), (60, 66), (80, 92)]
            b += [P("M" + " L".join(f"{gx+x_},{gy-y_+20}" for x_, y_ in pts), "none", "#4472c4", 2)] + [C(gx + x_, gy - y_ + 20, 2.6, "#4472c4", "#4472c4", 0) for x_, y_ in pts] + [L(gx - 4, gy, gx + 84, gy, "#333", 1)]
        if i == 2:
            b += [C(x + 55, 80, 30, "#4472c4", "#fff", 1)]
            for a in (0, 130, 230):
                b += [L(x + 55, 80, x + 55 + 30 * math.cos(math.radians(a)), 80 - 30 * math.sin(math.radians(a)), "#fff", 1.4)]
            b += [P(f"M{x+55},80 L{x+85},80 A30,30 0 0 0 {x+55+30*math.cos(math.radians(130)):.1f},{80-30*math.sin(math.radians(130)):.1f} Z", "#ed7d31", "#fff", 1.2)]
        if i == 3:
            for (px, py) in [(6, 8), (20, 24), (34, 30), (46, 52), (60, 56), (72, 78)]:
                b += [C(gx + px, gy - py - 6, 2.8, "#4472c4", "#4472c4", 0)]
            b += [L(gx - 4, gy, gx + 84, gy, "#333", 1), L(gx - 4, gy, gx - 4, gy - 84, "#333", 1)]
        b += [TL(x + 55, 128, d.split("\n"), 6.6, "middle", "#222", "normal", 9)]
    b += [T(235, 166, "Sales trend over five months → LINE chart (P25 Q1a(ix): D)", 7, fill=REDC, weight="bold")]
    save("i_chart_choice", 470, 174, "".join(b))


def flow_symbols():
    b = [T(235, 12, "Flowchart symbols", 9.5, fill=NAVY, weight="bold")]
    syms = ["terminator", "process", "io", "decision", "arrow", "connector"]
    names = ["Start / Stop", "Process", "Input / Output", "Decision", "Flow line", "Connector"]
    desc = ["rounded box", "rectangle: calculation,\nassignment (row = 1)", "parallelogram:\ninput / print", "diamond: yes / no\n(condition)", "arrow: order of steps", "circle: joins parts"]
    for i, (s, n, d) in enumerate(zip(syms, names, desc)):
        x = 6 + i * 78
        cx = x + 36
        b += [R(x, 20, 72, 108, "#fbfcfe", "#b9c7d8", 1, 4)]
        if s == "terminator": b += [R(cx - 26, 40, 52, 24, "#eaf3ff", BLUE, 1.6, 12), T(cx, 56, "START", 7.4, weight="bold")]
        if s == "process": b += [R(cx - 26, 40, 52, 24, "#eaf6ec", GREEN, 1.6, 0), T(cx, 56, "x = x + 1", 7)]
        if s == "io": b += [P(f"M{cx-20},64 L{cx-12},40 L{cx+28},40 L{cx+20},64 Z", "#fff4e0", ORANGE, 1.6), T(cx + 4, 56, "INPUT n", 7)]
        if s == "decision": b += [P(f"M{cx},36 L{cx+30},52 L{cx},68 L{cx-30},52 Z", "#f3eaff", PURPLE, 1.6), T(cx, 55, "n > 0 ?", 7)]
        if s == "arrow": b += [arrow(cx - 22, 52, cx + 22, 52, "#333", 2)]
        if s == "connector": b += [C(cx, 52, 12, "#ffe8e8", REDC, 1.6), T(cx, 55, "A", 8, weight="bold")]
        b += [T(cx, 86, n, 7.2, weight="bold"), TL(cx, 98, d.split("\n"), 6, "middle", "#333", "normal", 8)]
    b += [T(235, 146, "Process = rectangle; Input/Output = parallelogram (P25 Q1c(v) is FALSE)", 6.8, fill=REDC)]
    save("i_flow_symbols", 470, 154, "".join(b))


def flow_triangle():
    b = [T(235, 12, "Flowchart for the star triangle (P25 Q6e)", 9.5, fill=NAVY, weight="bold")]
    def term(x, y, t): return R(x - 24, y - 9, 48, 18, "#eaf3ff", BLUE, 1.4, 9) + T(x, y + 3, t, 7.4, weight="bold")
    def proc(x, y, t, w=64): return R(x - w / 2, y - 9, w, 18, "#eaf6ec", GREEN, 1.4, 0) + T(x, y + 3, t, 7.2)
    def io(x, y, t): return P(f"M{x-38},{y+9} L{x-30},{y-9} L{x+40},{y-9} L{x+32},{y+9} Z", "#fff4e0", ORANGE, 1.4) + T(x + 1, y + 3, t, 7)
    def dec(x, y, t): return P(f"M{x},{y-17} L{x+46},{y} L{x},{y+17} L{x-46},{y} Z", "#f3eaff", PURPLE, 1.4) + T(x, y + 3, t, 7)
    b += [term(130, 28, "Start"), arrow(130, 37, 130, 46), proc(130, 55, "row = 1"), arrow(130, 64, 130, 74), dec(130, 92, "row <= 5 ?")]
    b += [L(84, 92, 40, 92, "#333", 1.4), arrow(40, 92, 40, 102), term(40, 112, "Stop"), T(62, 88, "No", 6.8), arrow(130, 109, 130, 120), T(138, 116, "Yes", 6.8)]
    b += [proc(130, 130, "col = 1"), arrow(130, 139, 130, 150), dec(130, 168, "col <= row ?"), arrow(130, 185, 130, 192), T(138, 189, "Yes", 6.8), io(130, 201, 'print "*"'), L(98, 201, 52, 201, "#333", 1.4), proc(52, 224, "col = col + 1", 74)]
    b = b[:-1]
    b += [L(52, 201, 52, 168, "#333", 1.4), arrow(52, 168, 84, 168), T(30, 188, "col = col + 1", 6.6, "start", GREEN, "bold")]
    b += [L(176, 168, 220, 168, "#333", 1.4), T(198, 163, "No", 6.8), L(220, 168, 220, 135, "#333", 1.4), arrow(220, 135, 232, 135)]
    b += [io(268, 135, "print newline"), L(268, 144, 268, 154, "#333", 1.4), proc(268, 163, "row = row + 1", 78), L(268, 172, 268, 190, "#333", 1.4), L(268, 190, 318, 190, "#333", 1.4), L(318, 190, 318, 92, "#333", 1.4), arrow(318, 92, 176, 92)]
    b += [R(336, 26, 128, 108, "#fff", "#9db7d4", 1, 4), T(400, 40, "Python version", 7.6, fill=NAVY, weight="bold")]
    code = ["row = 1", "while row <= 5:", "    col = 1", "    while col <= row:", '        print("*", end="")', "        col += 1", "    print()", "    row += 1"]
    for k, ln in enumerate(code):
        b += [f'<text x="342" y="{54+k*10}" font-size="6.6" font-family="DejaVu Sans Mono, monospace" xml:space="preserve">{esc(ln)}</text>']
    save("i_flow_triangle", 470, 214, "".join(b))


def while_flow():
    b = [T(235, 12, "How loops work", 9.5, fill=NAVY, weight="bold")]
    b += [panel(6, 18, 228, 168, "while loop (condition first)")]
    b += [R(60, 38, 120, 22, "#eaf6ec", GREEN, 1.4, 0), T(120, 53, "i = 0   (start)", 7.6), arrow(120, 60, 120, 72)]
    b += [P("M120,72 L176,92 L120,112 L64,92 Z", "#f3eaff", PURPLE, 1.4), T(120, 95, "i < 5 ?", 7.6), arrow(120, 112, 120, 128), T(128, 122, "True", 6.6)]
    b += [R(60, 128, 120, 22, "#eaf6ec", GREEN, 1.4, 0), T(120, 143, "print(i);  i += 1", 7.2), L(180, 139, 208, 139, "#333", 1.4), L(208, 139, 208, 92, "#333", 1.4), arrow(208, 92, 176, 92)]
    b += [L(64, 92, 24, 92, "#333", 1.4), T(34, 88, "False", 6.6), arrow(24, 92, 24, 170), T(24, 180, "exit loop", 6.6)]
    b += [panel(238, 18, 226, 168, "for loop with range()")]
    b += [R(262, 38, 178, 22, "#eaf6ec", GREEN, 1.4, 0), T(351, 53, "for i in range(1, 4):", 7.6), arrow(351, 60, 351, 76), R(262, 76, 178, 22, "#fff4e0", ORANGE, 1.4, 0), T(351, 91, "i takes 1, then 2, then 3", 7.4), arrow(351, 98, 351, 114), R(262, 114, 178, 22, "#eaf6ec", GREEN, 1.4, 0), T(351, 129, "run the loop body", 7.4), arrow(351, 136, 351, 150), T(351, 164, "repeat until the sequence ends", 7, fill=REDC)]
    save("i_loops", 470, 194, "".join(b))


def range_line():
    b = [T(235, 12, "range(start, stop, step): stop is NOT included", 9.5, fill=NAVY, weight="bold")]
    b += [L(20, 62, 450, 62, "#333", 1.4, None, True)]
    for k in range(0, 11):
        x = 40 + k * 38
        b += [L(x, 56, x, 68, "#333", 1), T(x, 80, str(k), 7.4)]
    for k, c in ((2, GREEN), (5, GREEN), (8, GREEN)):
        b += [C(40 + k * 38, 62, 6, c, "#fff", 1.4)]
    b += [arrow(40 + 2 * 38, 44, 40 + 5 * 38 - 6, 44, GREEN, 1.4), arrow(40 + 5 * 38, 44, 40 + 8 * 38 - 6, 44, GREEN, 1.4), T(40 + 3.5 * 38, 38, "+3", 7.4, fill=GREEN, weight="bold"), T(40 + 6.5 * 38, 38, "+3", 7.4, fill=GREEN, weight="bold")]
    b += [C(40 + 10 * 38, 62, 6, "#fff", REDC, 1.6), T(40 + 10 * 38 - 8, 98, "stop = 10 (not printed)", 6.8, "end", REDC)]
    b += [T(235, 112, "range(2, 10, 3)  →  2  5  8        range(1, 4)  →  1  2  3        range(3, 0, -1)  →  3  2  1        range(5)  →  0 1 2 3 4", 7, fill="#222")]
    save("i_range", 470, 124, "".join(b))


def list_index():
    b = [T(235, 12, "Indexing and slicing a list", 9.5, fill=NAVY, weight="bold")]
    vals = [10, 20, 30, 40, 50]
    for i, v in enumerate(vals):
        x = 80 + i * 66
        b += [R(x, 46, 60, 34, "#eaf3ff", BLUE, 1.6, 0), T(x + 30, 68, str(v), 11, weight="bold"), T(x + 30, 38, str(i), 8.6, fill=GREEN, weight="bold"), T(x + 30, 96, str(i - 5), 8.6, fill=ORANGE, weight="bold")]
    b += [T(70, 38, "index", 7.6, "end", GREEN, "bold"), T(70, 96, "negative", 7.6, "end", ORANGE, "bold"), T(32, 68, "data =", 8, "end", "#111", "bold")]
    b += [P("M146,106 L146,114 L344,114 L344,106", "none", REDC, 1.8), T(245, 126, "data[1:4]  →  [20, 30, 40]   (start 1 included, stop 4 NOT included)", 7.4, fill=REDC, weight="bold")]
    b += [T(235, 146, "data[0:3] → [10,20,30]      data[1:3] → [20,30]      data[2:5] → [30,40,50]      data[-1] → 50      data[:2] → [10,20]", 6.6, fill="#222")]
    b += [T(235, 160, "colors = [\"red\",\"green\",\"blue\"]  →  colors[-1] is \"blue\" (last item)  (P25 Q4c)", 6.8, fill=GREEN, weight="bold")]
    save("i_list_index", 470, 180, "".join(b))


def structures():
    b = [T(235, 12, "Python data structures at a glance", 9.5, fill=NAVY, weight="bold")]
    items = [("LIST", "[ ]", "ordered, changeable,\nduplicates allowed", 'fruits = ["apple","mango"]', BLUE, "#eaf3ff"), ("TUPLE", "( )", "ordered, NOT changeable\n(immutable)", "pt = (10, 20, 30)", GREEN, "#eaf6ec"),
             ("SET", "{ }", "unordered, unique items,\nno indexing", "s = {1, 2, 3}", ORANGE, "#fff4e0"), ("DICTIONARY", "{k: v}", "key : value pairs,\nkeys unique", 'st = {"name":"Jampel"}', PURPLE, "#f3eaff")]
    for i, (n, br, d, ex, c, f) in enumerate(items):
        x = 6 + i * 116
        b += [R(x, 22, 110, 132, f, c, 1.6, 6), T(x + 55, 40, n, 9, fill=c, weight="bold"), T(x + 55, 64, br, 15, fill=c, weight="bold"), TL(x + 55, 84, d.split("\n"), 6.6, "middle", "#222", "normal", 9.5)]
        b += [R(x + 6, 108, 98, 22, "#fff", c, 0.9, 2), f'<text x="{x+55}" y="122" font-size="5.6" text-anchor="middle" font-family="DejaVu Sans Mono, monospace">{esc(ex)}</text>']
        b += [T(x + 55, 146, ["append, pop, index", "index, count only", "add, remove, union", "keys(), values(), get()"][i], 6.2, fill="#444")]
    save("i_structures", 470, 162, "".join(b))


def function_anatomy():
    b = [T(235, 12, "Anatomy of a function", 9.5, fill=NAVY, weight="bold")]
    code = [("def add(a, b=10):", 42), ("    total = a + b", 60), ("    return total", 78), ("result = add(5)", 114), ("print(result)", 132)]
    b += [R(10, 24, 216, 120, "#f7f7f7", "#888", 1, 3)]
    for ln, y in code:
        b += [f'<text x="20" y="{y}" font-size="9" font-family="DejaVu Sans Mono, monospace" xml:space="preserve">{esc(ln)}</text>']
    notes = [(244, 38, ["def = keyword", "add = function name"], BLUE, (150, 38)), (244, 66, ["a, b = parameters", "(b = 10 is a default value)"], GREEN, (120, 42)), (244, 94, ["return sends back the", "return value"], ORANGE, (120, 76)), (244, 122, ["add(5) = function CALL;", "5 = argument (b becomes 10)"], PURPLE, (120, 112))]
    for (x, y, t, c, (tx, ty)) in notes:
        b += [L(x - 4, y - 2, tx, ty, c, 0.9), TL(x, y, t, 7, "start", c, "bold", 9.5)]
    b += [T(244, 148, "result = 15", 7.2, "start", REDC, "bold")]
    b += [TL(235, 168, ["Local variables (total) exist only inside the function.", "If a function is defined twice with the same name, only the LAST definition is kept."], 6.6, "middle", "#444", "normal", 10)]
    save("i_function", 470, 184, "".join(b))


def recursion():
    b = [T(235, 12, "countConsonants(\"Bhutan\") unfolds step by step", 9.5, fill=NAVY, weight="bold")]
    steps = [('"Bhutan"', "B is a consonant", "1 + count(\"hutan\")"), ('"hutan"', "h is a consonant", "1 + count(\"utan\")"), ('"utan"', "u is a vowel", "count(\"tan\")"), ('"tan"', "t is a consonant", "1 + count(\"an\")"), ('"an"', "a is a vowel", "count(\"n\")"), ('"n"', "n is a consonant", "1 + count(\"\")"), ('""', "BASE CASE", "return 0")]
    for i, (t, d, r) in enumerate(steps):
        y = 26 + i * 22
        b += [R(10, y, 62, 18, "#eaf3ff" if i < 6 else "#ffe8e8", BLUE if i < 6 else REDC, 1.2, 3), T(41, y + 12, t, 7.4, weight="bold"), T(82, y + 12, d, 7.2, "start", "#222"), T(212, y + 12, r, 7.2, "start", "#111", "bold")]
    b += [R(318, 26, 144, 160, "#f4f8fd", "#9db7d4", 1, 4), TL(390, 40, ["Going back up (unwinding):", "count(\"\")    = 0", "count(\"n\")   = 1 + 0 = 1", "count(\"an\")  = 1", "count(\"tan\") = 1 + 1 = 2", "count(\"utan\")= 2", "count(\"hutan\")= 1 + 2 = 3", "count(\"Bhutan\")= 1 + 3 = 4"], 6.6, "middle", "#111", "normal", 15)]
    b += [T(390, 176, "Answer: 4 (B, h, t, n)", 7.4, fill=GREEN, weight="bold")]
    save("i_recursion", 470, 192, "".join(b))


def turtle_hex():
    b = [T(235, 12, "Turtle: a regular polygon turns 360° / sides", 9.5, fill=NAVY, weight="bold")]
    pts = [(120 + 52 * math.cos(math.radians(60 * k - 90 + 0)), 80 + 52 * math.sin(math.radians(60 * k - 90))) for k in range(6)]
    b += [P("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z", "#eaf3ff", BLUE, 2)]
    for k, (x, y) in enumerate(pts):
        b += [C(x, y, 3, REDC, REDC, 0)]
    b += [T(120, 82, "hexagon", 8, fill=BLUE, weight="bold")]
    b += [R(240, 26, 218, 112, "#f7f7f7", "#888", 1, 3)]
    code = ["import turtle", "t = turtle.Turtle()", "for _ in range(6):", "    t.forward(100)", "    t.right(60)", "turtle.done()"]
    for k, ln in enumerate(code):
        b += [f'<text x="250" y="{44+k*14}" font-size="8" font-family="DejaVu Sans Mono, monospace" xml:space="preserve">{esc(ln)}</text>']
    b += [TL(349, 134, ["6 sides, turns of 60° → HEXAGON (P24 Q1a(ix): D)"], 6.8, "middle", REDC, "bold")]
    b += [T(235, 158, "Square: 4 sides, turn 90° (360/4).   Triangle: turn 120°.   Pentagon: 72°.   Octagon: 45°.", 6.8, fill="#444")]
    save("i_turtle", 470, 168, "".join(b))


def bank_flow():
    b = [T(235, 12, "Mobile banking program: logic", 9.5, fill=NAVY, weight="bold")]
    def box(x, y, w, t, c=GREEN, f="#eaf6ec", h=20): return R(x, y, w, h, f, c, 1.4, 4) + T(x + w / 2, y + h / 2 + 3, t, 7.2)
    b += [box(160, 24, 150, "balance = 1000", BLUE, "#eaf3ff"), arrow(235, 44, 235, 54)]
    b += [P("M235,54 L300,72 L235,90 L170,72 Z", "#f3eaff", PURPLE, 1.4), T(235, 75, "while True: menu", 7)]
    b += [arrow(235, 90, 235, 102)]
    b += [P("M235,102 L300,120 L235,138 L170,120 Z", "#f3eaff", PURPLE, 1.4), T(235, 123, "choice ?", 7.4)]
    cases = [(30, "1: print balance"), (122, "2: deposit\n(amount > 0)"), (214, "3: withdraw\n(0 < amt <= bal.)"), (306, "4: print thanks\nbreak"), (398, "other:\ninvalid selection")]
    for (x, t) in cases:
        b += [L(235, 138, x + 35, 158, "#555", 1.2), R(x, 158, 70, 36, "#eaf6ec" if "4" not in t[:2] else "#ffe8e8", GREEN if "4" not in t[:2] else REDC, 1.4, 4), TL(x + 35, 172, t.split("\n"), 6.4, "middle", "#111", "normal", 9)]
    b += [P("M42,194 L42,214 L430,214 L430,72 L300,72", "none", "#555", 1.2, "4 3"), T(235, 210, "back to the menu (loop) until the user chooses 4", 6.6, fill="#444")]
    save("i_bank_flow", 470, 220, "".join(b))


def ranges_excel():
    b = [T(235, 12, "Common Excel functions", 9.5, fill=NAVY, weight="bold")]
    rows = [("SUM / AVERAGE / MAX / MIN / COUNT", "=MAX(E2:E5), =AVERAGE(B2:E2)"), ("IF", "=IF(B2>=50,\"Pass\",\"Fail\")"), ("AND / OR / NOT", "=NOT(A1>5)  reverses TRUE/FALSE"), ("SUMIF", "=SUMIF(B2:B6,\"IT\",C2:C6)  range, criteria, sum range"), ("COUNTIF / AVERAGEIF", "=COUNTIF(A1:A6,\">60\")"), ("VLOOKUP", "=VLOOKUP(value, table, col, FALSE)"), ("RANK", "=RANK(B2,B2:B10)  position in a list (not alphabetical)")]
    for i, (f, e) in enumerate(rows):
        y = 22 + i * 22
        b += [R(6, y, 190, 19, "#d6e5f4", "#555", 0.8, 0), T(12, y + 13, f, 7.2, "start", "#111", "bold"), R(196, y, 264, 19, "#fff", "#555", 0.8, 0), f'<text x="202" y="{y+13}" font-size="6.4" font-family="DejaVu Sans Mono, monospace">{esc(e)}</text>']
    save("i_excel_funcs", 470, 182, "".join(b))


if __name__ == "__main__":
    for f in (cloud_models, cloud_types, cc_licences, vlookup, chart_choice, flow_symbols, flow_triangle, while_flow, range_line, list_index, structures, function_anatomy, recursion, turtle_hex, bank_flow, ranges_excel):
        f()
