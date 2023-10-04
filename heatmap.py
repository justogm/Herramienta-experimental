import seaborn as sns
import matplotlib.pyplot as plt
from constantes import *

# Crear un DataFrame de pandas con los datos
import pandas as pd
df = pd.read_csv("datos/registro.csv")

df['y'] = ALTO_PANTALLA - df['y']

# Crear una matriz de densidad con la función kdeplot de Seaborn
plt.figure(figsize=(ANCHO_PANTALLA / 100, ALTO_PANTALLA / 100))  # Ajusta el tamaño de la figura
ax = sns.kdeplot(data=df, x='x', y='y', fill=True, cmap='viridis', levels=50, cbar=True, bw_adjust=0.8)


plt.xlim(0, ANCHO_PANTALLA)
plt.ylim(0, ALTO_PANTALLA)

plt.title('Mapa de Densidad del Mouse')
plt.show()
