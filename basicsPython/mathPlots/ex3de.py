import numpy as np
import matplotlib.pyplot as plt

# If this is the principal script, follow the next process
if __name__ == "__main__":
    def f(x):
        return np.exp(x)


    x1 = np.arange(-5, 5, 0.001)

    # Plotting Graph
    plt.gca()
    plt.gca().plot(x1, f(x1), color='red', alpha=0.65, label=r'$y_p = e^x$')
    plt.title("Solución Particular de la Ecuación Diferencial")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, 0, color='black')
    plt.axvline(0, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    plt.xlim(-4, 4)
    plt.ylim(-2, 10)

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/Tarea7/graf/exc7.png", dpi=300)

    plt.show()
