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

MESES = {
    "enero": "01",
    "febrero": "02",
    "marzo": "03",
    "abril": "04",
    "mayo": "05",
    "junio": "06",
    "julio": "07",
    "agosto": "08",
    "septiembre": "09",
    "octubre": "10",
    "noviembre": "11",
    "diciembre": "12",
}


def detectar_curso(nombre_archivo):

    nombre = nombre_archivo.lower()

    if "lr" in nombre:
        return "JAM LR"

    if "photoshop" in nombre:
        return "JAM Photoshop"

    return "JAM"


def cargar_curso(nombre):

    cursos = list_courses()

    for c in cursos:
        course_id, curso_nombre, *_ = c

        if curso_nombre == nombre:
            return course_id

    return add_course(
        nombre=nombre,
        categoria="edicion",
        modalidad="jam",
        area="edicion",
    )


def obtener_contacto(nombre, telefono):

    contacto = get_contact_by_phone(telefono)

    if contacto:
        # el objeto no tiene id, lo buscamos directo en la base
        import sqlite3
        conn = sqlite3.connect("data/alumnos.db")
        cur = conn.cursor()
        cur.execute(
            "SELECT id FROM contactos WHERE telefono = ?",
            (telefono,),
        )
        result = cur.fetchone()
        conn.close()

        if result:
            return result[0]

    contact = Contact(
        nombre=nombre,
        telefono=telefono,
        email=None,
        etiquetas="alumno",
        estado=None,
        origen="excel",
    )

    return add_contact(contact)


def importar_excel(path_excel):

    print(f"\nImportando: {path_excel.name}")

    curso_nombre = detectar_curso(path_excel.name)

    course_id = cargar_curso(curso_nombre)

    df = pd.read_excel(path_excel)

    meses = [c.lower() for c in df.columns if c.lower() in MESES]

    for idx, row in df.iterrows():

        nombre = row["Nombre"]

        if pd.isna(nombre):
            continue

        telefono = f"jam_{idx}"

        contact_id = obtener_contacto(nombre, telefono)

        for mes in meses:

            valor = row[mes.capitalize()]

            if pd.isna(valor):
                continue

            if valor == "X":
                continue

            mes_num = MESES[mes]

            fecha = f"2026-{mes_num}-01"

            add_enrollment(
                contact_id=contact_id,
                course_id=course_id,
                fecha=fecha,
                evento="jam",
                fuente="excel",
            )


def main():

    excels = list(DATA_FOLDER.glob("JAM*.xlsx"))

    print(f"\nArchivos JAM encontrados: {len(excels)}")

    for excel in excels:
        importar_excel(excel)


if __name__ == "__main__":
    main()