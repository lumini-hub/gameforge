#!/usr/bin/env python3
"""Builds the Class X Biology Model Question Papers (Set 1 and Set 2) with answer keys at the back."""
import random, subprocess, pathlib
import model_set1, model_set2

ROOT = pathlib.Path(__file__).parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
ROM = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx", "xxi", "xxii", "xxiii", "xxiv", "xxv"]
FIXED = {1: {15, 17, 21, 22}, 2: {2, 4, 11, 14, 19, 22, 23}}     # 1-based MCQ numbers whose option order must not change
SETS = {1: model_set1, 2: model_set2}


def balanced(mod, n, seed):
    """Reorder the options of each non-fixed MCQ so the correct letters are spread evenly over A-D."""
    rnd = random.Random(seed)
    fixed = FIXED[n]
    have = [m[2] for i, m in enumerate(mod.MCQS, 1) if i in fixed]
    free = [i for i in range(1, 26) if i not in fixed]
    pool = []
    for letter in "ABCD":
        pool += [letter] * 7
    for h in have:
        pool.remove(h)
    rnd.shuffle(pool)
    targets = dict(zip(free, pool))
    out = []
    for i, (q, opts, ans, why, fig) in enumerate(mod.MCQS, 1):
        if i in fixed:
            out.append((q, opts, ans, why, fig))
            continue
        opts = list(opts)
        ci = "ABCD".index(ans)
        ti = "ABCD".index(targets[i])
        opts[ci], opts[ti] = opts[ti], opts[ci]
        out.append((q, opts, "ABCD"[ti], why, fig))
    return out


CSS = """
@page { size: A4; margin: 17mm 17mm 24mm 17mm; }
@page set1 { @bottom-left { content: "BCSE/22-3/MODEL-1\\A Practice paper"; white-space: pre; font: italic bold 9pt "Liberation Serif", serif; border-top: 3px double #000; padding-top: 1.2mm; vertical-align: top; width: 40%; }
  @bottom-center { content: " "; border-top: 3px double #000; width: 20%; }
  @bottom-right { content: "Page " counter(page); font: bold 9pt "Liberation Serif", serif; border-top: 3px double #000; padding-top: 1.2mm; text-align: right; vertical-align: top; width: 40%; } }
@page set2 { @bottom-left { content: "BCSE/22-3/MODEL-2\\A Practice paper"; white-space: pre; font: italic bold 9pt "Liberation Serif", serif; border-top: 3px double #000; padding-top: 1.2mm; vertical-align: top; width: 40%; }
  @bottom-center { content: " "; border-top: 3px double #000; width: 20%; }
  @bottom-right { content: "Page " counter(page); font: bold 9pt "Liberation Serif", serif; border-top: 3px double #000; padding-top: 1.2mm; text-align: right; vertical-align: top; width: 40%; } }
@page keys { @bottom-left { content: "Biology model papers\\A Answer keys"; white-space: pre; font: italic bold 9pt "Liberation Serif", serif; border-top: 3px double #000; padding-top: 1.2mm; vertical-align: top; width: 40%; }
  @bottom-center { content: " "; border-top: 3px double #000; width: 20%; }
  @bottom-right { content: "Page " counter(page); font: bold 9pt "Liberation Serif", serif; border-top: 3px double #000; padding-top: 1.2mm; text-align: right; vertical-align: top; width: 40%; } }
.set1 { page: set1; } .set2 { page: set2; } .keys { page: keys; }
html { font-family: "Liberation Serif", "Times New Roman", serif; font-size: 11pt; line-height: 1.3; color: #000; }
body { margin: 0; }
.cover { text-align: center; border: 2px solid #000; padding: 7mm 5mm; margin: 0 0 6mm; }
.cover .t1 { font-size: 11pt; letter-spacing: 1px; } .cover .t2 { font-size: 20pt; font-weight: bold; margin: 2mm 0; } .cover .t3 { font-size: 13pt; }
.cover table { width: 100%; margin-top: 4mm; font-size: 11pt; } .cover td { text-align: left; padding: 0 3mm; } .cover td+td { text-align: right; }
.inst { border: 1px solid #000; padding: 3mm 4mm; margin: 0 0 6mm; font-size: 10.5pt; } .inst b { font-size: 11pt; }
h2.sec { text-align: center; font-size: 12pt; margin: 0 0 1mm; }
.sub { text-align: center; margin: 0 0 5mm; }
.q { font-weight: bold; margin: 4mm 0 2mm; display: flex; justify-content: space-between; }
.part { display: flex; margin: 1.5mm 0; }
.part .lab { width: 14mm; flex: none; }
.part .txt { flex: 1; text-align: justify; }
.part .mk { width: 12mm; flex: none; text-align: right; font-weight: bold; }
.dir { font-weight: bold; text-align: justify; }
.blk { break-inside: avoid; margin-bottom: 1mm; }
.opts { margin-left: 14mm; margin-bottom: 3mm; }
.opt { display: flex; gap: 6mm; } .opt span:first-child { width: 6mm; }
.fig { margin: 1mm 0 2mm; }
div.abox { display: flex; border: 1px solid #000; margin: 1.5mm 0 2.5mm; } div.abox .ans { flex: 1; } div.abox .mkc { width: 20mm; border-left: 1px solid #000; }
table.box { width: 100%; table-layout: fixed; border-collapse: collapse; margin: 1.5mm 0 2.5mm; }
table.box td { border: 1px solid #000; padding: 0; }
table.tab { width: 100%; border-collapse: collapse; margin: 1.5mm 0 3mm; }
table.tab td, table.tab th { border: 1px solid #000; padding: 1.6mm 2mm; vertical-align: top; text-align: left; font-weight: normal; }
table.tab th { font-weight: bold; }
table.tab td.m { width: 20mm; } table.tab td.a { width: 22mm; }
.rough { break-before: page; text-align: center; font-weight: bold; }
.newpage { break-before: page; }
.key td, .key th { font-size: 9.8pt; } .key h3 { font-size: 12pt; margin: 4mm 0 1.5mm; } .key h4 { font-size: 11pt; margin: 3mm 0 1mm; break-after: avoid; }
.key table.tab td { vertical-align: top; } .key tr { break-inside: avoid; }
"""


def box(h):
    return f'<div class="abox" style="height:{h}mm"><div class="ans"></div><div class="mkc"></div></div>'


def part(label, text, marks, fig="", h=None):
    mk = f"[{marks}]" if marks else ""
    out = f'<div class="part"><div class="lab">{label}</div><div class="txt">{text}</div><div class="mk">{mk}</div></div>'
    if fig:
        out += f'<div class="fig" style="margin-left:14mm">{fig}</div>'
    if h:
        out += box(h)
    return f'<div class="blk">{out}</div>'


def mcq(label, text, opts, fig=""):
    o = "".join(f'<div class="opt"><span>{l}</span><span>{t}</span></div>' for l, t in zip("ABCD", opts))
    f = f'<div class="fig" style="margin-left:14mm">{fig}</div>' if fig else ""
    return f'<div class="blk mcq"><div class="part"><div class="lab">{label}</div><div class="txt">{text}</div></div>{f}<div class="opts">{o}</div></div>'


def paper(n, mod, mcqs):
    h = [f'<div class="set{n}">']
    h.append(f'<div class="cover"><div class="t1">CLASS X &middot; PRACTICE EXAMINATION</div><div class="t2">BIOLOGY &mdash; MODEL QUESTION PAPER {n}</div><div class="t3">Final I pattern &middot; Section A (40) + Section B (60)</div>'
             f'<table><tr><td>Code: {mod.CODE}</td><td>Time: 2 hours 30 minutes</td></tr><tr><td>Total: 100 marks</td><td>Pages: see footer</td></tr></table></div>')
    h.append('<div class="inst"><b>Instructions.</b> (1) Section A is compulsory: Question 1 carries 40 marks. (2) In Section B attempt <b>any SIX</b> questions (10 marks each). (3) Write the answers in the spaces given; use a pencil for diagrams and graphs. (4) Circle only <b>ONE</b> letter in the multiple-choice questions. (5) The figures are drawn for practice and are not to scale.</div>')
    h.append('<h2 class="sec">SECTION A [40 MARKS]</h2><div class="sub">ANSWER <b>ALL</b> QUESTIONS</div><div class="q"><span>Question 1</span><span>[25]</span></div>')
    h.append('<div class="part"><div class="lab">a)</div><div class="txt dir">Directions: For each question there are four alternatives A, B, C and D. Choose the correct alternative and circle it neatly. If more than one letter is circled, NO score will be awarded.</div><div class="mk">[25]</div></div>')
    for r, (t, o, a, why, fg) in zip(ROM, mcqs):
        h.append(mcq(r + ".", t, o, fg))
    h.append('<div class="blk"><div class="part"><div class="lab">b)</div><div class="txt">Fill in the blanks with suitable word/s.</div><div class="mk">[5]</div></div><table class="tab">' + "".join(f'<tr><td style="width:12mm">{ROM[i]}.</td><td>{t}</td><td class="m"></td></tr>' for i, (t, a) in enumerate(mod.FILL)) + "</table></div>")
    h.append('<div class="blk"><div class="part"><div class="lab">c)</div><div class="txt">Write <b>TRUE</b> or <b>FALSE</b> for each statement in the ‘Answer’ column.</div><div class="mk">[5]</div></div><table class="tab">' + "".join(f'<tr><td style="width:12mm">{ROM[i]}.</td><td>{t}</td><td class="a"></td><td class="m"></td></tr>' for i, (t, a) in enumerate(mod.TF)) + "</table></div>")
    rows = []
    for i in range(7):
        a = f'<td class="a" style="height:10mm">{ROM[i] + "." if i < 5 else ""}</td><td>{ROM[i] + ". " + mod.MATCH_A[i] if i < 5 else ""}</td>'
        rows.append(f'<tr>{a}<td>{"abcdefg"[i]}. {mod.MATCH_B[i]}</td><td class="m"></td></tr>')
    h.append('<div class="blk"><div class="part"><div class="lab">d)</div><div class="txt">Match each item in <b>Column A</b> with the most appropriate item in <b>Column B</b>. Write the correct letter in the ‘Answer’ column.</div><div class="mk">[5]</div></div><table class="tab"><tr><th class="a" style="text-align:center">Answer</th><th style="text-align:center">Column A</th><th style="text-align:center">Column B</th><th class="m"></th></tr>' + "".join(rows) + "</table></div>")
    h.append('<div class="newpage"></div><h2 class="sec">SECTION B [60 MARKS]</h2><div class="sub">ATTEMPT <b>ANY SIX</b> QUESTIONS</div>')
    for q, parts in mod.QB.items():
        h.append(f'<div class="q" style="justify-content:flex-start;break-after:avoid"><span>Question {q}</span></div>')
        for (lab, text, marks, fig, bh, ans) in parts:
            h.append(part(lab, text, marks, fig, bh))
    h.append('<div class="rough">Rough Work</div></div>')
    return "".join(h)


def keys(n, mod, mcqs):
    h = [f'<div class="key"><h2 class="sec">ANSWER KEY &mdash; MODEL PAPER {n}</h2><div class="sub">{mod.CODE} &middot; for self-checking</div>']
    h.append('<h3>Section A &mdash; Q1(a) Multiple choice (1 mark each)</h3><table class="tab"><tr><th style="width:12mm">No.</th><th style="width:14mm">Answer</th><th>Reason</th></tr>')
    for r, (t, o, a, why, fg) in zip(ROM, mcqs):
        h.append(f"<tr><td>{r}.</td><td><b>{a}</b></td><td>{why}</td></tr>")
    h.append("</table>")
    h.append('<h3>Q1(b) Fill in the blanks &middot; Q1(c) True/False &middot; Q1(d) Matching (1 mark each)</h3><table class="tab"><tr><th style="width:12mm"></th><th>(b)</th><th>(c)</th><th>(d)</th></tr>')
    for i in range(5):
        h.append(f"<tr><td>{ROM[i]}.</td><td><b>{mod.FILL[i][1]}</b></td><td><b>{mod.TF[i][1]}</b></td><td><b>{mod.MATCH_ANS[i]}</b> &mdash; {mod.MATCH_B['abcdefg'.index(mod.MATCH_ANS[i])]}</td></tr>")
    h.append("</table><h3>Section B (10 marks per question; any six)</h3>")
    for q, parts in mod.QB.items():
        h.append(f"<h4>Question {q}</h4><table class='tab'><tr><th style='width:11mm'>Part</th><th style='width:11mm'>Marks</th><th>Model answer and marking points</th></tr>")
        for (lab, text, marks, fig, bh, ans) in parts:
            lead = text.split("<br>")[-1] if "<br>" in text else text
            h.append(f"<tr><td>{lab}</td><td>{marks}</td><td>{ans}</td></tr>")
        h.append("</table>")
    h.append("</div>")
    return "".join(h)


def build():
    m1, m2 = balanced(model_set1, 1, 11), balanced(model_set2, 2, 22)
    body = paper(1, model_set1, m1) + '<div class="newpage"></div>' + paper(2, model_set2, m2)
    body += '<div class="keys"><div class="newpage"></div><div class="cover"><div class="t2">ANSWER KEYS</div><div class="t3">Model Paper 1 and Model Paper 2</div></div>' + keys(1, model_set1, m1) + '<div class="newpage"></div>' + keys(2, model_set2, m2)
    body += '<div class="key"><p><b>Marking guide:</b> in Section B each bracketed point is worth 1 mark unless shown; accept any correct answer in different words. For graphs award marks for axes with units, correct plotting and the line/curve. For diagrams award marks for the drawing and for correct labels.</p></div></div>'
    return "<!doctype html><html><head><meta charset=utf-8><style>" + CSS + "</style></head><body>" + body + "</body></html>"


if __name__ == "__main__":
    f = ROOT / "BCSE_Class_X_Biology_Model_Papers.html"
    f.write_text(build(), encoding="utf-8")
    pdf = ROOT / "BCSE_Class_X_Biology_Model_Papers.pdf"
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", f"file://{f}"], check=True, stderr=subprocess.DEVNULL)
    print("wrote", pdf)
