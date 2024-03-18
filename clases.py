# nueva clase

class Persona:
    def __init__ (self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def Saludar(self):
        print(f"Hola {self.nombre} {self.apellido}")    
        
    @property
    def edad(self):
        return self._age

    @edad.setter
    def edad(self, new_age):
        if new_age < 0:
            raise ValueError("La edad no puede ser negativa")
        self._age = new_age
        
        
persona1 = Persona("Alberto", "Saleh", 44)

print(persona1.nombre)
print(persona1.apellido)
persona1.Saludar()

try:
    persona1.edad = -10
except Exception as e:
    print(e)
