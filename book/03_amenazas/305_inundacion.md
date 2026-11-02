---
title: Inundaciones
---

# Inundaciones

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

## Pendiente

- Verificar las citas de {cite:p}`kreibich2022unprecedented`, {cite:p}`jimenez2022nonstat` y {cite:p}`chanchi2023fuzzy` leyendo los artículos completos; hoy solo se apoyan en el objetivo declarado.
- Añadir las curvas de daño y valores máximos de daño para Colombia (capítulo 4.2).
- Añadir inundación pluvial urbana con los casos de SIDRo y Leticia y los sistemas urbanos de drenaje sostenible.
- Añadir los capítulos 2021 (14), 2023 (6) y 2025 de la serie de investigaciones GRD.
