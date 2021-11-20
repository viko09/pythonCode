# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:14:18 2021

@author: luiso
"""
from scipy import stats
import numpy as np

#Promedio
p=654.16

#ensayos
n=50

#Confianza
IC=0.95

q=1-p
alpha=(1-IC)
zsigma2=stats.norm.ppf(alpha/2,loc=0, scale=1)
zsigma2=abs(zsigma2)

F=zsigma2*np.sqrt(p*q/n+zsigma2**2/4/(n**2))

# Limite de confiaza inferior
LCI=(p+zsigma2**2/2/n-F)/(1+zsigma2**2/n)

# Limite de confiaza superior
LCS=(p+zsigma2**2/2/n+F)/(1+zsigma2**2/n)

print('límite de confianza inferior')
print(LCI)

print('límite de confianza superior')
print(LCS)
