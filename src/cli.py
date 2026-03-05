from src.database.db_manager import list_contacts


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
        exit()

    comando = sys.argv[1]

    if comando == "alumnos":
        mostrar_contactos("alumno")

    elif comando == "interesados":
        mostrar_contactos("interesado")

    elif comando == "buscar":
        texto = sys.argv[2]
        buscar(texto)

    else:
        print("comando no reconocido")
        