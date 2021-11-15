import matplotlib.pyplot as plt
import numpy as np


def f(xa, ya):
    return xa ** 2 - ((ya - 1) ** 2)


x1 = np.linspace(-10, 15, 30)
y1 = np.linspace(-10, 15, 30)

X, Y = np.meshgrid(x1, y1)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 95, cmap='Oranges')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(20, 65)
# mplot3d.Axes3D(X, Y, Z, 95, cmap='cubehelix', label=r'$x^2 - (y-1)^2$')
plt.title('Gráfica de la función')
plt.show()
