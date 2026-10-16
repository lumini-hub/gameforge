#!/usr/bin/env python3
"""Build the Class X Biology notes PDF from parts/b_*.html (two-column exam-notes layout)."""
import re, json, html, subprocess, pathlib, sys

ROOT = pathlib.Path(__file__).parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
TITLE = "BCSE Class X Biology - Exam Revision Notes"

PHOTO_DIR = "figs_b/photos"
WIDE = {"d_prokaryote": 85, "d_cell_membrane": 105, "d_chloroplast": 80, "d_digestive": 120, "d_nephron": 110, "d_mitosis": 105, "d_hotspot": 80}
SMALL = {"d_prokaryote", "d_neuron", "d_blood", "d_girdle", "d_hpylori", "d_lantana", "d_villus", "d_xylem_phloem", "d_photosynthesis", "d_cell_membrane", "d_tonicity", "d_biogas", "d_hotspot"}


def photo(key, cap):
    """Photo figure (Wikimedia Commons image stored locally) with a credit line."""
    d = ROOT / PHOTO_DIR
    try:
        c = json.loads((d / "credits.json").read_text(encoding="utf-8"))[key]
    except (OSError, KeyError):
        c = None
    if c is None or not (d / f"{key}.jpg").exists():
        print("photo not downloaded yet, skipped:", key, file=sys.stderr)
        return ""
    who = c["author"] if len(c["author"]) <= 42 else c["author"][:40].rstrip() + "…"
    from PIL import Image
    w, h = Image.open(d / f"{key}.jpg").size
    cls = "photo tall" if h > w * 1.1 else "photo"
    if key.startswith(("map_", "d_")):
        cls += " map"
    if key in SMALL:
        cls += " small"
    style = ""
    if key in WIDE:
        cls += " wide"
        style = f' style="--mh:{WIDE.get(key, 100)}mm"' if "WIDE" in globals() else ""
    return (f'<figure class="{cls}"{style}><img src="{PHOTO_DIR}/{key}.jpg" alt="{html.escape(cap, quote=True)}">'
            f'<figcaption>{cap} <span class="cr">Image: {html.escape(who)}, {html.escape(c["license"])}, Wikimedia Commons.</span></figcaption></figure>')


def expand(s):
    # paper tags  [[P25 Q2a]]  ;  diagram note tag  [[IMG text]]
    s = re.sub(r"\[\[IMG ([^\]]+)\]\]", r'<span class="t d">\1</span>', s)
    s = re.sub(r"\[\[pair:([a-z0-9_]+)\|([^|\]]*)\|([a-z0-9_]+)\|([^\]]*)\]\]", lambda m: '<div class="pair">' + photo(m.group(1), m.group(2)) + photo(m.group(3), m.group(4)) + "</div>", s)
    s = re.sub(r"\[\[fig:([a-z0-9_]+)\|([^\]]*)\]\]",
               lambda m: f'<figure class="wide">{(ROOT / "figs_b" / (m.group(1) + ".svg")).read_text(encoding="utf-8")}<figcaption>{m.group(2)}</figcaption></figure>', s)
    s = re.sub(r"\[\[photo:([a-z0-9_]+)\|([^\]]*)\]\]", lambda m: photo(m.group(1), m.group(2)), s)
    s = re.sub(r"\[\[([^\]]+)\]\]", r'<span class="t">\1</span>', s)
    s = re.sub(r"@@(.+?)@@", r'<span class="r">\1</span>', s, flags=re.S)
    # solved box:  <sol L="P25 Q2a [5]"> ... </sol>
    s = re.sub(r'<sol L="([^"]*)">', r'<div class="sol"><span class="l">\1</span> ', s)
    s = s.replace("</sol>", "</div>")
    return s


def main():
    parts = sorted((ROOT / "parts").glob("b_*.html"))
    body = "\n".join(p.read_text(encoding="utf-8") for p in parts)
    body = expand(body)
    css = (ROOT / "hist_style.css").read_text()
    doc = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{TITLE}</title><style>{css}</style></head><body>{body}</body></html>'
    out = ROOT / "bio.html"
    out.write_text(doc, encoding="utf-8")
    pdf = ROOT / "BCSE_Class_X_Biology_-_Exam_Notes.pdf"
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", f"file://{out}"], check=True, stderr=subprocess.DEVNULL)
    print("wrote", pdf)


if __name__ == "__main__":
    main()
