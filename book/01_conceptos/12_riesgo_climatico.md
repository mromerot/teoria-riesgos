---
title: Riesgo climático
---

# Riesgo climático

El riesgo climático es el riesgo de desastres visto hacia adelante: el clima cambia la amenaza, y el desarrollo cambia la exposición y la vulnerabilidad. Este capítulo explica cómo se incorpora esa mirada. El detalle de los escenarios está en [](../02_metodologia/23_escenarios_climaticos.md).

## 1. Tres vías por las que el clima cambia el riesgo

CCDR-tools resume que el cambio climático aumenta el riesgo de desastres de dos maneras: altera la frecuencia, la intensidad y la distribución geográfica de las amenazas relacionadas con el clima, y afecta la vulnerabilidad y los patrones de exposición {cite:p}`ccdr2025tools`. El riesgo se amplifica porque aumenta la amenaza y a la vez disminuye la resiliencia de hogares y comunidades {cite:p}`ccdr2025tools`. Por eso:

| Vía | Qué cambia | Ejemplo |
|---|---|---|
| **Amenaza** | Frecuencia, intensidad y distribución | Lluvias extremas, sequías, ascenso del nivel del mar |
| **Exposición** | Qué y cuánto hay en la zona de amenaza | Crecimiento urbano hacia laderas o costas ([](../04_vulnerabilidad/41_exposicion.md)) |
| **Vulnerabilidad** | Sensibilidad y capacidad de adaptación | Pobreza, salud, gobierno ([](../04_vulnerabilidad/43_vulnerabilidad_social.md)) |

## 2. Cambios esperados según CCDR-tools

CCDR-tools recoge los cambios principales que prevé el sexto informe del IPCC {cite:p}`ccdr2025tools`:

| Amenaza | Cambio esperado |
|---|---|
| Tormentas e inundación | El ciclo del agua se intensifica al calentarse el planeta |
| Aumento del nivel del mar | Los eventos de inundación costera podrían amenazar activos de hasta 20 % del PIB mundial hacia 2100 |
| Estrés por calor | Se agravan las consecuencias en salud y producción agrícola, en particular en países tropicales con baja capacidad de adaptación |
| Sequía | Gran reducción del almacenamiento natural de agua en dos tercios del mundo, sobre todo en el hemisferio sur |
| Ciclones tropicales | Aumento robusto de las tormentas más devastadoras, con hasta el doble de frecuencia bajo 2,5 °C de calentamiento |

Son cifras globales de una herramienta de síntesis. Cada capítulo de amenaza ([](../03_amenazas/index.md)) indica que hay que contrastarlas con el AR6 y con estudios colombianos antes de aplicarlas a una ciudad.

Los sismos y los volcanes no dependen del clima. Los movimientos en masa sí, de forma indirecta, porque la lluvia es uno de sus detonantes ([](../03_amenazas/304_mov_masa.md)).

## 3. Índices climáticos

CCDR-tools define los índices climáticos como medidas estandarizadas que resumen patrones del clima (temperatura, precipitación, presión). Las anomalías proyectadas respecto a un periodo base sirven para inferir cambios en la frecuencia e intensidad de las amenazas naturales {cite:p}`ccdr2025tools`.

| Índice | Descripción | Amenaza relacionada |
|---|---|---|
| CWD | Días húmedos consecutivos | Inundación, movimientos en masa |
| R20mm, Rx5day, R99p | Días con lluvia mayor a 20 mm, máximo en cinco días, días extremadamente húmedos | Inundación, movimientos en masa |
| slr | Ascenso del nivel del mar | Inundación costera |
| CDD, SPEI | Días secos consecutivos, índice estandarizado de precipitación y evapotranspiración | Sequía |
| WBGT, UTCI, tas, hi35 | Índices compuestos de calor, temperatura media, días con índice de calor mayor a 35 °C | Calor |

Fuente de la tabla: {cite:p}`ccdr2025tools`. Como las unidades difieren, CCDR-tools sugiere expresar las anomalías como porcentaje de cambio respecto de la variabilidad histórica cuando se necesite comparar o combinar índices {cite:p}`ccdr2025tools`.

## 4. Modelos y escenarios

Las proyecciones provienen de los modelos de CMIP6, que sustentan el sexto informe del IPCC y proyectan el clima con trayectorias socioeconómicas compartidas (SSP), que combinan emisiones con supuestos de desarrollo {cite:p}`ccdr2025tools,riahi2017ssp`. CCDR-tools ofrece los índices con estas dimensiones {cite:p}`ccdr2025tools`:

- **Escenarios:** SSP1-2.6, SSP2-4.5, SSP3-7.0 y SSP5-8.5.
- **Rango del ensamble:** percentiles p10, p50 y p90.
- **Periodos:** histórico (1981–2015) y cuatro futuros: 2020–2039, 2040–2059, 2060–2079 y 2080–2099.
- **Escala temporal:** mensual, estacional y anual.

Para planificación recomienda como escenarios principales SSP2-4.5 y SSP3-7.0, con SSP1-2.6 como límite optimista. Considera que SSP5-8.5 es útil como prueba de estrés, pero no como escenario habitual {cite:p}`ccdr2025tools`. Esa recomendación se apoya en el análisis de emisiones y en la evolución del protocolo de CMIP7; el libro la adopta como referencia por defecto y exige indicar el escenario en cada resultado.

```{note}
CLIMAAX usa en cambio las trayectorias RCP4.5 y RCP8.5 para sus proyecciones europeas {cite:p}`climaax2025handbook`. Al combinar flujos de ambos marcos, hay que dejar escrita la equivalencia de escenarios.
```

## 5. Cómo entra el clima en el cálculo

1. **Amenaza futura.** Se recalcula la amenaza con la anomalía del clima proyectado (por ejemplo, la precipitación extrema de periodo de retorno dado) y se repite el análisis probabilista ([](../02_metodologia/22_probabilista_pae.md)).
2. **Exposición y vulnerabilidad futuras.** Se proyectan con escenarios socioeconómicos, o se fijan de forma explícita en su valor actual para aislar el efecto del clima.
3. **Comparación.** Se reporta la PAE o el nivel de riesgo para cada combinación de escenario y periodo, junto con el caso histórico.

El punto 2 decide la interpretación: si exposición y vulnerabilidad se mantienen fijas, la diferencia es solo efecto climático; si cambian, es efecto combinado.

## 6. Incertidumbre

CLIMAAX distingue incertidumbres de los datos de entrada, de los modelos y de la comunicación de resultados, y recomienda declararlas {cite:p}`climaax2025handbook`. En el riesgo climático dominan tres:

- La **variabilidad natural** entre modelos y años, que el rango del ensamble (p10–p90) intenta cubrir {cite:p}`ccdr2025tools`.
- La **atribución débil** para algunas amenazas, como los ciclones tropicales {cite:p}`ccdr2025tools`.
- La **escala**: los modelos globales tienen resolución gruesa, y la isla de calor urbana o los efectos de ladera no aparecen sin reducción de escala (ver [](../03_amenazas/309_calor.md)).

## Pendiente

- Documentar la resolución y la reducción de escala de los productos disponibles para Colombia.
- Reunir proyecciones de cambio climático del IDEAM y estudios colombianos de la hoja de vigilancia, por amenaza.
- Verificar la tabla de cambios esperados contra el AR6 y la fuente primaria de la cifra de 20 % del PIB.
- Añadir la relación con El Niño–La Niña, que domina la variabilidad interanual en Colombia ([](../03_amenazas/308_sequia.md)).
