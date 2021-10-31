import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def estimate_b0_b1(x, y):
    # Number of elements of an array
    # n = np.size(x)

    # We got the mean value of X and Y
    m_x, m_y = np.mean(x), np.mean(y)

    # Now we calculate our sum XY and XX
    sum_xy = np.sum((x - m_x) * (y - m_y))
    sum_xx = np.sum((x - m_x) ** 2)

    # Regression Coefficients
    b_1 = sum_xy / sum_xx
    b_0 = m_y - b_1 * m_x

    return b_0, b_1


# Graph fun
def plot_reg(x, y, b):
    plt.scatter(x, y, color='g', alpha=0.55, marker='o', s=30)
    y_pred = b[0] + b[1] * x
    plt.plot(x, y_pred, color='purple', alpha=0.65)
    plt.xlabel('x (Variable Independiente)')
    plt.ylabel('y (Variable Dependiente)')
    plt.show()


# Main Code
def main():
    # Importing our dataset
    # Here we import our csv data
    data = pd.read_csv('measuresLens.csv')
    print(data)
# Focal distance: 7.872

    print("---------------------------------------------------------------")
    # We assign variables
    x_pd = data['Objeto (s)']
    print("---------------------------------------------------------------")
    y_pd = data['Imagen (s’)']
    print("---------------------------------------------------------------")
    x = pd.array(x_pd)
    y = pd.array(y_pd)
    print("---------------------------------------------------------------")

    # changing variable
    x_s = 1 / x
    y_s = 1 / y

    # b1 and b2
    b = estimate_b0_b1(x_s, y_s)
    print("Values: \n")
    print("b0 = {}, b1 = {}".format(b[0], b[1]))

    plot_reg(x_s, y_s, b)


if __name__ == "__main__":
    main()
