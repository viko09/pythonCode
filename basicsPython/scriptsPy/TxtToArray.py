# This script takes a .txt file and gives you an array.

# Author. Viko Luna

with open("datos.txt", "r") as archivo:
    # lines = archivo.readlines()
    line = [int(x) for x in archivo.read().splitlines()]

# print("data = ", lines, '\n')
print("data = ", line, '\n')

archivo.close()
