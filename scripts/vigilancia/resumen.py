import sys,json,subprocess,re,csv
D="/Users/mauricio/Documents/Data-science-local/ciudades/NUEVO-CONOCIMIENTO-GRD-2020-2026/"
S="/private/tmp/claude-501/-Users-mauricio/eea59470-bcaa-4751-b017-ddabaaa4cd33/scratchpad/vig/por_amenaza.json"
por=json.load(open(S)); rows={r["ID"]:r for r in csv.DictReader(open("fuentes/vig/nuevo.csv"))}
n=int(sys.argv[1]) if sys.argv[1].isdigit() else 1100
for cat in sys.argv[2:]:
    for i,f in por.get(cat,[]):
        r=rows[i]
        t=subprocess.run(["pdftotext","-l","3","-raw",D+f,"-"],capture_output=True,text=True).stdout
        m=re.search(r"(?i)(abstract|resumen|summary)",t); t=t[m.start():] if m else t
        print(f"## ID{i} [{r['AÑO'][:4]}] {r['TITULO/TITLE'][:110]} | DOI {r['DOI']}\n{re.sub(chr(10),' ',t)[:n]}\n")
