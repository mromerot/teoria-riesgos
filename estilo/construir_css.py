"""Escribe `teoria.css`: la hoja de estilo del libro con los íconos de amenaza incrustados como SVG.

Uso: `python estilo/construir_css.py` (después de cambiar `estilo.css` o un ícono de `iconos/`).
Cada ícono se asocia al enlace del sidebar cuya ruta termina en `/<slug>` (las páginas son planas).
"""
from pathlib import Path
from urllib.parse import quote

AQUI = Path(__file__).parent

# slug de la página en el sitio -> archivo del ícono
ICONOS = {
    "sismo": "sismo",
    "volcanes": "volcanes",
    "tsunami": "tsunami",
    "mov-masa": "mov_masa",
    "inundacion": "inundacion",
    "avenidas-torrenciales": "avenidas_torrenciales",
    "erosion-costera": "erosion",
    "erosion-fluvial": "erosion",
    "sequia": "sequia",
    "calor": "calor",
    "incendios": "incendios",
    "ciclones": "ciclones",
    "vendavales": "lluvias_vendavales",
    "analisis-multiamenaza": "sintesis",
    "riesgos-cascada": "sintesis",
    "trayectorias-ciclones": "ciclones",
    "sintesis-multiamenaza": "sintesis",
    "lista-ciudad": "lista",
    "pmgrd": "pmgrd",
}


def uri_svg(ruta: Path) -> str:
    svg = " ".join(ruta.read_text(encoding="utf-8").split())
    return "data:image/svg+xml," + quote(svg, safe=" =:/,';()-.")


def reglas() -> str:
    lineas = []
    selectores = ", ".join(f".myst-primary-sidebar a[href$='/{s}']" for s in ICONOS)
    lineas.append(f"{selectores} {{\n  display: flex;\n  align-items: center;\n  gap: 0.5rem;\n}}")
    lineas.append(
        ", ".join(f".myst-primary-sidebar a[href$='/{s}']::before" for s in ICONOS)
        + " {\n  content: \"\";\n  flex: none;\n  width: 1.45em;\n  height: 1.45em;\n"
        "  background: no-repeat center / contain;\n}"
    )
    for slug, archivo in ICONOS.items():
        uri = uri_svg(AQUI / "iconos" / f"{archivo}.svg")
        lineas.append(f".myst-primary-sidebar a[href$='/{slug}']::before {{ background-image: url(\"{uri}\"); }}")
    return "\n".join(lineas) + "\n"


if __name__ == "__main__":
    base = (AQUI / "estilo.css").read_text(encoding="utf-8")
    (AQUI / "teoria.css").write_text(base.replace("/* ICONOS */", reglas()), encoding="utf-8")
    print("escrito", AQUI / "teoria.css")
