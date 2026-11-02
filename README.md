# Teoría y métodos de análisis de riesgos de desastres y climáticos

Libro MyST con la teoría y los métodos para evaluar amenazas, exposición, vulnerabilidad y riesgo en ciudades de Colombia. Sigue CLIMAAX, CCDR-tools y CLIMADA.

Estado: las cinco partes y el glosario están escritas. Cada capítulo lista al final lo que falta verificar (varios artículos están citados solo por título o resumen).

Construir localmente: `myst build --html`.

`fuentes/vigilancia_ctei.csv` es un índice de la hoja de vigilancia CTeI. El texto extraído de los PDFs de referencia no se versiona.

## Plantilla para una ciudad nueva

`plantilla/` y `scripts/nueva_ciudad.py` crean el repositorio de análisis de una ciudad con el inventario de amenazas, el catálogo de datos, el plan de siete pasos y una página por amenaza:

```bash
python scripts/nueva_ciudad.py --listar
python scripts/nueva_ciudad.py --nombre "Ciudad" --municipio "Municipio, Depto" --divipola 00000 \
    --destino ../ciudad --amenazas inundacion,calor
```

El skill `nueva-ciudad` de Claude Code (en `~/.claude/skills/`) la invoca. La plantilla no incluye código de análisis; el paquete compartido está pendiente.

## Cuadernos de la parte 3

`book/03_amenazas/313_analisis_multiamenaza.ipynb` y `314_riesgos_cascada.ipynb` son cuadernos con **datos inventados**, con las salidas ya guardadas (se ven en el sitio sin ejecutar). Se pueden abrir en Colab desde el botón de cada página. Su fuente está en `scripts/cuadernos/` y se regeneran y ejecutan con:

```bash
python scripts/cuadernos/construir.py 313 314 315
```

## Diseño

La identidad visual (logo, paleta, íconos de amenaza y sidebar fijo) es la misma de EVA y SIDRo y vive en `estilo/`. Tras cambiar `estilo/estilo.css` o un ícono de `estilo/iconos/`, regenerar la hoja con:

```bash
python estilo/construir_css.py
```
