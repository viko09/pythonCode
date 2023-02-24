# Ciclo while
i = 0
while i < 10:
    print(i)
    i = i + 1

print('·'*35)
# Condicional dentro de un bucle utilizando la sentencia break la cual permite salir de un bucle
j = 0
while j < 10:
    if j == 3:
        break
    print(j)
    j = j + 1

print('·'*35)
# Funcion Continue: Si se cumple el if, va a saltar el caso de la condicion
k = 0
while k < 10:
    k = k + 1
    if k == 3:
        continue
    print(k)
