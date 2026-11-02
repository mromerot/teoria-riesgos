---
title: Avenidas torrenciales
---

# Avenidas torrenciales

Este capítulo sigue el molde de siete puntos ([](_molde.md)) y se apoya sobre todo en la guía metodológica del Servicio Geológico Colombiano (SGC) y la Pontificia Universidad Javeriana {cite:p}`sgc2021avenidas`. Esa guía es la referencia nacional para zonificar la amenaza y tiene licencia CC BY 4.0. Aquí se resume y se organiza para el análisis de una ciudad; para ejecutar un estudio hay que consultarla completa.

## 1. Fenómeno

La guía define la avenida torrencial como un flujo muy rápido, en canales de alta pendiente longitudinal, de agua con una cantidad significativa de sólidos {cite:p}`sgc2021avenidas`. El término agrupa flujos de detritos, flujos de lodo y flujos hiperconcentrados, que se distinguen por la proporción y el tamaño de los sedimentos {cite:p}`sgc2021avenidas`.

Se diferencia de la creciente súbita de [](305_inundacion.md) por la carga sólida: en una avenida torrencial los sedimentos y la madera cambian la densidad, la fuerza de impacto y la forma en que el flujo se desborda y se deposita. Por eso la profundidad no basta como variable de intensidad.

**Variable de intensidad.** La guía usa un índice de intensidad del flujo, IDF = h·v² (altura por velocidad al cuadrado, en m³/s²), propuesto por Jakob y colaboradores y adoptado como medida de la fuerza destructiva {cite:p}`sgc2021avenidas`. Se complementa con el tamaño de bloques, representado por el D90 (m).

```{note}
En Colombia las avenidas torrenciales ocurren con frecuencia junto con inundaciones y movimientos en masa. Un caso conocido es el de Mocoa en 2017, citado en [](305_inundacion.md).
```

### Definición según los HIPs de UNDRR

Los perfiles de información de amenazas ([](../01_conceptos/16_hips_undrr.md)) que corresponden a este capítulo son:

| Código | Perfil | Relación con el capítulo |
|---|---|---|
| MH0603 | Inundación repentina | Inundación de corta duración con un caudal pico relativamente alto (OMM, 2021) {cite:p}`undrr2025hips`. |
| GH0303 | Flujos de detritos, de tierra (lodo) y avalanchas de roca | Movimientos en masa gravitacionales en forma de fluido, que suelen dejar un depósito en abanico {cite:p}`undrr2025hips`. |

**Qué se incluye y por qué.** La avenida torrencial colombiana combina las dos cosas: el caudal pico rápido de MH0603 y el transporte de sedimentos de GH0303. Es una correspondencia de criterio de este libro, no una equivalencia declarada por los HIPs.

## 2. Amenaza

La guía organiza la zonificación en cuatro etapas {cite:p}`sgc2021avenidas`:

1. **Caracterización de la avenida torrencial**: geomorfología, susceptibilidad, inventario histórico (con un formato de inventario propio) e índices morfométricos para decidir qué cuencas son propensas.
2. **Análisis de detonantes**: sobre todo la lluvia. Se trabaja con periodos de retorno de 2,33, 5, 10, 25, 50, 100, 300 y 500 años, curvas intensidad–duración–frecuencia del IDEAM y registros de al menos 30 años; un modelo hidrológico produce los hidrogramas.
3. **Caracterización de la amenaza** con modelos fluidodinámicos bidimensionales que incorporan la reología del flujo. Los sólidos que alimentan la avenida provienen de movimientos en masa, erosión de laderas y socavación lateral.
4. **Zonificación** en categorías baja, media y alta.

### Escalas y criterios

La guía distingue dos escalas, que responden al Decreto 1077 de 2015 y a la Ley 388 de 1997 {cite:p}`sgc2021avenidas`:

| Escala | Uso | Criterio de zonificación |
|---|---|---|
| 1:25.000 | Rural | El IDF se pondera por la frecuencia de los periodos de retorno y se combina con el D90 en una matriz de tres por tres |
| 1:2.000 | Urbana y de expansión | Curvas de amenaza por celda (al menos seis puntos) y dos criterios cuyo máximo define la categoría |

En la escala 1:2.000, el primer criterio usa un índice de confiabilidad β entre 2,5 y 3 (probabilidad de 0,0025, es decir un periodo de retorno cercano a 400 años) con umbrales de IDF de 1 y 50 para baja, media y alta. El segundo fija un umbral de IDF = 5 y clasifica por recurrencia: alta si es menor de 30 años, media entre 30 y 100, baja desde 100 {cite:p}`sgc2021avenidas`.

**Falsos negativos.** Si un evento reciente (menos de 500 años) ocurrió donde el modelo dice amenaza baja, la guía propone reclasificar según la magnitud del evento {cite:p}`sgc2021avenidas`.

**Escenarios adicionales.** Represamiento por movimientos en masa, madera flotante (troncos de más de 1 m de largo y 10 cm de diámetro) y avulsión por rotura de diques {cite:p}`sgc2021avenidas`.

```{warning}
Hay que revisar el valor de cada umbral y de cada periodo de retorno en la guía antes de usarlos en un estudio: aquí se resumen para orientar, no para reemplazar el texto.
```

## 3. Exposición

La guía trata la zonificación de amenaza y propone, al final, estimar el riesgo de un escenario como el producto de la amenaza (H) por la vulnerabilidad (V), con el riesgo total como la integral sobre los escenarios {cite:p}`sgc2021avenidas`. Para la exposición se usan los mismos insumos que en inundación: población, edificaciones y vías sobre el abanico y los cauces ([](../04_vulnerabilidad/index.md)).

Los abanicos aluviales son lugares de expansión urbana frecuente, y la zonificación 1:2.000 está pensada justamente para esas áreas.

## 4. Vulnerabilidad

La guía no desarrolla funciones de daño propias. La vulnerabilidad debe tomarse de las funciones de daño por intensidad de [](../04_vulnerabilidad/42_funciones_dano.md), usando el IDF o la presión de impacto como variable, no solo la profundidad. Falta una fuente colombiana verificada para curvas de daño por IDF.

## 5. Riesgo

Con la curva de amenaza por celda (IDF contra periodo de retorno), la exposición y una función de daño, el riesgo se calcula como en [](../02_metodologia/22_probabilista_pae.md): se integran las pérdidas sobre la probabilidad anual de excedencia.

La guía advierte que la validación con casos piloto todavía está pendiente {cite:p}`sgc2021avenidas`. Un estudio completo requiere un equipo con geología, hidrología, geotecnia, hidráulica, SIG y manejo forestal, y la modelación toma de semanas a meses.

## 6. Clima

La guía concluye que modelar el cambio climático no mejoraría el análisis del detonante, porque las tendencias de precipitación extrema del IDEAM no son significativas, y que el cambio de cobertura y el crecimiento de la población pesan más {cite:p}`sgc2021avenidas`. Recomienda actualizar la zonificación periódicamente.

Este libro sigue esa postura para el detonante y propone, como criterio propio, revisar con el capítulo [](../02_metodologia/23_escenarios_climaticos.md) si el clima cambia la frecuencia de lluvias extremas en la cuenca de estudio.

## 7. Datos y medidas

### Datos necesarios

| Insumo | Fuente |
|---|---|
| Curvas IDF, series de lluvia (≥30 años) | IDEAM {cite:p}`sgc2021avenidas` |
| Modelo digital de elevación y geomorfología | SGC e IGAC {cite:p}`sgc2021avenidas` |
| Inventario histórico de eventos | Formato del anexo 1 de la guía {cite:p}`sgc2021avenidas` |
| Cobertura y suelos | Para la hidrología y el aporte de sedimentos |

### Incertidumbres principales

- Calibración de la reología con pocos eventos documentados.
- Cantidad de sedimentos disponibles y madera.
- Validación pendiente con casos piloto {cite:p}`sgc2021avenidas`.

### Medidas según la Ley 1523

| Proceso | Medida |
|---|---|
| Conocimiento | Zonificación 1:25.000 rural y 1:2.000 urbana; inventario histórico; monitoreo de lluvia |
| Reducción: prevención | Incorporar la zonificación al ordenamiento territorial, con restricción de usos en abanicos y rondas |
| Reducción: mitigación | Control de sedimentos y cobertura en la cuenca; por detallar con fuente |
| Manejo | Alerta temprana por lluvia y evacuación; por detallar con fuente |

## Pendiente

- Leer los capítulos 3, 5 y 6 de la guía completos y verificar umbrales.
- Añadir medidas de mitigación y alerta temprana con fuente.
- Añadir un caso colombiano (Mocoa 2017, Salgar 2015) con fuente primaria.
