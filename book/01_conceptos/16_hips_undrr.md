---
title: Perfiles de información de amenazas (HIPs) de UNDRR
short_title: HIPs de UNDRR
---

# Perfiles de información de amenazas (HIPs) de UNDRR

Hablar de «amenazas» sin una lista común produce análisis que no se pueden comparar. Los Perfiles de Información de Amenazas (*Hazard Information Profiles*, HIPs) del UNDRR y el Consejo Internacional de Ciencias (ISC) ofrecen esa lista y una definición para cada elemento. Este capítulo los presenta, explica cómo los usa el libro y dónde no calzan con el lenguaje colombiano.

## 1. Qué son los HIPs

Los HIPs son una descripción de cada uno de los **281 peligros** que cubre la edición de 2025, elaborada con un proceso consultivo de científicos y expertos de todo el mundo. Sirven como fuente estandarizada de información sobre amenazas para gobiernos, agencias, investigadores y educadores, y apoyan la evaluación del riesgo, la preparación, el registro de pérdidas y la planificación multisectorial {cite:p}`undrr2025hips`. Su origen es un grupo técnico que el UNDRR y el ISC crearon en 2019 para identificar el alcance completo de las amenazas relevantes para el Marco de Sendái, como base para que los países revisen sus políticas y su gestión operativa del riesgo {cite:p}`undrr2025hips`. Los HIPs se publican bajo la licencia CC BY 4.0 {cite:p}`undrr2025hips`.

Cada perfil tiene un código y una ficha. Del conjunto de datos que publica la API de PreventionWeb {cite:p}`undrr2025hips` se leen estos campos:

| Campo | Qué contiene |
|---|---|
| Código | Letras del tipo y número: `MH0101` (meteorológico e hidrológico), `GH` (geológico), `EN` (ambiental), `CH` (químico), `BI` (biológico), `TL` (tecnológico), `SO` (social), `ET` (extraterrestre) |
| Nombre y sinónimos | Término oficial y nombres alternativos (por ejemplo, «downburst»: «microburst», «macroburst») |
| Definición | Definición formal con su fuente (OMM, USGS, FAO, IPCC y otras) |
| Notas y contexto | Descripción ampliada, factores que lo impulsan y efectos |
| Relaciones | Qué otros peligros puede **causar** y por cuáles puede ser **causado** |
| Tipo y clúster | Dónde se clasifica |

## 2. Ocho tipos y sus clústeres

Los 281 peligros se agrupan en ocho tipos, y cada tipo se divide en clústeres, con la clasificación del informe técnico de revisión de definición y clasificación de amenazas de UNDRR e ISC {cite:p}`undrr2025hips`.

```{figure} figuras/hips_281_peligros.png
:label: fig-hips-281
:alt: Infografía circular con los ocho tipos de peligro de los HIPs 2025 y sus clústeres: meteorológico e hidrológico (8 clústeres, 53 peligros), social (4, 9), biológico (6, 83), ambiental (2, 24), tecnológico (6, 50), geológico (4, 25), químico (7, 27) y extraterrestre (2, 10), alrededor del número 281.
:width: 90%

Los 281 peligros de los HIPs 2025, por tipo y clúster. Infografía de UNDRR e ISC, tomada de PreventionWeb {cite:p}`undrr2025hips`. La página indica que los HIPs están bajo la licencia CC BY 4.0; la imagen se reproduce con esa atribución.
```

| Tipo | Clústeres | Peligros | Ejemplos de clústeres |
|---|---|---|---|
| Meteorológico e hidrológico | 8 | 53 | Convectivo, viento y presión, precipitación, temperatura, agua, marino |
| Geológico | 4 | 25 | Sísmico, volcánico, falla del terreno, otros peligros geológicos |
| Ambiental | 2 | 24 | Degradación ambiental |
| Biológico | 6 | 83 | Enfermedades infecciosas, enfermedades de interés en salud pública, enfermedades animales, de insectos y de plantas |
| Tecnológico | 6 | 50 | Ciberpeligros, fallas de construcción, fallas industriales, accidentes de transporte, residuos, radiación |
| Químico | 7 | 27 | Metales pesados, cancerígenos, gases tóxicos, contaminantes orgánicos persistentes |
| Social | 4 | 9 | Conflicto, posconflicto, conductual, económico |
| Extraterrestre | 2 | 10 | Clima espacial, extraterrestre |
| **Total** | **39** | **281** | |

Los conteos de peligros por tipo coinciden con los del conjunto de datos; los de clústeres son los de la página y la infografía.

## 3. Cómo se usan en este libro

1. **Lenguaje común.** Cada capítulo de la [parte 3](../03_amenazas/index.md) incluye una subsección «Definición según los HIPs», con el código, el clúster y la definición oficial (traducción propia) de los perfiles que corresponden a la amenaza, y con una decisión explícita de qué se incluye y qué no.
2. **Inventario de amenazas de una ciudad.** El paso 2 de la [lista de verificación](../05_sintesis/52_lista_ciudad.md) registra, para cada amenaza, los códigos HIP asociados. La plantilla de ciudad ya los trae.
3. **Cascadas y compuestos.** Las relaciones «causa» y «causado por» de los HIPs sirven para contrastar la matriz del capítulo de [cascadas](15_cascada_compuestos.md).
4. **Clasificar la literatura.** La tabla de artículos colombianos del proyecto está clasificada por clúster y amenaza específica de los HIPs.

### Los peligros del libro frente a los HIPs

El libro se apoya en **39 perfiles** de los 281: 20 meteorológicos e hidrológicos, 17 geológicos y 2 ambientales. Cada amenaza se asocia a estos códigos:

| Amenaza | Códigos HIP |
|---|---|
| Sismo | GH0101 Terremoto, GH0307 Licuefacción, GH0311 Ruptura superficial y fisuramiento |
| Volcanes | GH0201 Flujos y domos de lava, GH0202 Caída de ceniza y tefra, GH0203 Corrientes de densidad piroclástica, GH0204 Lahares, GH0205 Gases y aerosoles volcánicos |
| Tsunami | MH0705 Tsunami |
| Movimientos en masa | GH0300 Movimiento en masa gravitacional y sus subtipos GH0301 a GH0306 |
| Inundación | MH0600 Inundación, MH0601 costera, MH0602 estuarina, MH0603 repentina, MH0604 fluvial, MH0605 por aguas subterráneas, MH0606 por aguas superficiales, MH0607 por desborde de lago glaciar, MH0609 por encharcamiento (pluvial) |
| Erosión costera y nivel del mar | GH0405 Erosión y acreción costera, EN0402 Aumento del nivel del mar |
| Erosión fluvial | GH0404 Erosión y acreción fluvial |
| Sequía | MH0401 Sequía |
| Calor | MH0501 Ola de calor |
| Incendios forestales | EN0205 Incendios de vegetación |
| Ciclones tropicales | MH0309 Ciclón tropical, MH0703 Marejada de tormenta, MH0704 Marea de tormenta |
| Vendavales | MH0101 Ráfaga descendente, MH0302 Derecho, MH0103 Tormenta eléctrica, MH0304 Turbonada, MH0305 Tornado |

Los otros cuatro tipos (biológico, tecnológico, químico y social) y el extraterrestre quedan fuera del libro por ahora. Los pilotos de ciudad ya necesitaron dos que están ahí: el dengue (BI0207, y las enfermedades transmitidas por vectores, BI0108) y el incendio urbano, que en los HIPs se acerca a TL0305 «Fuego» (un peligro tecnológico de falla industrial, cuyo contexto menciona los incendios en áreas urbanas). Esa decisión de alcance está en el plan del proyecto (`plan/00_plan.md` del repositorio).

## 4. Las cascadas según los HIPs

Cada HIP lista los peligros que puede causar. Al cruzar esas listas entre las amenazas del libro se obtiene esta tabla de vínculos {cite:p}`undrr2025hips`:

| Amenaza | Puede causar, entre las del libro |
|---|---|
| Sismo | Movimientos en masa, tsunami; y, por perfiles secundarios, volcanes (gases) y erosión fluvial (licuefacción) |
| Volcanes | Movimientos en masa, incendios, erosión fluvial |
| Tsunami | Inundación, erosión costera |
| Movimientos en masa | Inundación, tsunami, lahares |
| Inundación | Movimientos en masa, lahares, erosión costera, erosión fluvial |
| Erosión costera | Movimientos en masa, erosión fluvial |
| Erosión fluvial | Movimientos en masa |
| Sequía | Incendios |
| Calor | Sequía, incendios |
| Incendios | Movimientos en masa |
| Ciclones tropicales | Inundación, erosión costera, vendavales (por los tornados) |
| Vendavales | Inundación, incendios |

La tabla coincide con la matriz del capítulo de cascadas ([](15_cascada_compuestos.md)) en los vínculos principales: sismo con movimientos en masa y tsunami, ciclón con inundación, sequía y calor con incendios, y erupción con lahares. Los HIPs añaden algunos que ese capítulo no tenía, como la inundación como causa de erosión de ríos y costas. Se tomó la relación tal como la publican los HIPs, y no se verificó cada una.

**Hacia la infraestructura.** Las 39 amenazas del libro aparecen en los HIPs como causa de 118 peligros distintos, y 33 de ellos son tecnológicos: colapso de edificios, falla de puentes, presas, túneles, interrupción de la energía, del agua y de las telecomunicaciones, incendios, derrames y accidentes de transporte {cite:p}`undrr2025hips`. La parte más grande de las cascadas, entonces, pasa por la infraestructura. Es lo que modela el [cuaderno de riesgos en cascada](../03_amenazas/314_riesgos_cascada.ipynb).

## 5. Dónde no calzan con el lenguaje colombiano

Las definiciones de los HIPs son globales y genéricas; la gestión del riesgo en Colombia usa términos propios. Los casos que el libro encontró:

| Término colombiano o del libro | Qué hay en los HIPs |
|---|---|
| Vendaval | **No hay un perfil.** El más cercano es la ráfaga descendente (MH0101), con la turbonada (MH0304) y el derecho (MH0302); el término colombiano es más amplio y no precisa el mecanismo ([](../03_amenazas/312_vendavales.md)) |
| Avenida torrencial, inundación lenta y rápida | Se reparten entre inundación repentina (MH0603), inundación fluvial (MH0604) y flujos de detritos (GH0303); la avenida torrencial tiene capítulo propio ([](../03_amenazas/316_avenidas_torrenciales.md)) |
| Marea de tormenta | Los HIPs distinguen la marejada (MH0703) de la marea de tormenta completa, que incluye la marea astronómica (MH0704) |
| Tsunami | Se clasifica entre los peligros meteorológicos e hidrológicos (marino), aunque el libro lo trata a partir de su origen geológico |
| Erosión costera y fluvial | Se clasifican como peligros geológicos |
| Incendios forestales | Se clasifican como peligro ambiental, y no meteorológico |
| Sequía | La definición es solo de precipitación; no cubre la sequía hidrológica, agrícola ni socioeconómica |

Además, los HIPs están solo en inglés (las traducciones del libro son propias), y en la API algunas definiciones largas llegan cortadas, como la de la tefra (GH0202).

## 6. La tabla de artículos y los HIPs

La tabla de 998 artículos colombianos del proyecto usa la clasificación por clúster y amenaza específica de los HIPs 2025. Su reparto muestra dónde está la literatura:

| Clúster en la tabla | Artículos |
|---|---|
| Geológico | 364 |
| Meteorología e hidrología | 185 |
| Ambiental | 67 |
| Tecnológico | 25 |
| Biológico | 10 |
| Social | 9 |
| Extraterrestre | 7 |
| Sin clasificar (por determinar o vacío) | 331 |

Entre las amenazas específicas, destacan terremoto (199), movimiento en masa (79), inundación (75), incendios forestales (45), erosión y acreción costera (33), ciclón tropical (27), inundación repentina (22), erosión y acreción fluvial (22) y sequía (21). Hay literatura colombiana de peligros tecnológicos por desastre natural (Natech, 16 artículos), que es un tema de cascada ([](15_cascada_compuestos.md)).

## Pendiente

- Leer el informe técnico de revisión de definición y clasificación de amenazas y la publicación de los HIPs 2025, de los que solo se consultó la página y el conjunto de datos.
- Confirmar la licencia de la infografía, que la página cubre con la declaración general de CC BY 4.0 de los HIPs.
- Revisar el campo de contexto y de factores de cada perfil usado, que no se incorporó aquí.
- Completar las 331 filas sin clasificar de la tabla de artículos con los HIPs.
- Decidir el alcance frente a los otros cuatro tipos (biológico, tecnológico, químico y social).
