with open("dat.txt", "r") as dats:
    line = [float(x) for x in dats.read().split()]

print("data = ", line, '\n')
dats.close()
