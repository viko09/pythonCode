import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# tus datos aqui
A = np.array([350, 350, 350, 358, 370, 370, 370, 371, 371, 372, 372, 384, 391, 391, 392])
B = np.array([350, 354, 359, 363, 365, 368, 369, 371, 373, 374, 376, 380, 383, 388, 392])
C = np.array([350, 361, 362, 364, 364, 365, 366, 371, 377, 377, 377, 379, 380, 380, 392])

print('Media A')
print(np.mean(A))
print('Mediana A')
print(np.median(A))
print('std A')
print(np.std(A))

print('------------------------------')

print('Media B')
print(np.mean(B))
print('Mediana B')
print(np.median(B))
print('std B')
print(np.std(B))

print('------------------------------')

print('Media C')
print(np.mean(C))
print('Mediana C')
print(np.median(C))
print('std C')
print(np.std(C))

print('------------------------------')

df = np.zeros((A.size + B.size + C.size, 2))
df = pd.DataFrame(df, columns=['Datos', 'Muestra'])
for k in range(A.size):
    df.Datos[k] = A[k]
    df.Muestra[k] = 'Tipo 1'
for k in range(B.size):
    df.Datos[k + A.size] = B[k]
    df.Muestra[k + A.size] = 'Tipo 2'
for k in range(C.size):
    df.Datos[k + A.size + B.size] = C[k]
    df.Muestra[k + A.size + B.size] = 'Tipo 3'

# Figura 1
fig, ax = plt.subplots()
ax = sns.boxplot(x="Datos", y="Muestra", data=df)
plt.savefig('/home/vikoluna/Documents/BUAP/5toSemtre/PYE/Examen1/pr5.png', dpi=300)  # Modificame
plt.title("Diagrama de Cajas y Bigotes")
plt.grid()
plt.show()
