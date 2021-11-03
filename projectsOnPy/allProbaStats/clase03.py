# -*- coding: utf-8 -*-
"""
Spyder Editor

Dos conjuntos de datos
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# tus datos aqui
A=np.array([6.0,5.0,11.0,33.0,4.0,5.0,80.0,18.0, \
            35.0,17.0,23.0])
    
B=np.array([4.0,14.0,11.0,9.0,9.0,8.0,4.0,20.0, \
            5.0,8.9,21.0,9.2,3.0,2.0,0.3])
        

print('Media A')
print(np.mean(A))

print('Mediana A')
print(np.median(A))

print('std A')
print(np.std(A))

print('Media B')
print(np.mean(B))

print('Mediana B')
print(np.median(B))

print('std B')
print(np.std(B))

df=np.zeros((A.size+B.size, 2))
df = pd.DataFrame(df,columns=['Datos', 'Muestra'])
for k in range(A.size):
    df.Datos[k]=A[k];
    df.Muestra[k]='A'
for k in range(B.size):
    df.Datos[k+A.size]=B[k];
    df.Muestra[k+A.size]='B'


# Figura 1
fig, ax = plt.subplots()
ax = sns.boxplot(x="Datos", y="Muestra", data=df)
plt.savefig('Figura01.png', dpi=300) # Modificame
plt.show()

# Figura 2
fig, ax = plt.subplots()
sns.violinplot(x="Datos", y="Muestra", data=df)
plt.savefig('Figura02.png', dpi=300) # Modificame
plt.show()