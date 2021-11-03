import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# If this is the principal script, follow the next process
if __name__ == "__main__":


    def f(t, k, c):
        return c*(np.exp(k*t)) + 18


    c = 382
    k = (np.log(338/382))/2
    t = np.arange(0, 110, 0.001)
    t1 = np.arange(0, 600, 0.0001)
    print(f(t1, k, c))
    datosY = pd.array(f(t1, k, c))
    datosX = pd.array(t1)
    print(datosX, datosY)
# Plotting Graph
    plt.gca()
    plt.gca().plot(t, f(t, k, c), color='purple', alpha=0.65, label=r'$T(t) = 382e^{(-0.06118735)t} + 18$')
    plt.plot(2, 356, color='r', alpha=0.55, marker='o')
    plt.plot(0, 400, color='r', alpha=0.55, marker='o')
    # plt.plot(30, 45, color='r', alpha=0.55, marker='o')
    # plt.plot(60, 63, color='r', alpha=0.55, marker='o')
    plt.title("Gráfica de datos y función")
    plt.xlabel('Tiempo en minutos (t)')
    plt.ylabel('Temperatura en Celcius (C°)')
    # plt.axhline(23, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc3.png")

    plt.show()

    # Plotting 2nd Graph
    plt.gca()
    plt.gca().plot(t1, f(t1, k, c), color='purple', alpha=0.65, label=r'$T(t) = 382e^{(-0.06118735)t} + 18$')
    plt.plot(0, 400, color='r', alpha=0.55, marker='o')
    plt.plot(2, 356, color='r', alpha=0.55, marker='o')
    # plt.plot(60, 63, color='r', alpha=0.55, marker='o')
    plt.title("Gráfica acercada")
    plt.xlabel('Tiempo en minutos (t)')
    plt.ylabel('Temperatura en Celcius (C°)')
    plt.axhline(18, 0, color='black')

    plt.xlim(100, 130)
    plt.ylim(12, 22)

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc3zout.png")

    plt.show()
