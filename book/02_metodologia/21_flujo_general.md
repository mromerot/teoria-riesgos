---
title: Flujo general de evaluación
---

# Flujo general de evaluación

Los tres marcos que sigue este libro coinciden en la ecuación base, pero se diferencian en qué ofrecen. Esta sección resume el aporte de cada uno y propone un flujo común para una ciudad de Colombia.

## La ecuación común

CLIMAAX y CCDR-tools expresan el riesgo como el producto de amenaza, exposición y vulnerabilidad {cite:p}`climaax2025handbook,ccdr2025tools`. CCDR-tools añade que el riesgo está atado a la probabilidad, de modo que también puede leerse como probabilidad por impacto {cite:p}`ccdr2025tools`. Es la misma idea del Atlas de Riesgo de Colombia ({cite:p}`ungrd2019atlas`; ver [](../01_conceptos/11_marco_riesgo.md)).

## Qué aporta cada marco

| Marco | Qué es | Qué se toma en este libro |
|---|---|---|
| **CLIMAAX** {cite:p}`climaax2025handbook,bachmann2026climaax` | Marco de cinco pasos para evaluaciones regionales de riesgo climático, con flujos de trabajo en cuadernos | El proceso participativo y el orden de los pasos |
| **CCDR-tools** {cite:p}`ccdr2025tools` | Herramientas en Python para tamizaje de riesgo a escala nacional o subnacional, con datos globales | La combinación espacial amenaza–exposición–vulnerabilidad y los indicadores estandarizados |
| **CLIMADA** {cite:p}`climada2025docs` | Marco de código abierto para evaluar riesgo climático y valorar medidas de adaptación | El cálculo de impacto por evento, las métricas de riesgo y la comparación de medidas |

## Los cinco pasos de CLIMAAX

El marco de CLIMAAX es un ciclo iterativo de cinco pasos: alcance (*scoping*), exploración del riesgo, análisis del riesgo, evaluación de riesgos clave, y monitoreo y evaluación {cite:p}`climaax2025handbook`. Su meta es informar la gestión del riesgo climático.

1. **Alcance.** Define objetivos, contexto, actores y quién es dueño de cada riesgo.
2. **Exploración.** Con lo anterior, lista las amenazas relevantes y decide qué flujos de trabajo y escenarios usar.
3. **Análisis.** Aplica los flujos de trabajo y estima el riesgo.
4. **Riesgos clave.** Prioriza entre los riesgos individuales.
5. **Monitoreo y evaluación.** Hace seguimiento de las tendencias.

El análisis del riesgo, a su vez, tiene cuatro pasos: preparar la aplicación, elegir y acceder a los datos, estimar la amenaza y combinarla con exposición y vulnerabilidad {cite:p}`climaax2025handbook`. Estimar primero el riesgo actual sirve de línea base para seguir las tendencias {cite:p}`climaax2025handbook`.

```{note}
CLIMAAX fue diseñado para regiones de Europa y muchos de sus datos precalculados son europeos. El propio handbook permite reemplazarlos por datos locales {cite:p}`climaax2025handbook`, que es lo que hace este libro para Colombia.
```

## Combinación espacial de los tres componentes

CCDR-tools describe el cálculo en dos pasos sobre capas ráster {cite:p}`ccdr2025tools`:

1. **Intersección amenaza–exposición.** Superponer la capa de amenaza con la de exposición (activos construidos, población) define la zona expuesta y la cantidad de activos dentro de ella.
2. **Vulnerabilidad.** Un modelo específico para cada combinación de amenaza y categoría expuesta convierte la intensidad en una fracción del valor del activo que se pierde.

Si no existe un modelo de vulnerabilidad, CCDR-tools calcula la **exposición** a clases o umbrales de amenaza en lugar del daño {cite:p}`ccdr2025tools`. Esto es útil para amenazas con un índice determinista, como los movimientos en masa.

## Flujo propuesto para una ciudad

Este es el orden de trabajo que seguirán los capítulos de amenaza y las aplicaciones.

1. **Alcance.** Área de estudio, escala, decisiones que apoyará el análisis y actores.
2. **Inventario de amenazas.** Cuáles de las del capítulo 3 aplican a la ciudad, según su localización y la historia de eventos.
3. **Datos.** Amenaza, exposición y vulnerabilidad, con preferencia por datos locales sobre globales.
4. **Línea base.** Riesgo actual por amenaza (PAE o exposición a umbrales). Ver [](22_probabilista_pae.md).
5. **Escenarios.** Cambio de la amenaza hidrometeorológica y de la exposición. Ver [](23_escenarios_climaticos.md).
6. **Síntesis y medidas.** Comparación entre amenazas y medidas por proceso de la Ley 1523 {cite:p}`ley1523`.

## Pendiente

- Verificar en la documentación de CLIMADA qué módulos usa para la valoración de medidas de adaptación y citarlos con precisión.
- Describir con más detalle los pasos de alcance y exploración de CLIMAAX con su guía de preguntas.
