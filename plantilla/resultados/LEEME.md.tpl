# Contrato de salida de ${nombre}

Todo análisis de ${nombre} deja sus resultados aquí, con la misma forma, para que se pueda auditar, repetir y comparar con otras ciudades. El contrato cubre los requisitos R3 (trazabilidad) y R4 (versionado) del libro de teoría. Se verifica con:

```bash
python scripts/verificar_salida.py
```

## Estructura

```
resultados/
  parametros.csv            todos los parámetros y supuestos de la corrida (obligatorio)
  03_datos/                 completitud de cada fuente de huellas, resumen de exposición, calibración de población
  04_linea_base/<amenaza>/  escenarios.csv, curva_excedencia.csv, pae.csv
  05_escenarios/<amenaza>/  mismos archivos, por escenario climático
  06_sintesis/              matriz.csv, financiamiento.csv, priorizacion.csv
```

La corrida se describe en `config/corrida.yaml` (versión del libro, fecha, quién ejecutó). Los parámetros van en `parametros.csv`, nunca solo dentro de un cuaderno.

## `parametros.csv`

Formato largo, una fila por parámetro, con estas columnas:

| Columna | Contenido |
|---|---|
| `parametro` | Clave de la lista de abajo (o una amenaza: `amenaza_<clave>_...`). |
| `valor` | Valor usado. |
| `unidad` | Unidad, o vacío. |
| `fuente` | De dónde sale (documento, capa, «propio»). Sin fuente, no hay parámetro. |
| `nivel` | `local`, `nacional`, `global` o `supuesto`. |
| `fecha_verificacion` | Fecha ISO en que se comprobó la fuente; vacío si no se comprobó. |
| `estado` | `verificado`, `por_verificar`, `por_defecto` o `supuesto`. |

`por_defecto` significa que se dejó el valor de una herramienta o plantilla sin contrastarlo con la ciudad. No es un estado aceptable para una cifra que se cite en la síntesis.

### Parámetros obligatorios

| Clave | Por qué importa |
|---|---|
| `version_libro` | Etiqueta o DOI del libro de teoría usado (R4). |
| `fecha_corrida` | Fecha ISO. |
| `dem_fuente`, `dem_tipo`, `dem_resolucion_m` | `dem_tipo` es `superficie` o `terreno`: un modelo de superficie incluye techos y árboles y sesga la altura sobre el cauce. |
| `dem_respaldo_usado` | `si` o `no`. Si el DEM principal falló y se usó otro, debe constar. |
| `huellas_fuente` | De dónde salen las huellas de edificios (catastro, Overture, OSM u otra) y su capa. |
| `huellas_completitud_pct` | Superficie de las huellas sobre la superficie construida de GHSL, en el área analizada. Con menos de 80 %, las cuentas quedan bajas; con más de 120 % hay duplicados o sobreestimación. |
| `huellas_fecha_extraccion` | Las fuentes cambian; la fecha va con el dato. |
| `huellas_licencia` | Términos de uso de la fuente: si prohíben publicar o redistribuir, los datos por edificio no se versionan ni se publican (carpeta `data/restringido/`). |
| `poblacion_total`, `poblacion_fuente`, `poblacion_anio` | Población con la que se calibró el modelo. |
| `costo_fuente` | `gem`, `jrc` o `propio`. |
| `costo_residencial_usd_m2`, `costo_residencial_rango_usd_m2` | El valor y el rango plausible. La pérdida es lineal en el costo: dos fuentes pueden diferir varias veces. |
| `contenidos_pct` | Contenidos como porcentaje del valor estructural. |
| `curva_dano_fuente` | Curva profundidad-daño usada y su región de origen. |
| `escenarios_origen` | `local`, `estudio` o `por_defecto`. Niveles de agua sin hidrología local no sirven para la PAE. |
| `rp_minimo_escenarios` | Periodo de retorno del escenario más frecuente. La PAE no cuenta eventos más frecuentes que ese. |
| `pae_exclusiones` | Qué no incluye la PAE (por ejemplo: «solo daño directo a edificaciones»). |

Por amenaza que aplique en `config/amenazas.yaml`, se agrega `amenaza_<clave>_metodo` (qué método y de qué nivel) y `amenaza_<clave>_calibrado` (`si` o `no`). Un puntaje heurístico sin calibrar se marca `no` y no se combina con dinero. Si hay un mapa oficial de la amenaza, el contraste con él se registra en `amenaza_<clave>_validacion` (qué mapa, qué cubre y qué no, y las medidas de acuerdo).

Si hay un índice de vulnerabilidad social, se agregan `ivs_indicadores`, `ivs_pesos` e `ivs_modo` (`absoluto` o `relativo`). Entre ciudades solo se comparan índices en modo absoluto.

## Tablas por paso

Todas son CSV con encabezado, sin datos personales: cuando haya duda, se agrega a manzana.

| Archivo | Columnas mínimas |
|---|---|
| `03_datos/completitud_<fuente>.csv` | `bloque`, `huellas_m2` (o `osm_m2`), `ghsl_m2`, `cobertura_pct`; una tabla por fuente de huellas comparada |
| `04_linea_base/<amenaza>/escenarios.csv` | `rp`, `nivel_agua_m`, `edificios`, `poblacion`, `perdida_usd` |
| `04_linea_base/<amenaza>/curva_excedencia.csv` | `rp`, `frecuencia_anual`, `perdida_usd` |
| `04_linea_base/<amenaza>/pae.csv` | `pae_usd`, `pae_poblacion`, `metodo_integracion`, `cola` |
| `06_sintesis/matriz.csv` | `amenaza`, `p90_puntaje`, `probabilidad`, `poblacion_expuesta_pct`, `servicio_critico`, `impacto`, `puntaje`, `calificacion` |
| `06_sintesis/financiamiento.csv` | `capa`, `desde_rp`, `hasta_rp`, `pae_usd`, `instrumento`, `costo_usd`, `supuesto_costo` |

La matriz guarda todos los valores intermedios, para poder reconstruir el cálculo.

## Reglas

1. No se suman PML entre amenazas ni se mezclan índices relativos con dinero (ver la síntesis del libro).
2. Cada cifra citada en `book/` sale de una fila de estas tablas y de un parámetro con fuente.
3. Si cambia el DEM, los costos, los escenarios o la versión del libro, se vuelve a correr y se archiva la corrida anterior en `resultados/archivo/AAAA-MM-DD/`.
4. Lo que la corrida enseñó sobre el libro (un parámetro que faltaba, un método que falló) se anota en `resultados/retroalimentacion.md`, para llevarlo de vuelta al libro (R5).
