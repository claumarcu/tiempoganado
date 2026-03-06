from __future__ import annotations

from collections import defaultdict

from src.database.db_manager import list_contacts


def auditar() -> None:

    contactos = list_contacts()

    telefonos = defaultdict(list)

    for c in contactos:
        telefonos[c.telefono].append(c)

    duplicados = {t: cs for t, cs in telefonos.items() if len(cs) > 1}

    print()
    print("Total contactos:", len(contactos))
    print("Telefonos duplicados:", len(duplicados))
    print()

    for telefono, lista in duplicados.items():

        print("Telefono:", telefono)

        for c in lista:
            print("   ", c.id, "|", c.nombre)

        print()


if __name__ == "__main__":
    auditar()