---
title: Marco conceptual del riesgo
---

# Marco conceptual del riesgo

## Qué es el riesgo de desastres

El riesgo de desastres es una pérdida **potencial**, no un hecho ocurrido: depende de qué puede pasar, de qué hay en el camino y de qué tan frágil es. La Ley 1523 de 2012 lo define como los daños o pérdidas potenciales que pueden presentarse por eventos físicos peligrosos de origen natural, socionatural, tecnológico, biosanitario o humano no intencional, en un periodo de tiempo específico, determinados por la vulnerabilidad de los elementos expuestos {cite:p}`ley1523`. Por eso se deriva de combinar amenaza y vulnerabilidad.

## Los tres componentes

El Atlas de Riesgo de Colombia {cite:p}`ungrd2019atlas` adopta la definición de la UNISDR (2009), con tres componentes que no pueden definirse sin los otros dos:

| Componente | Pregunta que responde | Definición resumida en la Ley 1523 {cite:p}`ley1523` |
|---|---|---|
| **Amenaza** | ¿Qué fenómeno puede ocurrir, con qué intensidad y frecuencia? | Peligro latente de que un evento físico se presente con severidad suficiente para causar pérdidas o daños. |
| **Exposición** | ¿Qué hay en el área que puede ser afectada? | Presencia de personas, medios de vida, bienes e infraestructura que por su localización pueden ser afectados. |
| **Vulnerabilidad** | ¿Qué tan fácil se daña lo expuesto? | Susceptibilidad o fragilidad física, económica, social, ambiental o institucional ante un evento peligroso. |

```{important}
Sin amenaza no hay riesgo, aunque haya vulnerabilidad. Sin elementos expuestos tampoco, aunque haya amenaza.
```

## Del concepto al cálculo

Los métodos de este libro (CLIMADA, CCDR-tools, CLIMAAX) comparten un orden de cálculo. El Atlas lo organiza en cuatro módulos {cite:p}`ungrd2019atlas`:

1. **Amenaza.** Un catálogo de eventos estocásticos, mutuamente excluyentes y colectivamente exhaustivos, cada uno con una frecuencia de ocurrencia asignada. Permite incluir eventos posibles que aún no han ocurrido.
2. **Elementos expuestos.** Cada uno recibe atributos según sus características (estructura, material, valor catastral, tipo de cultivo, costo).
3. **Vulnerabilidad.** Una función o modelo específico por amenaza que traduce la intensidad en grado de daño y, de ahí, en pérdida económica y humana.
4. **Cálculo del riesgo.** Se integran los daños de todos los eventos, ponderados por su frecuencia.

Como la amenaza y el daño son inciertos, el cálculo trata ambos como variables aleatorias y propaga la dispersión en vez de usar solo el valor medio {cite:p}`ungrd2019atlas`.

## Métricas de riesgo

El resultado central es la **curva de excedencia de pérdidas**, que relaciona cada valor de pérdida con su tasa de excedencia. De ella salen las dos métricas más usadas {cite:p}`ungrd2019atlas`:

- **Pérdida anual esperada (PAE, o AAL en inglés).** Es el valor esperado de la pérdida en un año. Equivale a la prima pura anual de un seguro simple y supone que la ocurrencia de eventos es estacionaria.
- **Pérdida máxima probable (PMP, o PML).** Es la pérdida asociada a periodos de retorno largos, poco frecuentes. En realidad es una curva de pérdida contra periodo de retorno. No hay un estándar para fijar los periodos de retorno del análisis.

```{warning}
El supuesto de estacionariedad de la PAE es justamente lo que el cambio climático cuestiona para las amenazas hidrometeorológicas. Ver [](12_riesgo_climatico.md).
```

## Los tres procesos de la gestión del riesgo en Colombia

La Ley 1523 organiza la gestión en tres procesos: conocimiento del riesgo, reducción del riesgo y manejo del desastre {cite:p}`ley1523`. Este libro cubre el primero: identificar, analizar y monitorear el riesgo. Las medidas de cada amenaza se clasifican en los otros dos al final de cada capítulo.

## Pendiente de verificar

- Citar la fuente primaria de la definición UNISDR (2009) en lugar de la cita indirecta vía Atlas.
- Añadir el marco IPCC AR6 (amenaza, exposición, vulnerabilidad y respuesta) en el capítulo 1.2.
