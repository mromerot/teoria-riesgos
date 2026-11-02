"""Genera las ilustraciones de cabecera de cada capítulo (SVG planos, 960 x 260) en `ilustraciones/`.

Uso: `python estilo/construir_ilustraciones.py`.
Estilo: escena plana con cielo en degradado, suelo en bandas y una casa como unidad de medida del riesgo
(la casa aparece en todas, igual que en las ilustraciones de CLIMAAX).
Cada amenaza usa los colores de su ícono de sidebar.
"""
from pathlib import Path
import math

OUT = Path(__file__).parent / "ilustraciones"
W, H = 960, 260
PAPEL, TINTA = "#F7F3EC", "#23303F"


def svg(nombre, fondo, cuerpo, titulo):
    g = f'''<linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{fondo[0]}"/><stop offset="1" stop-color="{fondo[1]}"/></linearGradient>'''
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{titulo}">
<title>{titulo}</title>
<defs>{g}<clipPath id="m"><rect width="{W}" height="{H}" rx="14"/></clipPath></defs>
<g clip-path="url(#m)">
<rect width="{W}" height="{H}" fill="url(#cielo)"/>
{cuerpo}
</g></svg>'''
    (OUT / f"{nombre}.svg").write_text(s, encoding="utf-8")


# ---------- piezas ----------
def casa(x, y, s=1.0, techo="#B5483A", pared=PAPEL, rot=0, grieta=False, sin_techo=False):
    r = f' rotate({rot})' if rot else ""
    t = "" if sin_techo else f'<polygon points="-8,-44 32,-76 72,-44" fill="{techo}"/>'
    if sin_techo:
        t = f'<polygon points="-8,-44 14,-62 20,-44" fill="{techo}"/>'
    c = '<path d="M40 -44 L34 -30 L42 -24 L35 -8 L40 0" fill="none" stroke="#3b2f2a" stroke-width="2"/>' if grieta else ""
    return (f'<g transform="translate({x} {y}) scale({s}){r}"><rect x="0" y="-44" width="64" height="44" fill="{pared}"/>{t}'
            f'<rect x="26" y="-24" width="12" height="24" fill="{techo}" opacity=".85"/><rect x="8" y="-34" width="12" height="12" fill="#9CC3DB"/>'
            f'<rect x="44" y="-34" width="12" height="12" fill="#9CC3DB"/>{c}</g>')


def sol(cx, cy, r, color="#F5B83D", rayos=12, largo=1.5, op=1):
    ls = "".join(f'<line x1="{cx+math.cos(a)*r*1.25:.1f}" y1="{cy+math.sin(a)*r*1.25:.1f}" x2="{cx+math.cos(a)*r*largo*1.1:.1f}" y2="{cy+math.sin(a)*r*largo*1.1:.1f}" stroke="{color}" stroke-width="{max(3,r*.12):.1f}" stroke-linecap="round"/>'
                  for a in [i * 2 * math.pi / rayos for i in range(rayos)])
    return f'<g opacity="{op}">{ls}<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/></g>'


def nube(x, y, s=1.0, c="#FFFFFF", op=1):
    return (f'<g transform="translate({x} {y}) scale({s})" fill="{c}" opacity="{op}"><ellipse cx="0" cy="0" rx="46" ry="16"/>'
            f'<circle cx="-14" cy="-14" r="18"/><circle cx="12" cy="-20" r="22"/><circle cx="30" cy="-8" r="14"/></g>')


def arbol(x, y, s=1.0, hoja="#3E8E5E", tronco="#7A5A3A", rot=0):
    return (f'<g transform="translate({x} {y}) scale({s}) rotate({rot})"><rect x="-3" y="-22" width="6" height="22" fill="{tronco}"/>'
            f'<circle cx="0" cy="-34" r="18" fill="{hoja}"/><circle cx="-11" cy="-26" r="11" fill="{hoja}" opacity=".9"/></g>')


def palma(x, y, s=1.0, rot=0, hoja="#2F8F6B"):
    h = "".join(f'<path d="M0 -62 q{dx} {-22} {dx*2} {dy}" fill="none" stroke="{hoja}" stroke-width="5" stroke-linecap="round"/>'
                for dx, dy in [(-26, 18), (-14, 26), (14, 26), (26, 18), (0, 30)])
    return (f'<g transform="translate({x} {y}) scale({s}) rotate({rot})"><path d="M0 0 q-6 -30 0 -62" fill="none" stroke="#8B6540" stroke-width="7" stroke-linecap="round"/>{h}</g>')


def ola(x0, x1, y, amp, per, color, op=1, grosor=None, relleno_hasta=None):
    pts = []
    x = x0
    d = f"M{x0} {y}"
    n = int((x1 - x0) / (per / 2))
    for i in range(n):
        d += f" q{per/4:.1f} {-amp if i%2==0 else amp} {per/2:.1f} 0"
    if relleno_hasta:
        return f'<path d="{d} L{x1} {relleno_hasta} L{x0} {relleno_hasta} Z" fill="{color}" opacity="{op}"/>'
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{grosor or 4}" stroke-linecap="round" opacity="{op}"/>'


def lluvia(x0, x1, y0, y1, n, c="#DCEBF7", op=.8):
    import random
    rnd = random.Random(7)
    return "".join(f'<line x1="{(xx:=rnd.uniform(x0,x1)):.0f}" y1="{(yy:=rnd.uniform(y0,y1)):.0f}" x2="{xx-5:.0f}" y2="{yy+13:.0f}" stroke="{c}" stroke-width="2.2" stroke-linecap="round" opacity="{op}"/>' for _ in range(n))


def suelo(y, color, color2=None, h=H):
    s = f'<rect x="0" y="{y}" width="{W}" height="{h-y}" fill="{color}"/>'
    if color2:
        s += f'<rect x="0" y="{y+22}" width="{W}" height="{h-y-22}" fill="{color2}"/>'
    return s


# ---------- escenas ----------
def sismo():
    c = suelo(176, "#C9A57A", "#A9835A")
    c += '<rect x="0" y="168" width="470" height="12" fill="#D9B88C"/>'          # bloque elevado
    c += '<path d="M470 168 L484 190 L474 206 L488 226 L478 260" fill="none" stroke="#5A3F28" stroke-width="5" stroke-linejoin="round"/>'
    c += casa(300, 168, 1.15, rot=-4, grieta=True) + casa(110, 168, .9, "#C0703A")
    c += casa(640, 188, 1.05, "#8A4A3A", rot=4)
    c += "".join(f'<path d="M{480-r*1.6} {236} a{r*1.6} {r} 0 0 1 {r*3.2} 0" fill="none" stroke="#fff" stroke-width="3" opacity="{.9-r/150:.2f}" stroke-dasharray="4 7"/>' for r in (20, 44, 70, 98))
    c += '<polygon points="480,238 486,250 498,250 488,258 492,270 480,263 468,270 472,258 462,250 474,250" fill="#E0482E" transform="translate(0 -26)"/>'
    c += '<polyline points="640,48 690,48 702,22 716,76 730,30 744,66 758,48 910,48" fill="none" stroke="#fff" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>'
    c += '<line x1="640" y1="48" x2="910" y2="48" stroke="#fff" stroke-width="1" opacity=".35"/>'
    svg("sismo", ("#F2D9B4", "#E9B98A"), c, "Casas en el borde de una falla y ondas sísmicas")


def volcanes():
    c = sol(150, 70, 28, "#F7E3A8", op=.9) if False else ""
    c += '<polygon points="380,200 600,70 640,70 840,200" fill="#6B4A3A"/><polygon points="600,70 640,70 660,92 580,92" fill="#3F2B25"/>'
    c += '<path d="M610 76 q-10 40 -30 66 q22 6 30 32 q10 -30 34 -34 q-22 -26 -4 -64 Z" fill="#E8542B"/><path d="M618 80 q-4 30 -12 50 q12 4 18 26 q6 -22 20 -26 q-14 -24 -6 -50 Z" fill="#F7B13A"/>'
    c += "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" opacity=".92"/>' for x, y, r, col in
                 [(618, 50, 22, "#4B4B55"), (600, 26, 28, "#5A5A66"), (640, 14, 32, "#6A6A76"), (690, 18, 26, "#7C7C88"), (740, 28, 22, "#8B8B96"), (570, 6, 20, "#6A6A76")])
    c += suelo(196, "#4C7A4A", "#3E6A40")
    c += arbol(60, 214, 1.1) + arbol(120, 226, .9) + casa(190, 222, 1.0, "#3C6E91") + casa(290, 214, .85, "#C0703A") + arbol(350, 222, .8)
    c += '<path d="M600 142 q-6 30 -24 56 M626 152 q6 30 24 46" fill="none" stroke="#E8542B" stroke-width="5" stroke-linecap="round"/>'
    svg("volcanes", ("#F0C79B", "#D98B6B"), c, "Volcán en erupción sobre un valle con casas")


def tsunami():
    c = suelo(206, "#E8D3A1", "#D8BE86")
    c += ola(0, W, 130, 10, 120, "#2D88C4", relleno_hasta=H) if False else ""
    c += '<path d="M960 260 L960 40 C 900 30 820 40 760 78 C 700 116 680 166 620 190 C 560 212 480 210 400 230 L400 260 Z" fill="#1F6FA8"/>'
    c += '<path d="M960 40 C 900 30 820 40 760 78 C 735 94 718 112 706 130 C 740 100 800 84 850 90 C 880 94 905 104 925 120 Z" fill="#8FD0F0"/>'
    c += '<path d="M706 130 C 690 150 660 160 640 170 C 664 164 690 158 712 140 Z" fill="#fff" opacity=".9"/>'
    c += "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".85"/>' for x, y, r in [(716, 120, 6), (740, 100, 4), (700, 140, 5), (760, 84, 3)])
    c += ola(380, 700, 236, 7, 70, "#9AD3F2", .8, 4)
    c += casa(70, 206, 1.15, "#C0703A") + casa(210, 206, .95, "#3C6E91") + palma(340, 206, 1.1, rot=8)
    c += nube(180, 56, 1.1, "#fff", .9) + nube(420, 36, .8, "#fff", .8)
    svg("tsunami", ("#BFE3F5", "#8FC6E4"), c, "Ola de tsunami acercándose a una costa con casas")


def mov_masa():
    c = '<polygon points="0,90 330,70 640,150 960,214 960,260 0,260" fill="#9C7A4F"/>'
    c += '<polygon points="330,70 640,150 600,176 360,116" fill="#B8935F"/>'
    c += '<polygon points="640,150 960,214 960,260 560,260 600,176" fill="#7A5A38"/>'
    c += '<path d="M360 116 L600 176" stroke="#5E4328" stroke-width="5" stroke-dasharray="2 8" stroke-linecap="round"/>'
    c += "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#5E4328"/>' for x, y, r in [(520, 160, 9), (560, 188, 7), (610, 214, 11), (690, 232, 8), (480, 148, 6)])
    c += arbol(80, 140, 1.1) + arbol(150, 118, 1.0) + arbol(230, 96, .9) + arbol(300, 96, .8, rot=-14) + arbol(420, 128, .8, rot=24) + arbol(470, 160, .8, rot=40)
    c += casa(780, 238, 1.1, "#B5483A", rot=-6)
    c += nube(120, 36, 1.0, "#E7ECF1") + lluvia(40, 260, 50, 100, 14, "#D6E4F0", .9)
    svg("mov_masa", ("#CFD8E0", "#B7C3CE"), c, "Ladera que se desliza hacia una casa")


def avenidas():
    c = '<polygon points="0,60 230,120 360,260 0,260" fill="#4C7A4A"/><polygon points="960,50 730,118 600,260 960,260" fill="#3E6A40"/>'
    c += '<path d="M340 90 C 410 130 380 170 440 200 C 480 220 440 240 430 260 L 620 260 C 600 230 560 210 540 180 C 520 150 560 120 600 90 Z" fill="#9B6C40"/>'
    c += '<path d="M380 100 C 440 130 420 170 470 196 C 500 214 480 238 480 260 L 580 260 C 570 230 540 210 520 180 C 510 150 540 124 570 100 Z" fill="#B88550"/>'
    c += "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#5E4328"/>' for x, y, r in [(470, 160, 9), (500, 200, 12), (520, 236, 14), (450, 220, 8), (560, 218, 9)])
    c += '<rect x="420" y="190" width="46" height="8" rx="4" fill="#3A2A1A" transform="rotate(-18 440 194)"/><rect x="520" y="226" width="40" height="7" rx="3.5" fill="#3A2A1A" transform="rotate(14 540 230)"/>'
    c += arbol(70, 150, 1.1, "#357A55") + arbol(150, 176, .9, "#357A55") + arbol(840, 140, 1.1) + arbol(900, 170, .9)
    c += casa(690, 250, 1.05, "#C0703A") + casa(800, 256, .85, "#3C6E91")
    c += nube(250, 40, 1.3, "#6F7C8C") + nube(420, 30, 1.0, "#5C6877") + lluvia(190, 480, 60, 120, 22, "#CFE0EE")
    c += '<polygon points="350,64 336,96 350,96 340,124 368,86 354,86 362,64" fill="#FFD84A"/>'
    svg("avenidas_torrenciales", ("#8EA3B5", "#6E8397"), c, "Avenida torrencial bajando por una quebrada hacia las casas")


def inundacion():
    c = nube(150, 44, 1.4, "#7D8FA2") + nube(420, 30, 1.2, "#6C7E91") + nube(720, 48, 1.4, "#7D8FA2") + lluvia(60, 820, 60, 150, 70, "#E5F1FA")
    c += casa(120, 190, 1.2) + casa(330, 190, 1.0, "#3C6E91") + arbol(520, 190, 1.0, "#357A55") + casa(640, 190, 1.15, "#C0703A") + arbol(820, 190, .9, "#357A55")
    c += ola(0, W, 176, 5, 80, "#2F7FB8", .95, relleno_hasta=H)
    c += ola(0, W, 176, 5, 80, "#9AD3F2", 1, 3)
    c += ola(0, W, 210, 6, 90, "#1F6FA8", .8, relleno_hasta=H) + ola(0, W, 210, 6, 90, "#BFE3F5", .9, 3)
    c += '<g stroke="#fff" stroke-width="2.5" opacity=".7"><line x1="78" y1="176" x2="78" y2="260"/></g>'
    svg("inundacion", ("#9FB2C4", "#7F95AA"), c, "Casas parcialmente inundadas bajo la lluvia")


def erosion_costera():
    c = sol(820, 62, 30, "#F7D060", 10)
    c += '<path d="M470 260 L470 176 C 470 164 450 160 430 160 L 0 160 L 0 260 Z" fill="#D8B882"/><path d="M0 160 L 430 160 C 450 160 470 164 470 176 L470 190 L0 190 Z" fill="#E8D3A1"/>'
    c += '<path d="M470 176 C 470 190 440 196 430 210 C 420 228 450 240 440 260" fill="none" stroke="#B88F5A" stroke-width="3"/>'
    c += '<line x1="520" y1="150" x2="520" y2="250" stroke="#B5483A" stroke-width="2.5" stroke-dasharray="6 7"/>'
    c += '<path d="M470 150 L 506 150 M 500 144 L 508 150 L 500 156" fill="none" stroke="#B5483A" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    c += '<path d="M470 260 L470 200 L960 200 L960 260 Z" fill="#2D88C4"/>' if False else ""
    c += ola(440, W, 200, 6, 100, "#2D88C4", relleno_hasta=H) + ola(440, W, 200, 6, 100, "#CDEBFA", 1, 3)
    c += ola(440, W, 232, 6, 110, "#1F6FA8", .85, relleno_hasta=H)
    c += palma(380, 160, 1.15, rot=14) + casa(120, 160, 1.15, "#C0703A") + palma(230, 160, 1.0, rot=-4) + palma(330, 160, .85, rot=10)
    c += nube(640, 50, 1.1, "#fff", .9)
    svg("erosion_costera", ("#CDEBFA", "#9FD4EE"), c, "Costa que retrocede: palmeras y una casa junto a un acantilado de arena")


def erosion_fluvial():
    c = suelo(150, "#6EA05A", "#5A8C4A")
    c += '<path d="M0 190 L 380 190 C 400 190 410 200 414 214 L 430 260 L0 260 Z" fill="#9C7A4F"/><path d="M586 190 L 960 190 L960 260 L 570 260 Z" fill="#9C7A4F"/>'
    c += '<path d="M410 196 C 430 200 560 200 590 196 L 600 260 L 420 260 Z" fill="#2D88C4"/>' if False else ""
    c += '<path d="M380 190 C 404 192 414 206 418 222 L 436 260 L 578 260 L 590 200 C 586 194 584 192 580 190 Z" fill="#2D88C4"/>'
    c += ola(398, 586, 206, 3, 40, "#CDEBFA", .9, 2.5) + ola(410, 580, 232, 3, 44, "#CDEBFA", .7, 2.5)
    c += '<path d="M380 150 L 380 190" stroke="#B5483A" stroke-width="2.5" stroke-dasharray="5 6"/>'
    c += '<path d="M286 150 L 380 150 L 388 166 L 372 176 L 380 190" fill="#6EA05A"/>' if False else ""
    c += '<polygon points="340,190 372,190 360,206 344,200" fill="#7A5A38" transform="translate(30 20) rotate(24 360 200)"/>'
    c += casa(250, 156, 1.1, "#B5483A") + arbol(130, 156, 1.0) + arbol(60, 156, .8) + arbol(700, 190, 1.0) + arbol(800, 190, .8) + casa(860, 190, .9, "#3C6E91")
    c += '<path d="M370 142 L 424 142 M 416 136 L 426 142 L 416 148" fill="none" stroke="#B5483A" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" transform="translate(0 -4)"/>'
    c += nube(640, 50, 1.2, "#fff", .9)
    svg("erosion_fluvial", ("#CFE6EE", "#A6CFDD"), c, "Orilla de un río que se desmorona junto a una casa")


def sequia():
    c = sol(760, 78, 52, "#FFE08A", 14, 1.4)
    c += suelo(170, "#C99A5B", "#B8844A")
    # grietas
    c += '<g fill="none" stroke="#6E4A28" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">' + "".join(f'<path d="{d}"/>' for d in [
        "M40 200 L120 214 L180 206 L260 230 L330 222", "M120 214 L106 248", "M260 230 L290 258", "M520 200 L600 224 L690 212 L780 238",
        "M600 224 L588 256", "M690 212 L720 188", "M840 206 L920 226 L960 220", "M420 236 L500 228"]) + "</g>"
    c += '<path d="M450 176 q-4 -40 -2 -78 M448 130 q-24 -14 -30 -34 M449 112 q22 -10 34 -32" fill="none" stroke="#5E4328" stroke-width="7" stroke-linecap="round"/>'
    c += casa(110, 176, 1.2, "#B5483A") + casa(260, 176, .9, "#8A5A3A")
    c += '<ellipse cx="620" cy="186" rx="26" ry="8" fill="#B8844A"/>'
    svg("sequia", ("#FBD99A", "#F2B76A"), c, "Sol, suelo agrietado y árbol seco junto a las casas")


def calor():
    c = sol(480, 60, 74, "#FFC83D", 16, 1.45)
    c += suelo(188, "#D9B77C", "#C79C5E")
    c += casa(380, 196, 1.9, "#B5483A")
    c += "".join(ola(x - 40, x + 40, y, 5, 28, "#FFF3C8", .7, 3.2) for x, y in [(210, 130), (250, 100), (730, 122), (770, 92), (180, 160), (800, 156)])
    c += '<g transform="translate(860 40)"><rect x="-9" y="0" width="18" height="110" rx="9" fill="#fff"/><rect x="-5" y="40" width="10" height="70" rx="5" fill="#E0482E"/><circle cx="0" cy="124" r="16" fill="#E0482E" stroke="#fff" stroke-width="4"/>' + "".join(f'<line x1="-9" y1="{y}" x2="-16" y2="{y}" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for y in (14, 34, 54, 74)) + "</g>"
    svg("calor", ("#FFD27A", "#F7A24E"), c, "Sol intenso sobre una casa, con ondas de calor y un termómetro")


def incendios():
    c = sol(110, 70, 36, "#FFB347", 0) + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" opacity=".85"/>' for x, y, r, col in
                                                 [(520, 40, 26, "#6E6A68"), (560, 20, 32, "#7C7876"), (610, 38, 28, "#8E8A88"), (660, 14, 22, "#A09C9A"), (470, 62, 20, "#5C5856")])
    c += '<polygon points="0,170 140,120 280,160 430,100 600,150 760,110 960,150 960,260 0,260" fill="#3C5E3E"/>'
    c += suelo(200, "#4C3A2C", "#3A2C22")
    c += "".join(arbol(x, 210, s, "#355A3A") for x, s in [(60, 1.1), (130, .9), (200, 1.0), (260, .8)])
    def llama(x, y, s):
        return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0 C -26 -16 -20 -44 -6 -62 C -8 -42 4 -40 6 -54 C 22 -40 30 -16 0 0 Z" fill="#E8542B"/>'
                f'<path d="M0 0 C -12 -8 -10 -24 -2 -34 C 0 -24 6 -22 8 -30 C 14 -20 14 -8 0 0 Z" fill="#FFC83D"/></g>')
    c += "".join(llama(x, y, s) for x, y, s in [(330, 214, 1.5), (400, 222, 1.9), (470, 214, 1.4), (540, 224, 1.7), (610, 216, 1.3), (350, 236, 1.0), (500, 238, 1.1)])
    c += "".join(arbol(x, 214, s, "#2C2A28", "#1E1C1A") for x, s in [(380, 1.0), (440, .9), (580, 1.0)])
    c += casa(780, 224, 1.15, "#C0703A") + arbol(900, 214, 1.0, "#355A3A")
    svg("incendios", ("#F2A56B", "#D9714A"), c, "Incendio forestal con humo avanzando hacia una casa")


def ciclones():
    c = ola(0, W, 218, 7, 100, "#1F6FA8", relleno_hasta=H) + ola(0, W, 218, 7, 100, "#BFE3F5", 1, 3)
    c += ola(0, W, 244, 7, 110, "#165A8C", .9, relleno_hasta=H)
    # espiral: tres brazos logarítmicos aplastados en perspectiva
    cx, cy = 560, 104
    for k in range(3):
        pts = []
        for n in range(0, 61):
            th = n * 0.13 + k * 2.094
            r = 14 * math.exp(0.2 * (n * 0.13))
            pts.append(f"{cx + math.cos(th) * r * 1.7:.1f},{cy + math.sin(th) * r * .62:.1f}")
        c += f'<polyline points="{" ".join(pts)}" fill="none" stroke="#fff" stroke-width="13" stroke-linecap="round" stroke-linejoin="round" opacity=".62"/>'
    c += f'<ellipse cx="{cx}" cy="{cy}" rx="22" ry="9" fill="#44627F"/><ellipse cx="{cx}" cy="{cy}" rx="9" ry="3.6" fill="#8FA6BD"/>'
    c += palma(150, 218, 1.35, rot=26) + palma(230, 218, 1.1, rot=22, hoja="#2A7F5B") + casa(330, 218, 1.0, "#3C6E91", rot=0)
    c += '<g stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".85"><path d="M40 70 h110 M70 92 h90 M20 112 h110"/></g>'
    svg("ciclones", ("#8FA6BD", "#5F7C99"), c, "Ciclón tropical sobre el mar con palmeras dobladas por el viento")


def vendavales():
    c = suelo(196, "#6EA05A", "#5A8C4A")
    c += "".join(f'<path d="M{x0} {y} h{l} q18 0 18 -14 q0 -12 -12 -12 q-8 0 -8 8" fill="none" stroke="#fff" stroke-width="4.5" stroke-linecap="round" opacity=".9"/>' for x0, y, l in [(20, 70, 260), (60, 110, 330), (30, 150, 220), (360, 56, 200)])
    c += arbol(520, 206, 1.25, "#3E8E5E", rot=18) + arbol(620, 206, 1.1, "#3E8E5E", rot=24) + arbol(720, 206, 1.2, "#3E8E5E", rot=14)
    c += casa(820, 206, 1.1, "#B5483A", sin_techo=True)
    c += '<g fill="#B5483A">' + "".join(f'<polygon points="0,0 22,-8 26,6 4,12" transform="translate({x} {y}) rotate({r})"/>' for x, y, r in [(790, 90, 20), (720, 50, -30), (860, 60, 40)]) + "</g>"
    c += '<g fill="#6EA05A">' + "".join(f'<ellipse cx="{x}" cy="{y}" rx="10" ry="4.5" transform="rotate({r} {x} {y})"/>' for x, y, r in [(480, 100, 30), (560, 64, -20), (640, 118, 50), (900, 130, 10)]) + "</g>"
    c += nube(330, 40, 1.5, "#7D8A99") + nube(640, 28, 1.2, "#6C7988")
    svg("vendavales", ("#B8C4D1", "#97A7B8"), c, "Viento fuerte que arranca el techo de una casa y dobla los árboles")


def natech():
    c = nube(170, 46, 1.3, "#6C7988") + nube(480, 34, 1.0, "#5C6877") + lluvia(90, 560, 56, 130, 30, "#CFE0EE", .8)
    c += '<polygon points="560,40 544,84 560,84 548,122 580,72 562,72 572,40" fill="#FFD84A"/>'
    c += suelo(200, "#6B7A66", "#59685A")
    def tanque(x, y, w, h, col):
        return (f'<g><rect x="{x}" y="{y-h}" width="{w}" height="{h}" rx="6" fill="{col}"/><ellipse cx="{x+w/2}" cy="{y-h}" rx="{w/2}" ry="7" fill="#fff" opacity=".55"/>'
                f'<rect x="{x+6}" y="{y-h+10}" width="5" height="{h-18}" rx="2.5" fill="#fff" opacity=".35"/></g>')
    c += tanque(80, 200, 78, 78, "#B9C3CE") + tanque(176, 200, 64, 100, "#CFD6DE") + tanque(256, 200, 90, 62, "#A9B5C2")
    c += '<g fill="none" stroke="#3b4756" stroke-width="5"><path d="M118 122 V104 H208 V100"/><path d="M300 138 V110 H400 V200"/></g>'
    c += '<path d="M208 100 V86" stroke="#3b4756" stroke-width="5" fill="none"/>'
    def llama(x, y, s):
        return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0 C -26 -16 -20 -44 -6 -62 C -8 -42 4 -40 6 -54 C 22 -40 30 -16 0 0 Z" fill="#E8542B"/>'
                f'<path d="M0 0 C -12 -8 -10 -24 -2 -34 C 0 -24 6 -22 8 -30 C 14 -20 14 -8 0 0 Z" fill="#FFC83D"/></g>')
    c += llama(208, 92, 1.1) + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#4B4B55" opacity=".8"/>' for x, y, r in [(214, 20, 14), (234, 6, 18), (262, 12, 14)])
    c += ola(440, W, 190, 6, 90, "#2F7FB8", .95, relleno_hasta=H) + ola(440, W, 190, 6, 90, "#9AD3F2", 1, 3)
    c += ola(440, W, 224, 6, 100, "#1F6FA8", .85, relleno_hasta=H)
    c += casa(640, 192, 1.1, "#C0703A") + casa(790, 196, .9, "#3C6E91")
    c += '<g fill="#6B5B3A" opacity=".8"><ellipse cx="480" cy="212" rx="22" ry="5"/><ellipse cx="560" cy="236" rx="28" ry="5"/><ellipse cx="700" cy="226" rx="20" ry="4"/></g>'
    svg("natech", ("#9EA9B6", "#7C8A9A"), c, "Tanques industriales junto a un río crecido, con un rayo y una llama")


# ---------- partes ----------
def p_conceptos():
    c = suelo(214, "#E3DDCF")
    cx = [(360, "#E8542B", "Amenaza"), (480, "#2D88C4", "Exposición"), (600, "#7A5BC4", "Vulnerabilidad")]
    c += "".join(f'<circle cx="{x}" cy="116" r="78" fill="{col}" opacity=".55"/>' for x, col, _ in cx)
    c += '<circle cx="480" cy="116" r="22" fill="#23303F"/>'
    c += '<text x="480" y="122" text-anchor="middle" font-family="Georgia,serif" font-size="15" font-weight="700" fill="#fff">riesgo</text>'
    c += "".join(f'<text x="{x + (-34 if i==0 else (34 if i==2 else 0))}" y="{ 112 if i!=1 else 62}" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" font-weight="600" fill="#23303F">{t}</text>' for i, (x, col, t) in enumerate(cx))
    c += casa(120, 214, 1.2) + casa(780, 214, 1.0, "#3C6E91") + arbol(240, 214, 1.0) + arbol(860, 214, .9)
    svg("conceptos", ("#F3EEE3", "#E9E1D0"), c, "Riesgo como intersección de amenaza, exposición y vulnerabilidad")


def p_metodologia():
    c = ""
    xs = [60, 260, 460]
    for i, (x, t) in enumerate(zip(xs, ["Alcance", "Amenaza", "Riesgo"])):
        c += f'<rect x="{x}" y="70" width="150" height="64" rx="12" fill="#fff"/><text x="{x+75}" y="108" text-anchor="middle" font-family="system-ui,sans-serif" font-size="17" font-weight="600" fill="#23303F">{t}</text>'
        if i < 2:
            c += f'<path d="M{x+156} 102 h38 m-8 -7 l8 7 l-8 7" fill="none" stroke="#2B4C7E" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
    c += '<g transform="translate(680 40)"><rect x="0" y="0" width="240" height="170" rx="12" fill="#fff"/>'
    c += '<path d="M24 30 V140 H220" fill="none" stroke="#23303F" stroke-width="2"/>'
    c += '<path d="M24 36 C 70 40 90 70 120 96 C 150 120 180 132 220 136" fill="none" stroke="#2B4C7E" stroke-width="4"/>'
    c += '<path d="M24 36 C 70 40 90 70 120 96 C 150 120 180 132 220 136 L220 140 L24 140 Z" fill="#5DADE2" opacity=".35"/>'
    c += '<text x="120" y="160" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#23303F">probabilidad de excedencia</text>'
    c += '<text x="14" y="80" font-family="system-ui,sans-serif" font-size="12" fill="#23303F" transform="rotate(-90 14 80)" text-anchor="middle">pérdida</text></g>'
    c += casa(120, 214, 1.0) + casa(300, 214, .8, "#3C6E91") + casa(460, 214, .9, "#C0703A")
    c += suelo(214, "#C9D6E6")
    svg("metodologia", ("#DCE6F3", "#C2D3E8"), c, "Flujo de evaluación y curva de pérdida anual esperada")


def p_vulnerabilidad():
    c = suelo(206, "#DDE3CC", "#CBD3B2")
    def persona(x, y, s=1.0, col="#7A5BC4"):
        return f'<g transform="translate({x} {y}) scale({s})"><circle cx="0" cy="-34" r="7" fill="#E7C09A"/><path d="M-9 0 L-6 -26 H6 L9 0 Z" fill="{col}"/></g>'
    c += casa(70, 206, 1.25, "#B5483A") + casa(210, 206, 1.0, "#3C6E91", grieta=True) + casa(330, 206, .8, "#8A8F55", rot=-3, grieta=True)
    c += persona(430, 206, 1.4) + persona(462, 206, 1.1, "#2D88C4") + persona(490, 206, 0.8, "#E8542B")
    c += '<g transform="translate(580 36)"><rect width="320" height="150" rx="12" fill="#fff"/><path d="M26 124 H294 M26 124 V20" stroke="#23303F" stroke-width="2" fill="none"/>'
    c += '<path d="M26 120 C 120 118 150 70 190 54 C 230 40 260 38 294 36" fill="none" stroke="#7A5BC4" stroke-width="4"/>'
    c += '<path d="M26 120 C 150 116 200 100 230 80 C 260 60 280 54 294 52" fill="none" stroke="#2D88C4" stroke-width="4" stroke-dasharray="7 6"/>'
    c += '<text x="160" y="142" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#23303F">intensidad de la amenaza</text><text x="12" y="76" font-family="system-ui,sans-serif" font-size="12" fill="#23303F" transform="rotate(-90 12 76)" text-anchor="middle">daño</text></g>'
    svg("vulnerabilidad", ("#EAF0DA", "#D6E0BD"), c, "Casas, personas y curvas de daño según la intensidad")


def p_sintesis():
    c = ""
    for i, (y, col) in enumerate([(150, "#2D88C4"), (112, "#E8542B"), (74, "#3E8E5E")]):
        c += f'<polygon points="260,{y} 480,{y-48} 700,{y} 480,{y+48}" fill="{col}" opacity=".78" stroke="#fff" stroke-width="2"/>'
    c += casa(440, 120, .6, "#B5483A") + casa(520, 100, .5, "#3C6E91")
    c += '<g stroke="#23303F" stroke-width="2" stroke-dasharray="4 5" opacity=".5"><line x1="480" y1="26" x2="480" y2="226"/></g>'
    c += '<g font-family="system-ui,sans-serif" font-size="14" font-weight="600" fill="#23303F"><text x="730" y="80">Amenazas</text><text x="730" y="118">Exposición</text><text x="730" y="156">Vulnerabilidad</text></g>'
    svg("sintesis", ("#E1E4F2", "#C9CEE6"), c, "Capas de amenaza, exposición y vulnerabilidad sobre una ciudad")


def p_pmgrd():
    c = suelo(214, "#CFE3D4")
    c += '<g transform="translate(560 24) rotate(4)"><rect width="190" height="190" rx="12" fill="#fff"/><rect x="62" y="-10" width="66" height="24" rx="8" fill="#3FA66B"/>'
    c += "".join(f'<path d="M26 {y} l8 8 l14 -16" fill="none" stroke="#16603A" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><rect x="64" y="{y-6}" width="{w}" height="9" rx="4.5" fill="#B7D8C3"/>' for y, w in [(54, 100), (92, 80), (130, 100)]) + "</g>"
    c += casa(70, 214, 1.4) + casa(200, 214, 1.1, "#3C6E91") + casa(320, 214, 1.0, "#C0703A") + casa(430, 214, .8, "#8A4A3A")
    c += arbol(500, 214, 1.0) + arbol(820, 214, 1.1) + casa(860, 214, .9, "#3C6E91")
    svg("pmgrd", ("#DDF0E3", "#BFE0CB"), c, "Plan municipal de gestión del riesgo: lista de acciones para un municipio")


for f in [sismo, volcanes, tsunami, mov_masa, avenidas, inundacion, erosion_costera, erosion_fluvial, sequia, calor, incendios, ciclones, vendavales, natech,
          p_conceptos, p_metodologia, p_vulnerabilidad, p_sintesis, p_pmgrd]:
    f()
print("escritas", len(list(OUT.glob("*.svg"))), "ilustraciones en", OUT)
