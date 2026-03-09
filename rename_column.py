import sqlite3

conn = sqlite3.connect("data/alumnos.db")
cursor = conn.cursor()

print("Renombrando columna track → area...")

cursor.execute(
    """
    ALTER TABLE courses
    RENAME COLUMN track TO area
    """
)

conn.commit()

print("Columnas actuales de la tabla courses:")

cursor.execute("PRAGMA table_info(courses)")
for row in cursor.fetchall():
    print(row)

conn.close()

print("Migración terminada.")