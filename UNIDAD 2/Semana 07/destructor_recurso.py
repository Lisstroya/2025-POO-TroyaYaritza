# Este ejemplo muestra cómo se utiliza el destructor (_del_) en una clase en Python.

class Recurso:
    def __init__(self, nombre):
        """
        Constructor que simula la apertura de un recurso.
        """
        self.nombre = nombre
        print(f"[+] Recurso '{self.nombre}' inicializado.")

    def usar(self):
        """Simula el uso del recurso."""
        print(f"Usando el recurso: {self.nombre}")

    def _del_(self):
        """
        Destructor que se ejecuta cuando el objeto es destruido.
        """
        print(f"[-] Recurso '{self.nombre}' ha sido eliminado.")

# Código principal
if __name__ == "__main__":
    recurso1 = Recurso("Archivo temporal")
    recurso1.usar()
    del recurso1  # Eliminamos manualmente para ver el mensaje del destructor
    print("Este recurso ha sido cerrado correctamente. ¡Fin del programa!")