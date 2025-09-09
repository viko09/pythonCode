import numpy as np
from scipy.optimize import minimize

# Función objetivo de prueba (puedes reemplazarla por cualquier función que desees optimizar)
def objective_function(x):
    return x[0]**2 + x[1]**2  # Función de minimización simple (suma de cuadrados)

# Generar datos aleatorios para las variables de decisión
num_variables = 2
num_data_points = 100
data = np.random.uniform(-10, 10, (num_data_points, num_variables))

# Probar el optimizador con diferentes puntos iniciales
for i in range(num_data_points):
    initial_guess = data[i]  # Punto inicial aleatorio
    result = minimize(objective_function, initial_guess, method='Nelder-Mead')
    print(f'Punto inicial: {initial_guess}, Resultado de optimización: {result.x}, Valor de la función objetivo: {result.fun}')
