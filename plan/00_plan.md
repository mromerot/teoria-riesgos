# Plan del libro «Teoría y métodos de análisis de riesgos de desastres y climáticos»

Última actualización: 2026-11-02. Estado vivo en `plan/01_estado.md`.

## 1. Objetivo

1. Hacer análisis de riesgos de desastres y climáticos para **ciudades de Colombia**. El piloto fue Leticia (EVA); le siguieron SIDRo (barrio Los Rosales, Bogotá) y Sincelejo (en curso).
2. Los pilotos mostraron que hace falta **un libro con la teoría y los métodos** que sustente esos análisis.
3. Ese libro **se invoca cada vez** que se quiere analizar una ciudad: es la referencia común, no se reescribe por ciudad.
4. Se construye **paso a paso e iterativamente**, con estos modelos y fuentes:
   - marcos: CLIMAAX (proceso y flujos por amenaza), CCDR-tools (cálculo amenaza–exposición–vulnerabilidad), CLIMADA (impacto y medidas);
   - la colección *Investigaciones en gestión del riesgo de desastres en Colombia* (2021, 2023, 2025);
   - PreventionWeb de UNDRR (conceptos y terminología);
   - fuentes nacionales en PDF (Atlas 2019, DNP, Banco Mundial, Expertise E2050 y otras);
   - la tabla de artículos colombianos (998 registros; 317 PDFs en Drive).
5. El objetivo es ir construyendo todo de forma iterativa.

## 2. Qué implica «invocar el libro»

```
Pedido: «analiza el riesgo de <ciudad>»
   → skill /nueva-ciudad crea el repositorio de la ciudad (plantilla)
   → lista de verificación de 7 pasos (libro, parte 5)
   → por cada amenaza que aplica: capítulo de la parte 3, sección 7 (datos y medidas)
   → exposición, funciones de daño y vulnerabilidad social (parte 4)
   → resultados en el repositorio de la ciudad, con citas al libro (con su versión)
   → lo que faltó o falló vuelve al libro como corrección o capítulo nuevo
```

De ahí salen cinco requisitos para el libro:

| Requisito | Qué significa |
|---|---|
| R1. Interfaz estable | Molde de siete puntos, lista de verificación y plantilla no cambian de forma caprichosa; si cambian, se avisa. |
| R2. Capítulos accionables | La sección 7 de cada amenaza dice qué datos pedir, de qué nivel (local, nacional, global) y qué medidas considerar. |
| R3. Trazabilidad | Cada cifra o afirmación lleva su fuente y su estado de lectura (completa, resumen, solo título). |
| R4. Versionado | Cada análisis de ciudad cita una versión del libro (etiqueta y DOI), y la versión no cambia por debajo. |
| R5. Retroalimentación | Cada ciudad aporta lo aprendido; hay un lugar donde registrarlo. |

**Consecuencia para los libros de ciudad.** Los tres pilotos repiten una parte de «conceptos». Con este libro esa parte sobra en las ciudades: se enlaza. Cada libro de ciudad se reduce a alcance, datos, análisis por amenaza, síntesis y medidas.

## 3. Fuentes de referencia y su papel

| Fuente | Papel en el libro | Uso hasta ahora | Pendiente |
|---|---|---|---|
| CLIMAAX Handbook | Proceso de 5 pasos y flujos por amenaza | Alto | Guía de alcance y exploración; paso de riesgos clave |
| CCDR-tools | Cálculo y combinación espacial; EAI con cotas | Alto | Indicadores, conjuntos de datos por amenaza |
| CLIMADA | Impacto por evento, métricas, comparación de medidas | Parcial (solo la clase `Impact`) | Exposures, Hazard, ImpactFunc, Engine (adaptación y costo-beneficio) |
| *Investigaciones GRD de Colombia* | Casos y métodos colombianos | Parcial (2021: cap. 1, 2, 3, 10, 12; 2023: cap. 2 y 5) | 2025 completo y el resto de 2021 y 2023 |
| PreventionWeb (UNDRR) | Conceptos y terminología | Parcial (cascada, compuesto y 3 publicaciones multiamenaza) | Riesgo sistémico, intensivo y extensivo, directo e indirecto, resiliencia, capacidad, perfiles de amenazas (HIPs), GAR |
| PDFs nacionales (`referencia_colombia`, 9) | Marco y métodos de Colombia | Atlas 2019, DNP, Banco Mundial | Expertise E2050 (3), Informe de ciudades, Perfil de país, Modelación y adaptación |
| Libros de referencia (`libros_referencia`, 10) | Teoría de base por tema | Solo Chen et al. 2016 | Guía PMGRD, revisión de métodos y software, Baker (sismo), *Landslide Handbook*, GIZ *Climate Risk Sourcebook*, compuestos, atribución, adaptación, *Disaster Risk* (Routledge) |
| Tabla de artículos (998) y carpeta de PDFs (317) | Literatura colombiana por amenaza | ~50 citados por título o resumen | Lectura por niveles; ver plan de lectura |

## 4. Alcance de amenazas

- **En el libro (12):** sismo, volcanes, tsunami, movimientos en masa, inundación, erosión costera, erosión fluvial, sequía, calor, incendios forestales, ciclones tropicales, vendavales.
- **Que los pilotos usaron y el libro no tiene:** **dengue y salud** (Leticia, Sincelejo), **incendio urbano** (SIDRo), y **seguridad hídrica** (Sincelejo; puede cubrirse desde sequía).
- **Candidatas de la tabla de artículos, sin decidir:** contaminación del aire, perturbación geomagnética, accidentes tecnológicos por desastre natural (NaTech), licuefacción como capítulo propio.
- Decisión pendiente (ver sección 8).

## 5. Madurez de un capítulo

| Nivel | Nombre | Criterio |
|---|---|---|
| L0 | Esqueleto | Estructura y «Pendiente»; sin texto sustantivo |
| L1 | Borrador con fuentes | Escrito con fuentes primarias identificadas; hay afirmaciones por título o resumen, marcadas |
| L2 | Verificado | Toda cifra y toda afirmación sustantiva se trazan a una fuente leída; el «Pendiente» solo tiene mejoras |
| L3 | Validado con una ciudad | Se usó en un análisis real y se incorporó lo que faltó |

Un capítulo **provisional** es L1 con una cobertura de fuentes baja (la advertencia va al inicio).

## 6. Ciclo de iteración (una rebanada por sesión)

1. **Elegir la rebanada:** un capítulo, o una fuente, o un conjunto de artículos. Anotarla en `01_estado.md`.
2. **Leer:** si son artículos, hacer una ficha por artículo (sitio, método, datos, cifras con página, límites).
3. **Escribir o actualizar** el capítulo según el molde.
4. **Verificar:** cada cifra con su fuente; lo no verificado se marca «por verificar».
5. **Construir y revisar:** `myst build --html` sin avisos; revisar el resultado en el navegador.
6. **Registrar:** actualizar `01_estado.md` (nivel, fecha, pendientes) y hacer el commit.
7. **Desplegar** cuando se pida («despliega los cambios»: construir, commit, push y verificar la Action).

## 7. Fases

| Fase | Objetivo | Salidas | Criterio de terminado |
|---|---|---|---|
| **F0. Andamiaje** (hecha) | Estructura, 5 partes, 12 amenazas en L0–L1, plantilla, skill, diseño, despliegue | Sitio en línea, repositorio, plantilla | Hecho; falta desplegar el último commit |
| **F1. Orden y base** | Dejar el proyecto trazable | `plan/`, `CLAUDE.md`, `CITATION.cff`, licencia, inventario de fuentes, lista de cifras por verificar | Plan aprobado; inventario completo |
| **F2. Literatura colombiana** | Convertir los artículos en capítulos L2 | Copia local de PDFs, emparejamiento con la tabla, fichas, capítulos actualizados | Todos los artículos nivel A leídos; cobertura por capítulo registrada |
| **F3. Fuentes institucionales** | Agotar las fuentes de referencia | Capítulos y glosario ampliados con PreventionWeb, *Investigaciones GRD* 2025, E2050, informe de ciudades, Guía PMGRD, CLIMADA completo | Matriz de fuentes (sección 3) sin celdas «pendiente» críticas |
| **F4. Brechas de cobertura** | Cubrir lo que los pilotos usaron y el libro no | Capítulos de salud (dengue) e incendio urbano, si se decide; ajustes de alcance | Cada amenaza de los tres pilotos tiene capítulo o está descartada con motivo |
| **F5. Validación con ciudad real** | Probar la plantilla y el skill | Una ciudad creada con `/nueva-ciudad`; lista de lo que faltó; correcciones al libro | Un análisis de ciudad usa el libro sin consultar los pilotos; capítulos usados pasan a L3 |
| **F6. Publicación y versionado** | Citable y estable | Etiquetas, DOI (Zenodo), página en tu sitio actualizada, ciudades con versión fijada | Versión 1.0 publicada y citada por al menos un libro de ciudad |
| **Transversal** | Verificación de cifras pendientes, revisión del marco legal (Ley 1523), revisión de calidad | Lista cerrada en `01_estado.md` | Sin cifras «por verificar» en capítulos L2 |

Las fases F2 y F3 se pueden intercalar por capítulo en lugar de hacerlas completas una detrás de otra: tomar un capítulo y agotar sus fuentes (artículos, libros, PreventionWeb) antes de pasar al siguiente. El orden de capítulos propuesto es: sismo, movimientos en masa, inundación, erosión costera y fluvial, calor, sequía e incendios, ciclones y vendavales, tsunami y volcanes, y por último la parte 4 y las partes 1 y 2.

## 8. Decisiones abiertas

| Decisión | Opciones | Recomendación |
|---|---|---|
| ¿Se construye `eva-core` (paquete compartido)? | Sí ya; después de más ciudades; nunca | **Después.** Ya hay tres pilotos con código propio: extraer lo común (regla de tres) cuando se cierre F5, no antes. El libro define el método; el código vive en las ciudades. |
| ¿Dónde viven los cuadernos de ejemplo? | En el libro; en un repositorio aparte | **En el libro**, mientras sean didácticos y de poco peso. Los de análisis de ciudad viven en la ciudad. |
| ¿PDFs locales? | Leer de Drive; copiar a una carpeta local | **Copiar** a una carpeta ignorada por git. Ni los PDFs ni su texto ni las fichas se publican. |
| Profundidad de lectura | Todo a fondo; por niveles | **Por niveles A, B y C** (A: lectura completa de unos 60 a 80; B: lectura dirigida; C: solo índice). |
| ¿Subagentes para leer en paralelo? | Sí; no | **No por defecto**; solo si lo pides. |
| Alcance de amenazas | Solo las 12; añadir salud e incendio urbano; añadir más | **Añadir salud (dengue) e incendio urbano** en F4, porque los pilotos ya los usan. Las demás, solo si aparece una ciudad que las necesite. |
| Idioma y licencia | Español, CC BY 4.0 | Mantener. |

## 9. Riesgos del proyecto

| Riesgo | Mitigación |
|---|---|
| El libro crece sin cerrarse | Ciclo con una rebanada por sesión; niveles de madurez; el estado manda |
| Afirmaciones sin sustento | Estado de lectura por cita; «por verificar» visible; no citar borradores propios |
| Derechos de autor | No publicar PDFs, texto extraído ni fichas; parafrasear; figuras de terceros solo enlazadas |
| Deriva entre ciudades y libro | Plantilla con versión fijada; retroalimentación registrada (R5) |
| Cuadernos que dejan de correr | Fuentes de cuadernos en `scripts/cuadernos/`; datos descargados en caché ignorada; reconstrucción con un comando |
| Fuentes bloqueadas (p. ej. PreventionWeb, Wiley) | Leer desde el navegador cuando se pueda; no eludir verificaciones de bots |

## 10. Reglas fijas del proyecto

- Idioma: español. Citas con `{cite:p}` contra `references.bib`; lo no verificado se marca «por verificar».
- No inventar URLs ni datos; los datos inventados van rotulados como tales.
- No citar borradores propios no publicados.
- No hacer commit ni push sin que se pida; «despliega los cambios» significa construir, commit, push y verificar la Action.
- Una rebanada por sesión; al cerrarla, actualizar `plan/01_estado.md`.
