import pandas as pd
import matplotlib.pyplot as plt

# Code for the analysis of images produced by lens
# By. Victor Manuel Luna Mendoza

# ------------------------------------------
# Here we import our csv data
data = pd.read_csv('measures.csv')
print(data)
# ------------------------------------------
# We assign variables
x = data['ol']
print(x)

print("-"*45)

y = data['li']
print(y)

print("-"*45)
# ------------------------------------------
# We assign new variables
xArray = pd.array(x)
print(xArray)

yArray = pd.array(y)
print(yArray)

print("-"*45)

# Cambio de variable
xNew = 1/xArray
x_cv = pd.DataFrame(xNew)
print(x_cv)

yNew = 1/yArray
y_cv = pd.DataFrame(yNew)
print(y_cv)

# New Dataset
newData = pd.concat([x_cv, y_cv], axis=1, keys=["X = 1/s", "Y = 1/s'"])
print(newData)

# If we want to save our new dataset:
# compression_opts = dict(method='zip', archive_name='out.csv')
# newData.to_csv('out.zip', compression=compression_opts)

# ------------------------------------------
# Here we plot the graph
plt.plot(x, y, 'or', alpha=0.65, label='Datos experimentales')

# Graph's Data
plt.title('Gráfica (Objeto vs Imagen)')
plt.xlabel("Objeto (s)")
plt.ylabel("Imagen (s´)")

# Graph Settings
plt.grid(color='g', linestyle='dotted', linewidth=1)
plt.legend()

# Save as png
plt.savefig("datos1.png")

# Show.
plt.show()
# ------------------------------------------
# Here we plot the new graph
plt.plot(xNew, yNew, 'og', alpha=0.65, label='Datos con cambio de variable')

# Graph's Data
plt.title("Gráfica (1/Objeto vs 1/Imagen)")
plt.xlabel("Objeto (1/s)")
plt.ylabel("Imagen (1/s´)")

# Graph Settings
plt.grid(color='g', linestyle='dotted', linewidth=1)
plt.legend()

# Save as png
plt.savefig("datos2.png")

# Show.
plt.show()
