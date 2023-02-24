# Ciclo For
for i in range(0, 10):
    print(i)

print('·'*35)
# Ciclo For anidado, sirve para recorrer en mas dimensiones
for i in range(0,3):
    for j in range(0,3):
        print(j)
        print(i)

print('·'*35)
# Función Pass: No retorna nada, recorre el ciclo sin regresar algo
print("Función 'Pass' : ")
for i in range(0, 3):
    pass

print('·'*35)
# Recorrer arreglos de elementos
frutas = ['manzana', 'mango', 'platano']
for fruta in frutas:
    print(fruta)
