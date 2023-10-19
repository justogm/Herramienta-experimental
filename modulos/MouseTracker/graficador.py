import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import os
import plotly.express as px

class Graficador:
    def __init__(self, ancho, alto):
        self.ANCHO = ancho
        self.ALTO = alto
    

    def generarImagenes(self,ruta):
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
        plt.figure(figsize=(self.ANCHO/dpi, self.ALTO/dpi))
        plt.imshow(imagen)

        # Dibujar las líneas sobre la imagen
        try:
            x = coordenadasMov[:, 0]
            y = coordenadasMov[:, 1]
            plt.plot(x, y, linestyle='-', color='red', linewidth=(self.ANCHO+self.ALTO)*0.001, alpha=0.5)
        except IndexError:
            pass

        coordenadasClick = np.genfromtxt('datos/clicks.csv', delimiter=",", skip_header=1)

        try:
            x = coordenadasClick[:, 0]
            y = coordenadasClick[:, 1]
            plt.scatter(x, y, marker='x', color="blue", s=(self.ANCHO+self.ALTO)*0.1)
        except IndexError:
            pass

        plt.axis('off')

        plt.savefig(ruta, dpi=dpi, bbox_inches='tight', pad_inches=0)
        #plt.show()

    def generarAnimacion(self, ruta):
        '''generarAnimacion Genera animación de movimientos
        del mouse.

        A partir del registro de movimientos del mouse
        realiza una animación de el recorrido y la guarda
        como GIF.

        Args:
            ruta (str): Ruta donde se guardará.
        '''

        df = pd.read_csv("datos/movimientos.csv")
        df['y'] = self.ALTO - df['y']
        fondo = plt.imread("datos/captura.png")

        fig, ax = plt.subplots()

        height, width, _ = fondo.shape

        ax.imshow(fondo, extent=[0, width, 0, height])
        line, = ax.plot([], [], lw=2)

        # Función para inicializar el gráfico
        def init():
            line.set_data([], [])
            return line,

        # Función para actualizar el gráfico en cada cuadro de la animación
        def animate(i):
            x = df['x'][:i+1]
            y = df['y'][:i+1]
            line.set_data(x, y)
            return line,

        # Crea la animación
        ani = FuncAnimation(fig, animate, init_func=init, frames=len(df), blit=True, interval=50)
        ax.axis('off')
        plt.xlim(0, 1920)
        plt.ylim(0, 1080)
        # Muestra la animación
        ani.save(ruta, writer='pillow')
