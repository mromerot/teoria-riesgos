---
title: Evaluación de riesgos multiamenaza
---

# Evaluación de riesgos multiamenaza

Los capítulos de la [parte 3](../03_amenazas/index.md) analizan cada amenaza por separado. Este capítulo explica qué cambia cuando varias amenazas coinciden, se activan unas a otras o comparten vulnerabilidad. Se apoya en un método cuantitativo aplicado a los Alpes italianos {cite:p}`chen2016integrating` y en tres revisiones y análisis recientes sobre indicadores {cite:p}`white2025towards`, desigualdad {cite:p}`tiggeloven2026multihazard` y métodos basados en datos {cite:p}`ferrario2026harnessing`.

```{important}
**Alcance de las fuentes.** Ninguna de las cuatro trata a Colombia. El método de Chen et al. es de montaña europea y de lluvia extrema; las otras tres son revisiones o análisis globales. Todo lo que este capítulo propone para una ciudad colombiana está marcado como criterio de método. Los informes completos de las cuatro se leyeron; las citas internas que ellos hacen a otros trabajos se indican como tales y no se verificaron.
```

## 1. Por qué no basta una amenaza a la vez

Una evaluación de una sola amenaza puede ser incompleta porque no considera las interacciones ni los impactos de varias amenazas sobre un mismo lugar {cite:p}`white2025towards`. Además, las exposiciones y las vulnerabilidades pueden coincidir y cambiar en el tiempo {cite:p}`white2025towards`. Las revisiones señalan tres razones por las que la suma de análisis aislados subestima el riesgo {cite:p}`ferrario2026harnessing`:

1. Las amenazas que coinciden en el lugar y el tiempo pueden causar impactos mayores que la suma de los eventos por separado.
2. Una amenaza puede modificar la vulnerabilidad del sistema, como ocurre con amenazas consecutivas.
3. Los impactos se propagan entre escalas y sectores, más allá del área que el evento golpeó primero.

Estos puntos son la lectura que hacen Ferrario et al. de trabajos que citan; no son una cuantificación propia. La política internacional pide este cambio desde los años noventa: la Agenda 21, la Cumbre de Johannesburgo, el Marco de Hyogo y el Marco de Sendái piden enfoques multiamenaza para la reducción del riesgo {cite:p}`white2025towards`.

## 2. Terminología

La terminología es un problema reconocido: distintos grupos usan términos diferentes y eso dificulta el desarrollo y el uso de indicadores {cite:p}`white2025towards`. Este libro usa la clasificación de Zschau (2017), que adoptan Ferrario et al. {cite:p}`ferrario2026harnessing`:

| Término | Qué abarca | Interacciones entre amenazas | Interacciones en la vulnerabilidad |
|---|---|---|---|
| **Varias amenazas en capas** (*multi-layer single hazard*) | Más de una amenaza analizada por separado, con resultados superpuestos | No | No |
| **Multiamenaza** (*multi-hazard*) | Las amenazas y sus interacciones | Sí | No |
| **Riesgo multiamenaza** (*multi-hazard risk*) | El riesgo generado por varias amenazas y sus interrelaciones | Sí | No |
| **Multirriesgo** (*multi-risk*) | Lo anterior, más las interrelaciones a nivel de la vulnerabilidad | Sí | Sí |

Fuentes de la tabla: {cite:p}`ferrario2026harnessing,white2025towards,tiggeloven2026multihazard`. La definición de UNDRR (2017) que cita White et al. incluye dos ideas: seleccionar las varias amenazas importantes de un país y considerar los contextos en que pueden ocurrir de forma simultánea, en cascada o acumulativa {cite:p}`white2025towards`.

### Tipos de interacción

| Tipo | Definición | Ejemplo en el libro |
|---|---|---|
| **Disparo o cascada** | Una amenaza causa otra | Sismo y movimientos en masa ([](../03_amenazas/301_sismo.md)) |
| **Compuesta** | Una combinación de factores o amenazas contribuye al riesgo; pueden coincidir en espacio o tiempo sin estar relacionadas | Sequía y calor extremo ([](../03_amenazas/309_calor.md)) |
| **Amplificación** | Una amenaza aumenta (o reduce) la probabilidad o la magnitud de otra | Incendios que aumentan la probabilidad de deslizamientos {cite:p}`ferrario2026harnessing` |

Las definiciones vienen de White et al., que las toma de Ciurean et al. (2018) y Zscheischler et al. (2020) {cite:p}`white2025towards`. El capítulo siguiente ([](15_cascada_compuestos.md)) desarrolla las cascadas y los eventos compuestos. Los ejemplos de la última columna son del libro, salvo el de incendios y deslizamientos, que Ferrario et al. toman de un estudio del Himalaya {cite:p}`ferrario2026harnessing`.

## 3. Capas superpuestas o interacciones

White et al. revisaron 192 publicaciones. De los 174 artículos sobre amenazas, 49 % analizaba varias amenazas por separado y las presentaba superpuestas, y 51 % consideraba interacciones {cite:p}`white2025towards`. Entre las interacciones, las compuestas dominan (30 % de las 502 amenazas identificadas), mientras que el disparo y la amplificación suman 12 % {cite:p}`white2025towards`.

Este libro parte de la primera opción y deja de forma explícita lo que no cubre: las capas superpuestas son el punto de partida de la [síntesis](../05_sintesis/51_sintesis_multiamenaza.md), y las cascadas se revisan de forma cualitativa. Es una decisión de método de este libro.

## 4. Un procedimiento cuantitativo con datos escasos

Chen et al. proponen un procedimiento para valles de montaña con flujos de detritos, crecidas súbitas y crecidas de río, a escala media (1:25.000 a 1:50.000). Su punto de partida es que faltan datos de eventos pasados y las interacciones son complejas, por lo que hace falta un enfoque sistemático que combine métodos cuantitativos con supuestos y decisiones basados en expertos {cite:p}`chen2016integrating`.

### Pasos

1. **Inventarios.** Se recopilan los eventos históricos (inventario de flujos de detritos y de inundaciones, con imágenes y verificación en campo).
2. **Escenarios de amenaza.** Cada escenario es una lluvia con cierta frecuencia que dispara cierto número de eventos. Los periodos de retorno de la lluvia se estiman con la distribución de valores extremos generalizada (GEV) sobre las lluvias diarias máximas anuales {cite:p}`chen2016integrating`. Con una clasificación por expertos apoyada en las estadísticas, el estudio fijó cuatro escenarios: mayor (100 a 500 años), moderado (25 a 100), menor (10 a 25) y frecuente (1 a 10) {cite:p}`chen2016integrating`.
3. **Intensidad y probabilidad espacial.** Cada amenaza se modela por separado con su modelo (susceptibilidad estadística y trayectoria empírica para flujos de detritos; modelo hidrológico para crecidas súbitas; modelo hidráulico para crecidas de río). Como las zonas modeladas son mayores que las realmente afectadas, se calcula una **probabilidad espacial**: el área del inventario histórico del escenario dividida entre el área modelada {cite:p}`chen2016integrating`.
4. **Elementos en riesgo.** Edificaciones con valor de reposición por tipo de uso y personas dentro de ellas, distribuidas con un mapeo dasimétrico y con dos escenarios de ocupación, temporada turística y no turística {cite:p}`chen2016integrating`.
5. **Vulnerabilidad física.** Curvas de intensidad contra grado de pérdida (0 a 1) para edificaciones y personas, obtenidas de tres maneras: curvas de la literatura, curvas hechas por expertos y correlación entre daño e intensidad del evento de 2003 {cite:p}`chen2016integrating`.
6. **Pérdida y curva de riesgo.** Se aplica la ecuación de abajo, se grafica la pérdida contra la probabilidad anual del escenario (el inverso del periodo de retorno) y se integra el área bajo la curva para obtener la pérdida anual promedio {cite:p}`chen2016integrating`.

$$
L = P_s \cdot E \cdot V
$$

donde $P_s$ es la probabilidad espacial de que el elemento sea afectado en el escenario $k$, $E$ la cantidad de elementos expuestos (valor o personas) y $V$ su vulnerabilidad dada la intensidad {cite:p}`chen2016integrating`. Es la misma estructura del libro (amenaza × exposición × vulnerabilidad, [](11_marco_riesgo.md)), con la probabilidad espacial como corrección por la incertidumbre de la zona afectada.

### Reglas de combinación que el estudio aplica

- **Pérdida máxima y no suma por elemento.** Si un edificio puede ser afectado por más de una amenaza del mismo evento detonante, se toma la mayor pérdida y no la suma {cite:p}`chen2016integrating`. En el estudio se aplicó a flujos de detritos y crecidas súbitas, que comparten detonante y ubicación.
- **Número de escenarios.** Al menos tres escenarios, mejor seis o más con periodos de retorno distintos, para representar la curva {cite:p}`chen2016integrating`.
- **Curvas por amenaza.** El estudio presenta curvas y pérdidas anuales separadas para la crecida de río y para los flujos de detritos con crecidas súbitas (estos dos procesos se combinan con la regla del máximo) {cite:p}`chen2016integrating`.

Esta última regla ajusta lo que dice la [síntesis](../05_sintesis/51_sintesis_multiamenaza.md): la PAE de amenazas distintas se puede sumar si se evita contar dos veces el daño a un mismo elemento por un mismo evento.

### Incertidumbre con mínimo, medio y máximo

Cada factor ($P_s$, $E$, $V$, y los periodos de retorno) se expresa con valores mínimo, promedio y máximo, calculados o fijados por expertos cuando falta información. El resultado son tres curvas de riesgo por amenaza {cite:p}`chen2016integrating`. Los autores eligieron este enfoque en lugar de curvas de fragilidad con probabilidad de superar un estado de daño porque es más fácil de entender y de construir con juicio experto {cite:p}`chen2016integrating`. En una reunión con alcaldes, planificadores y protección civil de la zona, los asistentes indicaron que los resultados eran muy útiles para planificar la reducción del riesgo {cite:p}`chen2016integrating`.

### Qué mostraron los resultados

En el valle del río Fella, la pérdida anual promedio por flujos de detritos y crecidas súbitas varía entre 0,19 y 1,37 millones de euros (mínimo y máximo), y la de crecida de río entre 0,055 y 0,108 millones. Con los valores máximos, el riesgo económico de los primeros fue más de diez veces mayor {cite:p}`chen2016integrating`. La amplitud del rango ilustra la incertidumbre del método. El estudio atribuye las mayores incertidumbres a la definición de los escenarios y sus periodos de retorno, a la modelación de la intensidad y a las curvas de vulnerabilidad {cite:p}`chen2016integrating`.

### Validación y límites

Los autores reconocen que validar un análisis de riesgo es difícil; solo se puede comparar con eventos pasados parecidos. Con el evento de 2003, las pérdidas modeladas en edificaciones privadas (22,2 millones de euros para flujos y crecidas súbitas, 6,73 para el río) quedaron por debajo del daño reportado por la protección civil (59,1 millones), que incluía bienes comerciales e industriales no modelados {cite:p}`chen2016integrating`. Las muertes modeladas superaron las dos reportadas, entre otras razones porque no se consideraron las alertas ni las evacuaciones {cite:p}`chen2016integrating`. Además, los procesos se modelaron por separado, sin un modelo que analice sus interacciones a la vez {cite:p}`chen2016integrating`.

## 5. Indicadores multiamenaza

Un indicador es una característica observable y medible que simplifica la información para entender el estado de un fenómeno o seguirlo en el tiempo; un índice es una medida compuesta que combina varios indicadores en un valor {cite:p}`white2025towards`. Lo que encontró la revisión de White et al. {cite:p}`white2025towards`:

- Pocos estudios desarrollan indicadores de multiamenaza o multirriesgo de forma explícita. La mayoría son capas de amenazas individuales.
- El 88 % de las publicaciones se concentra en indicadores de amenaza, con predominio de las hidrometeorológicas, y solo el 20 % integra amenaza, vulnerabilidad y riesgo o impacto.
- En amenazas compuestas, los indicadores compuestos son los más usados (47 %), seguidos de los de probabilidad (19 %), frecuencia (15 %) e intensidad (4 %).
- No está claro hasta dónde se involucró a los actores en la creación de los indicadores.

Sus ocho recomendaciones, resumidas {cite:p}`white2025towards`:

| N.º | Recomendación |
|---|---|
| 1 | No limitarse a la amenaza: integrar vulnerabilidad, exposición, sensibilidad, capacidad de adaptación e impactos |
| 2 | Desarrollar indicadores de disparo, amplificación y cascada, no solo de amenazas compuestas |
| 3 | Que los indicadores compuestos se adapten al contexto regional, a las disparidades socioeconómicas y a las prioridades de los actores |
| 4 | Usar métodos mixtos: datos cuantitativos, información cualitativa y juicio de expertos |
| 5 | Construirlos con los actores de forma participativa |
| 6 | Usar términos claros y consistentes (multiamenaza, multirriesgo, indicador, índice) |
| 7 | Diseñarlos según la disponibilidad, resolución y calidad de los datos, que suelen ser escasos o desiguales |
| 8 | Alinearlos con los marcos internacionales (Sendái, ODS, alerta temprana) |

## 6. Vulnerabilidad social y desigualdad en la exposición

Tiggeloven et al. cruzan la coincidencia de amenazas con la población y con indicadores de vulnerabilidad socioeconómica. Su definición de multiamenaza es amplia: amenazas naturales que se solapan en espacio y tiempo, incluyendo disparo, eventos compuestos y desastres consecutivos {cite:p}`tiggeloven2026multihazard`.

**Método.** Superponen pares de amenazas del conjunto MYRIAD-HES (once tipos, 2004–2017) con la población de GHS-POP y con cinco indicadores: índice de desarrollo humano subnacional, índice de desarrollo de género, estabilidad política, acceso a atención de salud y grado de urbanización. Estratifican la población según la frecuencia de multiamenaza a la que ha estado expuesta (≥1, ≥5, ≥10 y ≥20 eventos) {cite:p}`tiggeloven2026multihazard`. Los indicadores se escogieron según un marco de 11 dimensiones de vulnerabilidad derivado del análisis de más de 400 trabajos; los datos permitieron cubrir 8 de las 11 {cite:p}`tiggeloven2026multihazard`.

**Resultados globales** {cite:p}`tiggeloven2026multihazard`:

- El 84 % de la población mundial estuvo expuesta al menos a un evento de multiamenaza en 2004–2017, el 34 % a más de cinco y el 8 % a más de veinte.
- Las poblaciones con menor desarrollo socioeconómico tienen mayor probabilidad de sufrir multiamenazas frecuentes.
- La intersección de cuatro indicadores (desarrollo humano, género, estabilidad política y acceso a salud) muestra una disparidad mediana de 7,4 %, que los autores leen como una desigualdad persistente.
- Para 2050, los patrones de exposición se mantienen casi iguales bajo los escenarios SSP2, SSP3 y SSP5, y lo que cambia según el escenario es la disparidad de vulnerabilidad.

**Sobre Sudamérica,** los autores señalan que la exposición a multiamenazas aumenta en las áreas con vulnerabilidades combinadas; lo contrario ocurre en América Central, Australia y Europa oriental {cite:p}`tiggeloven2026multihazard`. No hay un resultado específico para Colombia en el texto.

**Límites** que declaran los autores: los indicadores son estáticos y ocultan variaciones locales, se asume homogeneidad dentro de las unidades administrativas, y no sirven para análisis de causa y efecto; para estudios de caso recomiendan métodos mixtos {cite:p}`tiggeloven2026multihazard`. Las conclusiones valen para escala global y no para una ciudad.

## 7. Métodos basados en datos

Ferrario et al. revisaron 153 trabajos sobre aprendizaje automático y estadística multivariada para el riesgo climático multiamenaza {cite:p}`ferrario2026harnessing`. Lo relevante para este libro:

| Aspecto | Qué encontraron |
|---|---|
| Susceptibilidad multiamenaza | Es el enfoque más común: se entrena un modelo por amenaza con un inventario de huellas pasadas y se superponen los mapas. Cubre sobre todo inundaciones, deslizamientos, avalanchas e incendios |
| Interacciones | Las cópulas modelan la dependencia entre variables y la ocurrencia conjunta de extremos; el aprendizaje automático predice y encuentra los factores clave. Pocos estudios combinan ambos |
| Matriz de interacciones | Un estudio del Himalaya clasifica las interacciones en directas, mediadas por una condición ambiental y mediadas por infraestructura o procesos urbanos |
| Riesgo | La vulnerabilidad y la exposición se tratan casi siempre como capas fijas |

Las limitaciones que subrayan: la no estacionariedad del clima (los modelos entrenados con el pasado asumen relaciones estables), la distancia entre predecir la amenaza y predecir el impacto, la falta de marcos de cuantificación de incertidumbre de extremo a extremo, la validación con particiones espaciales insuficientes y la falta de catálogos de desastres con calidad homogénea {cite:p}`ferrario2026harnessing`.

## 8. Qué se adopta para una ciudad colombiana

Esta tabla es criterio de método de este libro, derivado de los apartados anteriores y de las limitaciones de datos de cada ciudad:

| Situación | Enfoque | Base |
|---|---|---|
| Hay amenazas probabilistas con exposición común (sismo, inundación, viento) | PAE por amenaza sobre un mismo inventario; evitar contar dos veces el daño a un elemento en el mismo evento | [](../05_sintesis/51_sintesis_multiamenaza.md), {cite:p}`chen2016integrating` |
| Amenazas con detonante común y pocos datos (lluvia, movimientos en masa, crecidas) | Escenarios por periodo de retorno de la lluvia, probabilidad espacial y mínimo, medio y máximo | {cite:p}`chen2016integrating` |
| Solo hay mapas de clases | Superposición y exposición a clases; declarar que es capa superpuesta | {cite:p}`white2025towards` |
| Se busca priorizar zonas por desigualdad | Cruce de la frecuencia de amenazas con indicadores de vulnerabilidad (DANE, DNP) | {cite:p}`tiggeloven2026multihazard`, [](../04_vulnerabilidad/43_vulnerabilidad_social.md) |
| Hay catálogos de eventos y datos abundantes | Modelos de susceptibilidad y cópulas, con validación espacial independiente | {cite:p}`ferrario2026harnessing` |

En todos los casos, el informe debe decir qué tipo de enfoque usó (capas, multiamenaza, multirriesgo) con los términos de la sección 2.

## Pendiente

- Leer los trabajos que estos cuatro artículos citan para las interacciones (por ejemplo, Gill y Malamud, Kappes et al., Zschau 2017) y contrastar las definiciones.
- Revisar el proyecto MYRIAD-EU y la plataforma de datos que White et al. mencionan, y su aplicabilidad a Colombia.
- Buscar literatura colombiana de multiamenaza y multirriesgo (hoja de vigilancia) y casos urbanos.
- Documentar cómo CLIMADA combina varias amenazas sobre una misma exposición.
- Añadir una guía para construir una matriz de interacciones entre las amenazas de la parte 3.
