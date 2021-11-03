# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 12:31:48 2021

@author: luiso
"""

from scipy import stats
import numpy as np

print('1')
x=np.arange(0, 9)
R1=stats.binom.pmf(x, 15, 0.2)
print(np.sum(R1))

print('1 otro')
R2=stats.binom.cdf(8, 15, 0.2)
print(R2)

print('2')
R3=stats.binom.cdf(8, 15, 0.2)-stats.binom.cdf(7, 15, 0.2)
print(R3)
print('2 otro')
print(stats.binom.pmf(8, 15, 0.2))

print('3')
R4=1-stats.binom.cdf(7, 15, 0.2)
print(R4)

