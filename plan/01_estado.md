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
- [ ] **F3. Fuentes institucionales**
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

Ver la tabla de la sección 3 de `plan/00_plan.md`. Resumen de lo que falta: CLIMADA más allá de `Impact`, *Investigaciones GRD* 2025, los conceptos clave de PreventionWeb, los 3 documentos E2050, el informe de ciudades, el perfil de país, la Guía PMGRD y los otros 9 libros de `libros_referencia`, y 317 PDFs de artículos.

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
- Cifras de EM-DAT sobre tormentas convectivas; definición de vendaval de la UNGRD (2017); primer reporte de 1932.
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
| 2026-11-02 | Parte 5, glosario, 1.2 a 1.5, plantilla y skill, cuadernos 313 a 315, figura de ciclones, diseño, vendavales | F0 cerrada; plan escrito |
