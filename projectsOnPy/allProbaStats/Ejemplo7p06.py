# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:14:18 2021

@author: luiso
"""
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np


data = [62,50,53,57,41,53,55,61,59,64,50,53,64,62,50,68,\
54,55,57,50,55,50,56,55,46,55,53,54,52,47,47,55,\
57,48,63,57,57,55,53,59,53,52,50,55,60,50,56,58]

I=stats.t.interval(0.95,len(data)-1,np.mean(data),scale=stats.sem(data)) 
print(I)
print('mean')
print(np.mean(data))
print('std')
print(np.std(data))

plt.boxplot(data)

plt.savefig('Figure 4.png', dpi=300) # Modificame


