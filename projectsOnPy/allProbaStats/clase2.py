# -*- coding: utf-8 -*-
"""
Spyder Editor

Gráficas de puntos
"""

import stemgraphic as sg
import matplotlib.pyplot as plt
import numpy as np

# tus datos aqui
A=np.array([5434,4948,4521,4570,4990,5702,5241 \
,5112,5015,4659,4806,4637,5670,4381 \
,4820,5043,4886,4599,5288,5299,4848 \
,5378,5260,5055,5828,5218,4859,4780 \
,5027,5008,4609,4772,5133,5095,4618 \
,4848,5089,5518,5333,5164,5342,5069 \
,4755,4925,5001,4803,4951,5679,5256 \
,5207,5621,4918,5138,4786,4500,5461 \
,5049,4974,4592,4173,5296,4965,5170 \
,4740,5173,4568,5653,5078,4900,4968 \
,5248,5245,4723,5275,5419,5205,4452 \
,5227,5555,5388,5498,4681,5076,4774 \
,4931,4493,5309,5582,4308,4823,4417 \
,5364,5640,5069,5188,5764,5273,5042 \
,5189,4986])
    
# tus datos aqui
n=12
    
hist, edges = np.histogram(A,n)
y = np.arange(hist.min(),hist.max())
x = np.linspace(np.min(A),np.max(A),n)
X,Y = np.meshgrid(x,y)
plt.scatter(X,Y, c=Y<=hist, cmap="Greys")
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.savefig('Figura02.png', dpi=150)
plt.show()

