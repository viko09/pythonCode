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

q = 1-p
alpha=(1-IC)
zsigma2=stats.norm.ppf(alpha/2,loc=0, scale=1)
zsigma2=abs(zsigma2)

F=np.sqrt(4*zsigma2**4*q*p*(q*p-w**2)+w**2*zsigma2**4)

n=(2*zsigma2**2*q*p-zsigma2**2*w**2+F)/w**2

print(n)

# NOTA en el libro cometen un error al multiplicar p*q=0.25
# lo cual es incorrecto p*q=0.22