import pyautogui
import time

registro = open("datos/registro.csv", "w")

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

        time.sleep(0.05)  # Espera 1 segundo antes de volver a registrar la posición
    except KeyboardInterrupt:
        registro.writelines(chunk)
        break

registro.close()