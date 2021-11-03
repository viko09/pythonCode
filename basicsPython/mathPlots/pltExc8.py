import numpy as np
import matplotlib.pyplot as plt

# import pandas as pd


# If this is the principal script, follow the next process
if __name__ == "__main__":
    def f(t):
        return ((-0.44284 * t + 10.6373)) ** 2 / 4


    t = np.arange(0, 100, 0.001)
    t1 = np.arange(0, 500, 0.01)

    # Plotting Graph
    plt.gca()
    plt.gca().plot(t, f(t), color='purple', alpha=0.65, label=r'$h(t) = \left(\frac{-0.44284t + 10.63729}{2}\right)^2$')
    # plt.plot(0, 75, color='r', alpha=0.55, marker='o', label='Condición inicial')
    # plt.plot(3, 118.54757, color='r', alpha=0.55, marker='o')
    plt.title("Gráfica de función de cambio")
    plt.xlabel('Tiempo en segundos (t)')
    plt.ylabel('Altura (h)')
    # plt.axhline(23, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc8.png")

    plt.show()

    # Plotting Graph
    plt.gca()
    plt.gca().plot(t1, f(t1), color='purple', alpha=0.65,
                   label=r'$h(t) = \left(\frac{-0.44284t + 10.63729}{2}\right)^2$')
    plt.plot(0, 28.28802, color='r', alpha=0.55, marker='o', label='Condición inicial')
    plt.plot(24.02061, 0.0001, color='r', alpha=0.55, marker='o')
    plt.title("Gráfica de función (Valores Iniciales)")
    plt.xlabel('Tiempo en segundos (t)')
    plt.ylabel('Altura (h)')
    # plt.axhline(23, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc8vi.png")

    plt.show()
