"""Descarga metadatos de Crossref para cada DOI de la hoja Vigilancia_CTeI (caché en fuentes/vig/crossref.json)."""
import csv, json, os, sys, time, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor
R = os.path.join(os.path.dirname(__file__), "..", "..", "fuentes", "vig")
cache_f = os.path.join(R, "crossref.json")
cache = json.load(open(cache_f)) if os.path.exists(cache_f) else {}
rows = list(csv.DictReader(open(os.path.join(R, "nuevo.csv"))))
dois = sorted({r["DOI"].strip().lower().replace("https://doi.org/", "") for r in rows if r["DOI"].strip()})
def get(d):
    if d in cache: return
    u = "https://api.crossref.org/works/" + urllib.parse.quote(d) + "?mailto=mauricio.romero.t@gmail.com"
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "teoria-riesgos/1.0"}), timeout=30) as f:
                cache[d] = json.load(f)["message"]; return
        except urllib.error.HTTPError as e:
            if e.code == 404: cache[d] = None; return
            time.sleep(2 * (i + 1))
        except Exception:
            time.sleep(2 * (i + 1))
with ThreadPoolExecutor(5) as ex: list(ex.map(get, dois))
json.dump(cache, open(cache_f, "w"))
print(len(dois), sum(1 for d in dois if cache.get(d)), "con metadatos")
