# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self._edad} años."

    def obtener_rol(self):
        return "Soy una persona."


# Clase derivada(herencia)
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Polimorfismo: sobrescribir metodo
    def obtener_rol(self):
        return f"Soy estudiante de la carrera de {self.carrera}."


# Clase derivada (herencia)
class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    # Polimorfismo
    def obtener_rol(self):
        return f"Soy profesor de la asignatura de {self.asignatura}."


# Función principal para probar las clases
def main():
    estudiante1 = Estudiante("Lisseth", 20, "Tecnologias de la Informacion")
    profesor1 = Profesor("Ing. Carlos Cedeño", 42, "Física")

    personas = [estudiante1, profesor1]

    for persona in personas:
        print(persona.presentarse())
        print(persona.obtener_rol())
        print("-" * 40)


# Ejecutar el programa
if __name__ == "__main__":
    main()