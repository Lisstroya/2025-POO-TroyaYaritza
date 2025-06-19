# Clase que representa un producto en la tienda
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"


# Clase que representa el carrito de compras del cliente
class CarritoDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto agregado: {producto}")

    def mostrar_carrito(self):
        if not self.productos:
            print("El carrito está vacío.")
        else:
            print("Productos en el carrito:")
            for p in self.productos:
                print(f" - {p}")

    def calcular_total(self):
        total = sum(p.precio for p in self.productos)
        return total


# Clase que representa al cliente
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = CarritoDeCompras()

    def comprar(self, producto):
        self.carrito.agregar_producto(producto)

    def ver_carrito(self):
        self.carrito.mostrar_carrito()

    def ver_total(self):
        total = self.carrito.calcular_total()
        print(f"Total a pagar: ${total:.2f}")


# Uso simulado del sistema
if __name__ == "__main__":
    # Crear productos disponibles
    prod1 = Producto("Camiseta", 17.99)
    prod2 = Producto("Pantalón", 28.50)
    prod3 = Producto("Zapatos", 75.00)

    # Crear un cliente
    cliente1 = Cliente("Lisseth")

    # Interacción del cliente con la tienda
    cliente1.comprar(prod1)
    cliente1.comprar(prod2)
    cliente1.comprar(prod3)
 
    cliente1.ver_carrito()
    cliente1.ver_total()