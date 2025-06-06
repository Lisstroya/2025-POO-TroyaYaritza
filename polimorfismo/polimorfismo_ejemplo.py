class Persona:
    def hablar(self):
        print("Hola, soy una persona.")

class Profesor(Persona):
    def hablar(self):
        print("Holaa chicos, soy el profesor.")

class Estudiante(Persona):
    def hablar(self):
        print("Hola, soy el nuevo estudiante.")

personas = [Persona(), Profesor(), Estudiante()]

for p in personas:
    p.hablar()

