# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 10:31:46 2021

@author: luiso
"""
import numpy as np
import matplotlib.pyplot as plt


x=np.array([1,2,3,4,5,6,7])
p=np.array([0.01,0.03,0.13,0.25,0.39,0.17,0.02])

mu=sum(x*p)

print('Valor de Espectacion')
print(mu)


plt.plot(x,p)
plt.plot(mu,np.median(p),'*')

plt.savefig('Figure 1.png', dpi=300) # Modificame
plt.show()