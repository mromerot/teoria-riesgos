---
title: Funciones de daño
---

# Funciones de daño

Una función de daño convierte la intensidad de una amenaza en pérdida para un tipo de elemento expuesto. Es el puente entre el mapa de amenaza y la cifra de impacto.

## 1. Qué es

CCDR-tools distingue dos componentes de la vulnerabilidad. Los **modelos de impacto** relacionan la intensidad de la amenaza con el daño que sufre una categoría expuesta; cuando describen daño físico se llaman funciones de fragilidad. Pueden ser cuantitativos (absolutos, en dinero, o relativos, como proporción del valor total) o cualitativos (clases nominales). Las **condiciones socioeconómicas** describen la susceptibilidad diferencial y se tratan en [](43_vulnerabilidad_social.md) {cite:p}`ccdr2025tools`.

El Atlas añade que cada elemento expuesto tiene su propia función por amenaza, y que estas funciones no solo dan una representación cuantitativa y continua de la pérdida, sino también una representación probabilista {cite:p}`ungrd2019atlas`.

## 2. Forma de la función

Dos reglas del Atlas fijan el esquema general {cite:p}`ungrd2019atlas`:

1. **Variable de entrada.** Es la intensidad que mejor se correlaciona con el daño: aceleración o deriva para sismo, profundidad o velocidad del agua para inundación, velocidad del viento para ciclones, espesor de ceniza para erupciones, altura de la ola para tsunami y marea de tormenta.
2. **Variable de salida aleatoria.** El daño para una intensidad dada no es un valor único. Se describe con el valor esperado y la varianza de la **relación de daño medio** (pérdida relativa al valor del elemento). Con intensidad cercana a cero no hay daño, y la variabilidad tiende a ser mayor hacia la mitad de la pérdida, aunque no siempre {cite:p}`ungrd2019atlas`.

En fórmula, para un elemento con valor $V$ y una intensidad $I$ del evento:

$$
L = V \cdot \mathrm{RDM}(I), \qquad \mathrm{RDM}(I)\in[0,1]
$$

donde $\mathrm{RDM}$ es la relación de daño medio. La pérdida del evento se suma sobre todos los elementos; la PAE se obtiene luego como se explica en [](../02_metodologia/22_probabilista_pae.md).

```{note}
El Atlas define las curvas por tipo estructural. Cuando un análisis solo tiene la categoría «vivienda», pierde la parte de la variabilidad que viene del tipo constructivo, y esa pérdida de información debe declararse como incertidumbre.
```

## 3. Funciones por amenaza

| Amenaza | Intensidad de entrada | Observación | Capítulo |
|---|---|---|---|
| Sismo | Aceleración espectral o deriva, según el método | Depende del tipo estructural y de los efectos de sitio {cite:p}`ungrd2019atlas` | [](../03_amenazas/301_sismo.md) |
| Inundación | Profundidad (y velocidad) del agua | Curvas por tipo de edificio y uso del suelo {cite:p}`climaax2025handbook` | [](../03_amenazas/305_inundacion.md) |
| Viento | Ráfaga de 3 segundos | CLIMAAX usa curvas por clase de activo {cite:p}`climaax2025handbook` | [](../03_amenazas/311_ciclones.md) |
| Ceniza volcánica | Espesor de ceniza | Función propia {cite:p}`ungrd2019atlas` | [](../03_amenazas/302_volcanes.md) |
| Tsunami y marea de tormenta | Altura de la ola o del agua | Función propia {cite:p}`ungrd2019atlas` | [](../03_amenazas/303_tsunami.md) |
| Movimientos en masa | Clase de amenaza, o factor de seguridad | Con frecuencia binaria o por clase | [](../03_amenazas/304_mov_masa.md) |
| Erosión (costera, fluvial) | Posición de la franja | Daño binario: el elemento está o no en la franja que se pierde | [](../03_amenazas/306_erosion_costera.md) |
| Calor | Temperatura de superficie, índices de estrés térmico | Clasificación de impacto, no curva continua {cite:p}`climaax2025handbook` | [](../03_amenazas/309_calor.md) |

Las filas de movimientos en masa y erosión resumen el criterio de método de los capítulos respectivos, donde se explica por qué no hay una curva estándar.

## 4. Fuentes de funciones

CLIMAAX lista funciones globales de daño y mortalidad {cite:p}`climaax2025handbook`:

| Función | Amenaza | Categoría | Tipo | Escala |
|---|---|---|---|---|
| Daño por inundación de Huizinga et al. (2017) | Inundación | Área construida | Función de daño | Regional |
| Mortalidad por inundación de Jonkman y Vrijling (2008) | Inundación | Población | Función de mortalidad | Global |
| Clasificación de índices de estrés térmico de Zare et al. (2019) | Calor | Población | Clasificación de impacto | Global |

Para edificaciones, CLIMAAX remite a los materiales de la base PAGER y a un estudio que reunió más de 1250 curvas de vulnerabilidad de infraestructura crítica para inundación, sismo, viento y deslizamientos (Nirandjan et al., 2024) {cite:p}`climaax2025handbook`. En CLIMADA, las funciones se agrupan en un conjunto de funciones de impacto (`ImpactFuncSet`), y cada punto de exposición apunta a la que le corresponde {cite:p}`climada2025docs`.

En CCDR-tools, el análisis de inundación ofrece dos enfoques: por **clases** de amenaza con umbrales, o por **función**, caso en que se escoge la mejor función de impacto para el país y la categoría de exposición {cite:p}`ccdr2025tools`.

### Fuentes colombianas

El Atlas documenta funciones por tipo estructural para las amenazas de su evaluación {cite:p}`ungrd2019atlas`. La hoja de vigilancia incluye estudios de vulnerabilidad física en Colombia, entre ellos los determinantes de la vulnerabilidad física de estructuras expuestas a inundación {cite:p}`hernandez2026physvuln` y, para sismo, los sesgos de los métodos de derivación de vulnerabilidad al evaluar el riesgo de varias ciudades con distinto nivel de amenaza {cite:p}`hoyos2022multicity`. Se citan por título; deben leerse para su método.

## 5. Calibrar y adaptar

CCDR-tools resume una regla práctica: los modelos locales sirven mejor para escalas locales, como la ciudad, y los globales para escalas nacional o subnacional. En países en desarrollo, un modelo global suele ser la única fuente, y debe aplicarse con cautela y reconociendo sus límites {cite:p}`ccdr2025tools`. CLIMAAX coincide: las curvas de daño se basan a menudo en datos locales agregados a escala global {cite:p}`climaax2025handbook`.

Para una ciudad colombiana, el orden de preferencia es:

1. Función derivada de daños observados en la propia ciudad o en una ciudad comparable.
2. Función nacional por tipo estructural, como las del Atlas.
3. Función global, con una advertencia explícita y un análisis de sensibilidad.

Este orden es criterio de método.

## Incertidumbres

- La función tiene incertidumbre propia (varianza), además de la de la amenaza. La incertidumbre epistémica de las curvas y de los modelos de amenaza puede alterar de forma apreciable la pérdida sísmica estimada {cite:p}`marulanda2021epistemic`.
- Las curvas globales de inundación se calibran con datos que pueden no representar la construcción local {cite:p}`climaax2025handbook`.
- Los daños por varios peligros en secuencia (sismo seguido de lluvia, por ejemplo) no se capturan con funciones independientes por amenaza.

## Pendiente

- Leer completos {cite:p}`hernandez2026physvuln` y {cite:p}`hoyos2022multicity`.
- Documentar el catálogo de tipos estructurales de la NSR-10 y su correspondencia con las funciones del Atlas.
- Añadir la forma de la `ImpactFunc` de CLIMADA (intensidad, relación media de daño, fracción de activos afectados) después de revisar su tutorial.
- Reunir funciones de daño para sequía agrícola e incendios, que no se trataron aquí.
