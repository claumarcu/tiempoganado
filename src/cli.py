from src.database.db_manager import (
    list_contacts,
    get_contacts_by_area,
    get_contacts_edicion_no_autoral,
    get_enrollments_by_phone,
    get_inactive_contacts,
    get_top_students,
)


def mostrar_contactos(filtro=None, limite=30):
    contactos = list_contacts()

    if filtro:
        contactos = [c for c in contactos if c.etiquetas == filtro]

    print()
    print("Total:", len(contactos))
    print()

    for c in contactos[:limite]:
        print(f"{c.id:4} | {c.etiquetas:10} | {c.nombre:30} | {c.telefono}")


def buscar(texto):
    contactos = list_contacts()

    resultados = [
        c for c in contactos
        if texto.lower() in c.nombre.lower()
    ]

    print()
    print("Resultados:", len(resultados))
    print()

    for c in resultados[:30]:
        print(f"{c.id:4} | {c.etiquetas:10} | {c.nombre:30} | {c.telefono}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("uso:")
        print("python -m src.cli alumnos")
        print("python -m src.cli interesados")
        print('python -m src.cli buscar "nombre"')
        print("python -m src.cli segmento edicion")
        print("python -m src.cli segmento autoral")
        print("python -m src.cli segmento fotografia")
        print("python -m src.cli segmento listo_autoral")
        print("python -m src.cli historial TELEFONO")
        print("python -m src.cli inactivos")
        exit()

    comando = sys.argv[1]

    if comando == "alumnos":
        mostrar_contactos("alumno")

    elif comando == "interesados":
        mostrar_contactos("interesado")

    elif comando == "buscar":
        texto = sys.argv[2]
        buscar(texto)

    elif comando == "segmento":

        if len(sys.argv) < 3:
            print("uso:")
            print("python -m src.cli segmento edicion")
            print("python -m src.cli segmento autoral")
            print("python -m src.cli segmento fotografia")
            print("python -m src.cli segmento listo_autoral")
            exit()

        tipo = sys.argv[2]

        if tipo == "edicion":
            rows = get_contacts_by_area("edicion")

        elif tipo == "autoral":
            rows = get_contacts_by_area("autoral")

        elif tipo == "fotografia":
            rows = get_contacts_by_area("fotografia")

        elif tipo == "listo_autoral":
            rows = get_contacts_edicion_no_autoral()

        else:
            print("segmento no reconocido")
            exit()

        print()
        print("Resultados:", len(rows))
        print()

        for r in rows:
            print(r)

    elif comando == "historial":

        if len(sys.argv) < 3:
            print("uso:")
            print("python -m src.cli historial TELEFONO")
            exit()

        telefono = sys.argv[2]

        rows = get_enrollments_by_phone(telefono)

        print()
        print("Historial de cursos")
        print()

        if not rows:
            print("No hay cursos registrados.")
        else:
            for r in rows:
                curso, fecha, evento = r
                print(f"{fecha:10} | {curso:20} | {evento}")

    elif comando == "inactivos":

        rows = get_inactive_contacts()

        print()
        print("Alumnos inactivos")
        print()

        if not rows:
            print("No hay alumnos inactivos.")
        else:
            for r in rows:
                contact_id, nombre, telefono, fecha = r
                print(f"{fecha:10} | {nombre:30} | {telefono}")

    elif comando == "top":

        rows = get_top_students()

        print()
        print("Alumnos con más cursos")
        print()

        if not rows:
            print("No hay alumnos con múltiples cursos.")
        else:
            for r in rows:
                nombre, telefono, total = r
                print(f"{total:3} | {nombre:30} | {telefono}")
                

    else:
        print("comando no reconocido")