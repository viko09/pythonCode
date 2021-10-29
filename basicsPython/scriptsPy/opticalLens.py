import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Here we import our csv data
data = pd.read_csv('measures20.csv')
print(data)
# Focal distance: 7.872

print("---------------------------------------------------------------")
# We assign variables
x = data['Objeto (s)']
print(x)
print("---------------------------------------------------------------")
y = data['Imagen (s’)']
print(y)

print("---------------------------------------------------------------")

x_fit = pd.array(x)
print(x_fit)

y_fit = pd.array(y)
print(y_fit)

print("---------------------------------------------------------------")

# Cambio de variable
x_test = 1/x_fit
print(x_test)
x_cv = pd.DataFrame(x_test)
print(x_cv)

y_test = 1/y_fit
print(y_test)
y_cv = pd.DataFrame(y_test)
print(y_cv)

print("---------------------------------------------------------------")
# New Dataset
newData = pd.concat([x_cv, y_cv], axis=1, keys=["X = 1/s", "Y = 1/s'"])
print(newData)
compression_opts = dict(method='zip', archive_name='out.csv')
newData.to_csv('out.zip', compression=compression_opts)

print("---------------------------------------------------------------")
# Values for the fitted fun
xFit = np.arange(8.577, 21.393, 0.01)

# Here we plot the graph
# plt.plot(x, y, 'bo', alpha=0.65, label='Datos')
plt.plot(x, y, 'or', alpha=0.55, label='Datos experimentales')
# plt.plot(xFit, fun(xFit, *popt), 'orangered', label='Ajuste')
plt.axhline(0, color='black')
plt.axvline(0, color='black')

# Limits of axes
plt.xlim(8, 22)
plt.ylim(9, 100)

# Graph's Data
plt.title("Gráfica de lente positiva (Objeto vs Imagen)")
plt.xlabel("Objeto (s)")
plt.ylabel("Imagen (s')")

# Graph Settings
plt.grid(color='g', linestyle='dotted', linewidth=1)
plt.legend()

# Save as png
plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/FEXPIII/practica4/datoslentes.png")

# Show.
plt.show()

plt.plot(x_test, y_test, 'bo', alpha=0.55, label='Datos nueva variable')

# Graph's Data
plt.title("Gráfica de datos con cambio de variable")
plt.xlabel("Objeto (1/s)")
plt.ylabel("Imagen (1/s')")

# Graph Settings
plt.grid(color='g', linestyle='dotted', linewidth=1)
plt.legend()

# Save as png
plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/FEXPIII/practica4/datoscam.png")

plt.show()
