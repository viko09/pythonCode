import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd


# If this is the principal script, follow the next process
if __name__ == "__main__":


    def f(t, c, u):
        return -(np.exp(-u)) + 3000


    c = -200*np.log(2925)
    t = np.arange(0, 150, 0.001)
    t1 = np.arange(0, 2000, 0.01)
    t2 = np.arange(0, 5, 0.01)
    u = (t+c)/200
    u1 = (t1+c)/200
    u2 = (t2+c) / 200
    print(c)

# Plotting Graph
    plt.gca()
    plt.gca().plot(t, f(t, c, u), color='purple', alpha=0.65, label=r'$S(t) = -e^{-\frac{t -200\ln(2925)}{200}} + '
                                                                    r'3000$')
    plt.plot(0, 75, color='r', alpha=0.55, marker='o', label='Condición inicial')
    plt.plot(3, 118.54757, color='r', alpha=0.55, marker='o')
    plt.title("Gráfica de función de cambio")
    plt.xlabel('Tiempo en minutos (t)')
    plt.ylabel('Cantidad de sal (gr)')
    # plt.axhline(23, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc6.png")

    plt.show()

    # Plotting Graph
    plt.gca()
    plt.gca().plot(t2, f(t2, c, u2), color='purple', alpha=0.65,
                   label=r'$S(t) = -e^{-\frac{t -200\ln(2925)}{200}} + 3000$')
    plt.plot(0, 75, color='r', alpha=0.55, marker='o', label='Condición inicial')
    plt.plot(3, 118.54757, color='r', alpha=0.55, marker='o')
    plt.title("Gráfica de función (Valores Iniciales)")
    plt.xlabel('Tiempo en minutos (t)')
    plt.ylabel('Cantidad de sal (gr)')
    # plt.axhline(23, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc6vi.png")

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
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/TareaExamen/graf/exc6zout.png")
    plt.show()
