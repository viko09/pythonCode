# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:05:56 2021

@author: luiso
"""
from scipy import stats
import numpy as np


#  h()
Ra = stats.hypergeom.pmf( 2,25,5, 10)

print('a')
print(Ra)

x=np.arange(0, 3)

Rb = stats.hypergeom.pmf(x,25,5, 10)

print('b')
print(sum(Rb))

Rbb = stats.hypergeom.cdf(2,25,5, 10)

print('b otro')
print(Rbb)