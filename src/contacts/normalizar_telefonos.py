import re
from src.database.db_manager import get_connection


def limpiar_numero(numero):
    if not numero:
        return None

    digits = re.sub(r"\D", "", numero)

    if len(digits) < 10:
        return None

    # cortar números demasiado largos
    if len(digits) > 13:
        digits = digits[:13]

    if digits.startswith("549"):
        return digits

    if digits.startswith("11"):
        return "549" + digits

    return digits


def normalizar():
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT id, telefono FROM contactos")
        rows = cursor.fetchall()

        corregidos = 0

        for r in rows:
            nuevo = limpiar_numero(r["telefono"])

            if nuevo and nuevo != r["telefono"]:
                cursor.execute(
                    "UPDATE contactos SET telefono=? WHERE id=?",
                    (nuevo, r["id"]),
                )
                corregidos += 1

        conn.commit()

    print("Teléfonos corregidos:", corregidos)


if __name__ == "__main__":
    normalizar()