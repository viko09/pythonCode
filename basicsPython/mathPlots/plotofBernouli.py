import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd


# If this is the principal script, follow the next process
if __name__ == "__main__":


    def f(t, c, u):
        return -(np.exp(u) / 2) + 150


    c = -(75 * np.log(240)) / 2
    t = np.arange(0, 150, 0.001)
    t1 = np.arange(0, 600, 0.01)
    u = -(2 * (t + c)) / 75
    u1 = -(2 * (t1 + c)) / 75
    print(c)

# Plotting Graph
    plt.gca()
    plt.gca().plot(t, f(t, c, u), color='purple', alpha=0.65, label=r'$S(t) = -\frac{e^{-\frac{2(t - 205.52)}{75}}}{2} + 150$')
    plt.plot(0, 30, color='r', alpha=0.55, marker='o', label='Condición inicial')
    plt.title("Gráfica de función de cambio")
    plt.xlabel('Tiempo en minutos (t)')
    plt.ylabel('Cantidad de sal (gr)')
    # plt.axhline(23, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc4.png")

    plt.show()

    plt.plot(t1, f(t1, c, u1), color='purple', alpha=0.65)
    plt.title("Gráfica de cantidad de sal después de mucho tiempo")
    plt.xlabel('Tiempo en minutos (t)')
    plt.ylabel('Cantidad de sal (gr)')
    # plt.axhline(23, 0, color='black')

    # plt.xlim(110, 150)
    # plt.ylim(20, 28)

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    # plt.legend()
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc4zout.png")
    plt.show()
