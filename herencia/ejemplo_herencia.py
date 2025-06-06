class Vehiculo:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad

    def info(self):
        print(f"Marca: {self.marca}")
        print(f"Velocidad: {self.velocidad} km/h")


class Moto(Vehiculo):
    def __init__(self, marca, velocidad, cilindrada):
        super().__init__(marca, velocidad)
        self.cilindrada = cilindrada

    def info(self):
        super().info()
        print(f"Cilindrada: {self.cilindrada} cc")


mi_moto = Moto("Shineray", 180, 260)
mi_moto.info()