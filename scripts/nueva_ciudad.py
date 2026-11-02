#!/usr/bin/env python3
"""Crea el repositorio de análisis de una ciudad nueva a partir de plantilla/.

Uso:
  python scripts/nueva_ciudad.py --nombre "Leticia" --municipio "Leticia, Amazonas" \
      --divipola 91001 --destino ../leticia2 --amenazas inundacion,erosion-fluvial,calor
  python scripts/nueva_ciudad.py --listar     # muestra las amenazas disponibles

No sobrescribe: si el destino existe y no está vacío, se detiene.
"""
import argparse
import datetime
import re
import sys
import unicodedata
from pathlib import Path
from string import Template

RAIZ = Path(__file__).resolve().parent.parent
PLANTILLA = RAIZ / "plantilla"

# clave -> (título, capítulo teórico, estado del respaldo en el libro, códigos HIP de UNDRR-ISC)
AMENAZAS = {
    "sismo": ("Sismo", "sismo", "solido", "GH0101, GH0307, GH0311"),
    "volcanes": ("Volcanes", "volcanes", "solido", "GH0201, GH0202, GH0203, GH0204, GH0205"),
    "tsunami": ("Tsunami", "tsunami", "solido", "MH0705"),
    "mov-masa": ("Movimientos en masa", "mov-masa", "solido", "GH0300, GH0301, GH0302, GH0303, GH0304, GH0305"),
    "avenidas-torrenciales": ("Avenidas torrenciales", "avenidas-torrenciales", "solido", "MH0603, GH0303"),
    "inundacion": ("Inundación", "inundacion", "solido", "MH0600, MH0601, MH0603, MH0604, MH0609"),
    "erosion-costera": ("Erosión costera y aumento del nivel del mar", "erosion-costera", "provisional", "GH0405, EN0402"),
    "erosion-fluvial": ("Erosión fluvial", "erosion-fluvial", "provisional", "GH0404"),
    "sequia": ("Sequía", "sequia", "solido", "MH0401"),
    "calor": ("Olas de calor", "calor", "provisional", "MH0501"),
    "incendios": ("Incendios forestales", "incendios", "solido", "EN0205"),
    "ciclones": ("Ciclones tropicales", "ciclones", "solido", "MH0309, MH0703, MH0704"),
    "natech": ("Natech", "natech", "provisional", "TL0309"),
    "vendavales": ("Vendavales", "vendavales", "provisional", "MH0101, MH0304, MH0302, MH0305"),
}
AVISO_PROV = (
    "\n\n```{warning}\nEl capítulo teórico es **provisional**: hay poca literatura de referencia. "
    "Busca la metodología específica antes de analizar y cita la fuente de cada decisión.\n```"
)


def slug(texto: str) -> str:
    s = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def render(archivo: Path, valores: dict) -> str:
    return Template(archivo.read_text(encoding="utf-8")).safe_substitute(valores)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--nombre")
    p.add_argument("--municipio")
    p.add_argument("--divipola", default="por completar")
    p.add_argument("--destino")
    p.add_argument("--amenazas", default="", help="claves separadas por coma; vacío = todas, marcadas por revisar")
    p.add_argument("--autor", default="Mauricio Romero")
    p.add_argument("--github", default="")
    p.add_argument("--listar", action="store_true")
    a = p.parse_args()

    if a.listar:
        for k, (t, _, e, h) in AMENAZAS.items():
            print(f"{k:16} {t}  [{e}]  HIP: {h}")
        return 0
    if not (a.nombre and a.municipio and a.destino):
        p.error("--nombre, --municipio y --destino son obligatorios")

    elegidas = [c.strip() for c in a.amenazas.split(",") if c.strip()]
    desconocidas = [c for c in elegidas if c not in AMENAZAS]
    if desconocidas:
        p.error(f"amenazas desconocidas: {desconocidas}. Usa --listar")
    todas = not elegidas
    aplican = list(AMENAZAS) if todas else elegidas

    destino = Path(a.destino).expanduser().resolve()
    if destino.exists() and any(destino.iterdir()):
        print(f"El destino {destino} existe y no está vacío. No se sobrescribe.", file=sys.stderr)
        return 1

    estado_aplica = "por_revisar" if todas else "si"
    bloque = "\n".join(
        f"{k}:\n  aplica: {'por_revisar' if todas else ('si' if k in elegidas else 'no')}\n"
        f"  respaldo: por_definir\n  hip: [{AMENAZAS[k][3]}]\n  eventos_historicos: null\n"
        f"  capitulo_teoria: https://mromerot.github.io/teoria-riesgos/{AMENAZAS[k][1]}"
        for k in AMENAZAS
    )
    tabla = "\n".join(
        f"| {AMENAZAS[k][0]} | [{AMENAZAS[k][1]}](https://mromerot.github.io/teoria-riesgos/{AMENAZAS[k][1]}) | "
        f"{AMENAZAS[k][3]} | {'por revisar' if todas else ('sí' if k in elegidas else 'no')} | por definir |"
        for k in AMENAZAS
    )
    pasos = "\n".join(f"- [ ] {AMENAZAS[k][0]}: riesgo actual con el método del capítulo" for k in aplican)
    lista = "\n".join(f"- [{AMENAZAS[k][0]}](a_{slug(k)}.md)" for k in aplican)

    v = dict(
        nombre=a.nombre, municipio=a.municipio, divipola=a.divipola, slug=slug(a.nombre),
        autor=a.autor,
        linea_github=(f"  github: {a.github}" if a.github else "  # github: https://github.com/USUARIO/REPO"), fecha=datetime.date.today().isoformat(),
        bloque_amenazas=bloque, tabla_amenazas=tabla, pasos_amenazas=pasos, lista_amenazas=lista,
    )

    destino.mkdir(parents=True, exist_ok=True)
    for f in sorted(PLANTILLA.rglob("*.tpl")):
        rel = f.relative_to(PLANTILLA)
        if rel.name in ("analisis_amenaza.md.tpl",):
            continue
        nombre_sal = rel.name[:-4]
        if rel.name == "analisis_index.md.tpl":
            sal = destino / "book" / "analisis" / "index.md"
        else:
            sal = destino / rel.parent / nombre_sal
        sal.parent.mkdir(parents=True, exist_ok=True)
        sal.write_text(render(f, v), encoding="utf-8")

    molde = PLANTILLA / "book" / "analisis_amenaza.md.tpl"
    for k in aplican:
        t, cap, est, _hip = AMENAZAS[k]
        w = dict(v, titulo=t, slug_teoria=cap, aviso=AVISO_PROV if est == "provisional" else "")
        (destino / "book" / "analisis" / f"a_{slug(k)}.md").write_text(render(molde, w), encoding="utf-8")

    print(f"Creado {destino} con {len(aplican)} páginas de amenaza.")
    print("Siguiente paso: abrir plan/01_estado.md y completar config/aoi.yaml.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
