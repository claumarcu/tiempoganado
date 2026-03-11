import pandas as pd
from pathlib import Path
import sqlite3

from src.database.db_manager import (
    Contact,
    get_contact_by_phone,
    add_contact,
    add_enrollment,
    add_course,
    list_courses,
)

DATA_FOLDER = Path("data_excel")


def normalizar_fecha(valor):

    import pandas as pd

    if pd.isna(valor):
        return None

    texto = str(valor)

    # Caso 1: fecha completa tipo 2022-09-22 00:00:00
    if "-" in texto and ":" in texto:
        return texto.split(" ")[0]

    # Caso 2: fecha tipo 2022-09-22
    if "-" in texto and len(texto) >= 10:
        return texto[:10]

    # Caso 3: formato tipo Jun 22
    texto = texto.lower()

    meses = {
        "jan":1,"january":1,
        "feb":2,"february":2,
        "mar":3,"march":3,
        "apr":4,"april":4,
        "may":5,
        "jun":6,"june":6,
        "jul":7,"july":7,
        "aug":8,"august":8,
        "sep":9,"september":9,
        "oct":10,"october":10,
        "nov":11,"november":11,
        "dec":12,"december":12,
    }

    mes = None

    for k,v in meses.items():
        if k in texto:
            mes = v
            break

    if mes is None:
        return None

    numeros = "".join([c for c in texto if c.isdigit()])

    if len(numeros) != 2:
        return None

    year = int(numeros)

    if year < 50:
        year += 2000
    else:
        year += 1900

    return f"{year}-{mes:02d}-01"


def obtener_curso(nombre):

    cursos = list_courses()

    for c in cursos:
        if c[1] == nombre:
            return c[0]

    return add_course(
        nombre=nombre,
        categoria="fotografia",
        modalidad="presencial",
        area="produccion",
    )


def obtener_contacto(nombre, telefono):

    conn = sqlite3.connect("data/alumnos.db")
    cur = conn.cursor()

    if telefono:

        cur.execute(
            "SELECT id FROM contactos WHERE telefono = ?",
            (telefono,),
        )

        r = cur.fetchone()

        if r:
            conn.close()
            return r[0]

    telefono_final = telefono if telefono else f"prod_{nombre}"

    contact = Contact(
        nombre=nombre,
        telefono=telefono_final,
        email=None,
        etiquetas="alumno",
        estado=None,
        origen="excel_producciones",
    )

    try:
        contact_id = add_contact(contact)

    except:

        cur.execute(
            "SELECT id FROM contactos WHERE telefono = ?",
            (telefono_final,),
        )

        r = cur.fetchone()
        conn.close()

        if r:
            return r[0]

        return None

    conn.close()

    return contact_id


def importar_excel(path_excel):

    print("Importando:", path_excel.name)

    df = pd.read_excel(path_excel, dtype=str)

    locaciones = df.columns[3:]

    for _, row in df.iterrows():

        nombre = row.iloc[0]
        telefono = row.iloc[1]

        if pd.isna(nombre):
            continue

        telefono = None if pd.isna(telefono) else str(telefono)

        contact_id = obtener_contacto(nombre, telefono)

        for locacion in locaciones:

            valor = row[locacion]

            fecha = normalizar_fecha(valor)

            if not fecha:
                continue

            curso_nombre = f"Produccion - {locacion}"

            course_id = obtener_curso(curso_nombre)

            add_enrollment(
                contact_id=contact_id,
                course_id=course_id,
                fecha=fecha,
                evento="produccion",
                fuente="excel",
            )


def main():

    excels = list(DATA_FOLDER.glob("*.xlsx"))

    for excel in excels:

        nombre = excel.name.lower()

        if "produccion" in nombre:

            importar_excel(excel)


if __name__ == "__main__":
    main()