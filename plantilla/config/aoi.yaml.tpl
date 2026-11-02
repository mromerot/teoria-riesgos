# Área de interés. Es el único archivo que cambia para pasar de una ciudad a otra.
nombre: "${nombre}"
municipio: "${municipio}"
codigo_divipola: "${divipola}"
slug: "${slug}"

# Cómo obtener el polígono, en orden de preferencia:
# 1) archivo propio (GeoJSON/GPKG) 2) capa oficial 3) OpenStreetMap 4) rectángulo de respaldo
geometria:
  archivo: null
  consulta_osm: "${nombre}, ${municipio}, Colombia"
  bbox_respaldo: null          # [lon_min, lat_min, lon_max, lat_max]

bufer_m: 1000
crs_trabajo: "EPSG:9377"       # MAGNA-SIRGAS / Origen-Nacional
crs_export: "EPSG:4326"
unidad_analisis: "manzana"     # manzana | lote | celda | municipio
