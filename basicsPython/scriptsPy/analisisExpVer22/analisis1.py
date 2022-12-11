import numpy as np
import matplotlib.pyplot as plt

# import pandas as pd


# If this is the principal script, follow the next process
if __name__ == "__main__":
    def f(a, b, c, x):
        return a*x**2 + b*x + c

    x = np.arange(20, 120, 20)
    y = [1.362, 1.427, 1.480, 1.516, 1.528]

    # Plotting Graph
    plt.gca()
    plt.plot(x, y, color='b', alpha=0.55, marker='o', label='Datos')
    plt.plot(x, f(x), color='g', alpha=0.55, label='Ajuste')
    plt.title("Frecuencia vs Voltaje")
    plt.xlabel('Frecuencia de la luz incidente')
    plt.ylabel('Voltaje')
    # plt.axhline(23, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    # plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc19vi.png")

    plt.show()
