---
title: Evaluación probabilista y pérdida anual esperada
---

# Evaluación probabilista y pérdida anual esperada

## Por qué probabilista

Las pérdidas históricas explican el pasado, pero no son una buena guía del futuro porque la mayoría de los desastres posibles aún no ocurrieron {cite:p}`ccdr2025tools`. El enfoque probabilista simula esos eventos con base en evidencia científica: reproduce la física o la estadística del fenómeno y recrea la intensidad de muchos eventos sintéticos {cite:p}`ccdr2025tools`. Esto pesa sobre todo en Colombia para eventos poco frecuentes como los sismos y los tsunamis, de los que hay pocos registros históricos {cite:p}`ungrd2019atlas`.

| Enfoque | Qué modela | Cuándo se usa |
|---|---|---|
| **Probabilista** | Muchos eventos, cada uno con su frecuencia | Cuando se quiere la pérdida esperada y la variabilidad entre eventos frecuentes y raros |
| **Determinista** | Un escenario (medio, mediano o el peor caso) | Cuando solo hay un índice de amenaza o se prueba un evento concreto |

El enfoque determinista no representa el rango completo de variabilidad alrededor del escenario elegido {cite:p}`ccdr2025tools`.

## Cálculo del impacto por evento

En CLIMADA el impacto es el efecto combinado de los eventos de amenaza sobre un conjunto de exposiciones, mediado por un conjunto de funciones de impacto {cite:p}`climada2025docs`. El cálculo necesita tres objetos: exposición, amenaza y funciones de impacto. Entrega, entre otras salidas {cite:p}`climada2025docs`:

- `at_event`: el impacto de cada evento, sumado sobre todas las ubicaciones.
- `eai_exp`: el impacto anual esperado de cada ubicación, ponderado por la frecuencia de los eventos.
- `aai_agg`: el impacto anual promedio agregado sobre eventos y ubicaciones.

```{warning}
Antes de calcular, las coordenadas de la exposición deben corresponder con los centroides de la amenaza. CLIMADA busca el vecino más cercano de cada exposición, por lo que conviene usar resoluciones similares {cite:p}`climada2025docs`.
```

## La curva de excedencia y el impacto anual esperado

Con capas de amenaza por periodo de retorno, el impacto anual esperado (EAI) se calcula multiplicando el impacto de cada escenario por su probabilidad de excedencia y sumando {cite:p}`ccdr2025tools`. El área bajo la curva de excedencia es el daño anual total considerando todas las probabilidades.

CCDR-tools calcula la integral como una suma de Riemann y reporta tres valores {cite:p}`ccdr2025tools`:

- **Cota inferior (EAI_LB):** suma de rectángulos construidos por debajo de la curva.
- **Cota superior (EAI_UB):** suma de rectángulos construidos por encima.
- **EAI:** promedio de ambas cotas.

Sin función de vulnerabilidad se calcula la **exposición anual esperada (EAE)**: la exposición anual a una amenaza por encima de un umbral {cite:p}`ccdr2025tools`.

El Atlas de Riesgo de Colombia usa el mismo principio con otros nombres: la curva de excedencia de pérdidas, la pérdida anual esperada (PAE) y la pérdida máxima probable (PMP) {cite:p}`ungrd2019atlas`. La correspondencia es:

| Atlas {cite:p}`ungrd2019atlas` | CCDR-tools {cite:p}`ccdr2025tools` | CLIMADA {cite:p}`climada2025docs` |
|---|---|---|
| PAE | EAI | `aai_agg` (total) y `eai_exp` (por ubicación) |
| Curva de excedencia de pérdidas | Curva de probabilidad de excedencia | Curva de frecuencia de excedencia |
| PMP | Impacto por periodo de retorno | Impacto por periodo de retorno |

## Incertidumbre

Como la amenaza y el daño son inciertos, el Atlas pide tratarlos como variables aleatorias y propagar su dispersión, no solo el valor medio {cite:p}`ungrd2019atlas`. El handbook de CLIMAAX dedica una sección a las incertidumbres en los datos de exposición y vulnerabilidad {cite:p}`climaax2025handbook`.

## Límites que hay que declarar

- **Daños directos.** CCDR-tools estima solo pérdidas directas, mortalidad y daño a lo construido. Las pérdidas indirectas (caída de producción o ingresos) quedan fuera {cite:p}`ccdr2025tools`.
- **Estacionariedad.** La PAE supone que el proceso de ocurrencia de eventos no cambia en el tiempo {cite:p}`ungrd2019atlas`. Ver [](23_escenarios_climaticos.md).
- **Periodos de retorno.** No hay un estándar para elegirlos {cite:p}`ungrd2019atlas`. Cada capítulo de amenaza declara cuáles usa.

## Pendiente

- Verificar con el código de CLIMADA los nombres exactos de las clases y el método de curva de excedencia.
- Revisar la cita del handbook de CLIMAAX sobre incertidumbres (`CRA_steps/analysis/uncertainties.html`) y resumir sus recomendaciones.
