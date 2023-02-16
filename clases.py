class Persona: 
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    def saluda(self, otra_persona):
        return f'hola {otra_persona.nombre}, me llamo {self.nombre}'

david = Persona('David', 34)
erika = Persona('Erika', 42)

print(david.saluda(erika))