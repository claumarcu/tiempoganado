from src.database.db_manager import get_connection

def limpiar_contactos_invalidos():
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM contactos
        WHERE etiquetas IS NULL
        """)

        deleted = cursor.rowcount

        conn.commit()

    print("Contactos eliminados:", deleted)


if __name__ == "__main__":
    limpiar_contactos_invalidos()