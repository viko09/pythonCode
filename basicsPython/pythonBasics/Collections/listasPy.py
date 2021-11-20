thisisaList = ['Pepe', 'Viko', 'Guanabacoa', 'Xochitl', 1, True, 8, -23, -6 + 4j, 7]
names = ['Pepe', 'Viko', 'Guanabacoa']

# Print List
print(names)

# Print type
print(type(thisisaList))

# Access to elements of a list
print(thisisaList[8])
print(type(thisisaList[8]))
print(thisisaList[0])

# Access to elements of a list in reverse
print(thisisaList[-1])
print(thisisaList[-2])

# ---------- FUNCIONES DE LISTAS ------------------
# print a range from 0 to n-1
print(thisisaList[0:3])
# From  0 to n-1
print(thisisaList[:3])
# From n to end
print(thisisaList[3:])

# Changing a value
names[2] = 'Victor'
print(names)

# Iterate a list
for elements in thisisaList:
    print(elements)
else:
    print('No more elements')

# Numbers of elemets in a list
print(len(names))
print(len(thisisaList))

# Add elements
names.append('Sandra')
print(names)

# Insert an element into an specific index
names.insert(2, 'Gustave')
print(names)

# Remove Elements
names.remove('Sandra')
print(names)

# Remove the last element added
names.pop()
print(names)

# Remove an index
del names[1]
print(names)

# Clear a list
names.clear()
print(names)

# Delete the list
del names
