import webbrowser
import time
import pyautogui
from modulos.MouseTracker.mousetracker import MouseTracker
from modulos.MouseTracker.heatmap import generarImagenes, generarAnimacion
import os
import json

class Test:
    RUTA_CONFIG = "config.json"
    DIMENSIONES_PANTALLA = pyautogui.size()

    def __init__(self):
        self.configs = None
        self.links = None
        self.animacion = None
        self.posInicial = None
        self.__cargarConfigs()

    def __cargarConfigs(self):
        with open(self.RUTA_CONFIG, "r") as archi:
            self.configs = json.load(archi)
            self.links = self.configs["links"]
            self.animacion = self.configs["decisionAnimacion"] == 's'
            self.posInicial = (int(self.configs["posInicial"]["x"]), int(self.configs["posInicial"]["y"]))

    def getTipo(self, link):
        if "figma" in link: return "FIGMA"

    def comenzarTests(self, tiempoDeCarga = 10):
        for link, i in zip(self.links.keys(), range(len(self.links.keys()))):
            mouseTracker = MouseTracker()
            print(f"Comenzando evaluación N°{i+1}")
            webbrowser.open(url=self.links[link], autoraise=True)
            time.sleep(tiempoDeCarga)
            pyautogui.moveTo(self.posInicial)
            if(self.getTipo(self.links[link]) =="FIGMA"): self.prepararFigma()
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