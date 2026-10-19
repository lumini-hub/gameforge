#!/usr/bin/env python3
"""Builds the Class X ICT Model Question Papers (Set 1 and Set 2) with answer keys at the back."""
import random, subprocess, pathlib
import biology_model as B
import ictm_set1, ictm_set2

ROOT = pathlib.Path(__file__).parent
ROM = B.ROM
SETS = {1: ictm_set1, 2: ictm_set2}

CSS = B.CSS.replace("BCSE/22-3/MODEL", "BCSE/ICT/MODEL").replace("Biology model papers", "ICT model papers") + """
pre.code { font-family: "DejaVu Sans Mono", "Liberation Mono", monospace; font-size: 9pt; line-height: 1.28; background: #f4f4f4; border: 1px solid #888; padding: 1.5mm 3mm; margin: 1.5mm 0 1.5mm 0; white-space: pre-wrap; break-inside: avoid; text-align: left; }
pre.code.out { background: #fff; border-style: dashed; }
code { font-family: "DejaVu Sans Mono", "Liberation Mono", monospace; font-size: 9.2pt; }
table.xl { border-collapse: collapse; margin: 1.5mm 0; font-size: 9.5pt; }
table.xl th, table.xl td { border: 1px solid #555; padding: 0.6mm 2.5mm; min-width: 9mm; text-align: left; }
table.xl th { background: #e4e4e4; font-weight: bold; text-align: center; }
table.xl td.hd { font-weight: bold; background: #f1f1f1; }
.fig svg { display: block; }
.key h3.sb { break-before: page; }
table.bt td:first-child { width: 11mm; } table.bt td:nth-child(2) { width: 11mm; }
.key pre.code { font-size: 8.4pt; padding: 1mm 2mm; margin: 1mm 0; }
.key code { font-size: 8.6pt; }
"""


def balanced(mod, seed):
    """Reorder options so the correct letters are spread over A-D."""
    rnd = random.Random(seed)
    pool = list("AAAABBBBCCCCDDD")
    rnd.shuffle(pool)
    out = []
    for (q, opts, ans, why, fig), tgt in zip(mod.MCQS, pool):
        opts = list(opts)
        ci, ti = "ABCD".index(ans), "ABCD".index(tgt)
        opts[ci], opts[ti] = opts[ti], opts[ci]
        out.append((q, opts, tgt, why, fig))
    return out


def paper(n, mod, mcqs):
    h = [f'<div class="set{n}">']
    h.append(f'<div class="cover"><div class="t1">CLASS X &middot; PRACTICE EXAMINATION</div><div class="t2">INFORMATION &amp; COMMUNICATION TECHNOLOGY<br>MODEL QUESTION PAPER {n}</div><div class="t3">Final I pattern &middot; Section A (40) + Section B (60)</div>'
             f'<table><tr><td>Code: {mod.CODE}</td><td>Time: 2 hours 30 minutes</td></tr><tr><td>Total: 100 marks</td><td>Pages: see footer</td></tr></table></div>')
    h.append('<div class="inst"><b>Instructions.</b> (1) Section A is compulsory: Question 1 carries 40 marks. (2) In Section B answer <b>ALL</b> questions (Q2 to Q7, 10 marks each). (3) Write the answers in the spaces given; write program code neatly with correct indentation. (4) Circle only <b>ONE</b> letter in the multiple-choice questions. (5) This is a practice paper made for revision; it is not an official question paper.</div>')
    h.append('<h2 class="sec">SECTION A [40 MARKS]</h2><div class="sub">ANSWER <b>ALL</b> QUESTIONS</div><div class="q"><span>Question 1</span><span>[40]</span></div>')
    h.append('<div class="part"><div class="lab">a)</div><div class="txt dir">Directions: For each question there are four alternatives A, B, C and D. Choose the correct alternative and circle it neatly. Each question carries 2 marks. If more than one letter is circled, NO score will be awarded.</div><div class="mk">[30]</div></div>')
    for r, (t, o, a, why, fg) in zip(ROM, mcqs):
        h.append(B.mcq(r + ".", t, o, fg))
    h.append('<div class="blk"><div class="part"><div class="lab">b)</div><div class="txt">Fill in the blanks with suitable word/s.</div><div class="mk">[5]</div></div><table class="tab">' + "".join(f'<tr><td style="width:12mm">{ROM[i]}.</td><td>{t}</td><td class="m"></td></tr>' for i, (t, a) in enumerate(mod.FILL)) + "</table></div>")
    h.append('<div class="blk"><div class="part"><div class="lab">c)</div><div class="txt">Write <b>TRUE</b> or <b>FALSE</b> for each statement in the &lsquo;Answer&rsquo; column.</div><div class="mk">[5]</div></div><table class="tab">' + "".join(f'<tr><td style="width:12mm">{ROM[i]}.</td><td>{t}</td><td class="a"></td><td class="m"></td></tr>' for i, (t, a) in enumerate(mod.TF)) + "</table></div>")
    h.append('<div class="newpage"></div><h2 class="sec">SECTION B [60 MARKS]</h2><div class="sub">ANSWER <b>ALL</b> QUESTIONS</div>')
    for q, parts in mod.QB.items():
        tot = sum(p[2] for p in parts)
        assert tot == 10, (n, q, tot)
        h.append(f'<div class="q" style="break-after:avoid"><span>Question {q}</span><span>[10]</span></div>')
        for (lab, text, marks, fig, bh, ans) in parts:
            h.append(B.part(lab, text, marks if lab else "", fig, bh))
    h.append('<div class="rough">Rough Work</div></div>')
    return "".join(h)


def keys(n, mod, mcqs):
    h = [f'<div class="key"><h2 class="sec">ANSWER KEY &mdash; MODEL PAPER {n}</h2><div class="sub">{mod.CODE} &middot; for self-checking</div>']
    h.append('<h3>Section A &mdash; Q1(a) Multiple choice (2 marks each)</h3><table class="tab"><tr><th style="width:12mm">No.</th><th style="width:14mm">Answer</th><th>Reason</th></tr>')
    for r, (t, o, a, why, fg) in zip(ROM, mcqs):
        h.append(f"<tr><td>{r}.</td><td><b>{a}</b></td><td>{why}</td></tr>")
    h.append("</table>")
    h.append('<h3>Q1(b) Fill in the blanks &middot; Q1(c) True/False (1 mark each)</h3><table class="tab"><tr><th style="width:12mm"></th><th>(b)</th><th>(c)</th></tr>')
    for i in range(5):
        h.append(f"<tr><td>{ROM[i]}.</td><td><b>{mod.FILL[i][1]}</b></td><td><b>{mod.TF[i][1]}</b></td></tr>")
    h.append("</table><h3 class='sb'>Section B (10 marks per question; all compulsory) &mdash; columns: part, marks, model answer</h3>")
    for q, parts in mod.QB.items():
        h.append(f"<h4>Question {q}</h4><table class='tab bt'>")
        for (lab, text, marks, fig, bh, ans) in parts:
            h.append(f"<tr><td>{lab}</td><td>{marks}</td><td>{ans}</td></tr>")
        h.append("</table>")
    h.append("</div>")
    return "".join(h)


def build():
    m1, m2 = balanced(ictm_set1, 31), balanced(ictm_set2, 32)
    body = paper(1, ictm_set1, m1) + '<div class="newpage"></div>' + paper(2, ictm_set2, m2)
    body += '<div class="keys"><div class="newpage"></div><div class="cover"><div class="t2">ANSWER KEYS</div><div class="t3">ICT Model Paper 1 and Model Paper 2</div></div>' + keys(1, ictm_set1, m1) + '<div class="newpage"></div>' + keys(2, ictm_set2, m2)
    body += '<div class="key"><p><b>Marking guide:</b> in Section B each bracketed point is worth the mark shown; accept any correct program or answer written in different words. For programs, minor spelling slips in names are not penalised when the logic is correct, but missing colons or wrong indentation can lose the mark for that line. For &ldquo;write the output&rdquo; questions the output must be exactly as printed (one line per <code>print</code> unless <code>end</code> is used).</p></div></div>'
    return "<!doctype html><html><head><meta charset=utf-8><style>" + CSS + "</style></head><body>" + body + "</body></html>"


if __name__ == "__main__":
    f = ROOT / "BCSE_Class_X_ICT_Model_Papers.html"
    f.write_text(build(), encoding="utf-8")
    pdf = ROOT / "BCSE_Class_X_ICT_Model_Papers.pdf"
    subprocess.run([B.CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", f"file://{f}"], check=True, stderr=subprocess.DEVNULL)
    print("wrote", pdf)
