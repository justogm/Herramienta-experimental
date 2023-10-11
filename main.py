import webbrowser
import time
import pyautogui
from modulos.MouseTracker.mousetracker import MouseTracker
from modulos.MouseTracker.heatmap import generarImagenes, generarAnimacion
import os
import json

# links = [LINK_DASHBOARD_A, LINK_DASHBOARD_B, LINK_CHATBOT]

# with open("config.json", "r") as archi:
#     configs = json.load(archi)
#     links = configs["links"]

# for link, i in zip(links.keys(), range(len(links.keys()))):
#     mouse_tracker = MouseTracker()
#     print(f"Comenzando evaluación N°{i+1}")
#     webbrowser.open(url=links[link], autoraise=True)
#     time.sleep(10)
#     pantalla = pyautogui.size()
#     pyautogui.moveTo(pantalla[0]/2, pantalla[1]/2)
#     pyautogui.hotkey('ctrl', 'alt', 'enter')
#     time.sleep(5)
#     pyautogui.press('z')
#     pyautogui.press('f11')
#     time.sleep(2)
#     mouse_tracker.start_tracking()
#     ruta = f"{os.path.dirname(os.path.abspath(__file__))}"
#     ruta += f"/imgs/Prototipo{i}"
#     pyautogui.press('f11')
#     generarImagenes(ruta)

class Test:
    RUTA_CONFIG = "config.json"
    DIMENSIONES_PANTALLA = pyautogui.size()

    def __init__(self):
        self.configs = None
        self.links = None
        self.animacion = None
        self.__cargarConfigs()

    def __cargarConfigs(self):
        with open(self.RUTA_CONFIG, "r") as archi:
            self.configs = json.load(archi)
            self.links = self.configs["links"]
            self.animacion = self.configs["decisionAnimacion"] == 's'

    def getTipo(self, link):
        if "figma" in link: return "FIGMA"

    def comenzarTests(self, tiempoDeCarga = 10):
        for link, i in zip(self.links.keys(), range(len(self.links.keys()))):
            mouseTracker = MouseTracker()
            print(f"Comenzando evaluación N°{i+1}")
            webbrowser.open(url=self.links[link], autoraise=True)
            time.sleep(tiempoDeCarga)
            pyautogui.moveTo(self.DIMENSIONES_PANTALLA[0]/2, self.DIMENSIONES_PANTALLA[1]/2)
            if(self.getTipo(self.links[link])=="FIGMA"): self.prepararFigma()
            pyautogui.press('f11')
            time.sleep(2)
            mouseTracker.start_tracking()

            ruta = f"{os.path.dirname(os.path.abspath(__file__))}/imgs/Prototipo{i}"
            pyautogui.press('f11')
            generarImagenes(ruta)
            # if(self.animacion):
            #     generarAnimacion(ruta = f"{os.path.dirname(os.path.abspath(__file__))}/imgs/VideoProt{i}.mp4")

    def prepararFigma(self):
        pyautogui.hotkey('ctrl', 'alt', 'enter')
        time.sleep(5)
        pyautogui.press('z')

if __name__ == "__main__":
    test = Test()
    test.comenzarTests()