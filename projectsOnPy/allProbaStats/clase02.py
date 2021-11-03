# -*- coding: utf-8 -*-
"""
Spyder Editor

Un conjunto de datos
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# tus datos aqui
A=np.array([0.684,2.540,0.924,3.130,1.038,0.598, \
            0.483,3.520,1.285,2.650,1.497])
    

print('Media')
print(np.mean(A))

print('Mediana')
print(np.median(A))

print('std')
print(np.std(A))

df=np.zeros((A.size, 2))
df = pd.DataFrame(df,columns=['Datos', 'Muestra'])
for k in range(A.size):
    df.Datos[k]=A[k];
    df.Muestra[k]='A'


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