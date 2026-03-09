from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Optional, List

DB_PATH = Path("data/alumnos.db")


@dataclass
class Contact:
    nombre: str
    telefono: str
    email: Optional[str] = None
    etiquetas: Optional[str] = None
    estado: Optional[str] = None
    origen: Optional[str] = None


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()


# -----------------------------
# CONTACTOS
# -----------------------------

def initialize_database() -> None:
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS contactos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                telefono TEXT UNIQUE,
                email TEXT,
                etiquetas TEXT,
                estado TEXT,
                origen TEXT
            )
            """
        )

        conn.commit()


def add_contact(contact: Contact) -> int:
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO contactos (nombre, telefono, email, etiquetas, estado, origen)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                contact.nombre,
                contact.telefono,
                contact.email,
                contact.etiquetas,
                contact.estado,
                contact.origen,
            ),
        )

        conn.commit()

        row_id = cursor.lastrowid
        if row_id is None:
            raise RuntimeError("No se pudo obtener lastrowid")

        return int(row_id)


def list_contacts() -> List[Contact]:
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT nombre, telefono, email, etiquetas, estado, origen
            FROM contactos
            """
        )

        rows = cursor.fetchall()

        contacts: List[Contact] = []

        for row in rows:
            contacts.append(
                Contact(
                    nombre=row[0],
                    telefono=row[1],
                    email=row[2],
                    etiquetas=row[3],
                    estado=row[4],
                    origen=row[5],
                )
            )

        return contacts


def get_contact_by_phone(phone: str) -> Optional[Contact]:
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT nombre, telefono, email, etiquetas, estado, origen
            FROM contactos
            WHERE telefono = ?
            """,
            (phone,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Contact(
            nombre=row[0],
            telefono=row[1],
            email=row[2],
            etiquetas=row[3],
            estado=row[4],
            origen=row[5],
        )


# -----------------------------
# CURSOS
# -----------------------------

def add_course(nombre: str, categoria: str, modalidad: str, area: str) -> int:

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO courses (nombre, categoria, modalidad, area)
            VALUES (?, ?, ?, ?)
            """,
            (nombre, categoria, modalidad, area),
        )

        conn.commit()

        row_id = cursor.lastrowid
        if row_id is None:
            raise RuntimeError("No se pudo obtener lastrowid")

        return int(row_id)


def list_courses():
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id, nombre, categoria, modalidad, area
            FROM courses
            """
        )

        return cursor.fetchall()


# -----------------------------
# ENROLLMENTS
# -----------------------------

def add_enrollment(
    contact_id: int,
    course_id: int,
    fecha: str,
    evento: str | None = None,
    fuente: str | None = None,
) -> int:

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO enrollments (contact_id, course_id, fecha, evento, fuente)
            VALUES (?, ?, ?, ?, ?)
            """,
            (contact_id, course_id, fecha, evento, fuente),
        )

        conn.commit()

        row_id = cursor.lastrowid
        if row_id is None:
            raise RuntimeError("No se pudo obtener lastrowid")

        return int(row_id)


def list_enrollments():

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT contact_id, course_id, fecha, evento, fuente
            FROM enrollments
            """
        )

        return cursor.fetchall()


def get_enrollments_by_contact(contact_id: int):

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                enrollments.fecha,
                courses.nombre,
                courses.modalidad,
                courses.track,
                enrollments.evento
            FROM enrollments
            JOIN courses
            ON enrollments.course_id = courses.id
            WHERE enrollments.contact_id = ?
            ORDER BY enrollments.fecha
            """,
            (contact_id,),
        )

def get_contacts_by_area(area: str):

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT DISTINCT
                contactos.id,
                contactos.nombre,
                contactos.telefono
            FROM contactos
            JOIN enrollments
                ON contactos.id = enrollments.contact_id
            JOIN courses
                ON enrollments.course_id = courses.id
            WHERE courses.area = ?
            """,
            (area,),
        )
        return cursor.fetchall()
    
def get_contacts_edicion_no_autoral():

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT DISTINCT
                c.id,
                c.nombre,
                c.telefono
            FROM contactos c
            JOIN enrollments e
                ON c.id = e.contact_id
            JOIN courses ed
                ON e.course_id = ed.id
            WHERE ed.area = 'edicion'
            AND c.id NOT IN (
                SELECT c2.id
                FROM contactos c2
                JOIN enrollments e2
                    ON c2.id = e2.contact_id
                JOIN courses au
                    ON e2.course_id = au.id
                WHERE au.area = 'autoral'
            )
        """)

        return cursor.fetchall()

def get_enrollments_by_phone(phone: str):

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                courses.nombre,
                enrollments.fecha,
                enrollments.evento
            FROM contactos
            JOIN enrollments
                ON contactos.id = enrollments.contact_id
            JOIN courses
                ON enrollments.course_id = courses.id
            WHERE contactos.telefono = ?
            ORDER BY enrollments.fecha
            """,
            (phone,),
        )

def get_inactive_contacts(months: int = 12):

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                contactos.id,
                contactos.nombre,
                contactos.telefono,
                MAX(enrollments.fecha) as ultimo_curso
            FROM contactos
            JOIN enrollments
                ON contactos.id = enrollments.contact_id
            GROUP BY contactos.id
            HAVING ultimo_curso <= date('now', ?)
            ORDER BY ultimo_curso
            """,
            (f"-{months} months",),
        )

        return cursor.fetchall()
    
def get_top_students(min_cursos: int = 3):

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                contactos.nombre,
                contactos.telefono,
                COUNT(enrollments.id) as total
            FROM contactos
            JOIN enrollments
                ON contactos.id = enrollments.contact_id
            GROUP BY contactos.id
            HAVING total >= ?
            ORDER BY total DESC
            """,
            (min_cursos,),
        )

        return cursor.fetchall()
