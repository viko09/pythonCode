# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:05:56 2021

@author: luiso
"""
from scipy import stats
import numpy as np

R1=stats.nbinom.pmf(10, 5, 0.2)

R2=stats.nbinom.cdf(10, 5, 0.2)
x=np.arange(0, 11)
R2a=sum(stats.nbinom.pmf(x, 5, 0.2))

print(R1)

print(R2)

print(R2a)