import tkinter as tk
from tkinter import messagebox

# Función para agregar un dato a la lista
def agregar_dato():
    dato = entrada.get()
    if dato.strip() != "":
        lista.insert(tk.END, dato)  # Se añade al final de la lista
        entrada.delete(0, tk.END)   # Borrar el contenido del campo de entrada
    else:
        messagebox.showwarning("Advertencia", "Debe ingresar un texto válido.")

# Función para limpiar todos los datos de la lista
def limpiar_lista():
    lista.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Registro de Informacion")
ventana.geometry("400x300")

# Etiqueta
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack(pady=5)

# Campo de entrada de texto
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

# Botón para agregar el dato ingresado a la lista
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

# Listbox para mostrar datos
lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=5)

# Botón Limpiar
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()