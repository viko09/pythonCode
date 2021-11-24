import pandas as pd
import matplotlib.pyplot as plt

# Here we import our csv data
data = pd.read_csv('muestra1.csv')
print(data)
print("-"*32)

# We assign variables
x = data['Distance_(pixels)']
print(x)
print("-"*32)
y = data['Gray_Value']
print(y)
print("-"*32)

# Here we plot the graph
plt.plot(x, y, 'purple', alpha=0.65, label='Datos experimentales')

# Graph's Data
plt.title("Análisis de la Figura")
plt.xlabel("Distancia (Pixeles)")
plt.ylabel("Cantidad de luz")

# Graph Settings
plt.grid(color='g', linestyle='dotted', linewidth=1)
plt.legend()

# Save as png
plt.savefig("muestra1.png")

# Show
plt.show()
