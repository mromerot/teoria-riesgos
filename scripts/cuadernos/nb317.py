"""Fuente del cuaderno 317 (sismicidad de Colombia con el catálogo del USGS). Adaptado de scr-ungrd/cuadernos-reproducibles-crc003 (CC BY 4.0)."""
CELLS = []
def md(t): CELLS.append(("md", t.strip("\n")))
def code(t): CELLS.append(("code", t.strip("\n")))

md(r'''
# Sismicidad de Colombia: catálogo USGS, completitud, cortes y 3D

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mromerot/teoria-riesgos/blob/main/book/03_amenazas/317_sismicidad_colombia.ipynb)

Este cuaderno **descarga datos reales** y muestra cómo caracterizar la sismicidad de una región: tasa de ocurrencia, distribución de profundidades y de magnitudes (relación de Gutenberg-Richter), completitud del catálogo en el tiempo, cortes transversales y una vista 3D de la profundidad. Son los insumos del análisis probabilista de amenaza sísmica de [](301_sismo.md). Se puede ejecutar completo en Colab o en un computador, sin cuenta ni claves.

**Origen y licencia.** Reúne el cuaderno «Análisis de Sismicidad de Colombia» de la Subdirección para el Conocimiento del Riesgo de la UNGRD ([cuadernos-reproducibles-crc003](https://scr-ungrd.github.io/cuadernos-reproducibles-crc003/), CC BY 4.0) y el cuaderno de sismicidad histórica y completitud del mismo grupo ([scr-ungrd/sismicidad-colombia](https://github.com/scr-ungrd/sismicidad-colombia), CC BY 4.0). Aquí se dejó el análisis estático y la vista 3D, y se añadió la estimación de la magnitud de completitud y de la *b* por máxima verosimilitud.

**Datos.** Servicio web FDSN de eventos del USGS ([earthquake.usgs.gov/fdsnws/event/1](https://earthquake.usgs.gov/fdsnws/event/1/)), dominio público, y la base de sismos significativos de NOAA/NCEI. Las secciones 1 a 4 usan el periodo 2000–2024, la región entre 5° S y 13° N y entre 82° O y 65° O, y magnitud mínima 3,0. Las secciones 5 a 9 usan un catálogo ampliado (1900–2026, magnitud mínima 2,5, entre 5° S y 16° N y entre 84° O y 66° O). La caja incluye parte de Ecuador, Perú, Venezuela y Panamá, por lo que **los sismos mayores del listado no son todos colombianos** (se muestra el lugar de cada uno).

```{warning}
Es un catálogo **global** del USGS, no el catálogo oficial del Servicio Geológico Colombiano (SGC), que tiene más estaciones locales y menor magnitud de completitud. Sirve para aprender el método; para un estudio de amenaza se debe usar el catálogo del SGC. No se usa aquí porque el SGC no publica un servicio web abierto y documentado (su consulta funciona solo desde el formulario del sitio y las descargas automáticas son rechazadas), no se encontró una licencia de datos abiertos para el catálogo y usarlo obligaría a una descarga manual, con lo que el cuaderno dejaría de correr completo con datos abiertos y sin credenciales.
```
''')

code(r'''
from io import StringIO
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
from scipy import stats

# ----------------------------- parámetros -----------------------------
PARAMS = dict(format="csv", starttime="2000-01-01", endtime="2024-12-31",
              minlatitude=-5, maxlatitude=13, minlongitude=-82, maxlongitude=-65,
              minmagnitude=3.0, orderby="time")
URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"
AZUL, ROJO, NARANJA = "#0154a5", "#c0392b", "#e08e0b"
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False})
''')

md(r'''
## 1. Descarga y limpieza

La consulta devuelve un CSV. Nos quedamos con tiempo, posición, profundidad y magnitud, y clasificamos cada sismo por profundidad focal: superficial (hasta 70 km), intermedio (70 a 300 km) y profundo (más de 300 km).
''')

code(r'''
r = requests.get(URL, params=PARAMS, timeout=120); r.raise_for_status()
raw = pd.read_csv(StringIO(r.text))
df = raw[["time", "latitude", "longitude", "depth", "mag", "magType", "place"]].dropna(subset=["mag", "depth"]).copy()
df.columns = ["tiempo", "lat", "lon", "prof_km", "mag", "tipo_mag", "lugar"]
df["tiempo"] = pd.to_datetime(df["tiempo"], utc=True)
df["anio"] = df["tiempo"].dt.year
df["clase"] = pd.cut(df["prof_km"], [-10, 70, 300, 1000], labels=["Superficial (≤ 70 km)", "Intermedio (70–300 km)", "Profundo (> 300 km)"])
print(f"Eventos descargados: {len(raw):,}; válidos: {len(df):,}")
print(df["clase"].value_counts().to_string())
print("\nTipos de magnitud:", df["tipo_mag"].value_counts().head(4).to_dict())
''')

md(r'''
## 2. Distribución en el tiempo

Un catálogo cambia con la red de estaciones: más estaciones detectan más sismos pequeños. Por eso la tasa anual **no** se interpreta como cambio de la actividad sin revisar la completitud.
''')

code(r'''
anual = df.groupby("anio").size()
fig, ax = plt.subplots(1, 2, figsize=(12, 3.8))
ax[0].bar(anual.index, anual.values, color=AZUL)
ax[0].axhline(anual.mean(), color=ROJO, ls="--", label=f"Media: {anual.mean():.0f} por año")
ax[0].set(title="Sismos por año (M ≥ 3,0)", ylabel="Eventos"); ax[0].legend()
mmax = df.groupby("anio")["mag"].max()
ax[1].scatter(mmax.index, mmax.values, c=AZUL, s=30)
ax[1].set(title="Magnitud máxima por año", ylabel="Magnitud")
plt.tight_layout(); plt.show()
''')

md(r'''
## 3. Relación de Gutenberg-Richter

La relación $\log_{10} N = a - b\,M$ da el número $N$ de sismos de magnitud mayor o igual a $M$. El parámetro $b$ (cerca de 1 en muchas regiones) mide la proporción de sismos pequeños y grandes, y $a$ el nivel de actividad. Ambos alimentan el análisis probabilista de amenaza.

El ajuste debe usar solo magnitudes por encima de la **magnitud de completitud** $M_c$, la menor magnitud desde la cual el catálogo registra todos los eventos. La estimamos con el método del máximo de la curvatura (el bin con más eventos) y calculamos $b$ de dos formas: regresión sobre la curva acumulada y máxima verosimilitud (Aki, 1965; Utsu, 1966), que es la más usada.
''')

code(r'''
def gr(mags, bin_=0.1):
    bins = np.round(np.arange(mags.min(), mags.max() + bin_, bin_), 2)
    h, edges = np.histogram(mags, bins=bins)
    centros = edges[:-1] + bin_ / 2
    mc = centros[np.argmax(h)]                       # máximo de curvatura
    sel = mags[mags >= mc]
    b_ml = np.log10(np.e) / (sel.mean() - (mc - bin_ / 2))   # Aki-Utsu
    b_se = b_ml / np.sqrt(len(sel))
    acum = np.array([(sel >= m).sum() for m in centros[centros >= mc]])
    m_ac = centros[centros >= mc]
    ok = acum > 0
    sl, ic, rr, _, _ = stats.linregress(m_ac[ok], np.log10(acum[ok]))
    return dict(mc=mc, n=len(sel), b_ml=b_ml, b_se=b_se, b_ls=-sl, a_ls=ic, r2=rr**2, m=m_ac[ok], logn=np.log10(acum[ok]), centros=centros, h=h)

g = gr(df["mag"].values)
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].scatter(g["m"], g["logn"], s=18, c=AZUL, label="Frecuencia acumulada")
ax[0].plot(g["m"], g["a_ls"] - g["b_ls"] * g["m"], c=ROJO, label=f"Ajuste: b = {g['b_ls']:.2f}")
ax[0].set(xlabel="Magnitud", ylabel="log10 N (≥ M)", title="Gutenberg-Richter"); ax[0].legend()
ax[1].bar(g["centros"], g["h"], width=0.09, color=AZUL)
ax[1].axvline(g["mc"], c=ROJO, ls="--", label=f"Mc ≈ {g['mc']:.1f}")
ax[1].set(xlabel="Magnitud", ylabel="Eventos", title="Histograma de magnitudes"); ax[1].legend()
plt.tight_layout(); plt.show()
print(f"Magnitud de completitud (curvatura): Mc = {g['mc']:.1f}  (n = {g['n']:,} eventos por encima)")
print(f"b por máxima verosimilitud: {g['b_ml']:.2f} ± {g['b_se']:.2f}")
print(f"b por regresión acumulada:  {g['b_ls']:.2f}  (R² = {g['r2']:.3f})")
''')

md(r'''
Si $M_c$ es mayor que 3,0, los sismos entre 3,0 y $M_c$ **no** forman parte del ajuste: incluirlos subestima $b$. La regresión sobre la curva acumulada no es independiente entre puntos y suele sesgar el resultado, por eso se prefiere la máxima verosimilitud.
''')

md(r'''
## 4. Profundidad focal

La profundidad y el tipo de fuente (subducción, intraplaca, cortical) cambian la atenuación del movimiento del suelo y el daño. En Colombia conviven sismos corticales, de subducción y de la zona profunda del Nido de Bucaramanga.
''')

code(r'''
colores = {"Superficial (≤ 70 km)": ROJO, "Intermedio (70–300 km)": NARANJA, "Profundo (> 300 km)": AZUL}
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
for k, c in colores.items():
    s = df[df["clase"] == k]
    ax[0].hist(s["prof_km"], bins=40, color=c, alpha=.75, label=f"{k} (n={len(s):,})")
    ax[1].scatter(s["prof_km"], s["mag"], s=5, color=c, alpha=.4)
ax[0].set(xlabel="Profundidad (km)", ylabel="Eventos", title="Profundidades focales"); ax[0].legend(fontsize=8)
ax[1].set(xlabel="Profundidad (km)", ylabel="Magnitud", title="Magnitud frente a profundidad")
plt.tight_layout(); plt.show()
''')

md(r'''
## 5. Catálogo ampliado y completitud en el tiempo

Hasta aquí el análisis usó los sismos de 2000 a 2024. Para saber si el número de sismos cambia por la actividad real o por la instrumentación, se amplía el catálogo a **1900–2026 con magnitud de 2,5 o más** en un cuadrante algo mayor (84° O a 66° O y 5° S a 16° N, el mismo del Catálogo Sísmico Integrado del SGC, Montejo et al., 2023), y se agregan los sismos anteriores a 1900 de la base de sismos significativos de NOAA/NCEI. La API del USGS entrega como máximo 20 000 eventos por consulta, así que la descarga se hace por décadas y cualquier tramo saturado se divide en dos. Las secciones 5 a 9 usan este catálogo ampliado y sus conteos no son comparables con los de las secciones 1 a 4.
''')

code(r'''
import io, time

# ---------------- Parámetros del catálogo ampliado ----------------
BBOX = dict(lon_min=-84.0, lon_max=-66.0, lat_min=-5.0, lat_max=16.0)   # cuadrante de Montejo et al. (2023)
ANIO_INI = 1900          # inicio del catálogo instrumental
FECHA_FIN = "2026-11-15"      # fecha fija: el resultado es reproducible
MAG_MIN = 2.5            # magnitud mínima de descarga
MAG_COMPLETA = 4.5       # umbral "completo" para comparar tasas
PROF_MAX = 200           # profundidad máxima de los cortes (km)
EXAG_VERTICAL = 3        # exageración vertical de los cortes

ANIO_FIN = pd.Timestamp(FECHA_FIN).year + (pd.Timestamp(FECHA_FIN).dayofyear - 1) / 365.25
LAT_MEDIA = (BBOX["lat_min"] + BBOX["lat_max"]) / 2
KM_LAT = 110.57
KM_LON = 111.32 * np.cos(np.radians(LAT_MEDIA))

def miles(n):
    """Entero con espacio como separador de miles."""
    return f"{int(n):,}".replace(",", " ")

def dec(x):
    """Número con coma decimal."""
    return f"{x:g}".replace(".", ",")

LIMITE = 20000

def _usgs_tramo(t0, t1):
    """Descarga un tramo temporal; si llega al límite, lo divide en dos."""
    params = dict(format="csv", orderby="time-asc", limit=LIMITE, eventtype="earthquake",
                  starttime=t0.strftime("%Y-%m-%dT%H:%M:%S"), endtime=t1.strftime("%Y-%m-%dT%H:%M:%S"),
                  minlatitude=BBOX["lat_min"], maxlatitude=BBOX["lat_max"],
                  minlongitude=BBOX["lon_min"], maxlongitude=BBOX["lon_max"], minmagnitude=MAG_MIN)
    for intento in range(4):
        r = requests.get(URL, params=params, timeout=180)
        if r.status_code in (200, 204):
            break
        time.sleep(5 * (intento + 1))
    r.raise_for_status()
    if r.status_code == 204 or not r.text.strip():
        return pd.DataFrame()
    d = pd.read_csv(io.StringIO(r.text))
    if len(d) >= LIMITE:
        tm = t0 + (t1 - t0) / 2
        return pd.concat([_usgs_tramo(t0, tm), _usgs_tramo(tm, t1)], ignore_index=True)
    return d

partes, t, fin = [], pd.Timestamp(year=ANIO_INI, month=1, day=1), pd.Timestamp(FECHA_FIN)
while t < fin:
    t2 = min(t + pd.DateOffset(years=10), fin)
    partes.append(_usgs_tramo(t, t2))
    t = t2
crudo = pd.concat([p for p in partes if len(p)], ignore_index=True).drop_duplicates("id")

tt = pd.to_datetime(crudo["time"], utc=True, format="ISO8601")
dias = np.where(tt.dt.is_leap_year, 366, 365)
usgs = pd.DataFrame({
    "anio_dec": tt.dt.year + (tt.dt.dayofyear - 1 + tt.dt.hour / 24) / dias,
    "fecha": tt.dt.strftime("%Y-%m-%d"),
    "lat": crudo["latitude"], "lon": crudo["longitude"], "prof_km": crudo["depth"],
    "mag": crudo["mag"], "lugar": crudo["place"], "fuente": "USGS", "historico": False})
print(f"USGS: {miles(len(usgs))} eventos de magnitud {dec(MAG_MIN)} o más, {usgs.fecha.min()} a {usgs.fecha.max()}")
''')

md(r'''
La base de sismos significativos de NOAA aporta los eventos anteriores a 1900 y, para todo el periodo, las víctimas reportadas. Eso permite identificar los sismos por su **impacto** y no solo por su magnitud. En los eventos históricos la magnitud proviene de intensidades macrosísmicas y casi nunca se conoce la profundidad.
''')

code(r'''
NOAA_URL = "https://www.ngdc.noaa.gov/hazel/hazard-service/api/v1/earthquakes"
COLS_NOAA = ["year", "month", "day", "latitude", "longitude", "eqDepth", "eqMagnitude", "locationName", "deaths"]

noaa = pd.DataFrame()
try:
    filas, pag, total = [], 1, 1
    while pag <= total:
        r = requests.get(NOAA_URL, params=dict(country="COLOMBIA", page=pag), timeout=120)
        r.raise_for_status()
        js = r.json()
        filas += js.get("items", [])
        total = int(js.get("totalPages", 1) or 1)
        pag += 1
    d = pd.DataFrame(filas).reindex(columns=COLS_NOAA)
    mes, dia = d["month"].fillna(7), d["day"].fillna(15)
    lugar = (d["locationName"].fillna("").astype(str)
             .str.split(":").str[-1].str.split(",").str[:2].str.join(",").str.replace(r"\s+", " ", regex=True)
             .str.replace(",", ", ").str.replace(r",\s+", ", ", regex=True).str.strip().str.title())
    noaa = pd.DataFrame({
        "anio_dec": d["year"] + (mes - 1) / 12 + (dia - 1) / 365.25,
        "fecha": (d["year"].astype("Int64").astype(str) + "-" + mes.astype(int).astype(str).str.zfill(2)
                  + "-" + dia.astype(int).astype(str).str.zfill(2)),
        "lat": d["latitude"], "lon": d["longitude"], "prof_km": d["eqDepth"], "mag": d["eqMagnitude"],
        "lugar": lugar, "fuente": "NOAA", "historico": d["year"] < ANIO_INI, "muertes": d["deaths"]})
    print(f"NOAA: {len(noaa)} sismos significativos, {int(noaa.anio_dec.min())}–{int(noaa.anio_dec.max())}")
except Exception as e:
    print(f"No se pudo obtener la base de NOAA ({type(e).__name__}: {e}). Se continúa sin históricos.")
    noaa = pd.DataFrame(columns=["anio_dec", "fecha", "lat", "lon", "prof_km", "mag", "lugar", "fuente", "historico", "muertes"])

# Catálogo unificado: USGS instrumental + históricos de NOAA anteriores a ANIO_INI
cat = pd.concat([usgs, noaa[noaa.historico].drop(columns="muertes")], ignore_index=True)
cat = cat[cat.lon.between(BBOX["lon_min"], BBOX["lon_max"]) & cat.lat.between(BBOX["lat_min"], BBOX["lat_max"])]
cat = cat.dropna(subset=["anio_dec", "lat", "lon", "mag"]).sort_values("anio_dec").reset_index(drop=True)
cat["anio"] = np.floor(cat.anio_dec).astype(int)
inst = cat[~cat.historico]

# Sismo de referencia: el mayor de agosto de 2026 en el catálogo del USGS
_ref = usgs[(usgs.fecha >= "2026-08-01") & (usgs.fecha <= "2026-08-31")].nlargest(1, "mag")
EVENTO_REF = dict(nombre="San José del Palmar, 10-ago-2026", lat=float(_ref.lat.iloc[0]), lon=float(_ref.lon.iloc[0]),
                  prof_km=float(_ref.prof_km.iloc[0]), mag=float(_ref.mag.iloc[0]))
FUENTES = {"USGS": "USGS ComCat", "NOAA": "NOAA/NCEI"}
CREDITO = "Datos: " + ", ".join(FUENTES[f] for f in sorted(cat.fuente.unique())) + "."

print(f"Catálogo unificado: {miles(len(cat))} eventos, {cat.anio.min()}–{cat.anio.max()}; "
      f"{miles(cat.prof_km.isna().sum())} sin profundidad conocida")
print(f"Sismo de referencia: M {EVENTO_REF['mag']:.1f}, {EVENTO_REF['prof_km']:.0f} km de profundidad")
''')

md(r'''
La tabla siguiente lista los ocho sismos con más víctimas mortales. La fecha asume mes julio y día 15 cuando la base no los registra, y la magnitud es de tipos mezclados (en los eventos históricos, derivada de intensidades).
''')

code(r'''
_v = noaa.dropna(subset=["muertes"]).nlargest(8, "muertes").copy()
_t = pd.DataFrame({
    "Fecha": _v["fecha"],
    "Lugar": _v["lugar"],
    "Magnitud": ["—" if pd.isna(m) else f"{m:.1f}".replace(".", ",") for m in _v["mag"]],
    "Víctimas mortales": [miles(m) for m in _v["muertes"]]}).reset_index(drop=True)
_t.index += 1
_t
''')

md(r'''
### 5.1 Completitud en el tiempo

La magnitud de completitud ($M_c$) es el umbral sobre el cual el catálogo registra prácticamente todos los sismos; para el catálogo de 2000 en adelante se estimó en la sección 3. La primera figura muestra el acumulado de sismos según el umbral de magnitud: si el crecimiento fuera actividad real, las tres curvas subirían por igual; lo que ocurre es que solo se dispara la de todos los eventos, con saltos en los años en que cambia la instrumentación.
''')

code(r'''
from matplotlib.colors import LinearSegmentedColormap, Normalize

HITOS = {1973: "Catálogo global PDE/NEIC (1973)", 1993: "Red Sismológica Nacional (1993)"}
fig, ax = plt.subplots(figsize=(8, 4.6))
for umbral, color in [(None, "#c2408c"), (MAG_COMPLETA, "#6a1b7a"), (6.0, "#1b0b2e")]:
    sub = cat if umbral is None else cat[cat.mag >= umbral]
    etiqueta = "Todos los sismos" if umbral is None else f"M ≥ {dec(umbral)}"
    ax.step(sub.anio_dec, np.arange(1, len(sub) + 1), where="post", color=color, lw=1.6, label=etiqueta)
for anio, texto in HITOS.items():
    ax.axvline(anio, color="0.6", lw=0.8, ls=":")
    ax.text(anio - 1.5, 0.03, texto, transform=ax.get_xaxis_transform(), rotation=90,
            ha="right", va="bottom", fontsize=7, color="0.35")
ax.set(yscale="log", xlim=(1550, 2030), xlabel="Año", ylabel="Sismos acumulados (escala log)",
       title="Acumulado de sismos: el salto es instrumental")
ax.legend(frameon=False, fontsize=8, loc="upper left")

n = len(cat)
for anio in (1973, 1993):
    print(f"Eventos desde {anio}: {100 * (cat.anio >= anio).sum() / n:.1f} % del catálogo")
''')

md(r'''
Si el umbral es completo, la tasa anual no debería tener tendencia instrumental. La segunda figura compara la tasa anual de todos los eventos con la de los umbrales altos.
''')

code(r'''
# Tasa anual desde 1973: si el umbral es completo, no debería haber tendencia instrumental
anios = np.arange(1973, int(ANIO_FIN) + 1)
fig, ax = plt.subplots(figsize=(8, 3.6))
todos = inst.anio.value_counts().reindex(anios, fill_value=0)
ax.bar(anios, todos, color="#f6a6b2", width=0.9, label=f"Todos (M ≥ {dec(MAG_MIN)})")
for umbral, color in [(MAG_COMPLETA, "#6a1b7a"), (5.5, "#1b0b2e")]:
    serie = inst[inst.mag >= umbral].anio.value_counts().reindex(anios, fill_value=0)
    ax.plot(anios, serie, color=color, lw=1.6, marker="o", ms=2.5, label=f"M ≥ {dec(umbral)}")
ax.set(yscale="symlog", xlabel="Año", ylabel="Sismos por año", ylim=(0, max(todos.max(), 1) * 6),
       title="Sismos por año según umbral de magnitud (el último año es parcial)")
ax.legend(frameon=False, fontsize=8, ncol=3, loc="upper left")

sub = inst[(inst.mag >= MAG_COMPLETA) & (inst.anio >= 1973) & (inst.anio < int(ANIO_FIN))]
por_anio = sub.anio.value_counts().reindex(anios[:-1], fill_value=0)
pend = np.polyfit(por_anio.index, por_anio.values, 1)[0]
print(f"M ≥ {dec(MAG_COMPLETA)} desde 1973: media {por_anio.mean():.1f} sismos/año, "
      f"tendencia lineal {pend:+.2f} sismos/año por año")
''')

md(r'''
Las curvas de los umbrales altos son estables, mientras que las barras de todos los eventos crecen con la instrumentación: el aumento del número de sismos registrados es un efecto de la red de estaciones y no de la actividad. Por eso, para comparar épocas, conviene filtrar por una magnitud completa.
''')

md(r'''
## 6. Mapa de sismicidad con profundidad y víctimas

El tamaño del círculo indica la magnitud y el color la profundidad focal (la escala se satura en 200 km). Los sismos sin profundidad conocida se dibujan como anillos vacíos y no como superficiales, y los eventos grandes se dibujan primero para que no tapen a los pequeños. Se etiquetan los de mayor magnitud (en negro) y los que más víctimas causaron según NOAA (en rojo); la estrella marca el sismo de referencia de agosto de 2026.
''')

code(r'''
URL_PAISES = ("https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/"
              "ne_50m_admin_0_countries.geojson")
_paises = requests.get(URL_PAISES, timeout=120).json()["features"]

def anillos(feature):
    """Anillos exteriores de un país (Polygon o MultiPolygon) como listas de (lon, lat)."""
    g = feature["geometry"]
    polis = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"]
    return [np.array(p[0]) for p in polis]

anillos_paises = {f["properties"]["ADMIN"]: anillos(f) for f in _paises}
colombia = anillos_paises["Colombia"]

CMAP = LinearSegmentedColormap.from_list("profundidad", ["#fde3df", "#f6a6b2", "#c2408c", "#6a1b7a", "#1b0b2e"])
NORM = Normalize(0, PROF_MAX)

def tam(mag):
    """Área del marcador: crece exponencialmente con la magnitud (M2≈1, M4≈8, M6≈57, M8≈430)."""
    return 2.75 ** (np.clip(np.asarray(mag, dtype=float), 2, 9.5) - 2)

def mapa_base(ax):
    ax.set_facecolor("#b7cde8")
    for nombre, polis in anillos_paises.items():
        for p in polis:
            if (p[:, 0].max() < BBOX["lon_min"] - 6 or p[:, 0].min() > BBOX["lon_max"] + 6
                    or p[:, 1].max() < BBOX["lat_min"] - 6 or p[:, 1].min() > BBOX["lat_max"] + 6):
                continue
            col, lw = ("#7d9189", 0.9) if nombre == "Colombia" else ("#8a9c95", 0.5)
            ax.fill(p[:, 0], p[:, 1], color=col, ec="k" if nombre == "Colombia" else "#333", lw=lw)
    ax.set_xlim(BBOX["lon_min"], BBOX["lon_max"]); ax.set_ylim(BBOX["lat_min"], BBOX["lat_max"])
    ax.set_aspect(1 / np.cos(np.radians(LAT_MEDIA)))
    ax.set_xlabel("Longitud"); ax.set_ylabel("Latitud")
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(True)

def leyenda_magnitud(ax, loc="lower left"):
    marcas = [ax.scatter([], [], s=tam(m), color="0.2", label=f"M{m}") for m in (4, 6, 8)]
    hueco = ax.scatter([], [], s=40, facecolors="none", edgecolors="0.25", linewidths=0.8, label="Prof. desconocida")
    ax.legend(handles=marcas + [hueco], loc=loc, fontsize=7, frameon=True, framealpha=0.85,
              labelspacing=1.1, borderpad=0.9)

fig, ax = plt.subplots(figsize=(7.2, 8.2))
mapa_base(ax)
d_ord = cat.sort_values("mag", ascending=False)             # grandes debajo
con, sin = d_ord[d_ord.prof_km.notna()], d_ord[d_ord.prof_km.isna()]
sc = ax.scatter(con.lon, con.lat, s=tam(con.mag), c=con.prof_km, cmap=CMAP, norm=NORM, alpha=0.75,
                linewidths=0, rasterized=True)
ax.scatter(sin.lon, sin.lat, s=tam(sin.mag), facecolors="none", edgecolors="0.25", linewidths=0.8)
fig.colorbar(sc, ax=ax, shrink=0.6, pad=0.02, extend="max", label="Profundidad (km)")
leyenda_magnitud(ax)

for _, r in cat.nlargest(6, "mag").iterrows():                # etiquetas por magnitud
    ax.annotate(f"M{r.mag:.1f} · {r.anio}", (r.lon, r.lat), xytext=(5, 5), textcoords="offset points",
                fontsize=7, fontweight="bold")
if len(noaa) and noaa.muertes.notna().any():                   # etiquetas por impacto
    for _, r in noaa.dropna(subset=["muertes", "lat", "lon"]).nlargest(6, "muertes").iterrows():
        ax.plot(r.lon, r.lat, marker="x", color="#b00020", ms=5, mew=1.2)
        ax.annotate(f"{r.lugar} {int(r.anio_dec)} · {miles(r.muertes)} muertes", (r.lon, r.lat),
                    xytext=(5, -9), textcoords="offset points", fontsize=6.5, color="#b00020")
ax.plot(EVENTO_REF["lon"], EVENTO_REF["lat"], marker="*", ms=13, color="#ffd400", mec="k", mew=0.8)
ax.set_title(f"Sismicidad de Colombia y territorios vecinos, {cat.anio.min()}–{cat.anio.max()}\n"
             f"{miles(len(cat))} sismos · ★ {EVENTO_REF['nombre']}", fontsize=10)
fig.text(0.01, 0.005, f"{CREDITO} Límites: Natural Earth.", fontsize=6.5, color="0.35")
plt.show()
''')

md(r'''
### 6.1 Animación a ritmo constante

La animación recorre la sismicidad de 1900 a 2026 con el mismo número de años por cuadro, de modo que el reloj avanza a velocidad constante, y compara dos paneles con el mismo reloj: a la izquierda, todo el catálogo; a la derecha, solo los sismos por encima de la magnitud de completitud. Si el aumento del panel izquierdo fuera actividad real, el derecho crecería igual. El video se genera con el codificador del sistema o con el paquete `imageio-ffmpeg` (`pip install imageio-ffmpeg`) y pesa unos 200 KB.
''')

code(r'''
from matplotlib import animation

ANIM_INI = 1900       # año de inicio de la animación
ANIOS_POR_CUADRO = 1  # años que avanza cada cuadro
FPS = 12              # cuadros por segundo

# Codificador de video: el del sistema o, si no hay, el que trae el paquete imageio-ffmpeg
import shutil, tempfile, os
TMP = tempfile.mkdtemp()
if not shutil.which("ffmpeg"):
    try:
        import imageio_ffmpeg
        plt.rcParams["animation.ffmpeg_path"] = imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        pass

def animar(df, mag_completa=MAG_COMPLETA, anio_ini=ANIM_INI, paso=ANIOS_POR_CUADRO, fps=FPS):
    df = df[df.anio_dec >= anio_ini].sort_values("anio_dec")
    grupos = [df, df[df.mag >= mag_completa]]
    titulos = ["Todo el catálogo", f"Solo M ≥ {dec(mag_completa)}"]
    hay_video = animation.writers.is_available("ffmpeg")
    if not hay_video:
        paso = max(paso, 2)                                   # el GIF pesa mucho: menos cuadros
    tiempos = np.append(np.arange(anio_ini, ANIO_FIN, paso), [ANIO_FIN] * fps)   # pausa final de 1 s

    fig, axs = plt.subplots(1, 2, figsize=(10, 6.3), dpi=90)
    cmap = CMAP.copy(); cmap.set_bad("0.35")
    capas = []
    for ax, g, titulo in zip(axs, grupos, titulos):
        mapa_base(ax); ax.set_xlabel(""); ax.set_ylabel(""); ax.tick_params(labelsize=7)
        ax.set_title(titulo, fontsize=11, fontweight="bold")
        sc = ax.scatter([], [], s=[], c=[], cmap=cmap, norm=NORM, alpha=0.75, linewidths=0)
        txt = ax.text(0.03, 0.03, "", transform=ax.transAxes, fontsize=10,
                      bbox=dict(fc="white", ec="none", alpha=0.8))
        capas.append((sc, txt, g.anio_dec.to_numpy(), g[["lon", "lat"]].to_numpy(),
                      tam(g.mag), np.ma.masked_invalid(g.prof_km.to_numpy(dtype=float))))
    reloj = fig.suptitle("", fontsize=16, fontweight="bold", y=0.98)
    fig.text(0.5, 0.015, "El aumento del panel izquierdo refleja mejor monitoreo, no más actividad sísmica. "
             + CREDITO, ha="center", fontsize=8.5)
    fig.subplots_adjust(left=0.05, right=0.98, top=0.9, bottom=0.08, wspace=0.12)

    def actualizar(i):
        t = tiempos[i]
        for sc, txt, tt, xy, s, c in capas:
            k = np.searchsorted(tt, t, side="right")
            sc.set_offsets(xy[:k]); sc.set_sizes(s[:k]); sc.set_array(c[:k])
            txt.set_text(f"{miles(k)} sismos")
        reloj.set_text(str(int(t)))
        return [c[0] for c in capas]

    anim = animation.FuncAnimation(fig, actualizar, frames=len(tiempos), interval=1000 / fps)
    if hay_video:
        salida = os.path.join(TMP, "animacion_sismicidad.mp4")
        # calidad constante (CRF 28): el video pesa unos 200 KB con poca pérdida visual
        anim.save(salida, writer=animation.FFMpegWriter(fps=fps, extra_args=["-crf", "28", "-preset", "slow", "-pix_fmt", "yuv420p"]))
    else:
        salida = os.path.join(TMP, "animacion_sismicidad.gif")
        anim.save(salida, writer=animation.PillowWriter(fps=fps))
    plt.close(fig)
    return salida

archivo_anim = animar(cat)
print("Animación guardada en", archivo_anim)
''')

code(r'''
from IPython.display import Video, Image, display
if archivo_anim.endswith(".mp4"):
    display(Video(archivo_anim, embed=True, html_attributes="controls loop muted playsinline"))
else:
    display(Image(filename=archivo_anim))
''')

md(r'''
## 7. Cortes transversales

Un corte vertical muestra cómo se distribuye la sismicidad en profundidad. El siguiente proyecta todo el cuadrante sobre un solo plano, Sur-Norte y Oeste-Este, hasta 200 km y con exageración vertical ×3, con la escala horizontal en kilómetros y los extremos rotulados. Hay dos advertencias de lectura: la exageración ×3 hace que una placa que buza 30° se vea a unos 60°, y al proyectar más de 2 000 km de país sobre un plano, estructuras que están a cientos de kilómetros entre sí aparecen una al lado de la otra.
''')

code(r'''
def corte(ax, df, eje="OE", banda=None, exag=EXAG_VERTICAL, lim=None, titulo=""):
    """Corte vertical. eje='OE' (mirando al norte) o 'SN' (mirando al oeste).
    banda=(min, max) limita la franja perpendicular al corte, en grados."""
    d = df[df.prof_km.notna() & (df.prof_km <= PROF_MAX)]
    if eje == "OE":
        if banda: d = d[d.lat.between(*banda)]
        h, origen, km, extremos = d.lon, BBOX["lon_min"], KM_LON, ("Oeste", "Este")
        lim = lim or (BBOX["lon_min"], BBOX["lon_max"]); ref = EVENTO_REF["lon"]
        en_banda = banda is None or banda[0] <= EVENTO_REF["lat"] <= banda[1]
    else:
        if banda: d = d[d.lon.between(*banda)]
        h, origen, km, extremos = d.lat, BBOX["lat_min"], KM_LAT, ("Sur", "Norte")
        lim = lim or (BBOX["lat_min"], BBOX["lat_max"]); ref = EVENTO_REF["lat"]
        en_banda = banda is None or banda[0] <= EVENTO_REF["lon"] <= banda[1]
    d = d.assign(h_km=(h - origen) * km).sort_values("mag", ascending=False)
    x0, x1 = [(v - origen) * km for v in lim]

    ax.set_facecolor("#e9e7ea")
    for z in (30, 70, 120, 150):
        ax.axhline(z, color="white", lw=0.8, zorder=0)
    ax.scatter(d.h_km, d.prof_km, s=tam(d.mag) * 0.6, c=d.prof_km, cmap=CMAP, norm=NORM,
               alpha=0.7, linewidths=0, rasterized=True)
    if en_banda and EVENTO_REF["prof_km"] <= PROF_MAX:
        ax.plot((ref - origen) * km, EVENTO_REF["prof_km"], marker="*", ms=14, color="#ffd400",
                mec="k", mew=0.8, zorder=5)
    ax.set_xlim(x0, x1); ax.set_ylim(PROF_MAX, 0); ax.set_aspect(exag)
    ax.set_yticks([0, 30, 70, 120, 150, PROF_MAX]); ax.set_ylabel("Profundidad (km)")
    ax.set_xlabel(f"Distancia {extremos[0]} → {extremos[1]} (km)")
    ax.annotate(f"◀ {extremos[0]}", (0, 1), xytext=(0, 3), xycoords="axes fraction",
                textcoords="offset points", fontsize=8, fontweight="bold")
    ax.annotate(f"{extremos[1]} ▶", (1, 1), xytext=(0, 3), xycoords="axes fraction",
                textcoords="offset points", fontsize=8, fontweight="bold", ha="right")
    ax.set_title(f"{titulo}  ·  exageración vertical ×{dec(exag)}  ·  {miles(len(d))} sismos", fontsize=9, pad=16)
    return d

fig, axs = plt.subplots(2, 1, figsize=(10, 7.6))
corte(axs[0], cat, "SN", titulo="Corte Sur-Norte (mirando al oeste)")
corte(axs[1], cat, "OE", titulo="Corte Oeste-Este (mirando al norte)")
fig.tight_layout(); plt.show()
''')

md(r'''
### 7.1 Cortes por franjas

En lugar de proyectar todo el país, se toman franjas de latitud. Así se separan los dos segmentos que el corte anterior superpone: el del **nido de Bucaramanga** y el del **occidente (Chocó–Eje Cafetero)**, donde ocurrió el sismo de agosto de 2026 (★). El último panel repite la franja occidental **sin exageración vertical**, para mostrar la geometría real.
''')

code(r'''
FRANJAS = {
    "Nido de Bucaramanga (6,3°–7,3° N)": (6.3, 7.3),
    "Chocó – Eje Cafetero (4,3°–5,7° N)": (4.3, 5.7),
}
LIM_LON = (-79.5, -71.0)

fig = plt.figure(figsize=(9, 9.6))
gs = fig.add_gridspec(3, 1, height_ratios=[EXAG_VERTICAL, EXAG_VERTICAL, 1.25], hspace=0.45)
for i, (nombre, banda) in enumerate(FRANJAS.items()):
    corte(fig.add_subplot(gs[i]), cat, "OE", banda=banda, lim=LIM_LON, titulo=nombre)
ultima = list(FRANJAS.items())[-1]
corte(fig.add_subplot(gs[2]), cat, "OE", banda=ultima[1], lim=LIM_LON, exag=1, titulo=ultima[0])
plt.show()
''')

md(r'''
## 8. Vista 3D interactiva

La vista 3D permite girar y acercar la nube de sismos para ver cómo cambia la profundidad con la posición. Se limita a magnitud 4 o más y a 200 km para que sea liviana; el eje vertical conserva la exageración de los cortes y el borde de Colombia se dibuja sobre la superficie. Pasa el cursor sobre un punto para ver su magnitud, fecha y profundidad.
''')

code(r'''
import plotly.graph_objects as go

d3 = cat[cat.prof_km.notna() & (cat.prof_km <= PROF_MAX) & (cat.mag >= 4.0)]
escala = [[i / 4, c] for i, c in enumerate(["#fde3df", "#f6a6b2", "#c2408c", "#6a1b7a", "#1b0b2e"])]

fig3d = go.Figure()
for p in colombia:                                              # borde de Colombia
    fig3d.add_trace(go.Scatter3d(x=list(p[:, 0]), y=list(p[:, 1]), z=[0] * len(p), mode="lines",
                                 line=dict(color="black", width=3), hoverinfo="skip", showlegend=False))
fig3d.add_trace(go.Scatter3d(
    x=d3.lon, y=d3.lat, z=-d3.prof_km, mode="markers", showlegend=False,
    marker=dict(size=np.clip((d3.mag - 3) * 1.8, 1.5, 12), color=d3.prof_km, colorscale=escala, cmin=0,
                cmax=PROF_MAX, opacity=0.75, line=dict(width=0), colorbar=dict(title="Prof. (km)", len=0.6)),
    text=[f"M{m:.1f} · {f}<br>{p:.0f} km" for m, f, p in zip(d3.mag, d3.fecha, d3.prof_km)], hoverinfo="text"))
fig3d.add_trace(go.Scatter3d(x=[EVENTO_REF["lon"]], y=[EVENTO_REF["lat"]], z=[-EVENTO_REF["prof_km"]],
    mode="markers+text", text=["★ 10-ago-2026"], textposition="top center", showlegend=False,
    marker=dict(size=7, color="#ffd400", symbol="diamond", line=dict(color="black", width=2))))

dx = (BBOX["lon_max"] - BBOX["lon_min"]) * KM_LON
dy = (BBOX["lat_max"] - BBOX["lat_min"]) * KM_LAT
fig3d.update_layout(
    title=f"Sismicidad M ≥ 4 hasta {PROF_MAX} km · exageración vertical ×{dec(EXAG_VERTICAL)}",
    height=620, margin=dict(l=0, r=0, t=40, b=0),
    scene=dict(xaxis_title="Longitud", yaxis_title="Latitud", zaxis_title="Profundidad (km)",
               xaxis=dict(range=[BBOX["lon_min"], BBOX["lon_max"]]),
               yaxis=dict(range=[BBOX["lat_min"], BBOX["lat_max"]]), zaxis=dict(range=[-PROF_MAX, 0]),
               aspectmode="manual", aspectratio=dict(x=1, y=dy / dx, z=PROF_MAX * EXAG_VERTICAL / dx),
               camera=dict(eye=dict(x=-1.3, y=-1.6, z=0.9))))
fig3d.show()
''')

md(r'''
## 9. Análisis departamental

Los análisis de la sismicidad de todo el país se consultan, en la práctica, por territorio: un departamento o un municipio necesita una lectura de su entorno sísmico que se pueda insertar en sus documentos de gestión del riesgo, como las fichas departamentales de escenarios de riesgo. Esta sección presenta un piloto para **Córdoba**: una figura de cuatro paneles y dos párrafos que resumen la sismicidad del departamento y de su entorno inmediato, y una función que repite el análisis para cualquier otro departamento de Colombia cambiando solo su nombre.

La figura usa el catálogo ampliado de la sección 5 y los límites departamentales de geoBoundaries (Runfola et al., 2020). Como la sismicidad no se detiene en un límite administrativo, el análisis no se restringe al departamento: considera los sismos dentro de Córdoba y los que ocurren en un radio de 100 km de su frontera, que son los que pueden sentirse en su territorio.
''')

code(r'''
import json, unicodedata
from datetime import datetime
from matplotlib.path import Path as MPath
from matplotlib.lines import Line2D
from scipy.spatial import cKDTree

URL_DEPTOS = ("https://github.com/wmgeolab/geoBoundaries/raw/9469f09/releaseData/gbOpen/COL/ADM1/"
              "geoBoundaries-COL-ADM1_simplified.geojson")
COLOR_PROF = {"Superficial (≤ 70 km)": "#e74c3c", "Intermedia (70–300 km)": "#f39c12", "Profunda (> 300 km)": "#2980b9"}


def _es(x, dec=1):
    """Número con coma decimal y espacio como separador de miles."""
    return f"{x:,.{dec}f}".replace(",", " ").replace(".", ",")


def _norm(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower().strip()


def cargar_departamentos(url=URL_DEPTOS):
    """Límites departamentales de Colombia (geoBoundaries ADM1) como {nombre: [anillos (lon, lat)]}."""
    feats = requests.get(url, timeout=120).json()["features"]
    salida = {}
    for f in feats:
        g = f["geometry"]
        polis = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"]
        salida[f["properties"]["shapeName"]] = [np.array(p[0]) for p in polis]
    return salida


def _buscar(deptos, nombre):
    for k in deptos:
        if _norm(k) == _norm(nombre):
            return k
    raise KeyError(f"'{nombre}' no está en la lista de departamentos: {sorted(deptos)}")


def _km(lon, lat, lat0):
    """Proyección plana local en kilómetros."""
    return np.c_[np.asarray(lon) * 111.32 * np.cos(np.radians(lat0)), np.asarray(lat) * 110.57]


def distancia_al_departamento(anillos, lon, lat, lat0, paso_km=3):
    """Distancia (km) de cada punto al límite del departamento (0 si está dentro) y máscara de interior."""
    lon, lat = np.asarray(lon, float), np.asarray(lat, float)
    pts = []
    for e in anillos:
        xy = _km(e[:, 0], e[:, 1], lat0)
        for a, b in zip(xy[:-1], xy[1:]):
            n = max(2, int(np.hypot(*(b - a)) / paso_km))
            pts.append(a + (b - a) * np.linspace(0, 1, n, endpoint=False)[:, None])
    d, _ = cKDTree(np.vstack(pts)).query(_km(lon, lat, lat0))
    dentro = np.zeros(len(lon), bool)
    for e in anillos:
        dentro |= MPath(e).contains_points(np.c_[lon, lat])
    return np.where(dentro, 0.0, d), dentro


def _periodo(T):
    """Período de retorno como texto: meses si es menor de un año y años en otro caso."""
    return f"cada {_es(T * 12, 0)} meses" if T < 1 else f"cada {_es(T, 0 if T >= 10 else 1)} años"


def clase_prof(p):
    return "Superficial (≤ 70 km)" if p <= 70 else ("Intermedia (70–300 km)" if p <= 300 else "Profunda (> 300 km)")


def indicadores_sismicos(depto, catalogo, deptos, radio_km=100, mag_completa=4.5, anio_completo=1973):
    """Indicadores sísmicos de un departamento y su entorno.
    catalogo: DataFrame con lat, lon, prof_km, mag, fecha (AAAA-MM-DD), anio_dec, lugar (y, opcional, historico).
    Devuelve (indicadores, eventos_en_el_radio): los indicadores son un dict serializable a JSON."""
    nombre = _buscar(deptos, depto)
    anillos = deptos[nombre]
    lat0 = float(np.mean(np.concatenate([e[:, 1] for e in anillos])))
    c = catalogo[~catalogo.get("historico", False)].copy() if "historico" in catalogo else catalogo.copy()
    dist, dentro = distancia_al_departamento(anillos, c.lon, c.lat, lat0)
    c = c.assign(dist_km=dist, dentro=dentro)
    area = c[c.dist_km <= radio_km].copy()
    anio_fin = float(c.anio_dec.max())
    comp = area[(area.mag >= mag_completa) & (area.anio_dec >= anio_completo)]
    anos = anio_fin - anio_completo
    b = float(np.log10(np.e) / (comp.mag.mean() - (mag_completa - 0.05)))          # Aki-Utsu, intervalo de 0,1
    se = b / np.sqrt(len(comp))
    tasa = lambda m: len(comp) / anos * 10 ** (-b * (m - mag_completa))               # sismos por año de magnitud >= m
    mayor = area.nlargest(1, "mag").iloc[0]
    ind = dict(
        departamento=nombre, radio_km=radio_km, mag_minima_catalogo=float(c.mag.min()),
        periodo=[int(c.anio_dec.min()), int(anio_fin)], mag_completa=mag_completa, anio_completo=anio_completo,
        n_dentro=int(area.dentro.sum()), n_hasta_50km=int((area.dist_km <= 50).sum()), n_en_radio=int(len(area)),
        n_completos_en_radio=int(len(comp)), pct_superficiales=float(100 * (comp.prof_km <= 70).mean()),
        b=b, b_error=float(se),
        retorno_anios={str(m): float(1 / tasa(m)) for m in (5, 6, 7)},
        mayor=dict(mag=float(mayor.mag), fecha=str(mayor.fecha), prof_km=float(mayor.prof_km), lugar=str(mayor.lugar),
                   dist_km=float(mayor.dist_km)),
        mayores=[dict(mag=float(r.mag), fecha=str(r.fecha), prof_km=float(r.prof_km), lugar=str(r.lugar),
                      dist_km=float(r.dist_km)) for r in area.nlargest(5, "mag").itertuples()])
    return ind, area, comp


def ficha_sismica(depto, catalogo, deptos, radio_km=100, mag_completa=4.5, anio_completo=1973, lugares=None):
    """Figura de cuatro paneles (mapa, sismos por año, Gutenberg-Richter y mayores sismos) de un departamento.
    lugares: dict opcional {nombre: (lat, lon)} para marcar localidades en el mapa. Devuelve (figura, indicadores)."""
    ind, area, comp = indicadores_sismicos(depto, catalogo, deptos, radio_km, mag_completa, anio_completo)
    nombre = ind["departamento"]
    anillos = deptos[nombre]
    lat0 = float(np.mean(np.concatenate([e[:, 1] for e in anillos])))
    tam = lambda m: np.clip((np.asarray(m, float) - 2.0) ** 2.3 * 2.2, 3, 400)

    fig = plt.figure(figsize=(8.4, 8.0))
    gs = fig.add_gridspec(2, 2, hspace=0.34, wspace=0.26, left=0.07, right=0.98, top=0.915, bottom=0.15)
    ax = fig.add_subplot(gs[0, 0])

    # (a) mapa ---------------------------------------------------------------
    todos = np.concatenate(anillos)
    m_deg = radio_km / 105 + 0.15
    x0, x1 = todos[:, 0].min() - m_deg, todos[:, 0].max() + m_deg
    y0, y1 = todos[:, 1].min() - m_deg, todos[:, 1].max() + m_deg
    ax.set_facecolor("#dbe8f3")
    for k, polis in deptos.items():
        for p in polis:
            ax.fill(p[:, 0], p[:, 1], color="#f4f1ea" if k != nombre else "#fbe3b5", ec="#8a8a8a" if k != nombre else "k",
                    lw=0.5 if k != nombre else 1.4, zorder=1 if k != nombre else 2)
    gx, gy = np.meshgrid(np.linspace(x0, x1, 130), np.linspace(y0, y1, 130))
    gd, _ = distancia_al_departamento(anillos, gx.ravel(), gy.ravel(), lat0)
    ax.contour(gx, gy, gd.reshape(gx.shape), levels=[50, radio_km], colors="k", linestyles=["--", ":"], linewidths=0.8, zorder=3)
    for clase, col in COLOR_PROF.items():
        s = area[area.prof_km.map(clase_prof) == clase].sort_values("mag", ascending=False)
        ax.scatter(s.lon, s.lat, s=tam(s.mag), color=col, alpha=0.65, linewidths=0.3, edgecolors="k", zorder=4)
    for nom, (la, lo) in (lugares or {}).items():
        ax.plot(lo, la, marker="*", ms=11, color="#ffd400", mec="k", mew=0.8, zorder=6)
        ax.annotate(nom, (lo, la), xytext=(6, -2), textcoords="offset points", fontsize=8, fontweight="bold", zorder=6)
    ax.set_xlim(x0, x1); ax.set_ylim(y0, y1); ax.set_aspect(1 / np.cos(np.radians(lat0)))
    ax.set_xlabel("Longitud"); ax.set_ylabel("Latitud"); ax.tick_params(labelsize=8)
    ax.set_title(f"(a) Epicentros en {nombre} y a menos de {radio_km} km", fontsize=9.5, fontweight="bold", loc="left")
    asa = [Line2D([], [], marker="o", ls="", color=col, mec="k", mew=0.3, ms=7, label=cl) for cl, col in COLOR_PROF.items()
           if cl in set(area.prof_km.map(clase_prof))]
    asa += [Line2D([], [], marker="o", ls="", color="0.55", mec="k", mew=0.3, ms=np.sqrt(tam(m)), label=f"M {m}") for m in (3, 5, 7)]
    asa += [Line2D([], [], color="k", ls="--", lw=0.8, label="50 km del límite"), Line2D([], [], color="k", ls=":", lw=0.8, label=f"{radio_km} km del límite")]
    fig.legend(handles=asa, loc="lower center", bbox_to_anchor=(0.5, 0.035), ncol=4, fontsize=7.4, frameon=False, columnspacing=1.8, handletextpad=0.4)

    # (b) sismos por año -----------------------------------------------------
    ax2 = fig.add_subplot(gs[0, 1])
    anios = np.arange(anio_completo, int(ind["periodo"][1]) + 1)
    capas = [("Dentro del departamento", comp.dentro, "#b2182b"), ("Hasta 50 km", (~comp.dentro) & (comp.dist_km <= 50), "#ef8a62"),
             (f"50 a {radio_km} km", comp.dist_km > 50, "#fddbc7")]
    base = np.zeros(len(anios))
    for etiqueta, m, col in capas:
        cuenta = comp[m].assign(a=lambda d: np.floor(d.anio_dec).astype(int)).a.value_counts().reindex(anios, fill_value=0).to_numpy()
        ax2.bar(anios, cuenta, bottom=base, color=col, width=0.85, label=etiqueta, ec="0.35", lw=0.3)
        base += cuenta
    ax2.set_title(f"(b) Sismos de M ≥ {_es(mag_completa)} por año", fontsize=9.5, fontweight="bold", loc="left")
    ax2.set_ylabel("Número de sismos", fontsize=8.5); ax2.tick_params(labelsize=8)
    ax2.legend(fontsize=7, frameon=False, loc="upper left")
    ax2.text(0.99, 0.97, "2026 es un año parcial", transform=ax2.transAxes, ha="right", va="top", fontsize=6.8, color="0.4")

    # (c) Gutenberg-Richter --------------------------------------------------
    ax3 = fig.add_subplot(gs[1, 0])
    anos = ind["periodo"][1] - anio_completo
    mm = np.arange(mag_completa, comp.mag.max() + 0.05, 0.1)
    obs = np.array([(comp.mag >= m - 1e-9).sum() for m in mm]) / anos
    ok = obs > 0
    ax3.semilogy(mm[ok], obs[ok], "o", ms=3.5, color="#0154a5", label="Observado")
    mx = np.arange(mag_completa, 7.6, 0.1)
    ajuste = len(comp) / anos * 10 ** (-ind["b"] * (mx - mag_completa))
    ax3.semilogy(mx, ajuste, color="#b2182b", lw=1.6, label=f"Ajuste: b = {_es(ind['b'], 2)} ± {_es(ind['b_error'], 2)}")
    for m in (5, 6, 7):
        T = ind["retorno_anios"][str(m)]
        ax3.plot([m], [1 / T], marker="D", ms=5, color="#b2182b", mec="k", mew=0.5, zorder=5)
        ax3.annotate(f"M ≥ {m}: {_periodo(T)}", (m, 1 / T), xytext=(8, 5), textcoords="offset points", fontsize=7.2, va="bottom")
    ax3.set_title("(c) Frecuencia de sismos y períodos de retorno", fontsize=9.5, fontweight="bold", loc="left")
    ax3.set_xlabel("Magnitud (M)", fontsize=8.5); ax3.set_ylabel("Sismos por año (≥ M)", fontsize=8.5)
    ax3.tick_params(labelsize=8); ax3.grid(True, which="major", alpha=0.3)
    ax3.legend(fontsize=7, frameon=False, loc="upper right")

    # (d) mayores sismos -----------------------------------------------------
    ax4 = fig.add_subplot(gs[1, 1])
    top = ind["mayores"][::-1]
    etiquetas = [f"{r['fecha'][:4]} · {r['lugar'].split(' of ')[-1].split(',')[0]}" for r in top]
    ys = range(len(top))
    ax4.hlines(ys, 5, [r["mag"] for r in top], color="0.6", lw=1.2)
    ax4.scatter([r["mag"] for r in top], ys, s=70, color=[COLOR_PROF[clase_prof(r["prof_km"])] for r in top], ec="k", lw=0.5, zorder=3)
    for i, r in enumerate(top):
        ax4.text(r["mag"] + 0.12, i, f"M {_es(r['mag'])} · prof. {_es(r['prof_km'], 0)} km\na {_es(r['dist_km'], 0)} km del límite", va="center", fontsize=6.8)
    ax4.set_yticks(list(ys)); ax4.set_yticklabels(etiquetas, fontsize=7.5)
    ax4.set_xlim(5, max(r["mag"] for r in top) + 1.8); ax4.set_ylim(-0.6, len(top) - 0.4)
    ax4.set_xlabel("Magnitud (M)", fontsize=8.5); ax4.tick_params(axis="x", labelsize=8); ax4.grid(True, axis="x", alpha=0.3)
    ax4.set_title(f"(d) Los cinco mayores sismos a menos de {radio_km} km", fontsize=9.5, fontweight="bold", loc="left")

    fig.suptitle(f"Sismicidad en {nombre} y su entorno", fontsize=12.5, fontweight="bold", x=0.07, ha="left", y=0.985)
    fig.text(0.07, 0.008, f"Catálogo USGS ComCat desde {ind['periodo'][0]} (M ≥ {_es(ind['mag_minima_catalogo'])}); los paneles (b) y (c) usan M ≥ {_es(mag_completa)} desde {anio_completo}. "
             "Límites: geoBoundaries (2017).", fontsize=6.8, color="0.35")
    return fig, ind
''')

code(r'''
def redactar_parrafos(ind):
    """Dos párrafos explicativos (Markdown) a partir de los indicadores de ficha_sismica."""
    d, m = ind["departamento"], ind["mayor"]
    T5, T6 = ind["retorno_anios"]["5"], ind["retorno_anios"]["6"]
    fecha = datetime.strptime(m["fecha"], "%Y-%m-%d")
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    lugar = m["lugar"].split(" of ")[-1].split(",")[0]
    p1 = (f"{d} registra poca sismicidad propia, pero está rodeado de fuentes activas. Entre {ind['periodo'][0]} y {ind['periodo'][1]} el catálogo del USGS "
          f"ubica {_es(ind['n_dentro'], 0)} sismos de magnitud {_es(ind['mag_minima_catalogo'])} o más dentro del departamento, {_es(ind['n_hasta_50km'], 0)} a menos de 50 km de su límite "
          f"y {_es(ind['n_en_radio'], 0)} a menos de {ind['radio_km']} km (figura, panel a). El mayor sismo en ese radio fue el de magnitud {_es(m['mag'])} del "
          f"{fecha.day} de {meses[fecha.month - 1]} de {fecha.year}, con epicentro en {lugar}, a {_es(m['dist_km'], 0)} km del departamento y {_es(m['prof_km'], 0)} km de profundidad (panel d). "
          f"La sismicidad cercana es sobre todo superficial: {_es(ind['pct_superficiales'], 0)} % de los sismos de magnitud {_es(ind['mag_completa'])} o más ocurre a 70 km de profundidad o menos.")
    p2 = (f"Con los sismos de magnitud {_es(ind['mag_completa'])} o más desde {ind['anio_completo']}, el período en que el catálogo es completo para ese umbral, la relación de "
          f"Gutenberg-Richter da un parámetro b de {_es(ind['b'], 2)} ± {_es(ind['b_error'], 2)}, lo que equivale a esperar, en promedio, un sismo de magnitud 5 o más {_periodo(T5)} y uno de magnitud 6 o más {_periodo(T6)} dentro de ese radio (panel c). Esta lectura describe la frecuencia de sismos en el entorno, no la amenaza en el territorio: no considera la "
          f"atenuación del movimiento con la distancia ni el efecto del suelo local, y mezcla tipos de magnitud sin homogeneizar, por lo que debe complementarse con estudios de amenaza y microzonificación "
          f"antes de usarse en decisiones de planificación.")
    return p1 + "\n\n" + p2


def guardar_ficha(fig, ind, parrafos, prefijo):
    """Escribe la figura (PNG a 300 ppp), los indicadores (JSON) y los párrafos (Markdown) para reutilizarlos en otros productos."""
    fig.savefig(f"{prefijo}.png", dpi=300, bbox_inches="tight")
    with open(f"{prefijo}.json", "w", encoding="utf-8") as f:
        json.dump(ind, f, ensure_ascii=False, indent=2)
    with open(f"{prefijo}.md", "w", encoding="utf-8") as f:
        f.write(parrafos + "\n")
''')

code(r'''
deptos = cargar_departamentos()
fig, ind = ficha_sismica("Córdoba", cat, deptos, lugares={"Montería": (8.75, -75.88)})
parrafos = redactar_parrafos(ind)
plt.show()
''')

md(r'''
Los dos párrafos siguientes salen del mismo cálculo que la figura: (a) epicentros dentro del departamento y a menos de 100 km de su límite, con color por profundidad y tamaño por magnitud; (b) sismos de magnitud 4,5 o más por año desde 1973, según su distancia al departamento; (c) frecuencia anual de sismos por magnitud, ajuste de Gutenberg-Richter y períodos de retorno aproximados; (d) los cinco mayores sismos a menos de 100 km. Fuente: USGS ComCat; límites departamentales: geoBoundaries (2017).
''')

code(r'''
from IPython.display import Markdown, display
display(Markdown(parrafos))
''')

code(r'''
_c = ind["retorno_anios"]
_t = pd.DataFrame({
    "Indicador": [f"Sismos dentro del departamento (M ≥ {_es(ind['mag_minima_catalogo'])})", "Sismos a menos de 50 km del límite", f"Sismos a menos de {ind['radio_km']} km del límite",
                  f"Sismos de M ≥ {_es(ind['mag_completa'])} en el radio desde {ind['anio_completo']}", "Parámetro b (máxima verosimilitud)",
                  "Período de retorno de M ≥ 5 (años)", "Período de retorno de M ≥ 6 (años)", "Mayor sismo en el radio"],
    "Valor": [_es(ind["n_dentro"], 0), _es(ind["n_hasta_50km"], 0), _es(ind["n_en_radio"], 0), _es(ind["n_completos_en_radio"], 0),
              f"{_es(ind['b'], 2)} ± {_es(ind['b_error'], 2)}", _es(_c["5"], 1), _es(_c["6"], 0),
              f"M {_es(ind['mayor']['mag'])}, {ind['mayor']['fecha']}"]}).set_index("Indicador")
_t
''')

md(r'''
### 9.1 Cómo reutilizar el análisis

La función `ficha_sismica(departamento, catalogo, deptos)` recibe el nombre de un departamento (con o sin tilde), un catálogo con las columnas `lat`, `lon`, `prof_km`, `mag`, `fecha`, `anio_dec` y `lugar`, y los límites que entrega `cargar_departamentos()`. Devuelve la figura y un diccionario de indicadores serializable a JSON, y `redactar_parrafos` y `guardar_ficha` producen los párrafos y los archivos (PNG a 300 ppp, JSON y Markdown) para insertarlos en otros documentos. El radio (`radio_km`), la magnitud de completitud (`mag_completa`) y el año desde el cual se considera completo el catálogo (`anio_completo`) son parámetros. Para otro departamento basta cambiar el nombre: `ficha_sismica("Antioquia", cat, deptos)`. Como el catálogo es un `DataFrame` de pandas, puede sustituirse por uno propio, siempre que tenga esas columnas.
''')

md(r'''
## 10. Lectura y límites

**Qué se puede afirmar.** El crecimiento del número de sismos registrados es un efecto de instrumentación: desaparece al filtrar por una magnitud completa. La sismicidad intermedia dibuja placas que se hunden hacia el este, con dos segmentos distintos, y el sismo de agosto de 2026 se ubica dentro del segmento occidental, a profundidad intermedia.

**Qué no.** Este cuaderno describe **amenaza**, no riesgo: no incluye exposición ni vulnerabilidad. La sismicidad cortical (la que más daño suele causar) queda mal representada en cortes a escala de país.

**Límites de los datos.**

- El catálogo del USGS es completo para la región solo desde magnitudes cercanas a 4,5; no reproduce los conteos del catálogo del Servicio Geológico Colombiano.
- Mezcla tipos de magnitud (Mw, mb, Ml, Ms) sin homogeneizar. El Catálogo Sísmico Integrado del SGC sí lo hace (Montejo et al., 2023).
- Muchas profundidades antiguas son valores fijos asignados por la agencia (10, 33, 35 km) y las incertidumbres en profundidad son mayores que las horizontales; la exageración vertical las amplifica.
- Las magnitudes históricas se derivan de intensidades y los eventos anteriores a 1900 dependen de lo que quedó documentado.
- La conversión de grados a kilómetros usa una aproximación plana con la latitud media del cuadrante.
''')

md(r'''
## 11. Qué sigue

- Sustituir el catálogo USGS por el del **SGC**, con su autorización y licencia, y comparar la magnitud de completitud.
- Separar fuentes (subducción, cortical, nido) y estimar $a$ y $b$ por fuente.
- Pasar de la sismicidad a la amenaza con modelos de movimiento del suelo (ver [](301_sismo.md)).

**Referencias.** Aki, K. (1965). Maximum likelihood estimate of *b* in the formula log N = a − bM and its confidence limits. *Bulletin of the Earthquake Research Institute*, 43, 237-239. Montejo, J., Arcila, M. y Zornosa, D. (2023). Catálogo Sísmico Integrado para Colombia. *Boletín Geológico*, 50(1). https://doi.org/10.32685/0120-1425/bol.geol.50.1.2023.665. NOAA National Centers for Environmental Information, Global Significant Earthquake Database. https://doi.org/10.7289/V5TD9V7K. Runfola, D. et al. (2020). geoBoundaries: A global database of political administrative boundaries. *PLOS ONE*, 15(4), e0231866. https://doi.org/10.1371/journal.pone.0231866. USGS Earthquake Hazards Program, FDSN Event Web Service. Utsu, T. (1966). A statistical significance test of the difference in b-value between two earthquake groups. *Journal of Physics of the Earth*, 14, 37-40. Wiemer, S. y Wyss, M. (2000). Minimum magnitude of completeness in earthquake catalogs. *Bulletin of the Seismological Society of America*, 90(4), 859–869.
''')

