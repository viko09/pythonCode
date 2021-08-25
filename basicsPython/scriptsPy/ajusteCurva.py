import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


# Fitting function
def func(x, a, b):
    return a * np.exp(b * x)
    # return a*x+b


# Experimental x and y data points
xData = np.array([6, 15, 25, 32, 37, 41, 45])
yData = np.array([25, 27, 30, 33, 37, 41, 45])

# Plot experimental data points
plt.plot(xData, yData, 'bo', label='experimental-data')

# Initial guess for the parameters
initialGuess = [1.0, 1.0]

# Perform the curve-fit
popt, pcov = curve_fit(func, xData, yData, initialGuess)
print(popt)

# x values for the fitted function
xFit = np.arange(0.0, 45.0, 0.01)

# Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='fit params: a=%5.3f, b=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
