import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd


# If this is the principal script, follow the next process
if __name__ == "__main__":

    # theta goes from 0 to 2pi
    theta = np.linspace(-2*np.pi, 2*np.pi, 1000)

    # compute x1 and x2
    x1 = np.cos(theta)
    x2 = np.sin(theta)

    # create the figure
    plt.plot(theta, x1, color='purple', alpha=0.65, label=r'$r = \cos\theta$')
    plt.plot(theta, x2, color='green', alpha=0.55, label=r'$r = \sin\theta$')
    plt.scatter(np.pi/4, np.sqrt(2)/2, color='orange', label='Intersección')
    plt.title("Simetría del problema")
    plt.xlabel(r'\theta')
    plt.ylabel(r'r')
    plt.axhline(0, 0, color='black')
    plt.axvline(0, 0, color='black')

    plt.xlim(-0.5, 4)
    plt.ylim(-1.5, 1.5)
    plt.gca().set_aspect('equal')
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    # Graph Settings

    plt.legend()
    plt.savefig("/home/vikoluna/Documents/BUAP/6toSemestre/CIVV/unidad2/Tarea4/circunf1.png", dpi=300)
    plt.show()
