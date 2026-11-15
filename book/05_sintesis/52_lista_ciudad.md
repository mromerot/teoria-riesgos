---
title: Lista de verificación para una ciudad nueva
---

# Lista de verificación para una ciudad nueva

Esta lista convierte el libro en un procedimiento de trabajo. Sigue el flujo propuesto en [](../02_metodologia/21_flujo_general.md) y dice, para cada paso, qué decidir, qué producir y qué capítulo consultar. Cada ciudad debe dejar constancia de lo que no pudo hacer.

## 1. Alcance

- [ ] Delimitar el área de estudio y la escala (ciudad, localidad, barrio, manzana).
- [ ] Escribir las decisiones que el análisis debe apoyar y quién las toma.
- [ ] Identificar actores y responsables, y los instrumentos donde entrará el resultado ([](../01_conceptos/13_marco_colombia.md)).
- [ ] Fijar el horizonte temporal y los escenarios ([](../01_conceptos/12_riesgo_climatico.md)).

**Producto:** una ficha de alcance de una página.

## 2. Inventario de amenazas

- [ ] Para cada amenaza de la [parte 3](../03_amenazas/index.md), responder: ¿aplica a esta ciudad? ¿Hay eventos históricos?
- [ ] Anotar la base disponible: metodología oficial, estudios locales, solo datos globales.
- [ ] Marcar las cascadas relevantes ([](51_sintesis_multiamenaza.md)).

**Producto:** tabla de amenazas con su respaldo y su prioridad inicial.

## 3. Datos

- [ ] Exposición: población, edificaciones, líneas vitales y suelo ([](../04_vulnerabilidad/41_exposicion.md)).
- [ ] Chequear la completitud de las huellas de edificios contra la superficie construida de GHSL, con más de una fuente de huellas, **antes** de calcular pérdidas.
- [ ] Leer los términos de uso de cada fuente. Los datos por edificio de fuentes con términos restrictivos no se versionan ni se publican (`data/restringido/`).
- [ ] Población: declarar fuente y año, y contrastar el total con cifras oficiales (el censo cuenta personas; el DANE publica además una cifra ajustada).
- [ ] Vulnerabilidad física: función de daño por tipo de elemento y amenaza ([](../04_vulnerabilidad/42_funciones_dano.md)).
- [ ] Vulnerabilidad social y capacidades ([](../04_vulnerabilidad/43_vulnerabilidad_social.md)).
- [ ] Amenaza: mapas oficiales (SGC, IDEAM, autoridades locales) o modelación propia. Si se usa un proxy de tamizaje, contrastarlo con el mapa oficial donde exista y anotar qué cubre y qué no ([](../03_amenazas/305_inundacion.md)).
- [ ] Registrar para cada insumo la fuente, la fecha, la resolución y el nivel de respaldo: local, nacional o global.

**Producto:** un catálogo de datos con niveles de respaldo.

## 4. Línea base

- [ ] Por amenaza, calcular el riesgo actual con el método de su capítulo.
- [ ] Para amenazas probabilistas, obtener la curva de excedencia, la PAE y la pérdida con periodos de retorno de referencia ([](../02_metodologia/22_probabilista_pae.md)).
- [ ] Para el resto, calcular la exposición a clases o la zonificación relativa.
- [ ] Documentar las incertidumbres de cada resultado.

**Producto:** un cuaderno o capítulo por amenaza con resultados reproducibles.

## 5. Escenarios

- [ ] Elegir los escenarios y periodos ([](../02_metodologia/23_escenarios_climaticos.md)) y justificarlos.
- [ ] Decidir si la exposición y la vulnerabilidad cambian o se mantienen fijas, y decirlo en el informe.
- [ ] Repetir el cálculo de las amenazas sensibles al clima.

**Producto:** tabla de resultados por escenario y periodo, junto con el caso histórico.

## 6. Síntesis y medidas

- [ ] Combinar la PAE con las reglas del capítulo anterior; no sumar PML ni mezclar índices con dinero.
- [ ] Priorizar con las cuatro preguntas de [](51_sintesis_multiamenaza.md).
- [ ] Proponer medidas por amenaza y proceso de la Ley 1523: conocimiento, reducción y manejo.
- [ ] Declarar las cascadas no cuantificadas y los capítulos provisionales usados.

**Producto:** síntesis multiamenaza y plan de medidas.

## 7. Seguimiento

- [ ] Guardar versión de datos, inventario, escenarios y fecha.
- [ ] Dejar los resultados en el formato del contrato de salida (ver abajo) y pasar el validador.
- [ ] Definir cuándo se repite el análisis y con qué indicadores se sigue.
- [ ] Anotar lo que la ciudad enseñó sobre el libro, para llevarlo de vuelta (R5).

## Contrato de salida

Cada repositorio de ciudad guarda sus resultados con la misma forma, para que se puedan auditar, repetir y comparar. La plantilla trae la especificación (`resultados/LEEME.md`), una tabla de parámetros (`resultados/parametros.csv`), los datos de la corrida (`config/corrida.yaml`) y un validador (`scripts/verificar_salida.py`).

- **Parámetros con fuente.** Cada parámetro lleva valor, unidad, fuente, nivel (local, nacional, global o supuesto), fecha de verificación y estado (`verificado`, `por_verificar`, `por_defecto` o `supuesto`). Un parámetro `por_defecto` no se cita en la síntesis.
- **Obligatorios.** Versión del libro, tipo de modelo de elevación y si hubo respaldo, fuente y completitud de las huellas, licencia de la fuente, población con fuente y año, fuente y rango del costo, curva de daño, origen de los escenarios, periodo de retorno mínimo y qué excluye la PAE.
- **Validador.** Da error si falta un parámetro o una fuente, y avisos si la completitud es menor a 80 % o mayor a 120 %, si se usó un modelo de elevación de respaldo o si una amenaza no está calibrada. Con `--estricto`, los parámetros por defecto también son error.
- **Tablas por paso.** `resultados/03_datos/`, `04_linea_base/<amenaza>/`, `05_escenarios/` y `06_sintesis/`, con las columnas mínimas que fija el contrato. Las corridas anteriores se archivan en `resultados/archivo/`.

Se probó con el piloto de inundación de Cali. Esa prueba cambió tres cosas del contrato: los parámetros de OpenStreetMap pasaron a ser de «huellas», porque la fuente puede ser el catastro; se añadieron la licencia de la fuente y la carpeta `data/restringido/`; y se añadió un parámetro para registrar el contraste con mapas oficiales.

## Aviso sobre capítulos provisionales

Si la ciudad tiene erosión costera, erosión fluvial, calor o vendavales como amenaza principal, los capítulos respectivos son provisionales y se apoyan en poca literatura de referencia. En ese caso, el análisis debe empezar con una búsqueda de metodologías específicas y citar la fuente de cada decisión.

## Pendiente

- Convertir esta lista en una plantilla de repositorio por ciudad y en un comando que la cree.
- Contrastarla con los análisis ya hechos en SIDRo y Leticia para ajustar lo que falte.
- Probar el contrato completo con una segunda ciudad (Sincelejo) y con un análisis que no sea de inundación.
- Fijar la versión del libro (etiqueta y DOI) que los análisis de ciudad deben citar (R4).
