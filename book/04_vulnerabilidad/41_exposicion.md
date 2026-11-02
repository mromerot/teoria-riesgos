---
title: Exposición
---

# Exposición

La exposición es el inventario de lo que puede perderse. Su calidad fija el techo de precisión del análisis: una amenaza bien modelada sobre un inventario grueso da una pérdida gruesa.

## 1. Qué es

La Ley 1523 define la exposición como la presencia de personas, medios de subsistencia, servicios ambientales y recursos económicos y sociales, bienes culturales e infraestructura que, por su localización, pueden ser afectados por una amenaza {cite:p}`ley1523,dnp2019imrd`. CCDR-tools la formula como los capitales físicos, humanos y productivos que podrían perderse, y señala que se mide como número de personas o tipos de activos en el área, para combinarlos luego con la vulnerabilidad de cada elemento {cite:p}`ccdr2025tools`.

El Atlas añade que la exposición se define por la relación entre un activo y la amenaza: están expuestos los activos que pueden ser afectados por al menos una amenaza. Por eso el análisis agrupa los elementos en portafolios y evalúa el riesgo por sectores {cite:p}`ungrd2019atlas`.

## 2. Cómo se construye el inventario

El Atlas describe dos etapas: **identificación** (qué activos pueden ser afectados) y **caracterización** (qué atributos determinan su daño, como tipo estructural, uso y valor) {cite:p}`ungrd2019atlas`. La resolución depende de la escala:

| Escala | Unidad de exposición | Fuente de la regla |
|---|---|---|
| Nacional y departamental | Proxy del inventario, a partir de población, indicadores económicos y distribución de tipos constructivos | {cite:p}`ungrd2019atlas` |
| Urbana y local | Elemento por elemento (edificio o predio), cada uno identificado y caracterizado | {cite:p}`ungrd2019atlas` |

Cuando no hay información detallada, el Atlas construye un **modelo proxy**: parte de información oficial demográfica, económica y social subnacional, y la combina con estadísticas de tipos constructivos para estimar el inventario {cite:p}`ungrd2019atlas`. Para el análisis departamental usó la base de exposición del GAR15, que cubre edificaciones públicas y privadas, urbanas y rurales, y **no incluye infraestructura ni agricultura** {cite:p}`ungrd2019atlas`.

```{important}
Para una ciudad, el proxy departamental es insuficiente. El Atlas mismo indica que a escala local es deseable la resolución edificio por edificio, y que algunas amenazas puntuales (por ejemplo, un deslizamiento) no admiten evaluaciones gruesas {cite:p}`ungrd2019atlas`. Los casos locales del Atlas lo ilustran: en Medellín se levantó la información de exposición de las edificaciones de la ciudad, y en San Andrés y Providencia se partió del marco geoestadístico del DANE, se fijó el valor de reposición por manzana y se asignó la función de vulnerabilidad de cada tipo estructural {cite:p}`ungrd2019atlas`.
```

## 3. Categorías de exposición

CCDR-tools trabaja con categorías estándar, entre ellas población, área construida y agricultura. Los datos se guardan como rásteres de presencia (1/0) o de cantidad (conteo, densidad), y admiten también polígonos de huellas de edificios o líneas para redes de distribución {cite:p}`ccdr2025tools`. En CLIMADA, la exposición es una tabla geográfica con una columna de valor (monetario, número de personas u otro), a la que se asigna la función de impacto y los puntos de la amenaza {cite:p}`climada2025docs`.

| Categoría | Qué se cuenta | Observación |
|---|---|---|
| Población | Personas por celda o por manzana | Define pérdida de vidas y afectados |
| Edificaciones | Número, área o valor, por tipo estructural | Es el insumo central de sismo, viento e inundación |
| Infraestructura y líneas vitales | Vías, redes, salud, educación | CLIMAAX usa OpenStreetMap para vías, instalaciones y torres {cite:p}`climaax2025handbook` |
| Suelo y agricultura | Cobertura, cultivos, ganado | Es la exposición de sequía e incendios |
| Ecosistemas | Áreas protegidas, manglar, páramo | Se mide en área o valor de restauración |

## 4. Fuentes de datos

CLIMAAX y CCDR-tools coinciden en un conjunto de fuentes globales que sirven como punto de partida {cite:p}`climaax2025handbook,ccdr2025tools`:

| Fuente | Qué ofrece | Resolución y cobertura citadas |
|---|---|---|
| GHS-POP (GHSL) | Población distribuida con el área construida | 100 m y 1 km, 1975–2030 cada cinco años {cite:p}`climaax2025handbook` |
| WorldPop | Población por modelo de bosque aleatorio | 3 y 30 segundos de arco, 2000–2020 {cite:p}`climaax2025handbook` |
| GPW v4 | Población sin modelar, a partir de censos | 30 segundos de arco {cite:p}`climaax2025handbook` |
| GHS-BUILT | Área y volumen construidos, altura de edificios | 10 m a 1 km {cite:p}`climaax2025handbook` |
| OpenStreetMap | Huellas de edificios, instalaciones, vías | Vectorial, actualizada por voluntarios {cite:p}`climaax2025handbook` |
| SPAM y GLW | Cultivos y ganado | Mallas de 5 minutos de arco, 2010 {cite:p}`climaax2025handbook` |
| LitPop, BlackMarble, OSM (CLIMADA) | Módulos de exposición para distribuir valor de activos | Módulos de exposición de CLIMADA {cite:p}`climada2025docs` |

Para Colombia se suman fuentes nacionales. El Índice Municipal de Riesgo usa el Censo Nacional de Población y Vivienda 2018 (DANE), el Mapa Nacional de Coberturas de la Tierra (IDEAM) y la densidad de semovientes del ICA {cite:p}`dnp2019imrd`. Un análisis urbano debe añadir el catastro, el censo de edificaciones y los inventarios sectoriales, cuya disponibilidad se documenta por ciudad.

### Qué enseña el caso de las ciudades latinoamericanas

Un análisis de la exposición a inundaciones en 363 ciudades latinoamericanas encontró alta heterogeneidad entre ciudades {cite:p}`xu2026latam`. Como criterio de método, esto desaconseja transferir exposiciones de una ciudad a otra y justifica un inventario propio.

## 5. Valor expuesto

Para pérdidas económicas, a cada elemento se le asigna un valor. El Atlas reporta el valor expuesto por departamento en millones de pesos, y la pérdida anual esperada relativa al valor expuesto en ‰ {cite:p}`ungrd2019atlas`. Tres decisiones deben quedar escritas en cada análisis:

1. Si el valor es de reposición, comercial o de uso.
2. El año y la moneda de referencia.
3. Si se incluye el contenido de las edificaciones.

## 6. Exposición futura

Los escenarios de cambio climático ([](../02_metodologia/23_escenarios_climaticos.md)) cambian la amenaza, pero la exposición también crece. CLIMAAX recoge proyecciones de población y de PIB alineadas con las trayectorias socioeconómicas compartidas (SSP) {cite:p}`climaax2025handbook,riahi2017ssp`. Si se omite el crecimiento de lo expuesto, la comparación entre el clima actual y el futuro atribuye todo el cambio a la amenaza.

## Incertidumbres

- Las celdas de población de los modelos globales redistribuyen censos y pueden concentrar o dispersar población donde no hay construcción detectada {cite:p}`climaax2025handbook`.
- OpenStreetMap depende de la cobertura voluntaria, que varía entre barrios formales e informales.
- El inventario de tipo estructural suele ser la parte más débil; por eso aparece con frecuencia como proxy {cite:p}`ungrd2019atlas`.

## Pendiente

- Documentar la disponibilidad real de catastro y censo de edificaciones en las ciudades ya analizadas.
- Revisar los módulos de exposición de CLIMADA (LitPop, OSM) contra su documentación completa.
- Definir una plantilla única de inventario de exposición para la ciudad nueva.
