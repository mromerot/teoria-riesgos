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

## Pendiente

- Leer completos {cite:p}`rey2021hurricane`, {cite:p}`osorio2024reconstructing` y {cite:p}`velasquezcalderon2027assessing`.
- La cifra de 80 % de muertes por huracanes donde tocan tierra está en el Atlas tal como se cita en el capítulo; falta hallar la fuente primaria que el Atlas no indica en ese pasaje.
- Añadir las funciones de vulnerabilidad al viento y los parámetros de la marea de tormenta del Atlas.
- Usar los radios de viento de IBTrACS (R34, R50, R64) para estimar la huella de viento de cada sistema sobre los sitios, y no solo la distancia.
- Extender el conteo a todo el periodo desde 1851 con las salvedades de calidad de datos, y a la costa del Pacífico si se agrega esa cuenca.
- Documentar la inclusión de ciclones en CLIMADA (módulo de ciclones tropicales) después de revisar su documentación.
