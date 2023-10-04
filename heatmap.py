import seaborn as sns
import matplotlib.pyplot as plt

# Tamaño de la pantalla (ajusta esto a tu pantalla)
screen_width = 1920
screen_height = 1080


# Crear un DataFrame de pandas con los datos
import pandas as pd
df = pd.read_csv("datos/registro.csv")


# Crear una matriz de densidad con la función kdeplot de Seaborn
plt.figure(figsize=(screen_width / 100, screen_height / 100))  # Ajusta el tamaño de la figura
ax = sns.kdeplot(data=df, x='x', y='y', fill=True, cmap='viridis', levels=50, cbar=True, bw_adjust=0.8)

# Invertir el eje Y
ax.invert_yaxis()
plt.xlim(0, screen_width)
plt.ylim(0, screen_height)

plt.title('Mapa de Densidad del Mouse')
plt.show()
