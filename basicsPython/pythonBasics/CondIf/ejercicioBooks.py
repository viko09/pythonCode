nombre = input("Ingrese el nombre del libro: ")
idlibro = int(input("Ingrese el ID del libro: "))
precio = float(input("Ingrese el precio del libro: "))

envio = input("¿El envio es gratuito? (Si/No)")
if envio == "Si":
    envio = "Si"
elif envio == "No":
    envio = "No"
else:
    while envio != "Si" and envio != "No":
        print("Es necesario ingresar 'Si' o 'No'.")
        envio = input("¿El envio es gratuito? (Si/No)")

print('='*45)

print(f'''
    Nombre: {nombre}
    ID: {idlibro}
    Precio: {precio}
    Envio Gratuito? {envio}
''')
