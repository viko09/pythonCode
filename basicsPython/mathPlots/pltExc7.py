import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd


# If this is the principal script, follow the next process
if __name__ == "__main__":


    def f(t, c, u):
        return np.exp(u)


    c = -(75*np.log(150))/2
    t = np.arange(0, 150, 0.001)
    t1 = np.arange(0, 500, 0.01)
    u = -(2*(t+c))/75
    u1 = -(2*(t1+c))/75

    print(c)

# Plotting Graph
    plt.gca()
    plt.gca().plot(t, f(t, c, u), color='purple', alpha=0.65, label=r'$S(t) = e^{\frac{-2(t -187.8988)}{75}}$')
    # plt.plot(0, 75, color='r', alpha=0.55, marker='o', label='Condición inicial')
    # plt.plot(3, 118.54757, color='r', alpha=0.55, marker='o')
    plt.title("Gráfica de función de cambio")
    plt.xlabel('Tiempo en minutos (t)')
    plt.ylabel('Cantidad de sal (gr)')
    # plt.axhline(23, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc7.png")

    plt.show()

    # Plotting Graph
    plt.gca()
    plt.gca().plot(t1, f(t1, c, u1), color='purple', alpha=0.65,
                   label=r'$S(t) = e^{\frac{-2(t -187.8988)}{75}}$')
    plt.plot(0, 150, color='r', alpha=0.55, marker='o', label='Condición inicial')
    plt.plot(360.59268, 0.01, color='r', alpha=0.55, marker='o')
    plt.title("Gráfica de función (Valores Iniciales)")
    plt.xlabel('Tiempo en minutos (t)')
    plt.ylabel('Cantidad de sal (gr)')
    # plt.axhline(23, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc7vi.png")

    plt.show()
