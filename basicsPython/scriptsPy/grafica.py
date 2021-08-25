import matplotlib.pyplot as plt
import numpy as np
import math


def f1(x):
    return (6.85*(10**-6))*np.sin(x)


x = np.arange(0, (math.radians(360)), 0.001)

fig = plt.figure()
ax = fig.add_subplot(111)

x_pi = f1(x)/np.pi
unit = 0.25
x_tick = np.arange(0, 2+unit, unit)

x_label = [r"$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$", r"$\frac{3\pi}{4}$", r"$\pi$", r"$\frac{5\pi}{4}$",
           r"$\frac{3\pi}{2}$", r"$\frac{7\pi}{4}$", r"$2\pi$"]
ax.set_xticks(x_tick*np.pi)
ax.set_xticklabels(x_label, fontsize=9)

plt.plot(x, f1(x), 'b', alpha=0.60)
plt.title("Torque respecto al Ángulo")
plt.axhline(0, 0, color='black')
plt.axvline(0, 0, color='black')
plt.xlabel('θ')
plt.ylabel('N*m')
plt.grid(alpha=0.75)
plt.show()
