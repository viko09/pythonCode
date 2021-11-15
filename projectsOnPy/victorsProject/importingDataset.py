import os
import pandas as pd


def data():
    print('Ingresa tus datos en csv, por favor.')
    readFile = input("Pega aqui el directorio: ")
    if os.path.isfile(readFile):
        existingFile = pd.read_csv(readFile)
        print(existingFile.head())
        print('\nEste es tu dataset?')
        answer = input('Si/No: ')
        if answer == "Si":
            print('-/'*30)
            print('Que deseas calcular?')
            print('1. Media')
            print('2. Mediana')
            print('3. Moda')
            opc = input()
        elif answer == 'No':
            print('Vuelve a intentarlo :c')
    else:
        print('El directorio que ingresaste es incorrecto, lo siento.')
