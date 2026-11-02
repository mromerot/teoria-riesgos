---
title: Síntesis multiamenaza
---

# Síntesis multiamenaza

Al final de un análisis urbano hay un resultado por amenaza, cada uno con su unidad y su método. Este capítulo explica qué operaciones son válidas entre ellos.

## 1. Tres tipos de resultado

CLIMAAX distingue tres salidas de un análisis de riesgo: un índice de riesgo (por ejemplo, de sequía), un daño económico (por ejemplo, de inundación costera) y una población expuesta {cite:p}`climaax2025handbook`. Los capítulos de amenaza de este libro producen esos mismos tipos:

| Tipo de resultado | Unidad | Amenazas que lo usan en este libro | Operación válida |
|---|---|---|---|
| **Pérdida probabilista** | Dinero por año (PAE) y pérdida con periodo de retorno | Sismo, inundación, ciclones, tsunami, volcanes ([](../02_metodologia/22_probabilista_pae.md)) | Sumar entre amenazas la PAE; comparar |
| **Exposición a clases o umbrales** | Elementos o personas dentro de una clase | Movimientos en masa, erosión | Contar y comparar; no convertir en dinero |
| **Riesgo relativo (zonificación)** | Clases de riesgo dentro del área | Incendios, sequía, calor | Ordenar dentro del área; no comparar entre ciudades |

## 2. Qué se puede combinar

La clasificación anterior es criterio de método de este libro. Tres reglas se desprenden de ella.

1. **La PAE se suma entre amenazas** porque es un valor esperado en la misma unidad, y el valor esperado de una suma es la suma de los valores esperados. El Atlas presenta una pérdida anual esperada multiamenaza, en millones de pesos y en ‰ del valor expuesto {cite:p}`ungrd2019atlas`. Para usarla hay que haber estimado todas las amenazas sobre el mismo inventario de exposición y con el mismo valor de reposición ([](../04_vulnerabilidad/41_exposicion.md)).
2. **La pérdida máxima probable no se suma.** Los eventos de periodo de retorno dado de amenazas distintas no ocurren a la vez. Sumar los PML de 500 años de cada amenaza sobrestima la pérdida de un solo año. El Atlas reporta el PML por amenaza para cada departamento {cite:p}`ungrd2019atlas`, y lo hace por separado.
3. **Un índice relativo no se mezcla con dinero.** Un mapa de clases de riesgo de incendio no puede sumarse a una PAE. Lo que sí se puede hacer es superponer mapas para ver coincidencias.

## 3. Probabilidad de excedencia

Los periodos de retorno se traducen a la probabilidad de ocurrencia en la vida útil o en un horizonte. El Atlas lo ilustra con tres pérdidas probables: la de 100 años tiene 39,4 % de probabilidad de ser superada en 50 años, la de 250 años 18 % y la de 500 años 10 % {cite:p}`ungrd2019atlas`. Presentar los tres umbrales junto a la PAE ayuda a que quien decide vea que un riesgo con PAE baja puede tener pérdidas máximas grandes (ver las islas en [](../03_amenazas/311_ciclones.md)).

## 4. Cascadas y eventos compuestos

Los análisis por amenaza asumen eventos independientes. En la realidad, un detonante activa varias amenazas ([](../03_amenazas/index.md)). La síntesis debe revisar al menos estas cadenas:

| Cadena | Dónde se trata |
|---|---|
| Sismo → tsunami, movimientos en masa, licuefacción | [](../03_amenazas/301_sismo.md), [](../03_amenazas/303_tsunami.md), [](../03_amenazas/304_mov_masa.md) |
| Lluvia intensa → inundación, movimientos en masa, erosión fluvial | [](../03_amenazas/305_inundacion.md), [](../03_amenazas/307_erosion_fluvial.md) |
| Ciclón → viento, marea de tormenta y lluvia | [](../03_amenazas/311_ciclones.md) |
| Sequía y calor → incendios | [](../03_amenazas/308_sequia.md), [](../03_amenazas/310_incendios.md) |

En el capítulo de calor se cita un estudio de extremos secos y cálidos compuestos en la cuenca del Orinoco {cite:p}`arias2025compound`. Como criterio de método, cuando no hay un modelo conjunto, la síntesis debe indicar qué cascadas no se cuantificaron en lugar de dar a entender que el riesgo total está completo.

## 5. Priorizar

El marco de CLIMAAX incluye un paso de evaluación de riesgos clave, donde se prioriza entre los riesgos individuales {cite:p}`climaax2025handbook`. Este libro no tiene una guía completa de ese paso (ver pendientes). Mientras se completa, la prioridad se justifica con cuatro preguntas que cada resultado debe responder:

1. ¿Qué tan grande es el impacto (PAE, pérdida máxima, personas expuestas)?
2. ¿Qué tan probable es (periodo de retorno)?
3. ¿Cuánto cambia con el clima futuro ([](../01_conceptos/12_riesgo_climatico.md))?
4. ¿Qué tan incierto es el resultado, y qué tanto depende de datos globales en lugar de locales?

Estas preguntas son criterio de método.

## 6. Comunicar y monitorear

CLIMAAX señala que estimar primero el riesgo actual sirve de línea base para seguir las tendencias en el paso de monitoreo y evaluación {cite:p}`climaax2025handbook`. Por eso cada informe debe guardar: la versión de los datos, el inventario de exposición, el escenario usado y la fecha. Los resultados de matriz o de zonificación son relativos al área estudiada ({cite:p}`climaax2025handbook`; ver [](../04_vulnerabilidad/43_vulnerabilidad_social.md)), y los informes deben decirlo.

## Pendiente

- Verificar cómo el Atlas agrega la PAE multiamenaza (suma directa o ajustes por traslape de eventos).
- Redactar una guía del paso de riesgos clave de CLIMAAX con sus criterios, tras leer el capítulo completo del handbook.
- Documentar el método de CLIMADA para combinar riesgos de varias amenazas sobre una misma exposición.
