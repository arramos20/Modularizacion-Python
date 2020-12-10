class Persona():
    def __init__(self, nombre, apellidos):
        self.nombre=nombre,
        self.apellidos=apellidos

class Empleado(Persona):

    def __init__(self, nombre, apellidos, sueldo):
        super().__init__(nombre, apellidos) #Manera 1 (Para herencia simple normalmente)
        self.sueldo=sueldo #Manera 2 (Hace lo mismo que la frase de arriba

    def __str__(self):
        return f"{self.nombre} {self.apellidos} Sueldo: {self.sueldo}"
