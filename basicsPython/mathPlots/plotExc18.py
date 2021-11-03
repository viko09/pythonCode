import numpy as np
import matplotlib.pyplot as plt

# import pandas as pd


# If this is the principal script, follow the next process
if __name__ == "__main__":
    def f(t):
        return 4000*np.exp(t*((np.log(7/4))/3))


    t = np.arange(0, 48, 0.001)
    t1 = np.arange(0, 6, 0.01)

    # Plotting Graph
    plt.gca()
    plt.gca().plot(t, f(t), color='purple', alpha=0.65, label=r'$P(t) = 4000e^{(0.18653)t}$')
    # plt.plot(0, 75, color='r', alpha=0.55, marker='o', label='Condición inicial')
    # plt.plot(3, 118.54757, color='r', alpha=0.55, marker='o')
    plt.title("Gráfica de función de cambio")
    plt.xlabel('Tiempo en horas (t)')
    plt.ylabel('Cantidad de Bacterias')
    # plt.axhline(23, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc18.png")

    plt.show()

    # Plotting Graph
    plt.gca()
    plt.gca().plot(t1, f(t1), color='purple', alpha=0.65,
                   label=r'$P(t) = 4000e^{(0.18653)t}$')
    plt.plot(0, 4000, color='r', alpha=0.55, marker='o', label='Condición inicial')
    plt.plot(3.71583, 8000, color='r', alpha=0.55, marker='o')
    plt.plot(3, 7000, color='r', alpha=0.55, marker='o')
    plt.title("Función (Valores Iniciales)")
    plt.xlabel('Tiempo en segundos (t)')
    plt.ylabel('Cantidad de bactérias')
    # plt.axhline(23, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc18vi.png")

    plt.show()
