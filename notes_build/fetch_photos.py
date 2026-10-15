#!/usr/bin/env python3
"""Download the Wikimedia Commons photos used in the History / Geography notes.

Reads photos_h.json / photos_g.json  ({key: {"file": "File:Name.jpg", "w": 700}}),
saves a resized JPEG to figs_h/photos/<key>.jpg (or figs_g/photos/), and writes the
author + licence + source URL to photos/credits so captions can credit them.
Images are stored in the repo, so building the PDFs needs no network access.
"""
import json, pathlib, re, sys, time, urllib.parse, urllib.request, urllib.error, html

ROOT = pathlib.Path(__file__).parent
API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "gameforge-notes/1.0 (educational class notes)"}


def http(url, as_json=False):
    for i in range(8):
        try:
            data = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
            return json.loads(data) if as_json else data
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
            time.sleep(8 * (i + 1))
    raise SystemExit("rate limited: " + url)


def clean(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def main(which):
    spec = json.loads((ROOT / f"photos_{which}.json").read_text())
    out = ROOT / f"figs_{which}" / "photos"
    out.mkdir(parents=True, exist_ok=True)
    credits = {}
    cpath = out / "credits.json"
    if cpath.exists():
        credits = json.loads(cpath.read_text())
    todo = {k: v for k, v in spec.items() if not (out / f"{k}.jpg").exists() or k not in credits}
    for k, v in todo.items():
        q = urllib.parse.urlencode({"action": "query", "format": "json", "titles": v["file"], "prop": "imageinfo",
                                    "iiprop": "url|extmetadata", "iiurlwidth": v.get("w", 700)})
        r = http(API + "?" + q, True)
        page = next(iter(r["query"]["pages"].values()))
        ii = page["imageinfo"][0]
        md = ii["extmetadata"]
        credits[k] = {"title": page["title"], "url": ii["descriptionurl"],
                      "author": clean(md.get("Artist", {}).get("value")) or "Unknown",
                      "license": clean(md.get("LicenseShortName", {}).get("value"))}
        time.sleep(2)
        (out / f"{k}.jpg").write_bytes(http(ii["thumburl"]))
        print(k, credits[k]["license"], "|", credits[k]["author"][:40], flush=True)
        time.sleep(2)
    cpath.write_text(json.dumps(credits, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1])
