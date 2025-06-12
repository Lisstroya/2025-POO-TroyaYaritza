# Cálculo del promedio semanal del clima - POO

class Climasemanal:
    def __init__(self):
        # Lista de temperaturas fijas para cada día de la semana
        self.temperaturas = [26, 27, 33, 29, 31, 30, 27]

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas) # Calcula el promedio de la lista de temperaturas

    def mostrar_resultados(self): # Imprime la lista de temperaturas y el promedio calculado
        print("Programación Orientada a Objetos (POO)")
        print("Temperaturas:", self.temperaturas)
        print(f"Promedio semanal: {self.calcular_promedio():.2f} °C")

# Crear un objeto de la clase Climasemanal y mostrar resultados
if __name__ == "__main__":
    clima = Climasemanal()
    clima.mostrar_resultados()