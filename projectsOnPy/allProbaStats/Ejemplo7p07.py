# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:14:18 2021

@author: luiso
"""
from scipy import stats

# ancho del intervalo de confianza
w = 50
# intervalo de confianza
IC = 0.95
# desviacion estandar
sigma = 175


alpha = (1-IC)
z = stats.norm.ppf(alpha/2, loc=0, scale=1)
n = (2*z*sigma/w)**2

# Muestras pequeñas
print(n)
