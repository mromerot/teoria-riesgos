---
title: Tsunami
---

# Tsunami

:::{image} ../../estilo/ilustraciones/tsunami.svg
:alt: Ola de tsunami que se acerca a una costa con casas
:class: ilustracion
:width: 100%
:::

Este capítulo sigue el molde de siete puntos ([](_molde.md)). El tsunami de origen sísmico es una amenaza secundaria del sismo: comparte con él la fuente y la lógica probabilista ([](301_sismo.md)), pero el daño lo produce el agua, por lo que su vulnerabilidad y su exposición son las de una inundación costera rápida.

## 1. Fenómeno

Un tsunami es una serie de olas de gran longitud de onda que ocurre generalmente por sismos en el fondo marino o cerca de la costa. También puede originarse por erupciones volcánicas, deslizamientos submarinos o impacto de meteoritos {cite:p}`ungrd2019atlas`. Inunda rápidamente las áreas costeras bajas y puede avanzar río arriba por las desembocaduras, afectando a las poblaciones cercanas a los cauces {cite:p}`ungrd2019atlas`.

El Atlas distingue tres procesos físicos: la **generación** (movimiento vertical de una gran masa de agua), la **propagación** por el océano y el **arribo**, en el que la ola se amplifica al disminuir la profundidad {cite:p}`ungrd2019atlas`. Para el análisis de riesgo solo importan las condiciones de arribo e impacto {cite:p}`ungrd2019atlas`.

| Rasgo | Valor según el Atlas {cite:p}`ungrd2019atlas` |
|---|---|
| Velocidad en mar abierto | Alrededor de 800 km/h en promedio |
| Amplitud lejos de la costa | No es significativa |
| Origen lejano | Puede tardar horas en llegar |
| Origen cercano | Puede tardar solo minutos en llegar |
| Altura en la costa | Depende de la batimetría, las irregularidades de la costa y la topografía tierra adentro |

**Variable de intensidad.** La profundidad de inundación y la altura máxima de la ola. La velocidad de la corriente importa para el daño estructural.

### Tsunami en Colombia

La mayor amenaza está en la **costa Pacífica**, expuesta a fuentes cercanas en la zona de subducción de la placa de Nazca bajo la suramericana y a fuentes lejanas en el Cinturón de Fuego. Hay registros de eventos de origen cercano en 1882, 1904, 1906, 1942, 1958 y 1979, y dos desastres, los de 1906 y 1979, siendo este último grave para Tumaco {cite:p}`ungrd2019atlas`.

En el **Caribe** continúan las investigaciones sobre fuentes locales, como sismos y deslizamientos submarinos. Estudios con fuentes cercana (Cinturón Deformado del Norte de Panamá) y lejana (Arco de las Antillas Menores) concluyen que las alturas de ola probables no superan significativamente las que produce la interacción océano–atmósfera. Para San Andrés y Providencia, no se identificó ninguna fuente probable que genere olas de más de decímetros {cite:p}`ungrd2019atlas`.

```{important}
La amenaza es mayor en el Pacífico, pero las pérdidas podrían ser mayores en el Caribe por la concentración de población e infraestructura {cite:p}`ungrd2019atlas`. Un análisis de riesgo no debe descartar el Caribe solo por su menor amenaza.
```

### Definición según los HIPs de UNDRR

Los perfiles de información de amenazas ([](../01_conceptos/16_hips_undrr.md)) que corresponden a este capítulo son:

| Código | Perfil (clúster) | Definición (traducción propia) |
|---|---|---|
| MH0705 | Tsunami (meteorológico e hidrológico, marino) | Término japonés que significa «ola» en el puerto; designa una serie de ondas viajeras de largo periodo, causadas típicamente por perturbaciones como terremotos bajo o cerca del fondo oceánico (COI, 2019). |

Fuente: {cite:p}`undrr2025hips`.

**Qué se incluye y por qué.**

- **Se incluye** la definición de la COI: sirve para el capítulo, que describe la generación, la propagación y la llegada de la ola.
- **Clasificación.** Los HIPs ubican el tsunami entre los peligros meteorológicos e hidrológicos (clúster marino), aunque su origen típico sea geológico. El libro lo trata aquí, junto a sus causas, y se anota la diferencia para no confundir al clasificar.
- **Causas y efectos.** Los HIPs lo registran como causado por terremotos, movimientos en masa, impactos de meteoritos y desechos espaciales, y como causa de inundación costera y estuarina, erosión costera, intrusión salina, enfermedades transmitidas por el agua y fallas de infraestructura {cite:p}`undrr2025hips`. Ver [](305_inundacion.md) y [](306_erosion_costera.md).

## 2. Amenaza

### Dos enfoques

| Enfoque | Qué entrega | Ejemplo |
|---|---|---|
| **Determinista** | Profundidad y extensión de inundación del peor escenario creíble | Guapi, Cauca: modelo TUNAMI N2, deformación del fondo con el modelo de Okada y batimetría GEBCO {cite:p}`sanchez2023guapi` |
| **Probabilista** | Profundidad por periodo de retorno | Evaluación global NGI y GA (2014) usada en el Atlas: mapas para 475 años en Pacífico y Caribe {cite:p}`ungrd2019atlas` |

La evaluación probabilista aporta frecuencia de ocurrencia y profundidad del agua, que es lo necesario para calcular el riesgo. Aunque su resolución es global, el Atlas la considera consistente con la amenaza existente a lo largo de toda la costa {cite:p}`ungrd2019atlas`.

### Cadena de modelación

Los estudios de la DIMAR para las bahías de Tumaco y Buenaventura, Málaga y el golfo de Cúpica incluyen {cite:p}`ungrd2019atlas`:

1. Definir escenarios sismotectónicos generadores de tsunami.
2. Calcular la deformación sísmica que fija las condiciones iniciales.
3. Propagar las ondas largas en aguas someras.
4. Evaluar el impacto en la costa con información topo-batimétrica a distintas resoluciones.

Para la **generación**, el sistema agua–lecho puede tratarse como acoplado (las ondas sísmicas influyen en la masa de agua) o desacoplado (la deformación elástica de la corteza se considera despreciable). Para la **propagación** se aplica generalmente la teoría de ondas en aguas poco profundas, válida cuando la longitud de onda es mucho mayor que la profundidad {cite:p}`ungrd2019atlas`.

```{warning}
El caso de Guapi es un método determinista con un solo modelo sobre una morfología costera deltaica. Sus propios autores recomiendan estudios adicionales para descartar una subestimación de la amenaza {cite:p}`sanchez2023guapi`.
```

Existe además una evaluación de la amenaza para la costa Pacífica central y sur de Colombia {cite:p}`escobar2020tsunami`, que debe consultarse para su método y resultados antes de aplicarlo a una ciudad.

### Qué enseña la simulación de un escenario

Los dos primeros pasos de la cadena (fuente y deformación) y el tercero (propagación) se pueden ejecutar con herramientas abiertas. Lo que sigue resume lo aprendido al reproducir el tsunami de 1979 en un cuaderno piloto, y qué decisiones de método se desprenden.

**Generación.** La deformación vertical del fondo de una falla rectangular se calcula con el modelo de dislocación elástica de {cite:t}`okada1985` y se toma como la elevación inicial de la superficie del agua, con deslizamiento $D = M_0/(\mu L W)$ y $M_0 = 10^{1{,}5 M_w + 9{,}1}$ N·m. Es el modelo con el que {cite:t}`sanchez2023guapi` calculan la deformación en Guapi; {cite:t}`escobar2020tsunami` parten de distribuciones de deslizamiento sobre la falla. Para Mw 8,3, 200 × 80 km y 30 GPa, el deslizamiento es de 7,4 m y la deformación va de +3,1 m a −1,3 m. **Calibrar la amplitud de una onda inicial para compensar un esquema difusivo no es una alternativa:** la primera versión del piloto lo hizo, con un pico inicial de 16 m, y ese número no tiene significado físico.

**Propagación.** La celeridad $c=\sqrt{gH}$ da unos 200 m/s sobre 4 000 m. Para tiempos de arribo bastan las ecuaciones de aguas someras **lineales**; para profundidad de inundación hacen falta las **no lineales** con celda seca y fricción (criterio del piloto; no está en las fuentes citadas aquí). El esquema numérico importa: una malla escalonada *forward-backward* conserva el 99,96 % de la amplitud de una onda plana tras 119 km, y Lax-Friedrichs conserva el 43 %. **Un solver nuevo se verifica con una onda plana y con un reposo exacto antes de usarlo**, y la fuente con una implementación independiente.

**Lectura en la costa.** Un modelo lineal sin fricción sobreestima la elevación en aguas someras y no calcula run-up. El piloto lee cada estación en la celda de mar más cercana con al menos 10 m de profundidad y excluye las que no tienen mar de esa profundidad cerca (varias coordenadas de la tabla de observaciones caen tierra adentro o en estuarios).

El cuaderno piloto de la Subdirección para el Conocimiento del Riesgo de la UNGRD simula el 12 de diciembre de 1979 con Okada, malla escalonada y 450 m de resolución ([cuadernos-reproducibles-crc003](https://scr-ungrd.github.io/cuadernos-reproducibles-crc003/), versión 2, licencia MIT). Sus resultados:

| Resultado | Valor | Lectura |
|---|---|---|
| Primer ascenso en Tumaco | 23 min; entre 21 y 26 min al variar la fuente y la resolución | Robusto. El modelo no lineal de {cite:t}`avila2026` da 22 min |
| Elevación máxima en celdas de mar de 10–25 m, Tumaco | 8,2–8,8 m; entre 4,2 y 8,8 m al variar la fuente | **Sensible a la fuente y sobreestimada**: {cite:t}`escobar2020tsunami` simulan 1,88–2,30 m para la isla de Tumaco en el escenario de 1979 |
| Forma de la señal | Descenso inicial y varias crestas durante 30–45 min; la máxima no es la primera | Un plan de evacuación no termina con el primer ascenso |

La geometría de la falla de ese piloto es un **supuesto** (no tiene la distribución de deslizamiento de Poveda y Pulido, 2019, en que se basan los dos estudios anteriores), y sus observaciones de 1979 están sin verificar. Por eso sirve como flujo de trabajo y como análisis de sensibilidad, no como mapa de amenaza. El cuaderno [](318_tsunami_tumaco_1979.ipynb) usa su tabla de observaciones para dos comprobaciones previas a cualquier calibración:

- **Run-up y distancia.** Los valores mayores están cerca de la fuente (hasta 5 m en el muelle de Tumaco) y bajan a 0,8 m en Buenaventura. Esas cifras duplican las alturas simuladas por {cite:t}`escobar2020tsunami`, otra razón para verificarlas.
- **Coherencia de los tiempos de arribo.** Los 15 minutos hasta Tumaco corresponden a una profundidad equivalente de unos 600 m, coherente con una plataforma y un talud. El arribo de Salinas (35 minutos a unos 460 km) exige una profundidad de unos 4 900 m a lo largo de toda la ruta, mayor de la esperable, por lo que ese dato es sospechoso hasta contrastarlo con la fuente.

**Lección para el análisis de una ciudad:** los datos históricos con los que se calibra un modelo de tsunami deben revisarse contra la física de la onda larga y contra las fuentes primarias antes de ajustar parámetros; y una simulación de escenario entrega con confianza el **tiempo de arribo** y con poca confianza la **amplitud**, mientras no se tenga la distribución de deslizamiento y un modelo no lineal.

## 3. Exposición

Los municipios costeros expuestos suman cerca de siete millones de habitantes (seis millones en el Caribe y uno en el Pacífico), el 16 % de la población, según el Atlas {cite:p}`ungrd2019atlas`. Los departamentos expuestos son Nariño, Cauca, Valle del Cauca y Chocó en el Pacífico, y La Guajira, Bolívar, Atlántico, Magdalena, Sucre, Córdoba, Antioquia, Chocó y San Andrés y Providencia en el Caribe {cite:p}`ungrd2019atlas`. El municipio con mayor población expuesta y probabilidad de pérdidas es Tumaco {cite:p}`ungrd2019atlas`.

El Atlas incluye los mapas de inundación por tsunami de origen cercano para las bahías de Tumaco y Buenaventura (DIMAR, 2014). Los datos del Atlas son de 2019 y las cifras de población deben actualizarse.

## 4. Vulnerabilidad

La vulnerabilidad física se modela con **funciones de fragilidad** que dan la probabilidad de daño de un edificio según un parámetro de demanda, típicamente la profundidad de inundación. En el Pacífico colombiano no se registró el daño físico de los eventos del siglo XX, lo que aumenta la incertidumbre del impacto futuro. Por eso se comparan funciones empíricas, construidas con daños observados en otras regiones, con funciones analíticas, para los edificios de Tumaco {cite:p}`paez2021tsunamifrag`.

La vulnerabilidad también incluye el tiempo disponible para evacuar. En fuente cercana puede ser solo de minutos {cite:p}`ungrd2019atlas`; para Tumaco, un modelo no lineal da 22 minutos hasta la primera ola {cite:p}`avila2026`. Ese factor no está en las curvas de daño y se aborda en las medidas del punto 7.

## 5. Riesgo

- **Probabilista.** Con profundidades por periodo de retorno, exposición y fragilidad se obtienen la curva de excedencia de pérdidas y la PAE ({cite:p}`ungrd2019atlas`; ver [](../02_metodologia/22_probabilista_pae.md)).
- **Escenario.** El peor escenario creíble sirve para planes de emergencia. El estudio del Programa de Mitigación de Riesgo por Tsunami en Tumaco simuló un evento de fuente cercana (1979, zona de subducción colombo–ecuatoriana) y uno de fuente lejana (1960, Chile). Los eligieron porque sus resultados se parecían a testimonios y datos mareográficos de 1979 {cite:p}`ungrd2019atlas`.

El mapa de peor escenario en Guapi muestra una altura máxima de 3,3 m, una distancia de inundación de 0,103 km, un área de 0,4 km² y una profundidad de inundación de 0,3 m {cite:p}`sanchez2023guapi`. Son resultados de un caso, no valores de referencia para otras ciudades.

## 6. Clima

Los tsunamis de origen tectónico no dependen del clima, como los sismos {cite:p}`ccdr2025tools`. Lo que sí cambia es el nivel del mar sobre el que ocurre la inundación. Como criterio de método de este libro, la profundidad de inundación de un escenario futuro debe sumar el ascenso del nivel del mar proyectado, tratado en [](306_erosion_costera.md). Esta combinación no la plantean las fuentes citadas aquí y debe verificarse en la literatura de amenazas compuestas.

## 7. Datos y medidas

### Datos y sistemas

| Elemento | Qué es | Referencia |
|---|---|---|
| Sistema Nacional de Detección y Alerta de Tsunami (SNDAT) | Seis instituciones, entre ellas OSSO, SGC, DIMAR, IDEAM y UNGRD, con roles definidos para declarar estados de alerta ante tsunamis de origen local, regional o lejano | {cite:p}`ungrd2019atlas` |
| Protocolo Nacional de Detección y Alerta de Tsunami | Operado por el SNDAT | {cite:p}`ungrd2019atlas` |
| Comisión Colombiana del Océano | Coordina alertas internacionales con los países del Pacífico y el Caribe | {cite:p}`ungrd2019atlas` |
| DIMAR | Escenarios, modelos de propagación y mapas de inundación | {cite:p}`ungrd2019atlas` |

Una propuesta reciente es un modelo de lógica difusa para emitir niveles de alerta a partir de parámetros sísmicos y oceanográficos de entrada, como apoyo a la decisión en alerta temprana (ID 835 de la hoja de vigilancia, DOI en la base).

### Incertidumbres principales

- Sin registros de daño físico de eventos colombianos, las fragilidades dependen de otras regiones {cite:p}`paez2021tsunamifrag`.
- La geometría de la falla puede cambiar la amplitud en la costa por un factor de 2 (4,2 a 8,8 m en Tumaco en el análisis de sensibilidad del cuaderno piloto) y apenas mueve el tiempo de arribo (21 a 26 min). Ese análisis varía un parámetro a la vez: no es una cuantificación de la incertidumbre.
- Fuentes del Caribe aún en investigación {cite:p}`ungrd2019atlas`.
- Resolución global de la amenaza probabilista {cite:p}`ungrd2019atlas`.

### Medidas según la Ley 1523

| Proceso | Medida | Fuente |
|---|---|---|
| Conocimiento | Mapas de inundación, monitoreo, simulación numérica | {cite:p}`ungrd2019atlas` |
| Reducción: prevención | Ordenamiento territorial (aplicado en Tumaco) | {cite:p}`ungrd2019atlas` |
| Reducción: mitigación | Planes de acción preventiva en zonas costeras; la primera propuesta de mitigación data del estudio posterior al evento de 1906 | {cite:p}`ungrd2019atlas` |
| Manejo | Rutas de evacuación, alerta temprana, planes de respuesta, programas educativos | {cite:p}`ungrd2019atlas` |

## Síntesis de evidencia

```{note}
**Método.** Síntesis narrativa por tipo de evidencia (no un metaanálisis con efectos agrupados: los estudios usan diseños, escalas y variables que no se pueden combinar en un solo estimador). Se leyeron los resúmenes de los artículos de la hoja de vigilancia que están en la carpeta de PDFs; las cifras vienen de esos resúmenes y **faltan por verificar contra el texto completo**.
```

| Estudio | Diseño y lugar | Resultado relevante |
|---|---|---|
| {cite:t}`escobar2020tsunamib` | Escenarios deterministas con modelos de déficit de deslizamiento, costa pacífica de Colombia | En el peor escenario la altura máxima fue 4,66 m en la isla de Tumaco y 4,34 m en El Morro; el 11 % y el 10 % de esas islas tendrían profundidades de inundación de 2 a 5 m |
| {cite:t}`lizarazo2021interplate` | Inversión de datos GPS, Caribe noroccidental colombiano | Estima el acoplamiento entre placas para evaluar el potencial sísmico y de tsunami, donde no hay megaterremotos registrados en 500 años |
| {cite:t}`gonzalez2021probabilistic` | Método probabilista de amenaza de tsunami, bahía de Cádiz (España) | Aplica el enfoque a zonas con marea meso y macromareal; referencia metodológica, no colombiana |
| {cite:t}`cabrera2020generation` | Experimentos de laboratorio y modelo analítico | La amplitud máxima de la ola por deslizamiento depende de una sola razón adimensional, la sumersión relativa |

**Lectura conjunta.** La evidencia revisada indica que el análisis de tsunami en Colombia descansa en escenarios deterministas del Pacífico y en estimaciones indirectas del Caribe, lo que limita el cálculo probabilista de la pérdida anual esperada.

- **Pacífico y Caribe se evalúan con métodos distintos.** En el Pacífico hay tsunamis históricos (1906, 1979) y escenarios deterministas; en el Caribe solo hay estimaciones indirectas de acoplamiento, sin eventos recientes {cite:p}`escobar2020tsunamib,lizarazo2021interplate`. Esto confirma que el análisis de una ciudad caribeña debe declarar mayor incertidumbre de la fuente.
- **Deterministas frente a probabilistas.** Los estudios colombianos revisados son deterministas; el enfoque probabilista aparece en la referencia española {cite:p}`gonzalez2021probabilistic`. Para calcular PAE ([](../02_metodologia/22_probabilista_pae.md)) hace falta el segundo.
- **Fuente no sísmica.** Los deslizamientos pueden generar olas con una ley simple de escala {cite:p}`cabrera2020generation`, relevante para costas con laderas sumergidas.

## Pendiente

- Leer {cite:p}`escobar2020tsunami` y {cite:p}`paez2021tsunamifrag` completos. Hoy se citan por título y resumen.
- Contrastar la tabla de observaciones de 1979 (el arribo de Salinas; las coordenadas de San Juan, El Charco y Buenaventura; las cifras de run-up frente a los 1,88–2,30 m de {cite:p}`escobar2020tsunami`) con Herd et al. (1981) y la base de la NOAA.
- Reemplazar la falla supuesta del piloto por la distribución de deslizamiento de Poveda y Pulido (2019) y repetir la simulación con ecuaciones no lineales y celda seca.
- Añadir la fuente primaria de la evaluación global (NGI y GA, 2014) y la del modelo de arribo (Madsen y Fuhrman, 2009), que el Atlas cita.
- Verificar con la literatura la combinación tsunami y ascenso del nivel del mar (punto 6).

## Bibliografía recomendada

Lista de los 9 registros de la hoja de vigilancia científica (pestaña `Vigilancia_CTeI`, columna `AMENAZA_ESPECIFICA` = «Tsunami»), en formato APA 7 con metadatos de Crossref. Son lecturas recomendadas: **no están verificadas contra el texto completo** ni se usan como evidencia hasta que se citen en el capítulo. Las entradas sin DOI carecen de autores en la hoja.

- Alerting tsunamis: a fuzzy logic model. (2025). *Congreso Internacional De Innovacion Y Tendencias*. `doi:10.1109/coniiti…(número de artículo: 11366132)` (no resuelve en Crossref; corregir en la hoja)

- Cabrera, M. A., Pinzon, G., Take, W. A., & Mulligan, R. P. (2020). Wave Generation Across a Continuum of Landslide Conditions From the Collapse of Partially Submerged to Fully Submerged Granular Columns. *Journal of Geophysical Research: Oceans*, *125*(12), e2020JC016465. https://doi.org/10.1029/2020jc016465

- El costo economico de los desastres naturales: el caso del tsunami y la emergencia nuclear en Japon en 2011. (2020). *Lecturas de Economia*. `doi:10.17533/udea.le.n93ia340531` (no resuelve en Crossref; corregir en la hoja)

- Escobar, R. S., Diaz, L. O., Guerrero, A. M., Galindo, M. P., Mas, E., Koshimura, S., Adriano, B., Urra, L., & Quintero, P. (2020). Tsunami hazard assessment for the central and southern pacific coast of Colombia. *Coastal Engineering Journal*, *62*(4), 540-552. https://doi.org/10.1080/21664250.2020.1818362

- González, M., Álvarez-Gómez, J. A., Aniel-Quiroga, Í., Otero, L., Olabarrieta, M., Omira, R., Luceño, A., Jelinek, R., Krausmann, E., Birkman, J., Baptista, M. A., Miranda, M., & Aguirre-Ayerbe, I. (2021). Probabilistic Tsunami Hazard Assessment in Meso and Macro Tidal Areas. Application to the Cádiz Bay, Spain. *Frontiers in Earth Science*, *9*, 591383. https://doi.org/10.3389/feart.2021.591383

- IMPACT AND RESPONSE IN CENTRAL AND SOUTH AMERICA DUE TO THE TSUNAMI GENERATED BY THE SUBMARINE ERUPTION OF HUNGA TONGA-HUNGA HA’APAI VOLCANO. (2022). *Science of Tsunami Hazards*. (Sin DOI; completar autores).

- Lizarazo, S. C., Sagiya, T., & Mora-Páez, H. (2021). Interplate coupling along the Caribbean coast of Colombia and its implications for seismic/tsunami hazards. *Journal of South American Earth Sciences*, *110*, 103332. https://doi.org/10.1016/j.jsames.2021.103332

- Lizarazo, S. C., Sagiya, T., & Mora-Páez, H. (2024). Viscoelastic earthquake cycle model for the Caribbean subduction zone in northwestern Colombia: Implications of coastal subsidence for seismic/tsunami hazards. *Journal of South American Earth Sciences*, *141*, 104931. https://doi.org/10.1016/j.jsames.2024.104931

- Paez-Ramirez, J., Lizarazo, J., Medina, S., Rivas, M., Luna, P., Mas, E., & Koshimura, S. (2021). A comparative analysis of empirical and analytical tsunami fragility functions for buildings in Tumaco, Colombia. *IOP Conference Series: Earth and Environmental Science*, *630*(1), 012008. https://doi.org/10.1088/1755-1315/630/1/012008
