# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:14:18 2021

@author: luiso
"""
from scipy import stats
import numpy as np
sigma=2
N=31
mu=80
I=stats.norm.interval(0.95, loc=mu, scale=sigma/np.sqrt(N))
print(I)