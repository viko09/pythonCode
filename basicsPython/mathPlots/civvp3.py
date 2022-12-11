import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Grid of 2D plot
x, y = np.meshgrid(np.linspace(-10, 10, 13), np.linspace(-10, 10, 13))

u = y
v = 1/2

# create the 2D plot
# plt.plot(theta, x2, color='green', alpha=0.55, label=r'$r = \sin\theta$')
# plt.scatter(np.pi / 4, np.sqrt(2) / 2, color='orange', label='Intersección')
plt.quiver(x, y, u, v)
plt.title("Diagrama de campo vectorial")
plt.xlabel(r'x')
plt.ylabel(r'y')
plt.axhline(0, 0, color='black')
plt.axvline(0, 0, color='black')

# plt.gca().set_aspect('equal')
plt.grid(color='g', linestyle='dotted', linewidth=1)
# Graph Settings

# plt.legend()
plt.savefig("/home/vikoluna/Documents/BUAP/6toSemestre/CIVV/unidad2/Tarea6/diag1.png", dpi=300)
plt.show()

# # Grid of 3D plot
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# X1, Y1, Z1 = np.meshgrid(np.arange(-10, 10, 12),
#                       np.arange(-10, 10, 12),
#                       np.arange(-10, 10, 18))
#
# u_1 = y
# v_1 = 1/2
# w_1 = 0
#
# ax.quiver(X1, Y1, Z1, u_1, v_1, w_1, length=0.1, color='black')
#
# plt.show()