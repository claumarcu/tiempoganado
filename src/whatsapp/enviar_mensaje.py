import pyautogui
import time

def enviar_mensaje(numero, mensaje):
    pyautogui.click(852, 338)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(numero, interval=0.1)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.write(mensaje, interval=0.05)
    pyautogui.press("enter")

enviar_mensaje("1155618828", "Mensaje de prueba")