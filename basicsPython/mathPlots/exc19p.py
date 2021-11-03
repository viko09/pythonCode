import numpy as np
import matplotlib.pyplot as plt

# import pandas as pd


# If this is the principal script, follow the next process
if __name__ == "__main__":
    def f(t, u):
        return (0.02526*(np.exp(u)))/0.000427*(-1+(np.exp(u)))


    t = np.arange(0, 50, 0.001)
    t1 = np.arange(0, 100, 0.01)
    u = (t + 0.00018)/39.58828
    u1 = (t1 + 0.00018) / 39.58828

    # Plotting Graph
    plt.gca()
    plt.gca().plot(t, f(t, u), color='purple', alpha=0.65, label=r'$P(t) = \frac{0.02526 e^{\frac{t + 0.00018}'
                                                                 r'{39.58828}}}{0.000427\left(-1 + e^{\frac{t + 0.00018}{39.58828}}\right)}$')
    # plt.plot(0, 75, color='r', alpha=0.55, marker='o', label='Condición inicial')
    # plt.plot(3, 118.54757, color='r', alpha=0.55, marker='o')
    plt.title("Gráfica de función de cambio")
    plt.xlabel('Tiempo en horas (t)')
    plt.ylabel('Cantidad de Población')
    # plt.axhline(23, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc19.png")

    plt.show()

    # Plotting Graph
    plt.gca()
    plt.gca().plot(t1, f(t1, u1), color='purple', alpha=0.65,
                   label=r'$P(t) = \frac{0.02526 e^{\frac{t + 0.00018}{39.58828}}}{0.000427\left(-1 + '
                         r'e^{\frac{t + 0.00018}{39.58828}}\right)}$')
    plt.plot(0, 1.25*10**10, color='r', alpha=0.55, marker='o', label='Condición inicial')
    # plt.plot(3.71583, 8000, color='r', alpha=0.55, marker='o')
    plt.plot(3, 7000, color='r', alpha=0.55, marker='o')
    plt.title("Función (Valores Iniciales)")
    plt.xlabel('Tiempo en segundos (t)')
    plt.ylabel('Cantidad de Población')
    # plt.axhline(23, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc19vi.png")

    plt.show()
