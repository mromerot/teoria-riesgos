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

## 3. Exposición

Los municipios costeros expuestos suman cerca de siete millones de habitantes (seis millones en el Caribe y uno en el Pacífico), el 16 % de la población, según el Atlas {cite:p}`ungrd2019atlas`. Los departamentos expuestos son Nariño, Cauca, Valle del Cauca y Chocó en el Pacífico, y La Guajira, Bolívar, Atlántico, Magdalena, Sucre, Córdoba, Antioquia, Chocó y San Andrés y Providencia en el Caribe {cite:p}`ungrd2019atlas`. El municipio con mayor población expuesta y probabilidad de pérdidas es Tumaco {cite:p}`ungrd2019atlas`.

El Atlas incluye los mapas de inundación por tsunami de origen cercano para las bahías de Tumaco y Buenaventura (DIMAR, 2014). Los datos del Atlas son de 2019 y las cifras de población deben actualizarse.

## 4. Vulnerabilidad

La vulnerabilidad física se modela con **funciones de fragilidad** que dan la probabilidad de daño de un edificio según un parámetro de demanda, típicamente la profundidad de inundación. En el Pacífico colombiano no se registró el daño físico de los eventos del siglo XX, lo que aumenta la incertidumbre del impacto futuro. Por eso se comparan funciones empíricas, construidas con daños observados en otras regiones, con funciones analíticas, para los edificios de Tumaco {cite:p}`paez2021tsunamifrag`.

La vulnerabilidad también incluye el tiempo disponible para evacuar. En fuente cercana puede ser solo de minutos {cite:p}`ungrd2019atlas`. Ese factor no está en las curvas de daño y se aborda en las medidas del punto 7.

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

**Lectura conjunta.**

- **Pacífico y Caribe se evalúan con métodos distintos.** En el Pacífico hay tsunamis históricos (1906, 1979) y escenarios deterministas; en el Caribe solo hay estimaciones indirectas de acoplamiento, sin eventos recientes {cite:p}`escobar2020tsunamib,lizarazo2021interplate`. Esto confirma que el análisis de una ciudad caribeña debe declarar mayor incertidumbre de la fuente.
- **Deterministas frente a probabilistas.** Los estudios colombianos revisados son deterministas; el enfoque probabilista aparece en la referencia española {cite:p}`gonzalez2021probabilistic`. Para calcular PAE ([](../02_metodologia/22_probabilista_pae.md)) hace falta el segundo.
- **Fuente no sísmica.** Los deslizamientos pueden generar olas con una ley simple de escala {cite:p}`cabrera2020generation`, relevante para costas con laderas sumergidas.

## Pendiente

- Leer {cite:p}`escobar2020tsunami` y {cite:p}`paez2021tsunamifrag` completos. Hoy se citan por título y resumen.
- Enlazar el cuaderno reproducible del tsunami de Tumaco de 1979 como ejemplo aplicado.
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

- Lizarazo, S. C., Sagiya, T., & Mora-Páez, H. (2024). Viscoelastic earthquake cycle model for the Caribbean subduction zone in northwestern Colombia: Implications of coastal subsidence for seismic/tsunami hazards. *Journal of South American Earth Sciences*, *141*, 104931. https://doi.org//10.1016/j.jsames.2024.104931

- Paez-Ramirez, J., Lizarazo, J., Medina, S., Rivas, M., Luna, P., Mas, E., & Koshimura, S. (2021). A comparative analysis of empirical and analytical tsunami fragility functions for buildings in Tumaco, Colombia. *IOP Conference Series: Earth and Environmental Science*, *630*(1), 012008. https://doi.org/10.1088/1755-1315/630/1/012008
