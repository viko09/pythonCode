# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 11:16:56 2021

@author: luiso
"""

import numpy as np
import matplotlib.pyplot as plt


x=np.array([4,6,8])
p=np.array([0.5,0.3,0.2])

mu=sum(x*p)

V=sum((x-mu)**2*p)

print('Valor de Espectacion')
print(mu)

print('Varianza')
print(V)

print('std')
print(np.sqrt(V))


plt.plot(x,p)
plt.plot(mu,np.median(p),'*')

plt.savefig('Figure 1.png', dpi=300) # Modificame
plt.show()