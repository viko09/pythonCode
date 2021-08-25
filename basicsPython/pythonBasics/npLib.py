import numpy as np
import time

# Arreglo a partir de un objeto iterable

lista = [10, 20, 30, 40, 50]

print(type(lista))

a = np.array(lista)

print(type(a))

print(a.ndim)
print(a.size)
print(a.itemsize)
print(a.shape)

# obtener elementos almacenados a partir de sus indices

print(a[0])
print(a[a.size - 1])  # conocer el ultimo elemento

print(a[1:4:2])
print(a[::-1])

lista = [0, 1, 3, 4]

for i in lista:
    print(a[i])

print(a[lista])

print(a[[0, 0, 3, 4]])

print(a)
print(a*10 - a**2 / 8)

# from numpy import * (se usa para usar las funciones sin llamarlas con np.)

# Making an array of numbers
A = np.array([1, 2, 3, 4, 5])
print(A)

# Checking the version of numpy
ver = np.__version__
print(ver)

# Measuring the time of execution
array1 = np.arange(100)
array2 = list(range(100))

start_time1 = time.time()
for i in range(10):
    my_array1 = array1 * 2
    print(my_array1)
print("\ntime elapsed: ", (time.time() - start_time1))

start_time2 = time.time()
for i in range(10):
    my_array2 = [2*x for x in array2]
    print(my_array2)

print("\ntime elapsed: ", (time.time() - start_time2))

# The following line create an array
A2 = np.arange(start=100)
print(A2)

# Making a list
list1 = list(range(10))
print('\n', list1)

# List to array
array1 = np.array(list1)
print(array1)
