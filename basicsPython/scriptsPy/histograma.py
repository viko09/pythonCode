# Histograma
# by. Viko Luna

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Your Data Here, Remember to change it
data = [0.95, 0.85, 0.92, 0.95, 0.93, 0.86, 1.00, 0.92, 0.85, 0.81,
        0.78, 0.93, 0.93, 1.05, 0.93, 1.06, 1.06, 0.96, 0.81, 0.96]

ySeg = [0.75, 0.85, 0.95, 1.05, 1.15]
mu = np.mean(data)
std = np.std(data)

plt.hist(data, bins=ySeg, edgecolor='black', ls='dotted', facecolor='yellow', alpha=0.55)
xmin, xmax = plt.xlim()
# x = np.sort(data)
# p = norm.pdf(x, mu, std)
# plt.plot(x, p, 'k', linewidth=2)
title = "Histograma de Frecuencias: "
plt.title(title)
plt.xlabel('Datos')
plt.ylabel('Frecuencia')
plt.axvline(mu, color='blue', label="Media")
plt.legend()
plt.xticks(ySeg)
plt.grid(alpha=0.75)
plt.savefig('/home/vikoluna/Documents/BUAP/5toSemtre/PYE/Examen1/4hist.png', dpi=150)
plt.show()
