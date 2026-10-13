#!/usr/bin/env python3
"""Assemble parts/*.html into a PDF using headless Chromium.
usage: build.py <doc-key>    (keys: e1, e2)
Fragments may use {{fn:arg|arg|...}} placeholders, expanded by the generators below.
"""
import html, re, subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

NAVY, TEAL, GOLD, RED, GREY = "#1b3a6b", "#0f6b63", "#8a4b00", "#b3261e", "#555"


def esc(s):
    return html.escape(s, quote=False)


def lines(svg_x, y, text, size=11, anchor="middle", fill="#1d1d1d", lh=None, weight="normal"):
    """multi-line svg text; '/' separates lines"""
    lh = lh or size * 1.25
    parts = text.split("/")
    out = []
    for i, p in enumerate(parts):
        out.append(f'<text x="{svg_x}" y="{y + i * lh}" font-size="{size}" text-anchor="{anchor}" fill="{fill}" font-weight="{weight}">{esc(p.strip())}</text>')
    return "".join(out)


def fig(svg, cap):
    return f'<figure>{svg}<figcaption>{esc(cap)}</figcaption></figure>'


# ---------- generators ----------
def g_flow(args):
    """flow:caption|box|box|... horizontal chain, wraps at 4 per row"""
    cap, boxes = args[0], args[1:]
    per = 4 if len(boxes) > 4 else len(boxes)
    rows = (len(boxes) + per - 1) // per
    bw, bh, gx, gy = 150, 62, 28, 30
    W = per * bw + (per - 1) * gx + 20
    H = rows * bh + (rows - 1) * gy + 20
    out = [f'<svg viewBox="0 0 {W} {H}" width="{W}" xmlns="http://www.w3.org/2000/svg" font-family="Liberation Sans, Arial">',
           '<defs><marker id="ah" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>']
    for i, b in enumerate(boxes):
        r, c = divmod(i, per)
        x, y = 10 + c * (bw + gx), 10 + r * (bh + gy)
        colour = [NAVY, TEAL, GOLD][i % 3]
        out.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="7" fill="#fff" stroke="{colour}" stroke-width="2"/>')
        head, _, body = b.partition("::")
        if body:
            out.append(lines(x + bw / 2, y + 16, head, 10.5, fill=colour, weight="bold"))
            out.append(lines(x + bw / 2, y + 30, body, 9, lh=11))
        else:
            out.append(lines(x + bw / 2, y + bh / 2 - (len(b.split('/')) - 1) * 5.5 + 3, b, 10, lh=12))
        if i < len(boxes) - 1:
            if c < per - 1:
                out.append(f'<line x1="{x + bw}" y1="{y + bh / 2}" x2="{x + bw + gx - 2}" y2="{y + bh / 2}" stroke="#555" stroke-width="1.6" marker-end="url(#ah)"/>')
            else:  # wrap arrow to next row start
                nx, ny = 10 + bw / 2, y + bh + gy - 2
                out.append(f'<path d="M{x + bw / 2},{y + bh} L{x + bw / 2},{y + bh + gy / 2} L{nx},{y + bh + gy / 2} L{nx},{ny}" fill="none" stroke="#555" stroke-width="1.6" marker-end="url(#ah)"/>')
    out.append("</svg>")
    return fig("".join(out), cap)


def g_plot(args):
    """plot:caption|exposition|rising|climax|falling|resolution  ('/' = line break)"""
    cap = args[0]
    bodies = args[1:6]
    titles = ["1 EXPOSITION", "2 RISING ACTION", "3 CLIMAX", "4 FALLING ACTION", "5 RESOLUTION"]
    cols = [TEAL, GOLD, RED, GOLD, TEAL]
    W = 640
    maxl = max(len(x.split("/")) for x in bodies)
    ch = 26 + maxl * 10.5
    H = 140 + ch + 8
    pts = [(62, 112), (170, 84), (320, 26), (470, 84), (578, 112)]
    out = [f'<svg viewBox="0 0 {W} {H}" width="{W}" xmlns="http://www.w3.org/2000/svg" font-family="Liberation Sans, Arial">',
           '<line x1="20" y1="122" x2="620" y2="122" stroke="#bbb"/>',
           f'<polyline points="{" ".join(f"{x},{y}" for x, y in pts)}" fill="none" stroke="{NAVY}" stroke-width="3.5" stroke-linejoin="round"/>']
    cw, gap = 124, 4
    x0 = (W - (5 * cw + 4 * gap)) / 2
    for i, (x, y) in enumerate(pts):
        out.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{cols[i]}"/><text x="{x}" y="{y + 4}" font-size="11" text-anchor="middle" fill="#fff" font-weight="bold">{i + 1}</text>')
        cx = x0 + i * (cw + gap)
        out.append(f'<rect x="{cx}" y="140" width="{cw}" height="{ch}" rx="6" fill="#fff" stroke="{cols[i]}" stroke-width="1.8"/>')
        out.append(f'<rect x="{cx}" y="140" width="{cw}" height="17" rx="6" fill="{cols[i]}"/>')
        out.append(lines(cx + cw / 2, 152.5, titles[i], 8.8, fill="#fff", weight="bold"))
        out.append(lines(cx + cw / 2, 170, bodies[i], 8, lh=10.5))
    out.append("</svg>")
    return fig("".join(out), cap)


def g_compare(args):
    """compare:caption|Left title|Right title|a;b;c|d;e;f"""
    cap, lt, rt, l, r = args[:5]
    arrow = args[5] if len(args) > 5 else "&#8596;"
    L, R = l.split(";"), r.split(";")
    n = max(len(L), len(R))
    W, H = 640, 60 + n * 40
    out = [f'<svg viewBox="0 0 {W} {H}" width="{W}" xmlns="http://www.w3.org/2000/svg" font-family="Liberation Sans, Arial">']
    out.append(f'<rect x="10" y="8" width="290" height="30" rx="6" fill="{NAVY}"/>{lines(155, 28, lt, 12, fill="#fff", weight="bold")}')
    out.append(f'<rect x="340" y="8" width="290" height="30" rx="6" fill="{TEAL}"/>{lines(485, 28, rt, 12, fill="#fff", weight="bold")}')
    for i in range(n):
        y = 50 + i * 40
        if i < len(L):
            out.append(f'<rect x="10" y="{y}" width="290" height="32" rx="5" fill="#eef3fb" stroke="{NAVY}"/>{lines(155, y + 14, L[i], 9.2, lh=11)}')
        if i < len(R):
            out.append(f'<rect x="340" y="{y}" width="290" height="32" rx="5" fill="#e9f6f4" stroke="{TEAL}"/>{lines(485, y + 14, R[i], 9.2, lh=11)}')
        out.append(f'<text x="320" y="{y + 20}" font-size="14" text-anchor="middle" fill="#555">{arrow}</text>')
    out.append("</svg>")
    return fig("".join(out), cap)


def g_timeline(args):
    """timeline:caption|label@text|label@text...  ('/' = line break in text)"""
    cap, items = args[0], args[1:]
    n = len(items)
    W = max(640, n * 104 + 30)
    H = 182
    pad = 56
    step = (W - 2 * pad) / max(n - 1, 1)
    out = [f'<svg viewBox="0 0 {W} {H}" width="{W}" xmlns="http://www.w3.org/2000/svg" font-family="Liberation Sans, Arial">',
           f'<line x1="20" y1="90" x2="{W - 20}" y2="90" stroke="{NAVY}" stroke-width="3"/>']
    for i, it in enumerate(items):
        lab, _, txt = it.partition("@")
        x = pad + i * step
        up = i % 2 == 0
        col = TEAL if up else GOLD
        out.append(f'<circle cx="{x}" cy="90" r="6.5" fill="{col}"/>')
        out.append(f'<line x1="{x}" y1="{83 if up else 97}" x2="{x}" y2="{72 if up else 108}" stroke="#aaa"/>')
        if up:
            out.append(lines(x, 14, lab, 9.5, fill=NAVY, weight="bold"))
            out.append(lines(x, 27, txt, 8.2, lh=9.6))
        else:
            out.append(lines(x, 122, lab, 9.5, fill=NAVY, weight="bold"))
            out.append(lines(x, 135, txt, 8.2, lh=9.6))
    out.append("</svg>")
    return fig("".join(out), cap)


CROSS = {
    "2023": dict(cells=[("W", 0, 3), ("O", 1, 3), ("R", 2, 3), ("L", 3, 3), ("D", 4, 3), ("V", 1, 4), ("E", 1, 5), ("R", 1, 6),
                        ("N", 0, 5), ("W", 2, 5), ("S", 3, 5), ("S", 4, 0), ("O", 4, 1), ("L", 4, 2), ("W", 5, 1), ("L", 6, 1)],
                 labels={(0, 3): 1, (0, 5): 2, (4, 1): 3, (1, 3): 4, (4, 0): 5},
                 cap="2023 Q8 crossword solved: 1 WORLD (down)  2 NEWS (down)  3 OWL (down)  4 OVER (across)  5 SOLD (across)"),
    "2025": dict(cells=[(ch, 0 + i, 3) for i, ch in enumerate("CONJUNCTION")] + [(ch, 1, i) for i, ch in enumerate("SYNONYM") if i != 3]
                       + [(ch, 3 + i, 7) for i, ch in enumerate("FURIOUS")] + [(ch, 5, 3 + i) for i, ch in enumerate("NEVER") if i not in (0, 4)]
                       + [(ch, 7, 1 + i) for i, ch in enumerate("INTERROGATIVE") if (1 + i) not in (3, 7)],
                 labels={(0, 3): 1, (1, 0): 2, (3, 7): 3, (5, 3): 4, (7, 1): 5},
                 cap="2025 Q8 crossword solved: 1 CONJUNCTION (down)  2 SYNONYM (across)  3 FURIOUS (down)  4 NEVER (across)  5 INTERROGATIVE (across)"),
}


def g_cross(args):
    d = CROSS[args[0]]
    cells = d["cells"]
    if args[0] == "2023":
        cells = [(c[0], c[1], c[2]) for c in cells]
    cs = 26
    rows = max(c[1] for c in cells) + 1
    cols = max(c[2] for c in cells) + 1
    W, H = cols * cs + 20, rows * cs + 20
    out = [f'<svg viewBox="0 0 {W} {H}" width="{min(W, 420)}" xmlns="http://www.w3.org/2000/svg" font-family="Liberation Sans, Arial">']
    for ch, r, c in cells:
        x, y = 10 + c * cs, 10 + r * cs
        out.append(f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="#fff" stroke="#222" stroke-width="1.4"/>')
        out.append(f'<text x="{x + cs / 2}" y="{y + cs - 7}" text-anchor="middle" font-size="14" font-weight="bold" fill="#0b5a2a">{ch}</text>')
    for (r, c), n in d["labels"].items():
        out.append(f'<text x="{10 + c * cs + 2}" y="{10 + r * cs + 8}" font-size="7.5" fill="#b3261e" font-weight="bold">{n}</text>')
    out.append("</svg>")
    return fig("".join(out), d["cap"])


def g_box(args):
    """gbox:caption|title@item;item;item|title@item;item  -> columns of coloured cards (mind-map style)"""
    cap, groups = args[0], args[1:]
    n = len(groups)
    cw = 200 if n <= 3 else 150
    W = n * (cw + 12) + 8
    maxi = max(len(g.partition("@")[2].split(";")) for g in groups)
    H = 44 + maxi * 17 + 12
    out = [f'<svg viewBox="0 0 {W} {H}" width="{min(W, 660)}" xmlns="http://www.w3.org/2000/svg" font-family="Liberation Sans, Arial">']
    for i, g in enumerate(groups):
        t, _, items = g.partition("@")
        x = 6 + i * (cw + 12)
        colour = [NAVY, TEAL, GOLD, RED][i % 4]
        out.append(f'<rect x="{x}" y="4" width="{cw}" height="{H - 8}" rx="8" fill="#fff" stroke="{colour}" stroke-width="2"/>')
        out.append(f'<rect x="{x}" y="4" width="{cw}" height="26" rx="8" fill="{colour}"/>')
        out.append(lines(x + cw / 2, 21, t, 10.5, fill="#fff", weight="bold"))
        for j, it in enumerate(items.split(";")):
            out.append(lines(x + 8, 46 + j * 17, "• " + it.strip().replace("/", " - "), 8.8, anchor="start"))
    out.append("</svg>")
    return fig("".join(out), cap)


GENS = {"flow": g_flow, "plot": g_plot, "compare": g_compare, "timeline": g_timeline, "cross": g_cross, "gbox": g_box}


def expand(text):
    def rep(m):
        name, _, rest = m.group(1).partition(":")
        if name not in GENS:
            return m.group(0)
        return GENS[name](rest.split("|"))
    return re.sub(r"\{\{(.+?)\}\}", rep, text, flags=re.S)


def count_essays(text, key):
    def rep(m):
        attrs, body = m.group(1), m.group(2)
        plain = re.sub(r"<h4>.*?</h4>", "", body, flags=re.S)
        plain = re.sub(r"<[^>]+>", " ", plain)
        n = len(re.findall(r"[A-Za-z0-9’'\-]+", html.unescape(plain)))
        tgt = re.search(r'data-target="(\d+)-(\d+)"', attrs)
        flag = ""
        if tgt and not (int(tgt.group(1)) <= n <= int(tgt.group(2))):
            flag = f"  <-- OUT OF RANGE {tgt.group(1)}-{tgt.group(2)}"
        print(f"[{key}] {re.search(r'data-id=\"([^\"]+)\"', attrs).group(1) if 'data-id' in attrs else '?'}: {n} words{flag}")
        return f'<div class="essay"{attrs}>{body}</div><div class="wc">≈ {n} words</div>'
    return re.sub(r'<div class="essay"([^>]*)>(.*?)</div><!--WC-->', rep, text, flags=re.S)


def chapter_titles(body):
    out = []
    for m in re.finditer(r'<div class="chapter">\s*<h1>(.*?)(?:<small>(.*?)</small>)?</h1>', body, flags=re.S):
        t = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
        sub = html.unescape(re.sub(r"<[^>]+>", "", m.group(2) or "")).strip()
        if t != "Contents":
            out.append((t, sub))
    return out


def toc_html(titles, pages):
    rows = "".join(f'<tr><td>{esc(t)}</td><td class="small">{esc(s)}</td><td class="c"><b>{pages.get(t, "-")}</b></td></tr>' for t, s in titles)
    return f'<table><tr><th>Chapter</th><th>What it covers / where it was asked</th><th class="c" style="width:9%">Page</th></tr>{rows}</table>'


def render(key, titles_text, body, toc):
    css = (ROOT / "style.css").read_text()
    doc = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{titles_text}</title><style>{css}</style></head><body><div class="doctitle">{titles_text}</div>{body.replace("{{TOC}}", toc)}</body></html>'
    out_html = ROOT / f"{key}.html"
    out_html.write_text(doc, encoding="utf-8")
    pdf = ROOT / f"{titles_text.replace(' ', '_').replace('&', 'and')}.pdf"
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", f"file://{out_html}"], check=True, stderr=subprocess.DEVNULL)
    return pdf


def find_pages(pdf, titles):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout).group(1))
    texts = [re.sub(r"\s+", " ", subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), str(pdf), "-"], capture_output=True, text=True).stdout) for i in range(1, n + 1)]
    pages, start = {}, 3
    for t, _ in titles:
        key = re.sub(r"\s+", " ", t)[:28]
        for i in range(start - 1, n):
            if key in texts[i] and re.search(re.escape(key), texts[i]):
                pages[t] = i + 1
                start = i + 1
                break
    return pages


def main():
    key = sys.argv[1]
    titles = {"e1": "BCSE Class X English I - Writing & Grammar Notes", "e2": "BCSE Class X English II - Literature Notes"}
    parts = sorted((ROOT / "parts").glob(f"{key}_*.html"))
    body = "\n".join(p.read_text(encoding="utf-8") for p in parts)
    body = count_essays(expand(body), key)
    ch = chapter_titles(body)
    pdf = render(key, titles[key], body, toc_html(ch, {}))
    pages = find_pages(pdf, ch)
    pdf = render(key, titles[key], body, toc_html(ch, pages))
    pages2 = find_pages(pdf, ch)
    if pages2 != pages:
        print("TOC page numbers shifted; re-rendering")
        pdf = render(key, titles[key], body, toc_html(ch, pages2))
    print("wrote", pdf)


if __name__ == "__main__":
    main()
