# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:05:56 2021

@author: luiso
"""
from scipy import stats

R1=stats.poisson.pmf(1, 2)

R1a=stats.binom.pmf(1,400, 0.005)


print(R1)

print(R1a)

R2=stats.binom.cdf(3,400, 0.005)
R2a=stats.poisson.cdf(3, 2)

print(R2)

print(R2a)