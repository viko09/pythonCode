# Objetos: Tienen caracteristicas y viven dentro de las clases
# Clases: Definen las características de los objetos
class Estudiante:
    def __init__(self, nombre, apellido, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso


# Self es una instancia, cuando se crea una nueva instancia usando la clase, el comando self indica que lo que se crea
# es una variable de la instancia

# init es un modulo que inicia nuestra instancia
estudiante1 = Estudiante('Adriana', 'Rojas', 'Python')
estudiante2 = Estudiante('Victor', 'Luna', 'Data Science')

print(estudiante1)
