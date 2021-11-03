import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# If this is the principal script, follow the next process
if __name__ == "__main__":


    def f(t, k, c):
        return c*(np.exp(k*t)) + 127.8


    c = -105.8
    k = (np.log((45-127.8)/-105.8))/30
    t = np.arange(0, 110, 0.001)
    t1 = np.arange(0, 600, 0.0001)
    print(f(t1, k, c))
    datosY = pd.array(f(t1, k, c))
    datosX = pd.array(t1)
    print(datosX, datosY)
# Plotting Graph
    plt.gca()
    plt.gca().plot(t, f(t, k, c), color='purple', alpha=0.65, label=r'$T(t) = -105.8e^{-0.008170749\cdot t} + 127.8$')
    plt.plot(0, 22, color='r', alpha=0.55, marker='o')
    plt.plot(97.24015, 80, color='r', alpha=0.55, marker='o')
    plt.plot(30, 45, color='r', alpha=0.55, marker='o')
    plt.plot(60, 63, color='r', alpha=0.55, marker='o')
    plt.title("Gráfica de datos y función")
    plt.xlabel('Tiempo en segundo (t)')
    plt.ylabel('Temperatura en Celcius (C°)')
    # plt.axhline(23, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc2.png")

    plt.show()

    # Plotting 2nd Graph
    plt.gca()
    plt.gca().plot(t1, f(t1, k, c), color='purple', alpha=0.65, label=r'$T(t) = -105.8e^{-0.008170749\cdot t} + 127.8$')
    plt.plot(0, 22, color='r', alpha=0.55, marker='o')
    plt.plot(97.24015, 80, color='r', alpha=0.55, marker='o')
    plt.plot(30, 45, color='r', alpha=0.55, marker='o')
    plt.plot(60, 63, color='r', alpha=0.55, marker='o')
    plt.title("Gráfica después de 10 minutos")
    plt.xlabel('Tiempo en segundo (t)')
    plt.ylabel('Temperatura en Celcius (C°)')
    # plt.axhline(23, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc2zout.png")

    plt.show()
