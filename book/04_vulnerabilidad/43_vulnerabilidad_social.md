---
title: Vulnerabilidad social y capacidades
---

# Vulnerabilidad social y capacidades

El mismo evento produce pérdidas distintas según quién lo sufre y qué recursos tiene para responder. Este capítulo trata esa parte del riesgo, que las funciones de daño no capturan.

## 1. Qué es

La Ley 1523 define la vulnerabilidad como la susceptibilidad física, económica, social, ambiental o institucional que tiene una comunidad de ser afectada o de sufrir efectos adversos si ocurre un evento físico peligroso {cite:p}`ley1523,dnp2019imrd`. CCDR-tools cita la definición de UNDRR: las condiciones físicas, sociales, económicas y ambientales que aumentan la susceptibilidad de personas, comunidades, activos o sistemas, y distingue la capacidad de afrontamiento como el factor que ayuda a las personas a manejar el riesgo {cite:p}`ccdr2025tools`.

## 2. Marco del IPCC AR6: sensibilidad y capacidad de adaptación

CCDR-tools descompone la vulnerabilidad según el AR6 {cite:p}`ccdr2025tools`:

| Componente | Dimensiones |
|---|---|
| **Sensibilidad** | Biofísica (edad, salud previa), socioeconómica (pobreza, educación, acceso a servicios) e institucional (calidad de gobierno, acceso a infraestructura) |
| **Capacidad de adaptación** | Recursos económicos, tecnología e infraestructura (salud, alerta temprana), capacidad institucional y capital social |

La herramienta insiste en que los pesos de las dimensiones dependen de la amenaza, el contexto y el propósito, y deben justificarse; no hay un esquema universal {cite:p}`ccdr2025tools`.

## 3. Construir un índice

CCDR-tools propone una receta {cite:p}`ccdr2025tools`:

1. Elegir indicadores. Ejemplos: densidad de población y urbanización, asentamientos informales, edad (adultos mayores y niños), educación, igualdad de género y estabilidad de gobierno. También el Índice de Riqueza Relativa como proxy de pobreza.
2. Revisar redundancia entre indicadores. Una forma es el análisis de componentes principales, descartando los que tengan correlación mayor a 0,7.
3. Combinar con pesos: iguales, de correlación inversa, de expertos, o según el esquema sensibilidad–capacidad.

Los resultados son semicuantitativos (puntaje o ranking), no pérdidas.

CLIMAAX construyó un índice de vulnerabilidad social con datos globales (GlobE-SoVI), de 1 a 10, que combina edad y sexo, educación e ingreso, tiempo de viaje al centro de salud y tipo de asentamiento; se validó con muertes por inundación {cite:p}`climaax2025handbook`. Su cobertura se probó en Europa, y para Colombia hay que verificar su aplicabilidad.

## 4. Indicadores colombianos

### Atlas de Riesgo 2019: riesgo integral

El Atlas calcula un **riesgo integral** (RI) que combina el riesgo físico (RF), obtenido de la PAE normalizada, con un **factor de impacto** (F) que representa la fragilidad social y la falta de resiliencia. Usa 16 indicadores municipales, independientes de la amenaza {cite:p}`ungrd2019atlas`:

| Aspecto | Indicadores |
|---|---|
| Fragilidad social (8) | Necesidades básicas insatisfechas (miseria, vivienda, servicios, dependencia), hacinamiento crítico, mortalidad infantil, analfabetismo, desempleo |
| Falta de resiliencia (8) | Índice de desempeño integral, gestión del riesgo, ingresos tributarios y no tributarios per cápita, valor agregado per cápita, porcentaje de población en cabecera, densidad empresarial, centros de salud |

Una PAE mayor a 10 ‰ del valor expuesto se toma como riesgo físico máximo (1) {cite:p}`ungrd2019atlas`. El valor del factor de impacto aumenta el riesgo físico mediante la ecuación de Moncho, citada por el Atlas.

### Índice Municipal de Riesgo ajustado por capacidades (DNP)

El DNP separa dos componentes {cite:p}`dnp2019imrd`:

- **Riesgo de desastres** = exposición a la amenaza × vulnerabilidad, de 0 a 100, para exceso de lluvias (inundación lenta, avenidas torrenciales, movimientos en masa) y déficit de lluvias (sequía, incendios). La vulnerabilidad por exceso de lluvias se mide con el Índice de Pobreza Multidimensional (DANE, Censo 2018); para déficit incorpora la presión hídrica y la frontera agrícola.
- **Capacidades**, de 0 a 100, en tres dimensiones: financiera (ingresos tributarios y no tributarios por habitante), socioeconómica (población en cabecera, valor agregado por habitante, empresas por habitantes) y de gestión del riesgo (consejo municipal, plan municipal, estrategia de respuesta e inversión por habitante en conocimiento y reducción).

El índice ajustado combina ambos mediante una fórmula que depende de (100 − riesgo) y de las capacidades (la expresión exacta queda por verificar en la fuente), y clasifica los municipios en cinco grupos de capacidad, uno de ellos para las 13 ciudades principales {cite:p}`dnp2019imrd`.

```{important}
El índice municipal sirve para **comparar municipios**, no para estimar la pérdida de una ciudad. Para un análisis urbano, sus componentes (IPM, capacidades) son un buen punto de partida a escala municipal, pero hay que bajarlos a barrio o manzana con datos del censo.
```

## 5. Del índice al riesgo

Dos formas de usar la vulnerabilidad social, según la pregunta:

| Uso | Cómo | Fuente |
|---|---|---|
| **Mapa bivariado** | Cruzar exposición a la amenaza con el índice social para marcar zonas de riesgo y pobreza | {cite:p}`ccdr2025tools` |
| **Matriz de riesgo** | Cruzar clases de exposición con clases de vulnerabilidad, como la matriz 10 + 10 del calor | {cite:p}`climaax2025handbook` |
| **Factor de ajuste** | Multiplicar el riesgo físico por un factor de impacto | {cite:p}`ungrd2019atlas` |

Los resultados de la matriz y del bivariado son **relativos** al área estudiada; no se pueden comparar entre ciudades sin normalizar.

## 6. Vulnerabilidad y clima

La vulnerabilidad cambia con el desarrollo. CLIMAAX reconoce que casi no hay proyecciones de vulnerabilidad social a escala europea, y recurre a proyecciones de PIB per cápita y población rural alineadas con los SSP como proxy {cite:p}`climaax2025handbook,riahi2017ssp`. Para Colombia, la forma práctica es explicitar un supuesto: o la vulnerabilidad social se mantiene fija, o se proyecta con un escenario de desarrollo.

## Incertidumbres

- Los índices dependen de los indicadores y de los pesos escogidos; dos índices razonables pueden ordenar de forma distinta las mismas zonas.
- El censo tiene fecha; los cambios posteriores (migración, nuevos asentamientos) no aparecen.
- La resolución municipal de los índices nacionales oculta las diferencias dentro de la ciudad, que suelen ser las decisivas.

## Pendiente

- Leer completo el documento del DNP (metodología de normalización y agregación) y verificar la fórmula de ajuste.
- Verificar la ecuación de Moncho en la fuente primaria que cita el Atlas.
- Evaluar los índices de vulnerabilidad social en la literatura colombiana (hoja de vigilancia) y su resolución urbana.
- Definir los indicadores mínimos por barrio disponibles en el censo del DANE para la ciudad nueva.
