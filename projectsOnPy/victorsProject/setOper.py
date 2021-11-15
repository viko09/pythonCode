from matplotlib_venn import venn2
from matplotlib_venn import venn3
from matplotlib import pyplot as plt


def sets():
    print('¿Cuantos conjuntos quieres operar?\n(De momento solo opero con 3 conjuntos :c )')
    print('2')
    print('3')

    opc = input()

    if opc == "2":
        print('Ingresa los datos de tus conjuntos, por favor.')
        print('Conjunto A: ')
        setA = {input()}
        print(setA)
        print('Conjunto B: ')
        setB = {input()}
        print(setB)
        S = setA | setB

        # complemento A'
        print('Complemento A' ':', S - setA)

        # Union
        print("Union A U B :", setA | setB)

        # Interseccion
        print("Interseccion A n B:", setA & setB)

        print('='*45)
        print('¿Deseas realizar un diagrama de Venn?')
        print('1. Si')
        print('2. No')
        opt = input()

        if opt == "1":
            print('Gracias, que tenga buen dia. Pulse cualquier tecla para continuar')
            input()
            venn2([setA, setB], ('A', 'B'))
            plt.show()
        else:
            print('Gracias, que tenga buen dia. Pulse cualquier tecla para continuar')
            input()

    elif opc == "3":
        print('Ingresa los datos de tus conjuntos, por favor.')
        print('Conjunto A: ')
        setA = set(input())
        print(setA)
        print('Conjunto B: ')
        setB = {input()}
        print(setB)
        print('Conjunto C: ')
        setC = {input()}
        print(setC)
        S = setA | setB | setC
        # complemento A'
        print('Complemento A' ':', S - setA)

        # Union
        print("Union A U B :", setA | setB)

        # Union
        print("Union A U C:", setA | setC)

        # Interseccion
        print("Interseccion A n B:", setA & setB)

        # Interseccion
        print("Interseccion A n C:", setA & setC)

        # (A  C)
        print("S-(A & C) :", S - (setA & setC))

        print('=' * 45)
        print('¿Deseas realizar un diagrama de Venn?')
        print('1. Si')
        print('2. No')
        opt = input()

        if opt == "1":
            print('Gracias, que tenga buen dia. Pulse cualquier tecla para continuar')
            input()
            venn3([setA, setB, setC], ('A', 'B', 'C'))
            plt.show()
        else:
            print('Gracias, que tenga buen dia. Pulse cualquier tecla para continuar')
            input()
    else:
        print('No reconozco tu operación.')
