import numpy as np
import matplotlib.pyplot as plt

# If this is the principal script, follow the next process
if __name__ == "__main__":


    def f(x):
        return ((1/8)*(np.exp(7*x))) - ((1/8)*(np.exp(-x)))


    def g(x):
        return ((7/8)*(np.exp(7*x))) + ((1/8)*(np.exp(-x)))


    x1 = np.arange(-5, 0.999, 0.001)

    # Plotting Graph
    plt.gca()
    plt.gca().plot(x1, f(x1), color='purple', alpha=0.65, label=r'$y_p = \frac{1}{8} e^{7x} - \frac{1}{8}e^{-x}$')
    plt.gca().plot(x1, g(x1), color='red', alpha=0.45, label=r'$y{´}_p = \frac{7}{8} e^{7x} + \frac{1}{8}e^{-x}$')
    plt.title("Solución Particular")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, 0, color='black')
    plt.axvline(0, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    plt.xlim(-5, 1)
    plt.ylim(-5, 5)

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/Tarea7/graf/exc1.png", dpi=150)

    plt.show()
