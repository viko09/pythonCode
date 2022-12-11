import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd


# If this is the principal script, follow the next process
if __name__ == "__main__":

    def f(t):
        return 1 -(0.000061 * t) + 0.000007733 * (t ** 2)


    t = np.arange(0, 10, 0.001)
    Ydata = np.array(f(t))
    print(len(Ydata))
    print(Ydata)
    abs_max = np.amax(np.abs(Ydata))
    normalized_array = f(t) * (len(Ydata)/abs_max)
    print(abs_max)

# Plotting Graph
    plt.gca()
    plt.gca().plot(t, normalized_array, color='orangered', alpha=0.75, label=r'$V(\theta) = 1 - 0.000061 \cdot \theta + 0.000007733 '
                                                              r'\cdot \theta^2$')
    plt.title("Gráfica de V vs θ")
    plt.xlabel('Volumen (V)')
    plt.ylabel('Variación (θ)')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/6toSemestre/Termo/Unidad1/tarea2/exc5.png")

    plt.show()
