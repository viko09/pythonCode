import numpy as np

# Generar datos aleatorios
num_Var = int(input("Ingrese el número de variables de la función: \n"))
num_Points = int(input("Ingrese el número de puntos a generar: \n"))


class random_dats:
    def random_point(self):
        datos = np.random.uniform(-10, 10, (num_Points, num_Var))
        return print(datos)

    # Probar el optimizador con diferentes puntos iniciales
    for i in range(num_Points):
        initial_guess =   # Punto inicial aleatorio
        result = minimize(objective_function, initial_guess, method='Nelder-Mead')
        print(
            f'Punto inicial: {initial_guess}, Resultado de optimización: {result.x}, '
            f'Valor de la función objetivo: {result.fun}')