# ${nombre}: instrucciones para Claude Code

Proyecto de análisis de riesgos de desastres y climáticos de ${nombre} (${municipio}). Idioma: español.

## Antes de trabajar
1. Lee `plan/01_estado.md` y trabaja un paso por sesión.
2. Para cada amenaza, abre su capítulo en el libro de teoría (enlace en `book/analisis/a_<amenaza>.md`) y sigue su sección 7 (datos y medidas).
3. Al terminar un paso, marca `[x]` con fecha y notas en `plan/01_estado.md`.

## Reglas
- Todo lo propio de la ciudad va en `config/*.yaml`, no en el código.
- Cada insumo se registra en `config/sources.yaml` con nivel de respaldo (local, nacional, global) y fecha de verificación. No inventar URLs.
- Citas con `{cite:p}` contra `references.bib`. Lo no verificado se marca «por verificar».
- Los capítulos provisionales del libro de teoría (erosión costera, erosión fluvial, calor, vendavales) exigen buscar la metodología específica y citarla.
- No sumar PML entre amenazas ni mezclar índices relativos con dinero (ver síntesis del libro).
- No publicar datos personales; agregar a manzana cuando haya duda.

## Comandos
```bash
myst start                   # vista previa
myst build --html            # construir
```
