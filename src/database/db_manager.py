from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Iterator, List, Optional

from src.config import DATABASE_CONFIG

# ---------------------------------------------------------------------
# DATA MODEL
# ---------------------------------------------------------------------

@dataclass
class Contact:
    id: Optional[int]
    nombre: str
    telefono: str
    email: Optional[str]
    etiquetas: Optional[str]
    estado: str
    origen: Optional[str]


# ---------------------------------------------------------------------
# DATABASE CONNECTION
# ---------------------------------------------------------------------

@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    conn = sqlite3.connect(
        DATABASE_CONFIG.db_path,
        timeout=DATABASE_CONFIG.timeout,
    )
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


# ---------------------------------------------------------------------
# DATABASE INITIALIZATION
# ---------------------------------------------------------------------

def initialize_database() -> None:
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS contactos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                telefono TEXT UNIQUE NOT NULL,
                email TEXT,
                etiquetas TEXT,
                estado TEXT DEFAULT 'activo',
                origen TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contacto_id INTEGER,
                mensaje TEXT,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(contacto_id) REFERENCES contactos(id)
            )
            """
        )

        conn.commit()


# ---------------------------------------------------------------------
# CONTACT OPERATIONS
# ---------------------------------------------------------------------

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

        return int(cursor.lastrowid)


def get_contact_by_phone(phone: str) -> Optional[Contact]:
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM contactos
            WHERE telefono = ?
            """,
            (phone,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Contact(
            id=row["id"],
            nombre=row["nombre"],
            telefono=row["telefono"],
            email=row["email"],
            etiquetas=row["etiquetas"],
            estado=row["estado"],
            origen=row["origen"],
        )


def list_contacts() -> List[Contact]:
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM contactos")

        rows = cursor.fetchall()

        contacts: List[Contact] = []

        for row in rows:
            contacts.append(
                Contact(
                    id=row["id"],
                    nombre=row["nombre"],
                    telefono=row["telefono"],
                    email=row["email"],
                    etiquetas=row["etiquetas"],
                    estado=row["estado"],
                    origen=row["origen"],
                )
            )

        return contacts