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
n = sp.Symbol('n')


eq=3/2*(1-x**2)

print(eq)

f = sp.Piecewise((0, x < 0),(eq,(0<=x)& (x<=1)),(0,1<x))

EQ=sp.integrate(eq, (x,0,n))-0.5
print(EQ)
# la solucion se convierte a numero
sol=float(sp.nsolve(EQ,n,(0,1)))
print(sol)


#Graficas A
ff=sp.lambdify(x,f)
fig, ax = plt.subplots()

xn=np.linspace(-0.5,2.5, 100)
ax.plot(xn,ff(xn),color = 'k')

# Segmento que se integro
x1=np.linspace(-0.5,sol, 100)

ax.fill_between(x1,ff(x1),color = 'b',alpha=0.5)
plt.title('Figura A')
plt.savefig('Figure 4.png', dpi=300) # Modificame
