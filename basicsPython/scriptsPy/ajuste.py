import numpy as np
import matplotlib.pyplot as plt

xdata = np.array([6, 15, 25, 32, 37, 41, 45])
ydata = np.array([25, 27, 30, 33, 37, 41, 45])

n = int(len(xdata))
sum_y = sum(ydata)
sum_x = sum(xdata)
x2 = sum(xdata * xdata)
xy = sum(xdata * ydata)
y2 = sum(ydata * ydata)
b = (sum_y * x2 - sum_x * xy) / (n * x2 - sum_x ** 2)
m = (n * xy - sum_y * sum_x) / (n * x2 - sum_x ** 2)
# r = (n * xy - sum_x * sum_y) / (np.sqrt(n * x2 - sum_x ** 2) * np.sqrt(n * y2 - sum_y ** 2))
beta = np.arange(n)
for j in range(n):
    beta[j] = (b + (m * xdata[j]) - ydata[j]) ** 2
beta2 = sum(beta)
errorm = np.sqrt((n / ((n * x2) - (sum_x * sum_x))) * (beta2 / (n - 2)))
errorb = np.sqrt((x2 / (n * x2)) * (beta2 / (n - 2)))

mmin = "{0:.2f}".format(m)
erm = "{0:.2f}".format(errorm)
erb = "{0:.2f}".format(errorb)
bmin = "{0:.2f}".format(b)


def f1(x):
    return m * x + b


txterrorm = str(erm)
txtm = str(mmin)
txterrorb = str(erb)
txtb = str(bmin)

print(txtm, txtb, txterrorm, txterrorb)

ecuacion = ' y = (' + txtm + '\pm' + txterrorm + ')x +(' + txtb + '\pm' + txterrorb + ')'

# Plot the fitted function
plt.plot(xdata, ydata, 'ro', alpha=0.5)
plt.plot(xdata, ydata, 'bo', xdata, [f1(i) for i in xdata], 'orange', alpha=0.75,
         label='Ajuste y = (0.50 ± 0.06)x + (19.75±0.83)')
plt.title('Datos Experimentales con Ajuste Lineal')
plt.text(6, -0.6, r'$' + ecuacion + '$', fontsize=10)
plt.xlabel('\u03B8 i')
plt.ylabel('\u03B8 r')
plt.grid()
plt.legend()
# plt.savefig('Prob24.png', dpi=150)
plt.show()
