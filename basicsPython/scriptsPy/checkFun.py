import numpy as np


def f1(x, y):
    return (y*((-8*(x**2)) - (y**2) + 4))/(2*(np.sqrt(4 - (y**2) - (4*(x**2)))))


def f2(x, y):
    return (x*(2 - (2*(x**2)) - (y**2)))/(np.sqrt((4- (4*(x**2)) - (y**2))))


x1 = 0
y1 = -((2*(np.sqrt(2)))/(np.sqrt(3)))

x2 = np.sqrt((1/3))
y2 = -((2*(np.sqrt(2)))/(np.sqrt(3)))

x3 = -np.sqrt((1/3))
y3 = -((2*(np.sqrt(2)))/(np.sqrt(3)))

print('f1 = ', f1(x1, y1), 'f2 = ', f2(x1, y1))
print('f1 = ', f1(x2, y2), 'f2 = ', f2(x2, y2))
print('f1 = ', f1(x3, y3), 'f2 = ', f2(x3, y3))
