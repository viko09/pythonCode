# Gráficas de tallos y hojas
# Viko Luna

import stemgraphic as sg
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Your Data Here
data = [122.2, 127.5, 130.4, 131.8, 132.7, 133.2, 134.0, 124.2, 127.9, 130.8, 132.3, 132.9, 133.3, 134.0, 124.3,
        128.6, 131.3, 132.4, 133.0, 133.3, 134.0, 125.6, 128.8, 131.4, 132.4, 133.1, 133.5, 134.1, 126.3, 129.0,
        131.4, 132.5, 133.1, 133.5, 134.2, 126.5, 129.2, 131.5, 132.5, 133.1, 133.5, 134.3, 126.5, 129.4, 131.6,
        132.5, 133.1, 133.8, 134.4, 127.2, 129.6, 131.6, 132.5, 133.2, 133.9, 134.4, 127.3, 130.2, 131.8, 132.6,
        133.2, 134.0, 134.6, 134.7, 135.2, 135.7, 135.9, 136.6, 137.8, 138.4, 139.1, 140.9, 143.6, 134.7, 135.2,
        135.8, 136.0, 136.8, 137.8, 138.4, 139.5, 140.9, 143.8, 134.7, 135.3, 135.8, 136.0, 136.9, 137.8, 138.4,
        139.6, 141.2, 143.8, 134.8, 135.3, 135.8, 136.1, 136.9, 137.9, 138.5, 139.8, 141.4, 143.9, 134.8, 135.4,
        135.8, 136.2, 137.0, 137.9, 138.5, 139.8, 141.5, 144.1, 134.8, 135.5, 135.8, 136.2, 137.1, 138.2, 138.6,
        140.0, 141.6, 144.5, 134.9, 135.5, 135.9, 136.3, 137.2, 138.2, 138.7, 140.0, 142.9, 144.5, 134.9, 135.6,
        135.9, 136.4, 137.6, 138.3, 138.7, 140.7, 143.4, 147.7, 135.2, 135.6, 135.9, 136.4, 137.6, 138.3, 139.0,
        140.7, 143.5, 147.7]

ySeg = [122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148]
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
plt.savefig('/home/vikoluna/Documents/BUAP/5 - Quinto Semestre/Prob. Stats./Tareas/ProbH13.png', dpi=150)
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
plt.savefig('/home/vikoluna/Documents/BUAP/5 - Quinto Semestre/Prob. Stats./Tareas/ProbHF13.png', dpi=150)
plt.show()

sg.stem_graphic(data, compact=True)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.savefig('/home/vikoluna/Documents/BUAP/5 - Quinto Semestre/Prob. Stats./Tareas/Prob13TH.png', dpi=150)
plt.show()
