grade = float(input('Proporciona un valor entre 0 y 10: '))

if 0 <= grade < 6:
    letter = 'F'
elif 6 <= grade < 7:
    letter = 'D'
elif 7 <= grade < 8:
    letter = 'C'
elif 8 <= grade < 9:
    letter = 'B'
elif 9 <= grade <= 10:
    letter = 'A'
else:
    letter = "Valor Desconocido"

print(letter)
