# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 13:54:46 2021

@author: luiso
"""

import sympy as sp

# Variables
x = sp.Symbol('x')
A = sp.Symbol('A')
B = sp.Symbol('B')


eq=1/(B-A)

f = sp.Piecewise((0, x < A),(eq,(A<=x)& (x<=B)),(0,B<x))

F=sp.integrate(f, (x,-sp.oo,x))

f0=sp.diff(F, x)

print(f0)

