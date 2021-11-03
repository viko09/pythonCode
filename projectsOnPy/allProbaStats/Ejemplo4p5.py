# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 13:54:46 2021

@author: luiso
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Variables
x = sp.Symbol('x')


f = sp.Piecewise((0, x < 0.5),(0.15*sp.exp(-0.15*(x-0.5)),x>=0.5))

# A
R=sp.integrate(f, (x,-sp.oo,sp.oo))
print('A')
print(R)

# B
R=sp.integrate(f, (x,-sp.oo,5))
print('B')
print(R)


#Graficas
ff=sp.lambdify(x,f)
fig, ax = plt.subplots()

xn=np.linspace(0,10, 100)
ax.plot(xn,ff(xn),color = 'k')

# Segmento que se integro
x1=np.linspace(0,5, 100)

ax.fill_between(x1,ff(x1),color = 'b',alpha=0.5)
plt.title('Figura B')

plt.savefig('Figure 4.png', dpi=300) # Modificame