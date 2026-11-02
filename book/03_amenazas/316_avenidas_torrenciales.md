---
title: Avenidas torrenciales
---

# Avenidas torrenciales

Este capítulo sigue el molde de siete puntos ([](_molde.md)) y se apoya sobre todo en la guía metodológica del Servicio Geológico Colombiano (SGC) y la Pontificia Universidad Javeriana {cite:p}`sgc2021avenidas`. Esa guía es la referencia nacional para zonificar la amenaza y tiene licencia CC BY 4.0. Aquí se resume y se organiza para el análisis de una ciudad; para ejecutar un estudio hay que consultarla completa.

## 1. Fenómeno

La guía define la avenida torrencial como un flujo muy rápido, en canales de alta pendiente longitudinal, de agua con una cantidad significativa de sólidos {cite:p}`sgc2021avenidas`. El término agrupa flujos de detritos, flujos de lodo y flujos hiperconcentrados, que se distinguen por la proporción y el tamaño de los sedimentos {cite:p}`sgc2021avenidas`.

Se diferencia de la creciente súbita de [](305_inundacion.md) por la carga sólida: en una avenida torrencial los sedimentos y la madera cambian la densidad, la fuerza de impacto y la forma en que el flujo se desborda y se deposita. Por eso la profundidad no basta como variable de intensidad.

**Variable de intensidad.** La guía usa un índice de intensidad del flujo, IDF = h·v² (altura por velocidad al cuadrado, en m³/s²), propuesto por Jakob y colaboradores y adoptado como medida de la fuerza destructiva {cite:p}`sgc2021avenidas`. Se complementa con el tamaño de bloques, representado por el D90 (m).

```{note}
En Colombia las avenidas torrenciales ocurren con frecuencia junto con inundaciones y movimientos en masa. Un caso conocido es el de Mocoa en 2017, citado en [](305_inundacion.md).
```

### Definición según los HIPs de UNDRR

Los perfiles de información de amenazas ([](../01_conceptos/16_hips_undrr.md)) que corresponden a este capítulo son:

| Código | Perfil | Relación con el capítulo |
|---|---|---|
| MH0603 | Inundación repentina | Inundación de corta duración con un caudal pico relativamente alto (OMM, 2021) {cite:p}`undrr2025hips`. |
| GH0303 | Flujos de detritos, de tierra (lodo) y avalanchas de roca | Movimientos en masa gravitacionales en forma de fluido, que suelen dejar un depósito en abanico {cite:p}`undrr2025hips`. |

**Qué se incluye y por qué.** La avenida torrencial colombiana combina las dos cosas: el caudal pico rápido de MH0603 y el transporte de sedimentos de GH0303. Es una correspondencia de criterio de este libro, no una equivalencia declarada por los HIPs.

## 2. Amenaza

La guía organiza la zonificación en cuatro etapas {cite:p}`sgc2021avenidas`:

1. **Caracterización de la avenida torrencial**: geomorfología, susceptibilidad, inventario histórico (con un formato de inventario propio) e índices morfométricos para decidir qué cuencas son propensas.
2. **Análisis de detonantes**: sobre todo la lluvia. Se trabaja con periodos de retorno de 2,33, 5, 10, 25, 50, 100, 300 y 500 años, curvas intensidad–duración–frecuencia del IDEAM y registros de al menos 30 años; un modelo hidrológico produce los hidrogramas.
3. **Caracterización de la amenaza** con modelos fluidodinámicos bidimensionales que incorporan la reología del flujo. Los sólidos que alimentan la avenida provienen de movimientos en masa, erosión de laderas y socavación lateral.
4. **Zonificación** en categorías baja, media y alta.

### Escalas y criterios

La guía distingue dos escalas, que responden al Decreto 1077 de 2015 y a la Ley 388 de 1997 {cite:p}`sgc2021avenidas`:

| Escala | Uso | Criterio de zonificación |
|---|---|---|
| 1:25.000 | Rural | El IDF se pondera por la frecuencia de los periodos de retorno y se combina con el D90 en una matriz de tres por tres |
| 1:2.000 | Urbana y de expansión | Curvas de amenaza por celda (al menos seis puntos) y dos criterios cuyo máximo define la categoría |

En la escala 1:2.000, el primer criterio usa un índice de confiabilidad β entre 2,5 y 3 (probabilidad de 0,0025, es decir un periodo de retorno cercano a 400 años) con umbrales de IDF de 1 y 50 para baja, media y alta. El segundo fija un umbral de IDF = 5 y clasifica por recurrencia: alta si es menor de 30 años, media entre 30 y 100, baja desde 100 {cite:p}`sgc2021avenidas`.

**Falsos negativos.** Si un evento reciente (menos de 500 años) ocurrió donde el modelo dice amenaza baja, la guía propone reclasificar según la magnitud del evento {cite:p}`sgc2021avenidas`.

**Escenarios adicionales.** Represamiento por movimientos en masa, madera flotante (troncos de más de 1 m de largo y 10 cm de diámetro) y avulsión por rotura de diques {cite:p}`sgc2021avenidas`.

```{warning}
Hay que revisar el valor de cada umbral y de cada periodo de retorno en la guía antes de usarlos en un estudio: aquí se resumen para orientar, no para reemplazar el texto.
```

## 3. Exposición

La guía trata la zonificación de amenaza y propone, al final, estimar el riesgo de un escenario como el producto de la amenaza (H) por la vulnerabilidad (V), con el riesgo total como la integral sobre los escenarios {cite:p}`sgc2021avenidas`. Para la exposición se usan los mismos insumos que en inundación: población, edificaciones y vías sobre el abanico y los cauces ([](../04_vulnerabilidad/index.md)).

Los abanicos aluviales son lugares de expansión urbana frecuente, y la zonificación 1:2.000 está pensada justamente para esas áreas.

## 4. Vulnerabilidad

La guía no desarrolla funciones de daño propias. La vulnerabilidad debe tomarse de las funciones de daño por intensidad de [](../04_vulnerabilidad/42_funciones_dano.md), usando el IDF o la presión de impacto como variable, no solo la profundidad. Falta una fuente colombiana verificada para curvas de daño por IDF.

## 5. Riesgo

Con la curva de amenaza por celda (IDF contra periodo de retorno), la exposición y una función de daño, el riesgo se calcula como en [](../02_metodologia/22_probabilista_pae.md): se integran las pérdidas sobre la probabilidad anual de excedencia.

La guía advierte que la validación con casos piloto todavía está pendiente {cite:p}`sgc2021avenidas`. Un estudio completo requiere un equipo con geología, hidrología, geotecnia, hidráulica, SIG y manejo forestal, y la modelación toma de semanas a meses.

## 6. Clima

La guía concluye que modelar el cambio climático no mejoraría el análisis del detonante, porque las tendencias de precipitación extrema del IDEAM no son significativas, y que el cambio de cobertura y el crecimiento de la población pesan más {cite:p}`sgc2021avenidas`. Recomienda actualizar la zonificación periódicamente.

Este libro sigue esa postura para el detonante y propone, como criterio propio, revisar con el capítulo [](../02_metodologia/23_escenarios_climaticos.md) si el clima cambia la frecuencia de lluvias extremas en la cuenca de estudio.

## 7. Datos y medidas

### Datos necesarios

| Insumo | Fuente |
|---|---|
| Curvas IDF, series de lluvia (≥30 años) | IDEAM {cite:p}`sgc2021avenidas` |
| Modelo digital de elevación y geomorfología | SGC e IGAC {cite:p}`sgc2021avenidas` |
| Inventario histórico de eventos | Formato del anexo 1 de la guía {cite:p}`sgc2021avenidas` |
| Cobertura y suelos | Para la hidrología y el aporte de sedimentos |

### Incertidumbres principales

- Calibración de la reología con pocos eventos documentados.
- Cantidad de sedimentos disponibles y madera.
- Validación pendiente con casos piloto {cite:p}`sgc2021avenidas`.

### Medidas según la Ley 1523

| Proceso | Medida |
|---|---|
| Conocimiento | Zonificación 1:25.000 rural y 1:2.000 urbana; inventario histórico; monitoreo de lluvia |
| Reducción: prevención | Incorporar la zonificación al ordenamiento territorial, con restricción de usos en abanicos y rondas |
| Reducción: mitigación | Control de sedimentos y cobertura en la cuenca; por detallar con fuente |
| Manejo | Alerta temprana por lluvia y evacuación; por detallar con fuente |

## Síntesis de evidencia

```{note}
**Método.** Síntesis narrativa por tipo de evidencia (no un metaanálisis con efectos agrupados: los estudios usan diseños, escalas y variables que no se pueden combinar en un solo estimador). Se leyeron los resúmenes de los artículos de la hoja de vigilancia que están en la carpeta de PDFs; las cifras vienen de esos resúmenes y **faltan por verificar contra el texto completo**.
```

| Estudio | Diseño y lugar | Resultado relevante |
|---|---|---|
| {cite:t}`arango2020morphometrical` | Aprendizaje automático con parámetros morfométricos de cuencas de montaña, norte de la cordillera Andina colombiana | Susceptibilidad a flujos torrenciales a escala de cuenca, para priorizar zonas antes de los mapas de amenaza |
| {cite:t}`arangocarmona2025hillslope` | Base de 22 eventos en cascada, 2009–2024, montañas tropicales (versión publicada en *Natural Hazards and Earth System Sciences*) | Solo pocos casos coinciden con las lluvias más extremas, lo que sugiere que otros controles, como el sedimento disponible, son necesarios; en regiones de pendientes fuertes y suelos finos hubo cascadas con lluvia de menor intensidad; los sismos y la lluvia pueden interactuar en el tiempo |
| {cite:t}`ramoscanon2023redundancia`; {cite:t}`ramoscanon2026desempeno` | Umbrales de alerta temprana de Mocoa (precipitación, nivel y caudal) con modelación física y análisis probabilista; evaluación con la avenida de 2018 | La avenida del 31 de marzo de 2017 causó 332 muertos, 398 heridos y 77 desaparecidos; en 2018 la combinación precipitación–movimientos en masa llegó a alerta roja una hora antes del impacto y la de precipitación–caudal no superó el umbral; se evacuó a más de 20 000 personas y no hubo víctimas. Los autores resaltan la necesidad de redundancia en los umbrales |
| {cite:t}`aponte2026vulnerabilidad` | Vulnerabilidad social con AHP y lógica difusa, quebrada Isabel Pérez, Cali (97 hogares) | El 52 % de los hogares tiene vulnerabilidad alta, el 20 % media y el 25 % baja; el capital financiero es lo más afectado (80 % con ingresos iguales o menores que los gastos) |
| {cite:t}`munoz2025experimental` | Ensayos de laboratorio en canal (pendientes de 5 a 20 %) y modelos numéricos para flujos de lodo | Estima parámetros reológicos y la altura de depósito para un caso real |
| {cite:t}`paez2025debris` | Revisión de modelación de flujos de lodo y detritos como herramienta de amenaza | Resalta que el cambio climático podría aumentar las pérdidas |
| {cite:t}`smolikova2021analysis` | Análisis de lluvia detonante de un flujo de detritos, República Checa | Acumulados de 2 a 60 días e índices de precipitación antecedente (1983–2018); referencia metodológica externa |
| {cite:t}`diaz2022alianzas` | Estudio cualitativo de la reconstrucción tras el desastre de Salgar (2015) | Las alianzas público-privadas y sin ánimo de lucro cumplieron un papel central en la reconstrucción |

**Lectura conjunta.**

- **La lluvia extrema no basta.** Si pocas cascadas ocurren con las lluvias más extremas {cite:p}`arangocarmona2025hillslope`, el detonante debe analizarse junto con el sedimento disponible. Esto es coherente con la estructura de la guía del SGC ({cite:p}`sgc2021avenidas`) que modela los sólidos aparte de la lluvia.
- **Priorización previa.** La morfometría de cuenca permite pasar de cientos de cuencas a unas pocas prioritarias antes de modelar {cite:p}`arango2020morphometrical`.
- **Alerta temprana con redundancia.** El caso de Mocoa muestra que varios umbrales independientes (lluvia–deslizamiento, lluvia–caudal) pueden fallar de manera distinta y que la redundancia salvó vidas en 2018 {cite:p}`ramoscanon2026desempeno,ramoscanon2023redundancia`.
- **Vulnerabilidad de quienes viven en la quebrada.** El capital financiero débil caracteriza a la mayoría de los hogares encuestados en Cali {cite:p}`aponte2026vulnerabilidad`; se suma a la exposición física.
- **Evidencia limitada.** Hay pocos estudios de validación de los umbrales de la guía del SGC con eventos colombianos; el de Mocoa es el más cercano.

## Pendiente

- Leer los capítulos 3, 5 y 6 de la guía completos y verificar umbrales.
- Añadir medidas de mitigación y alerta temprana con fuente.
- Añadir un caso colombiano (Mocoa 2017, Salgar 2015) con fuente primaria.

## Bibliografía recomendada

Lista de los 25 registros de la hoja de vigilancia científica (pestaña `Vigilancia_CTeI`, columna `AMENAZA_ESPECIFICA` = «Flujos de detritos y tierra (lodo) y avalanchas de roca»; «Inundación repentina»), en formato APA 7 con metadatos de Crossref. Son lecturas recomendadas: **no están verificadas contra el texto completo** ni se usan como evidencia hasta que se citen en el capítulo. Las entradas sin DOI carecen de autores en la hoja.

- Aponte García, V., Tarapuez Bolaños, D. F., García Millán, N., & Salcedo Hurtado, E. d. J. (2026). Vulnerabilidad social frente a avenida torrencial (flujo de detritos) en el área de influencia de la quebrada Isabel Pérez en Santiago de Cali, Colombia, usando lógica difusa. *Documents d'Anàlisi Geogràfica*, *72*(1), 135-167. https://doi.org/10.5565/rev/dag.1445

- Arango, M. I., Aristizábal, E., & Gómez, F. (2020). Morphometrical analysis of torrential flows-prone catchments in tropical and mountainous terrain of the Colombian Andes by machine learning techniques. *Natural Hazards*, *105*(1), 983-1012. https://doi.org/10.1007/s11069-020-04346-5

- Arango-Carmona, M. I., Voit, P., Hürlimann, M., Aristizábal, E., & Korup, O. (2025). Hillslope-Torrential Hazard Cascades in Tropical Mountains. *Egusphere*. https://doi.org/10.5194/egusphere-2025-1698

- Arango-Carmona, M. I., Voit, P., Hürlimann, M., Aristizábal, E., & Korup, O. (2025). Hillslope torrential hazard cascades in tropical mountains. *Natural Hazards and Earth System Sciences*, *25*(9), 3641-3663. https://doi.org/10.5194/nhess-25-3641-2025

- Assessing debris flow susceptibility using triggering and propagation models, a case study in the tropical region of the northern andes in colombia. (2023). *Revista de la Asociacion Geologica Argentina*. https://revista.geologica.org.ar/raga/article/view/1660

- Bocanegra, R. A., Ramírez, C. A., Salcedo, E. d. J., & Villegas, M. P. L. (2023). Determination of Hazard Due to Debris Flows. *Water*, *15*(23), 4057. https://doi.org/10.3390/w15234057

- Cardona, F. G., Giraldo, E. A., & Mergili, M. (2025). Modelling debris flood propagation in scarce data terrain, case study in the Colombian Andes. *Journal of South American Earth Sciences*, *165*, 105660. https://doi.org/10.1016/j.jsames.2025.105660

- Díaz Ramírez, J. H., Páez Martínez, H. J., Lizarralde, G., & Herazo, B. (2022). El rol de las alianzas sociales en el proceso de reconstrucción en Salgar, Colombia. *Letras Verdes. Revista Latinoamericana de Estudios Socioambientales*(31), 115-134. https://doi.org/10.17141/letrasverdes.31.2022.5092

- Garzon, L. F. L., Johnson, M. F., Mount, N., & Gomez, H. (2023). Exploring the effects of catchment morphometry on overland flow response to extreme rainfall using a 2D hydraulic-hydrological model (IBER). *Journal of Hydrology*, *627*, 130405. https://doi.org/10.1016/j.jhydrol.2023.130405

- Guerrero-Miranda, P., & Luque González, A. (2021). Social Responsibility, Sustainability, and Public Policy: The Lessons of Debris Management after the Manabí Earthquake in Ecuador. *International Journal of Environmental Research and Public Health*, *18*(7), 3494. https://doi.org/10.3390/ijerph18073494

- Henao Salgado, M. J., & Zambrano Nájera, J. (2022). Assessing Flood Early Warning Systems for Flash Floods. *Frontiers in Climate*, *4*, 787042. https://doi.org/10.3389/fclim.2022.787042

- Luna, C. C., Zambrano Nájera, J., & Vélez Upegui, J. J. (2025). Lessons learned from flash floods early warning system in a mountainous rur-urban region of Colombia. *Environmental Challenges*, *20*, 101199. https://doi.org/10.1016/j.envc.2025.101199

- Machuca, S., García-Delgado, H., & Ramos-Cañón, A. M. (2024). Assessing torrentiality in catchments of the tropical Andes: A morphometric approach. *Journal of South American Earth Sciences*, *134*, 104775. https://doi.org/10.1016/j.jsames.2023.104775

- Moreno-Alfonso, S. C., Sánchez, J. J., & Murcia, H. (2021). Evidences of an unknown debris avalanche event (<0.58 Ma), in the active azufral volcano (Nariño, Colombia). *Journal of South American Earth Sciences*, *107*, 103138. https://doi.org/10.1016/j.jsames.2020.103138

- Muñoz, F., Vega, J., & Hidalgo, C. (2025). Experimental and numerical mudflows modeling for runout and deposition height assessment. *Natural Hazards*, *121*(20), 23723-23754. https://doi.org/10.1007/s11069-025-07193-4

- Páez Pedraza, J. P. (2025). Mud and debris flow modeling as hazard assessment tool. *Ingenieria y Universidad*, *29*. https://doi.org/10.11144/javeriana.iued29.mdfm

- Paez, L. V., Sánchez, J. J., & Castro-Caicedo, Á. J. (2024). Morphology of the collapse scar of the Chiles Volcano (Colombia-Ecuador border) and geomechanical characterization of rock masses. *Boletín Geológico*, *51*(1). https://doi.org/10.32685/0120-1425/bol.geol.51.1.2024.714

- Ramos-Cañón, A. M., Munévar, M., Prada-Sarmiento, L. F., Escobar-Vargas, J., Vargas-Luna, A., Prieto, A. F., Reyes, N. C., Medina, M., Pérez, J., & Dorado, L. (2023). Redundancia de los umbrales del sistema de alerta temprana para avenidas torrenciales de Mocoa, Putumayo, Colombia. *Revista de Estudios Latinoamericanos sobre Reducción del Riesgo de Desastres REDER*, *7*(2), 142. https://doi.org/10.55467/reder.v7i2.129

- Ramos-Cañón, A., Prada-Sarmiento, L. F., Munévar-Peña, M., & Castro-Malaver, C. (2026). Desempeño Técnico del Sistema de Alerta Temprana para Avenidas Torrenciales en Mocoa, Colombia. *Revista de Estudios Latinoamericanos sobre Reducción del Riesgo de Desastres REDER*, *10*(2), 301. https://doi.org/10.55467/reder.v10i2.234

- Sanvitale, N., Bowman, E., & Cabrera, M. A. (2021). Experimental Investigation on the Impact Dynamics of Saturated Granular Flows on Rigid Barriers. *Environmental and Engineering Geoscience*, *27*(1), 127-138. https://doi.org/10.2113/eeg-d-20-00033

- Smolíková, J., Hrbáček, F., Blahůt, J., Klimeš, J., Vilímek, V., & Loaiza Usuga, J. C. (2021). Analysis of the rainfall pattern triggering the Lemešná debris flow, Javorníky Range, the Czech Republic. *Natural Hazards*, *106*(3), 2353-2379. https://doi.org/10.1007/s11069-021-04546-7

- The basal friction in the modeling of the propagation of shallow landslides – debris flow using r.avaflow. (2025). *Revista De La Asociacion Geologica Argentina*. (Sin DOI; completar autores).

- Trujillo-Vela, M. G., Ramos-Cañón, A. M., Escobar-Vargas, J. A., & Galindo-Torres, S. A. (2022). An overview of debris-flow mathematical modelling. *Earth-Science Reviews*, *232*, 104135. https://doi.org/10.1016/j.earscirev.2022.104135

- Trujillo-Vela, M., Galindo-Torres, S., Zhang, X., Ramos-Cañón, A., & Escobar-Vargas, J. (2021). SPH-DEM Coupling for Debris Flows. *14th WCCM-ECCOMAS Congress*. https://doi.org/10.23967/wccm-eccomas.2020.316

- Valencia Londoño, P. A., & Valencia Londoño, D. (2024). Persistent Vulnerability after Disaster Risk Reduction (DRR) Response: The Case of Salgar, Colombia. *Sustainability*, *16*(11), 4394. https://doi.org/10.3390/su16114394
