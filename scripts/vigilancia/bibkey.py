"""python bibkey.py DOI... -> añade a references.bib (si no están) y imprime clave por DOI."""
import sys, json, re, html, unicodedata
cr = json.load(open("fuentes/vig/crossref.json")); bib = open("references.bib").read()
def asc(s): return re.sub(r"[^a-z]", "", unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode())
def tex(s): return html.unescape(re.sub(r"<[^>]+>", "", s or "")).replace("&", r"\&").replace("%", r"\%")
add = ""
for d in sys.argv[1:]:
    d = d.lower().replace("https://doi.org/", ""); m = cr.get(d)
    if not m: print(d, "SIN METADATOS"); continue
    if f"doi       = {{{d}}}" in bib or f"doi = {{{d}}}" in bib.lower():
        mm = re.search(r"@\w+\{(\w+),[^@]*?doi\s*=\s*\{" + re.escape(d) + r"\}", bib, re.I | re.S); print(d, mm.group(1) if mm else "?"); continue
    a = m.get("author", [{}]); fam = asc(a[0].get("family", a[0].get("name", "anon")).split()[0])
    y = str((m.get("issued", {}).get("date-parts", [[0]])[0] or [0])[0])
    w = [x for x in asc(" ".join(m.get("title", ["x"])[:1]).replace(" ", "~")).split("~") if x] or ["x"]
    t = re.findall(r"[A-Za-z]{5,}", unicodedata.normalize("NFKD", m["title"][0]).encode("ascii", "ignore").decode()); key = fam + y + (t[0].lower() if t else "x")
    while re.search(r"\{" + key + ",", bib + add): key += "b"
    au = " and ".join(f"{tex(x.get('family',x.get('name','')))}, {tex(x.get('given',''))}".rstrip(", ") for x in m.get("author", [])) or "Anónimo"
    add += f"""
@article{{{key},
  author  = {{{au}}},
  title   = {{{tex(m['title'][0])}}},
  journal = {{{tex((m.get('container-title') or [''])[0])}}},
  year    = {{{y}}},
  volume  = {{{m.get('volume','')}}},
  number  = {{{m.get('issue','')}}},
  pages   = {{{m.get('page', m.get('article-number',''))}}},
  doi     = {{{d}}}
}}
"""
    print(d, key)
open("references.bib", "w").write(bib + add)
