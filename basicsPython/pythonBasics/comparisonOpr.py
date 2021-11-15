# Odd or Even
x = int(input("Por favor ingrese un número: "))
if x % 2 == 0:
    print("El número {}, es par.".format(x))
else:
    print("El número {}, es impar.".format(x))

# Underage or not
y = int(input("\nPor favor ingrese su edad: "))
if y >= 21:
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")

# The biggest number
z1 = int(input("\nPor favor ingrese el primer número: "))
z2 = int(input("\nPor favor ingrese el segundo número: "))
if z1 > z2:
    print(f'{z1} es mayor que {z2}.')
elif z1 == z2:
    print(f'{z1} es igual a {z2}')
else:
    print(f'{z2} es mayor que {z1}')

# The biggest number
z1 = int(input("\nPor favor ingrese el primer número: "))
z2 = int(input("\nPor favor ingrese el segundo número: "))
if z1 > z2:
    print(f'El número mayor es {z1}.')
elif z1 == z2:
    print('Los numeros son iguales')
else:
    print(f'El número mayor es {z2}.')
