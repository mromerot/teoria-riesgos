---
title: Erosión fluvial
---

# Erosión fluvial

Este capítulo sigue el molde de siete puntos ([](_molde.md)). Cubre la socavación del lecho, la erosión de orillas y la migración lateral de los cauces. Se relaciona con la inundación ([](305_inundacion.md)) porque ambas dependen del caudal, pero el daño aquí es la pérdida de terreno y de lo construido sobre él.

```{important}
**Cobertura de fuentes.** El Atlas de Riesgo de Colombia, CLIMAAX y CCDR-tools no tienen una metodología de erosión fluvial. Este capítulo se construye con la literatura de la hoja de vigilancia (22 registros de erosión y acreción fluvial). Es el capítulo con menos respaldo del libro y está marcado como provisional.
```

## 1. Fenómeno

Todo cauce natural está expuesto a socavación o erosión fluvial, producto de la interacción con el agua, que produce cambios morfológicos y desplazamientos del lecho que pueden afectar infraestructura y población cercanas {cite:p}`francorojas2024condiciones`. En los ríos meándricos de alta dinámica, el desplazamiento lateral del cauce es la forma de amenaza más relevante para vías y poblados.

Se distinguen procesos que conviene medir por separado:

| Proceso | Qué cambia | Ejemplo |
|---|---|---|
| **Socavación** | Descenso del lecho, sobre todo en estructuras | Pilas de puentes y obras de protección |
| **Erosión de orillas** | Retroceso del talud del cauce | Orillas de grandes ríos en zonas inundables {cite:p}`cardenas2024prioritizing` |
| **Migración lateral** | Desplazamiento del cauce en ríos meándricos | Río Unete (Casanare) frente a la vía Aguazul–Maní {cite:p}`francorojas2024condiciones` |
| **Sedimentación y barras** | Acreción en el cauce, que desvía la corriente | Barra fluvial en el tramo final del Magdalena {cite:p}`manzolli2022recent` |

**Variable de intensidad.** Tasa de desplazamiento del cauce (m/año), profundidad de socavación y fuerza tractiva sobre el material de la orilla.

### Erosión y acreción, dos caras del mismo proceso

Que un río erosione una orilla suele significar que acreciona la contraria. En un tramo de 3,5 km del Amazonas entre Nazaret y Leticia, un modelo numérico identificó sedimentación severa en el cauce izquierdo y la aparición de barras de arena en la parte colombiana del cauce, validadas con análisis multitemporal. El título del estudio plantea la pérdida potencial de soberanía por esos cambios {cite:p}`villadiegorojas2023fluvial`. Este es el caso más directo para Leticia.

### Definición según los HIPs de UNDRR

Los perfiles de información de amenazas ([](../01_conceptos/16_hips_undrr.md)) que corresponden a este capítulo son:

| Código | Perfil (clúster) | Definición (traducción propia) |
|---|---|---|
| GH0404 | Erosión y acreción fluvial (geológico, otros peligros) | La erosión fluvial es la remoción de material de las orillas y los lechos de ríos y quebradas; la acreción fluvial es la formación de tierra nueva, como barras de canal, bancos de arena y deltas, por sedimentación o por cambios del flujo (Lawler, 1993; Islam y Guchhait, 2020; Hasanuzzaman et al., 2024). |

Fuente: {cite:p}`undrr2025hips`.

**Qué se incluye y por qué.**

- **Se incluye.** El perfil trata erosión y acreción como dos caras del mismo proceso, igual que el capítulo, y su idea de acreción (barras, bancos de arena, deltas) corresponde a las barras del Amazonas cerca de Leticia que el capítulo describe.
- **No se incluye la erosión del suelo (GH0403).** Los HIPs la tratan aparte (remoción de partículas por agua, viento, cosecha y labranza); es una amenaza de ladera y de uso agrícola, y no la erosión de cauces.
- **Cascadas.** Los HIPs registran la erosión fluvial como causada por inundaciones, lahares, licuefacción, falla de presas y ascenso del nivel del mar, y como causa de movimientos en masa {cite:p}`undrr2025hips`.

## 2. Amenaza

### Análisis multitemporal

El método más usado es comparar imágenes satelitales y aéreas de varias fechas para medir el desplazamiento del cauce. En el río Unete se superpusieron imágenes durante 27 años, lo que permitió identificar sectores críticos por la proximidad entre río y vía y por la tasa de desplazamiento {cite:p}`francorojas2024condiciones`.

### Susceptibilidad por tipo de material

Después de identificar los puntos críticos se tomaron muestras de suelo y se cuantificó en laboratorio la **fuerza tractiva admisible**. La mayor susceptibilidad apareció en terrazas recientes de arenas limosas, seguidas de terrazas altas con arcillas de alta y baja plasticidad {cite:p}`francorojas2024condiciones`. Esta secuencia, mapa multitemporal + ensayo geotécnico, es el patrón de un estudio de amenaza a escala local.

### Modelación numérica

Para ríos grandes se usa modelación hidrodinámica y de transporte de sedimentos. Ejemplos: el modelo numérico del tramo Nazaret–Leticia {cite:p}`villadiegorojas2023fluvial`, la evolución de una barra fluvial por causas naturales y por estructuras portuarias en el tramo final del Magdalena {cite:p}`manzolli2022recent`, y la modelación bidimensional del transporte de sedimentos en una confluencia de ríos (ID 767 de la hoja).

Para caracterización morfológica semiautomática existe el South Rivers Toolbox (ID 488), por leer.

## 3. Exposición

La exposición es la franja que el río puede ocupar: vías, viviendas, redes de servicios, tierras agrícolas y puertos. El caso del río Unete muestra que la exposición puede reducirse a un solo elemento crítico, el único corredor vial entre dos municipios, con consecuencias para el transporte, el abastecimiento y la economía de ambos {cite:p}`francorojas2024condiciones`.

## 4. Vulnerabilidad

En erosión fluvial el elemento expuesto suele perderse por completo si queda dentro de la franja de erosión, por lo que, como criterio de método, se usa una función binaria o una vulnerabilidad cualitativa por tipo de elemento.

Las obras de protección cambian la vulnerabilidad y también el cauce. Un estudio sobre los efectos de la protección de orillas en la morfología fluvial (ID 900) y una revisión bibliométrica de medidas de control de erosión fluvial (ID 590) cubren este punto; quedan por leer.

## 5. Riesgo

El riesgo suele expresarse como elementos expuestos dentro de la franja de erosión proyectada, no como PAE. Para decidir dónde proteger con recursos limitados, un marco de apoyo a la decisión propone asignar de forma óptima los recursos públicos entre puntos de erosión en un gran río. El resumen señala que la financiación pública para esos puntos es limitada {cite:p}`cardenas2024prioritizing`.

Hay también simulaciones numéricas de soluciones basadas en la naturaleza para erosión de orillas {cite:p}`rivillasospina2025numerical`. Las cito por el título; deben leerse para su alcance.

## 6. Clima

Los cauces responden a los caudales y al régimen de lluvias; por lo tanto, los cambios en inundación ([](305_inundacion.md)) se trasladan a la erosión. Las fuentes de este capítulo no cuantifican esa relación. Como criterio de método, las proyecciones de caudal de la cuenca (por ejemplo, las del Magdalena en el capítulo de inundaciones) serían la entrada para evaluar el cambio de la tasa de migración. Esto requiere búsqueda de literatura específica.

## 7. Datos y medidas

### Datos

| Fuente | Qué ofrece |
|---|---|
| Imágenes satelitales y fotografías aéreas históricas | Posición del cauce en el tiempo |
| Ensayos geotécnicos de las orillas | Fuerza tractiva admisible y tipo de material |
| Batimetría y caudales | Entrada de los modelos hidrodinámicos; falta identificar las instituciones colombianas que los proveen |

La tabla es un resumen de los insumos que usan los estudios citados {cite:p}`francorojas2024condiciones,villadiegorojas2023fluvial`; no hay un catálogo oficial citado aquí.

### Incertidumbres

- La migración lateral no es lineal: un periodo de 27 años puede no representar el siguiente.
- Los modelos numéricos requieren batimetría reciente y validación con imágenes {cite:p}`villadiegorojas2023fluvial`.
- Las estructuras portuarias y las obras de protección alteran la sedimentación {cite:p}`manzolli2022recent`.

### Medidas según la Ley 1523

| Proceso | Medida | Referencia |
|---|---|---|
| Conocimiento | Monitoreo multitemporal del cauce, estudios de susceptibilidad geotécnica | {cite:p}`francorojas2024condiciones` |
| Reducción: prevención | Ordenamiento que respete la franja de movimiento del río | criterio de método |
| Reducción: mitigación | Protección de orillas priorizada, soluciones basadas en la naturaleza | {cite:p}`cardenas2024prioritizing,rivillasospina2025numerical` |

## Síntesis de evidencia

```{note}
**Método.** Síntesis narrativa por tipo de evidencia (no un metaanálisis con efectos agrupados: los estudios usan diseños, escalas y variables que no se pueden combinar en un solo estimador). Se leyeron los resúmenes de los artículos de la hoja de vigilancia que están en la carpeta de PDFs; las cifras vienen de esos resúmenes y **faltan por verificar contra el texto completo**.
```

| Estudio | Diseño y lugar | Resultado relevante |
|---|---|---|
| {cite:t}`cardenas2024prioritizing` | Marco de apoyo a la decisión con optimización para asignar recursos públicos | Prioriza la protección contra erosión de orillas en zonas de inundación |
| {cite:t}`manzolli2022recent` | Evolución geomorfológica de una barra de canal, río Magdalena | Atribuye los cambios a interferencias naturales y antrópicas |
| {cite:t}`garciadelgado2021climate` | Tasas de erosión en la cordillera Oriental | Compara el control del clima y de la tectónica en la variación espacio-temporal de las tasas |
| {cite:t}`calero2021evaluacion` | Evaluación de métodos de erosividad de la lluvia (USLE-EI30 y otros), Valle del Cauca | Compara métodos con datos de 12 estaciones |
| {cite:t}`lampreaquiroga2023erosion` | Tendencias de lluvia diaria de 26 estaciones (1980–2014) con Sen y Mann-Kendall e índice de Fournier modificado, corredor Bogotá–Duitama | Cuatro estaciones con tendencia positiva de lluvia mediana (6,90 a 28,80 mm/año) y una con descenso; el cuadrado del índice decadal máximo explica el grado de erosión con R² mayor que 0,50 |
| {cite:t}`vega2023assessment` | RUSLE-GGS (RUSLE con SIG, incertidumbre GLUE y relación de entrega de sedimento), cuenca del Cesar, 1991–2020, resolución 2,5 km | Primera estimación de erosión del suelo de esta cuenca; identifica puntos calientes con Getis-Ord |
| {cite:t}`rosas2020assessing` | RUSLE-SIG con incertidumbre GLUE y relación de entrega de sedimento, países en desarrollo | Propone un método para estimar erosión del suelo a escala nacional con pocas mediciones |

**Lectura conjunta.** La evidencia mezcla escalas: erosión de laderas y suelo (USLE/RUSLE, {cite:p}`calero2021evaluacion,rosas2020assessing`), dinámica de cauces {cite:p}`manzolli2022recent` y decisión de inversión {cite:p}`cardenas2024prioritizing`. Ninguno ofrece una amenaza de erosión de orillas lista para usar; el capítulo sigue siendo provisional.

## Pendiente

- Leer completos {cite:p}`cardenas2024prioritizing`, {cite:p}`manzolli2022recent`, {cite:p}`rivillasospina2025numerical` y {cite:p}`villadiegorojas2023fluvial`.
- Buscar metodologías de referencia (por ejemplo, de la Cormagdalena o el SGC) y guías de estudios de socavación para puentes.
- Definir cómo se integran la migración lateral y la inundación en una sola zonificación.
- Conectar con el capítulo de Leticia: el tramo Nazaret–Leticia es la aplicación directa.

## Bibliografía recomendada

Lista de los 33 registros de la hoja de vigilancia científica (pestaña `Vigilancia_CTeI`, columna `AMENAZA_ESPECIFICA` = «Erosión y acreción fluvial»; «Erosión del suelo»), en formato APA 7 con metadatos de Crossref. Son lecturas recomendadas: **no están verificadas contra el texto completo** ni se usan como evidencia hasta que se citen en el capítulo. Las entradas sin DOI carecen de autores en la hoja.

- Bolaño-Diaz, S., Camargo-Caicedo, Y., Tovar Bernal, F., & Bolaño-Ortiz, T. R. (2022). The Effect of Forest Fire Events on Air Quality: A Case Study of Northern Colombia. *Fire*, *5*(6), 191. https://doi.org/10.3390/fire5060191

- Calero Mosquera, D., Martínez López, C., & Menjívar Flores, J. C. (2021). Evaluación de modelos para estimar la erosividad de la lluvia en el Valle del Cauca, Colombia. *Acta Agronómica*, *70*(2). https://doi.org/10.15446/acag.v70n2.95115

- Calixto, N., Castaño, A., & Contreras-Ropero, J. (2024). Bibliometric Analysis of River Erosion Control Measures: Examination of Practices and Barriers in Colombia. *Hydrology*, *11*(9), 139. https://doi.org/10.3390/hydrology11090139

- Cardenas, A., Jalal, A., & Moreno, A. (2024). Prioritizing public resources for riverbank erosion protection: A decision support framework. *International Journal of Disaster Risk Reduction*, *115*, 105029. https://doi.org/10.1016/j.ijdrr.2024.105029

- CHICA-OSORIO, P. A., CARVAJAL-SERNA, L. F., & OCHOA, A. (2022). Comparison of stationary and nonstationary estimation of return period for sewer design in Antioquia (Colombia). *Anais da Academia Brasileira de Ciências*, *94*(suppl 4), e20200810. https://doi.org/10.1590/0001-3765202220200810

- Correa, S. B., van der Sleen, P., Siddiqui, S. F., Bogotá-Gregory, J. D., Arantes, C. C., Barnett, A. A., Couto, T. B. A., Goulding, M., & Anderson, E. P. (2022). Biotic Indicators for Ecological State Change in Amazonian Floodplains. *BioScience*, *72*(8), 753-768. https://doi.org/10.1093/biosci/biac038

- Diaz-Camacho, B., Restrepo-Prada, D., Quintero M., C. G., Viloria-Nunez, C., & Quiroga-Amaya, J. (2022). Computational Tool for Technological Risk Assessment in the Transport of Chemical Products. *2022 IEEE ANDESCON*, 1-6. https://doi.org/10.1109/andescon56260.2022.9989606

- Esteban Cantillo, O. J., & Quesada, B. (2022). Solid Waste Characterization and Management in a Highly Vulnerable Tropical City. *Sustainability*, *14*(24), 16339. https://doi.org/10.3390/su142416339

- Franco Rojas, A., Ayala Rojas, L. E., Padilla Gonzalez, E. A., Fajardo Ortiz, S. T., & Aguirre Alonso, J. C. (2024). Condiciones geomorfológicas y geotécnicas que determinan susceptibilidad ante socavación y migración de meandros en el río Unete afectando la infraestructura vial. *Investigaciones Geográficas*(115). https://doi.org/10.14350/rig.60912

- García-Delgado, H., Villamizar-Escalante, N., Bermúdez, M. A., Bernet, M., & Velandia, F. (2021). Climate or tectonics? What controls the spatial-temporal variations in erosion rates across the Eastern Cordillera of Colombia? *Global and Planetary Change*, *203*, 103541. https://doi.org/10.1016/j.gloplacha.2021.103541

- Jaramillo-González, R., Martínez, L., Aristizábal, E., García, E., & Marín, R. J. (2023). Definition of Rainfall Thresholds for Shallow Landslides in Colombian Tropical Mountainous Catchments as Debris Flow Triggering Mechanism. *E3S Web of Conferences*, *415*, 05009. https://doi.org/10.1051/e3sconf/202341505009

- Lamprea-Quiroga, P. S., Jaramillo-Rodríguez, O., & Mejía-Ayala, W. (2023). Soil erosion due to rainfall and the impacts of climate change in an Andean highland in Colombia. *Cuadernos de Investigación Geográfica*, *49*(2), 83-99. https://doi.org/10.18172/cig.5667

- Lapola, D. M., Pinho, P., Barlow, J., Aragão, L. E. O. C., Berenguer, E., Carmenta, R., Liddy, H. M., Seixas, H., Silva, C. V. J., Silva-Junior, C. H. L., Alencar, A. A. C., Anderson, L. O., Armenteras, D., Brovkin, V., Calders, K., Chambers, J., Chini, L., Costa, M. H., Faria, B. L., ... Walker, W. S. (2023). The drivers and impacts of Amazon forest degradation. *Science*, *379*(6630), eabp8622. https://doi.org/10.1126/science.abp8622

- Makarieva, A. M., Nefiodov, A. V., Nobre, A. D., Baudena, M., Bardi, U., Sheil, D., Saleska, S. R., Molina, R. D., & Rammig, A. (2023). The role of ecosystem transpiration in creating alternate moisture regimes by influencing atmospheric moisture convergence. *Global Change Biology*, *29*(9), 2536-2556. https://doi.org/10.1111/gcb.16644

- Manzolli, R. P., Portz, L., Villate-Daza, D., Pulido-Nossa, D., García-Becerra, D., & Alcántara-Carrió, J. (2022). Recent geomorphological evolution of channel bar in Magdalena River (Colombia) due to natural and anthropogenic interferences. *Estuarine, Coastal and Shelf Science*, *275*, 107959. https://doi.org/10.1016/j.ecss.2022.107959

- Marciano, A. G., Pacheco Torres, P. J., Luvizon Bérgamo, A., Barbosa, A. A., & Dos Reis Mendes Marciano, P. (2025). Modelización bidimensional del transporte de sedimentos en la confluencia de los ríos Suaçuí Grande y Doce tras el desastre de Mariana–MG, Brasil. *Cuadernos de Geografía: Revista Colombiana de Geografía*, *34*(1supl). https://doi.org/10.15446/rcdg.v34n1supl.108526

- Niño-Vega, R., & Vargas-Luna, A. (2026). Efectos en la morfología fluvial inducidos por obras de protección de márgenes. *Tecnología y ciencias del agua*, *17*(4), 72-122. https://doi.org/10.24850/j-tyca-2026-04-03

- Nunez, L. E., Rodriguez, J. A., Hoyos, J. M., Zachman, N., Campos, N., Lopez, C., & Villavicencio, J. (2025). Enhancing Wellbore Positioning and Operational Efficiency Through Advanced Surveying Technologies in ERD Project. *International Petroleum Technology Conference*, D022S008R007. https://doi.org/10.2523/iptc-24760-ms

- Ott, R. F., Pérez-Consuegra, N., Scherler, D., Mora, A., Huppert, K. L., Braun, J., Hoke, G. D., & Sandoval Ruiz, J. R. (2023). Erosion rate maps highlight spatio-temporal patterns of uplift and quantify sediment export of the Northern Andes. *Earth and Planetary Science Letters*, *621*, 118354. https://doi.org/10.1016/j.epsl.2023.118354

- Panagos, P., Hengl, T., Wheeler, I., Marcinkowski, P., Rukeza, M. B., Yu, B., Yang, J. E., Miao, C., Chattopadhyay, N., Sadeghi, S. H., Levi, Y., Erpul, G., Birkel, C., Hoyos, N., Oliveira, P. T. S., Bonilla, C. A., Nel, W., Al Dashti, H., Bezak, N., ... Borrelli, P. (2023). Global rainfall erosivity database (GloREDa) and monthly R-factor data at 1 km spatial resolution. *Data in Brief*, *50*, 109482. https://doi.org/10.1016/j.dib.2023.109482

- Pimiento, M. A., Duque, V., & Torres, A. (2023). Urban stormwater sediment risk assessment from drainage structures in Bogotá, Colombia. *Environmental Science: Water Research & Technology*, *9*(12), 3269-3280. https://doi.org/10.1039/d2ew00746k

- Rivillas-Ospina, G., Díaz, K., Gutiérrez, R. R., Berrío, Y., Doria, R., & Felizzola, M. (2025). Numerical simulation and application of nature based solutions to solve bank erosion in hydrosystems. *Ecohydrology & Hydrobiology*, *25*(3), 556-572. https://doi.org/10.1016/j.ecohyd.2024.09.005

- Rockwell, T. K., Costa, C. H., Meigs, A. J., Ragona, D., Owen, L. A., Murari, M. K., Masana, E., & Richard, A. D. (2022). Paleoseismology of the Marquesado-La Rinconada thrust system, Eastern Precordillera of Argentina. *Frontiers in Earth Science*, *10*, 1032357. https://doi.org/10.3389/feart.2022.1032357

- Roman Quintero, D. C., Ortiz Contreras, J. D., Tapias Camacho, M. A., & Oviedo-Ocaña, E. R. (2024). Empirical Estimation of Landslide Runout Distance Using Geometrical Approximations in the Colombian North–East Andean Region. *Sustainability*, *16*(2), 793. https://doi.org/10.3390/su16020793

- Rosas, M. A., & Gutierrez, R. R. (2020). Assessing soil erosion risk at national scale in developing countries: The technical challenges, a proposed methodology, and a case history. *Science of The Total Environment*, *703*, 135474. https://doi.org/10.1016/j.scitotenv.2019.135474

- Ruiz, D. M., Barrera, N., Reyes, J. C., López, C., & Restrepo, M. (2023). An approach to Colombian Andean earthen architecture in urban environments: a case study of Bogotá Historic Centre. *Journal of Architectural Conservation*, *29*(2), 168-192. https://doi.org/10.1080/13556207.2022.2160556

- Souza, I. P., Andreoli, R. V., Kayano, M. T., Cerón, W. L., Souza, R. A. F., & Roy, I. (2023). Interdecadal Pacific Oscillation modulation of ENSO teleconnections in its decaying stages: Relations with Indian Ocean basin‐wide mode and South American precipitation. *International Journal of Climatology*, *43*(7), 3264-3283. https://doi.org/10.1002/joc.8028

- Vega, S. P., Gutierrez, R. R., & Maturana, A. Y. (2023). Assessment of soil erosion in the Cesar watershed, an initial step toward the restoration of the Cesar River. *2023 IEEE Colombian Caribbean Conference (C3)*, 1-6. https://doi.org/10.1109/c358072.2023.10436193

- Villadiego-Rojas, L., Daza-González, R., Robles, G. A., & Restrepo, D. B. (2023). Fluvial Dynamics of the Amazon River between Nazareth and Leticia: Potential Loss of Colombia's Sovereignty Over the Amazon River. *Civil Engineering and Architecture*, *11*(3), 1167-1181. https://doi.org/10.13189/cea.2023.110305

- Volverás-Mambuscay, B., Merchancano-Rosero, J. D., López-Rendón, J. F., & Campo-Quesada, J. M. (2021). Pérdida de suelo en el sistema ancestral wachado en el trópico alto de Nariño, Colombia. *Agronomía Mesoamericana*, 120-136. https://doi.org/10.15517/am.v32i1.39284

- Wright, M. N., Bird, B. W., Gibson, D. K., Pollard, H., Escobar, J., & Barr, R. C. (2023). Fluvial responses to late Holocene hydroclimate variability in the midcontinental United States. *Quaternary Science Reviews*, *301*, 107939. https://doi.org/10.1016/j.quascirev.2022.107939

- Yépez, S., Salas, F., Nardini, A., Valenzuela, N., Osores, V., Vargas, J., Rodríguez, R., & Piégay, H. (2024). Semi-automated morphological characterization using South Rivers Toolbox. *Proceedings of IAHS*, *385*(0), 189-196. https://doi.org/10.5194/piahs-385-189-2024

- Zambrano, M. C., González, H. E. M., & Tequia, W. E. A. (2022). Three-dimensional Numerical Evaluation of Hydraulic Efficiency and Discharge Coefficient in Grate Inlets. *Environmental Research, Engineering and Management*, *78*(4), 121-136. https://doi.org/10.5755/j01.erem.78.4.31243
