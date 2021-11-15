import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# --------------------------------------------------------------------------
# Here we import our csv data
data = pd.read_csv('measures20.csv')
print(data)
# Focal distance: 7.872

print("---------------------------------------------------------------")
# We assign variables
x = data['Objeto (s)']
print(x)
print("---------------------------------------------------------------")
y = data['Imagen (s’)']
print(y)

print("---------------------------------------------------------------")

x_fit = pd.array(x)
print(x_fit)

y_fit = pd.array(y)
print(y_fit)

print("---------------------------------------------------------------")

# Cambio de variable
x_test = 1/x_fit
print(x_test)
x_cv = pd.DataFrame(x_test)
print(x_cv)

y_test = 1/y_fit
print(y_test)
y_cv = pd.DataFrame(y_test)
print(y_cv)

print("---------------------------------------------------------------")
# New Dataset
newData = pd.concat([x_cv, y_cv], axis=1, keys=["X = 1/s", "Y = 1/s'"])
print(newData)

# --------------------------------------------------------------------------

y_cv1 = pd.array(y_cv)
x_cv1 = pd.array(x_cv)

n = 20
sum_y = sum(y_cv1)
print("Suma (Y)", sum_y)
sum_x = sum(x_cv1)
print("Suma (X)", sum_x)
x2 = sum(x_cv1 * x_cv1)
print("Suma (XX)", x2)
xy = sum(x_cv1 * y_cv1)
print("Suma (XY)", xy)
y2 = sum(y_cv1 * y_cv1)
print("Suma (YY)", y2)
# b = (sum_y * x2 - sum_x * xy) / (n * x2 - sum_x ** 2)
# m = (n * xy - sum_y * sum_x) / (n * x2 - sum_x ** 2)


# r = (n * xy - sum_x * sum_y) / (np.sqrt(n * x2 - sum_x ** 2) * np.sqrt(n * y2 - sum_y ** 2))
# beta = np.arange(n)
# for j in range(n):
#     beta[j] = (b + (m * x_cv[j]) - y_cv[j]) ** 2
# beta2 = sum(beta)
# errorm = np.sqrt((n / ((n * x2) - (sum_x * sum_x))) * (beta2 / (n - 2)))
# errorb = np.sqrt((x2 / (n * x2)) * (beta2 / (n - 2)))

# mmin = "{0:.2f}".format(m)
# erm = "{0:.2f}".format(errorm)
# erb = "{0:.2f}".format(errorb)
# bmin = "{0:.2f}".format(b)

# def f1(x):
#     return m * x + b

# txterrorm = str(erm)
# txtm = str(mmin)
# txterrorb = str(erb)
# txtb = str(bmin)

# print(txtm, txtb, txterrorm, txterrorb)

# ecuacion = ' y = (' + txtm + '\pm' + txterrorm + ')x +(' + txtb + '\pm' + txterrorb + ')'

# Plot the fitted function
# plt.plot(x_cv, y_cv, 'ro', alpha=0.5)
# plt.plot(x_cv, y_cv, 'bo', x_cv, [f1(i) for i in x_cv], 'orange', alpha=0.75,
#          label='Ajuste y = (0.50 ± 0.06)x + (19.75±0.83)')
# plt.title('Datos Experimentales con Ajuste Lineal')
# # plt.text(6, -0.6, r'$' + ecuacion + '$', fontsize=10)
# plt.xlabel('\u03B8 i')
# plt.ylabel('\u03B8 r')
# plt.grid()
# plt.legend()
# # plt.savefig('Prob24.png', dpi=150)
# plt.show()