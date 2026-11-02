#!/usr/bin/env python3
"""Descarga los Hazard Information Profiles (HIPs) 2025 de UNDRR-ISC desde la API pública de PreventionWeb
y escribe un índice reducido en `fuentes/hips_281.csv` (código, nombre, tipo, clúster, definición en inglés).

Fuente y licencia: UNDRR-ISC (2025), 2025 Hazard Information Profiles, CC BY 4.0.
API documentada en https://www.preventionweb.net/understanding-disaster-risk/terminology/hips/machine-actionability-guide
Uso: python scripts/hips/extraer_hips.py
"""
import csv, json, urllib.request
from pathlib import Path

URL = "https://www.preventionweb.net/api/terms/hips"
RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / "fuentes" / "hips_281.csv"


def val(x):
    if isinstance(x, list):
        return [val(i) for i in x]
    if isinstance(x, dict):
        return x.get("@value", x)
    return x


def tipo_cluster(e):
    t = c = ""
    b = e.get("skos:broader") or []
    for i in (b if isinstance(b, list) else [b]):
        if i.get("dct:type") == "type":
            t = val(i["skos:prefLabel"])
        elif i.get("dct:type") == "cluster":
            c = val(i["skos:prefLabel"])
    return t, c


def main():
    req = urllib.request.Request(URL, headers={"Accept": "application/ld+json", "User-Agent": "teoria-riesgos"})
    grafo = json.load(urllib.request.urlopen(req, timeout=120))["@graph"]
    filas = []
    for e in grafo:
        t, c = tipo_cluster(e)
        sin = val(e.get("skos:altLabel")) or []
        sin = sin if isinstance(sin, list) else [sin]
        causas = [r.get("dct:identifier") for r in (e.get("xkos:causes") or [])]
        filas.append({
            "codigo": e["dct:identifier"], "nombre": val(e["skos:prefLabel"]), "tipo": t, "cluster": c,
            "definicion_en": (val(e.get("skos:definition")) or "").replace("\n", " ").strip(),
            "sinonimos_en": "; ".join(s for s in sin if s and s != "Not found"),
            "causa_de": ";".join(sorted(causas)),
        })
    filas.sort(key=lambda f: f["codigo"])
    SALIDA.parent.mkdir(exist_ok=True)
    with open(SALIDA, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0]))
        w.writeheader(); w.writerows(filas)
    print(f"{len(filas)} perfiles escritos en {SALIDA}")


if __name__ == "__main__":
    main()
