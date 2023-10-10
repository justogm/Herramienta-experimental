import webbrowser
import time
import pyautogui
from modulos.MouseTracker.mousetracker import MouseTracker
from modulos.MouseTracker.heatmap import generarImagenes
import os
import json

# links = [LINK_DASHBOARD_A, LINK_DASHBOARD_B, LINK_CHATBOT]

with open("links.json", "r") as archi:
    links = json.load(archi)

for link, i in zip(links.keys(), range(len(links.keys()))):
    mouse_tracker = MouseTracker()
    print(f"Comenzando evaluación N°{i+1}")
    webbrowser.open(url=links[link], autoraise=True)
    time.sleep(10)
    pantalla = pyautogui.size()
    pyautogui.moveTo(pantalla[0]/2, pantalla[1]/2)
    pyautogui.hotkey('ctrl', 'alt', 'enter')
    time.sleep(5)
    pyautogui.press('z')
    pyautogui.press('f11')
    time.sleep(2)
    mouse_tracker.start_tracking()
    ruta = f"{os.path.dirname(os.path.abspath(__file__))}"
    ruta += f"/imgs/Prototipo{i}"
    pyautogui.press('f11')
    generarImagenes(ruta)