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

La magnitud de completitud ($M_c$) es el umbral sobre el cual el catálogo registra prácticamente todos los sismos. Se estima aquí por máxima curvatura (el intervalo de magnitud más frecuente, más una corrección de 0,2; Wiemer y Wyss, 2000) en ventanas de cinco años, lo que da una estimación gruesa, suficiente para elegir un umbral de filtrado. La primera figura muestra el acumulado de sismos según el umbral de magnitud: si el crecimiento fuera actividad real, las tres curvas subirían por igual; lo que ocurre es que solo se dispara la de todos los eventos, con saltos en los años en que cambia la instrumentación.
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
La segunda figura presenta $M_c$ en el tiempo: el piso de detección baja a medida que se instalan estaciones.
''')

code(r'''
def mc_maxc(mags, paso=0.1, correccion=0.2, n_min=50):
    """Magnitud de completitud por máxima curvatura (Wiemer y Wyss, 2000)."""
    m = np.round(pd.Series(mags).dropna().to_numpy(), 1)
    if len(m) < n_min:
        return np.nan
    bordes = np.arange(m.min() - paso / 2, m.max() + paso, paso)
    h, _ = np.histogram(m, bins=bordes)
    return round(bordes[np.argmax(h)] + paso / 2 + correccion, 1)

ANIO_FIN = pd.Timestamp(FECHA_FIN).year + (pd.Timestamp(FECHA_FIN).dayofyear - 1) / 365.25
ventanas = np.arange(1960, int(ANIO_FIN) + 1, 5)
mc = pd.Series({a: mc_maxc(inst.loc[inst.anio.between(a, a + 4), "mag"]) for a in ventanas}, name="Mc")

fig, ax = plt.subplots(figsize=(8, 4.2))
ax.scatter(cat.anio_dec, cat.mag, s=2, alpha=0.25, color="#c2408c", linewidths=0, rasterized=True)
ax.step(list(mc.index) + [ANIO_FIN], list(mc.values) + [mc.values[-1]], where="post", color="k", lw=1.8,
        label="$M_c$ (ventanas de 5 años)")
ax.axhline(MAG_COMPLETA, color="#1b0b2e", lw=0.8, ls="--", label=f"Umbral de comparación (M {dec(MAG_COMPLETA)})")
ax.set(xlim=(1550, 2030), xlabel="Año", ylabel="Magnitud", title="El piso de detección baja con el tiempo")
ax.legend(frameon=False, fontsize=8, loc="lower left")
mc.dropna().to_frame().T
''')

md(r'''
Si el umbral es completo, la tasa anual no debería tener tendencia instrumental. La tercera figura compara la tasa anual de todos los eventos con la de los umbrales altos.
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
## 9. Lectura y límites

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
## 10. Qué sigue

- Sustituir el catálogo USGS por el del **SGC**, con su autorización y licencia, y comparar la magnitud de completitud.
- Separar fuentes (subducción, cortical, nido) y estimar $a$ y $b$ por fuente.
- Pasar de la sismicidad a la amenaza con modelos de movimiento del suelo (ver [](301_sismo.md)).

**Referencias.** Aki, K. (1965). Maximum likelihood estimate of *b* in the formula log N = a − bM and its confidence limits. *Bulletin of the Earthquake Research Institute*, 43, 237-239. Montejo, J., Arcila, M. y Zornosa, D. (2023). Catálogo Sísmico Integrado para Colombia. *Boletín Geológico*, 50(1). https://doi.org/10.32685/0120-1425/bol.geol.50.1.2023.665. NOAA National Centers for Environmental Information, Global Significant Earthquake Database. https://doi.org/10.7289/V5TD9V7K. USGS Earthquake Hazards Program, FDSN Event Web Service. Utsu, T. (1966). A statistical significance test of the difference in b-value between two earthquake groups. *Journal of Physics of the Earth*, 14, 37-40. Wiemer, S. y Wyss, M. (2000). Minimum magnitude of completeness in earthquake catalogs. *Bulletin of the Seismological Society of America*, 90(4), 859–869.
''')
