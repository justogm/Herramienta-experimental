import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from .src.constantes import *
import numpy as np
import os
import plotly.express as px

def generarImagenes(ruta):
    '''generarImagenes Genera imágenes a partir
    de los registros de interacciones del usuario.

    A partir de los registros de movimientos, clicks y scroll
    realiza gráficas sobre la imágen presentada al usuario para
    su posterior análisis

    Args:
        ruta (str): Ruta donde debe almacenarse la imágen.
    '''
    # Cargar la imagen
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    imagen = plt.imread('datos/captura.png')

    # Cargar las coordenadas desde el archivo 
    coordenadasMov = np.genfromtxt('datos/movimientos.csv', delimiter=',', skip_header=1)

    dpi = 50

    # Crear un gráfico
    plt.figure(figsize=(ANCHO_PANTALLA/dpi, ALTO_PANTALLA/dpi))
    plt.imshow(imagen)

    # Dibujar las líneas sobre la imagen
    try:
        x = coordenadasMov[:, 0]
        y = coordenadasMov[:, 1]
        plt.plot(x, y, linestyle='-', color='red', linewidth=(ANCHO_PANTALLA+ALTO_PANTALLA)*0.001, alpha=0.5)
    except IndexError:
        pass

    coordenadasClick = np.genfromtxt('datos/clicks.csv', delimiter=",", skip_header=1)

    try:
        x = coordenadasClick[:, 0]
        y = coordenadasClick[:, 1]
        plt.scatter(x, y, marker='x', color="blue", s=(ANCHO_PANTALLA+ALTO_PANTALLA)*0.1)
    except IndexError:
        pass

    plt.axis('off')

    plt.savefig(ruta, dpi=dpi, bbox_inches='tight', pad_inches=0)
    #plt.show()

# def generarAnimacion(ruta, muestreo=10, fps=30):
#     # Cargar los datos desde el archivo CSV
#     df = pd.read_csv("datos/movimientos.csv")

#     # Crear una figura y un eje para la animación con la imagen de fondo
#     background = plt.imread("datos/captura.png") # Ajusta los límites según la resolución de tu pantalla

#     bg_width, bg_height, _ = background.shape

#     # Crear la figura y el eje con el tamaño de la imagen de fondo
#     fig, ax = plt.subplots(figsize=(bg_width / 100, bg_height / 100), dpi=100)
#     ax.imshow(background, extent=[0, bg_width, 0, bg_height])
#     line, = ax.plot([], [], lw=2)
#     # Función para inicializar la animación
#     def init():
#         line.set_data([], [])
#         return line,

#     # Función para actualizar la animación en cada cuadro
#     def update(frame):
#         # data = df.iloc[:frame + 1]
#         x = df['x'][:frame+1]
#         y = df['y'][:frame+1]
#         line.set_data(x, y)
#         return line,

#     # Crea la animación
#     cuadros = len(df)
#     duracion = cuadros / fps
#     ani = FuncAnimation(fig, update, frames=cuadros, init_func=init, blit=True)
#     ani.save(ruta, writer='ffmpeg', fps=fps, extra_args=['-vcodec', 'libx264'])

#     # Guarda la animación en un archivo de video (requiere FFmpeg)
#     ani.save(ruta, writer='ffmpeg')


def generarAnimacion(ruta):
    df = pd.read_csv("datos/movimientos.csv")
    px.line(df, x="x", y="y")