import numpy as np
import matplotlib.pyplot as plt

# Principal script, follow the next process
if __name__ == "__main__":
    # Funcion T(t) = c1 * e^{kt}
    def T(c1, k, t):
        return c1*np.exp(k*t)


    # Funcion Y(y) = c2 * e^{ky}
    def Y(ct, k, y):
        return c2*np.exp(k*y)


    # Funcion u(t, y) = c1*c2 * e^{k(t+y)}
    def u(c, k, t, y):
        return c*np.exp(k*(t+y))


# Graficar para c1 y k, c2 y k para el k dado
    k1 = 1.5
    c1 = 2
    c2 = 3
    c = c1 * c2
    t = np.arange(-2, 2, 0.001)
    y = np.arange(-2, 2, 0.001)

# Plotting Graph T(t)
    plt.gca()
    plt.gca().plot(t, T(c1, k1, t), color='purple', alpha=0.85, label=r'$T(t) = c_1 e^{kt}, \: c_1 = 2, \: k = 1.5$')
    plt.title("Grafica de funcion T(t)")
    plt.xlabel('t')
    plt.ylabel('T(t)')
    plt.axhline(0, 0, color='black', linewidth=1)
    plt.axvline(0, 0, color='black', linewidth=1)

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/6toSemestre/FuncEsp/actividades/figuraT.png")
    plt.show()

# Plotting Graph Y(y)
    plt.gca()
    plt.gca().plot(y, Y(c2, k1, y), color='orangered', alpha=0.85, label=r'$Y(y) = c_2 e^{ky}, \: c_2 = 3, \: k = 1.5$')
    plt.title("Grafica de funcian Y(y)")
    plt.xlabel('y')
    plt.ylabel('Y(y)')
    plt.axhline(0, 0, color='black', linewidth=1)
    plt.axvline(0, 0, color='black', linewidth=1)

    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/6toSemestre/FuncEsp/actividades/figuraY.png")
    plt.show()
