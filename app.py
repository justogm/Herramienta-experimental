import pyautogui
import time
from src.constantes import *

# class MouseTracker:
#     def __init__(self):
#         self.registro = open("datos/registro.csv", "w")
#         self.instrucciones = open("src/instrucciones.txt", "r").readlines()

#     def registrar(self):
#         for i in self.instrucciones: print(i)

#         self.registro.write("x,y\n")
#         chunk = []
#         while 1:
#             try:
#                 x, y = pyautogui.position()
#                 reg = f"{x},{y}\n"
#                 chunk.append(reg)

#                 if(len(chunk) == 20):
#                     self.registro.writelines(chunk)
#                     chunk = []
                
#                 time.sleep(TIEMPO_MUESTREO)
#             except KeyboardInterrupt:
#                 self.registro.writelines(chunk)
#                 break
        
#         self.registro.close()
        
from pynput import mouse

class MouseTracker:
    def __init__(self):
        self.mouse_listener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
            on_scroll=self.on_scroll
        )

        self.regMov = open("datos/movimientos.csv", "w")
        self.chunkMov = []

        self.regClick = open("datos/clicks.csv", "w")
        self.chunkClick = []

        self.regScroll = open("datos/scroll.csv", "w")
        self.chunkScroll = []

    def on_move(self, x, y):
        if len(self.chunkMov) == 30:
            self.regMov.writelines(self.chunkMov)
            self.chunkMov = [f"{x},{y}"]
        else:
            self.chunkMov.append(f"{x},{y}")
        # print(f'Mouse movido a ({x}, {y})')

    def on_click(self, x, y, button, pressed):
        if pressed:
            if len(self.chunkClick) == 30:
                self.regClick.writelines(self.chunkClick)
                self.chunkClick = [f"{x},{y},{button}"]
            else:
                self.chunkMov.append(f"{x},{y},{button}")
            # print(f'Clic {button} presionado en ({x}, {y})')

    def on_scroll(self, x, y, dx, dy):
        mov = 'down' if dy < 0 else 'up'
        if len(self.chunkScroll) == 30:
            self.regScroll.writelines(self.chunkScroll)
            self.chunkScroll = [f"{x},{y},{}"]


    def start_tracking(self):
        self.regMov.write("x,y")
        self.regClick.write("x,y,lado")
        self.regScroll.write("x,y,mov")
        with self.mouse_listener as listener:
            listener.join()

        listener.start()

if __name__ == "__main__":
    tracker = MouseTracker()
    tracker.start_tracking()

        

