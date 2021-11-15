import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def estimate_b0_b1(x, y):
    # Number of elements of an array
    n = np.size(x)
    print(n)

    # We got the mean value of X and Y
    m_x, m_y = np.mean(x), np.mean(y)
    print("\nMedia (X): ", m_x.round(5))
    print("Media (Y): ", m_y.round(5))

    # Now we calculate our sum XY and XX
    sum_xy = np.sum((x - m_x) * (y - m_y))
    print("Suma (XY): ", sum_xy.round(5))
    sum_xx = np.sum((x - m_x) ** 2)
    print("Suma (XX): ", sum_xx.round(5))

    sumX = np.sum(x)
    sumY = np.sum(y)

    print("Suma (X): ", sumX.round(5))
    print("Suma (Y): ", sumY.round(5))

    # Regression Coefficients
    b_1 = sum_xy / sum_xx
    b_0 = m_y - b_1 * m_x


    return b_0, b_1


# Graph fun
def plot_reg(x, y, b):
    plt.scatter(x, y, color='r', alpha=0.45, marker='o', s=30, label='Datos de s y s con cambio de variable')
    plt.scatter(x[0], y[0], color='cyan', alpha=0.95, marker='o', s=30, label='Inicio: ({},{})'.format(x[0].round(4),
                                                                                                        y[0].round(4)))
    plt.scatter(x[19], y[19], color='green', alpha=0.75, marker='o', s=30,
                label='Fin: ({},{})'.format(x[19].round(4), y[19].round(4)))
    y_pred = b[0] + b[1] * x
    y_teor = 0.126 - 0.982*x

    print(y_pred)

    plt.gca()
    plt.gca().plot(x, y_pred, color='purple', alpha=0.65, label=r"Ajuste: ${}x + {}$".format(b[1].round(5),
                                                                                             b[0].round(5)))
    plt.gca().plot(x, y_teor, color='blue', alpha=0.55, label=r"Ajuste Experimental: $-0.982x + 0.126$")
    plt.xlabel("Objeto (1/s)")
    plt.ylabel("Imagen (1/s)")
    # Graph Settings
    plt.grid(color='g', linestyle='dotted', linewidth=1)
    plt.legend()

    plt.title('Recta de mejor ajuste')

    # Save as png
    plt.savefig("/home/vikoluna/Documents/BUAP/5toSemtre/FEXPIII/practica4/datExp3.png")

    plt.show()


# Main Code
def main():
    # Importing our dataset
    # Here we import our csv data
    data = pd.read_csv('measuresLens.csv')
    print(data)

    print("="*45)
# Focal distance: 7.872


    # We assign variables
    x_pd = data['Objeto (s)']

    y_pd = data['Imagen (ss)']

    x = pd.array(x_pd)
    y = pd.array(y_pd)

    # changing variable
    x_s = 1 / x
    y_s = 1 / y

    # b1 and b2
    b = estimate_b0_b1(x_s, y_s)
    print("\nValues: ")
    print("m = {}, b = {}".format(b[1].round(5), b[0].round(5)))

    print("foco = ", (1/b[0].round(5)).__round__(5))

    plot_reg(x_s, y_s, b)


if __name__ == "__main__":
    main()
