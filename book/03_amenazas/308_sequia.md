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

## Síntesis de evidencia

```{note}
**Método.** Síntesis narrativa por tipo de evidencia (no un metaanálisis con efectos agrupados: los estudios usan diseños, escalas y variables que no se pueden combinar en un solo estimador). Se leyeron los resúmenes de los artículos de la hoja de vigilancia que están en la carpeta de PDFs; las cifras vienen de esos resúmenes y **faltan por verificar contra el texto completo**.
```

| Estudio | Diseño y lugar | Resultado relevante |
|---|---|---|
| {cite:t}`contreras2020the` | Correlación y regresión por pasos, municipios de La Guajira, sequía 2012–2016 | La mortalidad infantil subió a 23,4 por 1000; se asoció con ingreso bajo, falta de seguro de salud, población indígena, analfabetismo, vivienda rural y hogares con niños pequeños; no con la falta de fuente de agua. Tres variables explican el 90,4 % |
| {cite:t}`ojedaflechas2020characterization` | Índice sintético con imágenes de satélite y componentes principales, Valle del Cauca | Se validó con el SPI-3 de 78 estaciones (correlaciones de 0,55 a 0,71 en El Niño); se añadió un modelo de susceptibilidad municipal con proceso analítico jerárquico |
| {cite:t}`nauditt2022evaluating` | Riesgo de sequía con productos abiertos de amenaza y vulnerabilidad en cuadrículas, trópico | Muestra que se puede combinar datos globales abiertos de amenaza y vulnerabilidad |
| {cite:t}`scott2021ecosystem` | Comparación de seguridad hídrica en ciudades de Latinoamérica | Examina si la inseguridad ecosistémica y la vulnerabilidad social llevan a fallas de seguridad hídrica |

**Lectura conjunta.** La evidencia colombiana apunta en una dirección: el impacto de la sequía sobre la salud depende más de la pobreza y la exclusión que del acceso físico al agua {cite:p}`contreras2020the`. Por eso el análisis de sequía debe combinar un índice de amenaza (SPI o índices satelitales, {cite:p}`ojedaflechas2020characterization`) con vulnerabilidad social ([](../04_vulnerabilidad/43_vulnerabilidad_social.md)). Los resultados de La Guajira son asociaciones entre municipios y no prueban causalidad individual.

**Estudios añadidos con el segundo lote de PDFs.**

| Estudio | Diseño y lugar | Resultado relevante |
|---|---|---|
| {cite:t}`paeztrujilo2023multivariate` | Modelo hidrológico SWAT y árboles de regresión multivariados | Relaciona características hidroclimáticas con la severidad de sequías agrícolas e hidrológicas |
| {cite:t}`villalbabarrios2024assessing`; {cite:t}`villalbabarrios2026analysis` | Análisis probabilista de caudales y duración de sequías en el río Sinú; índice SPI | Compara las sequías antes y después de la operación de una hidroeléctrica |
| {cite:t}`mora2026porque` | Historia climática, llanuras del Caribe, 1739–1825 | La sequía fue menos frecuente que el exceso de lluvia, pero sus efectos se agravaron por presiones sociales |

**Lectura adicional.** La regulación de un embalse cambia la serie de caudales y, por tanto, la sequía observada {cite:p}`villalbabarrios2024assessing,villalbabarrios2026analysis`; los registros históricos muestran que la presión social agravó la sequía mucho antes de los datos instrumentales {cite:p}`mora2026porque`.

## Pendiente

- Leer {cite:p}`nauditt2022evaluating`, {cite:p}`cerpareyes2022adjustment` y {cite:p}`ojedaflechas2020characterization` completos. Los dos últimos solo se conocen por su resumen.
- Añadir el caso urbano: desabastecimiento de acueductos y escasez en ciudades (ID 857, Bogotá), con las cifras del Estudio Nacional del Agua más reciente.
- Verificar si el IDEAM ya cuenta con una evaluación nacional de amenaza de sequía posterior a 2019.

## Bibliografía recomendada

Lista de los 21 registros de la hoja de vigilancia científica (pestaña `Vigilancia_CTeI`, columna `AMENAZA_ESPECIFICA` = «Sequía»), en formato APA 7 con metadatos de Crossref. Son lecturas recomendadas: **no están verificadas contra el texto completo** ni se usan como evidencia hasta que se citen en el capítulo. Las entradas sin DOI carecen de autores en la hoja.

- Anochi, J. A., & Shimizu, M. H. (2024). Precipitation Forecasting and Drought Monitoring in South America Using a Machine Learning Approach. *Meteorology*, *4*(1), 1. https://doi.org/10.3390/meteorology4010001

- Barrera Gaitán, K. G., Cárdenas Torres, N. D., Sánchez Hernández, K. A., Veettil, A. V., & Adem, A. A. (2026). Drought risk assessment and ecosystem resilience in the municipality of Mesitas del Colegio, Colombia. *Global Drought and Sustainability*, 279-297. https://doi.org/10.1016/b978-0-443-44625-2.00006-0

- Cerpa Reyes, L. J., Ávila Rangel, H., & Herazo, L. C. S. (2022). Adjustment of the Standardized Precipitation Index (SPI) for the Evaluation of Drought in the Arroyo Pechelín Basin, Colombia, under Zero Monthly Precipitation Conditions. *Atmosphere*, *13*(2), 236. https://doi.org/10.3390/atmos13020236

- Contreras, D., Voets, A., Junghardt, J., Bhamidipati, S., & Contreras, S. (2020). The Drivers of Child Mortality During the 2012–2016 Drought in La Guajira, Colombia. *International Journal of Disaster Risk Science*, *11*(1), 87-104. https://doi.org/10.1007/s13753-020-00255-0

- Desalination and the Reproduction of Water Injustices in the San Andrés Island Water Crisis. (2023). (Sin DOI; completar autores).

- Evaluacion probabilista del riesgo por sequía en el sector agrícola de Colombia. (2021). *Investigaciones en gestion del riesgo de desastres para Colombia: Avances, perspectivas y casos de estudio*. (Sin DOI; completar autores).

- Gironás, J., Núñez, M., Vicuña, S., Aedo, S., Morales, D., Vargas, J., de Dios Guzmán, J., & Suárez, F. (2025). Towards a Drought Monitoring, Tracking, and Management Platform Based on Quantitative Indices. *Global Issues in Water Policy*, 289-303. https://doi.org/10.1007/978-3-031-85040-0_13

- Guerrero, C. D., Herrera-Rodríguez, D., & Forero-Buitrago, G. A. (2021). Hidrología e hidráulica computacional aplicada al suministro de agua lluvia de la vereda el Tunal en Paipa, Boyacá Colombia. *INGENIERÍA Y COMPETITIVIDAD*, *23*(2), e2019502. https://doi.org/10.25100/iyc.v23i2.9502

- Joaqui-Barandica, O., Manotas-Duque, D. F., & Rivera-Cadavid, L. (2025). Evaluation of energy complementarity in colombia: An analysis of climate variability and non-conventional sources. *Results in Engineering*, *27*, 105824. https://doi.org/10.1016/j.rineng.2025.105824

- Kapica, J., Jurasz, J., Canales, F. A., Bloomfield, H., Guezgouz, M., De Felice, M., & Kobus, Z. (2024). The potential impact of climate change on European renewable energy droughts. *Renewable and Sustainable Energy Reviews*, *189*, 114011. https://doi.org/10.1016/j.rser.2023.114011

- Lane, K., Branch, N., Handley, J., Meddens, F., Gonzalez, P., Walsh, D., Advíncula, M., Herrera, A., Vivanco, C., & Moncada, W. (2025). Utilising Cultural Heritage to Improve Water Security and Agro-Pastoral Farming in the Peruvian Andes. *Cultural Heritage, Community Engagement and Sustainable Tourism*, 248-265. https://doi.org/10.4324/9781003491071-18

- Mamani, L., Andreoli, R. V., de Souza, I. P., Cevalho, W., Sales, D., Kayano, M. T., de Souza, R. A. F., Molina-Carpio, J., Ceron, W. L., & Macedo, T. (2025). Extreme droughts in the Amazon Basin during cyclic ENSO events coupled with Indian Ocean Dipole modes and Tropical North Atlantic warming. *Science of The Total Environment*, *963*, 178536. https://doi.org/10.1016/j.scitotenv.2025.178536

- Mora Pacheco, K. (2026). Porque “las aguas han sido muy pocas”: sequías y respuestas sociales en las llanuras de la Costa Norte neogranadina, 1739-1825. *Fronteras de la historia*, *31*(1), 366-400. https://doi.org/10.22380/20274688.3057

- Nauditt, A., Stahl, K., Rodríguez, E., Birkel, C., Formiga-Johnsson, R. M., Kallio, M., Ribbe, L., Baez-Villanueva, O. M., Thurner, J., & Hann, H. (2022). Evaluating tropical drought risk by combining open access gridded vulnerability and hazard data products. *Science of The Total Environment*, *822*, 153493. https://doi.org/10.1016/j.scitotenv.2022.153493

- Ojeda Flechas, C. D., Burbano Rodriguez, J. A., Carvajal Escobar, Y., & Hernández Torres, F. L. (2020). Characterization of comprehensive drought events associated with the ENSO warm phase through satellite images in the Valle del Cauca Colombia. *DYNA*, *87*(214), 204-214. https://doi.org/10.15446/dyna.v87n214.83221

- Ortega-Ramírez, A. T., Hinojosa-Flores, I. D., Martínez González, E. L. Á., Cid, E. R., & Chávez, A. S. (2026). Assessment and Response to Water Stress in Bogotá: A Multidimensional Analysis. *Water*, *18*(10), 1155. https://doi.org/10.3390/w18101155

- Paez-Trujilo, A., Cañon, J., Hernandez, B., Corzo, G., & Solomatine, D. (2023). Multivariate regression trees as an “explainable machine learning” approach to explore relationships between hydroclimatic characteristics and agricultural and hydrological drought severity: case of study Cesar River basin. *Natural Hazards and Earth System Sciences*, *23*(12), 3863-3883. https://doi.org/10.5194/nhess-23-3863-2023

- Scott, C. A., Zilio, M. I., Harmon, T., Zuniga-Teran, A., Díaz-Caravantes, R., Hoyos, N., Perillo, G. M. E., Meza, F., Varady, R. G., Neto, A. R., Velez, M. I., Martín, F., Escobar, J., Piccolo, M. C., Mussetta, P., Montenegro, S., Rusak, J. A., & Pineda, N. (2021). Do ecosystem insecurity and social vulnerability lead to failure of water security? *Environmental Development*, *38*, 100606. https://doi.org/10.1016/j.envdev.2020.100606

- Villalba-Barrios, A. F., Coronado Hernández, O. E., Fuertes-Miquel, V. S., Arrieta-Pastrana, A., & Ramos, H. M. (2024). Assessing Extreme Drought Events and Their Temporal Impact: Before and after the Operation of a Hydropower Plant. *Applied Sciences*, *14*(5), 1692. https://doi.org/10.3390/app14051692

- Villalba-Barrios, A. F., Coronado-Hernández, O. E., Arrieta-Pastrana, A., & Pérez-Sánchez, M. (2026). Analysis of the standardized precipitation index and its impact on drought hydrographs: Effects of a hydroelectric power plant. *Physics and Chemistry of the Earth, Parts A/B/C*, *144*, 104578. https://doi.org/10.1016/j.pce.2026.104578

- Wang, P., Chu, L., Ban, J., Asare, E. O., Sivakami, M., Henao, A. R., Chimoyi, L., Sullivan, T. P., & Chen, K. (2025). Drought, Extreme Heat, and Intimate Partner Violence in Low- and Middle-Income Countries. *JAMA Network Open*, *8*(8), e2527818. https://doi.org/10.1001/jamanetworkopen.2025.27818
