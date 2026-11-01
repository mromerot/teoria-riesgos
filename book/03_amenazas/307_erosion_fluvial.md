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

## Pendiente

- Leer completos {cite:p}`cardenas2024prioritizing`, {cite:p}`manzolli2022recent`, {cite:p}`rivillasospina2025numerical` y {cite:p}`villadiegorojas2023fluvial`.
- Buscar metodologías de referencia (por ejemplo, de la Cormagdalena o el SGC) y guías de estudios de socavación para puentes.
- Definir cómo se integran la migración lateral y la inundación en una sola zonificación.
- Conectar con el capítulo de Leticia: el tramo Nazaret–Leticia es la aplicación directa.
