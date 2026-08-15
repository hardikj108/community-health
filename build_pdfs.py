#!/usr/bin/env python3
"""Convert chapters/chapter-XX.md -> pdf/chapter-XX.pdf using markdown + WeasyPrint.
Usage: python3 build_pdfs.py [chapter-number ...]   (no args = all)
"""
import sys, os, glob, re
import markdown
from weasyprint import HTML

ROOT = os.path.dirname(os.path.abspath(__file__))
CH_DIR = os.path.join(ROOT, "chapters")
PDF_DIR = os.path.join(ROOT, "pdf")
CSS = os.path.join(ROOT, "assets", "style.css")
os.makedirs(PDF_DIR, exist_ok=True)

MD_EXT = ["tables", "fenced_code", "attr_list", "md_in_html", "sane_lists", "toc", "footnotes"]

def build(md_path):
    name = os.path.splitext(os.path.basename(md_path))[0]
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    html_body = markdown.markdown(text, extensions=MD_EXT)
    html = f"<!DOCTYPE html><html><head><meta charset='utf-8'></head><body>{html_body}</body></html>"
    out = os.path.join(PDF_DIR, name + ".pdf")
    HTML(string=html, base_url=ROOT).write_pdf(out, stylesheets=[CSS])
    size = os.path.getsize(out) / 1024
    print(f"  built {out}  ({size:.0f} KB)")

def main():
    args = sys.argv[1:]
    if args:
        files = []
        for a in args:
            n = re.sub(r"\D", "", a).zfill(2)
            files += glob.glob(os.path.join(CH_DIR, f"chapter-{n}.md"))
    else:
        files = sorted(glob.glob(os.path.join(CH_DIR, "chapter-*.md")))
    if not files:
        print("No chapter markdown files found in", CH_DIR); return
    for f in sorted(files):
        build(f)
    print(f"Done: {len(files)} PDF(s).")

if __name__ == "__main__":
    main()
