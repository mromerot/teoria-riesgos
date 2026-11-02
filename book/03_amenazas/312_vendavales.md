---
title: Vendavales
---

# Vendavales

Este capítulo sigue el molde de siete puntos ([](_molde.md)). Trata los vientos fuertes, repentinos y localizados que producen las tormentas convectivas y que en Colombia se conocen como vendavales. Se separa del capítulo de [ciclones tropicales](311_ciclones.md) porque el mecanismo, la escala y los datos son distintos: un ciclón es un sistema de cientos de kilómetros que se pronostica y se sigue durante días; un vendaval dura minutos y afecta unos pocos kilómetros.

```{important}
**Cobertura de fuentes.** El Atlas de Riesgo de Colombia, CLIMAAX y CCDR-tools no tienen una metodología de amenaza para vendavales; el Atlas los menciona solo como efecto indirecto de los ciclones. Este capítulo se apoya en la literatura de ráfagas descendentes {cite:p}`bolgiani2020microbursts`, en el Índice Municipal de Riesgo del DNP {cite:p}`dnp2019imrd`, en el flujo de tormentas de viento de CLIMAAX, pensado para Europa {cite:p}`climaax2025handbook`, y en dos estudios colombianos de convección de la hoja de vigilancia. No hay una metodología colombiana de amenaza por vendavales entre las fuentes revisadas, así que es un capítulo **provisional**.
```

## 1. Fenómeno

### Qué es una tormenta convectiva y qué es un vendaval

Las tormentas convectivas son una de las principales fuentes de amenaza de origen atmosférico. Incluyen las granizadas, las tormentas eléctricas, las tormentas severas, los tornados y los vendavales. Para el conjunto de las tormentas convectivas, EM-DAT registra entre 2000 y 2019 cerca de 8.000 muertes, 242 millones de personas afectadas y 904.000 personas sin hogar en el mundo {cite:p}`emdat2026`. Estas cifras se anotan sin verificar en la base, y la base no discrimina por tipo de viento.

Una ráfaga descendente (*downburst*) se define como un evento en el que una corriente descendente intensa, en los niveles bajos de la atmósfera, produce en la superficie un área de viento dañino con patrón divergente, que va de menos de uno a decenas de kilómetros {cite:p}`bolgiani2020microbursts`. Esos vientos de superficie forman un frente de ráfagas con forma de toroide, que se llama también flujo de salida (*outflow*) {cite:p}`bolgiani2020microbursts`. La corriente descendente se debe sobre todo a la flotabilidad térmica por el enfriamiento latente al cambiar de fase el agua, y también a la carga de condensado, es decir, al peso de la lluvia o del granizo {cite:p}`bolgiani2020microbursts`.

### El término en Colombia

En Colombia estas ráfagas se conocen como **vendavales**. La definición oficial, del documento de terminología de la UNGRD (2017), los describe como una perturbación atmosférica que genera vientos fuertes y destructivos en una sola dirección, con velocidades entre 50 y 80 km/h, durante intervalos cortos y con afectación local {cite:p}`ungrd2017terminologia`. El mismo documento los llama también ventisca, ráfaga y ventarrón, y define aparte el *temporal* como un vendaval acompañado de lluvias fuertes (borrasca o tromba) {cite:p}`ungrd2017terminologia`.

La definición no especifica el mecanismo que produce el viento. Como criterio de método, en este libro «vendaval» designa el viento fuerte, local y de corta duración que causa daño, venga de una ráfaga descendente o de otro proceso; el mecanismo se identifica aparte, con la clasificación siguiente.

### Clasificación de las ráfagas descendentes

La literatura las subdivide por el tamaño del flujo de salida y por la duración de los vientos máximos, y por la lluvia y la reflectividad de radar de la celda {cite:p}`bolgiani2020microbursts`:

| Clase | Criterio |
|---|---|
| **Macrorráfaga** (*macroburst*) | Flujo de salida de más de 4 km de diámetro, con vientos máximos de más de 5 minutos |
| **Microrráfaga** (*microburst*) | Flujo de salida de menos de 4 km, con vientos máximos de menos de 5 minutos |
| Ráfaga **seca** o de baja reflectividad | Precipitación menor a 0,25 mm y reflectividad menor a 35 dBZ |
| Ráfaga **húmeda** o de alta reflectividad | Precipitación mayor a 0,25 mm y reflectividad mayor a 35 dBZ |

Las microrráfagas son un peligro mayor para la aviación y se estudian desde los años ochenta por su relación con accidentes e incidentes de aeronaves {cite:p}`bolgiani2020microbursts`.

### Cómo evoluciona una microrráfaga

Los estudios de campo que resume Bolgiani et al. fijan una caracterización: viento máximo de superficie de al menos 10 m/s, una distancia media de unos 3,1 km entre los puntos de máxima diferencia radial de velocidad y una profundidad media del flujo de salida de unos 700 m. El ciclo de vida típico es corto: la corriente descendente llega a la superficie en el minuto 0, el flujo de salida alcanza la intensidad de microrráfaga a los 2,5 minutos, su viento máximo a los 7 y deja de ser microrráfaga hacia los 15 minutos {cite:p}`bolgiani2020microbursts`. Esos valores vienen de campañas en Estados Unidos y no se han contrastado en el trópico.

En esas campañas, las microrráfagas se concentraron en la tarde: el 91 % ocurrió entre las 10:00 y las 21:00 horas locales, con un máximo entre las 14:00 y las 16:00 (34 % de los eventos) {cite:p}`bolgiani2020microbursts`. También suelen desarrollarse con poca cortante del viento {cite:p}`bolgiani2020microbursts`.

### Qué tan frecuentes son en Colombia

El Índice Municipal de Riesgo del DNP reúne los desastres de Colombia por fenómeno a partir de datos de la UNGRD y del IDEAM. Los vendavales son el 13 % del total {cite:p}`dnp2019imrd`:

| Fenómeno | Proporción de los desastres |
|---|---|
| Incendios forestales | 32 % |
| Inundaciones | 30 % |
| Movimientos en masa | 18 % |
| **Vendavales** | **13 %** |
| Avenidas torrenciales | 4 % |
| Varios | 2 % |
| Sequías | 1 % |

La tabla se lee de una infografía del DNP, que además indica que más del 88 % de los desastres del país es de origen hidrometeorológico {cite:p}`dnp2019imrd`. Es una proporción de **registros**, no de pérdidas, y los vendavales se subregistran, como se explica en la sección 2. Los primeros reportes de vendavales en el país datan de 1932 (Armenia, Quindío) y hay reportes en todos los departamentos; este dato se toma de la base de datos de emergencias de la UNGRD y queda por verificar.

### Daños típicos

Los reportes describen sobre todo daño a cubiertas, tejas, ventanas y muros de edificaciones, en especial las que no cumplen los códigos de construcción, además de caída de árboles, daño a cultivos, interrupciones del servicio eléctrico y desprendimiento de objetos. Es una descripción general, sin fuente oficial citada. El Atlas, al hablar de los efectos indirectos de los ciclones, menciona la caída de árboles, techos y postes del servicio público {cite:p}`ungrd2019atlas`: es el mismo repertorio de daños.

**Variable de intensidad.** La ráfaga máxima de 3 segundos a 10 m sobre el suelo, como en los ciclones ([](311_ciclones.md)) y en el flujo de tormentas de viento de CLIMAAX {cite:p}`climaax2025handbook`. Para un vendaval hay que añadir su **extensión** y su **duración**, que son muy pequeñas.

### Definición según los HIPs de UNDRR

Los perfiles de información de amenazas ([](../01_conceptos/16_hips_undrr.md)) que corresponden a este capítulo son:

| Código | Perfil (clúster) | Definición (traducción propia) |
|---|---|---|
| MH0101 | Ráfaga descendente (meteorológico e hidrológico, convectivo) | Corriente descendente violenta y dañina que llega a la superficie del suelo, asociada con una tormenta severa (OMM, 1992). Se clasifica por la extensión del flujo de salida: microrráfaga (menos de 4 km) y macrorráfaga (más de 4 km). |
| MH0304 | Turbonada (viento y presión) | Fenómeno atmosférico con una variación muy grande de la velocidad del viento: empieza de repente, dura del orden de minutos y disminuye de repente; suele acompañarse de aguacero o tormenta (OMM, 2018). |
| MH0302 | Derecho (viento y presión) | Bandas de tormentas de movimiento rápido con vientos destructivos, que pueden ser tan fuertes como los de huracanes o tornados; a diferencia de ellos, los vientos siguen líneas rectas (NOAA, 2019). |
| MH0103 | Tormenta eléctrica (convectivo) | Una o más descargas eléctricas repentinas, manifestadas por un destello de luz (relámpago) y un sonido agudo o retumbante (trueno) (OMM). |
| MH0305 | Tornado (viento y presión) | Columna de aire en rotación que se extiende desde la base de una nube cumuliforme y suele ser visible como embudo de condensación en contacto con el suelo, o con una nube de polvo o escombros circulante en el suelo (OMM, 2017). |

Fuente: {cite:p}`undrr2025hips`.

**Qué se incluye y por qué.**

- **No hay un perfil de «vendaval».** Es el hallazgo principal de esta revisión. El término colombiano es más amplio que cualquier perfil: la definición de la UNGRD no precisa el mecanismo (ver «El término en Colombia», arriba), y los HIPs describen por separado la ráfaga descendente, la turbonada, el derecho y el tornado.
- **Ráfaga descendente (MH0101): se incluye como el perfil más cercano.** Su clasificación por tamaño (microrráfaga y macrorráfaga) coincide con la que el capítulo toma de la literatura, y sus sinónimos incluyen «microburst» y «macroburst». El perfil agrega que los vientos pueden llegar a 67 m/s y que estos eventos suelen durar de 5 a 30 minutos.
- **Turbonada, derecho y tornado: se incluyen como perfiles relacionados.** La turbonada (cambio brusco del viento que dura minutos) describe bien lo que se siente en un vendaval; el derecho es una banda de tormentas de gran escala que no consta en las fuentes del libro para Colombia, y el tornado se distingue por su rotación (la ráfaga descendente no rota).
- **Tormenta eléctrica (MH0103)** se incluye solo como contexto: es la nube que produce estos vientos.
- **Escala de vientos.** El rango oficial colombiano de 50 a 80 km/h se solapa con el «viento fuerte» (*gale*, MH0303) de la OMM, de 62 a 74 km/h (fuerza 8 de Beaufort), que no se incluye como perfil propio. No debe confundirse con el *temporal* de la terminología colombiana, que es un vendaval con lluvia fuerte {cite:p}`ungrd2017terminologia`.
- **Cascadas.** Los HIPs registran la ráfaga descendente como causada por la tormenta eléctrica y la turbonada, y como causa de inundaciones repentinas y de fallas de infraestructura {cite:p}`undrr2025hips`.

## 2. Amenaza

### El problema de la escala

Las microrráfagas abarcan normalmente menos de 4 km y 20 minutos, lo que limita su estudio con modelos globales y de mesoescala por la resolución {cite:p}`bolgiani2020microbursts`. Un evento así cae casi siempre entre dos estaciones y entre dos pasos de un modelo de reanálisis. Para los vendavales como se definen en Colombia (impactos de hasta unos 10 km), la dificultad es la misma, y se suma la baja cultura de reporte y la dificultad de detectarlos, de modo que los inventarios están incompletos (esta última afirmación queda por documentar con una fuente).

### Enfoques posibles

| Enfoque | Qué produce | Datos que pide | Estado |
|---|---|---|---|
| **Inventario histórico y análisis espaciotemporal** | Dónde y cuándo se han reportado vendavales, estacionalidad y recurrencia por municipio o barrio | Registros de gestión del riesgo, base de la UNGRD, prensa | Criterio de método de este libro; por documentar con casos |
| **Huella de ráfaga por evento** | Mapa de la ráfaga máxima de un evento, para estimar daños | Reanálisis o simulación de ráfagas | Existe para Europa {cite:p}`climaax2025handbook`; no hay equivalente citado para Colombia |
| **Observación directa** | Ráfagas instantáneas y su estructura | Red densa de estaciones de superficie y radar Doppler | Campañas en Estados Unidos {cite:p}`bolgiani2020microbursts` |
| **Simulación numérica** | Reproducción de eventos individuales | Modelos de mesoescala a cientos de metros de resolución | Ver abajo |
| **Viento de diseño** | Velocidad básica para el cálculo de estructuras | Norma sismorresistente, título de cargas de viento | Por documentar |

### Qué muestran la observación y la simulación

El proyecto MIST (Alabama, 1986) usó 41 estaciones de superficie y 30 más de otra red, en un área de unos 40 por 30 km, junto con tres radares Doppler. Registró 62 microrráfagas, 33 identificadas por las estaciones y 29 por los radares fuera del área de la red {cite:p}`bolgiani2020microbursts`. Es decir, casi la mitad de los eventos ocurrió fuera del área de las estaciones y solo la detectó el radar: **la cobertura espacial de las estaciones limita lo que se ve**.

Simulaciones con el modelo WRF a 400 m y 3 minutos reproducen microrráfagas de alta reflectividad de acuerdo con las observaciones, aunque tienden a subestimar la intensidad de las variables, sobre todo la velocidad vertical del viento {cite:p}`bolgiani2020microbursts`. La configuración de la microfísica del modelo cambia mucho el resultado: un esquema produjo sobreestimaciones grandes del número de eventos {cite:p}`bolgiani2020microbursts`. Para el pronóstico a muy corto plazo existen algoritmos que usan los meteorólogos operativos, como índices de viento y de severidad de microrráfagas húmedas {cite:p}`bolgiani2020microbursts`.

### Contexto de la convección en Colombia

Dos estudios de la hoja de vigilancia describen las tormentas convectivas desde la lluvia, no desde el viento:

- En la Sabana de Bogotá, la convección tiene un máximo marcado a primeras horas de la tarde en las dos temporadas de lluvia. Los vientos del oeste de esa hora están presentes en el 78 % de los días de lluvia, pero solo en el 26 % de los días se desarrollan eventos convectivos, de modo que no sirven como predictor {cite:p}`casallas2021convective`.
- Simulaciones de 4 km con el modelo WRF reproducen bien la estacionalidad y el ciclo diurno de los sistemas convectivos de mesoescala en el noroeste de Sudamérica, pero simulan sistemas más pequeños y de menor duración y sobrestiman la lluvia {cite:p}`hernandez2025mcs`.

Ninguno trata ráfagas de viento. Se citan como contexto de lo que los modelos y las observaciones captan de la convección en el país.

## 3. Exposición

Los elementos expuestos son los que el viento daña según los reportes: cubiertas, tejas, ventanas y muros, árboles, cultivos, líneas eléctricas y objetos sueltos. En el flujo de CLIMAAX la exposición es un mapa de activos clasificados por tipo, cada uno con su daño máximo por metro cuadrado {cite:p}`climaax2025handbook`. Para una ciudad colombiana hay que construirlo con el inventario de edificaciones por tipo de cubierta ([](../04_vulnerabilidad/41_exposicion.md)), más la red eléctrica y el arbolado urbano. Se desconoce qué proporción de la infraestructura del país es vulnerable a las ráfagas de los vendavales.

## 4. Vulnerabilidad

CLIMAAX define la vulnerabilidad al viento como una colección de curvas que relacionan la ráfaga con el porcentaje de daño de cada clase de activo; las seis curvas del flujo son de Feuerstein et al. (2011), hechas para Europa central {cite:p}`climaax2025handbook`. No hay curvas colombianas citadas en este libro, y la forma de los techos, su fijación y su mantenimiento pesan más que la clase del edificio (afirmación de criterio de método). La función de daño se explica en [](../04_vulnerabilidad/42_funciones_dano.md).

Hay un estudio de la hoja sobre el efecto de vientos extremos en tanques de almacenamiento atmosférico {cite:p}`ramirez2020tanks`, que puede servir como ejemplo de vulnerabilidad de infraestructura industrial; se cita por título.

## 5. Riesgo

Con datos de eventos reales se puede calcular el riesgo de dos maneras:

- **Por evento.** Se multiplica la ráfaga del evento por la curva de daño y el valor máximo de cada activo, y se obtiene un mapa de daños, como en el flujo de CLIMAAX {cite:p}`climaax2025handbook`. Sirve para reconstruir un evento histórico o para un escenario.
- **Por recurrencia.** Con un inventario de eventos se puede zonificar la amenaza por frecuencia de reportes (barrio, vereda, municipio) y cruzarla con exposición y vulnerabilidad. Es un riesgo **relativo**, no una pérdida anual esperada.

No hay en las fuentes un conjunto de eventos estocásticos de vendavales, por lo que no se calcula la PAE de la forma de [](../02_metodologia/22_probabilista_pae.md). El tamaño pequeño de cada evento hace que el riesgo sea una **acumulación de muchos eventos locales** más que una pérdida grande en un solo evento. Esta lectura es criterio de método.

Los vendavales se conectan con otras amenazas: la tormenta que los produce puede dejar lluvia intensa y crecidas súbitas ([](305_inundacion.md)), y el daño a la red eléctrica interrumpe servicios que dependen de ella ([](../01_conceptos/15_cascada_compuestos.md)).

## 6. Clima

El flujo de CLIMAAX no incluye proyecciones futuras de viento {cite:p}`climaax2025handbook`, y los modelos con resolución de convección todavía tienen sesgos {cite:p}`hernandez2025mcs`. Las ráfagas descendentes dependen de condiciones termodinámicas (la diferencia de temperatura potencial equivalente entre la superficie y los niveles medios, el gradiente de temperatura y el contenido de agua) {cite:p}`bolgiani2020microbursts`; por eso, como criterio de método, cabe esperar que respondan al calentamiento y a la humedad. **No hay en las fuentes de este libro una estimación del efecto del cambio climático sobre los vendavales en Colombia.**

## 7. Datos y medidas

### Datos

| Fuente | Qué ofrece | Referencia |
|---|---|---|
| Registros de las oficinas de gestión del riesgo y base de emergencias de la UNGRD | Fecha, lugar y daños de cada evento | {cite:p}`dnp2019imrd` (usa datos de la UNGRD) |
| Inventarios históricos de desastres (por ejemplo, DesInventar) | Reportes por municipio y fecha | Por documentar |
| Estaciones del IDEAM y de corporaciones regionales | Velocidad máxima y ráfaga del viento | Por documentar |
| Radar meteorológico | Estructura de la celda y señal de la ráfaga | {cite:p}`bolgiani2020microbursts` |
| Huellas de ráfaga | Mapas de ráfaga máxima por evento; solo para Europa | {cite:p}`climaax2025handbook` |

### Incertidumbres

- **Subregistro.** El inventario depende de la cultura de reporte y de la cobertura de la prensa y las oficinas locales.
- **Escala.** Eventos de menos de 4 km y 20 minutos escapan a las estaciones y a los reanálisis {cite:p}`bolgiani2020microbursts`.
- **Definición.** La definición oficial no precisa el mecanismo {cite:p}`ungrd2017terminologia`.
- **Curvas de daño.** No hay curvas colombianas por tipo de cubierta.

### Medidas según la Ley 1523

Las medidas siguientes son un criterio de método de este libro, derivado de la naturaleza del fenómeno; no vienen de una guía oficial citada.

| Proceso | Medida |
|---|---|
| Conocimiento | Protocolo de reporte para que cada evento quede con fecha, lugar y daño; red de observación de alta frecuencia y uso de radar; reconstrucción de eventos recientes |
| Reducción: prevención | Usar la zonificación por recurrencia en el ordenamiento y en los permisos de construcción |
| Reducción: mitigación | Fijación y mantenimiento de cubiertas, canales, poda del arbolado, protección de cultivos |
| Protección financiera | Seguros para vivienda y cultivos |
| Manejo | Alertas de muy corto plazo basadas en radar y en los algoritmos de pronóstico a muy corto plazo; difusión a la población |

## Pendiente

- Consultar la entrada de Wakimoto (2015) sobre microrráfagas (*Encyclopedia of Atmospheric Sciences*), que es de acceso cerrado y no se consultó.
- Verificar en EM-DAT las cifras de las tormentas convectivas y precisar qué tipos de evento incluye.
- Documentar el título de cargas de viento de la NSR-10, su mapa de amenaza eólica y la modificación de 2021, y el atlas de viento del IDEAM y la UPME.
- Reunir curvas de daño por tipo de cubierta para Colombia.
- Hacer un caso colombiano: un inventario sistemático de vendavales de un municipio, con su fuente, método y periodo, y su zonificación por recurrencia.
- Contrastar en el trópico andino los patrones de ciclo diurno y ambiente termodinámico que la literatura describe para Estados Unidos.
- Distinguir cuándo un viento fuerte es un vendaval de origen convectivo y cuándo es efecto de un ciclón o de una onda tropical.
