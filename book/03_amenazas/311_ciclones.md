---
short_title: Ciclones tropicales
title: Ciclones tropicales
---

# Ciclones tropicales

Este capítulo sigue el molde de siete puntos ([](_molde.md)). Para la mayor parte de Colombia continental el ciclón tropical es una amenaza indirecta. Para el archipiélago de San Andrés, Providencia y Santa Catalina y la península de La Guajira es directa. Los vendavales, que producen vientos fuertes locales sin ser ciclones, se tratan en [](312_vendavales.md). La marea de tormenta se conecta con [](306_erosion_costera.md) y la lluvia con [](305_inundacion.md) y [](304_mov_masa.md).

## 1. Fenómeno

Un ciclón tropical es un sistema de tormentas con circulación atmosférica y baja presión en el centro, que produce lluvias intensas. Se llama huracán, ciclón o tifón según la cuenca oceánica. Los vientos circulan alrededor del ojo, en contra de las manecillas del reloj en el hemisferio norte, por el efecto Coriolis {cite:p}`ungrd2019atlas`.

### Condiciones de formación

Los factores que más influyen son una temperatura superficial del mar mayor a 26 °C, latitudes entre 5° y 20° al norte y al sur del ecuador y alta humedad relativa en la troposfera. El agua cálida evapora rápido, el aire caliente asciende, se forma un centro de baja presión y el ciclo se refuerza por retroalimentación positiva {cite:p}`ungrd2019atlas`.

### Etapas e intensidad

| Etapa | Criterio de viento sostenido (Atlas) |
|---|---|
| Depresión tropical | Circulación cerrada en etapa formativa |
| Tormenta tropical | Mayor de 63 km/h; ya recibe nombre y puede ser peligrosa |
| Ciclón (huracán) | Mayor de 119 km/h; la forma más severa |

La escala Saffir–Simpson clasifica los ciclones por presión central y da rangos de velocidad sostenida del viento y de altura de la marea de tormenta {cite:p}`ungrd2019atlas`.

### Componentes de daño

El daño no depende solo de la velocidad del viento, sino también de la velocidad de traslación, la duración de los vientos fuertes, la lluvia, los cambios de dirección y de intensidad, y el tamaño del sistema {cite:p}`ungrd2019atlas`.

| Componente | Efecto |
|---|---|
| **Marea de tormenta** | Elevación del nivel del mar por el estrés del viento y la baja presión. El Atlas la señala como el efecto más dañino, porque cerca del 80 % de las muertes por huracanes ocurre donde tocan tierra |
| **Viento** | Destrucción de infraestructura y escombros convertidos en proyectiles |
| **Lluvia torrencial** | Inundaciones y deslizamientos, incluso muchos kilómetros tierra adentro |

Fuente de la tabla: {cite:p}`ungrd2019atlas`.

**Variable de intensidad.** Para viento, la ráfaga de 3 segundos a 10 m sobre la superficie. Para marea de tormenta, la altura de la ola en localizaciones costeras {cite:p}`ungrd2019atlas`.

### Ciclones y Colombia

La probabilidad de que los ciclones afecten el territorio continental es bastante reducida. Las zonas con amenaza directa son el archipiélago de San Andrés, Providencia y Santa Catalina y la península de La Guajira. En el resto del Caribe colombiano la afectación ha sido indirecta («coletazos») {cite:p}`ungrd2019atlas`. El Atlas da tres razones meteorológicas {cite:p}`ungrd2019atlas`:

1. Los sistemas que vienen de la costa africana tienden a moverse hacia el oeste–noroeste.
2. La línea de costa del Caribe colombiano no es perpendicular al oleaje, excepto La Guajira.
3. La Sierra Nevada de Santa Marta actúa como escudo natural para gran parte del litoral centro y sur.

Aun así, estos sistemas dejan lluvias cuantiosas que pueden dar crecidas, y los efectos indirectos incluyen deslizamientos, caída de árboles y techos, erosión de laderas e inundaciones de viviendas. La tormenta Beta en 2005 causó daños menores a la infraestructura costera {cite:p}`ungrd2019atlas`.

```{important}
El huracán Iota de 2020 destruyó el 56,4 % de las viviendas de Providencia y dañó parcialmente las demás {cite:p}`rey2021hurricane`. La baja frecuencia de eventos no implica bajo riesgo en las islas.
```

### Trayectorias de los ciclones en el Caribe

La figura muestra las trayectorias reales de los ciclones tropicales del Atlántico Norte entre 1980 y 2025, tomadas de la base de datos IBTrACS del NOAA {cite:p}`knapp2010ibtracs,knapp2019ibtracs`. Se dibuja con código Python en un cuaderno reproducible, que descarga los datos y se puede ejecutar en Colab: [](315_trayectorias_ciclones.ipynb).

```{figure} figuras/trayectorias_ciclones_caribe.png
:label: fig-trayectorias-caribe
:alt: Mapa de dos paneles. A la izquierda, trayectorias de huracanes que entraron al Caribe entre 1980 y 2025, coloreadas por categoría Saffir-Simpson. A la derecha, acercamiento al suroeste del Caribe con los sistemas que pasaron a menos de 250 km de San Andrés, Providencia, La Guajira y Cartagena.
:width: 100%

Trayectorias de ciclones tropicales en el Caribe, 1980-2025. Izquierda: huracanes que entraron a la región punteada, con cada tramo coloreado por su categoría. Derecha: sistemas que pasaron a menos de 250 km de sitios de Colombia; los números identifican los huracanes que pasaron a menos de esa distancia de San Andrés o Providencia. Datos: IBTrACS v04r01 {cite:p}`knapp2019ibtracs`. Elaboración propia con el cuaderno 315.
```

Lo que muestra la {numref}`fig-trayectorias-caribe`, con las cifras que calcula el cuaderno:

- De los 743 sistemas del Atlántico Norte de ese periodo, 631 alcanzaron al menos tormenta tropical y 321 llegaron a huracán. De estos, 192 entraron a la región del Caribe que usa la figura.
- A simple vista, la mayor parte de las trayectorias cruza el Caribe central y el norte con rumbo oeste-noroeste, y son menos las que llegan al sur; es una lectura de la figura, que el conteo de la tabla respalda en parte. El Atlas atribuye ese patrón a razones meteorológicas {cite:p}`ungrd2019atlas`.
- Los sistemas que pasaron a menos de 250 km de cuatro sitios de Colombia, en 46 temporadas:

| Sitio | Sistemas a menos de 250 km | Con viento ≥ 34 kt dentro del radio | Con viento ≥ 64 kt dentro del radio |
|---|---|---|---|
| San Andrés | 35 | 18 | 9 |
| Providencia | 40 | 19 | 9 |
| La Guajira (Cabo de la Vela) | 16 | 10 | 3 |
| Cartagena | 8 | 4 | 1 |

Fuente: cálculo propio con IBTrACS {cite:p}`knapp2019ibtracs`; el cuaderno 315 reproduce la tabla. La columna final es el viento máximo **del sistema dentro del radio**, no el viento que se sintió en el sitio.

Nueve huracanes pasaron a menos de 250 km de San Andrés o Providencia en ese periodo: Joan (1988), Cesar (1996), Beta (2005), Felix (2007), Ida (2009), Otto (2016), Eta (2020), Iota (2020) y Julia (2022). Iota pasó a unos 22 km de las islas.

La lectura de este libro es que el conteo es **coherente** con lo que dice el Atlas: el archipiélago y La Guajira son las zonas de amenaza directa, y la costa continental del Caribe, como Cartagena, recibe sistemas con mucha menos frecuencia {cite:p}`ungrd2019atlas`. Tres precauciones:

- **El conteo depende de la distancia elegida** (250 km) y de un periodo corto, de 46 temporadas. Con una o dos decenas de sistemas por sitio no se estima un periodo de retorno; para eso el Atlas usa un conjunto estocástico de ciclones {cite:p}`ungrd2019atlas`.
- **La distancia no es el impacto.** El viento, la lluvia y la marea de tormenta dependen del tamaño del sistema y de por qué lado pasa respecto del sitio.
- **Son mejores trayectorias.** Las reconstruye el Centro Nacional de Huracanes después de cada temporada, y su precisión es menor antes de la era satelital; por eso se parte de 1980.

### Definición según los HIPs de UNDRR

Los perfiles de información de amenazas ([](../01_conceptos/16_hips_undrr.md)) que corresponden a este capítulo son:

| Código | Perfil (clúster) | Definición (traducción propia) |
|---|---|---|
| MH0309 | Ciclón tropical (meteorológico e hidrológico, viento y presión) | Ciclón de origen tropical y diámetro pequeño (algunos cientos de kilómetros), con presión mínima de superficie que en ocasiones baja de 900 hPa, vientos muy violentos y lluvia torrencial, a veces con tormentas eléctricas; suele tener una región central, el «ojo» (OMM, 2023). Definición alternativa: ciclón sinóptico de núcleo cálido, no frontal, originado sobre aguas tropicales o subtropicales, con convección profunda organizada y circulación cerrada de viento en torno a un centro definido (OMM, 2024). |
| MH0703 | Marejada de tormenta (marino) | Diferencia entre el nivel real del agua bajo la influencia de una perturbación meteorológica y el nivel que habría ocurrido sin ella, es decir, con la marea astronómica (OMM, 2008, 2011, 2017). |
| MH0704 | Marea de tormenta (marino) | Nivel real del mar bajo la influencia de una perturbación meteorológica: la marea astronómica normal más la marejada (OMM, 2017). |

Fuente: {cite:p}`undrr2025hips`.

**Qué se incluye y por qué.**

- **Se incluyen los tres perfiles.** El HIP recuerda que «huracán», «tifón» y «ciclón» son nombres regionales del mismo fenómeno, y que en el Caribe y el Atlántico occidental se llama huracán; es el uso del libro.
- **Marejada y marea de tormenta.** Los HIPs las separan: la marejada es el exceso sobre la marea astronómica, y la marea de tormenta es el nivel total. El Atlas usa «marea de tormenta» para lo que los HIPs llaman marejada; el libro dice cuál usa en cada caso.
- **Etapas.** Los HIPs no tienen perfiles por etapa (depresión, tormenta, huracán) ni por categoría; la escala de Saffir–Simpson del Atlas queda fuera.
- **No se desarrollan** la depresión o ciclón de baja presión (MH0306), el ciclón subtropical (MH0308), el extratropical (MH0307) ni el viento (MH0301).
- **Cascadas.** Los HIPs registran el ciclón tropical como causa de inundación fluvial, repentina, costera y por aguas subterráneas, y de tornados, marejada y erosión costera {cite:p}`undrr2025hips`; ver [](312_vendavales.md) para los vientos fuertes que no son de un ciclón.

## 2. Amenaza

### Enfoque probabilista

INGENIAR (Cardona et al., 2015) desarrolló la metodología de evaluación probabilista usada en el Atlas. Genera un conjunto estocástico de ciclones a partir de la frecuencia histórica y de sus grados de intensidad. El conjunto debe contener todas las formas posibles en que la amenaza se puede manifestar en la región, en frecuencia y severidad {cite:p}`ungrd2019atlas`. El Atlas muestra mapas de viento y de marea de tormenta para un periodo de retorno de 100 años {cite:p}`ungrd2019atlas`.

La simulación matemática de ciclones se usa también para estimar la tormenta de diseño de edificios, el oleaje y las líneas de inundación por marejada, y las pérdidas {cite:p}`ungrd2019atlas`.

### Estudios locales

- **Inundación por huracán en el archipiélago.** Un estudio evalúa la amenaza de inundación por huracán en San Andrés, Providencia y Santa Catalina, a raíz de Iota {cite:p}`rey2021hurricane`.
- **Parámetros meteo–marinos de Matthew.** Establece una línea base de conocimiento del huracán Matthew de 2016 en el Caribe colombiano continental {cite:p}`ortizroyero2021coastal`.
- **Modelo paramétrico de viento.** Una modificación del modelo mejora la asimetría en la región de viento máximo {cite:p}`roldan2023modified`.
- **Reconstrucción de Eta e Iota** en San Andrés y Providencia, con vientos extremos, inundación por marea de tormenta e inundación por lluvia {cite:p}`osorio2024reconstructing`.
- **Riesgo de marea de tormenta** en condiciones climáticas del pasado cercano, para informar el uso del suelo {cite:p}`velasquezcalderon2027assessing`.

### Vientos fuertes que no son de un ciclón

Los vientos fuertes, repentinos y locales de las tormentas convectivas (los vendavales) no se modelan con la cadena de ciclones; tienen su propio capítulo: [](312_vendavales.md).

## 3. Exposición

Como criterio de método, se consideran expuestos al viento las edificaciones y las líneas vitales, y a la marea de tormenta la infraestructura costera, la población y los puertos. CLIMAAX define la exposición del viento como un mapa de activos con su daño máximo por metro cuadrado, clasificados por tipo {cite:p}`climaax2025handbook`.

El caso de San Andrés y Providencia muestra la importancia del inventario de vivienda y de su material y estado, que no se obtiene de datos globales.

## 4. Vulnerabilidad

Cada amenaza necesita su propia función de vulnerabilidad; el esquema general de valor esperado y varianza se describe en [](../04_vulnerabilidad/42_funciones_dano.md). Para viento, CLIMAAX define la vulnerabilidad como una colección de curvas de daño por clase de activo {cite:p}`climaax2025handbook`.

La vulnerabilidad social y cultural también pesa. Un caso es la reflexión sobre la vulnerabilidad en el Caribe tras huracanes y reconstrucción (ID 560) y los derechos territoriales raizales en Providencia tras Iota (ID 908), ambos por leer.

## 5. Riesgo

Con la cadena estocástica de eventos, la exposición y la vulnerabilidad se obtienen la curva de excedencia de pérdidas y la PAE ({cite:p}`ungrd2019atlas`; ver [](../02_metodologia/22_probabilista_pae.md)). Dos advertencias:

- La baja frecuencia hace que la PAE sea pequeña frente a la pérdida máxima probable. Para islas conviene mostrar ambas.
- Los componentes viento, marea de tormenta y lluvia se evalúan por separado y luego se combinan; CCDR-tools modela solo el viento del ciclón y trata las inundaciones y la marea de tormenta aparte {cite:p}`ccdr2025tools`.

## 6. Clima

El efecto del clima sobre los ciclones es difícil de atribuir, pero CCDR-tools resume que se espera un aumento robusto de los ciclones más devastadores, con tormentas de ese tipo hasta dos veces más frecuentes bajo 2,5 °C de calentamiento {cite:p}`ccdr2025tools`. Debe verificarse con el AR6 antes de aplicarlo al Caribe colombiano.

La marea de tormenta se suma al nivel del mar. CCDR-tools reúne conjuntos de datos de inundación costera y marea de tormenta que incluyen el efecto del ascenso del nivel del mar bajo proyecciones climáticas {cite:p}`ccdr2025tools`. Ver [](306_erosion_costera.md).

## 7. Datos y medidas

### Datos y monitoreo

| Elemento | Qué ofrece | Referencia |
|---|---|---|
| NOAA: Centro Nacional de Huracanes | Pronóstico de intensidad y trayectoria | {cite:p}`ungrd2019atlas` |
| Organización Meteorológica Mundial | Información internacional | {cite:p}`ungrd2019atlas` |
| GAR15-IBTrACS, IBTrACS v4 y STORM v4 | Conjuntos de amenaza de viento de ciclones listados por CCDR-tools | {cite:p}`ccdr2025tools` |
| IBTrACS v04r01, cuenca del Atlántico Norte | Trayectorias e intensidad desde 1851, de descarga abierta; usada en la figura de este capítulo | {cite:p}`knapp2019ibtracs` |

### Incertidumbres

- Pocos eventos históricos en el Caribe colombiano para calibrar frecuencia.
- Los modelos paramétricos de viento deben validarse localmente {cite:p}`roldan2023modified`.
- La resolución de los conjuntos globales de marea de tormenta es gruesa para una isla pequeña.

### Medidas según la Ley 1523

| Proceso | Medida |
|---|---|
| Conocimiento | Reconstrucción de eventos recientes, mapas de inundación por marea de tormenta |
| Reducción | Códigos de construcción para viento, ordenamiento costero, reconstrucción con criterios de reducción del riesgo |
| Manejo | Alerta temprana con el Centro Nacional de Huracanes, planes de evacuación, albergues |

La tabla de medidas es un criterio de método de este libro. El Atlas trata los ciclones sin detallar medidas {cite:p}`ungrd2019atlas`.

## Síntesis de evidencia

```{note}
**Método.** Síntesis narrativa por tipo de evidencia (no un metaanálisis con efectos agrupados: los estudios usan diseños, escalas y variables que no se pueden combinar en un solo estimador). Se leyeron los resúmenes de los artículos de la hoja de vigilancia que están en la carpeta de PDFs; las cifras vienen de esos resúmenes y **faltan por verificar contra el texto completo**.
```

| Estudio | Diseño y lugar | Resultado relevante |
|---|---|---|
| {cite:t}`ortiz2022huracan` | Modelo paramétrico de viento acoplado a SWAN, huracán de 1911 en San Andrés | Vientos cercanos a 200 km/h a 22 km de la costa norte de San Andrés; oleaje menor que el de Iota (2020) y Joan (1988); calibrado con la boya del huracán Matthew (2016) |
| {cite:t}`acostacoll2022cross` | Comparación entre radar terrestre NEXRAD y radar satelital GPM, Puerto Rico | Evalúa la correlación entre sensores durante ciclones para alertas oportunas |
| {cite:t}`varon2025desastres` | Revisión documental y de prensa, Colombia y Honduras | Las entidades de gestión siguen una visión clásica del riesgo orientada a mitigar efectos, no las causas estructurales de la vulnerabilidad |

**Lectura conjunta.** Hay un método reproducible para reconstruir eventos históricos sin registros (modelo paramétrico de viento más oleaje, calibrado con un evento reciente) {cite:p}`ortiz2022huracan`, útil para estimar la amenaza en el archipiélago. La evidencia sobre gestión es cualitativa y comparativa, de dos casos {cite:p}`varon2025desastres`.

**Estudios añadidos con el segundo lote de PDFs.**

| Estudio | Diseño y lugar | Resultado relevante |
|---|---|---|
| {cite:t}`alvarezecheverry2025multi` | Análisis multitemporal con Sentinel-2 e índices NDVI, NDWI, BSI y NBR, huracanes Iota y Eta (2020), archipiélago de San Andrés | En Providencia y Santa Catalina los más afectados fueron bosques, manglares, vegetación secundaria y playas |
| {cite:t}`hernandezhamon2024rapid` | Clasificación supervisada con Google Earth Engine y batimetría satelital, arrecifes de Providencia | Pérdida de 38,14 % en el arrecife posterior y de 6,15 % en la terraza rocosa; la cresta arrecifal casi no cambió y actuó como barrera del oleaje |
| {cite:t}`marquezperez2024overcoming` | Reflexión cultural sobre la comunidad raizal tras Iota (categoría 4, 2020) | La comunidad se adaptó y reorganizó pese a una respuesta gubernamental caótica |

**Lectura adicional.** Los efectos de un ciclón se miden tanto en la cobertura y los ecosistemas costeros como en la capacidad social de respuesta; los arrecifes funcionan como defensa natural {cite:p}`hernandezhamon2024rapid,alvarezecheverry2025multi,marquezperez2024overcoming`.

## Pendiente

- Leer completos {cite:p}`rey2021hurricane`, {cite:p}`osorio2024reconstructing` y {cite:p}`velasquezcalderon2027assessing`.
- La cifra de 80 % de muertes por huracanes donde tocan tierra está en el Atlas tal como se cita en el capítulo; falta hallar la fuente primaria que el Atlas no indica en ese pasaje.
- Añadir las funciones de vulnerabilidad al viento y los parámetros de la marea de tormenta del Atlas.
- Usar los radios de viento de IBTrACS (R34, R50, R64) para estimar la huella de viento de cada sistema sobre los sitios, y no solo la distancia.
- Extender el conteo a todo el periodo desde 1851 con las salvedades de calidad de datos, y a la costa del Pacífico si se agrega esa cuenca.
- Documentar la inclusión de ciclones en CLIMADA (módulo de ciclones tropicales) después de revisar su documentación.

## Bibliografía recomendada

Lista de los 25 registros de la hoja de vigilancia científica (pestaña `Vigilancia_CTeI`, columna `AMENAZA_ESPECIFICA` = «Ciclón tropical»), en formato APA 7 con metadatos de Crossref. Son lecturas recomendadas: **no están verificadas contra el texto completo** ni se usan como evidencia hasta que se citen en el capítulo. Las entradas sin DOI carecen de autores en la hoja.

- Acosta-Coll, M., Morales, A., Zamora-Musa, R., & Butt, S. A. (2022). Cross-Evaluation of Reflectivity from NEXRAD and Global Precipitation Mission during Extreme Weather Events. *Sensors*, *22*(15), 5773. https://doi.org/10.3390/s22155773

- Álvarez-Echeverry, A., Toro-Restrepo, L. J., Suárez-Gómez, J. A., & Osorio-Cano, J. D. (2025). Multi-temporal analysis of land cover changes due to hurricanes Iota and Eta on the islands of San Andres, Providencia and Santa Catalina. *DYNA*, *92*(235), 9-18. https://doi.org/10.15446/dyna.v92n235.113880

- Aparicio Cuervo, J. R., & Macías Perdomo, L. V. (2024). Hurricanes, reconstruction, and resistance: thinking through vulnerability in the Caribbean. *Disasters*, *49*(1), e12664. https://doi.org/10.1111/disa.12664

- Arregocés, H. A., & Fuentes Molina, N. (2026). Quantifying the Contribution of Tropical Cyclones to Precipitation Variability in Northern South America (2016–2025). *Environments*, *13*(6), 331. https://doi.org/10.3390/environments13060331

- Bernal, R., Lacouture, S., Perez-Cardona, S., & Rettberg, A. (2026). Peace, democracy, and the weather: did hurricane Matthew botch the 2016 Colombian peace referendum? *Journal of Peace Research*, *63*(4), 661-674. https://doi.org/10.1093/jopres/xjag014

- Cabarcas-Mier, A., Rey, W., Torrecillas, C., Paladio-Hernandez, A., Cahuich-López, M., Salles, P., Muñoz-Perez, J. J., de Santos-Medina, L., & Jigena-Antelo, B. (2025). Assessment of the shoreline dynamics in San Andres Island: A remote sensing and EOF analysis approach. *Regional Studies in Marine Science*, *90*, 104435. https://doi.org/10.1016/j.rsma.2025.104435

- Carbonó dela Rosa, M. E., Ospino-Castro, A., Robles-Algarín, C., Restrepo-Leal, D., & Olivero-Ortiz, V. (2026). Integrated Multi-Scale Spectral Framework for Tropical Cyclone Dynamics: Implications for Offshore Wind Energy Resilience in the Atlantic Caribbean Basin. *Energies*, *19*(10), 2473. https://doi.org/10.3390/en19102473

- Giraldo, S. (2023). Winds, Rain, and Thunder. *Managing Disaster Risks to Cultural Heritage*, 213-225. https://doi.org/10.4324/9781003263647-13

- Hernández-Hamón, H., Zapata-Ramírez, P. A., Vásquez, R. E., Zuluaga, C. A., Mejía, J. D. S., & Cano, M. (2024). Rapid Remote Sensing Assessment of Impacts from Hurricane Iota on the Coral Reef Geomorphic Zonation in Providencia. *Disaster Risk Reduction*, 69-87. https://doi.org/10.1007/978-981-97-6663-5_4

- Márquez-Pérez, A. I. (2024). Overcoming Iota: A Reflection on Old Providence and Santa Catalina Cultural Resilience In the Face of Disaster and Climate Change. *Disaster Risk Reduction*, 209-231. https://doi.org/10.1007/978-981-97-6663-5_10

- Martínez-Rivera, W., Carvalhaes, T., Jevtić, P., & Reddy, T. A. (2022). A treatment-effect model to quantify human dimensions of disaster impacts: the case of Hurricane Maria in Puerto Rico. *Natural Hazards*. https://doi.org/10.1007/s11069-022-05753-6

- Medina, N., Sanchez, A., & Vojinovic, Z. (2023). Emergency Evacuation Behavior in Small Island Developing States: Hurricane Irma in Sint Maarten. *Water*, *15*(11), 2117. https://doi.org/10.3390/w15112117

- Miramonti, A. (2026). Engaging Haitian youth in hurricane preparedness: Drama-based action research. *Emotion, Space and Society*, *59*, 101165. https://doi.org/10.1016/j.emospa.2026.101165

- Ortiz Royero, J. C., Cera, S. H., & Gomes, H. (2021). Coastal Meteo-marine Parameters of Hurricane Matthew along the Colombian Caribbean Coast: Establishing a Baseline of Knowledge. *Journal of Coastal Research*, *38*(1), 66-76. https://doi.org/10.2112/jcoastres-d-20-00108.1

- Ortiz, J. C., & Conde, M. (2022). El huracán que pasó sobre la Isla de San Andrés en 1911. *Revista de la Academia Colombiana de Ciencias Exactas, Físicas y Naturales*, *46*(180), 795-806. https://doi.org/10.18257/raccefyn.1743

- Osorio, A. F., Montoya, R., Ayala, F. F., & Osorio-Cano, J. D. (2024). Reconstructing the Eta and Iota Events for San Andrés and Providencia: A Focus on Urban and Coastal Flooding. *Disaster Risk Reduction*, 39-67. https://doi.org/10.1007/978-981-97-6663-5_3

- Osorio-Cano, J. D., Alcérreca-Huerta, J. C., Navarro, B. A., & Álvarez-Silva, O. (2024). The Seaflower Biosphere Reserve: Research advances on ocean and coastal processes and related hazards for the regional management. *Ocean & Coastal Management*, *258*, 107414. https://doi.org/10.1016/j.ocecoaman.2024.107414

- Pérez-Arévalo, R., Jiménez-Caldera, J. E., Serrano-Montes, J. L., Rodrigo-Comino, J., Ortiz Royero, J. C., & Caballero-Calvo, A. (2025). Impacts of Urban Morphology on Micrometeorological Parameters and Cyclonic Phenomena in Northern Colombian Caribbean. *Climate*, *13*(5), 87. https://doi.org/10.3390/cli13050087

- Rey, W., Ruiz-Salcines, P., Salles, P., Urbano-Latorre, C. P., Escobar-Olaya, G., Osorio, A. F., Ramírez, J. P., Cabarcas-Mier, A., Jigena-Antelo, B., & Appendini, C. M. (2021). Hurricane Flood Hazard Assessment for the Archipelago of San Andres, Providencia and Santa Catalina, Colombia. *Frontiers in Marine Science*, *8*, 766258. https://doi.org/10.3389/fmars.2021.766258

- Roldán, M., Montoya, R. D., Rios, J. D., & Osorio, A. F. (2023). Modified parametric hurricane wind model to improve the asymmetry in the region of maximum winds. *Ocean Engineering*, *280*, 114508. https://doi.org/10.1016/j.oceaneng.2023.114508

- Valencia, J., Yepes, J., Mejía, J. F., Builes-Jaramillo, A., & Salas, H. D. (2024). Influence of Tropical Easterly Waves on the ChocoJet during the 2019 OTREC Campaign. *Journal of Hydrometeorology*, *25*(2), 325-337. https://doi.org/10.1175/jhm-d-23-0039.1

- Varón Rojas, D. H., & Reyes Corea, S. M. (2025). Desastres y sufrimiento: Temporada de huracanes en Colombia y Honduras. *Revista de Estudios Latinoamericanos sobre Reducción del Riesgo de Desastres REDER*, *9*(1), 97. https://doi.org/10.55467/reder.v9i1.172

- Velásquez-Calderón, C. S., Alvarez, A., Rey, W., Ruiz-Salcines, P., Urbano-Latorre, C. P., & Santos-Martínez, A. (2027). Assessing hurricane storm surge risk under near-past climate conditions to inform land-use planning in small Caribbean islands: San Andrés, Providencia, and Santa Catalina, Colombia. *Ocean & Coastal Management*, *283*, 108404. https://doi.org/10.1016/j.ocecoaman.2026.108404

- Velásquez-Calderón, C. S., Ortiz-Roca, F., & Santos-Martínez, A. (2026). Maritory and spatial justice after hurricane Iota: Raizal territorial rights in Providencia and Santa Catalina,Western Caribbean. *International Journal of Disaster Risk Reduction*, *141*, 106171. https://doi.org/10.1016/j.ijdrr.2026.106171

- Zapata-Henao, M., Hoyos, C. D., & Cardona, Y. (2026). Evaluation and Setup of a High-Resolution Regional Coupled Ocean–Atmosphere Model for Hindcasting Tropical Cyclones in the North Atlantic Ocean Basin. *Atmosphere*, *17*(4), 356. https://doi.org/10.3390/atmos17040356
