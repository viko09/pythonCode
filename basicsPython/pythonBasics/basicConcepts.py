print("Hello world")

x = 2
y = 3
z = x ** y

print(z)

numericList = [1, 2, 3, 4]
stringList = ["Victor", "Alemania", "Mujeres", "alegria"]
combinedList = [1, "Mujer", 2, "Victor", 532, "Luna"]
L1 = list(range(10))  # Genera un conjunto de valores

print(numericList)
print(stringList)
print(combinedList)
print(numericList, L1)

# Uso de range y generacion de listas

L2 = list(range(0, 20, 2))
print("L2 = ", L2)

L3 = list(range(20, 0, -2))
print(L3)

# FUNCIONES DE LAS LISTAS:
# append: al final de la lista añade un valor
L3.append(43)
print("Append = ", L3)
# remove: elimina un elemento de la lista
L3.remove(4)
print("Remove = ", L3)
# index: devuelve el numero de la posición de un elemento
indx = L3.index(6)
indx2 = L3.index(43)
print("Index = ", indx)
print("Index = ", indx2)

# Se puede trabajar con el numero que devuelve
d = indx * 2
print(d)
