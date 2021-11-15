import numpy as np
import matplotlib.pyplot as plt

# If this is the principal script, follow the next process
if __name__ == "__main__":


    def f(x):
        return ((1/3)*(np.exp(x))) + ((1/3)*(np.exp(-2*x)))


    def g(x):
        return ((1/3)*(np.exp(x))) - ((2/3)*(np.exp(-2*x)))


    def h(x):
        return ((1/3)*(np.exp(x))) + ((4/3)*(np.exp(-2*x)))


    x1 = np.arange(-3, 3, 0.001)

    # Plotting Graph
    plt.gca()
    plt.gca().plot(x1, f(x1), color='purple', alpha=0.65, label=r'$y_p = \frac{1}{3}e^x + \frac{1}{3}e^{-2x}$')
    plt.gca().plot(x1, g(x1), color='red', alpha=0.45, label=r'$y{´}_p = \frac{1}{3}e^x - \frac{2}{3}e^{-2x}$')
    plt.gca().plot(x1, h(x1), color='green', alpha=0.45, label=r'$y{´´}_p = \frac{1}{3}e^x + \frac{4}{3}e^{-2x}$')
    plt.title("Solución Particular")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, 0, color='black')
    plt.axvline(0, 0, color='black')

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    plt.xlim(-2.5, 2.5)
    plt.ylim(-4, 7)

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/DE/Tareas/Tarea7/graf/exc3.png", dpi=300)

    plt.show()
