"""Para las filas sin PDF local, busca versión de acceso abierto (Unpaywall) y descarga solo PDFs legítimos de acceso abierto."""
import csv, json, os, re, urllib.request, urllib.parse, time
from concurrent.futures import ThreadPoolExecutor
B = os.path.join(os.path.dirname(__file__), "..", "..")
DEST = "/Users/mauricio/Documents/Data-science-local/ciudades/NUEVO-CONOCIMIENTO-GRD-2020-2026/_descargados_acceso_abierto"
os.makedirs(DEST, exist_ok=True)
rows = list(csv.DictReader(open(f"{B}/fuentes/vig/nuevo.csv")))
emp = json.load(open(f"{B}/fuentes/vig/emparejado.json"))
tiene = {v[0] for v in emp.values() if v}
log_f = f"{B}/fuentes/vig/descargas.json"
log = json.load(open(log_f)) if os.path.exists(log_f) else {}
H = {"User-Agent": "Mozilla/5.0 (teoria-riesgos; mailto:mauricio.romero.t@gmail.com)"}
def slug(s): return re.sub(r"[^A-Za-z0-9]+", "_", s)[:60]
def tarea(r):
    i, d = r["ID"], r["DOI"].strip().lower().replace("https://doi.org/", "")
    if i in tiene or not d or i in log: return
    res = {"doi": d, "estado": "sin_oa"}
    try:
        u = f"https://api.unpaywall.org/v2/{urllib.parse.quote(d)}?email=mauricio.romero.t@gmail.com"
        j = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=30))
        if j.get("is_oa"):
            locs = [j.get("best_oa_location")] + (j.get("oa_locations") or [])
            for l in [x for x in locs if x and x.get("url_for_pdf")]:
                try:
                    data = urllib.request.urlopen(urllib.request.Request(l["url_for_pdf"], headers=H), timeout=60).read(60_000_000)
                    if data[:5] == b"%PDF-":
                        fn = f"{i}_{slug(d)}.pdf"; open(f"{DEST}/{fn}", "wb").write(data)
                        res = {"doi": d, "estado": "descargado", "archivo": fn, "url": l["url_for_pdf"], "licencia": l.get("license")}; break
                except Exception: continue
            else: res["estado"] = "oa_sin_pdf_directo"; res["url"] = (j.get("best_oa_location") or {}).get("url")
    except Exception as e: res["estado"] = "error"
    log[i] = res
with ThreadPoolExecutor(4) as ex: list(ex.map(tarea, rows))
json.dump(log, open(log_f, "w"), ensure_ascii=False, indent=0)
from collections import Counter; print(Counter(v["estado"] for v in log.values()))
