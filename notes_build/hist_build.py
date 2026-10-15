#!/usr/bin/env python3
"""Build the Class X History notes PDF from parts/h_*.html (two-column exam-notes layout)."""
import re, subprocess, pathlib, sys

ROOT = pathlib.Path(__file__).parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
TITLE = "BCSE Class X History - Exam Revision Notes"


def expand(s):
    # paper tags  [[P25 Q2a]]  ;  diagram note tag  [[IMG text]]
    s = re.sub(r"\[\[IMG ([^\]]+)\]\]", r'<span class="t d">\1</span>', s)
    s = re.sub(r"\[\[fig:([a-z0-9_]+)\|([^\]]*)\]\]",
               lambda m: f'<figure>{(ROOT / "figs_h" / (m.group(1) + ".svg")).read_text(encoding="utf-8")}<figcaption>{m.group(2)}</figcaption></figure>', s)
    s = re.sub(r"\[\[([^\]]+)\]\]", r'<span class="t">\1</span>', s)
    s = re.sub(r"@@(.+?)@@", r'<span class="r">\1</span>', s, flags=re.S)
    # solved box:  <sol L="P25 Q2a [5]"> ... </sol>
    s = re.sub(r'<sol L="([^"]*)">', r'<div class="sol"><span class="l">\1</span> ', s)
    s = s.replace("</sol>", "</div>")
    return s


def main():
    parts = sorted((ROOT / "parts").glob("h_*.html"))
    body = "\n".join(p.read_text(encoding="utf-8") for p in parts)
    body = expand(body)
    css = (ROOT / "hist_style.css").read_text()
    doc = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{TITLE}</title><style>{css}</style></head><body>{body}</body></html>'
    out = ROOT / "hist.html"
    out.write_text(doc, encoding="utf-8")
    pdf = ROOT / "BCSE_Class_X_History_-_Exam_Notes.pdf"
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", f"file://{out}"], check=True, stderr=subprocess.DEVNULL)
    print("wrote", pdf)


if __name__ == "__main__":
    main()
