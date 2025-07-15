# Dashboard de POO
# Este archivo permite navegar entre unidades, subcarpetas y ejecutar scripts seleccionados
import os
import subprocess

#Funcion para mostrar el codigo fuente en consola
def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        return None
    except Exception as e:
        print(f"Ocurrió un error. No es posible leer el archivo: {e}")
        return None
#Funcion para ejecutar un script .py
def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

#Funcion para crear un nuevo archivo vacio
def crear_nuevo_script(ruta):
    """
    Crea un nuevo archivo Python vacío con un encabezado básico.
    """
    nombre_script = input("Nombre del nuevo script (sin .py): ") + '.py'
    ruta_completa = os.path.join(ruta, nombre_script)
    if os.path.exists(ruta_completa):
        print("El archivo ya existe.")
    else:
        with open(ruta_completa, 'w') as f:
            f.write("# Nuevo script Python\n\n")
        print(f"Archivo {nombre_script} creado con éxito.")

#Funcion principal que muestra el menu de unidades
def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    # Unidades disponibles
    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    while True:
        print("Menu Principal - Archivo Dashboard")
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("\nElige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print( "Opción no válida. Intenta nuevamente.")

#Submenu para seleccionar subcarpetas dentro de una unidad
def mostrar_sub_menu(ruta_unidad):
    if not os.path.exists(ruta_unidad):
        print("Esta ruta no existe:", ruta_unidad)
        return

    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\n Submenú - Selecciona una subcarpeta")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                indice = int(eleccion_carpeta) - 1
                if 0 <= indice < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[indice]))
                else:
                    print("Opción no valida.")
            except ValueError:
                print("Entrada inválida. Debe ser un número.")

#Funcion que muestra los scripts Python de una subcarpeta seleccionada
def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\n Scripts - Opciones disponibles")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("8 - Crear nuevo script")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Selecciona una opción: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '8':
            return  # Regresa al menú principal
        elif eleccion_script == '9':
            crear_nuevo_script(ruta_sub_carpeta)
            scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]  # Actualiza la lista
        else:
            try:
                indice = int(eleccion_script) - 1
                if 0 <= indice < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Deseas ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se pudo ejecutar el script.")
                        else:
                            print("Opción no valida.")
                        input("Presiona Enter para continuar...")
                else:
                    print("Opción no valida.")
            except ValueError:
                print("Entrada invalida. Vuelve a intentarlo.")

# Punto de entrada del programa
if __name__ == "__main__":
    mostrar_menu()