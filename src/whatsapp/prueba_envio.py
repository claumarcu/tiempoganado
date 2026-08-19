import pyautogui
import time

print("Preparando prueba...")
time.sleep(3)

pyautogui.click(852, 338)
time.sleep(1)

numeros = [
    "16505216945"
]

for numero in numeros:
    pyautogui.click(852, 338)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(numero, interval=0.1)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.write("mira lo que logre, ya manda mensajes por mi", interval=0.05)
    pyautogui.press("enter")

print("Listo")