import pyautogui
import time
from src.constantes import *

registro = open("datos/registro.csv", "w")
instrucciones = open("src/instrucciones.txt", "r").readlines()
for i in instrucciones: print(i)
registro.write("x,y\n")
chunk = []
while True:
    try:
        x, y = pyautogui.position()
        reg = f"{x},{y}\n"
        chunk.append(reg)

        if(len(chunk) == 20):
            registro.writelines(chunk)
            chunk = []

        time.sleep(TIEMPO_MUESTREO)  # Espera 1 segundo antes de volver a registrar la posición
    except KeyboardInterrupt:
        registro.writelines(chunk)
        break

registro.close()