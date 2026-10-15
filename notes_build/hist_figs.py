#!/usr/bin/env python3
"""Diagrams for the History notes -> figs_h/*.svg (hand-built SVG)."""
import math, pathlib

OUT = pathlib.Path(__file__).parent / "figs_h"
OUT.mkdir(exist_ok=True)
NAVY, TEAL, GOLD, RED, GREY, GREEN, PURPLE = "#0e3a66", "#0f7b6c", "#b36200", "#b3211b", "#666", "#2a7a3a", "#5b3a8a"
FONT = 'font-family="DejaVu Sans, Liberation Sans, Arial, sans-serif"'
DEFS = ('<defs><marker id="a" markerUnits="userSpaceOnUse" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="context-stroke"/></marker></defs>')


def save(name, w, h, body):
    (OUT / f"{name}.svg").write_text(f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" {FONT}>{DEFS}{body}</svg>', encoding="utf-8")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def T(x, y, s, size=9, anchor="middle", fill="#111", weight="normal", style="normal"):
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{fill}" font-weight="{weight}" font-style="{style}">{esc(s)}</text>'


def TL(x, y, lines, size=8, anchor="middle", fill="#111", weight="normal", lh=None):
    lh = lh or size * 1.22
    return "".join(T(x, y + i * lh, ln, size, anchor, fill, weight) for i, ln in enumerate(lines))


def L(x1, y1, x2, y2, c="#333", w=1.4, dash=None, arrow=False):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = ' marker-end="url(#a)"' if arrow else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}"{d}{m}/>'


def R(x, y, w, h, fill="#fff", stroke="#333", sw=1.3, rx=3):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def C(x, y, r, fill="#fff", stroke="#333", sw=1.3):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def P(d, fill="none", stroke="#333", sw=1.5, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{da}/>'


def box(x, y, w, h, title, lines=(), col=NAVY, fill="#fff", tsize=8.6, lsize=7.4):
    b = [R(x, y, w, h, fill, col, 1.5)]
    if lines:
        b.append(T(x + w / 2, y + 11.5, title, tsize, fill=col, weight="bold"))
        b.append(TL(x + w / 2, y + 22.5, list(lines), lsize))
    else:
        n = title.split("\n")
        b.append(TL(x + w / 2, y + h / 2 - (len(n) - 1) * 5 + 3, n, tsize, fill=col, weight="bold"))
    return "".join(b)


def timeline(name, items, w=470, h=190, title=None):
    """items: (label, text-lines) alternate above/below a central line"""
    n = len(items)
    pad = 52
    step = (w - 2 * pad) / max(n - 1, 1)
    b = []
    if title:
        b.append(T(w / 2, 13, title, 9.5, fill=NAVY, weight="bold"))
    cy = h / 2 + (6 if title else 0)
    b.append(L(14, cy, w - 14, cy, NAVY, 3))
    for i, (lab, lines) in enumerate(items):
        x = pad + i * step
        up = i % 2 == 0
        col = TEAL if up else GOLD
        b.append(C(x, cy, 5.5, col, col))
        if up:
            b.append(L(x, cy - 6, x, cy - 22, "#999", 1))
            b.append(T(x, cy - 66 + 38 - 24 - 6 + 24 - 2, "", 1))
            ys = cy - 26 - len(lines) * 9.2
            b.append(T(x, ys - 3, lab, 8.2, fill=NAVY, weight="bold"))
            b.append(TL(x, ys + 8, lines, 6.9, lh=8.6))
        else:
            b.append(L(x, cy + 6, x, cy + 22, "#999", 1))
            b.append(T(x, cy + 32, lab, 8.2, fill=NAVY, weight="bold"))
            b.append(TL(x, cy + 42, lines, 6.9, lh=8.6))
    save(name, w, h, "".join(b))


# 1 ------------------------------------------------------------------ Indus town plan
def indus():
    b = []
    b.append(R(10, 8, 450, 176, "#fbf5e6", "#999", 1, 4))
    b.append(R(25, 22, 150, 54, "#e3c9a0", RED, 1.8))
    b.append(T(100, 41, "CITADEL (raised, west)", 8.5, fill=RED, weight="bold"))
    b.append(R(40, 50, 52, 20, "#bfe3f5", NAVY, 1.4)); b.append(T(66, 63, "Great Bath", 7.2))
    b.append(R(108, 50, 52, 20, "#e8d35e", GOLD, 1.4)); b.append(T(134, 63, "Granary", 7.2))
    # lower town grid
    for i in range(6):
        b.append(L(190 + i * 52, 22, 190 + i * 52, 176, "#a9772e", 5))
    for j in range(4):
        b.append(L(25, 96 + j * 28, 450, 96 + j * 28, "#a9772e", 5))
    for i in range(5):
        for j in range(3):
            b.append(R(197 + i * 52, 102 + j * 28, 38, 16, "#d9b98a", "#8a5a1c", 1, 1))
    b.append(T(325, 17, "LOWER TOWN: fire-baked brick houses on a GRID", 7.6, fill=NAVY, weight="bold"))
    b.append(L(190, 40, 440, 40, TEAL, 2.4, dash="6 3"))
    b.append(T(318, 36, "covered brick drain along the street, with manholes", 7, fill=TEAL))
    b.append(C(262, 150, 4, TEAL, TEAL)); b.append(T(272, 153, "soak pit / waste bin at the house front", 6.8, anchor="start", fill=TEAL))
    b.append(TL(100, 108, ["Streets cross at", "RIGHT ANGLES", "(grid pattern)"], 7.6, fill="#5a3a0a", weight="bold"))
    b.append(TL(100, 146, ["Every house: bath-room", "drain joins the street", "drain"], 7, fill="#444"))
    save("indus_plan", 470, 190, "".join(b))


# 2 ------------------------------------------------------------------ Buddha's life
def buddha():
    timeline("buddha_life", [
        ("c. 563 BCE", ["Birth at Lumbini", "(Siddhartha Gautama,", "Shakya prince)"]),
        ("Age 29", ["GREAT RENUNCIATION:", "leaves palace after", "the Four Sights"]),
        ("6 years", ["extreme fasting;", "gives it up: MIDDLE", "PATH"]),
        ("Age 35", ["ENLIGHTENMENT", "under the Bodhi tree,", "Bodh Gaya"]),
        ("Soon after", ["FIRST SERMON,", "Deer Park, Sarnath", "(Four Noble Truths)"]),
        ("Age 80", ["MAHAPARINIRVANA", "at Kushinagar"]),
    ], 470, 200, "Life of the Buddha")


# 3 ------------------------------------------------------------------ eightfold path
def eightfold():
    b = []
    cx, cy, r = 160, 105, 48
    b.append(C(cx, cy, r, "#fff7e0", GOLD, 2.4)); b.append(C(cx, cy, 14, GOLD, GOLD))
    groups = [("Right View", NAVY), ("Right Intention", NAVY), ("Right Speech", TEAL), ("Right Action", TEAL), ("Right Livelihood", TEAL), ("Right Effort", PURPLE), ("Right Mindfulness", PURPLE), ("Right Concentration", PURPLE)]
    for i, (nm, col) in enumerate(groups):
        a = -math.pi / 2 + i * 2 * math.pi / 8
        b.append(L(cx + 14 * math.cos(a), cy + 14 * math.sin(a), cx + r * math.cos(a), cy + r * math.sin(a), GOLD, 2))
        rr = r + 12
        x, y = cx + rr * math.cos(a), cy + rr * math.sin(a)
        anc = "middle" if abs(math.cos(a)) < 0.3 else ("start" if math.cos(a) > 0 else "end")
        b.append(T(x + (4 if anc == "start" else -4 if anc == "end" else 0), y + (4 if abs(math.sin(a)) < 0.3 else (9 if math.sin(a) > 0 else -4)), nm, 7.4, anc, col, "bold"))
    b.append(R(308, 36, 156, 38, "#e4ecf7", NAVY, 1.3)); b.append(T(386, 50, "WISDOM (Panna)", 8, fill=NAVY, weight="bold")); b.append(T(386, 63, "View, Intention", 7.4))
    b.append(R(308, 82, 156, 50, "#dff1ee", TEAL, 1.3)); b.append(T(386, 96, "ETHICAL CONDUCT (Sila)", 8, fill=TEAL, weight="bold")); b.append(T(386, 109, "Speech, ACTION,", 7.4)); b.append(T(386, 121, "Livelihood", 7.4))
    b.append(R(308, 140, 156, 38, "#ece4f6", PURPLE, 1.3)); b.append(T(386, 154, "MENTAL DISCIPLINE (Samadhi)", 8, fill=PURPLE, weight="bold")); b.append(T(386, 167, "Effort, Mindfulness, Focus", 7.4))
    b.append(T(386, 18, "The Noble Eightfold Path", 8.6, fill=NAVY, weight="bold"))
    save("eightfold", 470, 200, "".join(b))


# 4 ------------------------------------------------------------------ triangular trade
def triangle():
    b = []
    b.append(box(190, 10, 90, 34, "EUROPE", (), NAVY, "#e4ecf7", 9.5))
    b.append(box(20, 128, 110, 34, "THE AMERICAS\n(plantations)", (), GREEN, "#e3f3e5", 8.5))
    b.append(box(340, 128, 110, 34, "WEST AFRICA", (), GOLD, "#fbeed6", 9.5))
    b.append(L(265, 46, 380, 126, NAVY, 2.4, arrow=True))
    b.append(TL(350, 74, ["Z: MANUFACTURED", "GOODS (guns, cloth,", "rum, iron)"], 7.2, anchor="start", fill=NAVY, weight="bold"))
    b.append(L(338, 150, 134, 150, GOLD, 2.4, arrow=True))
    b.append(TL(236, 178, ["X: ENSLAVED AFRICANS (the Middle Passage)"], 7.2, fill=GOLD, weight="bold"))
    b.append(L(60, 126, 192, 40, GREEN, 2.4, arrow=True))
    b.append(TL(8, 76, ["Y: RAW MATERIALS", "(sugar, cotton,", "tobacco, rum)"], 7.2, anchor="start", fill=GREEN, weight="bold"))
    b.append(T(235, 105, "Atlantic triangular trade", 8.6, fill="#444", style="italic"))
    save("triangle", 470, 190, "".join(b))


# 5 ------------------------------------------------------------------ choe-sid
def choesid():
    b = []
    b.append(box(165, 6, 140, 30, "ZHABDRUNG NGAWANG\nNAMGYAL (supreme)", (), RED, "#fbe9e8", 8))
    b.append(L(210, 36, 105, 62, "#555", 1.5, arrow=True)); b.append(L(260, 36, 365, 62, "#555", 1.5, arrow=True))
    b.append(box(20, 62, 170, 42, "CHOE (religion)", ("JE KHENPO - Chief Abbot", "heads the Central Monastic Body"), NAVY, "#e4ecf7"))
    b.append(box(280, 62, 170, 42, "SID (state)", ("DRUK DESI - civil ruler", "(3-year term, Council-elected)"), TEAL, "#dff1ee"))
    b.append(L(365, 104, 365, 124, "#555", 1.5, arrow=True))
    b.append(box(190, 124, 260, 36, "CHOGI CHILA NAMSUM (3 Poenlops)", ("Paro (west)  |  Dagana (south)  |  Trongsa (east)",), GOLD, "#fbeed6", 8.4, 7.2))
    b.append(L(320, 160, 320, 172, "#555", 1.5, arrow=True))
    b.append(box(190, 172, 260, 18, "Dzongpoens (dzong governors)", (), GREY, "#f1f1f1", 7.6))
    b.append(box(20, 124, 150, 36, "Dzong = both monastery", ("and administrative centre",), PURPLE, "#efe7f6", 8, 7))
    save("choesid", 470, 196, "".join(b))


# 6 ------------------------------------------------------------------ Bhutan-British timeline
def bb():
    timeline("bhutan_british", [
        ("1772-74", ["Cooch Behar war;", "Panchen Lama's", "mediation; Treaty 1774"]),
        ("1775", ["Bogle's trade", "treaty (May)"]),
        ("1783", ["Samuel Turner's", "mission"]),
        ("1864", ["Eden mission;", "Duar War begins", "(12 Nov)"]),
        ("1865", ["Treaty of Sinchula", "(11 Nov)"]),
        ("1903-04", ["Younghusband;", "Ugyen Wangchuck", "mediates; KCIE 1905"]),
        ("1907", ["Ugyen Wangchuck", "becomes first", "Druk Gyalpo"]),
        ("1910", ["Treaty of Punakha", "(subsidy Rs 100,000)"]),
        ("1949", ["Indo-Bhutan Treaty", "(Rs 500,000;", "Dewathang back)"]),
        ("2007", ["Revised Treaty:", "greater autonomy"]),
    ], 470, 215, "Bhutan - British India - India: key dates")


# 7 ------------------------------------------------------------------ monarchy
def monarchy():
    timeline("monarchy", [
        ("1907-26", ["1st King", "Ugyen Wangchuck"]),
        ("1926-52", ["2nd King", "Jigme Wangchuck"]),
        ("1952-72", ["3rd King", "Jigme Dorji W.", "(modernisation)"]),
        ("1972-2006", ["4th King", "Jigme Singye W.", "(GNH, democracy)"]),
        ("2006-", ["5th King", "Jigme Khesar", "Namgyel W."]),
    ], 470, 165, "The Wangchuck dynasty")


# 8 ------------------------------------------------------------------ env flow (Q1xi)
def envflow():
    b = []
    b.append(box(120, 6, 230, 26, "SIGNIFICANCE OF ENVIRONMENT (Article 5)", (), NAVY, "#e4ecf7", 8.4))
    xs = [10, 124, 238, 352]
    labs = [("Every Bhutanese is a", "TRUSTEE (5.1)"), ("GOVERNMENT is", "responsible (5.2)"), ("LEGISLATION by", "Parliament (5.5)"), ("X = 60% FOREST", "COVER / PAs")]
    cols = [TEAL, TEAL, TEAL, RED]
    for x, (a, c2), col in zip(xs, labs, cols):
        b.append(L(235, 32, x + 54, 66, "#777", 1.2))
        b.append(R(x, 66, 108, 38, "#fff" if col != RED else "#fdecec", col, 1.6)); b.append(T(x + 54, 82, a, 7.8, fill=col, weight="bold")); b.append(T(x + 54, 95, c2, 7.8, fill=col, weight="bold"))
    b.append(T(235, 122, "Box X in the 2025 paper = a government commitment about Protected Areas / forest cover (best option A).", 6.9, fill="#555"))
    save("env_flow", 470, 130, "".join(b))


# 9 ------------------------------------------------------------------ medieval vs modern
def hist_compare():
    b = []
    b.append(box(10, 6, 215, 24, "MEDIEVAL historiography", (), GOLD, "#fbeed6", 9))
    b.append(box(245, 6, 215, 24, "MODERN historiography", (), TEAL, "#dff1ee", 9))
    rows = [("Based on religion, will of God, myths", "Based on reason and evidence"),
            ("Focus: kings, wars, saints, glory of rulers", "Focus: all people, society, economy, women, environment"),
            ("Written by monks / court scribes (patrons)", "Written by trained historians (objective)"),
            ("Sources taken on trust, no checking", "Sources cross-checked; archaeology, oral history"),
            ("Single (religious / royal) viewpoint", "Many viewpoints; inclusive voices")]
    for i, (l, r) in enumerate(rows):
        y = 38 + i * 26
        b.append(R(10, y, 215, 22, "#fff", GOLD, 1)); b.append(T(117, y + 14, l, 7.2))
        b.append(R(245, y, 215, 22, "#fff", TEAL, 1)); b.append(T(352, y + 14, r, 7.2))
        b.append(T(235, y + 15, "vs", 7, fill=GREY, weight="bold"))
    save("hist_compare", 470, 172, "".join(b))


# 10 ----------------------------------------------------------------- colonial India timeline
def colonial():
    timeline("colonial", [
        ("1600", ["East India", "Company founded"]),
        ("1757", ["Battle of", "Plassey"]),
        ("1764-65", ["Buxar; Company", "gets the Diwani"]),
        ("1857", ["Great Revolt"]),
        ("1858", ["Crown rule", "begins"]),
        ("1885", ["Indian National", "Congress formed"]),
        ("1905", ["Partition of", "Bengal"]),
        ("1919", ["Rowlatt Act;", "Jallianwala Bagh"]),
        ("1947", ["Independence", "(15 August)"]),
    ], 470, 190, "From trade to colony to nation")


# 11 ----------------------------------------------------------------- government structure
def govt():
    b = []
    b.append(box(165, 6, 140, 30, "DRUK GYALPO", ("Head of State, symbol of unity",), RED, "#fbe9e8", 8.6, 7))
    for x, t, l, col in [(10, "LEGISLATURE", ("Parliament:", "National Council +", "National Assembly"), NAVY), (180, "EXECUTIVE", ("Lhengye Zhungtshog", "(Cabinet) led by the", "Prime Minister"), TEAL), (350, "JUDICIARY", ("Supreme Court,", "High Court, Dzongkhag", "& Dungkhag courts"), GOLD)]:
        b.append(L(235, 36, x + 55, 58, "#777", 1.3, arrow=True))
        b.append(box(x, 58, 110, 52, t, l, col, "#fff", 8.4, 7.2))
    b.append(T(235, 128, "Separation of powers (Constitution, 2008). Local: Dzongkhag Tshogdu (DT), Gewog Tshogde (GT), Thromde.", 6.8, fill="#555"))
    save("govt", 470, 136, "".join(b))


# 12 ----------------------------------------------------------------- GNH
def gnh():
    b = []
    b.append(C(235, 70, 34, "#fff3d6", GOLD, 2)); b.append(TL(235, 66, ["GROSS", "NATIONAL", "HAPPINESS"], 8, fill=GOLD, weight="bold"))
    pill = [("Sustainable & equitable\nsocio-economic development", 20, 14, NAVY), ("Conservation of the\nenvironment", 330, 14, GREEN), ("Preservation & promotion\nof culture", 20, 102, PURPLE), ("Good\ngovernance", 330, 102, TEAL)]
    for t, x, y, col in pill:
        b.append(R(x, y, 120, 36, "#fff", col, 1.6)); b.append(TL(x + 60, y + 15, t.split("\n"), 7.6, fill=col, weight="bold"))
    for x, y in [(140, 32), (330, 32), (140, 120), (330, 120)]:
        b.append(L(x, y, 235 + (-34 if x < 235 else 34) * 0.6, 70 + (-14 if y < 70 else 14), "#999", 1.2))
    b.append(T(235, 150, "4 pillars  |  9 domains: well-being, health, education, time use, culture, governance, community vitality, ecology, living standards", 6.4, fill="#555"))
    save("gnh", 470, 158, "".join(b))


# 13 ----------------------------------------------------------------- exploration
def explore():
    timeline("explore", [
        ("1453", ["Ottomans take", "Constantinople;", "trade routes blocked"]),
        ("1488", ["Dias rounds", "Cape of Good", "Hope (Portugal)"]),
        ("1492", ["Columbus reaches", "the Americas", "(Spain)"]),
        ("1498", ["Vasco da Gama", "reaches Calicut", "(India)"]),
        ("1519-22", ["Magellan's fleet", "sails round", "the world"]),
    ], 470, 170, "Age of Exploration")


# 14 ----------------------------------------------------------------- 4th King timeline
def fourth():
    timeline("fourth_king", [
        ("1955", ["Born 11 Nov,", "Dechencholing"]),
        ("1971", ["Chairman, Planning", "Commission"]),
        ("1972", ["Ascends throne", "(24 July, age 16)"]),
        ("1974", ["Coronation,", "2 June"]),
        ("1981/91", ["DYT / GYT:", "decentralisation"]),
        ("2003", ["Operation", "All Clear"]),
        ("2005-06", ["Constitution draft;", "abdicates 9 Dec 2006"]),
    ], 470, 185, "The Fourth Druk Gyalpo: milestones")


def flow(name, boxes, per=3, w=470, bw=140, bh=44, gx=25, gy=22, col=NAVY):
    rows = (len(boxes) + per - 1) // per
    H = rows * bh + (rows - 1) * gy + 12
    x0 = (w - (per * bw + (per - 1) * gx)) / 2
    b = []
    for i, (t, lines) in enumerate(boxes):
        r, c = divmod(i, per)
        x, y = x0 + c * (bw + gx), 6 + r * (bh + gy)
        cc = [NAVY, TEAL, GOLD][i % 3]
        b.append(R(x, y, bw, bh, "#fff", cc, 1.6))
        b.append(T(x + bw / 2, y + 12, t, 8, fill=cc, weight="bold"))
        b.append(TL(x + bw / 2, y + 23, lines, 6.9, lh=8.4))
        if i < len(boxes) - 1:
            if c < per - 1:
                b.append(L(x + bw, y + bh / 2, x + bw + gx - 1, y + bh / 2, "#555", 1.6, arrow=True))
            else:
                nx = x0 + bw / 2
                b.append(P(f"M{x + bw / 2},{y + bh} L{x + bw / 2},{y + bh + gy / 2} L{nx},{y + bh + gy / 2} L{nx},{y + bh + gy - 1}", "none", "#555", 1.6).replace("/>", ' marker-end="url(#a)"/>'))
    save(name, w, H, "".join(b))


def duar():
    flow("duar_war", [
        ("1. Causes", ["border raids/disputes in the", "Duars; British want the", "fertile Duars (tea, revenue)"]),
        ("2. Eden mission 1864", ["sent to Punakha; insulted;", "forced to sign a treaty", "giving up the Duars"]),
        ("3. War declared", ["Britain annexes Ambari", "Falakata; declares war", "12 Nov 1864"]),
        ("4. Fighting", ["Dewangiri retaken by", "Bhutan (Jigme Namgyel)", "but British prevail"]),
        ("5. Sinchula 11 Nov 1865", ["Duars + Dewangiri ceded;", "annual payment;", "peace and friendship"]),
        ("6. Result", ["Bhutan loses ~1/5 land;", "closer ties with British;", "road to 1907 monarchy"]),
    ], per=3)


def vedic_budd():
    flow("vedic_to_buddha", [
        ("Vedic society", ["costly yajnas, animal", "sacrifice, Brahmin power,", "rigid caste"]),
        ("6th c. BCE change", ["new towns and traders;", "people question ritual", "and inequality"]),
        ("New paths", ["Buddhism (Buddha),", "Jainism (Mahavira):", "non-violence, equality"]),
    ], per=3)


if __name__ == "__main__":
    for f in (duar, vedic_budd, indus, buddha, eightfold, triangle, choesid, bb, monarchy, envflow, hist_compare, colonial, govt, gnh, explore, fourth):
        f()
    print(sorted(p.name for p in OUT.glob("*.svg")))
