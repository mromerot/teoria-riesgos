---
title: Olas de calor
---

# Olas de calor

:::{image} ../../estilo/ilustraciones/calor.svg
:alt: Sol intenso sobre una casa con ondas de calor
:class: ilustracion
:width: 100%
:::

Este capítulo sigue el molde de siete puntos ([](_molde.md)). Es el que mejor ilustra la diferencia entre un marco hecho para Europa y una ciudad tropical: las definiciones de ola de calor de CLIMAAX dependen de percentiles climatológicos y de umbrales regionales, y en Colombia no hay una definición oficial adoptada en las fuentes revisadas.

```{important}
**Cobertura de fuentes.** El Atlas de Riesgo de Colombia no trata el calor. El capítulo se apoya en el flujo de olas de calor de CLIMAAX, en la sección de estrés térmico de CCDR-tools, en pocos estudios colombianos de la hoja de vigilancia y, desde noviembre de 2026, en un caso aplicado con datos abiertos reales: el cuaderno CRC002 de Cartagena {cite:p}`romero2026crc002` (ver [](#caso-cartagena)). Sigue siendo provisional: es un solo caso, con una sola estación y sin datos de salud.
```

## 1. Fenómeno

Una ola de calor se define por una temperatura máxima y mínima diaria que supera un umbral durante un tiempo mínimo. Las metodologías usan definiciones distintas {cite:p}`climaax2025handbook`. El impacto más claro es el sobrecalentamiento de las áreas urbanas: reduce el confort y amenaza la salud, sobre todo de poblaciones vulnerables, y acompaña a la sequía y a la escasez de agua {cite:p}`climaax2025handbook`.

CCDR-tools añade que la incomodidad térmica aumenta cuando el calor se asocia con humedad alta, que el estrés térmico puede causar deterioro a largo plazo y reducir la productividad y los ingresos, y que los eventos extremos aumentan la morbilidad y la mortalidad {cite:p}`ccdr2025tools`. La respuesta individual al calor varía con la condición médica, el estado físico, el peso, la edad y la situación económica {cite:p}`ccdr2025tools`.

**Variable de intensidad.** Temperatura máxima y mínima, o un índice que combine calor y humedad. CCDR-tools lista dos: la temperatura de globo y bulbo húmedo (WBGT), que considera la carga de trabajo y el efecto sobre la salud, y el Índice Universal de Clima Térmico (UTCI), más físico y que también cubre el estrés por frío {cite:p}`ccdr2025tools`.

### Calor en ciudades tropicales

Como criterio de método, en una ciudad tropical se debe distinguir entre ola de calor (anomalía respecto del clima local) y calor persistente propio del clima. La hoja de vigilancia muestra interés en Colombia por el calor extremo urbano y por sus efectos en salud; se ve en los dos estudios de abajo.

Un caso con datos reales confirma el criterio. En la estación del IDEAM del aeropuerto de Cartagena (2019–2026), la temperatura mínima diaria supera 24 °C en 92 % de los días, de modo que un umbral nocturno absoluto de ese valor no separa nada: la definición «Tmáx ≥ 35 °C y Tmín ≥ 24 °C» equivale en la práctica a «Tmáx ≥ 35 °C», que ocurre en 3,8 % de los días {cite:p}`romero2026crc002`. En un clima cálido todo el año, el umbral debe salir de la distribución local (por ejemplo, un percentil por día del año).

### Definición según los HIPs de UNDRR

Los perfiles de información de amenazas ([](../01_conceptos/16_hips_undrr.md)) que corresponden a este capítulo son:

| Código | Perfil (clúster) | Definición (traducción propia) |
|---|---|---|
| MH0501 | Ola de calor (meteorológico e hidrológico, temperatura) | Período marcado e inusual de tiempo caluroso sobre una región, que persiste al menos dos o tres días y noches consecutivos durante la época caliente del año según las condiciones climatológicas locales, con condiciones térmicas registradas por encima de umbrales dados (OMM y OMS, 2015). |

Fuente: {cite:p}`undrr2025hips`.

**Qué se incluye y por qué.**

- **Se incluye.** La definición deja los umbrales a la climatología local, lo que respalda el criterio del capítulo: para una ciudad colombiana el umbral debe fijarse con datos locales y no copiarse de Europa.
- **Distinguir ola de calor y calor persistente.** El perfil habla de un período «inusual» según el clima local; es coherente con la distinción que hace el capítulo entre anomalía y clima cálido normal.
- **No se incluye** la ola de calor marina (MH0708, IPCC 2019: temperatura superficial del mar extrema que persiste de días a meses), aunque puede ser relevante para los ecosistemas del Caribe; queda como tema por considerar.
- **Cascadas.** Los HIPs registran la ola de calor como causa de sequía e incendios {cite:p}`undrr2025hips`.

## 2. Amenaza

### Definiciones de ola de calor

CLIMAAX ofrece dos metodologías de amenaza, que difieren en datos de entrada, umbrales y algoritmo {cite:p}`climaax2025handbook`. A ellas se suma el percentil local del ETCCDI, que se usa en el Caribe colombiano:

| Método | Definición de ola de calor | Notas |
|---|---|---|
| **EuroHEAT** | Periodo de al menos dos días con la temperatura aparente máxima y la mínima sobre el percentil 90 de la distribución mensual, con base en 1971–2000 | Recomendado, porque usa varios modelos regionales |
| **Xclim** | Umbrales absolutos de temperatura máxima y mínima y duración mínima definidos por el usuario (por ejemplo, 2 o 3 días) | Usa un solo modelo regional. Los umbrales suelen ser regionales y basados en impactos esperados en salud |
| **Percentil local (ETCCDI)** | Racha de al menos 3 días (corta) o 5 (larga) con la temperatura máxima sobre el percentil 90 de cada día del año | Es la definición que usan Esteban-Cantillo et al. en San Andrés, Providencia y Santa Catalina {cite:p}`cantillo2024historical`, dentro de la familia de índices TX90p y duración de rachas cálidas {cite:p}`avila2023current` |

El método de percentil local es el que mejor se adapta a un clima sin estación caliente definida, porque no exige copiar un umbral de otra región. Los dos métodos de CLIMAAX usan proyecciones EURO-CORDEX con resolución de 12 × 12 km, que **no tienen en cuenta la isla de calor urbana** y por eso no sirven para evaluar el riesgo dentro de las ciudades {cite:p}`climaax2025handbook`.

```{warning}
Para Colombia no hay un equivalente directo de EURO-CORDEX en las fuentes revisadas. Un análisis urbano necesita estaciones del IDEAM, proyecciones con reducción de escala o datos satelitales, con umbrales definidos localmente. El caso de Cartagena probó tres rutas abiertas, sin credenciales {cite:p}`romero2026crc002`:

- **Estaciones del IDEAM** en datos.gov.co (temperatura máxima y mínima, temperatura y humedad relativa horarias; la estación de Rafael Núñez empieza en septiembre de 2019): sirven como ancla, pero son series cortas y con huecos (26 % de los días sin datos suficientes).
- **NEX-GDDP-CMIP6** (proyecciones diarias de 0,25°, 35 modelos): se obtiene el punto de interés por OPeNDAP del servidor THREDDS de la NASA, sin descargar los archivos completos.
- **ERA5-Land** no sustituye a la estación en una celda costera: en el aeropuerto de Cartagena subestima la Tmáx en promedio 2,3 °C, con correlación diaria de 0,15.
```

### Compuestos

El calor extremo se combina con sequía. En la cuenca del Orinoco, un estudio de extremos secos y cálidos compuestos analiza sus implicaciones para los incendios {cite:p}`arias2025compound`. Ver [](310_incendios.md).

## 3. Exposición

La exposición a calor se mide con la temperatura de superficie. En el flujo de riesgo local de CLIMAAX, la exposición proviene de la temperatura de superficie terrestre de Landsat 8 (30 × 30 m, periodo 2013–2021, cada 16 días), con la limitación de datos faltantes los días nublados {cite:p}`climaax2025handbook`. En una ciudad andina o amazónica, la nubosidad frecuente es un problema práctico para esta fuente.

En Cartagena, un compuesto de siete años de escenas Landsat 8 y 9 (228 escenas, 168 fechas válidas por píxel en la mediana) con la cobertura de ESA WorldCover mostró que la superficie construida tiene una LST de las 10:30 de la mañana de 44,5 °C en la mediana, frente a 36,9 °C de las zonas arboladas: +6,1 °C en la media y +3,9 °C en el percentil 90 sobre una referencia vegetada no urbana. A escala de 300 m, cada 10 % más de superficie construida se asocia con +0,71 °C en la LST media y cada 10 % más de arbolado con −0,68 °C en el percentil 90 {cite:p}`romero2026crc002`.

## 4. Vulnerabilidad

La vulnerabilidad se representa con los grupos de población vulnerable: personas mayores de 65 años y menores de 5, con datos WorldPop de 100 × 100 m para 2020 {cite:p}`climaax2025handbook`. Es una aproximación gruesa; el censo del DANE permite una mejor para Colombia. Una advertencia práctica: las estructuras por edad y sexo de WorldPop pesan unos 0,5 GB por grupo de edad para Colombia y el servidor no admite descargas parciales, de modo que en el caso de Cartagena no se usaron y la vulnerabilidad por edad quedó pendiente del censo por manzana {cite:p}`romero2026crc002`.

La evidencia en salud pública recogida en una revisión narrativa colombiana indica que las mujeres embarazadas tienen mayor riesgo de parto prematuro con altas temperaturas, y que adultos y niños pueden tener mayor riesgo de deshidratación. La revisión plantea la necesidad de un sistema de alerta temprana como política de salud pública {cite:p}`salazarceballos2025sistema`.

## 5. Riesgo

CLIMAAX usa una **matriz de riesgo 10 + 10** que cruza exposición (diez clases de temperatura de superficie) y vulnerabilidad (diez intervalos de población vulnerable). Las clases van de «muy bajo», con menos de 20–25 °C, a «muy alto», con más de 55 °C, y se pueden cambiar según el área {cite:p}`climaax2025handbook`. El nivel de riesgo es **relativo** al área elegida: solo refleja diferencias entre las zonas analizadas {cite:p}`climaax2025handbook`. El caso de Cartagena adaptó la matriz a rangos percentiles de amenaza (LST), exposición (población por celda de 100 m) y una vulnerabilidad parcial, y probó que la clasificación es estable ante la fórmula: cinco variantes mantuvieron una correlación de Spearman de 0,93 o más con la base {cite:p}`romero2026crc002`.

Un estudio de la hoja sobre el efecto de los bosques urbanos en la exposición al calor extremo en una ciudad tropical vulnerable (Bogotá, ID 644) queda por leer {cite:p}`giraldocharria2025urban`.

## 6. Clima

El calor es muy sensible al clima. CCDR-tools anticipa que el aumento de temperatura agravará las consecuencias del estrés térmico sobre la salud y la producción agrícola, en particular en países tropicales con baja capacidad de adaptación {cite:p}`ccdr2025tools`. Para la ola de calor de diciembre de 2022 en el sur de Sudamérica, un estudio de atribución concluye, por su título, que fue 60 veces más probable por el cambio climático {cite:p}`rivera20232022`; es una región distinta de Colombia, y se cita como ejemplo de método de atribución.

CLIMAAX compara los escenarios RCP4.5 y RCP8.5 para un periodo de referencia (1971–2000) y tres periodos futuros {cite:p}`climaax2025handbook`; ver [](../02_metodologia/23_escenarios_climaticos.md).

Con cinco modelos de NEX-GDDP-CMIP6, el porcentaje de días con Tmáx sobre el percentil 90 de 1985–2014 en la celda del aeropuerto de Cartagena pasa de 10 % a una mediana de 50 % hacia 2061–2080 bajo SSP2-4.5, 63 % bajo SSP3-7.0 y 78 % bajo SSP5-8.5; los días con Tmáx ≥ 35 °C, anclados a la estación, pasan de unos 14 al año a 95, 153 y 189 respectivamente {cite:p}`romero2026crc002`. Esas cifras describen una celda de 25 km, no diferencias entre barrios.

## 7. Datos y medidas

### Datos

| Fuente | Qué ofrece | Referencia |
|---|---|---|
| Landsat 8 | Temperatura de superficie a 30 m | {cite:p}`climaax2025handbook` |
| WorldPop | Población por grupos de edad | {cite:p}`climaax2025handbook` |
| Conjuntos de estrés por calor | WBGT, UTCI, índices de calor y humedad (resoluciones de 10 a 30 km) | {cite:p}`ccdr2025tools` |
| IDEAM, estaciones locales | Temperatura máxima, mínima, horaria y humedad relativa en datos abiertos (datos.gov.co: conjuntos ccvq-rp9s, afdg-3zpb, sbwg-7ju4 y uext-mhny); la estación de Cartagena empieza en 2019 | {cite:p}`ideam2026temperaturas` |
| NEX-GDDP-CMIP6 | Tmáx y Tmín diarias proyectadas, 0,25°, 1950–2100 | {cite:p}`thrasher2022nex` |
| ERA5-Land | Reanálisis de 9 km; sesgo frío en celdas costeras | {cite:p}`munoz2021era5land` |
| ESA WorldCover | Cobertura del suelo a 10 m para explicar la LST | {cite:p}`zanaga2022worldcover` |

### Incertidumbres

- Datos de proyección a 12 km sin efecto de isla de calor {cite:p}`climaax2025handbook`.
- La temperatura de superficie no es la temperatura del aire que determina el estrés fisiológico.
- Falta una definición de ola de calor para Colombia; el percentil local es una alternativa defendible, pero no oficial.
- Las proyecciones de un solo punto heredan un sesgo del modelo respecto de la estación (en Cartagena, de 0,2 a 0,8 °C en la mediana de la Tmáx y de 0,8 a 1,2 °C en el percentil 90), que el umbral relativo evita y el absoluto solo corrige anclando a la estación {cite:p}`romero2026crc002`.
- Con pocos años de estación, la referencia absoluta hereda la variabilidad interanual (de 3 a 21 días al año con Tmáx ≥ 35 °C en Cartagena).

### Medidas según la Ley 1523

| Proceso | Medida | Referencia |
|---|---|---|
| Conocimiento | Sistema de alerta temprana para altas temperaturas y olas de calor | {cite:p}`salazarceballos2025sistema` |
| Reducción | Infraestructura verde urbana, como los bosques urbanos que reducen la exposición | {cite:p}`giraldocharria2025urban` (por título) |
| Manejo | Atención en salud a grupos vulnerables | {cite:p}`salazarceballos2025sistema` |

(caso-cartagena)=
## Caso aplicado: Cartagena (CRC002)

El cuaderno CRC002 {cite:p}`romero2026crc002` aplica este capítulo a Cartagena de Indias con datos abiertos reales: la estación del IDEAM del aeropuerto, cinco modelos de NEX-GDDP-CMIP6 bajo SSP2-4.5, SSP3-7.0 y SSP5-8.5, Landsat 8 y 9, WorldCover, WorldPop y OpenStreetMap. Su primera versión usaba datos sintéticos; la auditoría que dio origen a la segunda versión dejó cuatro lecciones de método que valen para cualquier ciudad tropical.

| Lección | Qué se encontró en Cartagena | Qué implica para el capítulo |
|---|---|---|
| **El umbral nocturno absoluto no discrimina.** | Tmín ≥ 24 °C en 92 % de los días | Usar percentiles locales por día del año, no un número |
| **Un reanálisis puede no servir en la costa.** | ERA5-Land subestima la Tmáx 2,3 °C, con correlación diaria de 0,15 | Validar cada conjunto contra una estación antes de usarlo |
| **El sesgo del modelo se evita comparando contra su propio clima.** | Los cinco modelos quedan 0,2 a 0,8 °C sobre la estación en la mediana de la Tmáx | Percentil relativo por modelo; para umbrales absolutos, anclar a la estación por cambio de cuantiles |
| **Los datos sintéticos producen conclusiones circulares.** | El mapa de isla de calor de la versión 1 reproducía los puntos calientes que el propio código dibujó | Rotular los datos inventados y no leer su salida como hallazgo |

**Resultados de referencia** (celda de 25 km del aeropuerto; mediana de cinco modelos):

| Escenario | % de días con Tmáx sobre el P90 de 1985–2014 | Días con Tmáx ≥ 35 °C al año (anclados a la estación) |
|---|---|---|
| Estación 2019–2026 | — | 14 |
| SSP2-4.5, 2061–2080 | 50 | 95 |
| SSP3-7.0, 2061–2080 | 63 | 153 |
| SSP5-8.5, 2061–2080 | 78 | 189 |

En un clima sin estación caliente definida, la «ola de calor» pasa a ser la condición típica hacia fin de siglo en el escenario más cálido: el percentil de 1985–2014 sigue sirviendo para medir el cambio, pero deja de describir un evento excepcional. Para el nivel intraurbano, la superficie construida de Cartagena es 6,1 °C más caliente en la media (3,9 °C en el percentil 90) que una referencia vegetada, y el Humidex máximo diario observado supera 45 (categoría «peligroso» de Environment Canada, por verificar contra el original {cite:p}`masterton1979humidex`) en 46 % de los días. El caso deja pendientes la vulnerabilidad por edad y condiciones sociales, la función de impacto y las proyecciones de humedad.

## Síntesis de evidencia

```{note}
**Método.** Síntesis narrativa por tipo de evidencia (no un metaanálisis con efectos agrupados: los estudios usan diseños, escalas y variables que no se pueden combinar en un solo estimador). Se leyeron los resúmenes de los artículos de la hoja de vigilancia que están en la carpeta de PDFs; las cifras vienen de esos resúmenes y **faltan por verificar contra el texto completo**.
```

- {cite:t}`salazarceballos2025sistema` propone, en Colombia, un sistema de alerta temprana para altas temperaturas y olas de calor como política de salud pública. Se lee aquí solo el título y el inicio del documento, que es una versión anticipada sin edición final.

- {cite:t}`bustos2024observation` analiza 30 años de temperatura superficial diaria y proyecciones de 19 modelos CMIP6 para las olas de calor marinas en el Caribe, un fenómeno poco estudiado; en 1983–2012 hubo tendencias significativas de la frecuencia (1,32 eventos por década y nodo).

- {cite:t}`cantillo2024historical` analiza siete estaciones (década de 1960 a 2020) y proyecciones CMIP6 de 2071 a 2100 para las islas de San Andrés, Providencia y Santa Catalina; según el resumen, las olas de calor se triplicaron en frecuencia y duplicaron su duración máxima desde finales de los años ochenta, y los días calurosos aumentan entre 60 % y 89 % hacia fin de siglo en los cuatro escenarios SSP evaluados. Definen la ola de calor con el percentil 90 de la temperatura máxima. (Cifras del resumen, por verificar contra el texto completo.)

- {cite:t}`avila2023current` evalúa modelos de alta resolución con los índices del ETCCDI para América Latina y el Caribe entre 1981 y 2014 y proyecta cambios de 2021 a 2050 bajo SSP5-8.5; según el resumen, no hay evidencia clara de que una mayor resolución mejore el desempeño en los extremos y hay consenso en el aumento de los extremos de temperatura.

**Lectura conjunta.** La evidencia nacional sobre olas de calor es escasa (confianza baja), por lo que el capítulo sigue siendo provisional. Las olas de calor marinas del Caribe se suman como una variante a considerar para ciudades costeras.

## Pendiente

- Leer {cite:p}`giraldocharria2025urban` y {cite:p}`rivera20232022` completos.
- Probar el percentil local de ola de calor en otras ciudades colombianas y con series más largas del IDEAM (la de Cartagena empieza en 2019).
- Incorporar los datos sociales por manzana del censo DANE 2018 para la vulnerabilidad al calor, que el caso de Cartagena dejó pendiente.
- Buscar o construir una función de impacto del calor (mortalidad o atención en salud) validada para Colombia; sin ella no se calcula la pérdida anual esperada.
- Buscar literatura de isla de calor urbana en Bogotá, Medellín, Cali y Barranquilla.

## Bibliografía recomendada

Lista de los 8 registros de la hoja de vigilancia científica (pestaña `Vigilancia_CTeI`, columna `AMENAZA_ESPECIFICA` = «Ola de calor»), en formato APA 7 con metadatos de Crossref. Son lecturas recomendadas: **no están verificadas contra el texto completo** ni se usan como evidencia hasta que se citen en el capítulo. Las entradas sin DOI carecen de autores en la hoja.

- Arias, P. A., Fernández-Berrío, A., Bedoya-Pineda, V., Acevedo-Ortiz, M. Y., & Martínez, J. A. (2025). Compound dry and hot extremes and their implications for fire activity over the Orinoco River Basin in northern South America. *Climate Dynamics*, *63*(4), 175. https://doi.org/10.1007/s00382-025-07660-5

- Bustos Usta, D. F., Torres Parra, R. R., Rodríguez-López, L., Castillo Alvarez, M., & Bourrel, L. (2024). Observation and Projection of Marine Heatwaves in the Caribbean Sea from CMIP6 Models. *Remote Sensing*, *16*(13), 2357. https://doi.org/10.3390/rs16132357

- Cuartas, J., Narea, M., Ahun, M., & Vergunst, F. (2026). Prenatal and Early Childhood Ambient Heat Exposure and Developmental Outcomes: A Systematic Review. *Clinical Child and Family Psychology Review*, *29*(3), 493-505. https://doi.org/10.1007/s10567-026-00569-3

- Giraldo-Charria, D. L., Escobedo, F. J., Clerici, N., & Quesada, B. (2025). Urban forests mitigate extreme heat exposure in a vulnerable tropical city. *Urban Climate*, *59*, 102311. https://doi.org/10.1016/j.uclim.2025.102311

- Palacios-Gutiérrez, A., Valencia-Delfa, J. L., & Villeta, M. (2025). Identification of extreme temperature and precipitation patterns in Spain based on multiscale analysis of time series. *Natural Hazards*, *121*(7), 7991-8009. https://doi.org/10.1007/s11069-024-07082-2

- Rivera, J. A., Arias, P. A., Sörensson, A. A., Zachariah, M., Barnes, C., Philip, S., Kew, S., Vautard, R., Koren, G., Pinto, I., Vahlberg, M., Singh, R., Raju, E., Li, S., Yang, W., Vecchi, G. A., Harrington, L. J., & Otto, F. E. L. (2023). 2022 early-summer heatwave in Southern South America: 60 times more likely due to climate change. *Climatic Change*, *176*(8), 102. https://doi.org/10.1007/s10584-023-03576-3

- Salazar-Ceballos, A., & Álvarez-Miño, L. (2025). Sistema de alerta temprana para altas temperaturas y olas de calor: la necesidad de una política de salud pública en Colombia. *Biomédica*, *45*(Sp. 2), 7-16. https://doi.org/10.7705/biomedica.7934

- Zhou, W., Melack, J. M., MacIntyre, S., Amaral, J. H. F., & Barbosa, P. M. (2026). Conditions leading to exceptionally high temperatures in shallow tropical lakes. *Limnology and Oceanography*, *71*(6), e70415. https://doi.org/10.1002/lno.70415
