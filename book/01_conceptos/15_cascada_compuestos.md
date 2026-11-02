---
title: Amenazas en cascada y riesgos compuestos
---

# Amenazas en cascada y riesgos compuestos

El capítulo anterior ([](14_riesgo_multiamenaza.md)) define las interacciones entre amenazas. Este las desarrolla en dos de sus formas más importantes: la **cascada**, en que un evento dispara a otros, y el **evento compuesto**, en que varios factores se combinan para producir un impacto mayor. Se apoya en los recursos citados en la página de conocimiento del riesgo del sitio web del autor, es decir, en las páginas de PreventionWeb sobre ambos conceptos {cite:p}`undrr2026cascading,undrr2026compound`, en el editorial de *npj Natural Hazards* sobre amenazas en cascada y desastres compuestos {cite:p}`alcantara2025cascading`, en las guías de Bevacqua et al. para estudiar eventos compuestos {cite:p}`bevacqua2021guidelines` y en una nota técnica australiana {cite:p}`arc2022compound`.

```{important}
**Alcance de las fuentes.** Los ejemplos son de Asia, Australia, Europa y Estados Unidos, salvo un estudio sudamericano que el editorial de *npj* menciona de pasada. Ninguna fuente de este capítulo analiza una ciudad colombiana. Las páginas de PreventionWeb son resúmenes divulgativos de otros estudios; las cifras que traen se atribuyen a ellas y no se verificaron en el estudio original. Todo lo que se propone para una ciudad colombiana es criterio de método.
```

## 1. Amenazas en cascada

### Definición

PreventionWeb define el riesgo en cascada, con base en UNDRR (2021), como el riesgo de que uno o varios eventos peligrosos precipiten riesgos y eventos posteriores. Los eventos en cascada ocurren cuando amenazas o fallas disparan cadenas de amenazas o impactos interrelacionados, y pueden dar lugar a desastres en cascada: eventos extremos cuyos impactos crecen con el tiempo y generan eventos secundarios y terciarios inesperados y de gran impacto {cite:p}`undrr2026cascading`. El ejemplo que da es un terremoto que dispara deslizamientos e inundaciones {cite:p}`undrr2026cascading`.

### Cadena de propagación

La página describe la cadena en cinco etapas {cite:p}`undrr2026cascading`:

| Etapa | Qué ocurre |
|---|---|
| 1. Evento detonante | La amenaza |
| 2. Impacto primario | Daño directo o interrupción |
| 3. Falla de sistemas interdependientes | La falla de un componente dispara fallas en otros sistemas conectados |
| 4. Crisis secundarias | Se propagan entre sectores |
| 5. Efectos sociales de largo plazo | Desplazamiento, deterioro de servicios, tensiones |

A diferencia de los demás capítulos, el daño ya no está solo en lo que la amenaza toca. Está en cómo la interrupción de un servicio afecta a otros. La página insiste en que la evaluación debe mirar si la infraestructura resiste la amenaza y, además, cómo se propagan las interrupciones por los sistemas conectados y afectan a las personas y los servicios esenciales {cite:p}`undrr2026cascading`.

### Ejemplos de las fuentes

| Ejemplo | Qué muestra | Fuente |
|---|---|---|
| El Niño, sequía prolongada e incendios en Indonesia | Una señal climática global dispara una sequía; la vegetación seca multiplica por cinco el área quemada; los incendios producen emergencias de calidad del aire, pérdidas económicas e interrupción del transporte | {cite:p}`undrr2026cascading` (resumen de un estudio) |
| Lluvias monzónicas y deslizamientos en un campamento de refugiados en Bangladesh | Más de 130 deslizamientos dañaron miles de refugios y forzaron reubicaciones; la poca tierra disponible limitó la respuesta | {cite:p}`undrr2026cascading` |
| Deslizamientos que ensanchan el cauce durante una crecida (Colorado) | Los deslizamientos aportan sedimento aguas abajo y amplían el cauce, lo que aumenta la vulnerabilidad a inundación | {cite:p}`alcantara2025cascading` |
| Falla de presas en Derna (Libia, 2023) | Un evento meteorológico se convirtió en desastre por décadas de abandono de la infraestructura y fragmentación política; las señales de deformación de las presas eran detectables con interferometría satelital antes del colapso | {cite:p}`alcantara2025cascading` |

El editorial agrega que los sistemas de montaña son puntos críticos de interacción entre amenazas por su topografía abrupta, su sensibilidad ecológica y su exposición climática {cite:p}`alcantara2025cascading`. Esa descripción coincide con la de las laderas andinas, y se conecta con [](../03_amenazas/304_mov_masa.md) y [](../03_amenazas/307_erosion_fluvial.md).

(limbe)=
### Un ejemplo con retroalimentación: las inundaciones de Limbe (Camerún)

En Limbe, ciudad costera de Camerún, la inundación no se explica solo por la lluvia intensa. Resulta de decisiones de uso del suelo, mal manejo de residuos, gobernanza débil y falta de infraestructura, con efectos en cascada sobre la educación, el transporte, la salud y la economía {cite:p}`awah2025mindmaps`. Para entenderla, la autora y su equipo usaron modelación participativa de dinámica de sistemas. Funcionarios, líderes comunitarios, grupos de jóvenes y comerciantes dibujaron los problemas en tarjetas, los conectaron con sus impactos en discusiones facilitadas, y el resultado se digitalizó en el programa Vensim y se validó con el grupo {cite:p}`awah2025mindmaps`. El estudio completo identifica las interdependencias y los bucles de retroalimentación del sistema de gestión del riesgo de inundación de la ciudad {cite:p}`awah2024participatory`.

Una de las cascadas que describe el blog tiene forma de bucle: los drenajes bloqueados causan inundación, que interrumpe el transporte, lo que afecta los negocios y produce pérdidas económicas, que a su vez reducen la inversión en infraestructura, y el ciclo continúa {cite:p}`awah2025mindmaps`. El diagrama de abajo es un dibujo propio de ese bucle, hecho a partir de la descripción del texto. No reproduce la figura original de CDKN («Economic sub-model of cascading effects of flooding in Limbe»), que está protegida por derechos de autor y puede verse en la [página de la historia](https://cdkn.org/story/flood-maps-mind-maps-participatory-systems-modelling-floods-limbe-cameroon).

```{mermaid}
flowchart TB
    A[Drenajes bloqueados<br/>e infraestructura insuficiente] --> B[Inundación]
    B --> C[Interrupción<br/>del transporte]
    C --> D[Negocios afectados]
    D --> E[Pérdidas económicas]
    E --> F[Menos inversión<br/>en infraestructura]
    F -. refuerza .-> A
```

*Bucle de refuerzo de la cascada económica de las inundaciones en Limbe. Elaboración propia a partir de {cite:t}`awah2025mindmaps`.*

Lo que enseña el ejemplo para este libro:

- **La cascada puede cerrarse sobre sí misma.** La cadena de cinco etapas de arriba termina en efectos de largo plazo, pero aquí el último efecto (menos inversión) agrava la causa inicial. Una evaluación que solo sigue la cadena hacia adelante no ve ese refuerzo.
- **Las causas no son solo físicas.** Los autores ponen cuatro áreas críticas: política y gobernanza, degradación ambiental, tensión económica e impactos sociales {cite:p}`awah2025mindmaps`. Es la misma idea del riesgo sistémico del editorial {cite:p}`alcantara2025cascading` y se conecta con la vulnerabilidad social ([](../04_vulnerabilidad/43_vulnerabilidad_social.md)).
- **El conocimiento local entra en el modelo.** El blog afirma que la experiencia vivida de la comunidad aportó información que complementa los datos {cite:p}`awah2025mindmaps`. Coincide con la recomendación de co-desarrollo con actores del capítulo anterior ([](14_riesgo_multiamenaza.md)).
- **Es un método cualitativo.** El resultado es un mapa de relaciones y bucles, no una pérdida anual esperada. Sirve para identificar qué cuantificar y dónde intervenir, y puede preceder al diagrama causal que piden Bevacqua et al. {cite:p}`bevacqua2021guidelines`. Es una lectura de este libro.

El caso es de África y de una inundación con drenaje urbano deficiente. Su relevancia para una ciudad colombiana depende de las condiciones locales y no se evaluó aquí.

### Riesgo sistémico

El editorial plantea que los desastres ya no están definidos por los extremos naturales sino por interacciones complejas entre varias amenazas, vulnerabilidades sociales arraigadas y fallas de gobernanza {cite:p}`alcantara2025cascading`. Los enfoques centrados en una sola amenaza resultan insuficientes, y los casos muestran que las consecuencias de un evento dependen de la vulnerabilidad social y de la capacidad de respuesta de comunidades e instituciones {cite:p}`alcantara2025cascading`. Para este libro la consecuencia es que la vulnerabilidad social y las capacidades ([](../04_vulnerabilidad/43_vulnerabilidad_social.md)) son parte del análisis de cascadas y no un anexo.

## 2. Eventos y riesgos compuestos

### Definición

Para el IPCC (2021), citado por PreventionWeb, el riesgo compuesto es el riesgo de que dos o más amenazas o impulsores de riesgo interactúen, de forma simultánea o consecutiva, y produzcan impactos mayores que la suma de los eventos individuales y dificulten la respuesta y la recuperación {cite:p}`undrr2026compound`. Los eventos compuestos pueden ocurrir al mismo tiempo, en sucesión cercana o a la vez en regiones distintas, y varios factores de estrés pueden superar la capacidad de afrontamiento de un sistema más rápido que un factor aislado {cite:p}`undrr2026compound`. La definición de Zscheischler et al. (2020), que retoman Bevacqua et al., es más amplia: combinaciones de impulsores o amenazas climáticas que contribuyen al riesgo social o ambiental {cite:p}`bevacqua2021guidelines`.

### Cuatro tipos

Bevacqua et al. adoptan la tipología de Zscheischler et al. (2020) {cite:p}`bevacqua2021guidelines`:

| Tipo | Qué es | Caso de estudio de las guías |
|---|---|---|
| **Precondicionado** | Una condición previa del clima o del tiempo aumenta el impacto que dispara una o más amenazas | Primaveras secas y soleadas que agravan el efecto de veranos cálidos y secos en la vegetación |
| **Multivariado** | Impulsores o amenazas concurrentes en un mismo lugar | Inundación costera compuesta en Perth (Australia): nivel del mar, oleaje y caudal de río |
| **Temporalmente compuesto** | Una sucesión de amenazas produce el impacto | Deslizamientos profundos en Portugal, causados por agrupaciones de lluvias moderadas |
| **Espacialmente compuesto** | Amenazas en varios lugares conectados producen un impacto agregado | Fallas simultáneas de cosechas en Francia y Alemania |

Las guías advierten que los límites entre tipos no son nítidos, por ejemplo, la inundación costera multivariada puede tener rasgos temporales si varias tormentas seguidas elevan el caudal del río {cite:p}`bevacqua2021guidelines`. Para una ciudad colombiana pesan sobre todo el precondicionado, el multivariado y el temporal, por la relación entre lluvias sucesivas, suelos saturados y movimientos en masa (criterio de método).

### Ejemplos de las fuentes

| Ejemplo | Tipo de combinación | Fuente |
|---|---|---|
| Queensland, 2019: calor extremo seguido de lluvias e inundación. Murieron unas 500.000 cabezas de ganado y las pérdidas superaron los USD 1.200 millones | Sucesión (ola de calor, inundación) | {cite:p}`undrr2026compound` |
| Japón, 2018: inundación seguida de una ola de calor, con vivienda, electricidad y agua potable afectadas | Sucesión (inundación, ola de calor) | {cite:p}`undrr2026compound` |
| Pakistán, 2022: ola de calor extrema y luego un monzón con casi el 190 % de la lluvia normal; las inundaciones afectaron a más de 33 millones de personas y las pérdidas superaron los USD 30.000 millones | Sucesión con precondición (suelos secos y deshielo acelerado) | {cite:p}`undrr2026compound` |
| Australia 2009: la ola de calor de Victoria con los incendios de Black Saturday y dos ciclones tropicales en otras regiones, conectados por ondas atmosféricas de gran escala | Compuesto en tiempo y espacio | {cite:p}`arc2022compound` |
| Europa, estudio de 2026: más del 70 % de las inundaciones fueron compuestas, con pérdidas promedio 2,8 veces mayores que las de inundaciones solas | Inundación con otras amenazas (sequía, calor, tormenta de viento) | {cite:p}`undrr2026compound` (resumen) |
| Louisiana: un evento comparable al huracán Ida (ciclón, apagón y ola de calor) pasaría de un periodo de retorno de unos 278 años en el clima histórico a 16,2 años en 2070–2100 bajo SSP5-8.5 | Ciclón, falla eléctrica y calor | {cite:p}`undrr2026compound` (resumen) |

Del editorial, un estudio de eventos compuestos de sequía, calor e incendios conecta América Central y el sureste de Sudamérica {cite:p}`alcantara2025cascading`, y otro encuentra que sequía y calor combinados redujeron casi a la mitad el rendimiento del maíz en Sinaloa, México {cite:p}`alcantara2025cascading`. Para el Orinoco, ver [](../03_amenazas/310_incendios.md).

### Cascada y compuesto: en qué se diferencian

Esta tabla es una síntesis de este libro, a partir de las definiciones anteriores:

| | Cascada | Compuesto |
|---|---|---|
| Relación entre amenazas | Una causa otra, o una falla causa otra | Se combinan; pueden no tener relación causal |
| Pregunta típica | ¿Qué sigue después del evento y por dónde se propaga? | ¿Qué combinación de factores produce el impacto extremo? |
| Herramienta principal | Mapa de detonantes y consecuencias, interdependencias de sistemas | Análisis de impulsores y dependencia estadística entre variables |
| Ejemplo | Sismo y deslizamientos | Sequía y calor, y luego incendios |

Una misma historia puede tener ambos rasgos: una sequía y una ola de calor compuestas pueden desencadenar incendios en cascada, que degradan la calidad del aire {cite:p}`alcantara2025cascading`.

## 3. Cómo se analiza un evento compuesto

Bevacqua et al. identifican cinco elementos físicos de un evento compuesto: los impactos, las amenazas que los causan, los impulsores de las amenazas, los modificadores de esos impulsores y el cambio climático, que puede influir en todos los anteriores {cite:p}`bevacqua2021guidelines`. Seis recomendaciones surgen de sus cuatro casos {cite:p}`bevacqua2021guidelines`:

1. **Diagramas causales** como lenguaje común entre disciplinas.
2. **Indicador de impacto simple** (por ejemplo, nivel del agua, ocurrencia de deslizamientos, rendimiento agregado de cultivos) y análisis hacia atrás para identificar las amenazas e impulsores relevantes. Si no hay datos de impacto, se necesita el conocimiento de expertos para definir indicadores aproximados.
3. **Composiciones de las condiciones climáticas** asociadas a los impactos, interpretadas con cuidado para no confundir correlación con causa.
4. **Modelos físicos** para estudiar la dinámica, en especial bajo cambio climático, donde la regresión simple puede fallar fuera del rango observado.
5. **Incertidumbre alta** en las probabilidades de ocurrencia y sus cambios; las narrativas de eventos (*storylines*), que ponen el énfasis en la plausibilidad antes que la probabilidad, son útiles para la preparación.
6. **Tipos no excluyentes**: los métodos de distintos tipos pueden combinarse.

### Umbrales: un ejemplo

La nota técnica australiana muestra cómo se definen los eventos compuestos en la práctica. Para viento y lluvia fijó el percentil 99 de cada una (ocurre unas tres veces al año); un evento caliente son tres días seguidos con temperatura diaria por encima del percentil 95; un evento seco es un mes con lluvia trimestral 1,3 desviaciones estándar por debajo de la media {cite:p}`arc2022compound`. Los umbrales son de Australia y los autores trabajan con extremos moderados para tener muestras suficientes. Para una ciudad colombiana los umbrales deben fijarse con datos locales ([](../03_amenazas/309_calor.md)).

### Precauciones sobre resolución

La nota aconseja no extraer información de un solo píxel del análisis: hay que sacar conclusiones de los patrones espaciales amplios. Además, los modelos climáticos tienen resolución que no permite simular sistemas de pequeña escala, como los que causan eventos de lluvia y viento {cite:p}`arc2022compound`. Es la misma limitación de escala que afecta el análisis urbano del calor.

## 4. Cómo se analiza una cascada

PreventionWeb propone {cite:p}`undrr2026cascading`:

- **Mapear detonantes y consecuencias** entre sistemas, para visualizar emergencias secundarias y cadenas complejas.
- **Modelar las interdependencias** entre sectores e identificar los vínculos críticos de la infraestructura.
- **Mapas de sistemas participativos**, que muestran bucles de retroalimentación como el de Limbe ([ejemplo de Limbe](#limbe)).
- **Pasar de modelos estáticos a dinámicos**, que combinan información meteorológica en tiempo real, imágenes satelitales, telemetría de la infraestructura y análisis de vulnerabilidad con inteligencia artificial. El ejemplo es modelar un corte de energía en tiempo real para anticipar efectos en hospitales, telecomunicaciones y agua.

El editorial coincide en que las herramientas tradicionales no captan las dinámicas en cascada, pide métodos nuevos (interferometría de radar, proyecciones de lluvia subhoraria, modelos de cultivos basados en procesos, análisis espaciotemporal de incendios) e indicadores que vayan más allá de las pérdidas económicas, para recoger impactos sociales en cascada, desplazamiento de largo plazo, alteración ecológica y fragilidad institucional {cite:p}`alcantara2025cascading`.

### Reducción

Reducir el riesgo en cascada exige gobernanza y coordinación entre sectores, con mecanismos de intercambio de datos en tiempo real y planificación conjunta entre gobiernos, operadores de infraestructura y servicios meteorológicos. Los servicios críticos, como los hospitales, deben prepararse para interrupciones prolongadas con energía de respaldo, reservas de combustible y planes de contingencia {cite:p}`undrr2026cascading`. Los sistemas de alerta temprana multiamenaza son centrales porque detectan amenazas de varias fuentes y comunican alertas coordinadas antes de que los impactos se propaguen {cite:p}`undrr2026cascading`.

Para los riesgos compuestos, la lista incluye infraestructura resiliente, soluciones basadas en la naturaleza, alerta temprana, planificación urbana informada por el riesgo y campañas de sensibilización; y atender vulnerabilidades de fondo, como el acceso a salud, la pobreza y la desigualdad {cite:p}`undrr2026compound`. El editorial añade el aspecto de gobernanza: fragmentación entre sectores, niveles administrativos y horizontes de tiempo, y la necesidad de gobernanza anticipatoria y de incluir a las comunidades expuestas {cite:p}`alcantara2025cascading`.

## 5. Qué hacer en una ciudad colombiana

Estas pautas son criterio de método de este libro, y combinan lo anterior con los capítulos de amenaza.

### Matriz de cascadas

Cada fila es un detonante; las columnas, lo que puede seguir según los capítulos de la parte 3. La tabla ordena lo que ya dicen esos capítulos y las fuentes de este; no es un inventario exhaustivo.

| Detonante | Amenazas o fallas que puede disparar | Capítulos |
|---|---|---|
| Sismo | Tsunami, movimientos en masa, licuefacción, incendios y fallas tecnológicas {cite:p}`alcantara2025cascading` | [](../03_amenazas/301_sismo.md), [](../03_amenazas/303_tsunami.md), [](../03_amenazas/304_mov_masa.md) |
| Lluvia intensa | Inundación, movimientos en masa, erosión fluvial, avenidas torrenciales | [](../03_amenazas/305_inundacion.md), [](../03_amenazas/304_mov_masa.md), [](../03_amenazas/307_erosion_fluvial.md) |
| Ciclón tropical | Viento, marea de tormenta, lluvia (inundación, deslizamientos) | [](../03_amenazas/311_ciclones.md), [](../03_amenazas/306_erosion_costera.md) |
| Erupción | Caída de ceniza, flujos piroclásticos, lahares | [](../03_amenazas/302_volcanes.md) |
| Sequía y calor | Incendios forestales, estrés hídrico | [](../03_amenazas/308_sequia.md), [](../03_amenazas/309_calor.md), [](../03_amenazas/310_incendios.md) |
| Tormenta convectiva severa | Vendaval, lluvia intensa y crecida súbita, interrupción del servicio eléctrico | [](../03_amenazas/312_vendavales.md), [](../03_amenazas/305_inundacion.md) |
| Incendio forestal | Pérdida de cobertura, que favorece deslizamientos y crecidas con lluvias posteriores | [](../03_amenazas/310_incendios.md), [](../03_amenazas/304_mov_masa.md) |
| Falla de una línea vital (energía, agua, comunicaciones, vías) | Interrupción de servicios en hospitales y respuesta de emergencia | [](../04_vulnerabilidad/41_exposicion.md) |

La fila de incendios y deslizamientos viene de un caso del Himalaya que describen Ferrario et al. ({cite:p}`ferrario2026harnessing`; ver [](14_riesgo_multiamenaza.md)) y de la lluvia sobre áreas quemadas que trata el editorial para el suroeste de Estados Unidos {cite:p}`alcantara2025cascading`. No se verificó para Colombia.

### Procedimiento

1. **Listar los detonantes** de la ciudad con la matriz y la historia de eventos.
2. **Dibujar el diagrama causal** de cada cadena relevante (Bevacqua, recomendación 1), con los actores locales si es posible, y marcar los bucles de retroalimentación.
3. **Elegir un indicador de impacto** por cadena (nivel del agua, número de edificaciones o personas afectadas, horas sin servicio).
4. **Mapear las líneas vitales** que cada cadena interrumpe y las poblaciones que dependen de ellas ([](../04_vulnerabilidad/41_exposicion.md)).
5. **Clasificar la combinación**: cascada, o compuesta (precondicionada, multivariada, temporal o espacial).
6. **Cuantificar lo que se pueda**: con escenarios por periodo de retorno ([](14_riesgo_multiamenaza.md)) si hay datos, o con una narrativa de evento (*storyline*) si la probabilidad es incierta.
7. **Declarar lo que quedó sin cuantificar** en la síntesis ([](../05_sintesis/51_sintesis_multiamenaza.md)).

## 6. Clima

Los eventos compuestos son sensibles al clima. La nota australiana proyecta que los eventos calientes y secos aumentan en todo el continente, con reducciones del periodo de retorno, mientras los eventos húmedos y ventosos cambian poco en el conjunto y con señales distintas entre el norte y el sur {cite:p}`arc2022compound`. PreventionWeb resume estudios según los cuales los eventos compuestos de inundación y ola de calor aumentarían en la mayoría de las cuencas del mundo, con los trópicos como foco global {cite:p}`undrr2026compound`; la cifra viene de un resumen y no se contrastó. Ver [](12_riesgo_climatico.md).

Un artículo sobre cambios del régimen de lluvias proyecta que cerca de 3.000 millones de personas (38 % de la población actual) enfrentarían condiciones significativamente más secas o más húmedas bajo un escenario intermedio, y 5.000 millones (66 %) bajo uno alto, hacia fines de siglo. Entre las regiones pobladas con acuerdo en una tendencia seca el artículo menciona América Central y el Caribe, el sur de Sudamérica, el este de Brasil y la Amazonía {cite:p}`trancoso2024wetterdrier`. No trata eventos compuestos ni nombra a Colombia. Como criterio de método, sirve como contexto de precondiciones (suelos más secos o más húmedos antes de un evento), pero no como resultado para una ciudad.

## Incertidumbre y límites

- Las probabilidades de eventos compuestos y su cambio son muy inciertas, por la incertidumbre de varios impulsores y de su interacción {cite:p}`bevacqua2021guidelines`.
- Los modelos globales no resuelven los procesos de pequeña escala que pueden dominar los extremos compuestos {cite:p}`arc2022compound`.
- La mayoría de los ejemplos cuantificados no es de Colombia ni de los trópicos andinos.
- Las páginas de PreventionWeb son divulgativas: las cifras que traen (pérdidas, periodos de retorno, porcentajes) deben contrastarse con los estudios que resumen.

## Pendiente

- Leer completo el artículo de Awah et al. (2024) sobre Limbe y su submodelo económico; solo se leyeron el resumen y el blog.
- Leer los estudios originales que PreventionWeb resume (Louisiana, Europa 2026, Pakistán, Indonesia) y los tres recursos que esa página recomienda.
- Leer el estudio de eventos compuestos de sequía, calor e incendios de Sudamérica que cita el editorial y buscar casos colombianos de cascadas urbanas (Mocoa, Armero, Providencia) con su literatura.
- Revisar la definición de riesgo en cascada del informe de UNDRR de 2021 (revisión de definición y clasificación de amenazas), que PreventionWeb cita y no se consultó.
- Documentar cómo CLIMADA representa eventos secuenciales y compuestos.
- Desarrollar una guía para dibujar el diagrama causal y la matriz de interdependencias de líneas vitales.
