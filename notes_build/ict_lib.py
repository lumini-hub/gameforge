#!/usr/bin/env python3
"""Shared SVG helpers for the ICT note diagrams -> figs_i/*.svg (hand-built SVG)."""
import math, pathlib, re, textwrap

OUT = pathlib.Path(__file__).parent / "figs_i"
OUT.mkdir(exist_ok=True)
NAVY, TEAL, GOLD, RED, GREY, GREEN, PURPLE = "#0e3a66", "#0f7b6c", "#b36200", "#b3211b", "#666", "#2a7a3a", "#5b3a8a"
FONT = 'font-family="DejaVu Sans, Liberation Sans, Arial, sans-serif"'
DEFS = ('<defs><marker id="a" markerUnits="userSpaceOnUse" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="context-stroke"/></marker></defs>')


def _grow(m):
    v = float(m.group(1))
    return 'font-size="%s"' % round(v * 1.16 if v < 8 else v, 2)


def save(name, w, h, body):
    body = re.sub(r'font-size="([0-9.]+)"', _grow, body)
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




def Q(x, y, w, h, fill="#fff", stroke="#333", sw=1.3):
    return R(x, y, w, h, fill, stroke, sw, 0)


def E(cx, cy, rx, ry, fill="#fff", stroke="#333", sw=1.3, rot=0):
    t = f' transform="rotate({rot} {cx} {cy})"' if rot else ""
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{t}/>'


def lab(x, y, tx, ty, text, anchor="middle", size=7.4, col="#111", weight="normal"):
    """text at (x,y) with a thin leader line to the point (tx,ty) on the drawing.
    anchor=middle: line leaves above/below the text; anchor=start/end: line leaves the side of the text."""
    if anchor == "middle":
        sx, sy = x, (y + 2 if y < ty else y - size)
    else:
        sx, sy = (x - 2 if anchor == "start" else x + 2), y - size / 2 + 0.5
    return L(sx, sy, tx, ty, "#666", 0.8) + T(x, y, text, size, anchor, col, weight)


def panel(x, y, w, h, title, col=NAVY):
    return R(x, y, w, h, "#fbfcfe", "#b9c7d8", 1, 3) + T(x + w / 2, y + 11, title, 8.4, fill=col, weight="bold")
