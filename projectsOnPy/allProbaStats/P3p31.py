# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 12:31:48 2021

@author: luiso
"""

from scipy import stats
import numpy as np

print('a')
R1=stats.binom.pmf(3, 6, 0.5)
print(R1)

print('b')
x=np.arange(3, 7)
R2=stats.binom.pmf(x, 6, 0.5)
print(np.sum(R2))

print('bb menor o igual que 3')
x=np.arange(0, 4)
R2ba=stats.binom.pmf(x, 6, 0.5)
print(np.sum(R2ba))
print('bb menor o igual que 3 otro')
R2bb=stats.binom.cdf(3, 6, 0.5)
print(R2bb)


print('b')
x=np.arange(0, 2)
R3=stats.binom.pmf(x, 6, 0.5)
print(np.sum(R3))
print('b otro')
R4=stats.binom.cdf(1, 6, 0.5)
print(R4)
