import sqlite3

conn = sqlite3.connect("data/alumnos.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

print("TABLAS EN LA BASE:")
for t in tables:
    print("-", t[0])