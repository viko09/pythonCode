# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:14:18 2021

@author: luiso
"""
from scipy import stats

# ancho del intervalo de confianza
w = 0.2
# intervalo de confianza
IC = 0.99
# desviacion estandar
sigma = 0.75


alpha = (1-IC)
z = stats.norm.ppf(alpha/2, loc=0, scale=1)
n = (2*z*sigma/w)**2

print(n)

