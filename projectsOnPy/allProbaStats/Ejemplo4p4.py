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

#  0<=x<=360
f = sp.Piecewise((0, x < 0),(1/360,(0<=x)& (x<=360)),(0,360<x))

# A
R=sp.integrate(f, (x, 90, 180))
print('A')
print(R)

# B
R=sp.integrate(f, (x,0,90))+sp.integrate(f, (x,270,360))
print('B')
print(R)

#Graficas A---------------------------
fig, ax = plt.subplots()

ff=sp.lambdify(x,f)
xc=np.linspace(-10,380, 200)
ax.plot(xc,ff(xc),color = 'k')

# Segmento que se integro
x1=np.linspace(90,180, 100)
ax.fill_between(x1,ff(x1),color = 'b',alpha=0.5)
plt.title('Figura A')
plt.savefig('Figure 4.png', dpi=300) # Modificame

#Graficas B--------------------------
ff=sp.lambdify(x,f)
fig, ax = plt.subplots()

xc=np.linspace(-10,380, 200)
ax.plot(xc,ff(xc),color = 'k')

# Segmento que se integro
x1=np.linspace(0,90, 100)
x2=np.linspace(270,360, 100)
ax.fill_between(x1,ff(x1),color = 'b',alpha=0.5)
ax.fill_between(x2,ff(x2),color = 'b',alpha=0.5)
plt.title('Figura B')
plt.savefig('Figure 4.png', dpi=300) # Modificame