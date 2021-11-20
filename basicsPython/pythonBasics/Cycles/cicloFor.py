chain = 'Hello'

for letra in chain:
    print(letra)
else:
    print('End of For Cycle')


for letra in 'Holanda':
    if letra == 'a':
        print(f'I found: {letra}')
        # If we just want 1 letter, use break
        break

# --------------------------------------------------
for i in range(6):
    if i % 2 == 0:
        print(f'Valor: {i}')

print('\n')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')
