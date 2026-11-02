# Teoría y métodos de análisis de riesgos: instrucciones para Claude Code

Libro MyST (`mystmd`) con la teoría y los métodos para analizar riesgos de desastres y climáticos de ciudades de Colombia. Se invoca cada vez que se analiza una ciudad (skill `nueva-ciudad`). Autor: Mauricio Romero. Idioma: **español**.

## Antes de trabajar
1. Lee `plan/01_estado.md` (qué está hecho, madurez de cada capítulo, pendientes) y, si hace falta, `plan/00_plan.md`.
2. Trabaja **una rebanada por sesión** (un capítulo, una fuente o un grupo de artículos) y al cerrarla actualiza `plan/01_estado.md`.

## Estructura
- `book/01_conceptos` a `05_sintesis` y `book/recursos`: el libro. Cada capítulo de amenaza sigue el molde de siete puntos (`book/03_amenazas/_molde.md`).
- `book/03_amenazas/31x_*.ipynb`: cuadernos con salidas guardadas; su fuente está en `scripts/cuadernos/` y se reconstruyen con `python scripts/cuadernos/construir.py 313 314 315` (ejecutar con `JUPYTER_DATA_DIR` vacío si el kernel `python3` del usuario falla).
- `plantilla/` y `scripts/nueva_ciudad.py`: plantilla de repositorio de ciudad.
- `estilo/`: identidad visual; tras cambiar `estilo.css` o un ícono, `python estilo/construir_css.py`.
- `fuentes/`: índice de la hoja de vigilancia (`vigilancia_ctei.csv`). `fuentes/texto/` y los PDFs **no se versionan**.

## Reglas
- Cada afirmación con cita `{cite:p}` contra `references.bib`; lo no verificado se marca «por verificar». No citar lo que solo se conoce por título sin decirlo.
- No citar borradores propios no publicados.
- No inventar URLs ni datos; los datos inventados van rotulados.
- No publicar PDFs, texto extraído ni fichas de lectura; parafrasear, citas literales de menos de 15 palabras, figuras de terceros solo enlazadas.
- Construir con `myst build --html` y dejarlo **sin avisos**.
- Nada de commit ni push sin que se pida. «Despliega los cambios» = construir, commit, push y verificar la Action (cuenta `mromerot`).
- Los capítulos provisionales llevan su advertencia al inicio.
