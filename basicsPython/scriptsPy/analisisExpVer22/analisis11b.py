import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# Function
def fun(x, a, b, c):
    return a*x**2 + b*x + c


# Data
xData = np.array([20, 40, 60, 80, 100])
yData = np.array([1.362, 1.427, 1.480, 1.516, 1.528])

# Plot data
# plt.plot(xData, yData, 'bo', label='Datos')
plt.plot(xData, yData, color='b', alpha=0.55, marker='o', label='Datos')

# Curve
popt, pcov = curve_fit(fun, xData, yData)
print(popt)

# Values for the fitted fun
xFit = np.arange(20.0, 99.9999, 0.01)

plt.plot(xFit, fun(xFit, *popt), 'red', label=r'Ajuste: -2.196x10⁻⁵ x² + 4.741x10⁻³ x + 1.274')
plt.title('Frecuencia vs Voltaje')
plt.xlabel(r'Frecuencia de la luz incidente $\upsilon$')
plt.ylabel(r'Voltaje en el ánado del fototubo $V$')
plt.grid()
plt.legend()
plt.show()
