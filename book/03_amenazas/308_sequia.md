---
title: Sequía
---

# Sequía

Este capítulo sigue el molde de siete puntos ([](_molde.md)). La sequía es una amenaza lenta cuya evaluación probabilista es poco común, y por eso este capítulo se apoya en el Atlas, en el capítulo de sequía agrícola de la serie 2021 y en el flujo de CLIMAAX de sequía relativa.

## 1. Fenómeno

La sequía se origina por un déficit de lluvias durante un periodo extendido, que produce escasez de agua para alguna actividad o sector. Sus impactos resultan de la interacción entre el evento natural (menos lluvia de la esperada) y la demanda de agua, que las actividades humanas suelen agravar {cite:p}`ungrd2019atlas`. Es una amenaza lenta: poco notoria al comienzo, con efectos que pueden extenderse mucho tiempo {cite:p}`ungrd2019atlas`.

### Tipos de sequía

Una sola definición no sirve en todas las circunstancias, porque lo que es sequía en un lugar puede no serlo en otro {cite:p}`ungrd2019atlas`. El Atlas y CLIMAAX coinciden en separarla por el sistema afectado {cite:p}`ungrd2019atlas,climaax2025handbook`:

| Tipo | Qué se afecta | Escala de tiempo |
|---|---|---|
| **Meteorológica** | Déficit de precipitación, agravado por evaporación y calor | Corto plazo, puede empezar y terminar rápido |
| **Agrícola** | Humedad del suelo, biomasa y rendimiento de cultivos | Mediano plazo |
| **Hidrológica** | Caudales, embalses, humedales, aguas subterráneas | Largo plazo, tarda más en desarrollarse |
| **Socioeconómica** | Relación entre oferta y demanda de agua de las comunidades | Según la demanda |

La cascada entre tipos depende de la severidad, la duración y la distribución espacio–temporal del evento {cite:p}`climaax2025handbook`. Además, la sequía puede ser **estacional** (cada año por la misma época) o **contingente** (inesperada, cuando normalmente llueve) {cite:p}`ungrd2019atlas`.

### Sequía en Colombia

Su intensidad y extensión están estrechamente ligadas al fenómeno El Niño. Los eventos generalizados de sequía suelen asociarse con El Niño de intensidad moderada a fuerte {cite:p}`ungrd2019atlas`. El Atlas recuerda varios casos: el de 1982–1983, el más fuerte de 1997–1998, el de 1991–1992 que contribuyó al apagón de 1992 y el de 2014–2016, con déficit de lluvias en las temporadas lluviosas de las regiones Caribe y Andina {cite:p}`ungrd2019atlas`.

También puede haber sequía por confluencia de temperaturas muy cálidas, baja humedad y vientos fuertes que aumentan la evapotranspiración y secan el suelo, sin que la falta de lluvia sea la única causa {cite:p}`ungrd2019atlas`.

**Variable de intensidad.** Depende del índice: déficit de precipitación, índice estandarizado de precipitación (SPI), humedad del suelo, caudal. No existe un índice universal {cite:p}`ungrd2019atlas`.

### Definición según los HIPs de UNDRR

Los perfiles de información de amenazas ([](../01_conceptos/16_hips_undrr.md)) que corresponden a este capítulo son:

| Código | Perfil (clúster) | Definición (traducción propia) |
|---|---|---|
| MH0401 | Sequía (meteorológico e hidrológico, precipitación) | Período de tiempo anormalmente seco, caracterizado por una deficiencia prolongada de precipitación por debajo de cierto umbral, sobre un área grande y durante más de un mes (OMM, 2023). |

Fuente: {cite:p}`undrr2025hips`.

**Qué se incluye y por qué.**

- **Se incluye, pero solo como definición meteorológica.** El perfil habla únicamente de déficit de precipitación; no cubre los demás tipos de sequía del capítulo (agrícola, hidrológica, socioeconómica), que se apoyan en el Atlas y en CLIMAAX. El capítulo mantiene su clasificación por sistema afectado y usa el perfil como punto de partida.
- **Umbral y duración.** La definición no fija un umbral numérico (lo deja «por debajo de cierto umbral») y pide más de un mes; el capítulo, siguiendo al Atlas, subraya que no hay un índice universal.
- **No se incluye la desertificación (EN0206),** que los HIPs definen como degradación de la tierra en zonas áridas, semiáridas y subhúmedas secas; es un proceso distinto.
- **Cascadas.** Los HIPs registran la sequía como causa de incendios, entre otros efectos {cite:p}`undrr2025hips`; ver [](310_incendios.md).

## 2. Amenaza

### Índices

Los índices describen anomalías meteorológicas e hidrológicas, pero no hay consenso sobre cuál representa mejor la posibilidad de impactos significativos en un sector {cite:p}`ungrd2019atlas`. Para el cálculo hay que definir el comienzo, la severidad y el final de las sequías {cite:p}`ungrd2019atlas`.

En ecosistemas cercanos al ecuador hay periodos muy cálidos con poca lluvia, donde un índice que use solo precipitación, como el SPI, puede no ser suficiente. Un estudio colombiano ajusta el SPI para evaluar la sequía por esa razón {cite:p}`cerpareyes2022adjustment`. Otro caracteriza eventos de sequía integral del Valle del Cauca durante la fase cálida de ENSO con un índice sintetizado de temperatura superficial, vegetación y precipitación, validado con el SPI de tres meses en 78 estaciones, con correlaciones de 0,55 a 0,71 {cite:p}`ojedaflechas2020characterization`.

### Enfoque probabilista

El Atlas lo describe así {cite:p}`ungrd2019atlas`:

1. Se generan eventos regionales de sequía que aún no han ocurrido, combinando déficit de lluvias con altas temperaturas durante un periodo prolongado.
2. Se identifican las sequías con índices que definen duración, severidad e intensidad.
3. Se obtienen mapas de amenaza por escenario y mapas de amenaza integrada, que comparan intensidades según el periodo de retorno.

Con la amenaza integrada se clasifica la región por severidad, duración y frecuencia, y se priorizan intervenciones y usos del suelo {cite:p}`ungrd2019atlas`.

```{important}
El Atlas afirma que Colombia no cuenta con una evaluación de la amenaza de sequía en sentido estricto, y que la evaluación probabilista del riesgo de sequía es poco común por la complejidad de modelar la amenaza y su interacción con los sistemas socioecológicos {cite:p}`ungrd2019atlas`. Esto es de 2019; hay que verificar si cambió.
```

### Método de CLIMAAX

El flujo de sequía relativa estima la amenaza como la probabilidad de exceder la mediana de los déficits severos de precipitación de una región, para un periodo de referencia o de proyección, con precipitación mensual por unidad territorial {cite:p}`climaax2025handbook`. Su resultado es un mapa de riesgo relativo, no pérdidas absolutas. Sigue la metodología global de Carrão et al. (2016) y calcula el riesgo como producto de amenaza, exposición y vulnerabilidad {cite:p}`climaax2025handbook`.

## 3. Exposición

La exposición es la distribución espacial de la sequía frente a los sistemas que puede impactar: cultivos, ganado, humedales, población y usos industriales del agua {cite:p}`climaax2025handbook`. CLIMAAX usa un modelo no compensatorio que considera la distribución de cultivos y ganadería, la competencia por el agua y la necesidad humana directa {cite:p}`climaax2025handbook`.

El Atlas incluye mapas de **índice de vulnerabilidad por disponibilidad de agua** y de **índice de escasez**, para año seco y año medio {cite:p}`ungrd2019atlas`. Son la base nacional para esta exposición.

## 4. Vulnerabilidad

En sequía, la vulnerabilidad es la de los medios de vida, más que la de lo construido. La sequía no daña edificaciones, pero degrada los medios de subsistencia (agua y cultivos) y con ello aumenta la vulnerabilidad y el riesgo de la población expuesta {cite:p}`cardona2021sequia`.

- **Cultivos.** Modelos de estrés hídrico estiman el efecto de la falta de agua en el crecimiento del follaje y el rendimiento {cite:p}`ungrd2019atlas`.
- **Dimensión social.** Durante la sequía de 2012–2016 en La Guajira, la mortalidad infantil subió a 23,4 por mil, sobre todo en la comunidad wayuu. A escala municipal se encontró correlación positiva con hogares de bajos ingresos, falta de aseguramiento en salud, población indígena y otras condiciones {cite:p}`contreras2020the`.

## 5. Riesgo

La evaluación prospectiva con eventos estocásticos futuros permite estimar la reducción del rendimiento de cultivos, las pérdidas de ganado o la reducción de reservas, y de ahí los efectos secundarios como venta forzada de activos, menor seguridad alimentaria o menor producción de energía {cite:p}`ungrd2019atlas`. Los resultados sirven para diseñar protección financiera contra pérdidas agrícolas, hacer análisis costo–beneficio de estrategias de manejo (riego, reservas, semillas resistentes) y planear contingencias bajo escenarios de cambio climático {cite:p}`ungrd2019atlas`.

El capítulo de la serie 2021 presenta la metodología probabilista para el sector agrícola con un generador de clima estocástico, y la aplica al cultivo de maíz {cite:p}`cardona2021sequia`.

Un estudio sobre riesgo de sequía tropical combina datos abiertos de vulnerabilidad y amenaza en cuadrícula {cite:p}`nauditt2022evaluating`. Lo cito por el título; debe leerse para confirmar su alcance.

## 6. Clima

La sequía es sensible al clima por dos vías, la variabilidad (El Niño) y la tendencia. El Atlas señala que la variabilidad ligada a El Niño y las tendencias de cambio climático influyen en la presencia de sequías meteorológicas {cite:p}`ungrd2019atlas`. CCDR-tools anticipa una reducción del almacenamiento natural de agua en dos tercios del planeta {cite:p}`ccdr2025tools`, con la advertencia de la sección [](../02_metodologia/23_escenarios_climaticos.md) sobre su alcance mundial.

El flujo de CLIMAAX usa precipitación del conjunto de cinco modelos CMIP6 de ISIMIP 3b y las trayectorias SSP126, SSP370 y SSP585 para 2031–2060 y 2071–2100 {cite:p}`climaax2025handbook`.

## 7. Datos y medidas

### Datos

| Fuente | Qué ofrece | Referencia |
|---|---|---|
| IDEAM: Estudio Nacional del Agua (ENA 2014) | Ciclo hidrológico, cuencas, uso y calidad del agua, escenarios | {cite:p}`ungrd2019atlas` |
| IDEAM | Mapas de índices de escasez y vulnerabilidad por disponibilidad de agua | {cite:p}`ungrd2019atlas` |
| Comité Técnico Nacional del fenómeno de El Niño | IDEAM, DIMAR, SGC, DNP y Cancillería | {cite:p}`ungrd2019atlas` |

### Incertidumbres

- Ausencia de un índice universal {cite:p}`ungrd2019atlas`.
- Pocos estudios probabilistas de riesgo de sequía {cite:p}`ungrd2019atlas`.
- Los flujos de CLIMAAX trabajan a nivel de unidad territorial europea y requieren adaptación {cite:p}`climaax2025handbook`.

### Medidas según la Ley 1523

| Proceso | Medida | Referencia |
|---|---|---|
| Conocimiento | Mapas de amenaza integrada, seguimiento de El Niño | {cite:p}`ungrd2019atlas` |
| Reducción | Redes de riego, reservas, semillas resistentes, usos del suelo según la amenaza | {cite:p}`ungrd2019atlas` |
| Protección financiera | Herramientas de protección financiera contra pérdidas agrícolas | {cite:p}`ungrd2019atlas` |

## Pendiente

- Leer {cite:p}`nauditt2022evaluating`, {cite:p}`cerpareyes2022adjustment` y {cite:p}`ojedaflechas2020characterization` completos. Los dos últimos solo se conocen por su resumen.
- Añadir el caso urbano: desabastecimiento de acueductos y escasez en ciudades (ID 857, Bogotá), con las cifras del Estudio Nacional del Agua más reciente.
- Verificar si el IDEAM ya cuenta con una evaluación nacional de amenaza de sequía posterior a 2019.
