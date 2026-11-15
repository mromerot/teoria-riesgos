# Metadatos de la corrida de análisis (ver resultados/LEEME.md).
# Se actualiza cada vez que se vuelve a correr el análisis.
ciudad: "${nombre}"
creado: "${fecha}"

libro_teoria:
  version: null          # etiqueta o DOI del libro usado (R4); obligatorio antes de citar resultados
  url: "https://mromerot.github.io/teoria-riesgos/"

corrida:
  fecha: null            # AAAA-MM-DD
  ejecutada_por: "${autor}"
  entorno: null          # por ejemplo: python 3.13, versiones de paquetes principales
  commit: null           # commit del repositorio de la ciudad al correr

# Herramientas externas usadas como referencia o para tamizaje. No son fuente de cifras.
herramientas_externas: []
#  - {nombre: "OpenHVRA", version: "0.13.1", uso: "tamizaje de nivel 0", licencia: "AGPL-3.0"}
