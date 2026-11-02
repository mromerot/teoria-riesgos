# Catálogo de datos (paso 3). Una entrada por insumo, con niveles local -> nacional -> global.
# verificado: fecha en que se comprobó que el recurso responde (null = pendiente).
# No añadir URLs sin comprobarlas.
capas:
  exposicion_poblacion:
    tema: "Población"
    niveles:
      - {nivel: nacional, fuente: "Censo Nacional de Población y Vivienda 2018 (DANE)", url: null, verificado: null}
      - {nivel: global, fuente: "GHS-POP o WorldPop", url: null, verificado: null}
  exposicion_edificaciones:
    tema: "Edificaciones"
    niveles:
      - {nivel: local, fuente: "Catastro o censo de edificaciones de la ciudad", url: null, verificado: null}
      - {nivel: global, fuente: "OpenStreetMap, GHS-BUILT", url: null, verificado: null}
  vulnerabilidad_social:
    tema: "Vulnerabilidad social y capacidades"
    niveles:
      - {nivel: nacional, fuente: "IPM e Índice Municipal de Riesgo ajustado por capacidades", url: null, verificado: null}
