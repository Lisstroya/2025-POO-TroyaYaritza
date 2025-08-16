#Clase que representa un producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos Get (obtener valores)
    def get_id(self): return self.id_producto
    def get_nombre(self): return self.nombre
    def get_cantidad(self): return self.cantidad
    def get_precio(self): return self.precio

    # Métodos Set (modificar valores)
    def set_nombre(self, nombre): self.nombre = nombre
    def set_cantidad(self, cantidad): self.cantidad = cantidad
    def set_precio(self, precio): self.precio = precio

    # Representación en texto del producto
    def __str__(self):
        return f"{self.id_producto:<8} | {self.nombre:<20} | {self.cantidad:^8} | ${self.precio:<8.2f}"


# Clase que administra los productos (usando diccionario)
class Inventario:
    def __init__(self):
        self.productos = {}

    # Agregar producto
    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("ID ya existente.")
            return
        self.productos[producto.get_id()] = producto
        print("Producto agregado.")

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            self.productos.pop(id_producto)
            print("Producto eliminado.")
        else:
            print( "Producto no encontrado.")

    # Actualizar producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            p = self.productos[id_producto]
            if cantidad is not None:
                p.set_cantidad(cantidad)
            if precio is not None:
                p.set_precio(precio)
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    # Buscar por nombre
    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]

    # Mostrar todos
    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
            return
        print("\nID       | Nombre | Cantidad | Precio")
        print("-" * 50)
        for p in self.productos.values():
            print(p)