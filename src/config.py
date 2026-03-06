from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

# ---------------------------------------------------------------------
# ROOT PATHS
# ---------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"


# ---------------------------------------------------------------------
# DATA FILES
# ---------------------------------------------------------------------

DATABASE_PATH = DATA_DIR / "alumnos.db"
CONTACTS_FILE = DATA_DIR / "contactos.csv"
TAGS_FILE = DATA_DIR / "etiquetas.json"

LOG_FILE = LOG_DIR / "historial_envios.log"


# ---------------------------------------------------------------------
# ENVIRONMENT
# ---------------------------------------------------------------------

def get_env(name: str, default: str | None = None) -> str:
    value = os.getenv(name, default)
    if value is None:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


# ---------------------------------------------------------------------
# WHATSAPP CONFIG
# ---------------------------------------------------------------------

@dataclass(frozen=True)
class WhatsAppConfig:
    rate_limit_seconds: float = 15.0
    max_daily_messages: int = 200
    default_country_code: str = "54"


# ---------------------------------------------------------------------
# DATABASE CONFIG
# ---------------------------------------------------------------------

@dataclass(frozen=True)
class DatabaseConfig:
    db_path: Path = DATABASE_PATH
    timeout: float = 10.0


# ---------------------------------------------------------------------
# GLOBAL SETTINGS OBJECTS
# ---------------------------------------------------------------------

WHATSAPP_CONFIG = WhatsAppConfig()
DATABASE_CONFIG = DatabaseConfig()


# ---------------------------------------------------------------------
# ENSURE DIRECTORIES EXIST
# ---------------------------------------------------------------------

def ensure_directories() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    LOG_DIR.mkdir(exist_ok=True)


ensure_directories()