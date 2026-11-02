version: 1
project:
  title: ${nombre}
  subtitle: Riesgos de desastres y climáticos
  description: Análisis de riesgos de desastres y climáticos de ${nombre} (${municipio}), construido con el libro de teoría y métodos https://mromerot.github.io/teoria-riesgos/
  keywords: [riesgo de desastres, riesgo climático, ${municipio}, MyST]
  authors:
    - name: ${autor}
  license:
    content: CC-BY-4.0
${linea_github}
  bibliography: [references.bib]
  jupyter: true
  toc:
    - file: index.md
    - file: book/01_alcance.md
    - file: book/02_amenazas.md
    - file: book/03_datos.md
    - title: Análisis
      children:
        - file: book/analisis/index.md
        - pattern: book/analisis/a_*.md
    - file: book/05_sintesis.md
site:
  template: book-theme
  title: ${nombre}
