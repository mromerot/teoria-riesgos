---
title: Sismos
---

# Sismos

:::{image} ../../estilo/ilustraciones/sismo.svg
:alt: Casas en el borde de una falla, con ondas sísmicas
:class: ilustracion
:width: 100%
:::

Este capítulo sigue el molde de siete puntos ([](_molde.md)). A diferencia de la inundación, el sismo es una amenaza geofísica: no depende del clima y su evaluación descansa sobre la ingeniería sísmica y no sobre la hidrología. Por eso este capítulo usa más el Atlas de Riesgo de Colombia y la literatura nacional que los marcos CLIMAAX y CCDR-tools, que se centran en amenazas hidrometeorológicas {cite:p}`ccdr2025tools`.

## 1. Fenómeno

Los sismos son movimientos del suelo producidos por una liberación repentina de energía. Las fuerzas tectónicas y convectivas del interior de la Tierra acumulan esfuerzos de forma gradual en el contacto entre placas o en fallas de la corteza. Cuando se alcanza la resistencia de la roca, la energía se libera como ondas que se propagan en todas direcciones y hacen vibrar el terreno {cite:p}`ungrd2019atlas`.

Las **ondas de cuerpo** (P, de compresión, y S, de corte) son las responsables de las mayores afectaciones sobre lo construido. Las **ondas de superficie** (Love y Rayleigh) producen movimientos horizontales de corte y movimientos elípticos verticales en la superficie {cite:p}`ungrd2019atlas`. La intensidad se atenúa con la distancia a la fuente porque las ondas pierden energía al viajar, de modo que aceleración, velocidad y desplazamiento del terreno son distintos en cada punto {cite:p}`ungrd2019atlas`.

### Marco tectónico de Colombia

Colombia se ubica en la convergencia de tres placas: Nazca, Caribe y Suramérica. Su movimiento relativo originó el relieve y la estructura de las cordilleras, y la convergencia entre Nazca y Suramérica también se absorbe en grandes sistemas de fallas intracontinentales, responsables de la sismicidad superficial {cite:p}`ungrd2019atlas`. Entre los sistemas de fallas más destacados están el de Romeral y el del Piedemonte Llanero, que se extienden desde Ecuador hasta el norte del país {cite:p}`ungrd2019atlas`.

Hay además fallas con poco peso en la sismicidad nacional pero muy importantes a escala local, que deben entrar en los estudios de microzonificación {cite:p}`ungrd2019atlas`.

### Variable de intensidad

La amenaza se expresa con parámetros de movimiento fuerte: aceleración máxima del terreno (PGA), velocidad (PGV), desplazamiento (PGD) y ordenadas del espectro de respuesta. El PGA es el parámetro más empleado {cite:p}`ungrd2019atlas`. Para amenazas secundarias, como la licuefacción, se usan además variables geotécnicas (ver el punto 2).

```{note}
Zonas de amenaza sísmica en la norma NSR-10, según la aceleración pico efectiva (Aa): baja, hasta 0,10 g; intermedia, entre 0,10 g y 0,20 g; alta, mayor que 0,20 g. Según el estudio incorporado en la NSR-10, 553 cabeceras municipales (cerca del 39,7 % de la población) están en zona alta, 431 (47,3 %) en zona intermedia y 139 (13 %) en zona baja {cite:p}`ungrd2019atlas`.
```

### Definición según los HIPs de UNDRR

Los perfiles de información de amenazas ([](../01_conceptos/16_hips_undrr.md)) que corresponden a este capítulo son:

| Código | Perfil (clúster) | Definición (traducción propia) |
|---|---|---|
| GH0101 | Terremoto (geológico, sísmico) | Término que describe el deslizamiento repentino de una falla y la sacudida del suelo que produce la energía sísmica radiada durante ese evento. El deslizamiento puede deberse a cambios de esfuerzo en la Tierra o a actividad volcánica o magmática (USGS). |
| GH0307 | Licuefacción (geológico, falla del terreno) | Pérdida de resistencia de sedimentos sueltos, saturados o casi saturados, en o cerca de la superficie, por sacudidas fuertes como las de un sismo, por cargas cíclicas o vibraciones, o por exceso de presión de poros (AGI; USGS). |
| GH0311 | Ruptura superficial y fisuramiento (geológico, otros) | Desplazamientos localizados del terreno por esfuerzos de tensión, compresión y corte, sobre todo en sedimentos no consolidados; la ruptura superficial es la prolongación hacia arriba del deslizamiento de la falla en profundidad (Arizona Geological Survey; USGS). |

Fuente: {cite:p}`undrr2025hips`.

**Qué se incluye y por qué.**

- **Terremoto (GH0101): se incluye** como definición de referencia. Coincide con el enfoque del capítulo: un evento de la fuente (la falla) y su efecto (la sacudida del terreno).
- **Licuefacción (GH0307): se incluye.** Los HIPs la tratan como un peligro propio, no como parte del terremoto; el capítulo la trata como amenaza secundaria del sismo (sección «Amenazas secundarias»).
- **Ruptura superficial (GH0311): solo se menciona.** Importa donde una traza de falla activa cruza la ciudad; el capítulo no la desarrolla.
- **Cascadas.** Los HIPs registran el terremoto como causa de movimientos en masa, licuefacción, tsunami, incendios y fallas de edificios, puentes, presas, energía y agua {cite:p}`undrr2025hips`; ver [](../01_conceptos/16_hips_undrr.md) y [](../01_conceptos/15_cascada_compuestos.md).

## 2. Amenaza

### Por qué probabilista

Los terremotos pequeños (Mw ≤ 3,5) son mucho más frecuentes que los grandes (Mw ≥ 7,5), pero no es posible estimar cuándo, dónde ni con qué magnitud ocurrirá el próximo {cite:p}`ungrd2019atlas`. La alta incertidumbre motivó los análisis probabilistas de amenaza sísmica, que estiman a largo plazo las posibles localizaciones y frecuencias de los terremotos y propagan las incertidumbres {cite:p}`ungrd2019atlas`.

### Etapas del análisis probabilista

El método fue establecido por Cornell (1968) y Esteva (1970) y se resume en cuatro pasos, según Reiter (1990) {cite:p}`ungrd2019atlas`:

1. **Caracterizar las fuentes** que influyen en el sitio, por su geometría y por la distribución de probabilidad de inicio de la ruptura. Es usual modelarlas como planos y asignar probabilidad uniforme dentro de cada uno.
2. **Definir la sismicidad de cada fuente** a partir del catálogo sísmico y sus características sismotectónicas.
3. **Estimar el movimiento fuerte en el sitio** con funciones de atenuación que consideren su incertidumbre.
4. **Combinar las incertidumbres** de localización, tamaño y atenuación para obtener las tasas anuales de excedencia de los parámetros de movimiento fuerte.

La tasa de excedencia de una intensidad en un punto es la suma ponderada de las probabilidades de excedencia sobre todos los escenarios que definen la amenaza, con las frecuencias anuales de los terremotos como pesos. Esos escenarios deben ser estocásticos, mutuamente excluyentes y colectivamente exhaustivos {cite:p}`ungrd2019atlas`. En notación habitual, para una intensidad $a$ y fuentes $i$:

$$
\nu(a) \;=\; \sum_i \int_{M_0}^{M_u} \left|\frac{d\lambda_i(M)}{dM}\right| \, P\big(A>a \mid M, R_i\big)\, dM
$$

donde $\lambda_i(M)$ es la tasa de excedencia de magnitudes de la fuente $i$ y $P(A>a\mid M,R_i)$ la probabilidad de que la intensidad supere $a$ dado un sismo de magnitud $M$ a la distancia $R_i$. La forma de la ecuación es la clásica de Cornell y Esteva. El Atlas la describe con palabras y la sustenta en el teorema de la probabilidad total {cite:p}`ungrd2019atlas`.

### Sismicidad de las fuentes

Es común suponer que los terremotos de una fuente siguen un proceso de Poisson: el número de ocurrencias en una ventana de tiempo es independiente del de otra, es decir, el proceso no tiene memoria. La tasa de excedencia de magnitudes $\lambda(M)$ suele ser una versión modificada de la relación de Gutenberg y Richter, definida por tres parámetros que se estiman por máxima verosimilitud e información experta {cite:p}`ungrd2019atlas`:

| Parámetro | Significado |
|---|---|
| $\beta$ | Pendiente de la curva de recurrencia de magnitudes en la zona de magnitudes bajas |
| $M_u$ | Magnitud máxima, según la máxima longitud de ruptura posible y las características morfotectónicas |
| $\lambda_0$ | Número promedio de eventos por año con magnitud mayor que la umbral $M_0$ |

### Ejemplo con datos reales: sismicidad con el catálogo del USGS

El cuaderno [](317_sismicidad_colombia.ipynb) descarga el catálogo del USGS para Colombia y su área de influencia (2000–2024, magnitud de 3,0 o más) y muestra cómo se obtienen los insumos de esta sección. Está adaptado del cuaderno de la Subdirección para el Conocimiento del Riesgo de la UNGRD, con licencia CC BY 4.0 ([cuadernos-reproducibles-crc004](https://scr-ungrd.github.io/cuadernos-reproducibles-crc004/)). Con los datos descargados al ejecutarlo:

| Resultado | Valor |
|---|---|
| Eventos del catálogo | 4 201 |
| Sismos superficiales (hasta 70 km) / intermedios (70 a 300 km) | 2 290 / 1 910 |
| Magnitud de completitud ($M_c$, máximo de la curvatura) | 4,3 |
| $b$ por máxima verosimilitud (Aki-Utsu), sismos con $M \ge M_c$ | 1,06 ± 0,02 |
| $b$ por regresión sobre la curva acumulada | 0,93 |

Lo que enseña el ejemplo:

- **Completitud primero.** El ajuste de Gutenberg-Richter solo vale para magnitudes sobre $M_c$. Con un catálogo global la completitud es mayor que con el del SGC.
- **Dos estimadores de $b$ dan resultados distintos.** La regresión sobre la curva acumulada y la máxima verosimilitud difieren en 0,13; para una tasa de recurrencia se prefiere la segunda ($\beta = b \ln 10$, ver la tabla anterior).
- **La caja de búsqueda no es el país.** Incluye parte de Ecuador, Perú, Venezuela y Panamá, y los mayores sismos del listado (por ejemplo, el de Ecuador de 2016, de magnitud 7,8) no son colombianos. Para una ciudad hay que delimitar las fuentes que la afectan.
- **El catálogo USGS no reemplaza al del SGC** para un estudio de amenaza.

Los valores salen de una descarga del 2 de noviembre de 2026; el USGS puede revisar magnitudes, por lo que las cifras pueden variar un poco al repetirlo.

### Atenuación del movimiento fuerte

La intensidad se modela como variable aleatoria, usualmente con distribución lognormal cuyos momentos entrega la función de atenuación. Estas funciones dependen de la magnitud, de la distancia fuente–sitio y del mecanismo focal de ruptura {cite:p}`ungrd2019atlas`. Existen varias definiciones de distancia (epicentral, hipocentral, a la superficie de falla) y la elección debe corresponder al modelo adoptado {cite:p}`ungrd2019atlas`.

Para el norte de Suramérica hay modelos regionalizados. El modelo NoSAm para sismos corticales regionaliza el modelo global ASK14 de NGA-West2, corrige su desajuste con los datos observados para magnitudes moderadas y distancias intermedias y grandes, y añade atenuación para trayectorias que cruzan el arco volcánico {cite:p}`arteta2023nosam`.

### Amenaza sísmica nacional y local

La evaluación nacional que respalda la NSR-10 siguió cinco pasos: modelar las fuentes sismogénicas, asignar los eventos de los catálogos a cada fuente, caracterizar cada fuente con parámetros estadísticos, aplicar el modelo probabilista (software CRISIS V7.2) e interpretar los resultados para el diseño {cite:p}`ungrd2019atlas`. El Atlas muestra el mapa para un periodo de retorno de 475 años y un periodo estructural de 0,5 s, calculado **en roca firme**. Sirve como insumo para microzonificación y estudios de sitio, no como valor directo en el suelo de la ciudad {cite:p}`ungrd2019atlas`.

```{important}
A escala de ciudad, la amenaza en roca debe modificarse por el efecto del suelo. La microzonificación sísmica (caracterización geotécnica y geológica de cada sitio) es esencial para evaluar la respuesta de los suelos {cite:p}`ungrd2019atlas`. En 2019 había 16 ciudades con estudios de microzonificación: Popayán, Bogotá, Manizales, Cali, Medellín, Armenia, Pereira, Ibagué, el Valle de Aburrá, Bucaramanga (indicativo), Dosquebradas, Santa Rosa de Cabal, Palmira, Tuluá y Buga {cite:p}`ungrd2019atlas`.
```

### Amenazas secundarias

Un marco probabilista de amenaza de licuefacción para sitios con una capa superior no licuable sobre una capa licuable se aplicó al distrito de Aguablanca, en Cali, un área de susceptibilidad moderada a alta. Está pensado para regiones con pocos datos, porque aprovecha la información sísmica y geotécnica local {cite:p}`cruz2026liquefaction`. Los tsunamis de origen sísmico se tratan en [](303_tsunami.md).

## 3. Exposición

La exposición sísmica es el inventario de edificaciones e infraestructura con su ubicación, tipología estructural, material, altura, edad y uso. Es la parte que más varía entre ciudades.

Un ejemplo colombiano de construcción del modelo de exposición para una provincia combinó información de la Fundación del Modelo Global de Terremotos (GEM), encuestas y el censo nacional. Se asignaron curvas de fragilidad y vulnerabilidad a los tipos de edificios de la región {cite:p}`feliciano2023sabana`. Ese enfoque es replicable en otras ciudades cuando no hay catastro con tipología estructural.

La edad es un atributo clave: una parte significativa del inventario nacional data de antes del primer código de diseño sísmico obligatorio (Decreto 1400 de 1984) {cite:p}`feliciano2023sabana,ungrd2019atlas`.

## 4. Vulnerabilidad

La vulnerabilidad física sísmica se expresa con **funciones de fragilidad** (probabilidad de superar un estado de daño dada la intensidad) y **funciones de vulnerabilidad** (relación entre intensidad y pérdida esperada). El Atlas exige definir cada función por su valor esperado y su varianza, porque las pérdidas por una misma intensidad no son idénticas entre edificios similares {cite:p}`ungrd2019atlas`.

Hay estudios recientes de fragilidad y vulnerabilidad por tipología constructiva de Colombia: mampostería confinada {cite:p}`archbold2025confined` y mampostería no reforzada informal {cite:p}`reyes2025urm`. La elección entre derivar curvas propias o usar curvas genéricas afecta el resultado: un estudio metodológico sobre varias ciudades con distintos niveles de amenaza examina los sesgos de los métodos de derivación de la vulnerabilidad en lugares con poca información {cite:p}`hoyos2022multicity`.

Para la dimensión social de la vulnerabilidad se ofrecen índices demográficos aplicados a la pérdida directa (ver [](../04_vulnerabilidad/43_vulnerabilidad_social.md)). El estudio de la provincia de Sabana Centro incorporó uno {cite:p}`feliciano2023sabana`.

## 5. Riesgo

El flujo es el del Atlas: catálogo de eventos estocásticos, exposición, vulnerabilidad y cálculo de pérdidas. Sus resultados son la curva de excedencia de pérdidas, la PAE y la PMP ({cite:p}`ungrd2019atlas`; ver [](../02_metodologia/22_probabilista_pae.md)).

Dos modalidades se usan en la práctica:

| Modalidad | Uso | Ejemplo |
|---|---|---|
| **Probabilista** | PAE, PMP, seguros, priorización | Atlas de Riesgo {cite:p}`ungrd2019atlas` |
| **Escenarios** | Planes de emergencia, comunicación | Dieciocho escenarios de sismo de 475 años de periodo de retorno simulados con la herramienta OpenQuake para Sabana Centro {cite:p}`feliciano2023sabana` |

```{warning}
**Escala.** Las evaluaciones probabilistas a escala urbana muestran discrepancias importantes frente a las regionales o nacionales. Hacer análisis específicos para muchas ciudades puede no ser factible, por lo que se usan métodos más generales. Es necesario cuantificar los sesgos de cada método, tanto en la amenaza como en la vulnerabilidad {cite:p}`hoyos2022multicity`.
```

**Incertidumbre epistémica.** Combinar varios modelos de amenaza produce una incertidumbre epistémica que afecta las estimaciones probabilistas de riesgo sísmico {cite:p}`marulanda2021epistemic`.

## 6. Clima

Los sismos no son sensibles al clima. CCDR-tools lo plantea así: el cambio climático no afecta de forma significativa las amenazas geofísicas, que incluyen terremotos, tsunamis y actividad volcánica, aunque sí puede afectar las hidrometeorológicas {cite:p}`ccdr2025tools`.

Para la amenaza, el Atlas la considera estacionaria y sus órdenes de magnitud normalmente no cambian en la historia. Aun así, los estudios deben actualizarse periódicamente porque hay más registros de movimiento fuerte y mejores funciones de atenuación {cite:p}`ungrd2019atlas`.

Lo que sí cambia con el tiempo es la exposición y, en menor medida, la vulnerabilidad (crecimiento urbano, reforzamiento, nueva normativa). Por eso los escenarios de este capítulo son de **exposición**, no climáticos. Esto es un criterio de método de este libro, no una afirmación de las fuentes citadas.

## 7. Datos y medidas

### Datos disponibles

| Fuente | Qué ofrece | Referencia |
|---|---|---|
| Servicio Geológico Colombiano (SGC) | Catálogo e información histórica de sismos, mapas de sismicidad, Red Sismológica Nacional y Red Nacional de Acelerógrafos | {cite:p}`ungrd2019atlas` |
| Red Nacional | 53 estaciones sismológicas en zonas de alta actividad y 103 acelerógrafos (cifras de 2019) | {cite:p}`ungrd2019atlas` |
| OSSO | Sismómetros en Valle del Cauca, Cauca y Risaralda, con reportes diarios y mensuales | {cite:p}`ungrd2019atlas` |
| Redes urbanas | LISA (Bogotá) y SisMan LISA (Manizales), acelerógrafos interconectados | {cite:p}`ungrd2019atlas` |
| AIS | Mapas de amenaza, microzonificación y normas de la NSR | {cite:p}`ungrd2019atlas` |
| GEM | Modelos de exposición y fragilidad de edificaciones | {cite:p}`feliciano2023sabana` |

Las cifras de estaciones son de 2019 y deben actualizarse al aplicarlas.

### Normativa

El Código Colombiano de Construcciones Sismo Resistentes se expidió con el Decreto 1400 de 1984, después del terremoto de Popayán de 1983. Fue actualizado con el Decreto 33 de 1998 (NSR-98) y con el Decreto 926 de 2010 (NSR-10) {cite:p}`ungrd2019atlas`. La actualización NSR-22 se prepara en el comité AIS-300, que propone coeficientes sísmicos de diseño; sus autores critican el uso del movimiento fuerte orientado al riesgo (RTGM) por transmitir una falsa seguridad {cite:p}`bernal2021nsr22`.

```{note}
La NSR-22 es una propuesta que, según el capítulo citado, debía ser estudiada por la Comisión Asesora del Régimen de Construcciones Sismo Resistentes. Verificar su estado de adopción antes de citarla como norma vigente.
```

### Incertidumbres principales

- El mapa nacional es en roca. Sin microzonificación, el efecto de sitio queda sin cuantificar {cite:p}`ungrd2019atlas`.
- La tipología estructural del inventario suele estimarse, no medirse {cite:p}`feliciano2023sabana`.
- El método de derivación de la vulnerabilidad sesga los resultados a escala urbana {cite:p}`hoyos2022multicity`.
- Combinar varios modelos de amenaza añade incertidumbre epistémica {cite:p}`marulanda2021epistemic`.

### Medidas según la Ley 1523

| Proceso | Medida | Fuente |
|---|---|---|
| Conocimiento | Microzonificación sísmica, redes de acelerógrafos, escenarios de riesgo | {cite:p}`ungrd2019atlas,feliciano2023sabana` |
| Reducción: prevención | Normas de diseño y construcción sismo resistente, ordenamiento territorial según la amenaza | {cite:p}`ungrd2019atlas` |
| Reducción: mitigación | Reforzamiento de edificaciones existentes; planes de mitigación para infraestructura escolar | {cite:p}`ungrd2019atlas,fernandez2021escolar` |
| Manejo | Atención de emergencias apoyada en las redes de acelerógrafos | {cite:p}`ungrd2019atlas` |

## Síntesis de evidencia

```{note}
**Método.** Síntesis narrativa por tipo de evidencia (no un metaanálisis con efectos agrupados: los estudios usan diseños, escalas y variables que no se pueden combinar en un solo estimador). Se leyeron los resúmenes de los artículos de la hoja de vigilancia que están en la carpeta de PDFs; las cifras vienen de esos resúmenes y **faltan por verificar contra el texto completo**. De los 63 PDFs clasificados como sismo, aquí se usan los que aportan a amenaza, exposición, vulnerabilidad y riesgo de ciudad; los de ingeniería estructural de elementos, ensayos de laboratorio y control de estructuras no se usan.
```

| Bloque | Estudio | Diseño y lugar | Resultado relevante |
|---|---|---|---|
| Fuente sísmica | {cite:t}`chicanganamonton2022sismicidad` | Sismicidad y sismotectónica del Sistema de Fallas de Algeciras | Cuatro sismos históricos con M > 6,5 desde finales del siglo XVIII, uno de ellos el de 1967 (Mw 7,2) |
| Fuente sísmica | {cite:t}`salcedohurtado2021reevaluacion`; {cite:t}`di2021macroseismic` | Reevaluación macrosísmica del sismo de 1925 y de otros previos a la era digital | Los datos macrosísmicos permiten reubicar y redimensionar sismos históricos |
| Fuente sísmica | {cite:t}`munoz2020calibration`; {cite:t}`jarrin2022current` | Calibración de la magnitud local en cinco zonas; movimiento de la placa de Nazca con GPS | Mejoran el catálogo y el marco tectónico |
| Fuente sísmica | {cite:t}`garciaarias2026towards` | Aprendizaje automático para el Nido Sísmico de Bucaramanga | El nido es uno de los tres volúmenes con más sismicidad intermedia del mundo y cercano a centros urbanos |
| Movimiento del suelo | {cite:t}`arteta2023ground` | Modelo de movimiento del suelo para sismos corticales del norte de Suramérica | Los sismos corticales cercanos a ciudades contribuyen mucho a la amenaza; el sismo del Eje Cafetero (1999, Mw 6,2) causó daños del 1,9 % del PIB |
| Movimiento del suelo | {cite:t}`gomezgarcia2023crustal`; {cite:t}`londono2022seismic`; {cite:t}`celorio2025urban` | Espesor sismogénico cortical; atenuación en el Valle Medio del Magdalena; longitudes de atenuación urbanas | Insumos para modelos de atenuación y de efectos de ciudad |
| Efectos de sitio | {cite:t}`mercado2024performance` | Parámetros estimadores de efectos de sitio, norte de Suramérica | Compara estimadores simplificados de la amplificación local |
| Vulnerabilidad | {cite:t}`chavezgarcia2021vulnerability` | Informe de daños de Armenia (1999) frente al número de pisos y edad de la construcción, con dos evaluaciones previas (1993 y 2004) | El daño fue desproporcionado (aceleración pico de 580 gal) y se relaciona con la vulnerabilidad y con los efectos de sitio |
| Vulnerabilidad | {cite:t}`fernandez2022simplified` | Metodología simplificada por componentes para escuelas | Los daños en escuelas se deben también a diseño y construcción deficientes |
| Riesgo | {cite:t}`acevedo2020seismic` | Evaluación de riesgo sísmico y escenarios para edificaciones residenciales de Bogotá (8,0 millones), Medellín (2,5) y Cali (2,4), con metodología uniforme | Permite comparar las tres ciudades con los mismos modelos de amenaza, vulnerabilidad y exposición |
| Riesgo | {cite:t}`hoyos2022seismic`; {cite:t}`marulanda2021epistemicb` | Sesgos al derivar vulnerabilidad en varias ciudades; incertidumbre epistémica en riesgo sísmico | La derivación de vulnerabilidad se sesga según el nivel de amenaza; la incertidumbre epistémica es relevante en estimados probabilistas |
| Exposición y respuesta | {cite:t}`hurtado2026building`; {cite:t}`aroquipa2022seismic`; {cite:t}`ordaz2023review` | Predicción de colapso con aprendizaje automático; resiliencia de edificios; aceleraciones de diseño | Enlazan daño observado, resiliencia y normativa |
| Comunicación | {cite:t}`acevedo2025earthquake` | Iniciativa de transferencia de conocimiento de riesgo sísmico | Para que el riesgo sirva a la toma de decisiones, quien lo genera debe transferirlo a los usuarios finales |

**Lectura conjunta.**

- **El riesgo sísmico urbano se calcula con el mismo marco en las tres mayores ciudades** {cite:p}`acevedo2020seismic`; esto sirve de plantilla para otras ciudades, a costa de documentar las incertidumbres epistémicas {cite:p}`marulanda2021epistemicb` y los sesgos de vulnerabilidad {cite:p}`hoyos2022seismic`.
- **Fuentes corticales cercanas.** El caso del Eje Cafetero en 1999 y los sismos históricos de Algeciras y de 1925 muestran que no basta la subducción para la amenaza de una ciudad {cite:p}`arteta2023ground,chicanganamonton2022sismicidad,salcedohurtado2021reevaluacion`.
- **Efectos de sitio.** El daño de Armenia fue mayor que el que explicaba la fuente {cite:p}`chavezgarcia2021vulnerability`; el análisis debe incluir microzonificación o estimadores de amplificación {cite:p}`mercado2024performance`.
- **Falta de metadatos.** Dos estudios de la hoja (modelos de movimiento del suelo del norte de Suramérica y tipologías por aprendizaje profundo) tienen un DOI que no resuelve en Crossref y no se citan.

## Pendiente

- Leer los resultados completos de {cite:p}`hoyos2022multicity`, {cite:p}`marulanda2021epistemic`, {cite:p}`archbold2025confined`, {cite:p}`reyes2025urm` y {cite:p}`cruz2026liquefaction`. Hoy se citan por título o resumen. Del primero y el segundo no verifiqué si los casos son colombianos.
- Añadir las funciones de vulnerabilidad del Atlas con sus parámetros y las pérdidas anuales esperadas por sismo para ciudades de referencia.
- Buscar la cifra de población en zonas de amenaza sísmica intermedia y alta. El capítulo no la usa: la cifra de 87 % de mis notas no aparece en el texto extraído del Atlas, y la de 83 % del estudio de Sabana Centro no se verificó. No citar ninguna hasta hallar la fuente.
- Añadir el caso de Bogotá, Medellín y Cali (DOI 10.1177/8755293020942537) y la reevaluación de la serie 2021, capítulo 2, para infraestructura escolar.
- Documentar herramientas: OpenQuake (GEM) y CAPRA/CRISIS. Quedan por contrastar con su documentación.

## Bibliografía recomendada

Lista de los 194 registros de la hoja de vigilancia científica (pestaña `Vigilancia_CTeI`, columna `AMENAZA_ESPECIFICA` = «Terremoto (sismo)»; «Licuefacción»), en formato APA 7 con metadatos de Crossref. Son lecturas recomendadas: **no están verificadas contra el texto completo** ni se usan como evidencia hasta que se citen en el capítulo. Las entradas sin DOI carecen de autores en la hoja.

- A. Prieto, G. (2026). Diversidad sísmica de profundidad intermedia: Colombia, un laboratorio natural. *Revista de la Academia Colombiana de Ciencias Exactas, Físicas y Naturales*. https://doi.org/10.18257/raccefyn.3274

- Abuchar, V. J., & Arteta, C. A. (2025). V-FAST: A story-based vulnerability and fragility assessment toolkit for advancing PBEE. *Earthquake Spectra*, *41*(5), 3644-3668. https://doi.org/10.1177/87552930251377782

- Acevedo, A. B., Yepes-Estrada, C., González, D., & Mejía, L. J. (2025). Am I at Risk if an Earthquake Occurs? An Initiative for Raising Seismic Risk Awareness and Knowledge Transferring in the Community. *IDRiM Journal*, *15*(2). https://doi.org/10.5595/001c.150381

- Acevedo, A. B., Yepes‐Estrada, C., González, D., Silva, V., Mora, M., Arcila, M., & Posada, G. (2020). Seismic risk assessment for the residential buildings of the major three cities in Colombia: Bogotá, Medellín, and Cali. *Earthquake Spectra*, *36*(1S), 298-320. https://doi.org/10.1177/8755293020942537

- Acosta, C., & Fuentes, J. (2023). Building Rights for Funding Housing Reconstruction: Mexico City’s After the 2017 Earthquake. *International Handbook of Disaster Research*, 2295-2313. https://doi.org/10.1007/978-981-19-8388-7_40

- Actualizacion de los coeficientes sísmicos de diseño estructural para la Norma Colombiana de Construccion Sismo Resistente NSR. (2021). *Investigaciones en gestion del riesgo de desastres para Colombia: Avances, perspectivas y casos de estudio*. (Sin DOI; completar autores).

- Adhikari, R. K., D'Ayala, D., Fernandez, R., Yamin, L., Nassirpour, A., P Vatteri, A., Ferreira, C., & Cortes, F. (2023). GLOSI taxonomy: A tool for ‘seismic risk assessment’ oriented classification of school buildings. *International Journal of Disaster Risk Reduction*, *87*, 103594. https://doi.org/10.1016/j.ijdrr.2023.103594

- Advances in rapid assessment of damaged buildings by earthquakes. (2021). *Disaster Advances*. (Sin DOI; completar autores).

- Afanador García, N., Guerrero Gómez, G., & Nolasco Serna, C. (2021). Strength of the flexural joint of mortar joints and solid fired clay brick prisms. *Journal of Physics: Conference Series*, *2139*(1), 012017. https://doi.org/10.1088/1742-6596/2139/1/012017

- Alpala, R., Alpala, J., Rosell, P. A., Euillades, L. D., Euillades, P. A., & Battaglia, M. (2025). Satellite Geodesy Reveals Shallow, Transient Magma Intrusions at Sotará Volcano, Colombia. *Journal of Geophysical Research: Solid Earth*, *130*(12), e2025JB031856. https://doi.org/10.1029/2025jb031856

- Angarita, C., Montes, C., & Arroyo, O. (2024). Machine learning – based approach for predicting pushover curves of low-rise reinforced concrete frame buildings. *Structures*, *70*, 107694. https://doi.org/10.1016/j.istruc.2024.107694

- Arango-Serna, S., Gallo, L., Zambrano, J. H., Cruz, A., Sandoval, E., & Thomson, P. (2023). New seismic monitoring center in South America to assess the liquefaction risk posed by subduction earthquakes. *Journal of Seismology*, *27*(3), 385-407. https://doi.org/10.1007/s10950-023-10142-y

- Arango-Serna, S., Herrera, M., Cruz, A., Sandoval, E., Thomson, P., & Ledezma, C. (2021). Use of ambient noise records in seismic engineering: An approach to identify potentially liquefiable sites. *Soil Dynamics and Earthquake Engineering*, *148*, 106837. https://doi.org/10.1016/j.soildyn.2021.106837

- Archbold, J., Carrillo, J., Orjuela Mejia, J., & Piedrahita, J. (2025). Seismic fragility assessment of confined masonry houses in Colombia. *Earthquake Spectra*, *41*(5), 3586-3611. https://doi.org/10.1177/87552930251378782

- Ardila, L., Reyes, J. C., & Moreno, M. P. (2022). Evaluation of Torsional Parameters in Seismic Code Provisions for Multi-story Unsymmetric-Plan Buildings. *Geotechnical, Geological and Earthquake Engineering*, 81-90. https://doi.org/10.1007/978-3-030-83221-6_7

- Aristizabal, C., Bard, P.-Y., & Beauval, C. (2022). Site-Specific PSHA: Combined Effects of Single-Station-Sigma, Host-to-Target Adjustments and Nonlinear Behavior. A case study at Euroseistest. *Italian Journal of Geosciences*, *141*(1), 5-34. https://doi.org/10.3301/ijg.2022.02

- Aroquipa, H., & Hurtado, A. (2022). Seismic resilience assessment of buildings: A simplified methodological approach through conventional seismic risk assessment. *International Journal of Disaster Risk Reduction*, *77*, 103047. https://doi.org/10.1016/j.ijdrr.2022.103047

- Aroquipa, H., Hurtado, A., Angel, C., Aroquipa, A., Gamarra, A., & Almeida Del Savio, A. (2023). A cost-benefit analysis for the appraisal of social and market prices in the probabilistic seismic risk assessment of building portfolios: A methodology for the evaluation of disaster risk reduction programs. *International Journal of Disaster Risk Reduction*, *90*, 103637. https://doi.org/10.1016/j.ijdrr.2023.103637

- Arroyo, O., & Casallas‐Ojeda, M. (2026). Toward Sustainable Seismic Retrofit: A Review of Performance‐Based Earthquake Engineering, Sustainability, and Policy Frameworks. *Earthquake Spectra*, *42*(3), e70102. https://doi.org/10.1002/esp4.70102

- Arroyo, O., Angarita, C., Montes, C., Bonett, R., & Carrillo, J. (2026). Machine Learning‐Based Evaluation of Roof Drifts and Accelerations of Reinforced Concrete Wall Buildings During Ground Motions. *Earthquake Spectra*, *42*(1), e70018. https://doi.org/10.1002/esp4.70018

- Arroyo, O., Bonett, R., & Caballero‐Castro, L. F. (2026). Effect of Slab Modeling Assumptions in Bidirectional Seismic Analysis of Low‐Rise RC Frames: Comparing ACI 318, Eurocode 8, and Other Design Codes. *Earthquake Spectra*, *42*(2), e70056. https://doi.org/10.1002/esp4.70056

- Arroyo, O., Bonett, R., Feliciano, D., & Carrillo, J. (2024). Effect of earthquake directionality on the seismic response of RC wall buildings. *Structures*, *70*, 107773. https://doi.org/10.1016/j.istruc.2024.107773

- Arroyo, O., Bonett, R., Vidales, F., Ocampo, J. J., Feliciano, D., Carrillo, J., & Novoa, D. (2025). Seismic fragility assessment of reinforced concrete wall buildings in Colombia: Insights and implications for earthquake‐resistant design. *Earthquake Spectra*, *41*(1), 354-380. https://doi.org/10.1177/87552930241297564

- Arteta, C. A., Pajaro, C. A., Mercado, V., Montejo, J., Arcila, M., & Abrahamson, N. A. (2023). Ground-Motion Model (GMM) for Crustal Earthquakes in Northern South America (NoSAm Crustal GMM). *Bulletin of the Seismological Society of America*, *113*(1), 186-203. https://doi.org/10.1785/0120220168

- Arteta, C. A., Piedrahita, J., & Segura Jr., C. L. (2025). Autoregularized Model of Compressive Behavior of Structural Wall Boundary Elements. *ACI Structural Journal*, *122*(2). https://doi.org/10.14359/51743302

- Automating building typology identification for seismic risk assessment using deep learning. (2025). *Earthquake Spectra*. `doi:10.1177/875529302513274` (no resuelve en Crossref; corregir en la hoja)

- Ávila-Guzmán, M. P., Herrera, S., Lizarazo-Marriaga, J., Rivas, M., Sierra, J., Arias, C., Ávila, G., Bernal, G., Paéz, J. S., Florez, J. S., Puentes, M., Sanchez, R., Quintero, P., & Ruiz, D. (2026). The impact of earthquake-induced debris on the near-field tsunami pedestrian mobility and safety: Tumaco Island case of study. *Natural Hazards*, *122*(9), 409. https://doi.org/10.1007/s11069-026-08104-x

- Barrera, N., Ruiz, D. M., Reyes, J. C., Alvarado, Y. A., & Carrasco-Beltrán, D. (2023). Seismic Performance of a 1:4 Scale Two-Story Rammed Earth Model Reinforced with Steel Plates Tested on a Bi-Axial Shaking Table. *Buildings*, *13*(12), 2950. https://doi.org/10.3390/buildings13122950

- Bastidas, N., Caballero-Castro, L. F., & Arroyo, O. (2026). Comparative seismic performance of TADAS and BRBs in retrofitting non-ductile RC frames: Insights from a public attention building in Colombia. *Structures*, *91*, 112692. https://doi.org/10.1016/j.istruc.2026.112692

- Bay, C. O., Palazzo, G. L., Almazán, J. L., & Villalba-Morales, J. D. (2026). Impact of a displacement-based design procedure in the hysteretic steel dampers-based seismic retrofitting of mid-rise regular reinforced concrete framed buildings. *Asian Journal of Civil Engineering*, *27*(7), 3435-3458. https://doi.org/10.1007/s42107-026-01676-w

- Benjumea, J., Saiidi, M. “., & Itani, A. (2021). Large-Scale Biaxial Shake-Table Studies of a Precast Bridge Model. *Journal of Structural Engineering*, *147*(7), 04021104. https://doi.org/10.1061/(asce)st.1943-541x.0003060

- Benjumea, J., Saiidi, M. “., & Itani, A. (2021). Biaxial Seismic Performance of a Two-Span Concrete Bridge Model with Six ABC Connections. *Journal of Bridge Engineering*, *26*(8), 04021056. https://doi.org/10.1061/(asce)be.1943-5592.0001753

- Benjumea, J., Saiidi, M., & Itani, A. (2020). Seismic performance analysis and assessment of a precast bridge computational model. *DYNA*, *87*(212), 80-89. https://doi.org/10.15446/dyna.v87n212.80143

- Bermúdez, H. D., Martini, M., Vega, F. J., Bolívar, L., Vajda, V., Vega-Sandoval, F. A., Bermúdez, D., & Cui, Y. (2026). The Chicxulub mega-earthquake: Stratigraphic evidence from the Cretaceous-Paleogene boundary of Colombian Pacific and northeastern Mexico. *Journal of South American Earth Sciences*, *176*, 106058. https://doi.org/10.1016/j.jsames.2026.106058

- Bishop, B. T., Cho, S., Warren, L., Soto-Cordero, L., Pedraza, P., Prieto, G. A., & Dionicio, V. (2022). Oceanic intraplate faulting as a pathway for deep hydration of the lithosphere: Perspectives from the Caribbean. *Geosphere*, *19*(1), 206-234. https://doi.org/10.1130/ges02534.1

- Blandón, C. A., Bonett, R., Feliciano, D., Carrillo, J., Savvas, S., & Takeuchi, C. (2025). Out-of-plane cyclic tests of pre-damaged hollow clay masonry school facades retrofitted with bamboo-reinforced mortar. *Structures*, *81*, 110255. https://doi.org/10.1016/j.istruc.2025.110255

- Blandón, C., & Bonett, R. (2020). Thin slender concrete rectangular walls in moderate seismic regions with a single reinforcement layer. *Journal of Building Engineering*, *28*, 101035. https://doi.org/10.1016/j.jobe.2019.101035

- Bolin, J., Shanshan, W., Mohammed, O. I., Ponnore, J. J., Ali, H. E., Assilzadhe, H., & Escorcia-Gutierrez, J. (2025). RETRACTED: Impact of joint interactions in concrete segmental tunnels: Advanced numerical modeling for seismic resilience. *Structures*, *78*, 109164. https://doi.org/10.1016/j.istruc.2025.109164

- Bonett, R., Vidales, F., Arroyo, O., Ocampo, J. J., Feliciano, D., & Carrillo, J. (2026). Impact of Structural Configurations on Seismic Performance of Low‐ and Mid‐Rise Thin Lightly Reinforced Concrete Wall Buildings. *Earthquake Spectra*, *42*(2), e70010. https://doi.org/10.1002/esp4.70010

- Building collapse prediction due to earthquakes through ML algorithm: Hybrid methodology based on past-earthquake damage reports and resilience index. (2026). *Resilient Cities and Structures 5 (2026) 102-117*. `doi:10.1016/j.rens.2026.02.001` (no resuelve en Crossref; corregir en la hoja)

- Caballero-Castro, L. F., Cano-Castaño, H. A., Molina-Herrera, M., Villalba-Morales, J. D., & Arroyo, O. (2024). Evaluating the response modification factor (R) for reinforced concrete and steel structures equipped with TADAS devices designed for high seismic hazard in Colombia. *Structures*, *65*, 106748. https://doi.org/10.1016/j.istruc.2024.106748

- Caballero-Castro, L. F., Feliciano, D., Montes, C., Molina, M., Arroyo, O., & Villalba-Morales, J. D. (2025). Seismic loss assessment of medium-rise reinforced concrete frames in Colombia equipped with TADAS dampers. *Structures*, *75*, 108732. https://doi.org/10.1016/j.istruc.2025.108732

- Cadena, Ó. E., & Sánchez, J. J. (2022). Conduit resonance models for long-period seismicity at Galeras volcano (Colombia), during 2004–2010. *Journal of South American Earth Sciences*, *113*, 103661. https://doi.org/10.1016/j.jsames.2021.103661

- Caicedo, D., Lara-Valencia, L., Blandon, J., & Graciano, C. (2021). Seismic response of high-rise buildings through metaheuristic-based optimization using tuned mass dampers and tuned mass dampers inerter. *Journal of Building Engineering*, *34*, 101927. https://doi.org/10.1016/j.jobe.2020.101927

- Carrillo, J., Arteta, C. A., & Vera, X. (2024). Post-earthquake safety assessment of schools after the 2016 Ecuador M7.8 earthquake. *Soil Dynamics and Earthquake Engineering*, *179*, 108561. https://doi.org/10.1016/j.soildyn.2024.108561

- Castro-Cabrera, P., Castellanos-Dominguez, G., Mera, C., Franco-Marín, L., & Orozco-Alzate, M. (2021). Adaptive classification using incremental learning for seismic-volcanic signals with concept drift. *Journal of Volcanology and Geothermal Research*, *413*, 107211. https://doi.org/10.1016/j.jvolgeores.2021.107211

- Celorio, M., Guéguen, P., Aochi, H., de Martin, F., & Bonilla, L. F. (2025). Urban Attenuation Lengths in City-Like Environments: Insights from 3D Numerical Simulations of Site–City Interaction. *Bulletin of the Seismological Society of America*, *116*(1), 515-531. https://doi.org/10.1785/0120250139

- Celorio, M., Guéguen, P., Touma, R., & Roux, P. (2026). Experimental characterization of urban-like scattering and attenuation from a dense nodal array: implications for seismic ground motion. *Geophysical Journal International*, *246*(1), ggag165. https://doi.org/10.1093/gji/ggag165

- Chalarca, B., Bedoya-Ruiz, D., & Herrera, J. P. (2023). Experimental behavior and seismic performance assessment of Unbonded Post-tensioned Precast Concrete Walls for low-rise buildings. *Engineering Structures*, *289*, 116251. https://doi.org/10.1016/j.engstruct.2023.116251

- Chávez-García, F. J., Monsalve-Jaramillo, H., & Vila-Ortega, J. (2021). Vulnerability and site effects in earthquake disasters in Armenia (Colombia) – Part 2 : Observed damage and vulnerability. *Natural Hazards and Earth System Sciences*, *21*(8), 2345-2354. https://doi.org/10.5194/nhess-21-2345-2021

- Chávez-García, F. J., Monsalve-Jaramillo, H., & Vila-Ortega, J. (2023). Estructura del subsuelo de la Sabana de Bogotá. Análisis de dispersión de ondas superficiales a partir de sismos y ruido sísmicos. *Geofísica Internacional*, *62*(1), 419-429. https://doi.org/10.22201/igeof.2954436xe.2023.62.1.1449

- Chen, J., Ponnore, J. J., Ali, H. E., Elkamchouchi, D. H., & Escorcia-Gutierrez, J. (2025). Enhancing seismic resilience of reinforced concrete frame structures through restoration order modeling and the ISN framework: An intelligent modeling framework. *Structures*, *82*, 110565. https://doi.org/10.1016/j.istruc.2025.110565

- Chen, M. C., Restrepo, J. I., Blandon, C., & Velásquez, J. F. (2021). Performance-based seismic design framework for inertia-sensitive nonstructural components in base-isolated buildings. *Journal of Building Engineering*, *43*, 103073. https://doi.org/10.1016/j.jobe.2021.103073

- Chicangana-Montón, G., Bocanegra-Gómez, A., Pardo-Mayorga, J., Salcedo-Hurtado, E. d. J., Gómez-Capera, A., & Vargas-Jiménez, C. A. (2022). Sismicidad y sismotectónica para el sector norte del ámbito del Sistema de Fallas de Algeciras, Cordillera Oriental, Colombia. *Boletín de Geología*, *44*(1). https://doi.org/10.18273/revbol.v44n1-2022005

- Contribucion de la geodesia espacial en la gestion del riesgo en Colombia. Casos de estudio. (2021). *Investigaciones en gestion del riesgo de desastres para Colombia: Avances, perspectivas y casos de estudio*. (Sin DOI; completar autores).

- Correal, J. F., Hidalgo, V., Reyes, J. C., & Ángel, C. C. (2020). A comparative study of seismic diaphragm design forces for RC dual system buildings. *Bulletin of Earthquake Engineering*, *18*(9), 4515-4540. https://doi.org/10.1007/s10518-020-00870-8

- Cortés Arias, A. M., Peña Ocampo, F., & Cundumí Sánchez, O. (2021). INFLUENCE OF THE DYNAMIC SOIL-STRUCTURE INTERACTION IN CONCRETE FRAMES WITH INCORPORATED VISCOUS DAMPERS. *Proceedings of the 8th International Conference on Computational Methods in Structural Dynamics and Earthquake Engineering (COMPDYN 2015)*, 5078-5092. https://doi.org/10.7712/120121.8850.19376

- Cristancho, K., Otálvaro, I. F., Ruiz, D. M., Barrera, N., Villalba-Morales, J. D., Alvarado, Y. A., & Cundumí, O. (2024). Seismic Behavior of Bahareque Walls Under In-Plane Horizontal Loads. *Buildings*, *15*(1), 4. https://doi.org/10.3390/buildings15010004

- Cruz, A., Chieffo, N., Karimzadeh, S., Ortiz, A., Sandoval, E., & Lourenço, P. B. (2025). Earthquake vulnerability assessment of non-engineered URM residential buildings. *International Journal of Disaster Risk Reduction*, *122*, 105476. https://doi.org/10.1016/j.ijdrr.2025.105476

- Cruz, A., Farnoudkia, H., Karimzadeh, S., Chieffo, N., Sandoval, E., & Lourenço, P. B. (2026). Rapid seismic screening of non-engineered URM buildings in liquefaction-prone areas. *Soil Dynamics and Earthquake Engineering*, *210*, 110521. https://doi.org/10.1016/j.soildyn.2026.110521

- Cruz, A., Ghasemi, M., Karimzadeh, S., Karimzadeh, S., Askan, A., Matsuoka, M., & Lourenço, P. B. (2025). 28 March 2025 Myanmar Earthquake: Strong Ground Motions, Macroseismic Intensity, Liquefaction, and ALOS-2 ScanSAR Remote Sensing Damage Observations. *Seismological Research Letters*, *97*(3), 1595-1612. https://doi.org/10.1785/0220250258

- Cruz, A., Karimzadeh, S., Chieffo, N., Sandoval, E., & Lourenço, P. B. (2026). Probabilistic liquefaction hazard assessment in urban centres with a non-liquefiable surface layer overlying a liquefiable stratum. *Bulletin of Earthquake Engineering*, *24*(9), 6809-6841. https://doi.org/10.1007/s10518-026-02512-x

- Cumulative damage in RC buildings – The case of the 2017 Puebla-Morelos earthquake. (2023). *Conference Paper*. https://www.researchgate.net/publication/344364135_cumulative_damage_in_rc_buildings_-_the_case_of_the_2017_puebla-morelos_earthquake

- Cundumí García, J. S., & Cundumí Sánchez, O. (2021). COMPARISON BETWEEN DYNAMIC NONLINEAR ANALYSIS WITH ASCE 7-10 AND ASCE 7-16 IN CONCRETE FRAMES WITH VISCOUS DAMPERS INCORPORATED. *Proceedings of the 8th International Conference on Computational Methods in Structural Dynamics and Earthquake Engineering (COMPDYN 2015)*, 5342-5356. https://doi.org/10.7712/120121.8870.19422

- De La Hoz, C., Tary, J. B., & Lomax, A. (2021). Empirical subspace detection applied to triggered seismicity by the July 25, 2011, M 5.0 earthquake in the Sea of Marmara, Turkey. *Computers & Geosciences*, *152*, 104738. https://doi.org/10.1016/j.cageo.2021.104738

- Determination of the impact of natural disasters within the Colombian territory using Geographic Information Systems. (2021). *International Journal of Engineering Research and Technology*. (Sin DOI; completar autores).

- Di Giacomo, D., & Sarabia, A. M. (2021). Use of macroseismic and instrumental data to reassess earthquake locations: Examples from pre-digital earthquakes in Colombia. *Journal of South American Earth Sciences*, *111*, 103467. https://doi.org/10.1016/j.jsames.2021.103467

- Eddy current damping in roller seismic isolators: A non-contact energy dissipation mechanism alternative. (2026). *Smart Structures and Systems*. `doi:10.12989/sss.2026.37.1.049` (no resuelve en Crossref; corregir en la hoja)

- EDP Risk Estimation with the Conditional Scenario Spectra (CSS) for Multiple Causal Tectonic Settings. (2022). *12th National Conference on Earthquake Engineering, NCEE 2022*. (Sin DOI; completar autores).

- El-Sekelly, W., & Mercado, V. (2024). Practical considerations in liquefaction numerical simulations calibrated with historical data. *Soil Dynamics and Earthquake Engineering*, *180*, 108608. https://doi.org/10.1016/j.soildyn.2024.108608

- Escobar-Rey, L. K., Mencin, D., Dittmann, T., Mothes, P. A., & Mora-Páez, H. (2024). A Geodetic-Based Earthquake Early Warning System for Colombia and Ecuador. *Seismological Research Letters*, *96*(1), 294-309. https://doi.org/10.1785/0220230390

- Estimating magnitude and location from macroseismic data of the 1925 Colombian earthquake. (2022). *Bulletin of Geophysics and Oceanography*. `doi:10.4430/bgo00386` (no resuelve en Crossref; corregir en la hoja)

- Estrella-Villarreal, C., Ospina-Ostios, L., & Díaz-Tamayo, A. (2024). Exposure to Seismic Hazard in a High-Complexity Hospital in Cali, Colombia. *Disaster Medicine and Public Health Preparedness*, *18*, e301. https://doi.org/10.1017/dmp.2024.313

- Feliciano, D., Arroyo, O., Cabrera, T., Contreras, D., Valcárcel Torres, J. A., & Gómez Zapata, J. C. (2023). Seismic risk scenarios for the residential buildings in the Sabana Centro province in Colombia. *Natural Hazards and Earth System Sciences*, *23*(5), 1863-1890. https://doi.org/10.5194/nhess-23-1863-2023

- Feliciano, D., Novoa, D., Arroyo, O., Carrillo, J., Liel, A., Montes, C., & Bonett, R. (2025). Seismic assessment of non-engineered incrementally constructed unreinforced masonry infilled RC frames considering material variability. *International Journal of Disaster Risk Reduction*, *128*, 105703. https://doi.org/10.1016/j.ijdrr.2025.105703

- Fernández, R., Correal, J. F., D’Ayala, D., & Medaglia, A. L. (2023). A decision-making framework for school infrastructure improvement programs. *Structure and Infrastructure Engineering*, *21*(2), 165-184. https://doi.org/10.1080/15732479.2023.2199361

- Fernández, R., Yamin, L., D’Ayala, D., Adhikari, R., Reyes, J. C., Echeverry, J., & Fuentes, G. (2022). A simplified component-based methodology for the seismic vulnerability assessment of school buildings using nonlinear static procedures: application to RC school buildings. *Bulletin of Earthquake Engineering*, *20*(12), 6555-6585. https://doi.org/10.1007/s10518-022-01445-5

- Florez, A. J., Giraldo, L. F., Gutierrez Soto, M., & Zuñiga, F. O. (2021). Structural sparsity in control design of active and semi‐active systems. *Structural Control and Health Monitoring*, *28*(8). https://doi.org/10.1002/stc.2758

- Gabriel, E., Rodríguez-Cortés, F., Coville, J., Mateu, J., & Chadœuf, J. (2022). Mapping the intensity function of a non-stationary point process in unobserved areas. *Stochastic Environmental Research and Risk Assessment*, *37*(1), 327-343. https://doi.org/10.1007/s00477-022-02304-0

- Garani, G., Pramantiotis, G., & Arboleda, F. J. M. (2025). Spatio-Temporal Earthquake Analysis via Data Warehousing for Big Data-Driven Decision Systems. *Computers, Materials & Continua*, *0*(0), 1-10. https://doi.org/10.32604/cmc.2025.071509

- García-Arias, S., Velandia, F., Khurama, S., & Florez, M. A. (2026). Towards earthquake forecasting in the bucaramanga nest, a machine learning approach. *Journal of Seismology*, *30*(2), 11. https://doi.org/10.1007/s10950-026-10364-w

- Garrido, A., Pongutá, F., & Buitrago, O. Y. (2021). Relocation of public healthcare network of a large city in the event of a major earthquake: a combined methodological analysis. *Journal of Humanitarian Logistics and Supply Chain Management*, *12*(2), 220-248. https://doi.org/10.1108/jhlscm-04-2021-0040

- Generation of a map of seismic events that occurred in Colombia during the last decade. (2021). *International Journal of Engineering Research and Technology*. (Sin DOI; completar autores).

- Geotechnical Aspects of Underground Construction in Soft Ground. (2021). *Proceedings of the 10th International Symposium on Geotechnical Aspects of Underground Construction in Soft Ground, IS-CAMBRIDGE 2022,*. https://doi.org/10.1201/9780429321559

- Godoy, G. C., & Jiménez, C. A. V. (2025). Remote Sensing Detection of Gases and Surface Anomalies as Potential Seismic Precursors. *First Break*, *43*(7), 55-61. https://doi.org/10.3997/1365-2397.fb2025053

- Gómez-García, Á. M., González, Á., Cacace, M., Scheck-Wenderoth, M., & Monsalve, G. (2023). Crustal Seismogenic Thickness and Thermal Structure of NW South America. *Solid Earth*. https://doi.org/10.5194/egusphere-2023-798

- Gómez-García, Á. M., González, Á., Cacace, M., Scheck-Wenderoth, M., & Monsalve, G. (2024). Thermal structure of the southern Caribbean and northwestern South America: implications for seismogenesis. *Solid Earth*, *15*(2), 281-303. https://doi.org/10.5194/se-15-281-2024

- Gonzalez, D., Rueda-Plata, D., Acevedo, A. B., Duque, J. C., Ramos-Pollán, R., Betancourt, A., & García, S. (2020). Automatic detection of building typology using deep learning methods on street level images. *Building and Environment*, *177*, 106805. https://doi.org/10.1016/j.buildenv.2020.106805

- Ground Motion Models for Northern South America. (2022). *12th National Conference on Earthquake Engineering, NCEE 2022*. `doi:10.1177/8755293021102758` (no resuelve en Crossref; corregir en la hoja)

- Gutiérrez, J. D., Tapias-Rivera, J., Hijuelos-Cárdenas, M. L., & Montaño-Villalba, L. E. (2026). Effect of sea surface temperature in El Niño regions on dengue dynamics in Colombia: Evidence from causal machine learning. *PLOS Global Public Health*, *6*(1), e0005796. https://doi.org/10.1371/journal.pgph.0005796

- Guzman, A., Leon, C., Vuelvas, J., & Manrique, M. (2021). Earthquake Simulator. *2021 IEEE 5th Colombian Conference on Automatic Control (CCAC)*, 268-273. https://doi.org/10.1109/ccac51819.2021.9633272

- Herrera, J. P., Bedoya-Ruiz, D., & Hurtado, J. E. (2020). Performance-based seismic assessment of precast ferrocement walls for one and two-storey housing. *Engineering Structures*, *214*, 110589. https://doi.org/10.1016/j.engstruct.2020.110589

- Hoyos, M. C., & Hernandez, A. F. (2022). Seismic Risk Assessment of Multiple Cities: Biases in the Vulnerability Derivation Methods for Urban Areas With Different Hazard Levels. *Frontiers in Earth Science*, *10*, 910118. https://doi.org/10.3389/feart.2022.910118

- Hurtado, A., Aroquipa, H., Restrepo, D., Nieto, F., & Carrillo, J. (2026). Building collapse prediction due to earthquakes through ML algorithm: Hybrid methodology based on past-earthquake damage reports and resilience index. *Resilient Cities and Structures*, *5*(1), 102-117. https://doi.org/10.1016/j.rcns.2026.02.001

- Hurtado, M. I., Vega, J. A., & Hidalgo, C. A. (2020). Comparison of Geometric and Experimental Models for the Assessment of the Runout and Deposition Height of a Debris Flow in Cohesive Soils. *IOP Conference Series: Materials Science and Engineering*, *960*(2), 022027. https://doi.org/10.1088/1757-899x/960/2/022027

- Jaimes, N., Prieto, G. A., & Rodriguez, C. (2021). Detection of Building Response Changes Using Deconvolution Interferometry: A Case Study in Bogota, Colombia. *Seismological Research Letters*, *93*(2A), 931-942. https://doi.org/10.1785/0220210219

- Jarrin, P., Nocquet, J.-M., Rolandone, F., Mora-Páez, H., Mothes, P., & Cisneros, D. (2022). Current motion and deformation of the Nazca Plate: new constraints from GPS measurements. *Geophysical Journal International*, *232*(2), 842-863. https://doi.org/10.1093/gji/ggac353

- Kumbhar, O. G., & Kumar, R. (2018). Effect of Modeling Assumptions on Seismic Performance of RC Building. *Lecture Notes in Civil Engineering*, 73-84. https://doi.org/10.1007/978-981-13-0362-3_6

- Lagardère, C., & Vargas, C. A. (2021). Earthquake distribution and lithospheric rheology beneath the Northwestern Andes, Colombia. *Geodesy and Geodynamics*, *12*(1), 1-10. https://doi.org/10.1016/j.geog.2020.12.002

- Lemos-Micolta, E. D., Velasco-Cuervo, I. C., Madera-Sierra, I. E., Rojas-Manzano, M. A., Cundumí, O., Patino, E., Salmeron-Becerra, M., Lopez-Arias, M., Dyke, S. J., & Velay-Lizancos, M. (2025). Assessment of the Mechanical Properties of Low-Cost Seismic Isolators Exposed to Environmental Conditions. *Applied Sciences*, *15*(7), 3467. https://doi.org/10.3390/app15073467

- Leon, D., Valdivia, J., & Bucheli, V. (2021). A revision of seismicity models based on complex systems and earthquake networks. *Journal of Seismology*, *26*(1), 137-145. https://doi.org/10.1007/s10950-021-10017-0

- Leonardi, A., Cabrera, M. A., & Pirulli, M. (2021). Coriolis-induced instabilities in centrifuge modeling of granular flow. *Granular Matter*, *23*(2), 52. https://doi.org/10.1007/s10035-021-01111-8

- Leyva, H., Bojórquez, J., Bojórquez, E., Reyes-Salazar, A., Carrillo, J., & López-Almansa, F. (2021). Multi-objective seismic design of BRBs-reinforced concrete buildings using genetic algorithms. *Structural and Multidisciplinary Optimization*, *64*(4), 2097-2112. https://doi.org/10.1007/s00158-021-02965-5

- Li, Z., Yan, G., Zandi, Y., Gholizadeh, M., Chen, Y., Khairy, Y., & Escorcia-Gutierrez, J. (2026). A bayesian ordinal structural equation modeling framework for evaluating the seismic resilience of IoT-enabled buildings under uncertainty. *Structures*, *88*, 111650. https://doi.org/10.1016/j.istruc.2026.111650

- Liquefaction and site response analysis using the PDMY03 effective stress model. (2026). *Geomechanics and Engineering*. `doi:10.12989/gae.2026.46.2.255` (no resuelve en Crossref; corregir en la hoja)

- Londoño, J. M., Velásquez, L. V., & Bermúdez, J. C. (2022). Seismic wave attenuation at Valle Medio del Magdalena, Colombia. *Journal of South American Earth Sciences*, *119*, 103987. https://doi.org/10.1016/j.jsames.2022.103987

- Lopez-Caballero, F., Aristizábal, C., & Sánchez-Silva, M. (2020). A model to estimate the lifetime of structures located in seismically active regions. *Engineering Structures*, *215*, 110662. https://doi.org/10.1016/j.engstruct.2020.110662

- Mantilla-Duarte, C. A., & Angulo, J. M. (2025). Entropy-based assessment of complexity structural effects of the third dimension, case seismic nest of Los Santos (Colombia). *Stochastic Environmental Research and Risk Assessment*, *39*(3), 911-923. https://doi.org/10.1007/s00477-024-02890-1

- Martínez-Jaramillo, D., & Prieto, G. A. (2024). Tectonic setting of the northwestern andes Constrained by a high-resolution earthquake catalog: Block Kinematics. *Journal of South American Earth Sciences*, *134*, 104761. https://doi.org/10.1016/j.jsames.2023.104761

- Marulanda, M. C., de la Llera, J. C., Bernal, G. A., & Cardona, O. D. (2021). Epistemic uncertainty in probabilistic estimates of seismic risk resulting from multiple hazard models. *Natural Hazards*, *108*(3), 3203-3227. https://doi.org/10.1007/s11069-021-04820-8

- Mebarki, A., & Jerez, S. (2024). Emergency management and urban resilience under seismic risks. Part II: validation and sensitivity analysis for buildings seismic damage evaluation. *Emergency Management Science and Technology*, *4*(1), 0-0. https://doi.org/10.48130/emst-0024-0025

- Melo, D. A., Garcia-Troncoso, N., Villamizar, S., Castañeda, G., & Gomez, D. (2026). The Learning Experience for Earthquake Awareness Program (LEAP): An Experiential Approach to Seismic Design for Young Students. *Sustainability*, *18*(3), 1233. https://doi.org/10.3390/su18031233

- Mendoza, C., Matos, J., Galvão, N., & Viviescas, Á. (2021). Reliability based performance assessment of a roadway bridge under seismic actions. *IABSE Congress Reports*, 212-219. https://doi.org/10.2749/christchurch.2021.0212

- Mercado, V., Díaz-Parra, F. J., Pajaro, C. A., Montejo, J., Posada, G., Arcila, M., & Arteta, C. A. (2024). Performance evaluation of parameters as estimators of seismic site effects in northern South America. *Soil Dynamics and Earthquake Engineering*, *180*, 108584. https://doi.org/10.1016/j.soildyn.2024.108584

- Mercado, V., Pico, M., Duque, J., & El-Sekelly, W. (2026). Effects of soil heterogeneity on the numerical simulation of liquefiable soil deposits using a multi-surface plasticity model. *Soil Dynamics and Earthquake Engineering*, *203*, 110097. https://doi.org/10.1016/j.soildyn.2026.110097

- Meza-Muñoz, A. O., Rivas-Ordoñez, F. S., Madera-Sierra, I. E., Rojas-Manzano, M. A., Patino-Reyes, E. D., Salmerón-Becerra, M. I., & Dyke, S. J. (2024). Development of a Matrix for Seismic Isolators Using Recycled Rubber from Vehicle Tires. *Polymers*, *16*(21), 2977. https://doi.org/10.3390/polym16212977

- Mitigacion del riesgo sísmico de la infraestructura escolar. (2021). *Investigaciones en gestion del riesgo de desastres para Colombia: Avances, perspectivas y casos de estudio*. (Sin DOI; completar autores).

- Miura, H., Matsuoka, M., Reyes, J. C., Pulido, N., Hashimoto, M., Riaño, A. C., Hurtado, A., Rincon, R., García, H., & Lozano, C. (2023). Quick Estimation Model for Mapping Earthquake Impacts in Bogotá, Colombia. *ISPRS International Journal of Geo-Information*, *12*(12), 471. https://doi.org/10.3390/ijgi12120471

- Molina-Gómez, F., González-Olaya, R., & Camacho-Tauta, J. (2024). Exploring liquefaction resistance in saturated and gassy sands at different state parameters. *Transportation Geotechnics*, *49*, 101410. https://doi.org/10.1016/j.trgeo.2024.101410
get rights and content

- Molina-Gómez, F., Viana da Fonseca, A., Ferreira, C., & Caicedo, B. (2024). Insights into the assessment and interpretation of earthquake-induced liquefaction in sands under different degrees of saturation. *Earth-Science Reviews*, *258*, 104925. https://doi.org/10.1016/j.earscirev.2024.104925

- Moreno González, C. L., Montoya, G. A., & Lozano Garzón, C. (2025). Toward Reliable Post-Disaster Assessment: Advancing Building Damage Detection Using You Only Look Once Convolutional Neural Network and Satellite Imagery. *Mathematics*, *13*(7), 1041. https://doi.org/10.3390/math13071041

- Moreno-Torres, O., Franco-Leyva, A., & Sierra, M. M. (2024). Impact of Liquefiable Layers on Site Response Analysis. *Civil Engineering and Architecture*, *12*(6), 4144-4158. https://doi.org/10.13189/cea.2024.120628

- Muñoz Lopez, C., Velasquez, L., & Dionicio, V. (2020). Calibration of Local Magnitude Scale for Colombia. *Bulletin of the Seismological Society of America*, *110*(4), 1971-1981. https://doi.org/10.1785/0120190226

- Murray, P. B., Feliciano, D., Goldwyn, B. H., Liel, A. B., Arroyo, O., & Javernick‐Will, A. (2023). Seismic safety of informally constructed reinforced concrete houses in Puerto Rico. *Earthquake Spectra*, *39*(1), 5-33. https://doi.org/10.1177/87552930221123085

- Naranjo-Vesga, J., Ortiz-Karpf, A., Wood, L., Jobe, Z., Paniagua-Arroyave, J. F., Shumaker, L., Mateus-Tarazona, D., & Galindo, P. (2020). Regional controls in the distribution and morphometry of deep-water gravitational deposits along a convergent tectonic margin. Southern Caribbean of Colombia. *Marine and Petroleum Geology*, *121*, 104639. https://doi.org/10.1016/j.marpetgeo.2020.104639

- Navarro-Rodríguez, A., Castro-Artola, O. A., Rösler, B., García-Guerrero, E. E., Aguirre-Castro, O. A., Galarza-Falfan, J., & Inzunza-Gonzalez, E. (2026). Real-time seismic signal classification using deep vision architectures for earthquake early warning systems. *Earth Science Informatics*, *19*(4), 44. https://doi.org/10.1007/s12145-026-02099-6

- Niasar, A. N., Alaee, F. J., & Zamani, S. M. (2020). Experimental investigation on the performance of unreinforced masonry wall, retrofitted using engineered cementitious composites. *Construction and Building Materials*, *239*, 117788. https://doi.org/10.1016/j.conbuildmat.2019.117788

- Norini, G., Aghib, F. S., Di Capua, A., Facciorusso, J., Castaldini, D., Marchetti, M., Cavallin, A., Pini, R., Ravazzi, C., Zuluaga, M. C., Aldighieri, B., Furlanetto, G., Testa, B., de Franco, R., Caielli, G., Groppelli, G., Boniolo, G., Corsi, A., Baraldi, F., & Piccin, A. (2021). Assessment of liquefaction potential in the central Po plain from integrated geomorphological, stratigraphic and geotechnical analysis. *Engineering Geology*, *282*, 105997. https://doi.org/10.1016/j.enggeo.2021.105997

- Nuñez, E., Boainy, N., González, F., Torres, R., Picón, R., & Guerrero, N. (2020). Cyclic Behavior of Hollow Section Beam–Column Moment Connection: Experimental and Numerical Study. *Metals*, *10*(12), 1608. https://doi.org/10.3390/met10121608

- Núñez, F., Ruiz, D., & Cortés, J. (2021). Nonlinear dynamic analysis of steel buildings subjected to earthquakes. *Revista ingeniería de construcción*, *36*(2), 173-196. https://doi.org/10.4067/s0718-50732021000200173

- Nuñez-Moreno, F., Ruiz, D. M., Aristizabal-Vargas, S., Gutierrez-Quintero, C., & Alvarado, Y. A. (2025). Seismic Performance of a Full-Scale Moment-Frame Housing System Constructed with Recycled Tetra Pak (Thermo-Stiffened Polymeric Aluminum Composite). *Buildings*, *15*(5), 813. https://doi.org/10.3390/buildings15050813

- Nuzzo, I., Riascos, C., Losanno, D., & Caterino, N. (2023). Loss-Driven Rapid Warning Methodology for Seismic Risk Mitigation of a Target Railway Infrastructure. *Procedia Structural Integrity*, *44*, 1832-1839. https://doi.org/10.1016/j.prostr.2023.01.234

- Obando, J. C., Carrillo, J., & Arroyo, O. (2024). Inelastic acceleration ratios for nonstructural components. *Structures*, *69*, 107374. https://doi.org/10.1016/j.istruc.2024.107374

- Ordaz, M., Salgado‐Gálvez, M. A., & Cardona, O. D. (2023). Review and comparison of different strategies to define earthquake design accelerations. *Earthquake Engineering & Structural Dynamics*, *52*(13), 3945-3961. https://doi.org/10.1002/eqe.3950

- Oviedo-Amezquita, J. A., Jaramillo-Santana, N., Blandon-Uribe, C. A., & Bernal-Zuluaga, A. M. (2021). Development and validation of an acceptance criteria and damage index for buckling-restrained braces (BRB). *Journal of Building Engineering*, *43*, 102534. https://doi.org/10.1016/j.jobe.2021.102534

- Parada Alzate, L. M., Andramunio Acero, C. P., López Muñoz, M. T., Rondón Martínez, Y. F., & Moreno Pérez, L. A. (2024). Zonificación de Altos Valores de Conservación (AVC) del Complejo Cenagoso de Zapatosa (Colombia) a partir de una evaluación multicriterio. *Investigaciones Geográficas*(115). https://doi.org/10.14350/rig.60945

- Payán-Serrano, O., Bojórquez, E., Carrillo, J., Bojórquez, J., Leyva, H., Rodríguez-Castellanos, A., Carvajal, J., & Torres, J. (2024). Seismic Performance Prediction of RC, BRB and SDOF Structures Using Deep Learning and the Intensity Measure INp. *AI*, *5*(3), 1496-1516. https://doi.org/10.3390/ai5030072

- Paz-Orozco, H., de Brito Junior, I., Chong, M., Anacona-Mopan, Y., Segura Dorado, J. A., & Moyano, M. (2023). Earthquake Decision-Making Tool for Humanitarian Logistics Network: An Application in Popayan, Colombia. *Logistics*, *7*(4), 68. https://doi.org/10.3390/logistics7040068

- Pérez-Cuervo, J. R., Sañudo-Fontaneda, L. A., & Díaz-Bello, S. (2026). Development of a Constitutive Model Based on Fique Fibre (Furcraea macrophylla) as a Reinforcement Material in Bioengineering Projects. *Applied Sciences*, *16*(13), 6692. https://doi.org/10.3390/app16136692

- Pérez-Orozco, A. B., Blanco-Carvajal, E., Pedraza-Ballén, J. R., & Galvis-Cuadrado, M. A. (2023). Sistema multiagente para el análisis del comportamiento social ante un acontecimiento sismológico. *AiBi Revista de Investigación, Administración e Ingeniería*, *11*(2), 66-81. https://doi.org/10.15649/2346030x.3249

- Performance and Comparison of Derivation Methods for Fragility Curves When Using Hazard-Consistent CS Ground Motion Selection. (2022). *12th National Conference on Earthquake Engineering, NCEE 2022*. (Sin DOI; completar autores).

- Performance of prototype seismic isolators reinforced with fiber and a recycled rubber tire matrix. (2023). *Engineering Structures*. `doi:10.1007/s13762-022-04734-4` (no resuelve en Crossref; corregir en la hoja)

- Piscal-Arévalo, C. M., Villalba-Morales, J. D., Hurtado, X., Ángel-Giraldo, D. C., & Rincón-Chuscano, C. A. (2023). Structural behavior of a seismic-isolated stadium grandstand considering hard and soft soil conditions. *DYNA*, *90*(226), 58-65. https://doi.org/10.15446/dyna.v90n226.105469

- Posada, G., Díaz-Parra, F., & Montejo, J. (2025). Characterizing Seismic Response and Ground Motion Topographic Effects: A Local-Scale Study for Geotechnical Applications. *Annals of Geophysics*, *68*(3), NS337. https://doi.org/10.4401/ag-9251

- Posada, G., Monsalve, G., Hoyos, C. D., Pérez-Hincapié, A. M., & Trujillo-Cadavid, J. C. (2022). Ground accelerations and empirical site classification through H/V response spectral ratio (HVRSR) using historical records from the strong motion network of the Aburrá Valley, Colombia. *Soil Dynamics and Earthquake Engineering*, *152*, 107063. https://doi.org/10.1016/j.soildyn.2021.107063

- Prieto, G. A., & Kohler, M. D. (2024). Time‐varying damping ratios and velocities in a high‐rise during earthquakes and ambient vibrations from coda wave interferometry. *Earthquake Spectra*, *40*(3), 2092-2115. https://doi.org/10.1177/87552930241240458

- Quintanar, L., Molina-García, S. P., & Espíndola, V. H. (2022). The Gorgona island, Colombia, earthquake of 10 September 2007 (Mw 6.8); rupture process and implications on the seismic hazard in the region. *Journal of South American Earth Sciences*, *118*, 103941. https://doi.org/10.1016/j.jsames.2022.103941

- Raja, M. N. A., Mercado, V., Abdoun, T., & El-Sekelly, W. (2025). Seismic site amplification prediction- an integrated Bayesian optimisation explainable machine learning approach. *Georisk: Assessment and Management of Risk for Engineered Systems and Geohazards*, *19*(3), 573-592. https://doi.org/10.1080/17499518.2025.2521870

- Reference framework for estimating the seismic hazard for technological risks in oil and gas infrastructure. (2024). *10th Latin American Conference on Process Safety 2024*. (Sin DOI; completar autores).

- Reyes, J. C. (2022). Seismic Behaviour of Torsionally-Weak Buildings with and Without Base Isolators. *Geotechnical, Geological and Earthquake Engineering*, 177-188. https://doi.org/10.1007/978-3-030-83221-6_15

- Reyes, J. C., Acosta, J. E., & Kwong, N. S. (2023). Comprehensive evaluation of target spectra for selecting bidirectional ground motions in nonlinear response history analysis of frame buildings at far‐field sites. *Earthquake Engineering & Structural Dynamics*, *52*(12), 3853-3878. https://doi.org/10.1002/eqe.3952

- Reyes, J. C., Avila, W. A., Kalkan, E., & Sierra, A. (2021). Reducing Processing Time of Nonlinear Analysis of Symmetric-Plan Buildings. *Journal of Structural Engineering*, *147*(6), 04021073. https://doi.org/10.1061/(asce)st.1943-541x.0003000

- Reyes, J. C., Clavijo, A., Martinez, L., Gomez, I. D., & De La Llera, J. C. (2025). Empirical Estimation of Accidental Torsion Using Seismic Records from 76 Symmetric-Plan Buildings. *Geotechnical, Geological and Earthquake Engineering*, 97-105. https://doi.org/10.1007/978-3-031-84220-7_10

- Reyes, J. C., Correal, J. F., Gonzalez-Mancera, A., Echeverry, J. S., Gómez, I. D., Sandoval, J. D., & Ángel, C. C. (2020). Experimental evaluation of permeable cable-supported façades subjected to wind and earthquake loads. *Engineering Structures*, *214*, 110679. https://doi.org/10.1016/j.engstruct.2020.110679

- Reyes, J. C., Smith‐Pardo, J. P., Portilla, S., Torres, E., & Riaño, A. C. (2026). Seismic Fragility and Vulnerability of Partially Grouted Flexural‐Controlled Reinforced Masonry Buildings in Colombia. *Earthquake Spectra*, *42*(3), e70080. https://doi.org/10.1002/esp4.70080

- Reyes, J. C., Torres, E., Portilla, S., Riaño, A. C., & Paul Smith-Pardo, J. (2025). Analytical seismic fragility and vulnerability curves for Colombian informal unreinforced masonry buildings. *Earthquake Spectra*, *41*(5), 3556-3585. https://doi.org/10.1177/87552930251360037

- Rueda-Plata, D., González, D., Acevedo, A. B., Duque, J. C., & Ramos-Pollán, R. (2021). Use of deep learning models in street-level images to classify one-story unreinforced masonry buildings based on roof diaphragms. *Building and Environment*, *189*, 107517. https://doi.org/10.1016/j.buildenv.2020.107517

- Ruiz, D. M., Barrera, N., Reyes, J. C., Alvarado, Y. A., Villalba-Morales, J. D., Gómez, I. D., Vacca, H. A., & Carrasco-Beltrán, D. (2023). Bi-axial shaking table tests to evaluate the seismic performance of two-story rammed-earth walls retrofitted with steel plates. *Bulletin of Earthquake Engineering*, *21*(14), 6393-6422. https://doi.org/10.1007/s10518-023-01769-w

- Ruiz, D. M., Lizarazo, D. F., Alvarado, Y. A., & Vacca, H. (2026). Structural Performance of Full-Scale Cast-in-Place UHPC Moment Frames Under Pseudo-Static Cyclic Loading. *Buildings*, *16*(5), 902. https://doi.org/10.3390/buildings16050902

- Ruiz, D. M., Reyes, J. C., Bran, C., Restrepo, M., Alvarado, Y. A., Barrera, N., Laverde, C., & Suesca, D. (2022). Flexural behavior of rammed earth components reinforced with steel plates based on experimental, numerical, and analytical modeling. *Construction and Building Materials*, *320*, 126231. https://doi.org/10.1016/j.conbuildmat.2021.126231

- Salazar, A., Salazar, E., Cadena, O., & Hernández, R. (2020). Discrimination of seismic waves produced by volcanoes using self-organizing maps. *Journal of Physics: Conference Series*, *1702*(1), 012015. https://doi.org/10.1088/1742-6596/1702/1/012015

- Salazar, B., Ortiz, A., Marulanda Casas, J., Arcila, M., & Montejo, J. (2026). Bayesian Model Updating and Model Selection of Ground Motion Models for Crustal Earthquakes in Colombia. *Earthquake Spectra*, *42*(3), e70090. https://doi.org/10.1002/esp4.70090

- Salcedo-Hurtado, E. d. J., Blandón-Silva, J. C., & Ríos-García, L. (2021). Reevaluación de intensidades macrosísmicas del terremoto del 07 de junio de 1925 en Colombia. *Boletín de Geología*, *43*(3). https://doi.org/10.18273/revbol.v43n3-2021002

- Sánchez Carmona, F., Ordaz Hernández, A., Espinoza Rodríguez, L. M., & Salcedo Hurtado, E. d. J. (2025). Análisis del peligro sísmico: una aproximación cartográfica para el municipio de Toluca, Estado de México. *Cuadernos de Geografía: Revista Colombiana de Geografía*, *34*(2), 436-453. https://doi.org/10.15446/rcdg.v34n2.108571

- Sandoval, E., & Bobet, A. (2020). The undrained seismic response of the Daikai Station. *Tunnelling and Underground Space Technology*, *103*, 103474. https://doi.org/10.1016/j.tust.2020.103474

- Sciuti, V. F., Vargas, R., Guerrero, N., Marante, M. E., & Hild, F. (2023). Digital image correlation analyses of masonry infilled frame: Uncertainty-based mesh refinement and damage quantification. *Mathematics and Mechanics of Solids*, *30*(1), 93-115. https://doi.org/10.1177/10812865231174840

- Seismic damage index as a function of seismic vulnerability for structures in non-structural masonry and reinforced concrete, in city of sincelejo. (2021). *International Journal of Engineering Research and Technology*. (Sin DOI; completar autores).

- Sierra, C., Jaramillo, J., Gomez, J., Sáenz, M., & Vergara, J. (2021). Simplified Evaluation of Ground Motion Amplification in the Vicinity of a Topographic Feature. *Journal of Earthquake Engineering*, *26*(13), 6745-6762. https://doi.org/10.1080/13632469.2021.1927899

- Site response analysis using true coupled constitutive models for liquefaction triggering. (2023). *Earthquake and Structures*. `doi:10.12989/eas.2023.25.1.027` (no resuelve en Crossref; corregir en la hoja)

- Source characteristics of the Mw 6 Mutatá earthquake, Murindo seismic cluster, northwestern Colombia. (2022). *Journal of South American Earth Sciences, 115, art. no. 103728.*. `doi:j.jsames.2022.103728` (no resuelve en Crossref; corregir en la hoja)

- Tarque, N., Ruiz, D. M., Reyes, J. C., & Blondet, M. (2026). State of the Art of Earthquake Resistant Earthen Construction in Colombia and Peru: From Laboratory and Numerical Research to a Latin American Construction Standard. *RILEM Bookseries*, 1315-1330. https://doi.org/10.1007/978-3-032-16767-5_103

- Validation of the seismic response of an RC frame building with masonry infill walls - The case of the 2017 Mexico earthquake. (2022). *Advances in Computational Design*. `doi:10.12989/acd.2022.7.229` (no resuelve en Crossref; corregir en la hoja)

- Vallejo, J. F., Fleck Fadel Miguel, L., & Villalba-Morales, J. D. (2026). Assessment of Objective Functions in the Optimization of Tuned Liquid Dampers for Seismic Retrofit of Vertically Irregular Steel Frames. *Buildings*, *16*(9), 1696. https://doi.org/10.3390/buildings16091696

- Vargas, L., Aguilar, V., Calderón, S., Araya-Letelier, G., & Sandoval, C. (2025). Design of partially grouted reinforced masonry shear walls in an earthquake-prone area: Proposal based on the LRFD approach. *Engineering Structures*, *330*, 119915. https://doi.org/10.1016/j.engstruct.2025.119915

- Vargas-Alzate, Y. F., Hurtado, J. E., & Pujades, L. G. (2021). New insights into the relationship between seismic intensity measures and nonlinear structural response. *Bulletin of Earthquake Engineering*, *20*(5), 2329-2365. https://doi.org/10.1007/s10518-021-01283-x

- Vargas-Alzate, Y. F., Hurtado, J. E., & Pujades, L. G. (2022). Correction to: New insights into the relationship between seismic intensity measures and nonlinear structural response. *Bulletin of Earthquake Engineering*, *20*(5), 2367-2367. https://doi.org/10.1007/s10518-022-01320-3

- Vargas-Alzate, Y., & Hurtado, J. (2021). Efficiency of Intensity Measures Considering Near- and Far-Fault Ground Motion Records. *Geosciences*, *11*(6), 234. https://doi.org/10.3390/geosciences11060234

- Vega, S. C., Gisbert, C. M., & Viviescas, A. (2026). Nonlinear Seismic Response of Long-Span Bridges Constructed by the Balanced Cantilever Method Under Earthquake Excitations. *Applied Sciences*, *16*(7), 3312. https://doi.org/10.3390/app16073312

- Vela, V., Ghahari, F., Kohler, M. D., Prieto, G. A., & Taciroglu, E. (2026). Vertical‐Component Seismic Response and System Identification of a 52‐Story High‐Rise Building Using Earthquake Data. *Earthquake Spectra*, *42*(2), e70036. https://doi.org/10.1002/esp4.70036

- Velasco-Cuervo, I. C., Lemos-Micolta, E. D., Madera-Sierra, I. E., Rojas-Manzano, M. A., Muñoz-Velez, M. F., Cundumí, O., Patino, E., Salmeron-Becerra, M., Dyke, S. J., & Velay-Lizancos, M. (2025). Impact of Aging and Low Temperatures on the Mechanical Properties of Low-Cost Seismic Isolator Prototypes. *Buildings*, *15*(13), 2238. https://doi.org/10.3390/buildings15132238

- Velásquez, J. F., Restrepo, J. I., Blandón, J. J., & Bolaños, F. (2025). Characterization of the Strain Rates in Steel Reinforcement During the Seismic Response of Reinforced Concrete Structures. *Earthquake Engineering & Structural Dynamics*, *54*(8), 2134-2151. https://doi.org/10.1002/eqe.4352

- Vélez Correa, J. A., Salcedo Hurtado, E. d. J., & Castaño Castaño, A. N. (2023). Progresión de la vulnerabilidad frente a sismos en la zona urbana del Distrito de Santiago de Cali, Colombia. *Revista de Estudios Latinoamericanos sobre Reducción del Riesgo de Desastres REDER*, *7*(2), 233. https://doi.org/10.55467/reder.v7i2.135

- Villacreses, J. P., Caicedo, B., Caro, S., Yepez, F., & Puebla, J. S. (2020). Determination of Elastic Parameters due a Dynamic Hertzian Contact. *World Congress on Civil, Structural, and Environmental Engineering*. https://doi.org/10.11159/icgre20.134

- Visualizing the Catastrophe. Photographs and Visual Objects of the 1906 Earthquake in Valparaiso. (2023). *Historia Regional*. https://www.researchgate.net/publication/373649404_visualizar_la_catastrofe_fotografias_y_objetos_visuales_sobre_el_terremoto_de_1906_en_valparaiso

- Wagner, L. S., Prieto, G. A., Montes, C., Ramos, J. P., Dionicio, V., & Pedraza, P. (2025). Breaking the Caribbean Plate: Subduction Initiation Beneath the Northern Margin of Panama. *Geophysical Research Letters*, *52*(18), e2025GL116734. https://doi.org/10.1029/2025gl116734

- Xia, L., You, X., AlKhatib, O. J., Zandi, Y., Sadighi Agdas, A., & Escorcia-Gutierrez, J. (2026). Hybrid AI and finite element framework for seismic assessment of 3D-Printed recycled concrete building wall systems under soil-structure interaction. *Soil Dynamics and Earthquake Engineering*, *210*, 110561. https://doi.org/10.1016/j.soildyn.2026.110561

- Yao, X., Yan, G., Gaaz, T. S., Albaijan, I., Elattar, S., Alrawashdeh, A. I., & Gutierrez, J. E. (2025). Network-driven evaluation of recovery mechanisms in seismic performance of frame structures. *Structures*, *79*, 109367. https://doi.org/10.1016/j.istruc.2025.109367

- Yepes-Estrada, C., Acevedo, A. B., Pérez, H., García, N., Prieto, A., & Calderón, A. (2025). Understanding Seismic Risk in Santiago De Cali (Colombia) for its Application in Risk Management. *International Journal of Disaster Risk Reduction*. https://doi.org/10.2139/ssrn.5079332

- Yépez, F., Benítez, D., Pérez-Pérez, N., Grijalva, F., & Orjuela-Cañon, Á. D. (2025). On the use of AI algorithms applied to strong motion records for the prediction of earthquake fault mechanisms. *IET Conference Proceedings*, *2025*(4), 25-31. https://doi.org/10.1049/icp.2025.1240

- Zamora, V., Hoyos, J., Che, R., & Rodríguez, C. (2025). Effective Torsional Vibration Mitigation in Caño Limon's Underreaming Applications. *SPE/IADC International Drilling Conference and Exhibition*, D012S004R002. https://doi.org/10.2118/223777-ms

- Zapata, A., Arroyo, O., & Bonett, R. (2025). Impact of modeling slabs in the earthquake response of thin reinforced concrete wall buildings. *Bulletin of Earthquake Engineering*, *24*(1), 551-580. https://doi.org/10.1007/s10518-025-02309-4

- Zeballos-Velarde, C., Butron-Revilla, C., Manchego-Huaquipaco, G., & Yory, C. (2023). The role of ancestral practices as social capital to enhance community disaster resilience. The case of the Colca Valley, Peru. *International Journal of Disaster Risk Reduction*, *92*, 103737. https://doi.org/10.1016/j.ijdrr.2023.103737

- Zhong, Y., Gu, C., Prieto, G. A., Fehler, M., Wu, P., Yuan, Z., Xu, W., Xu, S., & Lu, X. (2025). Acoustic Events Detection and Classification for Urban DAS Data with Supervised Learning. *Seismological Research Letters*, *96*(5), 3112-3131. https://doi.org/10.1785/0220240222

- Zúñiga-Olvera, C., Valverde-Burneo, D., Garcia-Troncoso, N., Silva, C. E., Gómez P., D., & Bompa, D. V. (2023). Comparative analysis of the seismic behavior of low-rise buildings with hidden and drop beams. *Proceedings of the 21th LACCEI International Multi-Conference for Engineering, Education and Technology (LACCEI 2023): “Leadership in Education and Innovation in Engineering in the Framework of Global Transformations: Integration and Alliances for Integral Development”*. https://doi.org/10.18687/laccei2023.1.1.219
