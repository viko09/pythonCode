# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 10:41:49 2021

@author: luiso
"""

import numpy as np
import matplotlib.pyplot as plt


x=np.array([0,1,2,3,4,5,6,7,8,9,10])
p=np.array([0.002,0.001,0.002,0.005,0.02,0.04,0.18,0.37,0.25,0.12,0.01])

mu=sum(x*p)

print('Valor de Espectacion')
print(mu)


plt.plot(x,p)
plt.plot(mu,np.median(p),'*')

plt.savefig('Figure 1.png', dpi=300) # Modificame
plt.show()