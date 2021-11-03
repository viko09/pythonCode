# ###################################
# ###########CALCULATOR##############
# ############by. Viko###############
import pandas as pd

print('=' * 42)
print('¡Bienvenido a la calculadora del curso!\n'
      '            FCFM - BUAP\n'
      'Creado por: Victor Manuel Luna Mendoza ;)')
print('=' * 42)

print('Ingresa tus datos en csv, por favor.')
readFile = input("Pega aqui el directorio: ")

print('-'*45)

data = pd.read_csv(readFile)
print('\nLa cabezera de tus datos son: ')
print(data.head())
