---
title: Incendios forestales
---

# Incendios forestales

:::{image} ../../estilo/ilustraciones/incendios.svg
:alt: Incendio forestal con humo avanzando hacia una casa
:class: ilustracion
:width: 100%
:::

Este capítulo sigue el molde de siete puntos ([](_molde.md)). Los incendios de la cobertura vegetal tienen casi siempre origen humano, así que su amenaza combina un fenómeno natural (combustible y clima) con una causa social (la ignición).

## 1. Fenómeno

Los incendios de la cobertura vegetal se mantienen mientras coincidan combustible, calor y oxígeno. Esa combinación se conoce como la «gran tríada». De ella dependen la ocurrencia y la propagación, junto con el tipo de vegetación, la cantidad de combustible, las condiciones meteorológicas, la topografía y las actividades humanas {cite:p}`ungrd2019atlas`. Según su propagación, el Atlas distingue incendios superficiales, subterráneos (por debajo del suelo) y aéreos (por la copa de los árboles o matorrales) {cite:p}`ungrd2019atlas`.

El fuego no siempre es negativo: forma parte de la historia natural de algunos ecosistemas, y su uso controlado hace parte de prácticas comunitarias. En ecosistemas sensibles al fuego sus efectos pueden ser catastróficos. Un incendio fuera de los límites históricos del régimen de un ecosistema puede transformarlo en otro distinto y aumentar la probabilidad de nuevos incendios {cite:p}`ungrd2019atlas`.

### Origen humano

Según el Protocolo Nacional de Prevención, Control de Incendios Forestales y Restauración de Áreas Afectadas, cerca del 95 % de los incendios en Colombia es de origen antrópico {cite:p}`ungrd2019atlas`. Un estudio de cartografía participativa en áreas protegidas encuentra también factores socioculturales como causa de los incendios (ID 101 de la hoja de vigilancia).

### Dónde y cuándo ocurren

El Atlas, con datos del IDEAM, describe un patrón regional {cite:p}`ungrd2019atlas`:

| Región | Patrón de incendios |
|---|---|
| **Orinoquía** | Alta ocurrencia, por una temporada seca intensa y por el uso del fuego para renovar pastos |
| **Caribe** | Similar a la Orinoquía, en menor extensión, por menor carga de combustible |
| **Amazonía** | Procesos recurrentes entre sabana y bosque, sobre todo en La Macarena |
| **Andes** | Baja ocurrencia, con quemas importantes en páramo, un ecosistema de alto valor ecológico |

Los incendios se concentran en las temporadas secas anuales (diciembre a marzo y julio a agosto), y El Niño y La Niña intensifican o atenúan el número de eventos y el área afectada {cite:p}`ungrd2019atlas`.

**Variable de intensidad.** Depende del método: un índice de peligro de incendio (como el FWI), la susceptibilidad de la cobertura o el área quemada.

### Definición según los HIPs de UNDRR

Los perfiles de información de amenazas ([](../01_conceptos/16_hips_undrr.md)) que corresponden a este capítulo son:

| Código | Perfil (clúster) | Definición (traducción propia) |
|---|---|---|
| EN0205 | Incendios de vegetación (ambiental, degradación ambiental) | Todo incendio de vegetación no planificado e incontrolado que, sin importar la fuente de ignición, pueda afectar negativamente valores sociales, económicos o ambientales y requiera una respuesta de supresión u otra acción según la política de la agencia (FAO, 2024). |

Fuente: {cite:p}`undrr2025hips`.

**Qué se incluye y por qué.**

- **Se incluye.** La definición es independiente de la fuente de ignición, lo que calza con el énfasis del capítulo en el origen humano de la mayoría de los incendios.
- **Clasificación.** Los HIPs lo ubican entre los peligros ambientales, y no entre los meteorológicos; el capítulo mantiene la relación con el clima ([](308_sequia.md), [](309_calor.md)).
- **No se incluyen:** el humo (MH0205: partículas en suspensión producidas por la combustión), que es un asunto de calidad del aire, ni las quemas controladas, que quedan fuera de la definición.
- **Incendio urbano.** Los HIPs no tienen un perfil de incendio urbano o estructural; el más cercano es TL0305 «Fuego», de tipo tecnológico (falla industrial), cuyo contexto reconoce los incendios en áreas urbanas. Se retoma en la decisión de alcance del [plan](../01_conceptos/16_hips_undrr.md).
- **Cascadas.** Los HIPs registran los incendios de vegetación como causados por sequía, ola de calor, rayos y erupciones, y como causa de movimientos en masa y de contaminación del aire {cite:p}`undrr2025hips`.

## 2. Amenaza

### Método del IDEAM

El procedimiento nacional del IDEAM (2011) es **paramétrico y espacial**, basado en la ponderación y calificación secuencial de factores normalizados organizados jerárquicamente. Evalúa la amenaza a partir de cuatro grupos de factores del territorio {cite:p}`ungrd2019atlas`:

1. **Susceptibilidad de la cobertura vegetal.** Condición pirogénica de la vegetación, con base en el modelo de combustibles de Páramo (2007).
2. **Factores climáticos** que influyen sobre el tipo de vegetación presente.
3. **Factores de relieve** que influyen en la propagación del fuego.
4. **Factor histórico**, que refleja la frecuencia de eventos.

La aplicación requiere como mínimo la cobertura vegetal, series históricas de precipitación y temperatura, la topografía, la red vial y, si es posible, un inventario de incendios previos {cite:p}`ungrd2019atlas`. El IDEAM definió un protocolo para mapas de zonificación a escala 1:100.000 que permite análisis estandarizados y comparables {cite:p}`ungrd2019atlas`.

### Método de CLIMAAX

El flujo de CLIMAAX con el Índice de Clima de Incendio (FWI) mide el peligro con un índice de 0 a 100 que combina temperatura del mediodía, lluvia, viento y humedad relativa, y que da cuenta del efecto de la humedad del combustible y del clima en el comportamiento del fuego {cite:p}`climaax2025handbook`. El peligro resulta de la interacción entre ese clima y la vegetación quemable {cite:p}`climaax2025handbook`.

### Aproximaciones basadas en datos

Hay estudios colombianos con aprendizaje automático: un modelo de probabilidad de fuego con datos abiertos para la ecorregión de los Llanos colombo–venezolanos {cite:p}`barreto2020open`; un análisis de riesgo de incendio en sabanas tropicales con enfoque multiescenario {cite:p}`gonzalez2025predicting`; y un estudio de los factores hidroclimáticos y de uso del suelo del riesgo de incendio en el Caribe colombiano. Este último encuentra que la fragmentación del hábitat por agricultura, ganadería y expansión urbana redujo los incendios naturales pero aumentó los de ignición humana {cite:p}`camargocaicedo2025hydroclimatic`.

El capítulo de la serie 2023 sobre la Orinoquía compara instrumentos de teledetección para identificar áreas quemadas {cite:p}`incendios2023orinoquia`.

## 3. Exposición

La exposición es la cobertura vegetal y lo que hay en ella o a su alrededor: población, infraestructura, áreas protegidas y actividades económicas. CLIMAAX incluye población que vive en la interfaz urbano–forestal (periurbana junto a áreas vegetadas), áreas protegidas, densidad de población y un índice de costo de restauración del ecosistema {cite:p}`climaax2025handbook`.

## 4. Vulnerabilidad

El método del IDEAM evalúa la vulnerabilidad con la población, los valores de protección de infraestructura e instalaciones, las actividades económicas, el patrimonio natural, histórico y cultural, la acción institucional y algunos aspectos territoriales {cite:p}`ungrd2019atlas`.

CLIMAAX define la vulnerabilidad como la combinación de los sistemas humano, ecológico y socioeconómico sensibles al fuego (marco EFFIS), y permite escoger qué parámetros de vulnerabilidad incluir mediante un análisis de Pareto con el peligro {cite:p}`climaax2025handbook`.

## 5. Riesgo

El riesgo se obtiene como la probabilidad de que se presenten consecuencias o daños, de la interacción de la amenaza y la vulnerabilidad, que son elementos dinámicos y cambiantes. La cartografía del riesgo define los escenarios existentes {cite:p}`ungrd2019atlas`. El IDEAM lo calcula para condiciones normales de precipitación y temperatura y para condiciones de El Niño, y el Atlas muestra ambos mapas {cite:p}`ungrd2019atlas`.

A diferencia de las amenazas de los capítulos anteriores, este riesgo es **relativo** (zonificación en clases), no una pérdida anual esperada.

## 6. Clima

Los incendios son sensibles al clima. Las sequías extremas aumentan la frecuencia e intensidad de los incendios en América Latina, según una revisión sistemática de literatura publicada entre 2012 y 2023 {cite:p}`acevedoortiz2026sequias`. En la cuenca del Orinoco, los extremos secos y cálidos compuestos tienen implicaciones para la actividad de incendios {cite:p}`arias2025compound`.

CLIMAAX usa el FWI con proyecciones climáticas para analizar el cambio en la duración de la temporada de peligro {cite:p}`climaax2025handbook`. Como los incendios dependen además de la ignición humana, el clima solo explica una parte de la amenaza.

## 7. Datos y medidas

### Datos y marco institucional

| Elemento | Qué ofrece | Referencia |
|---|---|---|
| IDEAM | Seguimiento y monitoreo de incendios, mapa de zonificación de riesgo, protocolo 1:100.000 | {cite:p}`ungrd2019atlas` |
| Estadísticas de incendios (IDEAM) | Número de incendios y área afectada por departamento | {cite:p}`ungrd2019atlas` |
| Comisión Nacional Asesora de Incendios Forestales | Estudios, prevención y atención | {cite:p}`ungrd2019atlas` |
| Protocolo Nacional de Prevención, Control de Incendios Forestales y Restauración de Áreas Afectadas | Lineamientos para prevención, detección y atención | {cite:p}`ungrd2019atlas` |
| EFFIS y Copernicus | FWI y parámetros de vulnerabilidad para el flujo de CLIMAAX | {cite:p}`climaax2025handbook` |

### Incertidumbres

- El origen humano de la ignición no se modela con variables climáticas.
- Hay mucha diversidad de regímenes de fuego, de ecosistemas y de prácticas culturales {cite:p}`ungrd2019atlas`.
- Los datos de EFFIS son europeos; hay que verificar su cobertura y sustituirlos por datos de Colombia.

### Medidas según la Ley 1523

Los resultados sirven para planificar actividades de prevención y mitigación, establecer áreas prioritarias de gestión y emitir alertas tempranas {cite:p}`ungrd2019atlas`.

| Proceso | Medida | Referencia |
|---|---|---|
| Conocimiento | Zonificación, inventario y monitoreo de incendios | {cite:p}`ungrd2019atlas` |
| Reducción | Prevención y mitigación en áreas prioritarias; manejo del fuego con la comunidad | {cite:p}`ungrd2019atlas` |
| Manejo | Alertas tempranas, detección y atención | {cite:p}`ungrd2019atlas` |

## Síntesis de evidencia

```{note}
**Método.** Síntesis narrativa por tipo de evidencia (no un metaanálisis con efectos agrupados: los estudios usan diseños, escalas y variables que no se pueden combinar en un solo estimador). Se leyeron los resúmenes de los artículos de la hoja de vigilancia que están en la carpeta de PDFs; las cifras vienen de esos resúmenes y **faltan por verificar contra el texto completo**.
```

| Estudio | Diseño y lugar | Resultado relevante |
|---|---|---|
| {cite:t}`acevedoortiz2026sequias` | Revisión sistemática 2012–2023 (SciELO y Scopus), América Latina | Las sequías extremas aumentan la frecuencia e intensidad de los incendios; el 37 % de los estudios usó datos del programa Queimadas del INPE y el 27 % la misión TRMM para sequía |
| {cite:t}`armenteras2021induced` | Análisis de frecuencia de fuego y trayectorias posfuego, 2001–2018, bosques de Latinoamérica | Estudia cómo la frecuencia de fuego influye en la pérdida posterior de bosque |
| {cite:t}`barreto2020open` | Bosque aleatorio con datos abiertos (MODIS MCD64A1, 2015–2019), llanos colombo-venezolanos | Mapa de probabilidad de ocurrencia de fuego con variables de topografía, presencia humana y clima |
| {cite:t}`anderson2021alert` | Sistema de alerta de cinco niveles combinando clima y factores antrópicos, áreas protegidas de Suramérica | Usa la tendencia de focos activos como indicador de la intensificación del uso humano del fuego |
| {cite:t}`gonzalez2025predicting` | Escenarios múltiples de cambio climático, sabanas de Colombia | Evalúa el riesgo de fuego bajo escenarios de emisión |
| {cite:t}`ballesterosgonzalez2020estimating` | Modelo químico-transporte WRF-Chem, norte de Suramérica | Estima el efecto de la quema de biomasa en la calidad del aire y la salud |
| {cite:t}`jones2024state` | Informe global de incendios 2023–2024 | Atribuye eventos extremos al clima y al uso del suelo y proyecta riesgos futuros |

**Lectura conjunta.**

- **Doble causa.** Los estudios coinciden en que el fuego responde a un factor climático (sequía y calor) y a uno humano (uso del fuego y cambio de cobertura) {cite:p}`acevedoortiz2026sequias,anderson2021alert`. Un modelo de amenaza debe tener ambos, no solo la precipitación.
- **Datos abiertos.** MODIS, TRMM y focos activos permiten construir mapas de probabilidad sin datos locales {cite:p}`barreto2020open,acevedoortiz2026sequias`; su validación con eventos locales queda pendiente.
- **Efectos fuera del área quemada.** El humo afecta ciudades lejanas {cite:p}`ballesterosgonzalez2020estimating`; el análisis urbano debe considerar la calidad del aire, no solo la cercanía al fuego.
- **Clima futuro.** Hay escenarios para sabanas colombianas {cite:p}`gonzalez2025predicting`.

**Estudios añadidos con el segundo lote de PDFs.**

- {cite:t}`armenteras2023landscape` documenta un aumento de la ocurrencia y severidad de megaincendios en Suramérica, atribuido al cambio climático y a prácticas insostenibles de uso del suelo, y pide coordinación científica y manejo del paisaje.
- {cite:t}`oliveras2025integrated` y {cite:t}`puiggirones2025preserve` proponen el manejo integrado del fuego y el uso del fuego como herramientas de adaptación y de conservación de la biodiversidad bajo regímenes de fuego alterados. Se leen aquí solo por su título y resumen.
- {cite:t}`fontana2023women` explora con teatro foro las experiencias de mujeres en crisis de incendios y conflicto en Colombia.

**Lectura adicional.** El manejo del paisaje y la dimensión social (conflicto, género) completan el enfoque de amenaza basado en clima y sequía.

## Pendiente

- Leer {cite:p}`gonzalez2025predicting`, {cite:p}`arias2025compound` y {cite:p}`acevedoortiz2026sequias` completos. Los dos primeros se conocen por título o resumen parcial.
- Verificar el estado actual del protocolo y de la normativa de incendios posteriores a 2019.
- Añadir las cifras recientes de área quemada y su relación con El Niño 2023–2024.
- Evaluar el FWI sobre reanálisis ERA5 para Colombia y su calibración con el inventario del IDEAM.

## Bibliografía recomendada

Lista de los 41 registros de la hoja de vigilancia científica (pestaña `Vigilancia_CTeI`, columna `AMENAZA_ESPECIFICA` = «Incendios forestales»), en formato APA 7 con metadatos de Crossref. Son lecturas recomendadas: **no están verificadas contra el texto completo** ni se usan como evidencia hasta que se citen en el capítulo. Las entradas sin DOI carecen de autores en la hoja.

- Acevedo Ortiz, M. Y., Arias Gómez, P. A., & Villa Garzón, F. A. (2026). Sequías e incendios forestales en América Latina: una revisión sistemática de literatura. *Colombia forestal*, *29*(1), e23266. https://doi.org/10.14483/2256201x.23266

- Aguilar-Garavito, M., Sesquilé, E., Cortina-Segarra, J., Legizamo, Á., & Ruiz-Santacruz, S. (2024). Producción y germinación de bellotas del roble andino Quercus humboldtii (Fagaceae) afectado por incendios recurrentes. *Revista de Biología Tropical*, *72*(1), e53407. https://doi.org/10.15517/rev.biol.trop..v72i1.53407

- Anderson, L. O., Burton, C., dos Reis, J. B. C., Pessôa, A. C. M., Bett, P., Carvalho, N. S., Junior, C. H. L. S., Williams, K., Selaya, G., Armenteras, D., Bilbao, B. A., Xaud, H. A. M., Rivera‐Lombardi, R., Ferreira, J., Aragão, L. E. O. C., Jones, C. D., & Wiltshire, A. J. (2021). An alert system for Seasonal Fire probability forecast for South American Protected Areas. *Climate Resilience and Sustainability*, *1*(1), e19. https://doi.org/10.1002/cli2.19

- Armenteras, D., & de la Barrera, F. (2023). Landscape management is urgently needed to address the rise of megafires in South America. *Communications Earth & Environment*, *4*(1), 305. https://doi.org/10.1038/s43247-023-00964-6

- Armenteras, D., Dávalos, L. M., Barreto, J. S., Miranda, A., Hernández-Moreno, A., Zamorano-Elgueta, C., González-Delgado, T. M., Meza-Elizalde, M. C., & Retana, J. (2021). Fire-induced loss of the world’s most biodiverse forests in Latin America. *Science Advances*, *7*(33), eabd3357. https://doi.org/10.1126/sciadv.abd3357

- Ballesteros-González, K., Sullivan, A. P., & Morales-Betancourt, R. (2020). Estimating the air quality and health impacts of biomass burning in northern South America using a chemical transport model. *Science of The Total Environment*, *739*, 139755. https://doi.org/10.1016/j.scitotenv.2020.139755

- Barreto, J. S., & Armenteras, D. (2020). Open Data and Machine Learning to Model the Occurrence of Fire in the Ecoregion of “Llanos Colombo–Venezolanos”. *Remote Sensing*, *12*(23), 3921. https://doi.org/10.3390/rs12233921

- Cabrera, A., Ferro, C., Casallas, A., & López-Barrera, E. A. (2024). Wildfire Scenarios for Assessing Risk of Cover Loss in a Megadiverse Zone within the Colombian Caribbean. *Sustainability*, *16*(8), 3410. https://doi.org/10.3390/su16083410

- Camacho-De Angulo, Y. V., Cechinel Rosa, N., Solano-Correa, Y. T., & Roisenberg, M. (2024). Fire Scars Mapping Over Brazilian Amazon Forest by Exploiting Sentinel-2 Data and Deep Learning. *IGARSS 2024 - 2024 IEEE International Geoscience and Remote Sensing Symposium*, 2773-2776. https://doi.org/10.1109/igarss53475.2024.10642369

- Camargo Caicedo, Y., Bolaño-Diaz, S., Pomares-Meza, G. M., Pérez-Pérez, M., Soro, T. D., Bolaño-Ortiz, T. R., & Vélez-Pereira, A. M. (2025). Hydroclimatic and Land Use Drivers of Wildfire Risk in the Colombian Caribbean. *Fire*, *8*(6), 221. https://doi.org/10.3390/fire8060221

- Celis, N., Casallas, A., Lopez-Barrera, E. A., Felician, M., De Marchi, M., & Pappalardo, S. E. (2023). Climate Change, Forest Fires, and Territorial Dynamics in the Amazon Rainforest: An Integrated Analysis for Mitigation Strategies. *ISPRS International Journal of Geo-Information*, *12*(10), 436. https://doi.org/10.3390/ijgi12100436

- Davalos, L., Dávalos, L. M., & Armenteras, D. (2024). Criminal control shapes options for Amazon forests. *Authorea*. https://doi.org/10.22541/au.173498193.35964980/v1

- Espinoza, I. G., Franco-Gaviria, F., Castañeda, I., Robinson, C., Room, A., Berrío, J. C., Armenteras, D., & Urrego, D. H. (2022). Holocene Fires and Ecological Novelty in the High Colombian Cordillera Oriental. *Frontiers in Ecology and Evolution*, *10*, 895152. https://doi.org/10.3389/fevo.2022.895152

- Fontana, L., Miramonti, A., & Johnston, C. (2023). Women in Wildfire Crises: Exploring Lived Experiences of Conflict through Forum Theatre (Creative Intervention). *Studies in Social Justice*, *17*(2), 269-279. https://doi.org/10.26522/ssj.v17i2.3993

- González, T. M., González-Trujillo, J. D., Elizalde, M. M., & Armenteras, D. (2025). Predicting fire risk in colombia tropical savannas: A multi-scenario approach. *Agricultural and Forest Meteorology*, *369*, 110566. https://doi.org/10.1016/j.agrformet.2025.110566

- González, T. M., González-Trujillo, J. D., Muñoz, A., & Armenteras, D. (2022). Effects of fire history on animal communities: a systematic review. *Ecological Processes*, *11*(1), 11. https://doi.org/10.1186/s13717-021-00357-7

- GOULART, F. F., ROQUE, F. O., LIBONATI, R., ANDERSON, L. O., BERLINCK, C. N., MARENGO, J. A., RIBEIRO, D. B., DAMASCENO-JUNIOR, G. A., QUINTERO, J. M. O., FERNANDES, S., BURITICÁ, S. R., TOMA, T. S. P., ASHWORTH, L., AGUILAR, R., NEGREIROS, D., & FERNANDES, G. W. (2026). Fire in South America’s wetlands: temporal and spatial patterns. *Anais da Academia Brasileira de Ciências*, *98*(1), e20240622. https://doi.org/10.1590/0001-3765202620240622

- Jones, M. W., Kelley, D. I., Burton, C. A., Di Giuseppe, F., Barbosa, M. L. F., Brambleby, E., Hartley, A. J., Lombardi, A., Mataveli, G., McNorton, J. R., Spuler, F. R., Wessel, J. B., Abatzoglou, J. T., Anderson, L. O., Andela, N., Archibald, S., Armenteras, D., Burke, E., Carmenta, R., ... Xanthopoulos, G. (2024). State of Wildfires 2023–2024. *Earth System Science Data*, *16*(8), 3601-3685. https://doi.org/10.5194/essd-16-3601-2024

- La paradoja del fuego: del contexto internacional al caso de Colombia. (2023). (Sin DOI; completar autores).

- La paradoja del fuego: del contexto internacional al caso de Colombia. (2023). `doi:isbn: 978-958-49-8882-9` (no resuelve en Crossref; corregir en la hoja)

- Linley, G. D., Jolly, C. J., Doherty, T. S., Geary, W. L., Armenteras, D., Belcher, C. M., Bliege Bird, R., Duane, A., Fletcher, M., Giorgis, M. A., Haslem, A., Jones, G. M., Kelly, L. T., Lee, C. K. F., Nolan, R. H., Parr, C. L., Pausas, J. G., Price, J. N., Regos, A., ... Nimmo, D. G. (2025). ‘Megafire’—You May Not Like It, But You Cannot Avoid It. *Global Ecology and Biogeography*, *34*(4), e70032. https://doi.org/10.1111/geb.70032

- Maquina para apagar incendios forestales. (2018). *Patente de Invencion Nacional*. `doi:nc2018/0007209` (no resuelve en Crossref; corregir en la hoja)

- Martha Patricia, V. G., & Parra Cindy Carolina, F. (2024). Fuzzy Logic, Artificial Intelligence, and Planet Scope Imagery for the Zonification of Wildfire Vulnerability. *IGARSS 2024 - 2024 IEEE International Geoscience and Remote Sensing Symposium*, 3971-3975. https://doi.org/10.1109/igarss53475.2024.10642446

- Meza Elizalde, M. C., González Delgado, T. M., & Castro - Lima, F. (2026). Fire severity reshapes fuel loads and structure in flooded tropical forests of the Orinoco. *SSRN*. https://doi.org/10.2139/ssrn.6222328

- Meza, M. C., Espelta, J. M., González, T. M., & Armenteras, D. (2023). Fire reduces taxonomic and functional diversity in Neotropical moist seasonally flooded forests. *Perspectives in Ecology and Conservation*, *21*(2), 101-111. https://doi.org/10.1016/j.pecon.2023.04.003

- Montoya Alvis, J., Orozco Mendoza, G. L., & Zartha Sossa, J. W. (2025). Extreme Fire Events in Wildland–Urban Interface Areas: A Review of the Literature Concerning Determinants for Risk Governance. *Sustainability*, *17*(10), 4505. https://doi.org/10.3390/su17104505

- Moreno, A., Bélanger, V., Cherkesly, M., & Rancourt, M.-È. (2026). Evacuation network design and planning under traffic congestion: An application to wildfires in Canada. *Transportation Research Part E: Logistics and Transportation Review*, *213*, 104965. https://doi.org/10.1016/j.tre.2026.104965

- Mosquera-Guerra, F., Moreno-Niño, N., Garcia-Suabita, W., & Armenteras-Pascual, D. (2024). Impact of wildfires on the suitability habitat of the lowland tapir in a native savanna landscape of northern South America. *Discover Conservation*, *1*(1), 15. https://doi.org/10.1007/s44353-024-00013-z

- Neira Mendieta, S., McAleavy, T., Rodriguez Coca, D., Solano-Charris, E. L., Park, H., & Javier Guerrero, W. (2025). Determining barriers to wildland firefighter response efficacy in the mid- and western United States. *International Journal of Emergency Services*, *14*(2), 185-197. https://doi.org/10.1108/ijes-07-2024-0042

- Oliveras Menor, I., Prat-Guitart, N., Spadoni, G. L., Hsu, A., Fernandes, P. M., Puig-Gironès, R., Ascoli, D., Bilbao, B. A., Bacciu, V., Brotons, L., Carmenta, R., de-Miguel, S., Gonçalves, L. G., Humphrey, G., Ibarnegaray, V., Jones, M. W., Machado, M. S., Millán, A., de Morais Falleiro, R., ... Armenteras Pascual, D. (2025). Integrated fire management as an adaptation and mitigation strategy to altered fire regimes. *Communications Earth & Environment*, *6*(1), 202. https://doi.org/10.1038/s43247-025-02165-9

- Participatory Mapping Reveals Sociocultural Drivers of Forest Fires in Protected Areas of the Post-Conflict Colombian Amazon. (2021). *DRYAD*. `doi:10.5061/dryad.cz8w9gj3n` (no resuelve en Crossref; corregir en la hoja)

- Pereira, A. d. M. M., Damasceno-Junior, G. A., Libonati, R., Anderson, L. O., Souza, A. H. d. A., Ferreira, B. H. d. S., Nunes, A. V., Siqueira, A. L., Guerra, A., Rabelo, A. C. P., Desbiez, A. L. J., Falcette, A. H. L., Garcia, Á. d. S., Kellermann, B., Oliveira, B. G. d., Jenkins, B., Peres, C. A., Berlinck, C. N., Ribeiro, D. B., ... Roque, F. d. O. (2025). Catastrophic wildfires in the Pantanal wetlands as catalysts for transformative change. *Environmental Science & Policy*, *174*, 104273. https://doi.org/10.1016/j.envsci.2025.104273

- Puig-Gironès, R., Palmero-Iniesta, M., Fernandes, P. M., Oliveras Menor, I., Ascoli, D., Kelly, L. T., Charles-Dominique, T., Regos, A., Harrison, S., Armenteras, D., Brotons, L., de-Miguel, S., Spadoni, G. L., Carmenta, R., Machado, M., Cardil, A., Santos, X., Erdozain, M., Canaleta, G., ... Pons, P. (2025). The use of fire to preserve biodiversity under novel fire regimes. *Philosophical Transactions of the Royal Society B: Biological Sciences*, *380*(1924), 20230449. https://doi.org/10.1098/rstb.2023.0449

- Quishpe-Vásquez, C., Oliva, P., López-Barrera, E. A., & Casallas, A. (2024). Wildfires impact on PM2.5 concentration in galicia Spain. *Journal of Environmental Management*, *367*, 122093. https://doi.org/10.1016/j.jenvman.2024.122093

- Rojano, R. E., Arregoces, H. A., & Restrepo, G. (2025). Interannual variations in PM10 and PM2.5 due to wildfires in four air quality monitoring networks in the Colombian caribbean. *Environmental Challenges*, *21*, 101360. https://doi.org/10.1016/j.envc.2025.101360

- Sharobiddinov, D., Siddiqui, H. U. R., Saleem, A. A., Mezquita, G. M., Vargas, D. L. R., & Díez, I. d. l. T. (2025). Edge-Based Autonomous Fire and Smoke Detection Using MobileNetV2. *Sensors*, *25*(20), 6419. https://doi.org/10.3390/s25206419

- Signori, R. T., Mamani, L., Cevalho, W., de Souza, I. P., Kayano, M. T., de Oliveira, M. B. L., Céron, W. L., Andreoli, R. V., & de Souza, R. A. F. (2026). How climate variability modes influenced the fires in South America during the extreme droughts of 2023–2024. *Science of The Total Environment*, *1028*, 181705. https://doi.org/10.1016/j.scitotenv.2026.181705

- Smith, M. N., Stark, S. C., Taylor, T. C., Schietti, J., de Almeida, D. R. A., Aragón, S., Torralvo, K., Lima, A. P., de Oliveira, G., de Assis, R. L., Leitold, V., Pontes‐Lopes, A., Scoles, R., de Sousa Vieira, L. C., Resende, A. F., Coppola, A. I., Brandão, D. O., de Athaydes Silva Junior, J., Lobato, L. F., ... Nelson, B. W. (2023). Diverse anthropogenic disturbances shift Amazon forests along a structural spectrum. *Frontiers in Ecology and the Environment*, *21*(1), 24-32. https://doi.org/10.1002/fee.2590

- Suarez, D., Gomez, C., Medaglia, A. L., Akhavan-Tabatabaei, R., & Grajales, S. (2024). Integrated Decision Support for Disaster Risk Management: Aiding Preparedness and Response Decisions in Wildfire Management. *Information Systems Research*, *35*(2), 609-628. https://doi.org/10.1287/isre.2022.0118

- Torres, J. F., Valencia, S., Martínez-Álvarez, F., & Hoyos, N. (2023). Predicting Wildfires in the Caribbean Using Multi-source Satellite Data and Deep Learning. *Lecture Notes in Computer Science*, 3-14. https://doi.org/10.1007/978-3-031-43078-7_1

- Valencia, G. M., Anaya, J. A., & Caro-Lopera, F. J. (2022). Estimación de emisiones atmosféricas de CO₂, NO₂, CO, NH₃ y Black Carbon vía bottom up, generados por quema de biomasa en el norte de América del Sur. *Revista de Teledetección*(59), 23-46. https://doi.org/10.4995/raet.2022.15594
