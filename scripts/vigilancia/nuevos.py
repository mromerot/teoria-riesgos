import csv,sys,glob,re,subprocess,os
D="/Users/mauricio/Documents/Data-science-local/ciudades/NUEVO-CONOCIMIENTO-GRD-2020-2026/"
rows=list(csv.DictReader(open("fuentes/vig/disp.csv"))); bib=open("references.bib").read().lower()
cats=sys.argv[2:]; n=int(sys.argv[1])
files=glob.glob(D+"*.pdf")
for r in rows:
    if r["AMENAZA_ESPECIFICA"].strip() not in cats: continue
    if not r.get("PDF disponible","").lower().startswith("s"): continue
    d=r["DOI"].strip().lower()
    if d and d in bib: continue
    f=[x for x in files if d and d.replace("/","_") in x.lower()]
    if not f:
        t=set(w for w in re.findall(r"[a-z]{5,}",r["TITULO/TITLE"].lower()))
        f=[x for x in files if len(t)>3 and len(t&set(re.findall(r"[a-z]{5,}",os.path.basename(x).lower())))>=0.7*len(t)]
    if not f: print("## ID",r["ID"],"SIN ARCHIVO",r["TITULO/TITLE"][:80]); continue
    txt=subprocess.run(["pdftotext","-l","3","-raw",f[0],"-"],capture_output=True,text=True).stdout
    m=re.search(r"(?i)(abstract|resumen|summary)",txt); txt=txt[m.start():] if m else txt
    print(f"## ID{r['ID']} [{r['AÑO']}] {r['TITULO/TITLE'][:100]} | {d}\n{re.sub(chr(10),' ',txt)[:n]}\n")
