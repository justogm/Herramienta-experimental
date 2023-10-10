import seaborn as sns
import matplotlib.pyplot as plt
from .src.constantes import *
import numpy as np
import os

def generarImagenes(ruta):
    # Cargar la imagen
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    imagen = plt.imread('datos/captura.png')

    # Cargar las coordenadas desde el archivo (supongamos que el archivo es un archivo CSV)
    coordenadasMov = np.genfromtxt('datos/movimientos.csv', delimiter=',', skip_header=1)

    dpi = 50

    # Crear un gráfico
    plt.figure(figsize=(ANCHO_PANTALLA/dpi, ALTO_PANTALLA/dpi))
    plt.imshow(imagen)

    # Dibujar las líneas sobre la imagen
    try:
        x = coordenadasMov[:, 0]
        y = coordenadasMov[:, 1]
        plt.plot(x, y, linestyle='-', color='red', linewidth=(5))  # Puedes ajustar el estilo y color según tus preferencias
    except IndexError:
        pass

    coordenadasClick = np.genfromtxt('datos/clicks.csv', delimiter=",", skip_header=1)

    try:
        x = coordenadasClick[:, 0]
        y = coordenadasClick[:, 1]
        plt.scatter(x, y, marker='x', color="green")
    except IndexError:
        pass

    plt.axis('off')

    plt.savefig(ruta, dpi=dpi, bbox_inches='tight', pad_inches=0)
    #plt.show()
