# Estado del proyecto «Teoría y métodos de análisis de riesgos»

Última actualización: 2026-11-02.
**Regla:** al cerrar una rebanada, actualizar nivel, fecha y pendientes aquí. El plan está en `plan/00_plan.md`.

## Fases

- [x] **F0. Andamiaje**: 5 partes, 12 amenazas, glosario, plantilla de ciudad, skill `/nueva-ciudad`, diseño con la identidad de EVA, sitio en https://mromerot.github.io/teoria-riesgos/, enlaces desde `mromerot.github.io` y `/web`.
  - [ ] Desplegar el último commit local (diseño, vendavales, cuadernos 313 a 315).
- [ ] **F1. Orden y base**
  - [x] `plan/00_plan.md` y `plan/01_estado.md` (2026-11-02)
  - [ ] `CLAUDE.md` del proyecto (escrito el 2026-11-02, falta aprobación)
  - [ ] `CITATION.cff` y `LICENSE`
  - [ ] Inventario de fuentes (matriz de la sección 3 del plan) con su estado de lectura
  - [ ] Cerrar la lista de cifras por verificar (abajo)
- [ ] **F2. Literatura colombiana**: esperando tres decisiones (copia local de PDFs, niveles A, B y C, subagentes).
- [ ] **F3. Fuentes institucionales**, incluido el barrido de `mromerot.github.io/web/grd/`
- [ ] **F4. Brechas de cobertura** (salud y dengue, incendio urbano)
- [ ] **F5. Validación con ciudad real**
- [ ] **F6. Publicación y versionado**

## Madurez de los capítulos

Ninguno ha llegado a L2 (verificado) ni a L3 (validado con una ciudad).

| Parte | Capítulo | Nivel | Base principal | Pendiente clave |
|---|---|---|---|---|
| 1 | Marco conceptual del riesgo | L1 | CLIMAAX, CCDR-tools, Atlas, Ley 1523 | Contrastar definiciones con PreventionWeb |
| 1 | Riesgo climático | L1 | CCDR-tools, CMIP6 | Tabla de cambios esperados contra el AR6; proyecciones del IDEAM |
| 1 | Marco normativo de Colombia | L1 | Atlas, Banco Mundial 2012 | Artículos de la Ley 1523 sin contrastar con el texto oficial |
| 1 | Riesgos multiamenaza | L1 (cerca de L2) | Chen 2016, White 2025, Tiggeloven 2026, Ferrario 2026 (leídos completos) | Lo que esos artículos citan; literatura colombiana |
| 1 | HIPs de UNDRR | L1 | Página y API de PreventionWeb (CC BY 4.0) | Informe técnico y publicación 2025 sin leer; licencia de la infografía |
| 1 | Cascadas y compuestos | L1 | PreventionWeb (resúmenes), Bevacqua 2021, editorial npj | Leer los estudios que PreventionWeb resume; Awah 2024 completo |
| 2 | Flujo general | L1 | CLIMAAX, CCDR-tools, CLIMADA | Módulos de CLIMADA; guía de alcance de CLIMAAX |
| 2 | Probabilista y PAE | L1 | CCDR-tools, CLIMADA | Verificar con la documentación completa de CLIMADA |
| 2 | Escenarios climáticos | L1 | CLIMAAX, CCDR-tools | Reducción de escala para Colombia |
| 3 | Sismo | L1 | Atlas, literatura nacional | Cifra de población en zonas de amenaza |
| 3 | Volcanes | L1 | Atlas | Literatura reciente |
| 3 | Tsunami | L1 | Atlas, caso de Guapi | Literatura reciente |
| 3 | Movimientos en masa | L1 | Atlas, SGC, literatura nacional | Artículos leídos completos |
| 3 | Inundación | L1 | Atlas, CLIMAAX | Artículos leídos completos |
| 3 | Erosión costera | L1 **provisional** | Hoja de vigilancia | Metodología de referencia; Pacífico |
| 3 | Erosión fluvial | L1 **provisional** | Hoja de vigilancia | Metodología de referencia; puentes |
| 3 | Sequía | L1 | Atlas, CLIMAAX | Artículos leídos completos |
| 3 | Olas de calor | L1 **provisional** | CLIMAAX, CCDR-tools | Definición para Colombia; isla de calor urbana |
| 3 | Incendios forestales | L1 | Atlas, CLIMAAX | Datos de área quemada recientes |
| 3 | Ciclones tropicales | L1 | Atlas, IBTrACS (datos reales) | 80 % de muertes en tierra sin fuente primaria |
| 3 | Vendavales | L1 **provisional** | DNP, Bolgiani 2020, CLIMAAX | Definición UNGRD 2017, EM-DAT, NSR-10, caso colombiano |
| 4 | Exposición | L1 | Atlas, CLIMAAX, CCDR-tools | Plantilla de inventario |
| 4 | Funciones de daño | L1 | Atlas, CLIMAAX | Estudios de vulnerabilidad física leídos |
| 4 | Vulnerabilidad social | L1 | CCDR-tools, DNP, Atlas | Fórmula del DNP, ecuación de Moncho |
| 5 | Síntesis multiamenaza | L1 | Atlas, Chen 2016 | Guía del paso de riesgos clave de CLIMAAX |
| 5 | Lista de verificación | L1 | El libro, SIDRo y EVA | Probarla con una ciudad real |
| R | Glosario | L1 | Ver cada término | Ampliar con PreventionWeb |

### Cuadernos (parte 3)

| Cuaderno | Datos | Estado |
|---|---|---|
| 313 Análisis multiamenaza | Inventados | Ejecutado, con salidas guardadas |
| 314 Riesgos en cascada | Inventados | Ejecutado, con salidas guardadas |
| 315 Trayectorias de ciclones | Reales (IBTrACS) | Ejecutado; descarga de 58 MB en caché local |

## Cobertura de las fuentes de referencia

Ver la tabla de la sección 3 de `plan/00_plan.md`. Resumen de lo que falta: el barrido de la sección GRD de tu sitio personal (ver el plan), CLIMADA más allá de `Impact`, *Investigaciones GRD* 2025, los conceptos clave de PreventionWeb, los 3 documentos E2050, el informe de ciudades, el perfil de país, la Guía PMGRD y los otros 9 libros de `libros_referencia`, y 317 PDFs de artículos.

## Pilotos y brechas

| Piloto | Amenazas que analizó | Falta en el libro |
|---|---|---|
| Leticia (EVA) | Inundación, sequía, erosión, calor, incendios, lluvias y vendavales, dengue | Dengue y salud |
| SIDRo (Los Rosales) | Sismo, incendio forestal, movimientos en masa, incendio urbano, calor | Incendio urbano |
| Sincelejo (en curso) | Arroyos y drenaje, seguridad hídrica, laderas, salud, calor, fuego, tormentas, sismo | Salud; seguridad hídrica puede cubrirse con sequía |

## Cifras y datos por verificar

- 80 % de muertes por huracanes donde tocan tierra (Atlas; sin fuente primaria en ese pasaje).
- Tabla de cambios esperados del AR6 y la cifra de 20 % del PIB en riesgo por inundación costera (CCDR-tools).
- Fórmula del índice municipal ajustado por capacidades (DNP) y ecuación de Moncho (Atlas).
- Artículos de la Ley 1523 que no vienen del Atlas ni del Banco Mundial (procesos, estructura del sistema, planes municipales, artículo 42 y análisis específicos).
- Autoría completa de tres capítulos de *Investigaciones GRD* en la bibliografía (obras costeras 2021 cap. 12; incendios de la Orinoquía 2023 cap. 5; 2021 cap. 10 con solo dos autores).
- Cifras de EM-DAT sobre tormentas convectivas; primer reporte de 1932.
- Entrada de Wakimoto (2015) sobre microrráfagas (acceso cerrado).
- NSR-10, título de cargas de viento, y su modificación de 2021.
- Las cifras de las páginas de PreventionWeb (resúmenes de estudios).
- Awah et al. (2024) sobre Limbe: solo se leyó el resumen.

## Deuda técnica

- El kernel Jupyter `python3` del usuario apunta a un entorno virtual inexistente; los cuadernos se ejecutan con `JUPYTER_DATA_DIR` vacío.
- El pie de figura sale como «Figure N» en inglés (rótulo del tema).
- Hasta desplegar, el botón de Colab del sitio publicado apunta a los nombres viejos de los cuadernos.
- `mromerot.github.io/web`: el menú de `docs/datascience` está desactualizado (entorno de Python de la renderización de Quarto).
- El enlace a «3. Amenazas» en `web/grd/teoria.qmd` y la regla del CSS usan el nombre autogenerado `index-3`.

## Registro de iteraciones

| Fecha | Rebanada | Resultado |
|---|---|---|
| 2026-11-01 | Andamiaje, partes 1 a 3 y 4, despliegue | F0 |
| 2026-11-02 | HIPs: capítulo 1.6, subsección «Definición según los HIPs» en los 12 capítulos de amenaza, índice `fuentes/hips_281.csv`, plantilla con códigos HIP | Hecho |
| 2026-11-02 | Parte 5, glosario, 1.2 a 1.5, plantilla y skill, cuadernos 313 a 315, figura de ciclones, diseño, vendavales | F0 cerrada; plan escrito |

## Fuentes nuevas (carpeta referencia_colombia)

- Incorporadas: guía de avenidas torrenciales (SGC 2021, cap. 316), guía de comunicación sobre volcanes (SGC 2024, cap. 302), guía de PMGRD (UNGRD 2021, cap. 53), Terminología GRD 2017 (definición de vendaval verificada).
- Sin leer aún: clasificación de movimientos en masa, Estrategia Nacional de Respuesta a Emergencias, guía de respuesta municipal, modelo nacional de amenaza sísmica.

## Vigilancia CTeI → libro (2026-11-02)

- `scripts/vigilancia/`: `crossref.py` (metadatos por DOI, caché `fuentes/vig/crossref.json`), `bibliografia.py` (genera «Bibliografía recomendada» APA 7 por capítulo desde `AMENAZA_ESPECIFICA`), `emparejar_pdfs.py` (PDFs de la carpeta ↔ filas; 258 de 317 emparejados, 243 filas), `descargar_oa.py` (Unpaywall → `_descargados_acceso_abierto/`, solo PDFs reales), `resumen.py`, `bibkey.py`, `insertar.py`.
- Bibliografía recomendada: 13 capítulos (sismo 194, inundación 102, mov. en masa 80, erosión costera 52, incendios 41, …). Amenazas de la hoja sin capítulo: Natech, choque financiero, agentes biológicos, perturbación geomagnética, contaminación del aire, dengue, etc.
- «Síntesis de evidencia» (narrativa, resúmenes leídos, cifras por verificar): hechas 301, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 316. **Pendientes**: 302 volcanes (lahares: 2 PDFs etnográficos sobre Armero), PDFs de Natech/choque financiero/biológicos, los 60 PDFs «POR DETERMINAR», y verificar cifras contra texto completo. Los PDFs descargados por acceso abierto (carpeta `_descargados_acceso_abierto`, registro en `fuentes/vig/descargas.json`) aún no se han leído.
- Errores de la hoja: fila 884 (SUDS Ibagué) tiene un DOI que en Crossref es otro artículo; varios DOI mal formados o no resueltos (se marcan en la bibliografía); 49 filas con DOI sin metadatos en Crossref.
- Un «metaanálisis» cuantitativo con efectos agrupados no es viable con estos estudios (diseños heterogéneos); se usa síntesis narrativa por tipo de evidencia.

## Segundo lote de PDFs con el RAG (2026-11-02)

- Las 561 PDFs de `NUEVO-CONOCIMIENTO-GRD-2020-2026` se renombraron («Autor - Año - Título - DOI») y se consolidaron; el índice RAG ya los tiene (503 emparejados con la hoja). La hoja ganó la columna W «PDF disponible» (496 Sí, 454 No); copia en `fuentes/vig/disp.csv`.
- Incorporados como evidencia (cifras de resumen por verificar): avenidas torrenciales (Mocoa, Cali, cascadas publicadas en NHESS), erosión fluvial/suelo, inundación (no estacionariedad), calor (olas de calor marinas), volcanes (Galeras, nueva síntesis), sequía, ciclones, erosión costera, incendios, vendavales (Soledad), claves duplicadas del bib unificadas.
- Siguen sin leer con el RAG: texto completo de estos estudios (verificar cifras con `ragrd evidencia`), tsunami (2 PDFs), Natech, choque financiero y los 60 «POR DETERMINAR».
- Al final: aplicar `/topic-sentence` a las «Lecturas conjuntas» y párrafos introductorios.

## Frontend y cuaderno de sismicidad (2026-11-02)

- Sidebar de la sección 3 agrupado como en la sección GRD del sitio personal (tipos de amenaza de los HIPs): geológicas, hidrológicas y meteorológicas, ambientales, más «Análisis integrados»; la sección tiene ahora flecha de despliegue como las 1 y 2. No hay capítulos de amenazas biológicas, tecnológicas, sociales ni extraterrestres.
- Ilustraciones de cabecera (SVG planos, `estilo/ilustraciones/`, generadas con `python estilo/construir_ilustraciones.py`): 13 amenazas y 5 partes (conceptos, metodología, vulnerabilidad, síntesis, PMGRD). Se insertan con la directiva `image` y la clase `ilustracion`.
- Cuaderno 317 (sismicidad con datos del USGS), adaptado de `scr-ungrd/cuadernos-reproducibles-crc004` (CC BY 4.0), anidado bajo Sismos.

## Natech, tsunami, verificación y oraciones temáticas (2026-11-02)

- Nuevo capítulo provisional `319_natech.md` (grupo «Amenazas tecnológicas»; HIP TL0309; 3 estudios con PDF + Atlas 2019), con ícono, ilustración, tarjeta en la portada y entrada en `scripts/nueva_ciudad.py`. Faltan 4 trabajos de la hoja sin PDF.
- Tsunami: subsección «Ejemplo aplicado: Tumaco 1979» y cuaderno 318 (`318_tsunami_tumaco_1979.ipynb`) con las observaciones del cuaderno piloto crc003 de la UNGRD (MIT). Hallazgo: el arribo de Salinas (35 min a unos 460 km) implica una profundidad equivalente de unos 4 900 m; contrastar con Herd et al. (1981) y NOAA. El cuaderno piloto está sin validar (amplitud de calibración de 8 m frente a 1–2 m de desplazamiento real).
- `ragrd evidencia` sobre 14 capítulos: ninguna cifra «no encontrada», «parcial» ni «dispersa». Las filas «sin_pdf» son fuentes que no son PDF (handbooks, HIPs). Solo cubre cifras de las tablas de evidencia.
- Skill `/topic-sentence` aplicado a las «Lectura conjunta» de 301–312, 316 y 319 (oración temática con calificador de confianza).
- Pendiente: choque financiero, los 60 «POR DETERMINAR», PDFs sin copia local (454 filas) y leer el texto completo de los estudios cuyas cifras vienen de resúmenes.

## Pendientes consolidados (2026-11-02)

Resumen de todo lo abierto al cierre de la sesión. Estado: todo lo hecho está desplegado (último commit `8b3bcd6`).

### A. Contenido del libro
1. **Verificar cifras de resúmenes contra el texto completo.** Las «Síntesis de evidencia» de 301–312, 316 y 319 salen de resúmenes. `ragrd evidencia` solo cubre cifras de tablas con cita; extenderlo al texto corrido y a las «Lecturas conjuntas». Prioridad: avenidas torrenciales (Mocoa, Cali), sismos y movimientos en masa.
2. **Capítulos provisionales por reforzar:** erosión costera (306), erosión fluvial (307), olas de calor (309), vendavales (312) y Natech (319). Faltan resultados completos de Soledad (vendavales) y de los estudios de calor.
3. **Tsunami:** contrastar la tabla de observaciones de 1979 (en especial el arribo de Salinas, 35 min a unos 460 km) con Herd et al. (1981) y la base de la NOAA. El cuaderno piloto crc003 de la UNGRD sigue sin validar.
4. **Natech:** conseguir los cuatro trabajos sin PDF (oleoductos y deslizamientos 2021, sistema de calificación 2022, revisión sistemática de 2024, derrames por fenómenos hidrológicos extremos 2025) y buscar casos colombianos con fuente primaria; medir qué fracción de los 3 466 eventos tecnológicos de la UNGRD (1998–2017) fue Natech.
5. **Amenazas de la hoja sin capítulo:** choque financiero (8 filas), agentes biológicos (7), perturbación geomagnética (7), contaminación del aire (6), enfermedades transmitidas por vectores, dengue y leptospirosis, residuos, falla de puente y de represa, entre otras. Decidir cuáles merecen capítulo (la web GRD ya tiene grupos biológicas, tecnológicas, sociales y extraterrestres).
6. **Los 249 registros «POR DETERMINAR»** de `AMENAZA_ESPECIFICA` (60 con PDF): clasificar con el skill `vigilancia-cti-clasificacion-hips` y decidir si alimentan algún capítulo.
7. **Parte 4 (vulnerabilidad):** curvas de daño con ejemplos de Colombia (4.2) y curvas por IDF para avenidas torrenciales.
8. **PMGRD (5.3):** verificar la vigencia de la guía y del Marco Estratégico 2018–2022; leer el Decreto 2157 de 2017 y la guía de respuesta municipal.
9. **Guías nacionales sin leer** en `referencia_colombia`: clasificación de movimientos en masa, Estrategia Nacional de Respuesta a Emergencias, guía de respuesta municipal y modelo nacional de amenaza sísmica. Del documento de avenidas torrenciales solo se leyeron las secciones clave (cap. 3, 5, 6 y 8.2 a medias).
10. **Marco normativo (1.3):** contrastar con el texto oficial los artículos de la Ley 1523 y sus decretos (ya listado en «Cifras y datos por verificar»).
11. **Estilo del texto:** `/topic-sentence` se aplicó a las «Lecturas conjuntas». Falta aplicarlo a los párrafos introductorios de cada capítulo y de las partes 1, 2, 4 y 5.

### B. Fuentes y datos
1. **PDFs sin copia local:** 454 filas de la hoja con «PDF disponible = No». Descarga de acceso abierto: 300 con versión abierta sin enlace directo (abrir los enlaces de `fuentes/vig/descargas.json`), 174 sin acceso abierto (acceso institucional o pedir a los autores), 22 con error de red por reintentar. No se evaden bloqueos de los sitios.
2. **Errores de la hoja Vigilancia_CTeI** (reportar al responsable):
   - fila 884 (SUDS en Ibagué): el DOI corresponde a otro artículo (2018);
   - DOI mal formados o que no resuelven (varios en sismos, incendios y erosión costera) y 49 filas con DOI sin metadatos en Crossref;
   - 48 grupos de DOI repetidos (51 filas de más) y registros que mezclan preprint y versión publicada;
   - 47 registros sin DOI y 48 filas reservadas vacías;
   - dos años 2027 (IDs 942 y 950).
3. **Metadatos APA:** las entradas sin DOI en «Bibliografía recomendada» no tienen autores; completarlos a mano o con OpenAlex.
4. **Claves del bib:** hay claves poco legibles (por ejemplo `departamento2023analysis`, `facultad2021flood`, `universidad2020modelacion`) porque Crossref devolvió la afiliación como autor; renombrarlas.

### C. RAG-GRD (`../RAG-GRD`)
1. Indexar los PDFs nuevos cada vez que se agreguen (`python3 -m ragrd indexar`); los 454 sin copia siguen fuera.
2. Consultas bilingües: el acierto@5 cae a 64–69 % en las tandas con documentos en inglés; valorar traducción automática de la consulta con `consultas/sinonimos.yml` o embeddings.
3. Un archivo (`Cadena - 2022 … Galeras volcano.pdf`) es una página HTML guardada como `.pdf`: conseguir el PDF real por vía institucional.
4. Extraer una tabla estructurada por artículo (diseño, lugar, método, resultado, cifra) para acelerar la síntesis de evidencia.

### D. Frontend y publicación
1. Rótulo «Figure N» en inglés en los pies de figura (rótulo del tema).
2. Las ilustraciones de cabecera existen para 14 amenazas y 5 partes; faltan para «Recursos» y para las páginas de los cuadernos (313 a 318). Revisar contraste y lectura en modo oscuro y en celular.
3. Botones de Colab: los cuadernos 317 y 318 apuntan a rutas del repositorio `mromerot/teoria-riesgos`; comprobar que abren tras el despliegue.
4. `mromerot.github.io/web`: actualizar el enlace a «3. Amenazas» (usa `index-3`), el menú de `docs/datascience` y la sección GRD (grupos y capítulos nuevos: avenidas torrenciales, Natech, PMGRD).
5. El kernel `python3` del usuario apunta a un entorno inexistente; los cuadernos se ejecutan con `JUPYTER_DATA_DIR` vacío (`scripts/cuadernos/construir.py 313 314 315 317 318`).

### E. Decisiones pendientes del usuario
- ¿Qué amenazas sin capítulo (A5) se incorporan y en qué orden?
- ¿Se extiende la verificación del RAG al texto corrido (A1) antes de pasar a nuevas ciudades?
- `eva-core` (aplazado): ¿se extrae como paquete común para Leticia, SIDRo y Sincelejo?
- Aplicar el libro a una ciudad piloto (Sincelejo en curso) y registrar qué falta en el libro.
