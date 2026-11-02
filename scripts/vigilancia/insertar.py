import sys,re
def insertar(arch, texto):
    p=f"book/03_amenazas/{arch}"; t=open(p).read()
    t=re.sub(r"\n## Síntesis de evidencia\n.*?(?=\n## )","",t,flags=re.S)
    i=t.index("\n## Pendiente") if "\n## Pendiente" in t else t.index("\n## Bibliografía recomendada")
    open(p,"w").write(t[:i]+"\n## Síntesis de evidencia\n\n"+texto.strip("\n")+"\n"+t[i:])
