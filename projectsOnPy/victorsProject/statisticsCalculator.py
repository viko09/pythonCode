# ###################################
# ###########CALCULATOR##############
# ############by. Viko###############

from projectsOnPy.victorsProject.importingDataset import data
from projectsOnPy.victorsProject.setOper import sets

print('=' * 42)
print('¡Bienvenido a la calculadora del curso!\n'
      '            FCFM - BUAP\n'
      'Creado por: Victor Manuel Luna Mendoza ;)')
print('=' * 42)

print('¿Que deseas hacer hoy?\n')
print('1. Cargar un dataset para su análisis')
print('2. Operaciones de conjuntos')

opc = input()

if opc == "1":
    data()
elif opc == "2":
    sets()
else:
    print('Por valor elige una de las opciones')
