#!/usr/bin/env python3
"""Diagrams for the Geography notes -> figs_g/*.svg (reuses the helpers from hist_figs)."""
import math, pathlib
import hist_figs as H
from hist_figs import T, TL, L, R, C, P, box, save, NAVY, TEAL, GOLD, RED, GREY, GREEN, PURPLE

H.OUT = pathlib.Path(__file__).parent / "figs_g"
H.OUT.mkdir(exist_ok=True)
BROWN = "#8a5a1c"
BLUE = "#2f6fb0"


def poly(pts, fill="none", stroke="#333", sw=1.4):
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


# 1 ---------------------------------------------------------------- Big Bang timeline
def big_bang():
    H.timeline("big_bang", [
        ("13.8 bya", ["BIG BANG: hot,", "dense point;", "space expands"]),
        ("seconds-min", ["matter forms;", "mostly hydrogen", "and helium"]),
        ("~400 000 yrs", ["universe cools;", "light released", "(background)"]),
        ("~200 m yrs", ["first stars and", "galaxies form"]),
        ("4.6 bya", ["solar nebula:", "Sun and planets", "form"]),
        ("4.54 bya", ["Earth forms;", "oceans, then", "life later"]),
    ], 470, 200, "Timeline of the universe (bya = billion years ago)")


# 2 ---------------------------------------------------------------- nebula
def nebula():
    H.flow("nebula", [
        ("1. Solar nebula", ["giant cloud of dust", "and gas (hydrogen,", "helium)"]),
        ("2. Collapse", ["gravity pulls it in;", "may be triggered by", "a supernova shock"]),
        ("3. Spinning disc", ["spins faster, flattens:", "hot dense centre,", "disc around it"]),
        ("4. Sun forms", ["centre becomes the", "Sun; fusion starts"]),
        ("5. Accretion", ["dust clumps ->", "planetesimals ->", "protoplanets"]),
        ("6. Planets", ["inner: small rocky;", "outer: gas and ice", "giants"]),
    ], per=3)


# 3 ---------------------------------------------------------------- earth layers
def earth_layers():
    b = []
    cx, cy = 120, 105
    b.append(C(cx, cy, 92, "#b7794a", "#444", 1.6))
    b.append(C(cx, cy, 88, "#e08a3c", "#444", 1.2))
    b.append(C(cx, cy, 52, "#f4c24a", "#444", 1.2))
    b.append(C(cx, cy, 26, "#fff3b0", "#444", 1.2))
    b.append(T(cx, cy + 3, "inner", 7.2)); b.append(T(cx, cy + 11, "core", 7.2))
    b.append(T(cx, cy - 36, "outer core", 7.6, weight="bold")); b.append(T(cx, cy + 62, "MANTLE", 8.4, weight="bold"))
    rows = [("CRUST", "5-10 km (oceanic), 30-70 km (continental); solid rock", RED, 20),
            ("MANTLE", "about 2,900 km thick; hot, slowly flowing rock", GOLD, 54),
            ("OUTER CORE", "about 2,200 km; liquid iron and nickel (makes the magnetic field)", GOLD, 88),
            ("INNER CORE", "about 1,200 km; solid iron-nickel, ~5,500 C", NAVY, 122)]
    for t, s, col, y in rows:
        b.append(T(238, y, t, 8.6, "start", col, "bold")); b.append(T(238, y + 11, s, 6.7, "start", "#333"))
    b.append(R(236, 138, 226, 38, "#eef3fb", NAVY, 1.2))
    b.append(T(349, 152, "LITHOSPHERE = crust + rigid top of mantle (~100 km)", 7.2, fill=NAVY, weight="bold"))
    b.append(T(349, 166, "floats on the ASTHENOSPHERE (weak, ductile layer)", 7.2, fill=NAVY, weight="bold"))
    save("earth_layers", 470, 205, "".join(b))


# 4 ---------------------------------------------------------------- plate boundaries
def plates():
    b = []
    names = ["CONVERGENT (collide)", "DIVERGENT (move apart)", "TRANSFORM (slide past)"]
    for i, nm in enumerate(names):
        ox = 8 + i * 155
        b.append(T(ox + 70, 12, nm, 7.6, fill=NAVY, weight="bold"))
        if i == 0:
            b.append(R(ox, 60, 68, 28, "#d9b98a", BROWN, 1.3, 1)); b.append(R(ox + 72, 60, 68, 28, "#c9a27a", BROWN, 1.3, 1))
            b.append(poly([(ox + 50, 60), (ox + 70, 32), (ox + 92, 60)], "#d9b98a", BROWN, 1.3))
            b.append(L(ox + 4, 48, ox + 34, 48, RED, 2.2, arrow=True)); b.append(L(ox + 136, 48, ox + 106, 48, RED, 2.2, arrow=True))
            b.append(TL(ox + 70, 106, ["Fold mountains form", "(Himalayas: India +", "Eurasia)"], 7.2))
        elif i == 1:
            b.append(R(ox, 60, 58, 28, "#d9b98a", BROWN, 1.3, 1)); b.append(R(ox + 82, 60, 58, 28, "#c9a27a", BROWN, 1.3, 1))
            b.append(R(ox + 58, 70, 24, 18, "#e08a3c", "#a34a00", 1, 1))
            b.append(L(ox + 52, 48, ox + 22, 48, RED, 2.2, arrow=True)); b.append(L(ox + 88, 48, ox + 118, 48, RED, 2.2, arrow=True))
            b.append(TL(ox + 70, 106, ["Rift valley / ocean ridge;", "new crust (sea-floor", "spreading)"], 7.2))
        else:
            b.append(R(ox, 52, 66, 22, "#d9b98a", BROWN, 1.3, 1)); b.append(R(ox + 74, 74, 66, 22, "#c9a27a", BROWN, 1.3, 1))
            b.append(L(ox + 34, 44, ox + 34 - 26, 44, RED, 2.2, arrow=True)); b.append(L(ox + 108, 104, ox + 134, 104, RED, 2.2, arrow=True))
            b.append(TL(ox + 70, 124, ["Fault; earthquakes", "(San Andreas Fault)"], 7.2))
    save("plates", 470, 140, "".join(b))


# 5 ---------------------------------------------------------------- Himalaya formation
def himalaya():
    b = []
    panels = [("1. Tethys Sea", "India (south) and Eurasia (north)"), ("2. India drifts north", "sea sediments squeezed"), ("3. Collision 50-70 mya", "crumpling, folding"), ("4. Himalayas today", "still rising ~ 4 mm/yr")]
    for i, (t, s) in enumerate(panels):
        ox = 6 + i * 116
        b.append(T(ox + 55, 12, t, 7.4, fill=NAVY, weight="bold"))
        b.append(R(ox, 20, 110, 80, "#e8f2fb", "#999", 1, 2))
        if i == 0:
            b.append(R(ox + 4, 62, 30, 36, "#d9b98a", BROWN, 1.2, 1)); b.append(R(ox + 76, 56, 30, 42, "#c9a27a", BROWN, 1.2, 1))
            b.append(T(ox + 55, 82, "sea", 7, fill=BLUE)); b.append(T(ox + 19, 96, "India", 6.8)); b.append(T(ox + 91, 96, "Eurasia", 6.8))
        elif i == 1:
            b.append(R(ox + 14, 62, 30, 36, "#d9b98a", BROWN, 1.2, 1)); b.append(R(ox + 76, 56, 30, 42, "#c9a27a", BROWN, 1.2, 1))
            b.append(L(ox + 6, 44, ox + 36, 44, RED, 2.2, arrow=True)); b.append(P(f"M{ox + 44},96 Q{ox + 60},84 {ox + 76},96", "#b9d8f0", BLUE, 1.2))
        elif i == 2:
            b.append(R(ox + 4, 66, 40, 32, "#d9b98a", BROWN, 1.2, 1)); b.append(R(ox + 66, 56, 40, 42, "#c9a27a", BROWN, 1.2, 1))
            b.append(P(f"M{ox + 40},98 Q{ox + 50},50 {ox + 58},72 Q{ox + 64},42 {ox + 72},98", "#c9a27a", BROWN, 1.4))
            b.append(L(ox + 6, 50, ox + 30, 50, RED, 2.2, arrow=True))
        else:
            b.append(poly([(ox + 4, 98), (ox + 4, 66), (ox + 30, 58), (ox + 46, 38), (ox + 56, 24), (ox + 66, 36), (ox + 82, 58), (ox + 106, 62), (ox + 106, 98)], "#c9a27a", BROWN, 1.4))
            b.append(poly([(ox + 50, 32), (ox + 56, 24), (ox + 62, 32)], "#fff", "#aaa", 1)); b.append(T(ox + 56, 18, "", 1))
        b.append(T(ox + 55, 112, s, 6.6, fill="#444"))
    b.append(T(235, 134, "Marine fossils (ammonites, shells) and marine limestone high in the Himalayas prove the area was once under the Tethys Sea.", 7, fill=GREY))
    save("himalaya", 470, 142, "".join(b))


# 6 ---------------------------------------------------------------- geological time scale
def gts():
    b = []
    cols = [("PRECAMBRIAN", "4.6 bya - 541 mya", ["Earth forms; crust", "oceans, atmosphere;", "first simple life", "(bacteria, algae)"], "#e5d6f0", PURPLE),
            ("PALAEOZOIC", "541 - 252 mya", ["fish, amphibians,", "first reptiles;", "first land plants,", "forests and coal"], "#d6ecd9", GREEN),
            ("MESOZOIC", "252 - 66 mya", ["age of dinosaurs;", "Pangaea breaks up;", "first mammals, birds;", "ends with extinction"], "#fbeed6", GOLD),
            ("CENOZOIC", "66 mya - today", ["age of mammals;", "Himalayas rise;", "Ice Ages (Pleistocene);", "humans appear"], "#dbe7f7", NAVY)]
    for i, (n, d, ls, f, c) in enumerate(cols):
        x = 6 + i * 116
        b.append(R(x, 8, 110, 24, f, c, 1.6)); b.append(T(x + 55, 21, n, 8.2, fill=c, weight="bold")); b.append(T(x + 55, 30, d, 6.6, fill="#333"))
        b.append(R(x, 34, 110, 58, "#fff", c, 1.3)); b.append(TL(x + 55, 47, ls, 7, lh=10.4))
        if i < 3:
            b.append(L(x + 110, 20, x + 116, 20, "#555", 1.4, arrow=True))
    b.append(T(235, 106, "Order (oldest to newest): Precambrian -> Palaeozoic -> Mesozoic -> Cenozoic   (i, iii, ii, iv in 2025 Q5a)", 7.6, fill=NAVY, weight="bold"))
    save("gts", 470, 114, "".join(b))


# 7 ---------------------------------------------------------------- wind transport
def wind():
    b = []
    b.append(L(20, 150, 450, 150, "#8a5a1c", 5))
    b.append(L(20, 120, 450, 120, "#aaa", 0.8, dash="4 3")); b.append(T(448, 116, "1.5 m", 7, "end", GREY))
    # suspension
    for x, y in [(70, 40), (110, 55), (150, 36), (190, 50)]:
        b.append(C(x, y, 2.2, "#999", "#777")); b.append(L(x + 4, y, x + 22, y, TEAL, 1.2, arrow=True))
    b.append(T(130, 22, "SUSPENSION: fine dust carried high in the air", 8, fill=TEAL, weight="bold"))
    # saltation
    for x0 in (230, 300, 370):
        b.append(P(f"M{x0},148 Q{x0 + 32},80 {x0 + 62},148", "none", GOLD, 1.6, "4 2")); b.append(C(x0, 147, 3, GOLD, GOLD))
    b.append(T(330, 70, "SALTATION: sand grains bounce", 8, fill=GOLD, weight="bold")); b.append(T(330, 82, "(up to about 1.5 m high)", 7.4, fill=GOLD))
    # creep
    for x in (60, 100, 140):
        b.append(C(x, 143, 6, "#c9a27a", BROWN)); b.append(L(x + 8, 143, x + 22, 143, RED, 1.6, arrow=True))
    b.append(T(14, 172, "SURFACE CREEP: heavy grains pushed / rolled", 7.8, "start", RED, "bold"))
    b.append(T(360, 172, "EROSION by wind: deflation (lifting) and abrasion", 7.6, fill=NAVY, weight="bold"))
    b.append(T(360, 183, "(sand blasting a rock surface)", 7.2, fill=NAVY))
    save("wind", 470, 190, "".join(b))


# 8 ---------------------------------------------------------------- karst
def karst():
    b = []
    b.append(R(10, 20, 330, 150, "#e9e2d0", "#8a7a55", 1.5, 2))
    b.append(P("M60,20 L60,50 L66,50 L66,20", "#bfe3f5", BLUE, 1)); b.append(T(63, 14, "swallow hole", 6.8, fill=BLUE))
    b.append(P("M190,20 Q196,48 210,48 Q224,48 230,20", "#e3d9b9", "#8a7a55", 1.4)); b.append(T(210, 14, "sinkhole (doline)", 6.8, fill=BROWN))
    for x in range(20, 60, 8): b.append(L(x, 22, x + 3, 28, "#8a7a55", 1))
    b.append(T(30, 34, "lapies", 6.8, fill=BROWN))
    b.append(P("M30,100 Q40,70 100,72 Q250,70 300,92 L300,152 L30,152 Z", "#cfe0ee", "#666", 1.2))
    for x in (80, 130, 200, 250):
        b.append(poly([(x - 7, 72), (x + 7, 72), (x, 100 + (x % 50))], "#fff7d6", "#8a7a55", 1))
    for x in (110, 170, 220):
        b.append(poly([(x - 8, 150), (x + 8, 150), (x, 122 + (x % 30))], "#fff7d6", "#8a7a55", 1))
    b.append(R(143, 74, 12, 76, "#fff7d6", "#8a7a55", 1, 1)); b.append(T(149, 166, "pillar", 6.8, fill=NAVY))
    b.append(P("M30,150 Q150,138 300,150", "none", BLUE, 2.2)); b.append(T(100, 160, "underground stream", 6.8, fill=BLUE))
    b.append(T(105, 66, "stalactite (hangs from roof)", 6.8, "middle", NAVY)); b.append(T(235, 140, "stalagmite (rises", 6.8, fill=NAVY)); b.append(T(235, 149, "from floor)", 6.8, fill=NAVY))
    b.append(T(10, 190, "Limestone dissolves in rainwater (carbonic acid) = EROSION; dripping water re-deposits calcite = DEPOSITION", 7, "start", "#444"))
    b.append(R(350, 24, 116, 130, "#eef3fb", NAVY, 1.2, 3))
    b.append(TL(408, 40, ["EROSIONAL:", "lapies, sinkholes,", "swallow holes,", "caves, tunnels", "", "DEPOSITIONAL:", "stalactite,", "stalagmite,", "pillar (column)"], 7.4, fill=NAVY, weight="bold", lh=11.4))
    save("karst", 470, 198, "".join(b))


# 9 ---------------------------------------------------------------- drainage patterns
def drainage():
    b = []
    names = ["DENDRITIC", "TRELLIS", "RADIAL", "PARALLEL"]
    notes = ["tree-like;", "uniform rock", "main rivers parallel,", "tributaries at 90 deg;", "folded mountains", "flows outward from", "a dome / peak", "streams parallel on", "a steep uniform slope"]
    for i, nm in enumerate(names):
        ox = 6 + i * 116
        b.append(R(ox, 18, 110, 86, "#fff", "#999", 1, 2)); b.append(T(ox + 55, 12, nm, 8, fill=NAVY, weight="bold"))
        if i == 0:
            b.append(L(ox + 55, 100, ox + 55, 30, BLUE, 2.2))
            for y, d in ((84, 1), (68, -1), (52, 1), (38, -1)):
                b.append(L(ox + 55, y, ox + 55 + d * 30, y - 22, BLUE, 1.5)); b.append(L(ox + 55 + d * 15, y - 11, ox + 55 + d * 22, y + 2 - 11, BLUE, 1))
        elif i == 1:
            b.append(L(ox + 30, 100, ox + 30, 24, BLUE, 2.2)); b.append(L(ox + 80, 100, ox + 80, 24, BLUE, 2.2))
            for y in (44, 62, 80):
                b.append(L(ox + 30, y, ox + 12, y, BLUE, 1.3)); b.append(L(ox + 30, y, ox + 80, y + 0.01, BLUE, 1.0, dash="1 3")); b.append(L(ox + 80, y + 8, ox + 98, y + 8, BLUE, 1.3))
        elif i == 2:
            b.append(poly([(ox + 55, 36), (ox + 72, 70), (ox + 38, 70)], "#d9b98a", BROWN, 1.2))
            for a in range(0, 360, 45):
                r = math.radians(a)
                b.append(L(ox + 55 + 10 * math.cos(r), 62 + 10 * math.sin(r), ox + 55 + 38 * math.cos(r), 62 + 38 * math.sin(r), BLUE, 1.5))
        else:
            for k in range(5):
                x = ox + 14 + k * 20
                b.append(L(x, 24, x + 8, 100, BLUE, 1.7))
        for j in range(2):
            pass
    lab = [["tree-like branches,", "same rock everywhere"], ["parallel main rivers,", "tributaries at right", "angles (fold mountains)"], ["flows outward from", "a dome / peak"], ["parallel streams on a", "steep uniform slope"]]
    for i, ls in enumerate(lab):
        b.append(TL(61 + i * 116, 116, ls, 6.8, fill="#333", lh=8.2))
    save("drainage", 470, 148, "".join(b))


# 10 --------------------------------------------------------------- climate zones
def zones():
    b = []
    b.append(L(40, 190, 40, 12, "#333", 1.4, arrow=True)); b.append('<text x="8" y="110" font-size="8" text-anchor="middle" transform="rotate(-90 8 110)">Altitude</text>')
    b.append(R(40, 14, 110, 36, "#e6f2fb", "#2f6fb0", 1.4, 0)); b.append(R(40, 50, 110, 56, "#dcecd0", GREEN, 1.4, 0)); b.append(R(40, 106, 110, 84, "#fbe3c0", GOLD, 1.4, 0))
    b.append(T(95, 36, "ALPINE", 8.4, fill=BLUE, weight="bold")); b.append(T(95, 82, "TEMPERATE", 8.4, fill=GREEN, weight="bold")); b.append(T(95, 150, "SUB-TROPICAL", 8.4, fill=GOLD, weight="bold"))
    for y, t in ((190, "200 m"), (106, "2000 m"), (50, "4000 m"), (14, "7500 m")):
        b.append(L(36, y, 40, y, "#333", 1.2)); b.append(T(34, y + 3, t, 7, "end"))
    rows = [("ALPINE (above ~4000 m)", "very cold, snow, short summer; meadows and shrubs;", "hardly inhabited; yak herders; cordyceps collection", BLUE, 26),
            ("TEMPERATE (~2000-4000 m)", "cool summer, cold dry winter; conifers, oak, rhododendron;", "Thimphu, Paro, Bumthang, Gasa; apples, potatoes, buckwheat", GREEN, 70),
            ("SUB-TROPICAL (~200-2000 m)", "hot humid summer, mild winter, heavy monsoon rain;", "rice, maize, citrus; Phuentsholing, Gelephu, Samdrup Jongkhar", GOLD, 140)]
    for t, a, c2, col, y in rows:
        b.append(L(152, y - 4, 172, y - 4, col, 1.4)); b.append(T(176, y, t, 8.2, "start", col, "bold")); b.append(T(176, y + 11, a, 6.9, "start")); b.append(T(176, y + 21, c2, 6.9, "start"))
    b.append(T(300, 196, "Temperature falls about 6.5 C for every 1000 m you climb (lapse rate)", 7, fill=GREY))
    save("zones", 470, 204, "".join(b))


# 11 --------------------------------------------------------------- climograph (redrawn 2025 graph)
def climograph():
    b = []
    gx, gy, gw, gh = 56, 34, 322, 120
    rain = [10, 25, 60, 120, 185, 320, 445, 325, 210, 100, 10, 8]
    tmax = [16.5, 18, 21.5, 24, 26, 27.5, 28, 28, 27, 25, 21.5, 18]
    tmin = [5, 6.5, 10, 13.5, 16.5, 19.5, 19.5, 19.5, 18, 14, 10, 6.5]
    mon = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    b.append(L(gx, gy + gh, gx + gw, gy + gh, "#333", 1.4)); b.append(L(gx, gy, gx, gy + gh, "#333", 1.4)); b.append(L(gx + gw, gy, gx + gw, gy + gh, "#333", 1.4))
    for v in (0, 100, 200, 300, 400, 500):
        y = gy + gh - v / 500 * gh
        b.append(L(gx - 3, y, gx, y, "#333", 1)); b.append(T(gx - 5, y + 3, str(v), 6.8, "end"))
        if v: b.append(L(gx, y, gx + gw, y, "#e3e3e3", 0.7))
    for t in (0, 10, 20, 30):
        y = gy + gh - t / 30 * gh
        b.append(T(gx + gw + 5, y + 3, str(t), 6.8, "start"))
    step = gw / 12
    pts1, pts2 = [], []
    for i, (r, a, c) in enumerate(zip(rain, tmax, tmin)):
        x = gx + i * step + step / 2
        h = r / 500 * gh
        b.append(R(x - 8, gy + gh - h, 16, h, "#d6e5f4", NAVY, 1, 0))
        pts1.append((x, gy + gh - a / 30 * gh)); pts2.append((x, gy + gh - c / 30 * gh))
        b.append(T(x, gy + gh + 10, mon[i], 6.8))
    b.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts1)}" fill="none" stroke="{RED}" stroke-width="1.8"/>')
    b.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts2)}" fill="none" stroke="{TEAL}" stroke-width="1.8"/>')
    b.append(T(gx + gw / 2, 11, "Climate of Bhutan (redrawn, approximate values)", 8, fill=NAVY, weight="bold"))
    b.append(T(16, gy + 60, "rain (mm)", 7, "middle")) if False else b.append(f'<text x="14" y="{gy + 70}" font-size="7" text-anchor="middle" transform="rotate(-90 14 {gy + 70})">rainfall (mm)</text>'); b.append(T(gx + gw + 24, gy + 4, "C", 7, "middle"))
    b.append(L(gx + 70, 24, gx + 84, 24, RED, 2)); b.append(T(gx + 88, 27, "Tmax", 7, "start")); b.append(L(gx + 120, 24, gx + 134, 24, TEAL, 2)); b.append(T(gx + 138, 27, "Tmin", 7, "start")); b.append(R(gx + 170, 19, 10, 9, "#d6e5f4", NAVY, 1, 0)); b.append(T(gx + 184, 27, "rainfall", 7, "start"))
    b.append(R(406, 34, 60, 120, "#fff7e6", GOLD, 1.2, 3))
    b.append(TL(436, 46, ["Jan - May:", "temperature and", "rain RISE as the", "SUMMER MONSOON", "approaches (2025", "Q1a-ii: B)", "", "Peak rain:", "July - August"], 6.7, fill="#333", lh=9.4))
    save("climograph", 470, 184, "".join(b))


# 12 --------------------------------------------------------------- orographic rainfall
def orographic():
    b = []
    b.append(poly([(20, 150), (150, 150), (220, 44), (300, 150), (450, 150)], "#d9b98a", BROWN, 1.6))
    b.append(L(14, 98, 80, 112, BLUE, 2.4, arrow=True)); b.append(T(46, 90, "moist monsoon wind", 7.4, fill=BLUE, weight="bold"))
    for x, y in ((100, 74), (130, 62), (160, 50)):
        b.append(P(f"M{x},{y} q8,-10 18,-4 q10,-8 18,2 q6,0 4,8 h-40 z", "#e8eef5", "#889", 1))
    b.append(T(100, 168, "WINDWARD: heavy rain", 7.6, fill=NAVY, weight="bold")); b.append(T(100, 178, "(southern foothills 5000+ mm)", 6.9, fill=NAVY))
    b.append(T(350, 168, "LEEWARD / RAIN SHADOW: dry", 7.6, fill=RED, weight="bold")); b.append(T(350, 178, "(Paro, Thimphu, north: ~ 500-1000 mm)", 6.9, fill=RED))
    b.append(T(220, 36, "Great Himalaya", 7.4, fill="#444"))
    b.append(L(300, 70, 350, 96, GREY, 1.6, "5 3", arrow=True)); b.append(T(380, 66, "dry, warm, sinking air", 7, fill=GREY))
    b.append(T(235, 14, "Mountains force air to rise, cool and drop rain on one side (orographic rainfall)", 8.2, fill=NAVY, weight="bold"))
    save("orographic", 470, 186, "".join(b))


# 13 --------------------------------------------------------------- time zones
def timezones():
    b = []
    b.append(T(235, 12, "Earth turns 360 deg in 24 h: 15 deg = 1 hour, 1 deg = 4 minutes", 8.6, fill=NAVY, weight="bold"))
    y0 = 78
    b.append(L(22, y0, 450, y0, "#333", 2.4))
    marks = [(-120, "120W"), (-90, "90W"), (-60, "60W"), (-30, "30W"), (0, "0 (GMT)"), (30, "30E"), (60, "60E"), (90, "90E"), (120, "120E"), (150, "150E")]
    for lon, t in marks:
        x = 236 + lon * 1.4
        b.append(L(x, y0 - 5, x, y0 + 5, "#333", 1.4)); b.append(T(x, y0 + 17, t, 7.2)); b.append(T(x, y0 + 28, f"{lon // 15:+d} h" if lon else "0 h", 7.2, fill=GOLD, weight="bold"))
    for lon, t, col in [(90, "BHUTAN 90E: GMT + 6 h", RED), (82.5, "", GREY), (151, "Sydney 151E: GMT + ~10 h", TEAL)]:
        pass
    b.append(C(236 + 90 * 1.4, y0, 4.5, RED, RED)); b.append(TL(236 + 90 * 1.4, 44, ["BHUTAN", "90E = GMT+6"], 7.4, fill=RED, weight="bold"))
    b.append(C(236, y0, 4.5, NAVY, NAVY)); b.append(TL(236, 44, ["LONDON", "0 = GMT"], 7.4, fill=NAVY, weight="bold"))
    
    b.append(C(236 + 151 * 1.4, y0, 4.5, PURPLE, PURPLE)); b.append(TL(236 + 151 * 1.4 - 8, 44, ["SYDNEY", "151E"], 7.4, fill=PURPLE, weight="bold"))
    b.append(R(14, 118, 442, 52, "#fff7e6", GOLD, 1.2, 3))
    b.append(TL(235, 132, ["EAST of a place = AHEAD in time (+).   WEST = BEHIND (-).", "Time difference = (longitude difference x 4) minutes.   Local time = GMT + (longitude / 15) h.", "Same longitude side: subtract the longitudes; opposite sides (E and W): add them."], 7.8, fill="#333", lh=12))
    save("timezones", 470, 176, "".join(b))


# 14 --------------------------------------------------------------- IAC numbering
def iac():
    b = []
    letters = "ABCDEFGHIJKLMNOP"
    s = 34
    ox, oy = 12, 22
    b.append(T(ox + 2 * s, 14, "Degree sheet 78 (1 deg x 1 deg)", 7.6, fill=NAVY, weight="bold"))
    for r in range(4):
        for c in range(4):
            k = c * 4 + r  # A..D down first column
            x, y = ox + c * s, oy + r * s
            hl = letters[k] == "E"
            b.append(R(x, y, s, s, "#fff3b0" if hl else "#fff", NAVY if hl else "#888", 2 if hl else 1, 0))
            b.append(T(x + s / 2, y + s / 2 + 3, letters[k], 9, fill=NAVY if hl else "#555", weight="bold" if hl else "normal"))
    # expand E
    ex, ey, es = 180, 22, 36
    b.append(T(ex + 2 * es, 14, "Sheet 78E split into 16 (15' x 15')", 7.6, fill=NAVY, weight="bold"))
    for r in range(4):
        for c in range(4):
            n = c * 4 + r + 1
            x, y = ex + c * es, ey + r * es
            hl = n == 11
            b.append(R(x, y, es, es, "#ffd24a" if hl else "#fff", RED if hl else "#888", 2.4 if hl else 1, 0))
            b.append(T(x + es / 2, y + es / 2 + 3, str(n), 9, fill=RED if hl else "#444", weight="bold" if hl else "normal"))
    b.append(L(ox + 1 * s + s, oy + 1 * s * 0 + 0, ex, ey, "#999", 1, "3 3"))
    b.append(R(340, 40, 124, 64, "#eef3fb", NAVY, 1.4, 3))
    b.append(TL(402, 58, ["Map number reads:", "degree sheet / letter", "/ number", "= 78E/11"], 7.8, fill=NAVY, weight="bold", lh=12))
    b.append(TL(402, 120, ["Columns count DOWN:", "1-4, 5-8, 9-12, 13-16", "so the highlighted cell", "(3rd column, 3rd row)", "is 11  (2025 Q1a-i: B)"], 7, fill="#333", lh=9.8))
    save("iac", 470, 180, "".join(b))


# 15 --------------------------------------------------------------- contours
def contours():
    b = []
    b.append(T(120, 12, "Contours of a hill", 8.4, fill=NAVY, weight="bold"))
    cx, cy = 120, 95
    for i, (rx, ry) in enumerate([(98, 70), (74, 52), (52, 36), (32, 22), (14, 10)]):
        col = BROWN
        b.append(f'<ellipse cx="{cx - (i * 3)}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{col}" stroke-width="{2.1 if i in (0, 4) else 1.3}"/>')
    for i, v in enumerate([100, 200, 300, 400]):
        b.append(T(cx - 98 + 4 + i * 23, cy - 2 - i * 0, str(v), 6.4, "start", BROWN))
    b.append(T(cx - 14, cy + 3, "peak", 6.8, "middle", RED))
    b.append(TL(120, 182, ["Close together = STEEP slope;", "far apart = GENTLE slope"], 7.4, fill="#333"))
    b.append(T(350, 12, "River valley: contours form a V pointing UPHILL", 8.2, fill=NAVY, weight="bold"))
    for k in range(4):
        y = 150 - k * 30
        b.append(P(f"M252,{y} L332,{y} L350,{y - 20} L368,{y} L448,{y}", "none", BROWN, 1.4))
        b.append(T(256, y - 3, str(100 + k * 100), 6.4, "start", BROWN))
    b.append(P("M350,168 L350,40", "none", BLUE, 2.2)); b.append(T(358, 160, "stream", 7, "start", BLUE)); b.append(T(350, 34, "higher ground", 7, fill=GREY))
    save("contours", 470, 200, "".join(b))


# 16 --------------------------------------------------------------- projected pop
def pop_proj():
    b = []
    years = [2017, 2022, 2027, 2032, 2037, 2042, 2047]
    vals = [727.1, 763.2, 797.3, 827, 851.2, 869.9, 883.9]
    gx, gy, gw, gh = 44, 22, 250, 104
    b.append(L(gx, gy + gh, gx + gw, gy + gh, "#333", 1.4)); b.append(L(gx, gy, gx, gy + gh, "#333", 1.4))
    for v in (0, 200, 400, 600, 800, 1000):
        y = gy + gh - v / 1000 * gh
        b.append(L(gx - 3, y, gx, y, "#333", 1)); b.append(T(gx - 5, y + 3, str(v), 6.6, "end"))
        if v: b.append(L(gx, y, gx + gw, y, "#e5e5e5", 0.7))
    st = gw / 7
    for i, (yr, v) in enumerate(zip(years, vals)):
        x = gx + i * st + st / 2
        h = v / 1000 * gh
        col = RED if yr in (2022, 2027) else BLUE
        b.append(R(x - 12, gy + gh - h, 24, h, col, "#223", 0.8, 0)); b.append(T(x, gy + gh - h - 3, str(v), 6.5)); b.append(T(x, gy + gh + 11, str(yr), 6.8))
    b.append(T(gx + gw / 2, 12, "Projected population of Bhutan (thousands)", 8, fill=NAVY, weight="bold"))
    b.append(R(312, 28, 152, 98, "#fff7e6", GOLD, 1.2, 3))
    b.append(TL(388, 42, ["2025 Q3(a): growth 2022 -> 2027", "797.3 - 763.2 = 34.1 thousand", "= 34,100 persons", "% growth = 34.1 / 763.2 x 100", "= 4.47 %  (about 4.5 %)", "(about 0.9 % a year)"], 7.4, fill="#333", lh=12.4))
    save("pop_proj", 470, 150, "".join(b))


# 17 --------------------------------------------------------------- growth rate line
def growth():
    b = []
    yrs = list(range(2012, 2023))
    vals = [1.09, 1.07, 1.02, 0.93, 0.87, 0.84, 0.79, 0.70, 0.66, 0.64, 0.64]
    gx, gy, gw, gh = 44, 24, 270, 96
    b.append(L(gx, gy + gh, gx + gw, gy + gh, "#333", 1.4)); b.append(L(gx, gy, gx, gy + gh, "#333", 1.4))
    for v in (0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2):
        y = gy + gh - v / 1.2 * gh
        b.append(L(gx - 3, y, gx, y, "#333", 1)); b.append(T(gx - 5, y + 3, f"{v:.1f}%", 6.5, "end"))
        if v: b.append(L(gx, y, gx + gw, y, "#e5e5e5", 0.7))
    st = gw / 11
    pts = []
    for i, (yr, v) in enumerate(zip(yrs, vals)):
        x = gx + i * st + st / 2
        y = gy + gh - v / 1.2 * gh
        pts.append((x, y)); b.append(T(x, gy + gh + 10, str(yr)[2:], 6.6))
    b.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{BLUE}" stroke-width="2"/>')
    for (x, y), v in zip(pts, vals):
        b.append(C(x, y, 2.6, BLUE, BLUE))
    b.append(T(gx + gw / 2, 12, "Population growth rate of Bhutan 2012-2022 (%)", 8, fill=NAVY, weight="bold"))
    b.append(R(332, 28, 132, 100, "#fff7e6", GOLD, 1.2, 3))
    b.append(TL(398, 42, ["Falls from 1.09% to 0.64%", "If it continues:", "- ageing population", "- fewer workers, labour", "  shortage; more imports", "- higher dependency", "- fewer students: school", "  closures; slower growth"], 6.9, fill="#333", lh=11.4))
    save("growth", 470, 150, "".join(b))


# 18 --------------------------------------------------------------- central place theory
def central():
    b = []
    def hexagon(cx, cy, r, fill, stroke):
        return poly([(cx + r * math.cos(math.radians(60 * k + 30)), cy + r * math.sin(math.radians(60 * k + 30))) for k in range(6)], fill, stroke, 1.2)
    r = 24
    dx = r * math.sqrt(3)
    cx0, cy0 = 120, 96
    cells = [(0, 0)]
    for k in range(6):
        a = math.radians(60 * k)
        cells.append((dx * math.cos(a), dx * math.sin(a)))
    for i, (x, y) in enumerate(cells):
        b.append(hexagon(cx0 + x, cy0 + y, r, "#fff7d6" if i else "#fde3a7", GOLD))
    for k in range(6):
        a = math.radians(60 * k)
        x, y = cx0 + dx * math.cos(a), cy0 + dx * math.sin(a)
        b.append(C(x, y, 4, TEAL, TEAL))
    for k in range(6):
        a = math.radians(60 * k + 30)
        x, y = cx0 + 2 * dx * 0.87 * math.cos(a) * 1.0, cy0 + 2 * dx * 0.87 * math.sin(a)
        b.append(C(x, y, 2.6, GREY, GREY))
    b.append(C(cx0, cy0, 7, RED, RED))
    b.append(T(120, 14, "Christaller's Central Place Theory", 8.6, fill=NAVY, weight="bold"))
    b.append(R(250, 22, 214, 140, "#eef3fb", NAVY, 1.2, 3))
    items = [(RED, "City / large town (high-order goods: hospital, university)"), (TEAL, "Town (medium goods)"), (GREY, "Village (low-order: salt, rice, vegetables)")]
    for i, (col, tx) in enumerate(items):
        b.append(C(262, 40 + i * 14, 4, col, col)); b.append(T(272, 43 + i * 14, tx, 6.8, "start"))
    b.append(TL(357, 90, ["Key ideas:", "- people travel SHORT distances for", "  low-order goods and FAR for high-order", "- hexagonal market areas (no gaps/overlap)", "- many villages, fewer towns, few cities", "- THRESHOLD = minimum customers", "- RANGE = maximum distance travelled"], 6.8, "middle", "#333", lh=10.4))
    save("central", 470, 176, "".join(b))


# 19 --------------------------------------------------------------- biodiversity levels
def biodiv():
    b = []
    b.append(C(120, 98, 86, "#e2f2e2", GREEN, 1.8)); b.append(C(120, 114, 58, "#fff7d6", GOLD, 1.8)); b.append(C(120, 126, 30, "#fde3e3", RED, 1.8))
    b.append(T(120, 34, "ECOSYSTEM diversity", 8.2, fill=GREEN, weight="bold")); b.append(T(120, 74, "SPECIES diversity", 8.2, fill=GOLD, weight="bold")); b.append(T(120, 126, "GENETIC", 7.6, fill=RED, weight="bold")); b.append(T(120, 136, "diversity", 7.6, fill=RED, weight="bold"))
    rows = [("Genetic diversity", "variety of genes within ONE species", "e.g. many local rice, maize and potato varieties; different yak breeds", RED),
            ("Species diversity", "number/variety of species in an area", "e.g. tiger, takin, red panda, black-necked crane, 5,500+ plant species", GOLD),
            ("Ecosystem diversity", "variety of habitats and ecosystems", "e.g. subtropical forest, temperate forest, alpine meadow, wetlands", GREEN)]
    for i, (t, a, c2, col) in enumerate(rows):
        y = 30 + i * 52
        b.append(R(222, y, 244, 44, "#fff", col, 1.4, 3)); b.append(T(230, y + 13, t, 8, "start", col, "bold")); b.append(T(230, y + 25, a, 6.9, "start")); b.append(T(230, y + 36, c2, 6.4, "start", "#555"))
    save("biodiv", 470, 196, "".join(b))


# 20 --------------------------------------------------------------- disaster cycle
def dm_cycle():
    b = []
    cx, cy, R0 = 235, 92, 62
    nodes = [("PREPAREDNESS", "plans, drills, early warning,", "emergency kits", NAVY, -90), ("RESPONSE", "rescue, first aid, shelter,", "food, communication", RED, 0), ("RECOVERY", "rebuild homes, schools,", "education in emergency", TEAL, 90), ("MITIGATION", "reduce risk: building codes,", "land use, tree planting", GOLD, 180)]
    for t, a, c2, col, ang in nodes:
        x, y = cx + R0 * 1.9 * math.cos(math.radians(ang)), cy + R0 * 1.0 * math.sin(math.radians(ang))
        b.append(R(x - 66, y - 18, 132, 36, "#fff", col, 1.8, 4)); b.append(T(x, y - 4, t, 8.2, fill=col, weight="bold")); b.append(TL(x, y + 6, [a], 6.4, fill="#333")); b.append(T(x, y + 14, c2, 6.4, fill="#333"))
    b.append(P(f"M{cx + 26},{cy - 44} Q{cx + 110},{cy - 46} {cx + 118},{cy - 22}", "none", "#666", 1.6).replace("/>", ' marker-end="url(#a)"/>'))
    b.append(P(f"M{cx + 118},{cy + 22} Q{cx + 110},{cy + 46} {cx + 26},{cy + 44}", "none", "#666", 1.6).replace("/>", ' marker-end="url(#a)"/>'))
    b.append(P(f"M{cx - 26},{cy + 44} Q{cx - 110},{cy + 46} {cx - 118},{cy + 22}", "none", "#666", 1.6).replace("/>", ' marker-end="url(#a)"/>'))
    b.append(P(f"M{cx - 118},{cy - 22} Q{cx - 110},{cy - 46} {cx - 26},{cy - 44}", "none", "#666", 1.6).replace("/>", ' marker-end="url(#a)"/>'))
    b.append(TL(cx, cy - 4, ["DISASTER", "MANAGEMENT", "CYCLE"], 8, fill="#444", weight="bold", lh=10.4))
    save("dm_cycle", 470, 190, "".join(b))


# 21 --------------------------------------------------------------- GLOF
def glof():
    H.flow("glof", [
        ("1. Global warming", ["temperature rises;", "glaciers melt and", "retreat quickly"]),
        ("2. Glacial lake", ["meltwater collects", "behind a moraine", "(loose rock) dam"]),
        ("3. Lake grows", ["water volume and", "pressure on the", "weak dam increase"]),
        ("4. Trigger", ["earthquake, avalanche,", "landslide or heavy", "rain breaks the dam"]),
        ("5. GLOF", ["sudden huge flood", "down the valley:", "Punakha, 1994"]),
        ("6. Damage", ["lives, homes, farms,", "bridges, roads, power;", "soil erosion"]),
    ], per=3)


# 22 --------------------------------------------------------------- mineral tree
def mineral_tree():
    b = []
    b.append(box(185, 6, 100, 22, "MINERALS", (), NAVY, "#e4ecf7", 9))
    heads = [("METALLIC", 8, NAVY, [("Ferrous (contain iron)", "iron, manganese,", "chromium"), ("Non-ferrous", "copper, gold, lead,", "zinc, aluminium")]),
             ("NON-METALLIC", 168, GREEN, [("Organic (fossil origin)", "coal, petroleum", "(fuels)"), ("Inorganic", "limestone, gypsum, mica,", "dolomite, sapphire")]),
             ("ENERGY MINERALS", 328, GOLD, [("Give fuel / nuclear power", "coal, petroleum, natural", "gas, uranium, thorium")])]
    for nm, x, col, subs in heads:
        b.append(L(235, 28, x + 70, 50, "#666", 1.4)); b.append(box(x, 50, 140, 20, nm, (), col, "#fff", 8.2))
        for j, (a, c1, c2) in enumerate(subs):
            y = 86 + j * 56
            b.append(L(x + 2, 60, x + 2, y + 24, "#aaa", 1)); b.append(L(x + 2, y + 24, x + 4, y + 24, "#aaa", 1)); b.append(R(x + 4, y, 132, 48, "#fff", col, 1.2, 3)); b.append(T(x + 70, y + 12, a, 7.3, fill=col, weight="bold")); b.append(T(x + 70, y + 25, c1, 6.8)); b.append(T(x + 70, y + 36, c2, 6.8))
    save("mineral_tree", 470, 202, "".join(b))


# 23 --------------------------------------------------------------- industry sectors
def sectors():
    H.flow("sectors", [
        ("PRIMARY", ["extracts raw materials:", "farming, forestry,", "mining, fishing"]),
        ("SECONDARY", ["manufactures / builds:", "cement, steel, food", "processing, hydropower"]),
        ("TERTIARY", ["services: trade, banks,", "teaching, tourism,", "transport, health"]),
        ("QUATERNARY", ["knowledge: research &", "development, IT, data,", "financial planning"]),
    ], per=4, bw=108, bh=44, gx=14)


# 24 --------------------------------------------------------------- cold house
def cold_house():
    b = []
    b.append(L(10, 150, 300, 150, "#6b8e23", 4))
    b.append(poly([(60, 96), (150, 58), (240, 96)], "#c9a27a", BROWN, 1.8)); b.append(T(150, 52, "sloped wooden / slate roof", 7.4, fill=BROWN, weight="bold"))
    b.append(R(70, 96, 160, 54, "#e8e1d0", "#6b5a3a", 3.2, 0))
    b.append(R(90, 112, 18, 16, "#bfe3f5", NAVY, 1.4, 0)); b.append(R(190, 112, 18, 16, "#bfe3f5", NAVY, 1.4, 0)); b.append(R(136, 118, 26, 32, "#8b5a2b", "#444", 1.4, 0))
    b.append(L(60, 80, 30, 70, RED, 1.2)); b.append(T(30, 66, "snow slides off", 6.8, "middle", BLUE))
    b.append(T(150, 168, "THICK stone / rammed-earth walls", 7.4, fill="#6b5a3a", weight="bold"))
    b.append(R(318, 22, 148, 138, "#eef3fb", NAVY, 1.2, 3))
    b.append(TL(392, 38, ["Why (Lunana / cold areas):", "", "1 Thick walls store heat", "  and block cold wind", "2 Sloped roof sheds snow", "  and rain", "3 Light wood/slate roof:", "  local, easy to repair", "4 Few, small south-facing", "  windows; low ceilings;", "  animals below, family above"], 6.9, fill="#333", lh=11))
    save("cold_house", 470, 176, "".join(b))


# 25 --------------------------------------------------------------- Bhutan sketch
def bhutan_sketch():
    b = []
    X0, Y0, S = 50, 28, 112.0
    def xy(lon, lat):
        return (X0 + (lon - 88.7) * S, Y0 + (28.4 - lat) * S)
    outline = [(88.75, 27.30), (88.95, 27.60), (89.15, 27.95), (89.55, 28.20), (89.95, 28.32), (90.40, 28.25), (91.00, 28.05), (91.70, 28.30), (91.90, 27.65), (92.10, 27.30), (92.10, 26.95), (91.50, 26.85), (90.50, 26.78), (89.50, 26.72), (88.85, 26.85)]
    b.append(poly([xy(*p) for p in outline], "#e6f0dc", "#4a7a3a", 2))
    for lon in (89, 90, 91, 92):
        x, _ = xy(lon, 28)
        b.append(L(x, 20, x, 226, "#ccc", 0.8, "3 3")); b.append(T(x, 236, f"{lon}E", 6.8, fill=GREY))
    for lat in (27, 28):
        _, y = xy(89, lat)
        b.append(L(40, y, 450, y, "#ccc", 0.8, "3 3")); b.append(T(36, y + 3, f"{lat}N", 6.8, "end", GREY))
    pts = [("Jhomolhari (peak, mark with a triangle)", 89.27, 27.83, "tri", RED), ("Masa Gang / Tsenda Gang (peaks, NW)", 89.75, 28.12, "tri", RED),
           ("Punakha Dzong (First King enthroned; dot)", 89.86, 27.58, "dot", NAVY), ("Simtokha Dzong (first dzong, Thimphu; DZ)", 89.68, 27.43, "dz", PURPLE),
           ("Dochula Pass (108 chortens; X)", 89.75, 27.50, "x", GOLD), ("Phobjikha / Gangtey (crane festival; dot)", 90.17, 27.47, "dot", GREEN),
           ("Pele La (Wangdue - Trongsa; ][ )", 90.20, 27.40, "x", GOLD), ("Royal Manas NP (oldest protected area; OP)", 90.80, 26.85, "op", TEAL),
           ("Chhukha (first hydropower, on Wang Chhu)", 89.55, 27.00, "dot", BLUE)]
    labs = []
    for i, (nm, lon, lat, kind, col) in enumerate(pts):
        x, y = xy(lon, lat)
        if kind == "tri": b.append(poly([(x, y - 6), (x - 5, y + 3), (x + 5, y + 3)], col, col, 1))
        elif kind == "dot": b.append(C(x, y, 3.6, col, col))
        elif kind == "dz": b.append(R(x - 6, y - 4, 12, 8, "#fff", col, 1.4, 1)); b.append(T(x, y + 3, "DZ", 5.5, fill=col, weight="bold"))
        elif kind == "x": b.append(T(x, y + 4, "X", 9, fill=col, weight="bold"))
        else: b.append(R(x - 7, y - 4, 14, 8, "#fff", col, 1.4, 1)); b.append(T(x, y + 3, "OP", 5.5, fill=col, weight="bold"))
        labs.append((i + 1, nm, x, y))
    for n, nm, x, y in labs:
        off = (8, 12) if n in (3, 5) else ((-4, -8) if n == 4 else (6, -5))
        b.append(f'<text x="{x + off[0]:.1f}" y="{y + off[1] - 4:.1f}" font-size="7" fill="#111" font-weight="bold">{n}</text>')
    for pts_ in [[(89.3, 27.62), (89.45, 27.3), (89.6, 27.0)], [(91.0, 27.8), (91.4, 27.3), (91.75, 26.85)]]:
        b.append(P("M" + " L".join(f"{xy(*p)[0]:.1f},{xy(*p)[1]:.1f}" for p in pts_), "none", BLUE, 2))
    b.append(T(xy(89.25, 27.3)[0], xy(89.25, 27.3)[1], "Wang Chhu", 6.4, "end", BLUE)); b.append(T(xy(91.45, 27.45)[0] + 4, xy(91.45, 27.45)[1], "Drangme Chhu", 6.4, "start", BLUE)); b.append(T(xy(91.45, 27.45)[0] + 4, xy(91.45, 27.45)[1] + 8, "(largest basin)", 6.2, "start", BLUE))
    for i, (n, nm, x, y) in enumerate(labs):
        col = i % 2
        row = i // 2
        b.append(T(20 + col * 235, 258 + row * 11, f"{n}  {nm}", 6.4, "start", "#222"))
    b.append(T(235, 10, "Bhutan: schematic location guide (NOT to scale; use your atlas for exact positions)", 7.8, fill=NAVY, weight="bold"))
    save("bhutan_sketch", 470, 318, "".join(b))


# 26 --------------------------------------------------------------- Asia sketch
def asia_sketch():
    b = []
    X0, Y0 = 20, 20
    def xy(lon, lat):
        return (X0 + (lon - 25) * 3.35, Y0 + (78 - lat) * 3.1)
    b.append(R(X0, Y0, 3.35 * 130, 3.1 * 78, "#f4f8fc", "#bbb", 1, 3))
    for lon in range(30, 160, 30):
        x, _ = xy(lon, 0); b.append(L(x, Y0, x, Y0 + 3.1 * 78, "#ddd", 0.7, "3 3")); b.append(T(x, Y0 + 3.1 * 78 + 9, f"{lon}E", 6.5, fill=GREY))
    for lat in range(0, 80, 20):
        _, y = xy(30, lat); b.append(L(X0, y, X0 + 3.35 * 130, y, "#ddd", 0.7, "3 3")); b.append(T(X0 - 3, y + 3, f"{lat}N", 6.5, "end", GREY))
    def ell(lon, lat, rx, ry, fill, stroke, label, lx=0, ly=0, col="#222", size=6.6):
        x, y = xy(lon, lat)
        b.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="1.4" fill-opacity=".75"/>')
        b.append(T(x + lx, y + ly + 2, label, size, fill=col, weight="bold"))
    ell(80, 33, 38, 11, "#d9b98a", BROWN, "TIBETAN PLATEAU", 0, 0, BROWN)
    ell(47, 22, 20, 11, "#f2d27a", GOLD, "ARABIAN", 0, -3, "#7a5200"); b.append(T(xy(47, 22)[0], xy(47, 22)[1] + 9, "DESERT", 6.6, fill="#7a5200", weight="bold"))
    ell(34, 43, 14, 4, "#bfe3f5", BLUE, "", 0, 0, BLUE); b.append(T(xy(34, 43)[0], xy(34, 43)[1] + 14, "BLACK SEA", 6.4, fill=BLUE, weight="bold"))
    ell(124, 36, 7, 7, "#bfe3f5", BLUE, "", 0, 0, BLUE); b.append(T(xy(124, 36)[0] + 12, xy(124, 36)[1] - 1, "YELLOW", 6.4, "start", BLUE, "bold")); b.append(T(xy(124, 36)[0] + 12, xy(124, 36)[1] + 7, "SEA", 6.4, "start", BLUE, "bold"))
    # Urals
    pts = [(59, 52), (60, 58), (61, 64), (62, 68)]
    b.append(P("M" + " L".join(f"{xy(*p)[0]:.1f},{xy(*p)[1]:.1f}" for p in pts), "none", RED, 3)); b.append(T(xy(62, 66)[0] + 6, xy(62, 66)[1], "URALS (N-S range)", 6.6, "start", RED, "bold"))
    # Caucasus
    pts = [(38, 44), (42, 43), (47, 41.5)]
    b.append(P("M" + " L".join(f"{xy(*p)[0]:.1f},{xy(*p)[1]:.1f}" for p in pts), "none", RED, 3)); b.append(T(xy(43, 45)[0], xy(43, 45)[1] - 2, "CAUCASUS", 6.6, "middle", RED, "bold"))
    # Yellow River & Yangtze
    b.append(P("M" + " L".join(f"{xy(*p)[0]:.1f},{xy(*p)[1]:.1f}" for p in [(96, 35), (103, 36), (107, 39), (111, 40), (112, 35), (118, 36), (119, 37.5)]), "none", GOLD, 2.2)); b.append(T(xy(108, 41.5)[0], xy(108, 41.5)[1], "HWANG HO (Yellow R.)", 6.4, "middle", GOLD, "bold"))
    b.append(P("M" + " L".join(f"{xy(*p)[0]:.1f},{xy(*p)[1]:.1f}" for p in [(92, 33), (98, 30), (104, 29), (110, 30.5), (116, 30.5), (121, 31.3)]), "none", BLUE, 2.2)); b.append(T(xy(108, 27)[0], xy(108, 27)[1], "YANGTZE (Chang Jiang)", 6.4, "middle", BLUE, "bold"))
    for nm, lon, lat in [("INDIA", 78, 22), ("CHINA", 110, 47), ("RUSSIA", 95, 62), ("JAPAN", 137, 38), ("BHUTAN *", 90.5, 27.3), ("INDONESIA", 112, 0)]:
        x, y = xy(lon, lat); b.append(T(x, y, nm, 6.4, fill="#888"))
    b.append(T(235, 12, "Asia: schematic location guide for the outline-map task (positions approximate)", 7.8, fill=NAVY, weight="bold"))
    save("asia_sketch", 470, 276, "".join(b))


def pangaea():
    H.flow("pangaea", [
        ("~300-200 mya", ["ALL land joined:", "supercontinent PANGAEA", "one ocean: Panthalassa"]),
        ("~200 mya", ["Pangaea splits:", "LAURASIA (north) and", "GONDWANA (south)"]),
        ("~65 mya on", ["continents drift to", "present positions;", "India hits Eurasia"]),
    ], per=3)


def pangaea_effects():
    b = []
    b.append(R(8, 8, 224, 98, "#fff", GOLD, 1.5, 4)); b.append(T(120, 22, "If all continents joined again (consequences)", 8, fill=GOLD, weight="bold"))
    b.append(TL(14, 36, ["1 Vast dry interior far from the sea: huge", "  deserts, extreme hot/cold (continental climate)", "2 One giant ocean, shorter coastline: less", "  coastal rainfall, fewer marine habitats", "3 Species mix; competition; extinction of some", "4 Old mountains erode, new ones where plates collide"], 6.9, "start", "#333", lh=10.6))
    b.append(R(240, 8, 222, 98, "#fff", NAVY, 1.5, 4)); b.append(T(351, 22, "Evidence for continental drift (Wegener)", 8, fill=NAVY, weight="bold"))
    b.append(TL(246, 36, ["1 Jigsaw fit: S. America / Africa coasts", "2 Same fossils (Mesosaurus, Glossopteris)", "3 Matching rock strata and coalfields", "4 Glacial deposits in now-warm lands", "5 Later: sea-floor spreading, GPS plate movement"], 6.9, "start", "#333", lh=11.4))
    save("pangaea_effects", 470, 114, "".join(b))


def rain_pop_note():
    pass


if __name__ == "__main__":
    for f in (big_bang, nebula, earth_layers, plates, himalaya, gts, wind, karst, drainage, zones, climograph, orographic, timezones, iac, contours, pop_proj, growth, central, biodiv, dm_cycle, glof, mineral_tree, sectors, cold_house, bhutan_sketch, asia_sketch, pangaea, pangaea_effects):
        f()
    print(sorted(p.name for p in H.OUT.glob("*.svg")))
