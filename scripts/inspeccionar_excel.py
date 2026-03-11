import pandas as pd
from pathlib import Path

CARPETA = Path("data_excel")

for archivo in CARPETA.glob("*.xlsx"):
    print("\n==============================")
    print("Archivo:", archivo.name)

    df = pd.read_excel(archivo)

    print("\nColumnas:")
    print(list(df.columns))

    print("\nCantidad de filas:", len(df))

    print("\nPrimeras 5 filas:")
    print(df.head())