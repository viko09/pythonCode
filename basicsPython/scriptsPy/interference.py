import pandas as pd
import matplotlib.pyplot as plt

# Code for the analysis of images produced by lens
# By. Victor Manuel Luna Mendoza

# ------------------------------------------
# Here we import our csv data
data = pd.read_csv('Values.csv')
print(data)
# ------------------------------------------
# We assign variables
x = data['Distance_(pixels)']
print(x)

print("-"*45)

y = data['Gray_Value']
print(y)

print("-"*45)
# ------------------------------------------

# Here we plot the graph
plt.plot(x, y, 'orange', alpha=0.75, label='Análisis de Imagen')

# Graph's Data
plt.title('Gráfica (Distancia (Pixeles) vs Escala de color)')
plt.xlabel("X")
plt.ylabel("Y")

# Graph Settings
plt.grid(color='g', linestyle='dotted', linewidth=1)
plt.legend()

# Save as png
# plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/FEXPIII/practica6/datos1.png")

# Show.
plt.show()
