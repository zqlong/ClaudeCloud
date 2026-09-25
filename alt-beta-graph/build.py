#!/usr/bin/env python3
"""Inject a graph-data JSON into the knowledge-graph template.

usage: build.py template.html data.json out.html
"""
import json, sys, html

tpl, data_path, out = sys.argv[1:4]
data = json.load(open(data_path, encoding="utf-8"))

# validate
secs = {s["id"] for s in data["sections"]}
slugs = [t["slug"] for t in data["terms"]]
assert len(slugs) == len(set(slugs)), "duplicate slugs"
for t in data["terms"]:
    assert t["section"] in secs, f"unknown section for {t['slug']}"
    for k in ("title", "summary"):
        assert t.get(k), f"{t['slug']} missing {k}"

page = open(tpl, encoding="utf-8").read()
payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
page = (page.replace("__DATA__", payload)
            .replace("__TITLE__", html.escape(data["title"]))
            .replace("__WORDMARK__", data.get("wordmark_html") or html.escape(data["title"])))
open(out, "w", encoding="utf-8").write(page)
print(f"wrote {out}: {len(slugs)} terms, {len(secs)} sections")
