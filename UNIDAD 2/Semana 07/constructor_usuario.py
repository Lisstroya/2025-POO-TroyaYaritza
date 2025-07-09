# Este ejemplo muestra cómo se utiliza  el constructor (_init_) en una clase en Python.

class Usuario:
    def __init__(self, nombre, edad):
        """
        Constructor que se ejecuta automáticamente al crear un objeto.
        Inicializa los atributos 'nombre' y 'edad'.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"[+] Usuario creado: {self.nombre}, {self.edad} años")

    def saludar(self):
        """Metodo para saludar al usuario."""
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Código principal (solo se ejecuta si el archivo es ejecutado directamente)
if __name__ == "__main__":
    usuario1 = Usuario("Lisseth", 20)
    usuario1.saludar()