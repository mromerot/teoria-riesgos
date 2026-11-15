#!/usr/bin/env python3
"""Verifica que resultados/ cumpla el contrato de salida (resultados/LEEME.md).

Uso: python scripts/verificar_salida.py [--estricto]
Sale con código 1 si falta un parámetro obligatorio o una fuente.
Con --estricto, los parámetros 'por_defecto' también son error.
"""
import argparse
import csv
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PARAMETROS = RAIZ / "resultados" / "parametros.csv"

OBLIGATORIOS = [
    "version_libro", "fecha_corrida",
    "dem_fuente", "dem_tipo", "dem_resolucion_m", "dem_respaldo_usado",
    "huellas_fuente", "huellas_completitud_pct", "huellas_fecha_extraccion", "huellas_licencia",
    "poblacion_total", "poblacion_fuente", "poblacion_anio",
    "costo_fuente", "costo_residencial_usd_m2", "costo_residencial_rango_usd_m2",
    "contenidos_pct", "curva_dano_fuente",
    "escenarios_origen", "rp_minimo_escenarios", "pae_exclusiones",
]
COLUMNAS = ["parametro", "valor", "unidad", "fuente", "nivel", "fecha_verificacion", "estado"]
ESTADOS = {"verificado", "por_verificar", "por_defecto", "supuesto"}
NIVELES = {"local", "nacional", "global", "supuesto"}
ENUMS = {
    "dem_tipo": {"superficie", "terreno"},
    "dem_respaldo_usado": {"si", "no"},
    "costo_fuente": {"gem", "jrc", "propio"},
    "escenarios_origen": {"local", "estudio", "por_defecto"},
}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--estricto", action="store_true")
    a = p.parse_args()

    if not PARAMETROS.exists():
        print(f"ERROR: no existe {PARAMETROS.relative_to(RAIZ)}")
        return 1
    with PARAMETROS.open(encoding="utf-8", newline="") as f:
        lector = csv.DictReader(f)
        faltan_cols = [c for c in COLUMNAS if c not in (lector.fieldnames or [])]
        if faltan_cols:
            print(f"ERROR: faltan columnas en parametros.csv: {faltan_cols}")
            return 1
        filas = {r["parametro"].strip(): r for r in lector if r["parametro"].strip()}

    errores, avisos = [], []
    for k in OBLIGATORIOS:
        if k not in filas or not filas[k]["valor"].strip():
            errores.append(f"falta el parámetro obligatorio «{k}»")
    for k, r in filas.items():
        if not r["fuente"].strip():
            errores.append(f"«{k}» no tiene fuente")
        if r["estado"].strip() not in ESTADOS:
            errores.append(f"«{k}»: estado «{r['estado']}» no válido ({sorted(ESTADOS)})")
        if r["nivel"].strip() not in NIVELES:
            errores.append(f"«{k}»: nivel «{r['nivel']}» no válido ({sorted(NIVELES)})")
        if k in ENUMS and r["valor"].strip() and r["valor"].strip() not in ENUMS[k]:
            errores.append(f"«{k}»: valor «{r['valor']}» no válido ({sorted(ENUMS[k])})")
        if r["estado"].strip() == "por_defecto":
            (errores if a.estricto else avisos).append(f"«{k}» se dejó por defecto: no citar su resultado")
        if r["estado"].strip() == "por_verificar":
            avisos.append(f"«{k}» está por verificar")

    if filas.get("dem_respaldo_usado", {}).get("valor", "").strip() == "si":
        avisos.append("se usó un DEM de respaldo: declararlo en el capítulo de datos")
    try:
        c = float(filas.get("huellas_completitud_pct", {}).get("valor", ""))
        if c < 80:
            avisos.append("completitud de las huellas menor a 80 %: las cuentas de edificios y población quedan bajas")
        elif c > 120:
            avisos.append("completitud de las huellas mayor a 120 %: posibles duplicados o sobreestimación")
    except ValueError:
        pass
    for k in filas:
        if k.startswith("amenaza_") and k.endswith("_calibrado") and filas[k]["valor"].strip() == "no":
            avisos.append(f"«{k[:-10]}» no está calibrada: no combinar con dinero")

    for m in avisos:
        print(f"AVISO: {m}")
    for m in errores:
        print(f"ERROR: {m}")
    print(f"{len(errores)} errores, {len(avisos)} avisos, {len(filas)} parámetros.")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
