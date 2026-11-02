"""Genera la subsección 'Bibliografía recomendada' (APA 7) de cada capítulo de amenaza desde la hoja Vigilancia_CTeI + Crossref."""
import csv, json, os, re, html, unicodedata
B = os.path.join(os.path.dirname(__file__), "..", "..")
rows = list(csv.DictReader(open(f"{B}/fuentes/vig/nuevo.csv")))
cr = json.load(open(f"{B}/fuentes/vig/crossref.json"))
MAPA = {
 "301_sismo.md": ["Terremoto (sismo)", "Licuefacción"],
 "302_volcanes.md": ["Lahares", "Flujos de lava y domos", "Corriente de densidad piroclástica", "Gases y aerosoles volcánicos"],
 "303_tsunami.md": ["Tsunami"],
 "304_mov_masa.md": ["Movimiento en masa gravitacional (“deslizamiento”)", "Flujos de detritos y tierra (lodo) y avalanchas de roca", "Subsidencia y levantamiento"],
 "305_inundacion.md": ["Inundación", "Inundación repentina", "Inundación por aguas superficiales", "Inundación de drenajes y alcantarillado"],
 "306_erosion_costera.md": ["Erosión y acreción costera", "Inundación costera", "Aumento del nivel del mar", "Pérdida de manglares", "Intrusión de agua salada"],
 "307_erosion_fluvial.md": ["Erosión y acreción fluvial", "Erosión del suelo"],
 "308_sequia.md": ["Sequía"],
 "309_calor.md": ["Ola de calor"],
 "310_incendios.md": ["Incendios forestales"],
 "311_ciclones.md": ["Ciclón tropical"],
 "312_vendavales.md": ["Viento", "Tormenta eléctrica"],
 "319_natech.md": ["Natech (accidente tecnológico inducido por desastre natural)"],
 "316_avenidas_torrenciales.md": ["Flujos de detritos y tierra (lodo) y avalanchas de roca", "Inundación repentina"],
}
def limpia(s):
    s = html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()
    return re.sub(r"\s+", " ", s).replace("*", "∗")
def ini(g):
    g = limpia(g)
    return " ".join(p[0] + "." if "-" not in p else "-".join(q[0] + "." for q in p.split("-") if q) for p in g.replace(".", ". ").split() if p)
def autores(m):
    a = [x for x in m.get("author", []) if x.get("family")]
    if not a:
        o = [x.get("name") for x in m.get("author", []) if x.get("name")]
        return limpia(", ".join(o)) if o else ""
    f = [f"{limpia(x['family'])}, {ini(x.get('given',''))}".rstrip(", ") for x in a]
    if len(f) == 1: return f[0]
    if len(f) <= 20: return ", ".join(f[:-1]) + ", & " + f[-1]
    return ", ".join(f[:19]) + ", ... " + f[-1]
def titulo_fin(t): return t if t[-1:] in ".?!" else t + "."
def enlace(d, m):
    if not d: return None
    if d.startswith("http"): return d if "doi.org" not in d else None
    return f"https://doi.org/{d}" if m else f"`doi:{d}` (no resuelve en Crossref; corregir en la hoja)"
def apa(r):
    d = r["DOI"].strip().lower().replace("https://doi.org/", "").replace("%e2%80%a6", "…")
    m = cr.get(d) if d else None
    anio = r["AÑO"].split(".")[0] or "s. f."
    if m:
        t = limpia((m.get("title") or [r["TITULO/TITLE"]])[0])
        rev = limpia((m.get("container-title") or [r["FUENTE"]])[0])
        au = autores(m)
        y = None
        for k in ("issued", "published-print", "published-online"):
            dp = (m.get(k) or {}).get("date-parts", [[None]])[0][0]
            if dp: y = str(dp); break
        anio = y or anio
        vol, iss, pg = m.get("volume"), m.get("issue"), m.get("page") or m.get("article-number")
        s = (au + " " if au else "") + f"({anio}). "
        if not au: s = titulo_fin(t) + f" ({anio}). "; t_part = ""
        else: t_part = titulo_fin(t) + " "
        s += t_part
        if rev:
            s += f"*{rev}*"
            if vol: s += f", *{limpia(vol)}*"
            if iss: s += f"({limpia(iss)})"
            if pg: s += f", {limpia(pg)}"
            s += ". "
        dd = m.get("DOI") or d
        s += (enlace(dd, m) or "")
        return (au or t).lower(), anio, s.strip()
    t = limpia(r["TITULO/TITLE"]); rev = limpia(r["FUENTE"])
    s = f"{titulo_fin(t)} ({anio}). " + (f"*{rev}*. " if rev else "")
    s += enlace(d, None) or "(Sin DOI; completar autores)."
    return t.lower(), anio, s.strip()
def norm(s): return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
for arch, cats in MAPA.items():
    sel = {}
    for r in rows:
        if r["AMENAZA_ESPECIFICA"].strip() in cats:
            k, y, s = apa(r); sel[s] = (norm(k), y)
    items = sorted(sel.items(), key=lambda kv: kv[1])
    p = f"{B}/book/03_amenazas/{arch}"
    t = open(p).read()
    t = re.split(r"\n## Bibliografía recomendada\n", t)[0].rstrip("\n")
    t += "\n\n## Bibliografía recomendada\n\n"
    t += (f"Lista de los {len(items)} registros de la hoja de vigilancia científica (pestaña `Vigilancia_CTeI`, columna `AMENAZA_ESPECIFICA` = " + "; ".join(f"«{c}»" for c in cats) +
          "), en formato APA 7 con metadatos de Crossref. Son lecturas recomendadas: **no están verificadas contra el texto completo** ni se usan como evidencia hasta que se citen en el capítulo. Las entradas sin DOI carecen de autores en la hoja.\n\n")
    t += "\n\n".join(f"- {s}" for s, _ in items) + "\n"
    open(p, "w").write(t)
    print(arch, len(items))
