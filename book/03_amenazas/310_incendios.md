---
title: Incendios forestales
---

# Incendios forestales

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

## Pendiente

- Leer {cite:p}`gonzalez2025predicting`, {cite:p}`arias2025compound` y {cite:p}`acevedoortiz2026sequias` completos. Los dos primeros se conocen por título o resumen parcial.
- Verificar el estado actual del protocolo y de la normativa de incendios posteriores a 2019.
- Añadir las cifras recientes de área quemada y su relación con El Niño 2023–2024.
- Evaluar el FWI sobre reanálisis ERA5 para Colombia y su calibración con el inventario del IDEAM.
