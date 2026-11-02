---
title: 3. Amenazas
---

# 3. Amenazas

Cada capítulo de amenaza sigue el mismo molde de siete puntos ([](_molde.md)): fenómeno, amenaza, exposición, vulnerabilidad, riesgo, clima, y datos y medidas.

## Estado de los capítulos

| Capítulo | Base principal | Respaldo | Sensible al clima |
|---|---|---|---|
| [](301_sismo.md) | Atlas 2019 y literatura nacional | Sólido | No |
| [](302_volcanes.md) | Atlas 2019 | Sólido en lo general, falta literatura reciente | No (lahares, en parte) |
| [](303_tsunami.md) | Atlas 2019 y caso de Guapi | Sólido | No (sí el nivel del mar) |
| [](304_mov_masa.md) | Atlas 2019 y literatura nacional | Sólido | Sí, por la lluvia |
| [](305_inundacion.md) | Atlas 2019 y CLIMAAX | Sólido | Sí |
| [](316_avenidas_torrenciales.md) | Guía metodológica SGC–Javeriana 2021 | Sólido | Poco (según la guía) |
| [](306_erosion_costera.md) | Literatura de la hoja de vigilancia | **Provisional** | Sí |
| [](307_erosion_fluvial.md) | Literatura de la hoja de vigilancia | **Provisional** | Sí |
| [](308_sequia.md) | Atlas 2019 y CLIMAAX | Sólido | Sí |
| [](309_calor.md) | CLIMAAX, CCDR-tools y dos estudios | **Provisional** | Sí |
| [](310_incendios.md) | Atlas 2019 y CLIMAAX | Sólido | Sí, y por ignición humana |
| [](311_ciclones.md) | Atlas 2019 y estudios del archipiélago | Sólido | Sí |
| [](312_vendavales.md) | Borrador UNGRD (Quindío), DNP y CLIMAAX | **Provisional** | Incierto |

«Sólido» significa que existe una metodología nacional o internacional descrita en una fuente de referencia. No significa que todas las citas se hayan verificado contra el texto completo: cada capítulo lista al final lo que falta leer.

## Análisis integrados con cuadernos

Cuatro secciones muestran con ejemplos ejecutables (cuadernos de Jupyter, abribles en Colab) cómo se combinan resultados o se trabaja con datos reales. Los dos primeros **usan datos inventados**, rotulados como tales, para enseñar el cálculo y no para sacar conclusiones sobre ninguna ciudad. Los otros dos usan datos reales.

| Sección | Qué muestra |
|---|---|
| [](313_analisis_multiamenaza.ipynb) | Escenarios por detonante, pérdida por edificación, mínimo, medio y máximo, curvas de riesgo, PAE con cotas, y qué se suma y qué no |
| [](314_riesgos_cascada.ipynb) | Una red de servicios interdependientes (daño directo frente a cascada) y un bucle de retroalimentación como el de Limbe |
| [](317_sismicidad_colombia.ipynb) | **Datos reales** (USGS): catálogo sísmico de Colombia y su área de influencia, magnitud de completitud, relación de Gutenberg-Richter y profundidades. Alimenta el capítulo de sismos |
| [](315_trayectorias_ciclones.ipynb) | **Datos reales** (IBTrACS): trayectorias de ciclones en el Caribe y conteo de sistemas cerca de sitios de Colombia. Genera la figura del capítulo de ciclones |

La teoría está en [](../01_conceptos/14_riesgo_multiamenaza.md) y [](../01_conceptos/15_cascada_compuestos.md).

## Cómo se relacionan

Varias amenazas comparten el detonante o el mecanismo, por lo que un análisis de ciudad debe revisar las cascadas y no solo cada amenaza por separado.

| Detonante | Amenazas que activa |
|---|---|
| Sismo | Tsunami, movimientos en masa, licuefacción |
| Lluvia intensa | Inundación, movimientos en masa, erosión fluvial |
| Ciclón tropical | Viento, marea de tormenta, lluvia (inundación y deslizamientos) |
| Tormenta convectiva severa | Vendaval, lluvia intensa (crecidas súbitas), granizo, tormentas eléctricas, interrupción de servicios (ver [](312_vendavales.md)) |
| Erupción | Caída de ceniza, flujos piroclásticos, lahares |
| Sequía y calor | Incendios forestales |
| Ascenso del nivel del mar | Erosión costera, inundación costera |

La teoría de las cascadas y los eventos compuestos está en [](../01_conceptos/15_cascada_compuestos.md). Este cuadro es un criterio de organización del libro, no una afirmación de una fuente única. Los vínculos sismo–tsunami, lluvia–deslizamiento y ciclón–lluvia aparecen en el Atlas {cite:p}`ungrd2019atlas`.
