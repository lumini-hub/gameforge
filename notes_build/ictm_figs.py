"""Black-and-white flowcharts for the ICT model papers (inline SVG strings)."""
FONT = 'font-family="Liberation Sans, Arial, sans-serif" font-size="11"'
DEF = '<defs><marker id="ar" markerUnits="userSpaceOnUse" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#000"/></marker></defs>'


def svg(w, h, body, width_mm):
    return f'<svg viewBox="0 0 {w} {h}" width="{width_mm}mm" xmlns="http://www.w3.org/2000/svg" {FONT}>{DEF}{body}</svg>'


def line(pts, arrow=True):
    d = "M" + " L".join(f"{x},{y}" for x, y in pts)
    m = ' marker-end="url(#ar)"' if arrow else ""
    return f'<path d="{d}" fill="none" stroke="#000" stroke-width="1.2"{m}/>'


def txt(x, y, s, anchor="middle", w="normal"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-weight="{w}">{s}</text>'


def term(cx, cy, s, w=70, h=24):
    return f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="12" fill="#fff" stroke="#000" stroke-width="1.3"/>' + txt(cx, cy + 4, s)


def proc(cx, cy, s, w=110, h=26):
    return f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" fill="#fff" stroke="#000" stroke-width="1.3"/>' + txt(cx, cy + 4, s)


def io(cx, cy, s, w=110, h=26):
    k = 10
    p = f"{cx-w/2+k},{cy-h/2} {cx+w/2+k},{cy-h/2} {cx+w/2-k},{cy+h/2} {cx-w/2-k},{cy+h/2}"
    return f'<polygon points="{p}" fill="#fff" stroke="#000" stroke-width="1.3"/>' + txt(cx, cy + 4, s)


def dec(cx, cy, s, w=110, h=50):
    p = f"{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}"
    return f'<polygon points="{p}" fill="#fff" stroke="#000" stroke-width="1.3"/>' + txt(cx, cy + 4, s)


def fig_sum_odd():
    """Set 1 Q6: sum of odd numbers up to 9 (output 25)."""
    b = term(130, 16, "START")
    b += line([(130, 28), (130, 46)])
    b += proc(130, 59, "sum = 0 ; i = 1", 120)
    b += line([(130, 72), (130, 94)])
    b += dec(130, 119, "i &lt;= 9 ?", 110, 50)
    b += line([(130, 144), (130, 166)]) + txt(138, 157, "Yes", "start")
    b += proc(130, 179, "sum = sum + i", 120)
    b += line([(130, 192), (130, 208)])
    b += proc(130, 221, "i = i + 2", 100)
    b += line([(80, 221), (30, 221), (30, 119), (75, 119)])
    b += line([(185, 119), (240, 119), (240, 262)]) + txt(205, 112, "No", "start")
    b += io(240, 275, "PRINT sum", 90)
    b += line([(240, 288), (240, 300)])
    b += term(240, 312, "STOP")
    return svg(300, 330, b, 70)


def fig_sign():
    """Set 2 Q6: positive / negative / zero."""
    b = term(130, 16, "START")
    b += line([(130, 28), (130, 42)])
    b += io(130, 56, "INPUT n", 90)
    b += line([(130, 69), (130, 85)])
    b += dec(130, 110, "n &gt; 0 ?", 100, 50)
    b += line([(180, 110), (215, 110)]) + txt(197, 103, "Yes")
    b += io(262, 110, "PRINT “Positive”", 96)
    b += line([(130, 135), (130, 165)]) + txt(140, 152, "No", "start")
    b += dec(130, 190, "n &lt; 0 ?", 100, 50)
    b += line([(180, 190), (215, 190)]) + txt(197, 183, "Yes")
    b += io(262, 190, "PRINT “Negative”", 96)
    b += line([(130, 215), (130, 245)]) + txt(140, 232, "No", "start")
    b += io(130, 258, "PRINT “Zero”", 96)
    b += line([(130, 271), (130, 300)])
    b += term(130, 312, "STOP")
    b += line([(322, 110), (350, 110), (350, 312), (165, 312)])
    b += line([(322, 190), (350, 190)], arrow=False)
    return svg(360, 330, b, 80)
