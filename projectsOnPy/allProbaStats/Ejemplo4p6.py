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
A = sp.Symbol('A')
B = sp.Symbol('B')


eq=1/(B-A)

f = sp.Piecewise((0, x < A),(eq,(A<=x)& (x<=B)),(0,B<x))

# A
R=sp.integrate(f, (x,-sp.oo,x))
print('A1')
print(R)
R=sp.integrate(eq, (x,A,x))
print('A2')
print(R)

# si A=2 y B=4
f=f.subs([(A, 2), (B, 4)])

#Graficas
ff=sp.lambdify(x,f)
fig, ax = plt.subplots()

xn=np.linspace(0,5, 100)
ax.plot(xn,ff(xn),color = 'k')

# Segmento que se integro
x1=np.linspace(0,5, 100)

ax.fill_between(x1,ff(x1),color = 'b',alpha=0.5)
plt.title('Figura')
plt.savefig('Figure 4.png', dpi=300) # Modificame