"""Empareja los PDFs de la carpeta con las filas de la hoja (por DOI en el texto o por título). Escribe fuentes/vig/emparejado.json"""
import csv, json, os, re, subprocess, glob, unicodedata
B = os.path.join(os.path.dirname(__file__), "..", "..")
D = "/Users/mauricio/Documents/Data-science-local/ciudades/NUEVO-CONOCIMIENTO-GRD-2020-2026"
rows = list(csv.DictReader(open(f"{B}/fuentes/vig/nuevo.csv")))
def norm(s): return re.sub(r"[^a-z0-9 ]", " ", unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode())
def toks(s): return set(w for w in norm(s).split() if len(w) > 3)
bydoi = {r["DOI"].strip().lower().replace("https://doi.org/", ""): r["ID"] for r in rows if r["DOI"].strip()}
tit = {r["ID"]: toks(r["TITULO/TITLE"]) for r in rows}
out = {}
for f in sorted(glob.glob(D + "/**/*.pdf", recursive=True)):
    try: txt = subprocess.run(["pdftotext", "-l", "2", "-raw", f, "-"], capture_output=True, text=True, timeout=60).stdout
    except Exception: txt = ""
    low = txt.lower().replace(" ", "")
    hit = None
    for m in re.findall(r"10\.\d{4,9}/[^\s\"<>]+", low):
        m = m.rstrip(".,;)")
        for d, i in bydoi.items():
            if m.startswith(d.replace(" ", "")): hit = (i, "doi"); break
        if hit: break
    if not hit:
        tt = toks(os.path.basename(f) + " " + txt[:1500]); best = (0, None)
        for i, t in tit.items():
            if len(t) >= 4:
                sc = len(t & tt) / len(t)
                if sc > best[0]: best = (sc, i)
        if best[0] >= 0.8: hit = (best[1], f"titulo {best[0]:.2f}")
    out[os.path.basename(f)] = hit
json.dump(out, open(f"{B}/fuentes/vig/emparejado.json", "w"), ensure_ascii=False, indent=0)
ok = [k for k, v in out.items() if v]
print(len(out), "pdfs;", len(ok), "emparejados;", len(set(v[0] for v in out.values() if v)), "filas distintas")
print("sin pareja:", [k for k, v in out.items() if not v][:15])
