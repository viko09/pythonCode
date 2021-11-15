import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.arrage(-15, 15, 0.001)


def fun(x, y):
    return x**2 - (y-1)**2


x1, y1 = fun(zline, zline)
ax.plot3D(x1, y1, zline, 'gray')
