---
title: Olas de calor
---

# Olas de calor

Este capítulo sigue el molde de siete puntos ([](_molde.md)). Es el que mejor ilustra la diferencia entre un marco hecho para Europa y una ciudad tropical: las definiciones de ola de calor de CLIMAAX dependen de percentiles climatológicos y de umbrales regionales, y en Colombia no hay una definición oficial adoptada en las fuentes revisadas.

```{important}
**Cobertura de fuentes.** El Atlas de Riesgo de Colombia no trata el calor. El capítulo se apoya en el flujo de olas de calor de CLIMAAX, en la sección de estrés térmico de CCDR-tools y en pocos estudios colombianos de la hoja de vigilancia (8 registros). Es un capítulo provisional.
```

## 1. Fenómeno

Una ola de calor se define por una temperatura máxima y mínima diaria que supera un umbral durante un tiempo mínimo. Las metodologías usan definiciones distintas {cite:p}`climaax2025handbook`. El impacto más claro es el sobrecalentamiento de las áreas urbanas: reduce el confort y amenaza la salud, sobre todo de poblaciones vulnerables, y acompaña a la sequía y a la escasez de agua {cite:p}`climaax2025handbook`.

CCDR-tools añade que la incomodidad térmica aumenta cuando el calor se asocia con humedad alta, que el estrés térmico puede causar deterioro a largo plazo y reducir la productividad y los ingresos, y que los eventos extremos aumentan la morbilidad y la mortalidad {cite:p}`ccdr2025tools`. La respuesta individual al calor varía con la condición médica, el estado físico, el peso, la edad y la situación económica {cite:p}`ccdr2025tools`.

**Variable de intensidad.** Temperatura máxima y mínima, o un índice que combine calor y humedad. CCDR-tools lista dos: la temperatura de globo y bulbo húmedo (WBGT), que considera la carga de trabajo y el efecto sobre la salud, y el Índice Universal de Clima Térmico (UTCI), más físico y que también cubre el estrés por frío {cite:p}`ccdr2025tools`.

### Calor en ciudades tropicales

Como criterio de método, en una ciudad tropical se debe distinguir entre ola de calor (anomalía respecto del clima local) y calor persistente propio del clima. La hoja de vigilancia muestra interés en Colombia por el calor extremo urbano y por sus efectos en salud; se ve en los dos estudios de abajo.

### Definición según los HIPs de UNDRR

Los perfiles de información de amenazas ([](../01_conceptos/16_hips_undrr.md)) que corresponden a este capítulo son:

| Código | Perfil (clúster) | Definición (traducción propia) |
|---|---|---|
| MH0501 | Ola de calor (meteorológico e hidrológico, temperatura) | Período marcado e inusual de tiempo caluroso sobre una región, que persiste al menos dos o tres días y noches consecutivos durante la época caliente del año según las condiciones climatológicas locales, con condiciones térmicas registradas por encima de umbrales dados (OMM y OMS, 2015). |

Fuente: {cite:p}`undrr2025hips`.

**Qué se incluye y por qué.**

- **Se incluye.** La definición deja los umbrales a la climatología local, lo que respalda el criterio del capítulo: para una ciudad colombiana el umbral debe fijarse con datos locales y no copiarse de Europa.
- **Distinguir ola de calor y calor persistente.** El perfil habla de un período «inusual» según el clima local; es coherente con la distinción que hace el capítulo entre anomalía y clima cálido normal.
- **No se incluye** la ola de calor marina (MH0708, IPCC 2019: temperatura superficial del mar extrema que persiste de días a meses), aunque puede ser relevante para los ecosistemas del Caribe; queda como tema por considerar.
- **Cascadas.** Los HIPs registran la ola de calor como causa de sequía e incendios {cite:p}`undrr2025hips`.

## 2. Amenaza

### Dos definiciones de CLIMAAX

CLIMAAX ofrece dos metodologías de amenaza, que difieren en datos de entrada, umbrales y algoritmo {cite:p}`climaax2025handbook`:

| Método | Definición de ola de calor | Notas |
|---|---|---|
| **EuroHEAT** | Periodo de al menos dos días con la temperatura aparente máxima y la mínima sobre el percentil 90 de la distribución mensual, con base en 1971–2000 | Recomendado, porque usa varios modelos regionales |
| **Xclim** | Umbrales absolutos de temperatura máxima y mínima y duración mínima definidos por el usuario (por ejemplo, 2 o 3 días) | Usa un solo modelo regional. Los umbrales suelen ser regionales y basados en impactos esperados en salud |

Ambos usan proyecciones EURO-CORDEX con resolución de 12 × 12 km, que **no tienen en cuenta la isla de calor urbana** y por eso no sirven para evaluar el riesgo dentro de las ciudades {cite:p}`climaax2025handbook`.

```{warning}
Para Colombia no hay un equivalente directo de EURO-CORDEX en las fuentes revisadas. Un análisis urbano necesita datos de reanálisis, estaciones del IDEAM o satelitales, con umbrales definidos localmente. El método Xclim, con umbrales absolutos, es el más adaptable.
```

### Compuestos

El calor extremo se combina con sequía. En la cuenca del Orinoco, un estudio de extremos secos y cálidos compuestos analiza sus implicaciones para los incendios {cite:p}`arias2025compound`. Ver [](310_incendios.md).

## 3. Exposición

La exposición a calor se mide con la temperatura de superficie. En el flujo de riesgo local de CLIMAAX, la exposición proviene de la temperatura de superficie terrestre de Landsat 8 (30 × 30 m, periodo 2013–2021, cada 16 días), con la limitación de datos faltantes los días nublados {cite:p}`climaax2025handbook`. En una ciudad andina o amazónica, la nubosidad frecuente es un problema práctico para esta fuente.

## 4. Vulnerabilidad

La vulnerabilidad se representa con los grupos de población vulnerable: personas mayores de 65 años y menores de 5, con datos WorldPop de 100 × 100 m para 2020 {cite:p}`climaax2025handbook`. Es una aproximación gruesa; el censo del DANE permite una mejor para Colombia.

La evidencia en salud pública recogida en una revisión narrativa colombiana indica que las mujeres embarazadas tienen mayor riesgo de parto prematuro con altas temperaturas, y que adultos y niños pueden tener mayor riesgo de deshidratación. La revisión plantea la necesidad de un sistema de alerta temprana como política de salud pública {cite:p}`salazarceballos2025sistema`.

## 5. Riesgo

CLIMAAX usa una **matriz de riesgo 10 + 10** que cruza exposición (diez clases de temperatura de superficie) y vulnerabilidad (diez intervalos de población vulnerable). Las clases van de «muy bajo», con menos de 20–25 °C, a «muy alto», con más de 55 °C, y se pueden cambiar según el área {cite:p}`climaax2025handbook`. El nivel de riesgo es **relativo** al área elegida: solo refleja diferencias entre las zonas analizadas {cite:p}`climaax2025handbook`.

Un estudio de la hoja sobre el efecto de los bosques urbanos en la exposición al calor extremo en una ciudad tropical vulnerable (Bogotá, ID 644) queda por leer {cite:p}`giraldocharria2025urban`.

## 6. Clima

El calor es muy sensible al clima. CCDR-tools anticipa que el aumento de temperatura agravará las consecuencias del estrés térmico sobre la salud y la producción agrícola, en particular en países tropicales con baja capacidad de adaptación {cite:p}`ccdr2025tools`. Para la ola de calor de diciembre de 2022 en el sur de Sudamérica, un estudio de atribución concluye, por su título, que fue 60 veces más probable por el cambio climático {cite:p}`rivera20232022`; es una región distinta de Colombia, y se cita como ejemplo de método de atribución.

CLIMAAX compara los escenarios RCP4.5 y RCP8.5 para un periodo de referencia (1971–2000) y tres periodos futuros {cite:p}`climaax2025handbook`; ver [](../02_metodologia/23_escenarios_climaticos.md).

## 7. Datos y medidas

### Datos

| Fuente | Qué ofrece | Referencia |
|---|---|---|
| Landsat 8 | Temperatura de superficie a 30 m | {cite:p}`climaax2025handbook` |
| WorldPop | Población por grupos de edad | {cite:p}`climaax2025handbook` |
| Conjuntos de estrés por calor | WBGT, UTCI, índices de calor y humedad (resoluciones de 10 a 30 km) | {cite:p}`ccdr2025tools` |
| IDEAM, estaciones locales | Temperaturas diarias (falta documentar la disponibilidad y los umbrales) | pendiente |

### Incertidumbres

- Datos de proyección a 12 km sin efecto de isla de calor {cite:p}`climaax2025handbook`.
- La temperatura de superficie no es la temperatura del aire que determina el estrés fisiológico.
- Falta una definición de ola de calor para Colombia.

### Medidas según la Ley 1523

| Proceso | Medida | Referencia |
|---|---|---|
| Conocimiento | Sistema de alerta temprana para altas temperaturas y olas de calor | {cite:p}`salazarceballos2025sistema` |
| Reducción | Infraestructura verde urbana, como los bosques urbanos que reducen la exposición | {cite:p}`giraldocharria2025urban` (por título) |
| Manejo | Atención en salud a grupos vulnerables | {cite:p}`salazarceballos2025sistema` |

## Pendiente

- Leer {cite:p}`giraldocharria2025urban` y {cite:p}`rivera20232022` completos.
- Definir un umbral o percentil de ola de calor para las ciudades colombianas, con datos del IDEAM.
- Evaluar datos satelitales de temperatura de superficie con menos limitación por nubosidad.
- Buscar literatura de isla de calor urbana en Bogotá, Medellín, Cali y Barranquilla.
