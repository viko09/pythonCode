# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:05:56 2021

@author: luiso
"""
from scipy import stats
import numpy as np

R1=stats.poisson.pmf(5, 4.5)


R2=stats.poisson.cdf(5, 4.5)

x=np.arange(0, 6)
R2a=sum(stats.poisson.pmf(x, 4.5))


print(R1)

print(R2)

print(R2a)