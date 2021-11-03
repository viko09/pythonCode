import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# If this is the principal script, follow the next process
if __name__ == "__main__":


    def f(t, k, c):
        return c*(np.exp(k*t)) + 23


    c = 257
    k = (np.log(233/257))/2
    t = np.arange(0, 150, 0.001)
    t1 = np.arange(90, 140, 0.01)
    print(f(t1, k, c))
    datosY = pd.array(f(t1, k, c))
    datosX = pd.array(t1)
    print(datosX, datosY)
# Plotting Graph
    plt.gca()
    plt.gca().plot(t, f(t, k, c), color='purple', alpha=0.65, label=r'$T(t) = Ce^{2k} + 23$')
    plt.plot(0, 280, color='r', alpha=0.55, marker='o')
    plt.plot(2, 256, color='r', alpha=0.55, marker='o')
    plt.title("Gráfica de datos y función de cambio")
    plt.xlabel('Tiempo en minutos (t)')
    plt.ylabel('Temperatura en Celcius (C°)')
    plt.axhline(23, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc1.png")

    plt.show()

    plt.plot(t, f(t, k, c), color='purple', alpha=0.65, label='Acercamiento de la gráfica')
    plt.xlabel('Tiempo en minutos (t)')
    plt.ylabel('Temperatura en Celcius (C°)')
    plt.axhline(23, 0, color='black')

    plt.xlim(110, 150)
    plt.ylim(20, 28)
    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc1zoom.png")
    plt.show()
