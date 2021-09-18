# Gráficas de tallos y hojas
# Viko Luna

import stemgraphic as sg
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Your Data Here
data = [8.9, 12.4, 8.6, 11.3, 9.2, 8.8, 6.2, 7.0, 7.1, 11.8, 10.7, 7.6, 9.1, 9.2, 8.2, 9.0, 8.7,
        9.1, 10.9, 10.3, 9.6, 7.8, 11.5, 9.3, 7.9, 8.8, 8.8, 12.7, 8.4, 7.8, 5.7, 10.5, 10.5, 9.6,
        8.9, 10.2, 10.3, 7.7, 10.6, 8.3, 8.8, 9.5, 8.8, 9.4]

ySeg = [5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5]
mu = np.mean(data)
std = np.std(data)

plt.hist(data, bins=ySeg, edgecolor='black', ls='dotted', facecolor='b', alpha=0.4)
plt.title('Histograma de Resistencia a la Tensión')
plt.xlabel('Resistencia a la tensión (lb/pulg²)')
plt.ylabel('Número de Pruebas')
plt.xticks(ySeg)
plt.axvline(mu, color='g', label="Promedio")
plt.legend()
plt.ylim(0, 40)
plt.grid(axis='y', alpha=0.75)
# plt.savefig('/home/vikoluna/Documents/BUAP/5 - Quinto Semestre/Prob. Stats./Tareas/ProbH13.png', dpi=150)
plt.show()

plt.hist(data, bins=ySeg, density=True, edgecolor='black', ls='dotted', facecolor='b', alpha=0.4)
xmin, xmax = plt.xlim()
x = np.sort(data)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
title = "Resultado del Ajuste: "
plt.title(title)
plt.xlabel('Resistencia a la tensión (lb/pulg²)')
plt.ylabel('Número de Pruebas')
plt.xticks(ySeg)
plt.grid(axis='y', alpha=0.75)
# plt.savefig('/home/vikoluna/Documents/BUAP/5 - Quinto Semestre/Prob. Stats./Tareas/ProbHF13.png', dpi=150)
plt.show()

sg.stem_graphic(data, compact=True)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
# plt.savefig('/home/vikoluna/Documents/BUAP/5 - Quinto Semestre/Prob. Stats./Tareas/Prob13TH.png', dpi=150)
plt.show()
