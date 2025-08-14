class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self): return self.id_producto
    def get_nombre(self): return self.nombre
    def get_cantidad(self): return self.cantidad
    def get_precio(self): return self.precio

    def set_nombre(self, nombre): self.nombre = nombre
    def set_cantidad(self, cantidad): self.cantidad = cantidad
    def set_precio(self, precio): self.precio = precio

    def __str__(self):
        return f"{self.id_producto:<8} | {self.nombre:<20} | {self.cantidad:^8} | ${self.precio:<8.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print( "ID ya existente.")
                return
        self.productos.append(producto)
        print("Producto agregado.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None: p.set_cantidad(cantidad)
                if precio is not None: p.set_precio(precio)
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
            return
        print("\nID       | Nombre  | Cantidad | Precio")
        print("-" * 50)
        for p in self.productos:
            print(p)