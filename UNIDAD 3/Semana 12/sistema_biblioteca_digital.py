import json
import os

# Clase que representa un libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos tupla para atributos inmutables
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.info[0]}' de {self.info[1]} | Categoría: {self.categoria} | ISBN: {self.isbn}"

# Clase que representa un usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # lista de libros

    def __str__(self):
        return f"Usuario: {self.nombre} | ID: {self.id_usuario} | Libros prestados: {len(self.libros_prestados)}"

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # clave = ISBN, valor = objeto Libro
        self.usuarios = {}  # clave = ID usuario, valor = objeto Usuario
        self.ids_usuarios = set()  # asegurar IDs únicos

#Funcionalidades
# Añadir/quitar libros
    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print("El libro ha sido registrado.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            print(f"Libro eliminado: {libro}")
        else:
            print("Libro no encontrado.")

 # Registrar/dar de baja usuarios
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("Ese ID ya está en uso.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario}")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario dado de baja: {usuario.nombre}")
        else:
            print("Usuario no encontrado.")

# Prestar/devolver libros
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        if isbn not in self.libros:
            print("Libro no disponible.")
            return
        usuario = self.usuarios[id_usuario]
        libro = self.libros.pop(isbn)
        usuario.libros_prestados.append(libro)
        print(f"Libro prestado: {libro.info[0]} a {usuario.nombre}")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        usuario = self.usuarios[id_usuario]
        libro_a_devolver = None
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                libro_a_devolver = libro
                break
        if libro_a_devolver:
            usuario.libros_prestados.remove(libro_a_devolver)
            self.libros[isbn] = libro_a_devolver
            print(f"Libro devuelto: {libro_a_devolver.info[0]} por {usuario.nombre}")
        else:
            print("El usuario no tiene prestado ese libro.")

# Buscar libros (por titulo, autor o categoria)
    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.libros.values() if libro.info[0].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros.values() if libro.info[1].lower() == autor.lower()]

    def buscar_por_categoria(self, categoria):
        return [libro for libro in self.libros.values() if libro.categoria.lower() == categoria.lower()]

# Listar libros prestados
    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        usuario = self.usuarios[id_usuario]
        if not usuario.libros_prestados:
            print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print(f"Libros prestados por {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f"  - {libro}")

 #Guardar y cargar en Json
    def guardar_datos(self, archivo_libros="libros.json", archivo_usuarios="usuarios.json"):
        # Guardar libros disponibles
        libros_data = {isbn: {
            "titulo": libro.info[0],
            "autor": libro.info[1],
            "categoria": libro.categoria,
            "isbn": libro.isbn
        } for isbn, libro in self.libros.items()}
        with open(archivo_libros, "w", encoding="utf-8") as f:
            json.dump(libros_data, f, indent=4)

 # Guardar usuarios y sus libros prestados (por ISBN)
        usuarios_data = {}
        for id_usuario, usuario in self.usuarios.items():
            usuarios_data[id_usuario] = {
                "nombre": usuario.nombre,
                "id_usuario": usuario.id_usuario,
                "libros_prestados": [libro.isbn for libro in usuario.libros_prestados]
            }
        with open(archivo_usuarios, "w", encoding="utf-8") as f:
            json.dump(usuarios_data, f, indent=4)

    def cargar_datos(self, archivo_libros="libros.json", archivo_usuarios="usuarios.json"):
        if os.path.exists(archivo_libros):
            with open(archivo_libros, "r", encoding="utf-8") as f:
                libros_data = json.load(f)
                for isbn, data in libros_data.items():
                    libro = Libro(data["titulo"], data["autor"], data["categoria"], data["isbn"])
                    self.libros[isbn] = libro

        if os.path.exists(archivo_usuarios):
            with open(archivo_usuarios, "r", encoding="utf-8") as f:
                usuarios_data = json.load(f)
                for id_usuario, data in usuarios_data.items():
                    usuario = Usuario(data["nombre"], data["id_usuario"])
                    for isbn in data["libros_prestados"]:
                        if isbn in self.libros:
                            libro = self.libros.pop(isbn)
                            usuario.libros_prestados.append(libro)
                    self.usuarios[id_usuario] = usuario
                    self.ids_usuarios.add(id_usuario)

# Menú interactivo
def menu():
    biblioteca = Biblioteca()
    biblioteca.cargar_datos()

    while True:
        print("\n===== 📚 MENÚ BIBLIOTECA DIGITAL =====")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados")
        print("9. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.añadir_libro(libro)

        elif opcion == "2":
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID único: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == "5":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":
            print("Buscar por: 1) Título  2) Autor  3) Categoría")
            sub = input("Elige: ")
            if sub == "1":
                titulo = input("Título: ")
                resultados = biblioteca.buscar_por_titulo(titulo)
            elif sub == "2":
                autor = input("Autor: ")
                resultados = biblioteca.buscar_por_autor(autor)
            else:
                categoria = input("Categoría: ")
                resultados = biblioteca.buscar_por_categoria(categoria)
            if resultados:
                print("Resultados:")
                for libro in resultados:
                    print("  -", libro)
            else:
                print("No se encontraron libros.")

        elif opcion == "8":
            id_usuario = input("ID del usuario: ")
            biblioteca.listar_libros_prestados(id_usuario)

        elif opcion == "9":
            biblioteca.guardar_datos()
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
