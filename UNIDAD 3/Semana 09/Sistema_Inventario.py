from Clases_producto_Inventario import Producto, Inventario

def menu():
    inventario = Inventario()

    while True:
        print("\n" + "=" * 24)
        print("SISTEMA INVENTARIO")
        print("=" * 24)
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad o precio del producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        print("=" * 24)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_p = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(Producto(id_p, nombre, cantidad, precio))
            except ValueError:
                print(" Ya existe un producto con ese ID.")

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
                print("\nID       | Nombre | Cantidad | Precio")
                print("-" * 50)
                for prod in resultados:
                    print(prod)
            else:
                print("Ningun producto coincide con la busqueda. Intenta de nuevo")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print(" Saliendo...")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    menu()