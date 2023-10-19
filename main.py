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
        '''__init__ Constructor de la clase Test.

        Se cargan configuraciones de utilidad para la 
        posterior evaluación.
        '''
        self.configs = None
        self.links = None
        self.animacion = None
        self.posInicial = None
        self.__cargarConfigs()

    def __cargarConfigs(self):
        '''__cargarConfigs Carga las configuraciones.

        Método utilizado en la construcción para cargar
        las configuraciones.
        '''
        with open(self.RUTA_CONFIG, "r") as archi:
            self.configs = json.load(archi)
            self.links = self.configs["links"]
            self.animacion = self.configs["decisionAnimacion"] == 's'
            self.posInicial = [self.configs["posInicial"]["x"], self.configs["posInicial"]["y"]]

    def getTipo(self, link):
        '''getTipo Devuelve el tipo de proyecto.

        Método para identificar con que tipo de proyecto se desea trabajar.

        Args:
            link (str): Link a interfaz a evaluar.

        Returns:
            str: "FIGMA" para prototipos de figma.
        '''
        if "figma" in link: return "FIGMA"

    def comenzarTests(self, tiempoDeCarga = 8):
        '''comenzarTests Comienza la evaluación.

        Con él se inicia la evaluación de las interfaces gráficas,
        se irán presentando al usuario de la forma que se cosidere
        apropiada, se iran registrando los eventos del mouse y al 
        final se generarán gráficas con las acciones realizadas
        por el usuario. 

        Args:
            tiempoDeCarga (int, optional): Tiempo que requiere la interfaz hasta estar funcional. Por defecto 8.
        '''
        for link, i in zip(self.links.keys(), range(len(self.links.keys()))):
            mouseTracker = MouseTracker()
            print(f"Comenzando evaluación N°{i+1}")
            webbrowser.open(url=self.links[link], autoraise=True)
            time.sleep(tiempoDeCarga)

            self.__moverAPosDeInicio()
            
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
        '''prepararFigma Prepara para el usuario la interfaz de figma.

        Realiza las interacciones necesarias para que el usuario no 
        tenga complicaciones extras.
        '''
        time.sleep(0)
        pyautogui.press('z')

    def __moverAPosDeInicio(self):
        '''__moverAPosDeInicio Mueve a posición de inicio

        Mueve el mouse a la posición indicada en las configuraciones.
        '''
        x, y = self.DIMENSIONES_PANTALLA[0], self.DIMENSIONES_PANTALLA[1]
        x, y = eval(self.posInicial[0]), eval(self.posInicial[1])
        self.posInicial = [x, y]
        pyautogui.moveTo(self.posInicial)


if __name__ == "__main__":
    test = Test()
    test.comenzarTests()