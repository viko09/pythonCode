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

eq=1/8+3/8*x

f = sp.Piecewise((0, x < 0),(eq,(0<=x)& (x<=2)),(0,2<x))

# A
F1=sp.integrate(f, (x,0,x))
F2=sp.integrate(eq, (x,0,x))

print('sol 1')
print(F1)
print('sol 2')
print(F2)

# P(1<=X<=1.5)  A
print('A')
print(sp.integrate(f, (x,1,1.5)))
print(F1.subs(x,1.5)-F1.subs(x,1))

# P(X>1)        B
print('B')
print(sp.integrate(f, (x,1,sp.oo)))
print(1-F1.subs(x,1))


#Graficas A ----------------
ff=sp.lambdify(x,f)
fig, ax = plt.subplots()

xn=np.linspace(-0.5,2.5, 100)
ax.plot(xn,ff(xn),color = 'k')

# Segmento que se integro
x1=np.linspace(1,1.5, 100)
ax.fill_between(x1,ff(x1),color = 'b',alpha=0.5)

plt.title('Figura A')
plt.savefig('Figure 4.png', dpi=300) # Modificame

#Graficas B
ff=sp.lambdify(x,f)
fig, ax = plt.subplots()

xn=np.linspace(-0.5,2.5, 100)
ax.plot(xn,ff(xn),color = 'k')

# Segmento que se integro
x1=np.linspace(1,2.5, 100)
ax.fill_between(x1,ff(x1),color = 'b',alpha=0.5)
plt.title('Figura B')
plt.savefig('Figure 4.png', dpi=300) # Modificame