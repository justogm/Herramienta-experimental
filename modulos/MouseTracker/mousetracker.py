from .src.constantes import *
        
from pynput import mouse, keyboard
import os
from PIL import ImageGrab
import sys

class StopTracking(Exception):
    pass

class MouseTracker:
    def __init__(self):
        self.mouse_listener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click
        )

        self.keyboard_listener = keyboard.Listener(
            on_press=self.on_key_press
        )

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        self.regMov = open("datos/movimientos.csv", "w")
        self.chunkMov = []

        self.regClick = open("datos/clicks.csv", "w")
        self.chunkClick = []

        self.regScroll = open("datos/scroll.csv", "w")
        self.chunkScroll = []

        self.escuchando = False

    def on_move(self, x, y):
        if len(self.chunkMov) == 30:
            self.regMov.writelines(self.chunkMov)
            self.regMov.flush()
            self.chunkMov = [f"{x},{y}\n"]
        else:
            self.chunkMov.append(f"{x},{y}\n")
        #print(f'Mouse movido a ({x}, {y})')

    def on_click(self, x, y, button, pressed):
        if pressed:
            if len(self.chunkClick) == 30:
                self.regClick.writelines(self.chunkClick)
                self.regClick.flush()
                self.chunkClick = [f"{x},{y},{button}\n"]
            else:
                self.chunkClick.append(f"{x},{y},{button}\n")

    def on_scroll(self, x, y, dx, dy):
        mov = 'down' if dy < 0 else 'up'
        if len(self.chunkScroll) == 30:
            self.regScroll.writelines(self.chunkScroll)
            self.regScroll.flush()
            self.chunkScroll = [f"{x},{y},{mov}\n"]
        else:
            self.chunkScroll.append(f"{x},{y},{mov}\n")

    def on_key_press(self, key):
        if key == keyboard.Key.esc:
            self.escuchando = False
            #print("Se apreto Esc.")

    def start_tracking(self):
        self.escuchando = True
        captura = ImageGrab.grab()
        captura.save("datos/captura.png")
        self.regMov.write("x,y\n")
        self.regClick.write("x,y,lado\n")
        self.regScroll.write("x,y,mov\n")
        try:
            with self.mouse_listener as mListener, self.keyboard_listener as kListener:
                while self.escuchando:
                    pass
                self.stop_tracking()
        except:
            self.stop_tracking()
            
    

            
                
    def stop_tracking(self):
        self.keyboard_listener.stop()
        self.mouse_listener.stop()
        self.regMov.writelines(self.chunkMov)
        self.regMov.flush()
        self.regClick.writelines(self.chunkClick)
        self.regClick.flush()
        self.regScroll.writelines(self.chunkScroll)
        self.regScroll.flush()
        # sys.exit()

        

if __name__ == "__main__":
    tracker = MouseTracker()
    tracker.start_tracking()

        

