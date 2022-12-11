import numpy as np
import matplotlib.pyplot as plt

# import pandas as pd


# If this is the principal script, follow the next process
if __name__ == "__main__":
    # ----tan (x)------------------------------------------------------------------------------------------------------

    def f(y):
        return np.tan(y)


    # compute x1 and x2
    x1 = np.arange(-3 * np.pi / 2, -np.pi / 2, 0.001)
    x2 = np.arange(-np.pi / 2, np.pi / 2, 0.001)
    x3 = np.arange(np.pi / 2 + 0.00001, 3 * np.pi / 2, 0.001)

    # create the figure
    plt.plot(x1, f(x1), color='purple', alpha=0.65)
    plt.plot(x2, f(x2), color='orangered', alpha=0.65)
    plt.plot(x3, f(x3), color='green', alpha=0.65)
    plt.title('Función Tangente: 'r'$y = \tan (x)$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, 0, color='black')
    plt.axvline(0, 0, color='black')

    plt.xlim(-2 * np.pi, 2 * np.pi)
    plt.ylim(-5, 5)
    # plt.gca().set_aspect('equal')
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    # Graph Settings

    unit = np.pi / 2

    x_tick = np.arange(-3 * np.pi / 2, 2 * np.pi, unit)
    x_label = [r"$-\frac{3\pi}{2}$", r"$-\pi$", r"$-\frac{\pi}{2}$", r"$0$", r"$\frac{\pi}{2}$", r"$\pi$",
               r"$\frac{3\pi}{2}$"]
    print(x_tick)
    plt.gca().set_xticks(x_tick)
    plt.gca().set_xticklabels(x_label, fontsize=10)

    plt.savefig("/home/vikoluna/Documents/BUAP/6toSemestre/ComplexV/unidad1/notas/tang1.png")
    plt.show()

    # -----cos (x)--------------------------------------------------------------------------------------------------

    def f(y2):
        return np.cos(y2)


    # compute x1 and x2
    x = np.arange(-3 * np.pi, 3 * np.pi, 0.001)
    xP = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, 4*np.pi/6, 5*np.pi/6, np.pi]

    # create the figure
    plt.plot(x, f(x), color='purple', alpha=0.65)
    plt.plot(xP, f(xP), 'bo', label=r'$0, \pi/6, \pi/4, \pi/3, \pi/2, 4\pi/6, 5\pi/6, \pi$')
    plt.title("Función Coseno: $y = \cos (x)$")
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
               r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$-2\pi$", r"$\frac{5\pi}{2}$"]
    print(x_tick)
    plt.gca().set_xticks(x_tick)
    plt.gca().set_xticklabels(x_label, fontsize=10)
    plt.legend()

    plt.savefig("/home/vikoluna/Documents/BUAP/6toSemestre/ComplexV/unidad1/notas/cos1.png")
    plt.show()

    # -------cos² (x)-----------------------------------------------------------------------------------------------

    def f(y3):
        return np.cos(y3) * np.cos(y3)


    # compute x1 and x2
    x = np.arange(-3 * np.pi, 3 * np.pi, 0.001)

    # create the figure
    plt.plot(x, f(x), color='green', alpha=0.65)
    plt.title("Función: $y = \cos^2 (x)$")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, 0, color='black')
    plt.axvline(0, 0, color='black')

    # Graph Settings
    plt.xlim(-5 * np.pi / 2, 5 * np.pi / 2)
    plt.ylim(-0.5, 1.5)
    # plt.gca().set_aspect('equal')
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    # Graph Settings

    unit = np.pi / 2

    x_tick = np.arange(-5 * np.pi / 2, 3 * np.pi, unit)
    x_label = [r"$-\frac{5\pi}{2}$", r"$-2\pi$", r"$-\frac{3\pi}{2}$", r"$-\pi$", r"$-\frac{\pi}{2}$", r"$0$",
               r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$-2\pi$", r"$\frac{5\pi}{2}$"]
    # print(x_tick)
    plt.gca().set_xticks(x_tick)
    plt.gca().set_xticklabels(x_label, fontsize=10)

    plt.savefig("/home/vikoluna/Documents/BUAP/6toSemestre/ComplexV/unidad1/notas/cos2.png")
    plt.show()


    # ----------2Cos(x)--------------------------------------------------------------------------------------------

    def f(y4):
        return 2 * np.cos(y4)


    # compute x1 and x2
    x = np.arange(-3 * np.pi, 3 * np.pi, 0.001)

    # create the figure
    plt.plot(x, f(x), color='blue', alpha=0.65)
    plt.title("Función: $y = 2\cos (x)$")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, 0, color='black')
    plt.axvline(0, 0, color='black')

    # Graph Settings
    plt.xlim(-5 * np.pi / 2, 5 * np.pi / 2)
    plt.ylim(-3, 3)
    # plt.gca().set_aspect('equal')
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    # Graph Settings

    unit = np.pi / 2

    x_tick = np.arange(-5 * np.pi / 2, 3 * np.pi, unit)
    x_label = [r"$-\frac{5\pi}{2}$", r"$-2\pi$", r"$-\frac{3\pi}{2}$", r"$-\pi$", r"$-\frac{\pi}{2}$", r"$0$",
               r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$-2\pi$", r"$\frac{5\pi}{2}$"]
    # print(x_tick)
    plt.gca().set_xticks(x_tick)
    plt.gca().set_xticklabels(x_label, fontsize=10)

    plt.savefig("/home/vikoluna/Documents/BUAP/6toSemestre/ComplexV/unidad1/notas/dosCos.png")
    plt.show()

    # ----------Sen (x)--------------------------------------------------------------------------------------------

    def f(y5):
        return np.sin(y5)


    # create the figure
    plt.plot(x, f(x), color='gold', alpha=0.95)
    plt.title("Función Seno: $y = \sin (x)$")
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
               r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$-2\pi$", r"$\frac{5\pi}{2}$"]
    # print(x_tick)
    plt.gca().set_xticks(x_tick)
    plt.gca().set_xticklabels(x_label, fontsize=10)

    plt.savefig("/home/vikoluna/Documents/BUAP/6toSemestre/ComplexV/unidad1/notas/sino.png")
    plt.show()

# ----------Cos (x + pi)--------------------------------------------------------------------------------------------

    def f(y6):
        return np.cos(y6 + np.pi)


    # create the figure
    plt.plot(x, f(x), color='purple', alpha=0.65)
    plt.title("Función Cos: $y = \cos (x + \pi)$")
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
               r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$-2\pi$", r"$\frac{5\pi}{2}$"]
    # print(x_tick)
    plt.gca().set_xticks(x_tick)
    plt.gca().set_xticklabels(x_label, fontsize=10)

    plt.savefig("/home/vikoluna/Documents/BUAP/6toSemestre/ComplexV/unidad1/notas/cosxmaspi.png")
    plt.show()

    # ----------Cos (x + pi/2)-----------------------------------------------------------------------------------------

    def f(y7):
        return np.cos(y7 + (np.pi / 2))


    # create the figure
    plt.plot(x, f(x), color='red', alpha=0.55)
    plt.title('Función Tangente: 'r'$y = \cos (x + \pi/2)$')
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
               r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$-2\pi$", r"$\frac{5\pi}{2}$"]
    # print(x_tick)
    plt.gca().set_xticks(x_tick)
    plt.gca().set_xticklabels(x_label, fontsize=10)

    plt.savefig("/home/vikoluna/Documents/BUAP/6toSemestre/ComplexV/unidad1/notas/cosxpi2.png")
    plt.show()

    # ----------Cos (x - pi)-----------------------------------------------------------------------------------------

    def f(y8):
        return np.cos(y8 - (np.pi / 2))


    # create the figure
    plt.plot(x, f(x), color='orchid', alpha=0.75)
    plt.title('Función Tangente: 'r'$y = \cos (x - \pi/2)$')
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
               r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$-2\pi$", r"$\frac{5\pi}{2}$"]
    # print(x_tick)
    plt.gca().set_xticks(x_tick)
    plt.gca().set_xticklabels(x_label, fontsize=10)

    plt.savefig("/home/vikoluna/Documents/BUAP/6toSemestre/ComplexV/unidad1/notas/cosmenospi2.png")
    plt.show()
