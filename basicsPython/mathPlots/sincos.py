import numpy as np
import matplotlib.pyplot as plt

# import pandas as pd


# If this is the principal script, follow the next process
if __name__ == "__main__":

    # ----------Sen (x)--------------------------------------------------------------------------------------------

    def f(y1):
        return np.sin(y1)

    # compute x1 and x2
    x = np.arange(-3 * np.pi, 3 * np.pi, 0.001)

    # create the figure
    plt.plot(x, f(x), color='orangered', alpha=0.95)
    plt.title(r'Función Seno: $y = \sin (x)$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, 0, color='black')
    plt.axvline(0, 0, color='black')

    # Graph Settings
    plt.xlim(-5 * np.pi / 2, 5 * np.pi / 2)
    plt.ylim(-1.5, 1.5)
    # plt.gca().set_aspect('equal')
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    # Graph Settings

    unit = np.pi / 2

    x_tick = np.arange(-5 * np.pi / 2, 3 * np.pi, unit)
    x_label = [r"$-\frac{5\pi}{2}$", r"$-2\pi$", r"$-\frac{3\pi}{2}$", r"$-\pi$", r"$-\frac{\pi}{2}$", r"$0$",
               r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$", r"$\frac{5\pi}{2}$"]
    # print(x_tick)
    plt.gca().set_xticks(x_tick)
    plt.gca().set_xticklabels(x_label, fontsize=10)

    plt.savefig("/home/vikoluna/Documents/BUAP/6toSemestre/CIVV/unidad2/participación5/sinx1.png")
    plt.show()

    # -----cos (x)--------------------------------------------------------------------------------------------------

    def f(y2):
        return np.cos(y2)


    # compute x1 and x2
    x = np.arange(-3 * np.pi, 3 * np.pi, 0.001)
    xP = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, 4*np.pi/6, 5*np.pi/6, np.pi]

    # create the figure
    plt.plot(x, f(x), color='purple', alpha=0.65)
    # plt.plot(xP, f(xP), 'bo', label=r'$0, \pi/6, \pi/4, \pi/3, \pi/2, 4\pi/6, 5\pi/6, \pi$')
    plt.title(r'Función Coseno: $y = \cos (x)$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, 0, color='black')
    plt.axvline(0, 0, color='black')

    # Graph Settings
    plt.xlim(-5 * np.pi / 2, 5 * np.pi / 2)
    plt.ylim(-1.5, 1.5)
    # plt.gca().set_aspect('equal')
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    # Graph Settings

    unit = np.pi / 2

    x_tick = np.arange(-5 * np.pi / 2, 3 * np.pi, unit)
    x_label = [r"$-\frac{5\pi}{2}$", r"$-2\pi$", r"$-\frac{3\pi}{2}$", r"$-\pi$", r"$-\frac{\pi}{2}$", r"$0$",
               r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$", r"$\frac{5\pi}{2}$"]
    print(x_tick)
    plt.gca().set_xticks(x_tick)
    plt.gca().set_xticklabels(x_label, fontsize=10)
    plt.savefig("/home/vikoluna/Documents/BUAP/6toSemestre/CIVV/unidad2/participación5/cosx1.png")
    plt.show()
