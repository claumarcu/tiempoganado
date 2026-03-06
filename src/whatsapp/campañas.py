import time

import pyautogui

from src.database.db_manager import list_contacts

MENSAJE = """Hola! 😊
Este es un mensaje de prueba de mi sistema de envíos.

No hace falta responder, estoy probando una herramienta nueva.
"""


# CONTACTOS DE PRUEBA
CONTACTOS_PRUEBA = [
    "1K Andrea Kranevitter",
    "1K stella rodriguez"
]


def obtener_contactos_prueba():

    contactos = list_contacts()

    return [c for c in contactos if c.nombre in CONTACTOS_PRUEBA]


def abrir_chat(numero):

    # aseguramos foco en WhatsApp
    pyautogui.click(300, 300)

    time.sleep(1)

    # abrir buscador
    pyautogui.hotkey("ctrl", "k")

    time.sleep(1)

    # escribir numero
    pyautogui.write(numero, interval=0.03)

    time.sleep(1)

    # abrir chat
    pyautogui.press("enter")

    time.sleep(2)


def escribir_mensaje():

    pyautogui.write(MENSAJE, interval=0.02)


def campaña():

    contactos = obtener_contactos_prueba()

    print()
    print("MODO PRUEBA ACTIVO")
    print("Contactos de prueba:", len(contactos))
    print()

    print("IMPORTANTE:")
    print("Dejá WhatsApp Web abierto en Chrome.")
    print("No toques mouse ni teclado mientras corre el script.")
    print()

    input("Presioná ENTER para comenzar...")

    for c in contactos:

        print("Preparando mensaje para:", c.nombre)

        abrir_chat(c.telefono)

        escribir_mensaje()

        input("Revisá el mensaje en WhatsApp. " \
        "Cuando quieras pasar al siguiente presioná ENTER...")

        time.sleep(1)


if __name__ == "__main__":

    campaña()