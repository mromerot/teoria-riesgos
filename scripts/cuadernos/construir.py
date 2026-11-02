"""Construye y ejecuta los cuadernos de book/03_amenazas a partir de nb3XX.py.
Uso:  python scripts/cuadernos/construir.py 313 314 315
"""
import importlib.util, sys
from pathlib import Path
import nbformat
from nbclient import NotebookClient

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / "book" / "03_amenazas"
NOMBRES = {"313": "313_analisis_multiamenaza", "314": "314_riesgos_cascada", "315": "315_trayectorias_ciclones", "317": "317_sismicidad_colombia", "318": "318_tsunami_tumaco_1979"}

def construir(num):
    spec = importlib.util.spec_from_file_location(f"nb{num}", Path(__file__).parent / f"nb{num}.py")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    nb = nbformat.v4.new_notebook()
    nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    nb.metadata["language_info"] = {"name": "python"}
    for tipo, texto in mod.CELLS:
        nb.cells.append(nbformat.v4.new_markdown_cell(texto) if tipo == "md" else nbformat.v4.new_code_cell(texto))
    NotebookClient(nb, timeout=300, kernel_name="python3", resources={"metadata": {"path": str(SALIDA)}}).execute()
    nbformat.validate(nb)
    destino = SALIDA / f"{NOMBRES[num]}.ipynb"
    nbformat.write(nb, destino)
    print("escrito", destino, f"({destino.stat().st_size/1024:.0f} KB)")

if __name__ == "__main__":
    for n in sys.argv[1:]:
        construir(n)
