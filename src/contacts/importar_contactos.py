from __future__ import annotations

import csv
import re
from pathlib import Path
from typing import Dict, Optional, Set

from src.config import CONTACTS_FILE
from src.database.db_manager import Contact, add_contact, initialize_database


def normalize_phone(phone: str) -> Optional[str]:
    """Normaliza teléfonos argentinos."""

    if not phone:
        return None

    digits = re.sub(r"\D", "", phone)

    if len(digits) < 8:
        return None

    # formato internacional correcto
    if digits.startswith("549"):
        return digits

    if digits.startswith("54"):
        return "9" + digits

    if digits.startswith("11"):
        return "549" + digits

    if len(digits) == 10:
        return "549" + digits

    return digits


def clean_text(text: str) -> str:
    """Limpia emojis y espacios extra."""

    if not text:
        return ""

    text = text.strip()

    # eliminar caracteres raros
    text = re.sub(r"[^\w\s@.-]", "", text)

    # normalizar espacios
    text = re.sub(r"\s+", " ", text)

    return text


def build_name(row: Dict[str, str]) -> str:
    """Reconstruye nombre desde columnas de Google Contacts."""

    first = row.get("First Name", "")
    middle = row.get("Middle Name", "")
    last = row.get("Last Name", "")

    name = f"{first} {middle} {last}".strip()

    name = clean_text(name)

    return name


def extract_phone(row: Dict[str, str]) -> Optional[str]:
    """Extrae primer teléfono válido."""

    for field in (
        "Phone 1 - Value",
        "Phone 2 - Value",
        "Phone 3 - Value",
    ):
        phone = row.get(field)

        if not phone:
            continue

        normalized = normalize_phone(phone)

        if normalized:
            return normalized

    return None


def detect_tag(name: str) -> Optional[str]:
    """
    Detecta etiquetas según convención agenda.

    1K → alumno
    1A → interesado
    """

    lowered = name.lower()

    if lowered.startswith("1k"):
        return "alumno"

    if lowered.startswith("1a"):
        return "interesado"

    return None


def importar() -> None:
    path = Path(CONTACTS_FILE)

    if not path.exists():
        raise RuntimeError(f"No existe archivo: {path}")

    initialize_database()

    inserted = 0
    skipped = 0

    seen: Set[str] = set()

    with open(path, encoding="utf-8") as f:

        reader = csv.DictReader(f)

        for row in reader:

            name = build_name(row)

            if not name:
                skipped += 1
                continue

            tag = detect_tag(name)

            phone = extract_phone(row)

            if not phone:
                skipped += 1
                continue

            if phone in seen:
                skipped += 1
                continue

            seen.add(phone)

            email = row.get("E-mail 1 - Value", "")

            contact = Contact(
                id=None,
                nombre=name,
                telefono=phone,
                email=email,
                etiquetas=tag,
                estado="activo",
                origen="google_contacts",
            )

            try:
                add_contact(contact)
                inserted += 1
            except Exception:
                skipped += 1

    print()
    print("Importación finalizada")
    print("Contactos insertados:", inserted)
    print("Contactos descartados:", skipped)


if __name__ == "__main__":
    importar()