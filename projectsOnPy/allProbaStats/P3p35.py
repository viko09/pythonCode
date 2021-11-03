# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:05:56 2021

@author: luiso
"""
from scipy import stats

R1 = stats.hypergeom.pmf(2, 20, 12, 5)

print(R1)

R2 = stats.hypergeom.cdf(5, 20, 12, 5)

print(R2)