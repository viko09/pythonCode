# Operaciones de conjuntos
from matplotlib_venn import venn3
from matplotlib import pyplot as plt

A = {0, 1, 2, 3, 4, 'Juan'}
B = {3, 4, 5, 6, 'Juan'}
C = {1, 3, 5, 'Pedro'}

# espacio muestral
S = A | B | C

# complemento A'
print('Complemento A' ':', S-A)

# Union
print("Union A U B :", A | B)

# Union
print("Union A U C:", A | C)

# Interseccion
print("Interseccion A n B:", A & B)

# Interseccion
print("Interseccion A n C:", A & C)

# (A  C)
print("S-(A & C) :", S-(A & C))

venn3([A, B, C], ('A', 'B', 'C'))
plt.savefig('Figure 1.png', dpi=300)  # Modificame
plt.show()
