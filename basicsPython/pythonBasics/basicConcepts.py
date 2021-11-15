print("Hello world")

# Saving variable

# Integer value
myVar1 = 2
# Float Value
myVar2 = 4.5
# String Value
myVar3 = "Hello, this is Victor"
# Boolean Value
f1 = True
f2 = False

# Python vars should start with lower case, digits are allowed but not at the start
print(myVar1)
print(myVar2)
print(myVar3)
print(type(f1))
print(type(f2))

myVar4 = myVar2
# Recycle and change a new variable
myVar2 = "New One"

print(myVar4)
print(myVar2)

# -----------------------------------------

x = 10
y = 34.5
z = x + y

print(x, " + ", y, " = ", z)


# Literals are assigned to variables

# ´´´ id() function: Give us the memory path where it is stored
# se eliminan y se vuelven a crear cuando termina de ejecutarse un programa
# the memory path is unique
# ```
print(id(myVar1))
print(id(myVar2))
print(id(myVar4))

# Data types: ´´´
# ''' Dynamic Variables
print(type(x))
print(type(myVar3))

newVar: str = 'This is a string value'

# Classes save data types, OOP

# String
group = "RHCP"
print(group)
# Adding strings, concatenate
print("My Favourite Group is" + group)
# Adding string with commas
print(x, " + ", y, " = ", z)
txt = "My Favourite Group is"
print(txt, group)

# Converting variable
x1 = "1"
x2 = "2"
print(x1 + x2)

newx1 = int(x1)
newx2 = int(x2)
print(newx1 + newx2)

# Boolean types
var1 = 8 < 4
print(var1)

if var1:
    print("The result is true")
else:
    print("The result was false")

# Input function: enter data from user console
resultado = input()
print(resultado)

enteringData = input("Please enter your data: ")
print("You have written ", enteringData)

# Sum of two numbers
# Concatenation:
num1 = input("Type the first string: ")
num2 = input("Type the second string: ")
# This is the sum
n1 = int(input("Type the first number: "))
n2 = float(input("Type the second number: "))

# Results
result1 = num1 + num2
result2 = n1 + n2
print(result1)
print(result2)

# Rate your day
rate = int(input("How was your day? (1-10): "))
print("My day rate was: ", rate)

# Arithmetics Operators
epsilon = 3
delta = 5.6
suma = epsilon + delta
resta = epsilon - delta
multiplicacion = epsilon*delta
division = epsilon/delta
divisionInt = epsilon//delta
modulo = epsilon % delta
# The better way to print
print(f"Resultado suma: {suma}")
print(f"Resultado resta: {resta}")
print(f"Resultado multiplicacion: {multiplicacion}")
print(f"Resultado division: {division}")
print(f"Resultado division entera: {divisionInt}")
print(f"Resultado modulo: {modulo}")  # Residuo

exponente = epsilon**delta
print(f"Resultado exponenciacion: {exponente}")

# Assignment operators
myVal = 10
print(myVal)
myVal = 10 + 1
print(myVal)
# Increment with reassignment
myVal += 12
print(myVal)
myVal -= 10
print(myVal)
myVal *= 2
print(myVal)
myVal /= 0.04
print(myVal)
myVal //= 0.0433
print(myVal)
myVal %= 0.0565
print(myVal)

# Comparison Operators
a = 5
b = 2

same = (a == b)
print(f'Resultado == : {same}')
different = a != b
print(f'Resultado != : {different}')

# This is where I put my variables
x = 2
y = 3
z = x ** y

print(z)

# It is not necessary specify the type of variable
numericList = [1, 2, 3, 4]
stringList = ["Victor", "Alemania", "Mujeres", "alegria"]
combinedList = [1, "Mujer", 2, "Victor", 532, "Luna"]
L1 = list(range(10))  # Genera un conjunto de valores

print(numericList)
print(stringList)
print(combinedList)
print(numericList, L1)

# Use of range and generation of lists

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

# Tuples: I can not add or delete elements of the tuple
tup = (5, 7, 9, 19, 'D')
# print(id(tup))
print(type(tup))
print(tup)
tup1 = tup.count(tup)
print(tup1)

# Dictionaries
newDic = {'name': 'Viko', 'email': 'someone@gmail.com', 'age': '13'}
print(newDic)

# Sets:
niuSet = {2, 4, 5, 6, 7, 7, 8, 8, 65, 4}

# Complex numbers
cplx = 6 + 8j
print(cplx)
print(cplx*3)

# integer division
inDiv = 10//3
print(inDiv)

# Hint: Pista
x: str = "Hola Esto es un hint x: int = "  # En cualquier momento puede cambiar
