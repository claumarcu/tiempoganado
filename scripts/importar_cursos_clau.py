import pandas as pd
from pathlib import Path
import sqlite3
import re

from src.database.db_manager import (
    Contact,
    add_contact,
    add_enrollment,
    add_course,
    list_courses,
)

DATA_FOLDER = Path("data_excel")


def extraer_fecha(nombre_archivo):

    meses = {
        "enero":1,"febrero":2,"marzo":3,"abril":4,
        "mayo":5,"junio":6,"julio":7,"agosto":8,
        "septiembre":9,"setiembre":9,
        "octubre":10,"noviembre":11,"diciembre":12,
    }

    texto = nombre_archivo.lower()

    mes = None
    for m in meses:
        if m in texto:
            mes = meses[m]
            break

    year_match = re.search(r"20\d{2}", texto)

    if mes and year_match:
        year = year_match.group()
        return f"{year}-{mes:02d}-01"

    return None


def obtener_curso(nombre):

    cursos = list_courses()

    for c in cursos:
        if c[1] == nombre:
            return c[0]

    return add_course(
        nombre=nombre,
        categoria="fotografia",
        modalidad="curso",
        area="clau",
    )


def obtener_contacto(nombre):

    telefono = f"clau_{nombre}"

    conn = sqlite3.connect("data/alumnos.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT id FROM contactos WHERE telefono = ?",
        (telefono,),
    )

    r = cur.fetchone()

    if r:
        conn.close()
        return r[0]

    contact = Contact(
        nombre=nombre,
        telefono=telefono,
        email=None,
        etiquetas="alumno",
        estado=None,
        origen="excel_clau",
    )

    contact_id = add_contact(contact)

    conn.close()

    return contact_id


def importar_excel(path_excel):

    print("Importando:", path_excel.name)

    df = pd.read_excel(path_excel)

    fecha = extraer_fecha(path_excel.name)

    curso_nombre = path_excel.stem

    course_id = obtener_curso(curso_nombre)

    for _, row in df.iterrows():

        nombre = row.iloc[0]

        if pd.isna(nombre):
            continue

        contact_id = obtener_contacto(nombre)

        add_enrollment(
            contact_id=contact_id,
            course_id=course_id,
            fecha=fecha,
            evento="curso_clau",
            fuente="excel",
        )


def main():

    excels = list(DATA_FOLDER.glob("*.xlsx"))

    for excel in excels:

        nombre = excel.name.lower()

        if "produccion" in nombre:
            continue

        if "jam" in nombre:
            continue

        if "madre" in nombre:
            continue

        if "papa" in nombre:
            continue

        importar_excel(excel)


if __name__ == "__main__":
    main()