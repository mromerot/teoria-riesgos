---
title: Escenarios climáticos y cambio de la amenaza
---

# Escenarios climáticos y cambio de la amenaza

## Para qué sirven los escenarios

Un escenario es una herramienta de planificación para explorar situaciones del tipo «qué pasa si» {cite:p}`climaax2025handbook`. En una evaluación de riesgo climático los escenarios cubren el clima y el desarrollo socioeconómico, por ejemplo lluvias, tendencias demográficas o precios. CLIMAAX da tres razones para explorar varios {cite:p}`climaax2025handbook`:

- **Mapear futuros distintos** y probar estrategias flexibles.
- **Guiar la adaptación**, con opciones de bajo arrepentimiento que sirven sea cual sea el futuro.
- **Evitar la maladaptación**, es decir, no invertir de más ni de menos.

Lo ideal es analizar todas las combinaciones de escenarios, pero en la práctica se usan pocas. La estrategia resultante se prueba después contra otros futuros posibles para ver si resiste {cite:p}`climaax2025handbook`. El escenario que se priorice depende de la tolerancia al riesgo de quien decide, y el desarrollo de escenarios debe ser lo más simple y transparente posible {cite:p}`climaax2025handbook`.

## Cómo cambia el riesgo con el clima

El clima puede aumentar el riesgo de dos maneras: cambiando la frecuencia, la intensidad y la distribución geográfica de las amenazas relacionadas con el tiempo, y afectando la vulnerabilidad y la exposición {cite:p}`ccdr2025tools`. CCDR-tools resume lo que espera el IPCC AR6 {cite:p}`ccdr2025tools`:

| Amenaza | Cambio esperado según CCDR-tools |
|---|---|
| Tormentas e inundaciones | El ciclo del agua se intensifica con el calentamiento |
| Aumento del nivel del mar | Las inundaciones costeras podrían amenazar activos de hasta 20 % del PIB mundial hacia 2100 |
| Estrés por calor | Más temperatura, con efectos en salud y agricultura, sobre todo en países tropicales con baja capacidad de adaptación |
| Sequías | Reducción del almacenamiento natural de agua en dos tercios del mundo |
| Ciclones tropicales | Aumento robusto de los más devastadores, aunque la atribución es difícil |

```{warning}
Estas cifras son un resumen de CCDR-tools sobre el IPCC AR6, de alcance mundial. Antes de usarlas para una ciudad de Colombia hay que contrastarlas con los escenarios del IDEAM y con los resultados regionales del AR6. Quedan pendientes de verificar contra la fuente primaria.
```

## Índices climáticos

CCDR-tools calcula índices climáticos con proyecciones CMIP6 para el nivel subnacional que se elija {cite:p}`ccdr2025tools`. El cambio de un índice frente a la línea base permite inferir cambios en la frecuencia e intensidad de la amenaza. Algunos ejemplos {cite:p}`ccdr2025tools`:

| Índice | Descripción | Amenaza relacionada |
|---|---|---|
| CWD | Días húmedos consecutivos (días/mes) | Inundación, deslizamiento |
| R20mm | Días con lluvia mayor a 20 mm | Inundación, deslizamiento |
| Rx5day | Precipitación máxima en cinco días (mm) | Inundación, deslizamiento |
| R99p | Días de precipitación extremadamente húmedos | Inundación, deslizamiento |

## Escenarios socioeconómicos y de emisiones

La literatura recomendada por CLIMAAX para los escenarios combina trayectorias de emisiones y trayectorias socioeconómicas compartidas (SSP) {cite:p}`riahi2017ssp,climaax2025handbook`. Las trayectorias SSP describen distintos desarrollos de la sociedad que se cruzan con los niveles de emisión.

## Del modelo a la estación: sesgo y umbral relativo

Las proyecciones con reducción de escala siguen teniendo sesgo respecto de una estación, sobre todo en celdas costeras. En el caso de Cartagena, cinco modelos de NEX-GDDP-CMIP6 quedaron entre 0,2 y 0,8 °C sobre la temperatura máxima mediana de la estación del IDEAM y entre 0,8 y 1,2 °C sobre su percentil 90 {cite:p}`romero2026crc002`. Hay dos salidas, cada una con su límite:

- **Umbral relativo:** el umbral sale de la climatología de cada modelo (por ejemplo, el percentil 90 de cada día del año en el periodo de referencia). El sesgo sistemático desaparece de la comparación, pero el resultado no tiene valor absoluto.
- **Umbral absoluto anclado a la estación:** a cada día observado se le suma el cambio por cuantil que proyecta el modelo entre la ventana de la estación y el periodo futuro. Da cifras comunicables (por ejemplo, días con 35 °C o más), pero hereda la variabilidad interanual de una serie corta.

Además, al reportar escenarios no se promedian trayectorias: la Tercera Comunicación Nacional sobre Cambio Climático promedió las cuatro RCP, y Arias et al. mostraron que ese promedio pierde escenarios alternos que importan para pensar futuros distintos {cite:p}`arias2022tercera`.

## Historias físicas de eventos (*storylines*)

Como alternativa cualitativa, CLIMAAX propone historias físicas de eventos {cite:p}`climaax2025handbook`. Esta aproximación representa la incertidumbre de los aspectos físicos del cambio climático sin asignarles probabilidades {cite:p}`shepherd2018storylines`. Es útil cuando se quiere explorar un evento extremo concreto, como una inundación o una sequía, en vez de una distribución completa.

## Qué hace cada capítulo de amenaza con esto

Cada capítulo del libro responde en su sexto punto (ver [](../03_amenazas/_molde.md)):

1. ¿Es la amenaza sensible al clima? Los sismos, volcanes y tsunamis de origen tectónico no lo son.
2. Si lo es, ¿qué índice o variable cambia y con qué fuente de proyecciones?
3. ¿Se mantiene la suposición de estacionariedad de la PAE? Si no, la PAE se calcula por periodos.

## Pendiente

- Incorporar los escenarios de cambio climático de Colombia (IDEAM, Tercera y Cuarta Comunicación Nacional) y sus datos de descarga.
- Verificar los valores de la tabla de CCDR-tools en el AR6 y añadir los resultados regionales para el norte de Sudamérica.
- Documentar cómo se elige el modelo CMIP6 y cómo se reduce de escala para ciudades.
