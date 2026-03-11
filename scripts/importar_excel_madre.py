import pandas as pd
import sqlite3
from pathlib import Path

from src.database.db_manager import (
    Contact,
    get_contact_by_phone,
    add_contact,
    add_enrollment,
    add_course,
    list_courses,
)

EXCEL = Path("data_excel/Excel madre.xlsx")

CURSOS = [
    "BASICO",
    "BASICO INT",
    "NIVEL II",
    "NIVEL III",
    "PHOTOS I",
    "PHOTOS II",
    "PHOTOS 3",
    "PHOTOS ByN",
    "Photoshop Pieles",
    "JORNADA ROD.",
    "PROYECTO",
    "LA MIRADA",
    "POETICAS",
    "LR",
]


def limpiar_fecha(texto):

    if pd.isna(texto):
        return None

    # Excel lo interpretó como fecha real
    if isinstance(texto, pd.Timestamp):
        return texto.strftime("%Y-%m-01")

    texto = str(texto).lower().strip()

    meses = {
        "ene": 1, "enero": 1,
        "feb": 2, "febrero": 2,
        "mar": 3, "marzo": 3,
        "abr": 4, "abril": 4,
        "may": 5, "mayo": 5,
        "jun": 6, "junio": 6,
        "jul": 7, "julio": 7,
        "ago": 8, "agosto": 8,
        "sep": 9, "sept": 9, "septiembre": 9,
        "oct": 10, "octubre": 10,
        "nov": 11, "noviembre": 11,
        "dic": 12, "diciembre": 12,
    }

    mes = None

    for k, v in meses.items():
        if k in texto:
            mes = v
            break

    if mes is None:
        return None

    numeros = [c for c in texto if c.isdigit()]

    if len(numeros) < 2:
        return None

    year = int("".join(numeros[-2:]))

    if year < 50:
        year += 2000
    else:
        year += 1900

    return f"{year}-{mes:02d}-01"


def cargar_cursos():

    existentes = {}

    rows = list_courses()

    for r in rows:
        course_id, nombre, categoria, modalidad, area = r
        existentes[nombre] = course_id

    for curso in CURSOS:

        if curso not in existentes:

            course_id = add_course(
                nombre=curso,
                categoria="hist",
                modalidad="hist",
                area="hist",
            )

            existentes[curso] = course_id

    return existentes


def obtener_contact_id(telefono):

    with sqlite3.connect("data/alumnos.db") as conn:
        cur = conn.cursor()

        cur.execute(
            "SELECT id FROM contactos WHERE telefono = ?",
            (telefono,)
        )

        row = cur.fetchone()

        if row:
            return row[0]

    return None


def main():

    df = pd.read_excel(EXCEL)

    df.columns = df.columns.str.strip()

    cursos = cargar_cursos()

    for i, row in df.iterrows():

        nombre = row.get("NOMBRE")
        telefono = row.get("CELULAR")

        if pd.isna(nombre):
            continue

        telefono = None if pd.isna(telefono) else str(telefono)

        if not telefono:
            telefono = f"excel_{i}"

        contact_id = obtener_contact_id(telefono)

        if contact_id is None:

            contact = Contact(
                nombre=nombre,
                telefono=telefono,
                email=row.get("MAIL"),
                etiquetas="alumno",
                estado=None,
                origen="excel",
            )

            contact_id = add_contact(contact)

        for curso in CURSOS:

            if curso not in row:
                continue

            fecha = limpiar_fecha(row[curso])

            if not fecha:
                continue

            course_id = cursos[curso]

            add_enrollment(
                contact_id=contact_id,
                course_id=course_id,
                fecha=fecha,
                evento="excel_madre",
                fuente="excel",
            )


if __name__ == "__main__":
    main()