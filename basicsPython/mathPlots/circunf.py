import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd


# If this is the principal script, follow the next process
if __name__ == "__main__":

    # theta goes from 0 to 2pi
    theta = np.linspace(0, 2*np.pi, 1000)

    # the radius of the circle
    r = 1

    # compute x1 and x2
    x1 = r * np.cos(theta)
    x2 = r * np.sin(theta)

    # create the figure
    plt.plot(x1, x2, color='purple', alpha=0.65, label=r'$x^2 + y^2 = 1$')
    plt.title("Circunferencia unitaria")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, 0, color='black')
    plt.axvline(0, 0, color='black')

    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.gca().set_aspect('equal')
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    # Graph Settings

    plt.legend()
    plt.savefig("/home/vikoluna/Documents/BUAP/6toSemestre/ComplexV/unidad1/notas/circunf1.png")
    plt.show()
