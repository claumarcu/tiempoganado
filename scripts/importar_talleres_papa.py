import pandas as pd
from pathlib import Path

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

    valor = str(valor).strip()

    if len(valor) != 6:
        return None

    year = int(valor[:2]) + 2000
    month = valor[2:4]
    day = valor[4:6]

    return f"{year}-{month}-{day}"


def obtener_curso(nombre):

    cursos = list_courses()

    for c in cursos:
        if c[1] == nombre:
            return c[0]

    return add_course(
        nombre=nombre,
        categoria="fotografia",
        modalidad="presencial",
        area="taller",
    )


def obtener_contacto(nombre, telefono):

    contacto = None

    if telefono:
        contacto = get_contact_by_phone(telefono)

    if contacto:
        import sqlite3

        conn = sqlite3.connect("data/alumnos.db")
        cur = conn.cursor()

        cur.execute(
            "SELECT id FROM contactos WHERE telefono = ?",
            (telefono,),
        )

        r = cur.fetchone()
        conn.close()

        if r:
            return r[0]

    contact = Contact(
        nombre=nombre,
        telefono=telefono if telefono else f"papa_{nombre}",
        email=None,
        etiquetas="alumno",
        estado=None,
        origen="excel_papa",
    )

    return add_contact(contact)


def es_participacion(valor):

    if pd.isna(valor):
        return False

    if valor == 1:
        return True

    if valor == "1":
        return True

    if valor == 1.0:
        return True

    return False


def importar_excel(path_excel):

    print("Importando:", path_excel.name)

    df = pd.read_excel(path_excel, header=None)

    fechas = df.iloc[0, 2:]
    cursos = df.iloc[1, 2:]

    for i in range(3, len(df)):

        nombre = df.iloc[i, 0]
        telefono = df.iloc[i, 1]

        if pd.isna(nombre):
            continue

        telefono = None if pd.isna(telefono) else str(telefono)

        contact_id = obtener_contacto(nombre, telefono)

        for col in range(2, len(df.columns)):

            valor = df.iloc[i, col]

            if not es_participacion(valor):
                continue

            fecha = normalizar_fecha(fechas[col])
            curso = cursos[col]

            if not fecha:
                continue

            if pd.isna(curso):
                continue

            course_id = obtener_curso(str(curso).strip())

            add_enrollment(
                contact_id=contact_id,
                course_id=course_id,
                fecha=fecha,
                evento="taller_papa",
                fuente="excel",
            )


def main():

    excels = list(DATA_FOLDER.glob("*.xlsx"))

    print("Excel encontrados:", len(excels))

    for excel in excels:

        nombre = excel.name.lower()

        if "jam" in nombre:
            continue

        if "madre" in nombre:
            continue

        importar_excel(excel)


if __name__ == "__main__":
    main()