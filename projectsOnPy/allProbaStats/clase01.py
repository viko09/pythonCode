# -*- coding: utf-8 -*-
"""
Spyder Editor

Un conjunto de datos
"""

import stemgraphic as sg
import matplotlib.pyplot as plt
import numpy as np


# tus datos aqui
A=np.array([16.1,9.6,24.9,20.4,12.7,21.2,30.2,25.8,18.5, \
   10.3,25.3,14.0,27.1,45.0,23.3,24.2,14.6,  \
       8.9,32.4,11.8,28.5])
    
# Puntos para el histograma
n=10

print('Media')
print(np.mean(A))

print('Mediana')
print(np.median(A))

print('std')
print(np.std(A))

# Figura 1
fig, ax = plt.subplots()
sg.stem_graphic(A,scale=10,compact=True);
plt.savefig('Figura01.png', dpi=300)
plt.show()

# Figura 2
fig, ax = plt.subplots(figsize=(5,1))
ax.spines["top"].set_color("None")
ax.spines["left"].set_color("None")
ax.spines["right"].set_color("None")
ax.spines['bottom'].set_position('zero')
plt.yticks([])
plt.scatter(A, A*0, c="g", alpha=0.5)
plt.scatter(np.mean(A), 0, c="r", alpha=0.5)
plt.savefig('Figura02.png', dpi=300)  # Modificame
plt.show()

# Figura 3
fig, ax = plt.subplots()
hist, edges = np.histogram(A,n)
y = np.arange(hist.min(),hist.max())
x = np.linspace(np.min(A),np.max(A),n)
X,Y = np.meshgrid(x,y)
plt.scatter(X,Y, c=Y<=hist, cmap="Greys")
plt.xlabel('Eje X') # Modificame
plt.ylabel('Eje Y') # Modificame
plt.savefig('Figura03.png', dpi=300) # Modificame
plt.show()

# Figura 4
fig, ax = plt.subplots()
plt.hist(A,n,ec="k")
plt.xlabel('Eje X') # Modificame
plt.ylabel('Eje Y') # Modificame
plt.savefig('Figura04.png', dpi=300) # Modificame
plt.show()
