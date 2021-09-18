# Histograma
# by. Viko Luna

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import seaborn as sns
import pandas as pd
import stemgraphic as sg


# Your Data Here
data = np.array([0.95, 0.85, 0.92, 0.95, 0.93, 0.86, 1.00, 0.92, 0.85, 0.81,
        0.78, 0.93, 0.93, 1.05, 0.93, 1.06, 1.06, 0.96, 0.81, 0.96])

# ySeg = [5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5]
mu = np.mean(data)
std = np.std(data)

print('Media A')
print(np.mean(data))
print('Mediana A')
print(np.median(data))
print('std A')
print(np.std(data))


plt.hist(data, density=True, edgecolor='black', ls='dotted', facecolor='yellow', alpha=0.55)
xmin, xmax = plt.xlim()
x = np.sort(data)
p = norm.pdf(x, mu, std)
# plt.plot(x, p, 'k', linewidth=2)
title = "Histograma de Frecuencias: "
plt.title(title)
plt.xlabel('Datos')
plt.ylabel('Frecuencia')
plt.axvline(mu, color='blue', label="Media")
plt.legend()
# plt.xticks(ySeg)
plt.grid(alpha=0.75)
plt.savefig('/home/vikoluna/Documents/BUAP/5toSemtre/PYE/Examen1/por4his.png', dpi=150)
plt.show()

df = np.zeros((data.size, 2))
df = pd.DataFrame(df, columns=['Datos', 'Muestra'])
for k in range(data.size):
    df.Datos[k] = data[k]
    df.Muestra[k] = 'Steps/s'

# Figura 1
fig, ax = plt.subplots()
ax = sns.boxplot(x="Datos", y="Muestra", data=df)
plt.savefig('/home/vikoluna/Documents/BUAP/5toSemtre/PYE/Examen1/pro4box.png', dpi=300)  # Modificame
plt.title("Diagrama de cajas y bigotes para los datos de cadencia")
plt.grid(alpha=0.65)
plt.show()

# Figura 2
fig, ax = plt.subplots()
sns.violinplot(x="Datos", y="Muestra", data=df)
plt.savefig('/home/vikoluna/Documents/BUAP/5toSemtre/PYE/Examen1/pro4vio.png', dpi=300)  # Modificame
plt.title("Diagrama de violín de la cadencia")
plt.grid(alpha=0.65)
plt.show()

# Figura 1
fig, ax = plt.subplots()
sg.stem_graphic(data)
plt.savefig('/home/vikoluna/Documents/BUAP/5toSemtre/PYE/Examen1/pro4tyh.png', dpi=300)
plt.grid(alpha=0.65)
plt.show()
