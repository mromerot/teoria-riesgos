---
title: Sismos
---

# Sismos

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

## Pendiente

- Leer los resultados completos de {cite:p}`hoyos2022multicity`, {cite:p}`marulanda2021epistemic`, {cite:p}`archbold2025confined`, {cite:p}`reyes2025urm` y {cite:p}`cruz2026liquefaction`. Hoy se citan por título o resumen. Del primero y el segundo no verifiqué si los casos son colombianos.
- Añadir las funciones de vulnerabilidad del Atlas con sus parámetros y las pérdidas anuales esperadas por sismo para ciudades de referencia.
- Buscar la cifra de población en zonas de amenaza sísmica intermedia y alta. El capítulo no la usa: la cifra de 87 % de mis notas no aparece en el texto extraído del Atlas, y la de 83 % del estudio de Sabana Centro no se verificó. No citar ninguna hasta hallar la fuente.
- Añadir el caso de Bogotá, Medellín y Cali (DOI 10.1177/8755293020942537) y la reevaluación de la serie 2021, capítulo 2, para infraestructura escolar.
- Documentar herramientas: OpenQuake (GEM) y CAPRA/CRISIS. Quedan por contrastar con su documentación.
