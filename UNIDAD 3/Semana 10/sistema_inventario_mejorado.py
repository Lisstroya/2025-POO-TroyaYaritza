import json
import os

# Clase que representa un producto
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

# Clase inventario mejorada
class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_desde_archivo()  # Cargar productos desde JSON al iniciar

 # Métodos para manejar productos
    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("ID ya existente.")
            return
        self.productos[producto.get_id()] = producto
        self.guardar_en_archivo()
        print("Producto agregado y guardado en el archivo inventario.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            self.productos.pop(id_producto)
            self.guardar_en_archivo()
            print("Producto eliminado y cambios guardados.")
        else:
            print("El producto no fue encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            p = self.productos[id_producto]
            if cantidad is not None:
                p.set_cantidad(cantidad)
            if precio is not None:
                p.set_precio(precio)
            self.guardar_en_archivo()
            print("Producto actualizado y cambios guardados.")
        else:
            print("El producto no fue encontrado.")

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
            return
        print("\nID       | Nombre        | Cantidad         | Precio")
        print("-" * 50)
        for p in self.productos.values():
            print(p)

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                lista = [{"id": p.get_id(), "nombre": p.get_nombre(),
                          "cantidad": p.get_cantidad(), "precio": p.get_precio()}
                         for p in self.productos.values()]
                json.dump(lista, f, indent=4)
        except PermissionError:
            print("Error: No se puede escribir en el archivo.")
        except Exception as e:
            print(f"Ocurrió un error al guardar: {e}")


    def cargar_desde_archivo(self):
        if not os.path.exists(self.archivo):
            with open(self.archivo, "w") as f:
                json.dump([], f)
            return
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                for item in data:
                    producto = Producto(item["id"], item["nombre"], item["cantidad"], item["precio"])
                    self.productos[producto.get_id()] = producto
        except json.JSONDecodeError:
            self.productos = {}
        except Exception as e:
            print(f"Ocurrió un error al cargar: {e}")

# Menú de usuario
def menu():
    inventario = Inventario()

    while True:
        print("\n" + "=" * 18)
        print("SISTEMA INVENTARIO")
        print("=" * 18)
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad o precio del producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        print("=" * 18)

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            try:
                id_p = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(Producto(id_p, nombre, cantidad, precio))
            except ValueError:
                print("Error: Cantidad y precio deben ser numéricos.")

        elif opcion == "2":
            inventario.eliminar_producto(input("ID del producto a eliminar: "))

        elif opcion == "3":
            id_p = input("ID del producto a actualizar: ")
            try:
                c = input("Nueva cantidad (Enter para no cambiar): ")
                p = input("Nuevo precio (Enter para no cambiar): ")
                nueva_cantidad = int(c) if c else None
                nuevo_precio = float(p) if p else None
                inventario.actualizar_producto(id_p, nueva_cantidad, nuevo_precio)
            except ValueError:
                print("Error: Cantidad y precio deben ser numéricos.")

        elif opcion == "4":
            nombre = input("Nombre o parte del nombre: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                print("\nID       | Nombre      | Cantidad       | Precio")
                print("-" * 50)
                for prod in resultados:
                    print(prod)
            else:
                print("Producto no coincide. Intenta nuevamente")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo...")
            break

if __name__ == "__main__":
    menu()
