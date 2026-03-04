from __future__ import annotations

import csv
import re
from pathlib import Path

from src.database.db_manager import Contact, add_contact, initialize_database
from src.config import CONTACTS_FILE


def normalize_phone(phone: str) -> str | None:
    """Normaliza teléfonos argentinos."""
    if not phone:
        return None

    digits = re.sub(r"\D", "", phone)

    if len(digits) < 8:
        return None

    # Si ya viene con código país
    if digits.startswith("54"):
        return digits

    # Si es celular típico argentino
    if digits.startswith("11"):
        return "549" + digits

    return digits


def build_name(row: dict) -> str:
    first = row.get("First Name", "").strip()
    last = row.get("Last Name", "").strip()

    name = f"{first} {last}".strip()

    if not name:
        return "sin_nombre"

    return name


def extract_phone(row: dict) -> str | None:
    for field in [
        "Phone 1 - Value",
        "Phone 2 - Value",
        "Phone 3 - Value",
    ]:
        phone = row.get(field)
        if phone:
            normalized = normalize_phone(phone)
            if normalized:
                return normalized

    return None


def importar() -> None:
    path = Path(CONTACTS_FILE)

    if not path.exists():
        raise RuntimeError(f"No existe archivo: {path}")

    initialize_database()

    inserted = 0
    skipped = 0
    seen = set()

    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            phone = extract_phone(row)

            if not phone:
                skipped += 1
                continue

            if phone in seen:
                skipped += 1
                continue

            seen.add(phone)

            name = build_name(row)
            email = row.get("E-mail 1 - Value")

            contact = Contact(
                id=None,
                nombre=name,
                telefono=phone,
                email=email,
                etiquetas=None,
                estado="activo",
                origen="google_contacts",
            )

            try:
                add_contact(contact)
                inserted += 1
            except Exception:
                skipped += 1

    print("Importación finalizada")
    print("Contactos insertados:", inserted)
    print("Contactos descartados:", skipped)


if __name__ == "__main__":
    importar()