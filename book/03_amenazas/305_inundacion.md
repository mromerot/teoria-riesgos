---
title: Inundaciones
---

# Inundaciones

:::{image} ../../estilo/ilustraciones/inundacion.svg
:alt: Casas parcialmente inundadas bajo la lluvia
:class: ilustracion
:width: 100%
:::

Este capítulo es el primero que sigue el molde de siete puntos ([](_molde.md)). Cubre la inundación fluvial lenta, la creciente súbita y la inundación pluvial urbana. Las avenidas torrenciales, con carga sólida, tienen su propio capítulo: [](316_avenidas_torrenciales.md). La inundación costera se trata en [](306_erosion_costera.md).

## 1. Fenómeno

Una inundación fluvial ocurre cuando lluvias persistentes elevan el nivel del agua de un cauce por encima de sus orillas, y el agua se dispersa sobre las llanuras de inundación y las zonas aledañas que normalmente no están sumergidas. Los desbordamientos son un evento natural y recurrente para un río {cite:p}`ungrd2019atlas`.

La magnitud depende de la intensidad de la lluvia, de su distribución en el espacio y el tiempo, del tamaño de la cuenca, del suelo y del drenaje natural o artificial {cite:p}`ungrd2019atlas`. El daño suele resultar de la ocupación de zonas propensas y de cambios del uso de la tierra, como la urbanización que transforma la cobertura natural {cite:p}`ungrd2019atlas`.

El Atlas distingue dos tipos {cite:p}`ungrd2019atlas`:

| Tipo | Dónde ocurre | Dinámica | Consecuencia típica |
|---|---|---|---|
| **Inundación lenta** | Zonas planas y valles aluviales extensos | El nivel sube centímetros por día, la afectación puede durar meses | Grandes extensiones afectadas, pocas muertes. Ejemplo: La Mojana |
| **Creciente súbita** | Cuencas de alta pendiente, sobre todo andinas | El nivel sube metros en pocas horas, la afectación dura horas o pocos días | Áreas menores pero mayor poder destructivo y riesgo de pérdida de vidas |

A estos dos tipos se suma la **inundación pluvial urbana**: una lluvia intensa y localizada produce escorrentía rápida, supera la capacidad hidráulica del alcantarillado y se agrava si se bloquean tuberías y alcantarillas {cite:p}`ungrd2019atlas`.

**Variable de intensidad.** La profundidad de inundación (m) es la variable principal para el daño a edificaciones. La velocidad y la carga sólida importan en crecientes súbitas.

```{note}
En el norte de Suramérica el ENSO reduce las lluvias durante El Niño y las aumenta durante La Niña. En 2010–2011, La Niña causó una de las peores emergencias por inundaciones, avenidas torrenciales y movimientos en masa del país {cite:p}`ungrd2019atlas`. En 2017, el desbordamiento de los ríos Mulato y Sangoyaco y de la quebrada Taruca arrasó el norte de Mocoa {cite:p}`ungrd2019atlas`.
```

### Definición según los HIPs de UNDRR

Los perfiles de información de amenazas ([](../01_conceptos/16_hips_undrr.md)) que corresponden a este capítulo son:

| Código | Perfil (clúster) | Definición (traducción propia) |
|---|---|---|
| MH0600 | Inundación (meteorológico e hidrológico, agua) | (1) Desbordamiento de agua fuera de los confines normales de un curso u otro cuerpo de agua; (2) acumulación de agua de drenaje sobre áreas normalmente no sumergidas; (3) esparcimiento controlado de agua para riego (OMM y UNESCO, 2012). |
| MH0604 | Inundación fluvial | Desbordamiento de agua fuera de los confines normales de un curso u otro cuerpo de agua (OMM, 2012). |
| MH0603 | Inundación repentina | Inundación de corta duración con un caudal pico relativamente alto (OMM, 2021). |
| MH0609 | Inundación por encharcamiento (pluvial) | Resulta del agua de lluvia que se acumula donde cae o cerca de ahí, porque cae más rápido de lo que el drenaje, natural o artificial, puede evacuar (OMM, 2006). |
| MH0601 | Inundación costera | Ocurre por múltiples fuentes: marejadas de tormenta, oleaje, seiches, crecidas cercanas a la costa, mareas, ascenso del nivel del mar y tsunamis; es más frecuente por marejadas con viento fuerte que coinciden con mareas altas (OMM, 2011; 2022). |

Fuente: {cite:p}`undrr2025hips`.

**Qué se incluye y por qué.**

- **Se incluyen el perfil general y cuatro subtipos** (fluvial, repentina, pluvial y costera). Del perfil general solo aplican las acepciones (1) y (2); el riego controlado (3) no es una amenaza.
- **Correspondencia con la clasificación del Atlas** (criterio de método de este libro): la *inundación lenta* de llanuras aluviales corresponde a MH0604; la *creciente súbita* a MH0603; la *inundación pluvial urbana* a MH0609. La definición de MH0603 se centra en la duración y el caudal pico, y no en la pendiente de la cuenca, que es lo que el Atlas destaca para las cuencas andinas.
- **Inundación costera (MH0601):** se trata en [](306_erosion_costera.md) y [](311_ciclones.md).
- **No se desarrollan** las inundaciones por aguas subterráneas (MH0605), por aguas superficiales (MH0606), estuarinas (MH0602) ni por desborde de lagos glaciares (MH0607).
- **Cascadas.** Los HIPs registran la inundación como causada por lluvia, ciclones, tormentas y falla de presas, y como causa de movimientos en masa, lahares, erosión de ríos y costas, enfermedades transmitidas por el agua y fallas de infraestructura {cite:p}`undrr2025hips`.

## 2. Amenaza

### Métodos usados en Colombia

El Atlas recoge cinco metodologías de estimación de la amenaza de inundación usadas en el país, según una consolidación de la Universidad Nacional de Colombia para el IDEAM {cite:p}`ungrd2019atlas`:

1. **Históricos**: marcas y placas sobre elementos artificiales.
2. **Paleohídricos**: registros geológicos de depósitos de inundaciones sin información histórica.
3. **Geológicos y geomorfológicos**: formas del terreno y depósitos para delimitar áreas activas, la frecuencia cualitativa y órdenes de magnitud de profundidad y velocidad.
4. **Sensores remotos**: reconocen suelos húmedos y delimitan áreas inundadas.
5. **Hidrológicos e hidráulicos**: estiman caudales, velocidades y niveles, y permiten asociar periodos de retorno.

Todos producen una zonificación, cuya calidad depende de la escala, la cobertura y el detalle topográfico de los datos de entrada {cite:p}`ungrd2019atlas`.

### Enfoque probabilista

Para el riesgo, la amenaza se representa como una colección de escenarios generados de forma estocástica. Cada uno tiene una frecuencia de ocurrencia y la distribución espacial de parámetros que permite construir la distribución de probabilidad de las intensidades {cite:p}`ungrd2019atlas`. El Atlas usa el mapa de profundidad de inundación a 50 años de periodo de retorno, obtenido de la evaluación global desarrollada para el GAR15 {cite:p}`ungrd2019atlas`.

CLIMAAX sigue una lógica equivalente: combina mapas de extensión de inundación para varios periodos de retorno con datos de exposición y vulnerabilidad {cite:p}`climaax2025handbook`. Su flujo de trabajo fluvial usa mapas europeos para periodos de retorno de 10 a 500 años, que **no incluyen** defensas como diques o presas, y solo cubre cuencas mayores de 150 km² {cite:p}`climaax2025handbook`. Por eso recomienda usar mapas locales cuando existan y contrastar siempre con el conocimiento local {cite:p}`climaax2025handbook`.

```{warning}
Para crecientes súbitas y para inundación pluvial urbana, los mapas globales y regionales no tienen el detalle necesario. CLIMAAX aconseja modelos locales de mayor resolución con defensas y drenaje, y alimentarlos con eventos de lluvia simulados para periodos de retorno dados {cite:p}`climaax2025handbook`.
```

### Modelación local en estudios colombianos

La literatura reciente en Colombia ofrece métodos para el nivel de ciudad. Algunos ejemplos, citados solo por lo que declaran sus resúmenes:

- Comparación de dos modelos hidrodinámicos (MODCEL e IBER) para inundación en un pueblo costero del norte {cite:p}`perez2022modcel`.
- Evaluación de crecientes en pequeñas cuencas andinas tropicales, motivada por la impermeabilización y las inundaciones repentinas urbanas {cite:p}`zambrano2022storm`.
- Evaluación del desempeño de modelos digitales de elevación globales en llanuras costeras planas del departamento de Córdoba, frente a LiDAR de alta resolución {cite:p}`fragozo2026dem`.

La calidad del modelo de elevación es una de las limitaciones más relevantes en llanuras. Conviene validarlo con datos locales antes de modelar.

## 3. Exposición

La inundación expone a población, edificaciones, infraestructura vial y de servicios, y áreas agropecuarias. Los estudios de amenaza sirven para el ordenamiento territorial, la regulación de usos del suelo y la definición de zonas de protección ambiental {cite:p}`ungrd2019atlas`.

El análisis de exposición combina la profundidad de inundación con capas de población y activos construidos {cite:p}`ccdr2025tools`. En CCDR-tools, las inundaciones fluviales y costeras probabilistas se cruzan con tres categorías de exposición: población, activos construidos y tierra agrícola {cite:p}`ccdr2025tools`.

En América Latina, un estudio de 363 ciudades de nueve países evalúa las disparidades en la exposición a inundación fluvial entre residentes, con datos del proyecto Salud Urbana en América Latina {cite:p}`xu2026latam`. Es una referencia para la dimensión de equidad de la exposición.

## 4. Vulnerabilidad

La vulnerabilidad física se modela con **curvas de daño por profundidad**: relacionan la profundidad de inundación con la fracción del valor del activo que se pierde {cite:p}`ccdr2025tools`. El Atlas presenta un esquema de función de vulnerabilidad para inundaciones, expresada como valor esperado y varianza del daño {cite:p}`ungrd2019atlas`. CLIMAAX calcula el daño combinando la profundidad, el tipo de uso del suelo, las curvas de daño y parámetros económicos del país {cite:p}`climaax2025handbook`.

Un estudio colombiano reciente analiza 13 factores de vulnerabilidad física de estructuras expuestas a corrientes de agua que cumplen funciones de protección contra inundaciones {cite:p}`hernandez2026physvuln`.

```{note}
La vulnerabilidad social y las capacidades se tratan en [](../04_vulnerabilidad/43_vulnerabilidad_social.md). Las curvas de daño, con ejemplos de Colombia, en [](../04_vulnerabilidad/42_funciones_dano.md).
```

## 5. Riesgo

Con capas de profundidad por periodo de retorno, la exposición y la curva de daño:

1. Para cada periodo de retorno se calcula el daño sobre cada píxel o activo.
2. Se grafica el daño contra la probabilidad de excedencia (la inversa del periodo de retorno).
3. El área bajo la curva es el **impacto anual esperado**, equivalente a la PAE del Atlas {cite:p}`ccdr2025tools,ungrd2019atlas`.

Con pocos periodos de retorno, el resultado es sensible a cómo se integra. CCDR-tools reporta una cota inferior, una superior y su promedio {cite:p}`ccdr2025tools`. Ver [](../02_metodologia/22_probabilista_pae.md).

Un enfoque alternativo es un índice de riesgo. Un estudio colombiano propone un sistema de lógica difusa que toma el nivel freático y su variación en el tiempo para obtener el nivel de riesgo de inundación en términos numéricos y lingüísticos {cite:p}`chanchi2023fuzzy`.

## 6. Clima

La inundación fluvial y pluvial es sensible al clima. Los índices relevantes son los días húmedos consecutivos (CWD), los días con más de 20 mm (R20mm), la precipitación máxima en cinco días (Rx5day) y los días extremadamente húmedos (R99p) {cite:p}`ccdr2025tools`. Ver [](../02_metodologia/23_escenarios_climaticos.md).

Tres líneas de evidencia relevantes para Colombia:

- **Cuenca del Magdalena.** Un estudio acopló el modelo hidrológico-hidrodinámico MGB con proyecciones del modelo regional Eta para evaluar el efecto del cambio climático en el caudal y la extensión de la inundación del río {cite:p}`munar2023magdalena`.
- **No estacionariedad.** El análisis de frecuencia asume tradicionalmente estacionariedad, pero el cambio climático y el cambio de uso del suelo la cuestionan. Un estudio colombiano lo aplica al diseño de drenaje vial {cite:p}`jimenez2022nonstat`.
- **Eventos sin precedentes.** A escala global, un conjunto de 45 pares de eventos en la misma área muestra que la gestión del riesgo ha reducido la vulnerabilidad a inundaciones y sequías, pero sus impactos siguen aumentando {cite:p}`kreibich2022unprecedented`.

```{warning}
Los dos últimos puntos solo se citan por el objetivo declarado en sus resúmenes. Falta leer los resultados completos antes de usarlos para afirmar magnitudes de cambio.
```

## 7. Datos y medidas

### Datos disponibles en Colombia

| Fuente | Qué ofrece | Referencia |
|---|---|---|
| IDEAM | Curvas intensidad–duración–frecuencia para periodos de retorno de 2, 3, 5, 10, 25, 50 y 100 años | {cite:p}`ungrd2019atlas` |
| IDEAM | Mapa nacional de zonas susceptibles a inundación | {cite:p}`ungrd2019atlas` |
| IDEAM | Mapas de inundación 1:100.000 para 22 departamentos, a partir de sensores remotos de 1988, 2000, 2011 y 2012 | {cite:p}`ungrd2019atlas` |
| IDEAM | Mapas de amenaza desde 1:500.000 hasta 1:5.000 en áreas piloto | {cite:p}`ungrd2019atlas` |
| IDEAM | Red de 1 932 estaciones meteorológicas, 609 hidrológicas y 96 hidrometeorológicas | {cite:p}`ungrd2019atlas` |
| UNGRD | Lineamientos para la evaluación probabilista del riesgo por inundación lenta | {cite:p}`ungrd2019atlas` |
| Minambiente | Guía técnica de los POMCA | {cite:p}`ungrd2019atlas` |

Los datos del Atlas son de 2019. Las cifras de estaciones y la disponibilidad de mapas deben actualizarse antes de aplicarse a una ciudad.

### Incertidumbres principales

- Calidad del modelo de elevación en llanuras {cite:p}`fragozo2026dem`.
- Ausencia de defensas y de gestión del agua en los mapas globales {cite:p}`climaax2025handbook`.
- Pocos periodos de retorno para integrar la curva de excedencia {cite:p}`ccdr2025tools`.

### Medidas según la Ley 1523

| Proceso | Medida | Fuente |
|---|---|---|
| Conocimiento | Zonificación de amenaza, monitoreo hidrometeorológico | {cite:p}`ungrd2019atlas` |
| Reducción: prevención | Ordenamiento territorial, regulación de usos del suelo, zonas de protección ambiental | {cite:p}`ungrd2019atlas` |
| Reducción: mitigación | Medidas estructurales de control de erosión y reforestación, protección comunitaria | {cite:p}`ungrd2019atlas` |
| Manejo | Boletines, avisos y alertas del IDEAM | {cite:p}`ungrd2019atlas` |

## Síntesis de evidencia

```{note}
**Método.** Síntesis narrativa por tipo de evidencia (no un metaanálisis con efectos agrupados: los estudios usan diseños, escalas y variables que no se pueden combinar en un solo estimador). Se leyeron los resúmenes de los artículos de la hoja de vigilancia que están en la carpeta de PDFs; las cifras vienen de esos resúmenes y **faltan por verificar contra el texto completo**.
```

| Bloque | Estudio | Diseño y lugar | Resultado relevante |
|---|---|---|---|
| Frecuencia y no estacionariedad | {cite:t}`universidad2020modelacion`; {cite:t}`ceron2021spatio` | Modelos aditivos generalizados con índices macroclimáticos y de embalse; variabilidad hidroclimática, alto Cauca | La frecuencia y magnitud de las crecidas cambia con el clima y con la regulación del embalse; hay un cambio significativo de las descargas de noviembre a enero tras 1986 |
| Frecuencia y no estacionariedad | {cite:t}`jimenezu2022stationary` | Análisis no estacionario con escenarios de uso del suelo y clima, drenaje vial | Los diseños con series estacionarias pueden subestimar el caudal |
| Pronóstico | {cite:t}`moreno2020computational` | Inteligencia computacional, ribera del Magdalena | Predicción de inundaciones con aprendizaje automático |
| Pluvial urbana | {cite:t}`martinez2021modelling`; {cite:t}`martinez2021multi` | Modelo acoplado de escorrentía superficial y alcantarillado; evaluación multiobjetivo de infraestructura verde y gris | Dimensiona infraestructura verde y gris para mitigar inundación urbana |
| Pluvial urbana | {cite:t}`saldarriaga2020reducing`; {cite:t}`guarda2026integrated` | Ubicación y tamaño óptimos de tanques de tormenta con clima cambiante; tanques de detención con aprendizaje automático | Reducen el caudal pico; ambos son estudios de diseño de medidas |
| Creciente súbita y alerta | {cite:t}`henao2022assessing`; {cite:t}`henao2025towards`; {cite:t}`zambrano2022storm` | Revisión sistemática de umbrales de lluvia; marco que integra alerta comunitaria e institucional; crecidas en cuencas andinas pequeñas | Los umbrales de lluvia son el método base de alerta para crecientes súbitas; se propone articular lo comunitario con lo institucional |
| Peatones | {cite:t}`corzo2024development` | Mapa de amenaza con fuerzas hidrodinámicas sobre peatones, Cúcuta | Incorpora la seguridad de las personas, que los mapas de profundidad no cubren |
| Eventos pequeños | {cite:t}`canonbarriga2022prioritizing` | Priorización de barrios con «pequeños desastres» por lluvia | Los mapas de inundación omiten efectos como el tráfico y las enfermedades de origen hídrico dentro y fuera de la llanura |
| Gestión y economía | {cite:t}`corderinovoa2020economics`; {cite:t}`facultad2021flood`; {cite:t}`departamento2023analysis` | Optimización de inversión; medidas locales en Tunja; ordenamiento en la cuenca baja del Sinú | La inversión puede optimizarse por tipo, combinación y momento de las medidas; la inundación lenta exige integrar la gestión del riesgo al ordenamiento |
| Global | {cite:t}`kreibich2022challenge`; {cite:t}`castellsquintana2022population` | Casos de crecidas y sequías sin precedentes; más de 3300 inundaciones y desplazamiento | Las inundaciones sin precedentes ponen a prueba la gestión; el desplazamiento por inundaciones se asocia con conflicto urbano |

**Lectura conjunta.** Los estudios revisados coinciden en que el análisis de inundación debe ir más allá de las series estacionarias y de la profundidad del agua, aunque la mayor parte de la literatura se ocupa del drenaje urbano y no de la amenaza.

- **Estacionariedad.** Tres estudios del alto Cauca y el Tolima muestran que las series no son estacionarias {cite:p}`universidad2020modelacion,ceron2021spatio,jimenezu2022stationary`; el análisis de frecuencia debe contrastarse con tendencias antes de fijar periodos de retorno.
- **Cambio de la estimación.** En Antioquia, comparar la estimación estacionaria y no estacionaria del periodo de retorno para diseño de alcantarillado es el mismo problema {cite:p}`chicaosorio2022comparison`.
- **Predominio de lo urbano.** La mayor parte de la evidencia de vigilancia es sobre medidas de drenaje, no sobre la amenaza {cite:p}`martinez2021modelling,saldarriaga2020reducing,guarda2026integrated`.
- **Alerta.** Para crecientes súbitas, los umbrales de lluvia son el instrumento de alerta más común {cite:p}`henao2022assessing`.
- **La profundidad no basta.** Hay que sumar fuerzas sobre personas {cite:p}`corzo2024development` y efectos distribuidos fuera del mapa de inundación {cite:p}`canonbarriga2022prioritizing`.
- **Nota sobre la hoja.** La fila 884 (SUDS en Ibagué) tiene un DOI que en Crossref corresponde a otro artículo (2018, pozos de infiltración); es un error de la hoja y no se cita aquí.

## Pendiente

- Verificar las citas de {cite:p}`kreibich2022unprecedented`, {cite:p}`jimenez2022nonstat` y {cite:p}`chanchi2023fuzzy` leyendo los artículos completos; hoy solo se apoyan en el objetivo declarado.
- Añadir las curvas de daño y valores máximos de daño para Colombia (capítulo 4.2).
- Añadir inundación pluvial urbana con los casos de SIDRo y Leticia y los sistemas urbanos de drenaje sostenible.
- Añadir los capítulos 2021 (14), 2023 (6) y 2025 de la serie de investigaciones GRD.

## Bibliografía recomendada

Lista de los 102 registros de la hoja de vigilancia científica (pestaña `Vigilancia_CTeI`, columna `AMENAZA_ESPECIFICA` = «Inundación»; «Inundación repentina»; «Inundación por aguas superficiales»; «Inundación de drenajes y alcantarillado»), en formato APA 7 con metadatos de Crossref. Son lecturas recomendadas: **no están verificadas contra el texto completo** ni se usan como evidencia hasta que se citen en el capítulo. Las entradas sin DOI carecen de autores en la hoja.

- A Politics of Global Datasets and Models in Flood Risk Management. (2025). *Water Alternatives*. (Sin DOI; completar autores).

- Alvarez Jaimes, M. A., Roman Quintero, D. C., Ortiz Contreras, J. D., Bedoya Rios, D. F., & Tapias Camacho, M. A. (2025). Implications of landslide runout modeling for vulnerability assessment: Benchmarking from a case study in the andean region. *International Journal of Disaster Risk Reduction*, *131*, 105920. https://doi.org/10.1016/j.ijdrr.2025.105920

- Anaya-Pallares, S., Avila-Rangel, H., Coronado-Hernández, O. E., Sisa-Camargo, A. H., & Pérez-Sánchez, M. (2025). Incorporating Uncertainty and Failure Probability in the Design of Urban Stormwater Channels for Resilient Cities. *Water*, *17*(13), 1918. https://doi.org/10.3390/w17131918

- Aponte García, V., Tarapuez Bolaños, D. F., García Millán, N., & Salcedo Hurtado, E. d. J. (2026). Vulnerabilidad social frente a avenida torrencial (flujo de detritos) en el área de influencia de la quebrada Isabel Pérez en Santiago de Cali, Colombia, usando lógica difusa. *Documents d'Anàlisi Geogràfica*, *72*(1), 135-167. https://doi.org/10.5565/rev/dag.1445

- Application of Random Forest in the Prediction of Extreme Flows: Evaluation against Deterministic Methods, exper-imental case of the Magdalena River Frío basin in Colombia. (2025). *Journal of Maritime Research*. (Sin DOI; completar autores).

- Arango, M. I., Aristizábal, E., & Gómez, F. (2020). Morphometrical analysis of torrential flows-prone catchments in tropical and mountainous terrain of the Colombian Andes by machine learning techniques. *Natural Hazards*, *105*(1), 983-1012. https://doi.org/10.1007/s11069-020-04346-5

- Arango-Carmona, M. I., Voit, P., Hürlimann, M., Aristizábal, E., & Korup, O. (2025). Hillslope-Torrential Hazard Cascades in Tropical Mountains. *Egusphere*. https://doi.org/10.5194/egusphere-2025-1698

- Arango-Carmona, M. I., Voit, P., Hürlimann, M., Aristizábal, E., & Korup, O. (2025). Hillslope torrential hazard cascades in tropical mountains. *Natural Hazards and Earth System Sciences*, *25*(9), 3641-3663. https://doi.org/10.5194/nhess-25-3641-2025

- Assessing debris flow susceptibility using triggering and propagation models, a case study in the tropical region of the northern andes in colombia. (2023). *Revista de la Asociacion Geologica Argentina*. https://revista.geologica.org.ar/raga/article/view/1660

- Bocanegra, R. A., Ramírez, C. A., Salcedo, E. d. J., & Villegas, M. P. L. (2023). Determination of Hazard Due to Debris Flows. *Water*, *15*(23), 4057. https://doi.org/10.3390/w15234057

- Bonalde-Marcano, E. M., & Núñez, L. A. (2025). Flood Mapping Using Contrastive Learning and Semantic Segmentation. *2025 IEEE Colombian Conference on Communications and Computing (COLCOM)*, 1-6. https://doi.org/10.1109/colcom66267.2025.11185779

- Canon-Barriga, C., Bogardi, J., & Tischbein, B. (2022). Prioritizing neighborhoods for intervention to mitigate urban small disasters triggered by rainfall. *Urban Water Journal*, *20*(10), 1672-1681. https://doi.org/10.1080/1573062x.2022.2026981

- CÁRDENAS DE LA OSSA, J. E., FLÓREZYEPES, G. Y., & HERNÁNDEZ GARCÍA, D. (2023). ANALYSIS OF RISK MANAGEMENT IN TERRITORIAL PLANNING IN AREAS SUSCEPTIBLE TO SLOW FLOODING. CASE STUDY RURAL SETTLEMENT “EL PLAYÓN” BAJO SINÚ (CÓRDOBA, COLOMBIA). *International Journal of Conservation Science*, *14*(1), 187-200. https://doi.org/10.36868/ijcs.2023.01.12

- Cardona, F. G., Giraldo, E. A., & Mergili, M. (2025). Modelling debris flood propagation in scarce data terrain, case study in the Colombian Andes. *Journal of South American Earth Sciences*, *165*, 105660. https://doi.org/10.1016/j.jsames.2025.105660

- Cardona, O. D., Bernal, G. A., & Marulanda, M. C. (2025). Flood risk assessment for the integrated disaster risk management and climate change adaptation action plan: La Mojana Region, Colombia. *Hydrosystem Restoration Handbook*, 135-147. https://doi.org/10.1016/b978-0-443-29802-8.00010-8

- Caro-Camargo, C. A., & Gil-Alvarado, L. (2021). Flood risk management contributions in localized areas. Case study: Tunja, Colombia. *Tecnología y ciencias del agua*, *12*(4), 384-420. https://doi.org/10.24850/j-tyca-2021-04-09

- Castells-Quintana, D., Lopez-Uribe, M. d. P., & McDermott, T. K. J. (2022). Population displacement and urban conflict: Global evidence from more than 3300 flood events. *Journal of Development Economics*, *158*, 102922. https://doi.org/10.1016/j.jdeveco.2022.102922

- Cerón, W. L., Kayano, M. T., Ocampo-Marulanda, C., Canchala, T., Rivera, I. A., Avila-Diaz, A., Andreoli, R. V., & de Souza, I. P. (2021). Spatio-Temporal Variability of Hydroclimatology in the Upper Cauca River Basin in Southwestern Colombia: Pre- and Post-Salvajina Dam Perspective. *Atmosphere*, *12*(11), 1527. https://doi.org/10.3390/atmos12111527

- Chanchí Golondrino, G. E., Ospina Alarcón, M. A., & Saba, M. (2023). Floods risk determination through a fuzzy logic system in developing countries. Case study Magdalena River, Colombia. *INTERNATIONAL JOURNAL OF COMPUTERS COMMUNICATIONS & CONTROL*, *18*(5). https://doi.org/10.15837/ijccc.2023.5.5103

- Chavez-Arias, G. Y., Coca Galeano, C. P., & Torres-Torres, J. J. (2024). Factores Subyacentes de Riesgo de Desastres por Avenida Torrencial, Inundación y Movimientos en Masa en Carmen de Atrato, Colombia. *Revista de Estudios Latinoamericanos sobre Reducción del Riesgo de Desastres REDER*, *8*(2), 99. https://doi.org/10.55467/reder.v8i2.160

- Corderi‐Novoa, D., Hori, T., & Yamin, L. E. (2020). The Economics of Investment and Prioritization of Flood Risk Reduction Measures in a Watershed. *Risk Analysis*, *41*(8), 1345-1361. https://doi.org/10.1111/risa.13642

- Coronado-Hernández, O. E., Fuertes-Miquel, V. S., & Arrieta-Pastrana, A. (2024). The Development of a Hydrological Method for Computing Extreme Hydrographs in Engineering Dam Projects. *Hydrology*, *11*(11), 194. https://doi.org/10.3390/hydrology11110194

- Cortés Zambrano, M., Amaya Tequia, W. E., & Gamba-Fernández, D. S. (2020). Implementation of the hydraulic modelling of urban drainage in the northeast sector, Tunja, Boyacá. *Revista Facultad de Ingeniería Universidad de Antioquia*. https://doi.org/10.17533/udea.redin.20200798

- Corzo Perez, G. A., Sanchez Tapiero, D. I., Contreras Martínez, M. A., & Zevenbergen, C. (2024). Development of a hazard risk map for assessing pedestrian risk in urban flash floods: A case study in Cúcuta, Colombia. *River*, *3*(1), 8-23. https://doi.org/10.1002/rvr2.78

- Cubides, E., & Santos, G. (2018). Control de escorrentías urbanas mediante Sistemas Urbanos de Drenaje Sostenible (SUDS): Pozos/Zanjas de infiltración. *Entre Ciencia e Ingeniería*, *12*(24), 32-42. https://doi.org/10.31908/19098367.3813

- Damasceno-Junior, G. A., Pereira, A. d. M. M., Saharjo, B. H., Archibald, S., Zhang, B., Bilbao, B., dos Santos Ferreira, B. H., Kairumba, C. K., Ribeiro, D. B., Campbell, D. G., Njoroge, D. M., Twinomujuni, D., Jaafar, S. M., Njunge, D., Bao, F., Bortolotto, I. M., Torres, J., Dufitumukiza, J. D., Austin, K. G., ... de Oliveira Roque, F. (2025). Flood-Fire Interplays in Wetlands: The Rising of an Actionable Field of Study. *Wetlands*, *45*(8), 122. https://doi.org/10.1007/s13157-025-02005-8

- De la percepcion de la amenaza a su cuantificacion. Caso de estudio: desbordamiento del río Unete en Aguazul, Casanare, Colombia. (2021). *Investigaciones en gestion del riesgo de desastres para Colombia: Avances, perspectivas y casos de estudio*. (Sin DOI; completar autores).

- Di Franco, L. A., Guerrero Rodríguez, A. F., & Borda Prada, L. O. (2024). Diachronic spatial analysis: the case of floods in the Luján River, Argentina. *Proceedings of the 22nd LACCEI International Multi-Conference for Engineering, Education and Technology (LACCEI 2024): “Sustainable Engineering for a Diverse, Equitable, and Inclusive Future at the Service of Education, Research, and Industry for a Society 5.0.”*. https://doi.org/10.18687/laccei2024.1.1.1713

- Díaz Ramírez, J. H., Páez Martínez, H. J., Lizarralde, G., & Herazo, B. (2022). El rol de las alianzas sociales en el proceso de reconstrucción en Salgar, Colombia. *Letras Verdes. Revista Latinoamericana de Estudios Socioambientales*(31), 115-134. https://doi.org/10.17141/letrasverdes.31.2022.5092

- Diaz Riveros, C. A., Cuesta Beleño, A., Frediani, J., Rodriguez Tarducci, R., & Cortizo, D. (2023). Comparative Analysis of Spatial and Environmental Data in Informal Settlements, from Point Clouds and RPAS Images. *Communications in Computer and Information Science*, 293-308. https://doi.org/10.1007/978-3-031-46813-1_20

- Dong, X., Kou, P., Yuan, Z., Tao, Y., Yu, H., Liang, W., Chen, R., Avtar, R., & Alonso-Rodriguez, A. (2025). Extreme flood significantly altered urban ground deformation patterns: multi-source remote sensing evidence from the 2020 Chongqing flood. *Hydrological Sciences Journal*, *70*(9), 1498-1516. https://doi.org/10.1080/02626667.2025.2494866

- Duarte, Y. E., Suárez Barón, M. J., García Cabrejo, O. J., Jaramillo Acevedo, C. A., & Meneses Escobar, C. A. (2025). Deep Learning and Time Series for the Prediction of Monthly Precipitation. A Case Study in the Department of Boyacá, Colombia. *Ingeniería*, *30*(1), e21930. https://doi.org/10.14483/23448393.21930

- Echeverri-Díaz, J., Coronado-Hernández, O. E., & Pérez-Sánchez, M. (2026). A Hybrid Multicriteria Index for Assessing Documentary-Methodological Robustness in Flood Mapping: Integrating Documentary Evidence, Entropy-Based Weighting, Remote Sensing, DEMs, Hydrological Data, and Statistical Validation. *Remote Sensing*, *18*(15), 2641. https://doi.org/10.3390/rs18152641

- Fontecha, J. E., Agarwal, P., Torres, M. N., Mukherjee, S., Walteros, J. L., & Rodríguez, J. P. (2021). A Two‐Stage Data‐Driven Spatiotemporal Analysis to Predict Failure Risk of Urban Sewer Systems Leveraging Machine Learning Algorithms. *Risk Analysis*, *41*(12), 2356-2391. https://doi.org/10.1111/risa.13742

- Fragozo Arevalo, J. M., Escobar-Vargas, J., & Escobar Villanueva, J. R. (2025). Local Altimetric Correction of Global DEMs in Data-Scarce Floodplains: A Practical GNSS-Based Approach. *ISPRS International Journal of Geo-Information*, *14*(12), 498. https://doi.org/10.3390/ijgi14120498

- Garzon, L. F. L., Johnson, M. F., Mount, N., & Gomez, H. (2023). Exploring the effects of catchment morphometry on overland flow response to extreme rainfall using a 2D hydraulic-hydrological model (IBER). *Journal of Hydrology*, *627*, 130405. https://doi.org/10.1016/j.jhydrol.2023.130405

- Giraldo, J. A., del Valle, J. I., González-Caro, S., & Sierra, C. A. (2022). Intra-annual isotope variations in tree rings reveal growth rhythms within the least rainy season of an ever-wet tropical forest. *Trees*, *36*(3), 1039-1052. https://doi.org/10.1007/s00468-022-02271-7

- Giraldo, J. A., del Valle, J. I., González‐Caro, S., David, D. A., Taylor, T., Tobón, C., & Sierra, C. A. (2023). Tree growth periodicity in the ever‐wet tropical forest of the Americas. *Journal of Ecology*, *111*(4), 889-902. https://doi.org/10.1111/1365-2745.14069

- Golin, A. S., Páez Campos, H. R., Guevara Ochoa, C., Dávila, C. F., & Vives, L. S. (2024). Assessing open‐access digital elevation models for hydrological applications in a large scale plain: Drainage networks, shallow water bodies and vertical accuracy. *Earth Surface Processes and Landforms*, *49*(15), 5269-5283. https://doi.org/10.1002/esp.6035

- Gómez Sotelo, L. G., & Flórez Yepes, G. Y. (2026). Integrated index for quantifying flood risk attenuation capacity in wetlands. *Wetlands Ecology and Management*, *34*(4), 70. https://doi.org/10.1007/s11273-026-10176-2

- González-Álvarez, Á., Herrera-Piñeres, M., & Viloria-Marimón, O. M. (2022). Sensitivity of peak flow response to imperviousness increase in a tropical Caribbean ungauged urban catchment. *Urban Water Journal*, *19*(5), 509-519. https://doi.org/10.1080/1573062x.2022.2044864

- Guarda, T., Sotomayor-Cuadrado, A. J., Coronado-Hernández, O. E., Arrieta-Pastrana, A., & Coronado-Hernández, J. R. (2026). An Integrated Explicit Hydrological Routing and Machine Learning Framework for Urban Detention System Design. *Water*, *18*(4), 483. https://doi.org/10.3390/w18040483

- Guerrero-Miranda, P., & Luque González, A. (2021). Social Responsibility, Sustainability, and Public Policy: The Lessons of Debris Management after the Manabí Earthquake in Ecuador. *International Journal of Environmental Research and Public Health*, *18*(7), 3494. https://doi.org/10.3390/ijerph18073494

- Guillard, M., Navarro, O., Cortes, S., & Fleury-Bahi, G. (2021). How do we adapt when we are faced with the effects of climate change? *International Journal of Disaster Risk Reduction*, *65*, 102586. https://doi.org/10.1016/j.ijdrr.2021.102586

- Henao Salgado, M. J., & Zambrano Nájera, J. (2022). Assessing Flood Early Warning Systems for Flash Floods. *Frontiers in Climate*, *4*, 787042. https://doi.org/10.3389/fclim.2022.787042

- Henao Salgado, M. J., Alfonso, L., & Vélez Upegui, J. J. (2025). Towards integrating community and institutional flood early warning systems: A framework applied to an Andean tropical case. *International Journal of Disaster Risk Reduction*, *116*, 105126. https://doi.org/10.1016/j.ijdrr.2024.105126

- Hernández-Atencia, Y., Cutupey-Márquez, J., Rojas, I., Lizcano, D., Muñoz-Ramos, J., & Peña, L. E. (2026). Identifying physical vulnerability drivers increasing in exposed structures to floods. *Progress in Disaster Science*, *29*, 100512. https://doi.org/10.1016/j.pdisas.2025.100512

- Jiménez-U, M., Peña, L. E., & López, J. (2022). Non-stationary analysis for road drainage design under land-use and climate change scenarios. *Heliyon*, *8*(2), e08942. https://doi.org/10.1016/j.heliyon.2022.e08942

- Kreibich, H., Van Loon, A. F., Schröter, K., Ward, P. J., Mazzoleni, M., Sairam, N., Abeshu, G. W., Agafonova, S., AghaKouchak, A., Aksoy, H., Alvarez-Garreton, C., Aznar, B., Balkhi, L., Barendrecht, M. H., Biancamaria, S., Bos-Burgering, L., Bradley, C., Budiyono, Y., Buytaert, W., ... Di Baldassarre, G. (2022). The challenge of unprecedented floods and droughts in risk management. *Nature*, *608*(7921), 80-86. https://doi.org/10.1038/s41586-022-04917-5

- López-Ramos, A., Medrano-Barboza, J. P., Martínez-Acosta, L., Acuña, G. J., Remolina López, J. F., & López-Lambraño, A. A. (2022). Assessment of Morphometric Parameters as the Basis for Hydrological Inferences in Water Resource Management: A Case Study from the Sinú River Basin in Colombia. *ISPRS International Journal of Geo-Information*, *11*(9), 459. https://doi.org/10.3390/ijgi11090459

- Luna, C. C., Zambrano Nájera, J., & Vélez Upegui, J. J. (2025). Lessons learned from flash floods early warning system in a mountainous rur-urban region of Colombia. *Environmental Challenges*, *20*, 101199. https://doi.org/10.1016/j.envc.2025.101199

- Machuca, S., García-Delgado, H., & Ramos-Cañón, A. M. (2024). Assessing torrentiality in catchments of the tropical Andes: A morphometric approach. *Journal of South American Earth Sciences*, *134*, 104775. https://doi.org/10.1016/j.jsames.2023.104775

- Martínez, C., Vojinovic, Z., & Sanchez, A. (2021). Multi-Objective Model-Based Assessment of Green-Grey Infrastructures for Urban Flood Mitigation. *Hydrology*, *8*(3), 110. https://doi.org/10.3390/hydrology8030110

- Martínez, C., Vojinovic, Z., Price, R., & Sanchez, A. (2021). Modelling Infiltration Process, Overland Flow and Sewer System Interactions for Urban Flood Mitigation. *Water*, *13*(15), 2028. https://doi.org/10.3390/w13152028

- Martínez-Acosta, L., Medrano-Barboza, J., Romero, I., Ortega, V., Gómez, R., González, N., & Martinez, E. (2026). Pluvial Flood Risk Assessment in Monteverde, Monteria, Colombia, by Means of Hydrological and Hydrodynamic Models. *Lecture Notes in Networks and Systems*, 47-62. https://doi.org/10.1007/978-3-032-19845-7_4

- Masud, A., Peppa, M. V., Solano-Correa, Y. T., Mills, J. P., & Button, C. (2026). Assessment of open-source and proprietary generated digital elevation models and building footprints for urban flood modelling in Cartagena De Indias, Colombia. *Geocarto International*, *41*(1), 2681279. https://doi.org/10.1080/10106049.2026.2681279

- Medrano-Barboza, J. P., Martínez-Acosta, L., Flórez Soto, A., Acuña, G. J., Canales, F. A., David Gómez Vásquez, R., Ayala Caballero, D. A., & Sejin Cogollo, S. (2026). Model-Based Evaluation of SUDS Efficiency in Urban Stormwater Management: A Case Study in Montería, Colombia. *Hydrology*, *13*(4), 111. https://doi.org/10.3390/hydrology13040111

- Mejia Ávila, D., Martínez Lara, Z., & Soto Barrera, V. C. (2023). Space–time modelling of a tropical wetland using multiscale images, vegetation indices and landscape metrics: case—Ayapel Wetland Complex, Colombia. *International Journal of Environmental Science and Technology*, *20*(10), 10787-10810. https://doi.org/10.1007/s13762-022-04734-3

- Méndez, D. P., Niño, B. C., Pérez-Sánchez, M., Sánchez-Romero, F. J., & Coronado Hernández, Ó. E. (2026). A data-driven integrated framework for sustainable evaluation of grey–green urban drainage strategies under rainfall variability: Hydrodynamic surrogate modelling and economic assessment. *Journal of Environmental Management*, *408*, 129927. https://doi.org/10.1016/j.jenvman.2026.129927

- Méndez, D. P., Niño, B. C., Pérez-Sánchez, M., Sánchez-Romero, F. J., & Hernández, Ó. E. C. (2026). Grey–green urban drainage performance and resilience under rainfall variability: An optimal coverage framework for Quito (Ecuador). *Sustainable Cities and Society*, *147*, 107544. https://doi.org/10.1016/j.scs.2026.107544

- Meza Cueto, L., Palacio Sañudo, J., Navarro Obeid, J., Vergara Álvarez, M. L., & Navarro Villamizar, D. (2022). Differences in the levels of adaptation, social support and family functionality according to the sex, age and school grade of children and adolescents affected by winter in Sucre, Colombia. *Gaceta Médica de Caracas*, *130*(Supl. 3). https://doi.org/10.47307/gmc.2022.130.s3.5

- Montes, C., Ariza, A., Camargo, D., Sanchez, F., Carvajal, J., & Saldarriaga, J. (2022). Experimental approach of free flow to pressurized flow in sewer pipes: upstream to downstream pressurization. *Journal of Hydraulic Research*, *60*(6), 907-921. https://doi.org/10.1080/00221686.2022.2076165

- Moreno, J. M., Sánchez, J. M., & Espitia, H. E. (2020). Use of computational intelligence techniques to predict flooding in places adjacent to the Magdalena River. *Heliyon*, *6*(9), e04872. https://doi.org/10.1016/j.heliyon.2020.e04872

- Moreno-Abdelnur, A., T Bateman, J. F., Meneses Bernal, J. E., Quesada, B., & Avila-Diaz, A. (2026). Integrated flood vulnerability assessment in a data-scarce tropical mountain-to-piedmont watershed. *Environmental Research Communications*, *8*(3), 035005. https://doi.org/10.1088/2515-7620/ae47ac

- Munar, A. M., Mendez, N., Narvaez, G., Campo Zambrano, F., Motta-Marques, D., Lyra Fialho Brêda, J. P., Santos Fleischmann, A., & Angarita, H. (2023). Modelling the climate change impacts on river discharge and inundation extent in the Magdalena River basin – Colombia. *Hydrological Sciences Journal*, *68*(9), 1286-1300. https://doi.org/10.1080/02626667.2023.2215932

- Muñoz-Diaz, E. E., Vargas-Luna, A., Nuñez-Moreno, F., Florez, C. F., Alvarado, Y. A., Ruiz, D. M., Mora, Á., & Correal, J. F. (2024). A New Module for the Evaluation of Bridges Based on Visual Inspection through a Digital Application Linked to an Up-to-Date Database of Damage Catalog for Colombia. *Buildings*, *14*(4), 1150. https://doi.org/10.3390/buildings14041150

- Muñoz-Duque, L. A., Navarro, O., Restrepo-Ochoa, D., & Fleury-Bahi, G. (2021). Risk perception and trust management in inhabitants exposed to coastal flooding: The case of Cartagena, Colombia. *International Journal of Disaster Risk Reduction*, *60*, 102261. https://doi.org/10.1016/j.ijdrr.2021.102261

- Nardini, A. G. C., Pellegrini, G., Mao, L., Ariza, Y., Herrera, F., Villanueva, J. R. E., & Navarro, E. A. O. (2026). Modelling the Hydrological and Flooding Behavior of a Caribbean Basin Merging Satellite Rainfall Data and Field Data. *Water*, *18*(12), 1527. https://doi.org/10.3390/w18121527

- NAVIGATING SOCIAL AND GENDER NORMS IN EARLY CHILDHOOD: A Case Study in a Flood-Prone Area in Amazonian Perú. (2025). *Routledge Handbook of Childhood Studies and Global Development*. (Sin DOI; completar autores).

- Ortega Sandoval, A. D., Sörensen, J., Rodríguez, J. P., & Bharati, L. (2023). Hydrologic–hydraulic assessment of SUDS control capacity using different modeling approaches: a case study in Bogotá, Colombia. *Water Science & Technology*, *87*(12), 3124-3145. https://doi.org/10.2166/wst.2023.173

- Ortega, A. D., Rodríguez, J. P., & Bharati, L. (2023). Building flood-resilient cities by promoting SUDS adoption: A multi-sector analysis of barriers and benefits in Bogotá, Colombia. *International Journal of Disaster Risk Reduction*, *88*, 103621. https://doi.org/10.1016/j.ijdrr.2023.103621

- Ortega-Corredor, L. A., Pineda, A., & Rodrigues, L. C. (2025). Flood pulses reshape phytoplankton richness through aggregation, density, and species abundance distribution across floodplains. *Science of The Total Environment*, *1000*, 180402. https://doi.org/10.1016/j.scitotenv.2025.180402

- Páez Pedraza, J. P. (2025). Mud and debris flow modeling as hazard assessment tool. *Ingenieria y Universidad*, *29*. https://doi.org/10.11144/javeriana.iued29.mdfm

- Parra Saad, A., Sanabria Buitrago, M., Sanabria, R., & Piñeros Dueñas, K. N. (2024). Incorporación de factores socioeconómicos al análisis de vulnerabilidad del riesgo por inundación en vías usando un modelo geoespacial. *Investigaciones Geográficas*(81), 201-223. https://doi.org/10.14198/ingeo.25788

- Pasqualotto, A. C., Vieceli, T., Würdig Riche, C. V., de Carvalho Hessel Dias, V. M., Ballalai, I., Cunha, J., Morejón, K. M. L., Weissmann, L., Chaves, T. d. S. S., Lucca, M. B., Mafaciolli, R., Bonamigo, R. R., Barth, A. L., Martins, A. F., Antochevis, L. C., Caierão, J., Motta, F. d. A., Scotta, M. C., Heinzelmann, R. S., ... Motta, F. (2026). Floods and infectious diseases: public health lessons from the 2024 southern Brazil disaster. *Clinical Microbiology Reviews*, *39*(1), e00165-24. https://doi.org/10.1128/cmr.00165-24

- Patwary, M. M., & Rodriguez-Morales, A. J. (2022). Deadly Flood and Landslides amid COVID-19 Crisis: A Public Health Concern for the World’s Largest Refugee Camp in Bangladesh. *Prehospital and Disaster Medicine*, *37*(2), 292-293. https://doi.org/10.1017/s1049023x22000164

- Pérez-Montiel, J. I., Cardenas-Mercado, L., & Nardini, A. G. C. (2022). Flood Modeling in a Coastal Town in Northern Colombia: Comparing MODCEL vs. IBER. *Water*, *14*(23), 3866. https://doi.org/10.3390/w14233866

- Pescador, J., Silva, L., Lora-Ariza, B., Landinez, J. F., Vaca, M., Romero, P., Piña, A., & Donado, L. D. (2026). Local-Scale Groundwater Modeling of Surface–Groundwater Interaction in a Complex Hydrological Setting. *Hydrology*, *13*(7), 179. https://doi.org/10.3390/hydrology13070179

- Pinto Argel, S., Quiróz, H. T., Narvaez-Campo, G., Campo Zambrano, F., Rosso Pinto, M., & Cardenas de la Ossa, J. (2026). Integrated Hydrological–Hydraulic Framework for Urban Flood Risk Management in Montería, Colombia: From 2D Modeling and Vulnerability Assessment to Structural, Non-Structural, and Emergency Intervention Measures. *Water*, *18*(13), 1576. https://doi.org/10.3390/w18131576

- Purwar, D., Flacke, J., Guzman, E. A., & Sliuzas, R. (2024). A qualitative analysis of cascading effects of critical infrastructure service failure post torrential floods in formal & informal settlement: the study-case of Medellin city, Colombia. *Sustainable and Resilient Infrastructure*, *9*(5), 496-512. https://doi.org/10.1080/23789689.2024.2340924

- Ramírez-Quele, G. A., González-Pérez, M. G., Flores-Vilchez, F., Asprilla-Lara, Y., & Rodríguez-Rodríguez, J. (2020). Efficiency of underground retention systems and reduction of urban floods in Tepic, Mexico. *Revista Facultad de Ingeniería Universidad de Antioquia*(99), 63-72. https://doi.org/10.17533/udea.redin.20200585

- Ramos-Cañón, A. M., Munévar, M., Prada-Sarmiento, L. F., Escobar-Vargas, J., Vargas-Luna, A., Prieto, A. F., Reyes, N. C., Medina, M., Pérez, J., & Dorado, L. (2023). Redundancia de los umbrales del sistema de alerta temprana para avenidas torrenciales de Mocoa, Putumayo, Colombia. *Revista de Estudios Latinoamericanos sobre Reducción del Riesgo de Desastres REDER*, *7*(2), 142. https://doi.org/10.55467/reder.v7i2.129

- Renteria-Mena, J. B., Plaza, D., & Giraldo, E. (2023). Multivariable NARX Based Neural Networks Models for Short-Term Water Level Forecasting. *ITISE 2023*, 60. https://doi.org/10.3390/engproc2023039060

- Renteria-Mena, J. B., Plaza, D., & Giraldo, E. (2024). Comparative Analysis of Nonlinear Methods for Multivariable Water Level Prediction: The Case Study of the Atrato River. *Journal of Electrical and Computer Engineering*, *2024*(1), 2894031. https://doi.org/10.1155/2024/2894031

- Saldarriaga, J., Salcedo, C., Solarte, L., Pulgarín, L., Rivera, M. L., Camacho, M., Iglesias-Rey, P. L., Martínez-Solano, F. J., & Cunha, M. (2020). Reducing Flood Risk in Changing Environments: Optimal Location and Sizing of Stormwater Tanks Considering Climate Change. *Water*, *12*(9), 2491. https://doi.org/10.3390/w12092491

- Samadi, V., Fowler, H. J., Lamond, J., Wagener, T., Brunner, M., Gourley, J., Moradkhani, H., Popescu, I., Wasko, C., Wright, D., Wu, H., Zhang, K., Arias, P. A., Duan, Q., Nazemi, A., van Oevelen, P. J., Prein, A. F., Roundy, J. K., Saberian, M., & Umutoni, L. (2025). The Needs, Challenges, and Priorities for Advancing Global Flood Research. *WIREs Water*, *12*(3), e70026. https://doi.org/10.1002/wat2.70026

- Sanabria, R. A., Gómez, C. F., Vaca, F. J., Sánchez, J. D., Aldana, D., & Franco, A. (2021). Communication Architecture for the Ponding Flood Prediction Model. *2021 International Symposium on Computer Science and Intelligent Controls (ISCSIC)*, 180-184. https://doi.org/10.1109/iscsic54682.2021.00042

- Sanvitale, N., Bowman, E., & Cabrera, M. A. (2021). Experimental Investigation on the Impact Dynamics of Saturated Granular Flows on Rigid Barriers. *Environmental and Engineering Geoscience*, *27*(1), 127-138. https://doi.org/10.2113/eeg-d-20-00033

- Schasfoort, N., Hoogesteger, J., & Duarte-Abadía, B. (2026). Hydrosocial river modernization: The enclosure of amphibious cultures in Canal del Dique, Colombia. *Environment and Planning E: Nature and Space*, 25148486261461999. https://doi.org/10.1177/25148486261461999

- Sedano, K., Carvajal-Escobar, Y., López-De la Cruz, J., & Francés, F. (2020). Modelación no estacionaria de la magnitud y frecuencia de las crecidas en el Alto Cauca mediante índices climáticos y de operación de embalse. *Tecnología y ciencias del agua*, *11*(3), 27-77. https://doi.org/10.24850/j-tyca-2020-03-02

- Smolíková, J., Hrbáček, F., Blahůt, J., Klimeš, J., Vilímek, V., & Loaiza Usuga, J. C. (2021). Analysis of the rainfall pattern triggering the Lemešná debris flow, Javorníky Range, the Czech Republic. *Natural Hazards*, *106*(3), 2353-2379. https://doi.org/10.1007/s11069-021-04546-7

- Souza, F. A. A., Bhattacharya Mis, N., Carolina Sarmento Buarque, A., José de Oliveira Sousa, B., Fialho, H. C. P., Abreu, F. G., Clara Fava, M., Restrepo-Estrada, C., Sanches de Oliveira, P. T., & Mendiondo, E. M. (2024). Evolution of social engagement in flood risk assessment: new approaches and emerging concerns using case studies from Brazil. *Research Handbook on Flood Risk Management*, 52-69. https://doi.org/10.4337/9781839102981.00011

- Suarez Castillo, C. R., Sañudo-Fontaneda, L. A., Roces-García, J., & Rodríguez, J. P. (2026). Fostering Amenity Criteria for the Implementation of Sustainable Urban Drainage Systems in Public Spaces: A Novel Decision Methodological Framework. *Applied Sciences*, *16*(2), 901. https://doi.org/10.3390/app16020901

- Trujillo-Vela, M. G., Ramos-Cañón, A. M., Escobar-Vargas, J. A., & Galindo-Torres, S. A. (2022). An overview of debris-flow mathematical modelling. *Earth-Science Reviews*, *232*, 104135. https://doi.org/10.1016/j.earscirev.2022.104135

- Trujillo-Vela, M., Galindo-Torres, S., Zhang, X., Ramos-Cañón, A., & Escobar-Vargas, J. (2021). SPH-DEM Coupling for Debris Flows. *14th WCCM-ECCOMAS Congress*. https://doi.org/10.23967/wccm-eccomas.2020.316

- Valencia Amaya, M. G. (2020). Climate shocks and human capital: The impact of the natural disasters of 2010 in Colombia on student achievement. *Cuadernos de Economía*, *39*(79), 303-328. https://doi.org/10.15446/cuad.econ.v39n79.56830

- Valencia Londoño, P. A., & Valencia Londoño, D. (2024). Persistent Vulnerability after Disaster Risk Reduction (DRR) Response: The Case of Salgar, Colombia. *Sustainability*, *16*(11), 4394. https://doi.org/10.3390/su16114394

- van der Werf, J. A., Pons, V., Smyth, K., Shi, B., Lechevallier, P., Abdalla, E. M. H., Andrusenko, E., Broekhuizen, I., Cavadini, G. B., Cortés Moreno, A. F., Cristiano, E., D'Ambrosio, R., Droste, A. M., Evangelisti, M., Fernandes, G., Garzón, A., Girot, E., Guericke, L., Liao, W., ... Yerima, H. Z. (2025). Flooded with potential: urban drainage science as seen by early-career researchers. *Water Science & Technology*, *91*(7), 861-875. https://doi.org/10.2166/wst.2025.045

- Villalba-Barrios, A. F., Coronado-Hernández, O. E., Fuertes-Miquel, V. S., Coronado-Hernández, J. R., & Ramos, H. M. (2023). Statistical Approach for Computing Base Flow Rates in Gaged Rivers and Hydropower Effect Analysis. *Hydrology*, *10*(7), 137. https://doi.org/10.3390/hydrology10070137

- Villegas González, P. A. (2021). “Gestión del riesgo por inundaciones. Un metamodelo para el desarrollo de artefactos participativos” modelos integrados de sistemas socio-ecológicos : caso de estudio en la ecorregión de La Mojana (Colombia). *Investigaciones en gestion del riesgo de desastres para Colombia: Avances, perspectivas y casos de estudio*. https://doi.org/10.11144/javeriana.10554.55023

- Xu, J., Dronova, I., Tinoco, V., Kephart, J. L., Bilal, U., Sanchez, B. N., Diez Roux, A. V., Gouveia, N., Sarmiento, O. L., Vives, A., Alazraqui, M., & Rodriguez, D. A. (2026). Heterogeneity in Flood Hazard Exposure in 363 Latin American Cities. *Ecosystem Health and Sustainability*, *12*, 0567. https://doi.org/10.34133/ehs.0567

- Zambrano Nájera, J., & Rey, D. M. (2022). Assessment of Storm Floods in a Small Tropical Andean Basins. *Frontiers in Climate*, *4*, 760894. https://doi.org/10.3389/fclim.2022.760894
