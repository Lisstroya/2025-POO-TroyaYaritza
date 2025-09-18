"""
AGENDA PERSONAL
"""
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class AgendaApp:
    def __init__(self):
        # Crear ventana principal
        self.root = tk.Tk()
        self.root.title("Agenda Personal")
        self.root.geometry("700x500")
        self.root.configure(bg='#f0f0f0')

        # Lista para almacenar eventos
        self.eventos = []

        # Crear interfaz
        self.crear_widgets()

    def crear_widgets(self):
        """Crea todos los elementos de la interfaz"""
        # Frame principal (con padding)
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título
        titulo = ttk.Label(main_frame, text="📅 LISSETH TROYA - AGENDA PERSONAL ",
                           font=("Arial", 16, "bold"))
        titulo.pack(pady=10)

        # TreeView para mostrar eventos
        tree_frame = ttk.Frame(main_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Scrollbar para el TreeView
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        columnas = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(tree_frame, columns=columnas, show="headings",
                                 yscrollcommand=scrollbar.set, height=8)

        # Configurar headings
        self.tree.heading("fecha", text="FECHA")
        self.tree.heading("hora", text="HORA")
        self.tree.heading("descripcion", text="DESCRIPCIÓN")

        # Configurar tamaño de columnas
        self.tree.column("fecha", width=120, anchor=tk.CENTER)
        self.tree.column("hora", width=100, anchor=tk.CENTER)
        self.tree.column("descripcion", width=350, anchor=tk.W)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.tree.yview)

        # Frame para entrada de datos
        input_frame = ttk.LabelFrame(main_frame, text="NUEVO EVENTO", padding=10)
        input_frame.pack(fill=tk.X, pady=10)

        # Fila 1: Fecha y Hora
        fecha_hora_frame = ttk.Frame(input_frame)
        fecha_hora_frame.pack(fill=tk.X, pady=5)

        # Campo de fecha
        ttk.Label(fecha_hora_frame, text="Fecha (AAAA-MM-DD):",
                  font=("Arial", 9)).pack(side=tk.LEFT, padx=5)
        self.entry_fecha = ttk.Entry(fecha_hora_frame, width=15,
                                     font=("Arial", 9))
        self.entry_fecha.pack(side=tk.LEFT, padx=5)
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        self.entry_fecha.insert(0, fecha_actual)

        # Campo de hora
        ttk.Label(fecha_hora_frame, text="Hora (HH:MM):",
                  font=("Arial", 9)).pack(side=tk.LEFT, padx=5)
        self.entry_hora = ttk.Entry(fecha_hora_frame, width=8,
                                    font=("Arial", 9))
        self.entry_hora.pack(side=tk.LEFT, padx=5)
        self.entry_hora.insert(0, "12:00")

        # Fila 2: Descripción
        desc_frame = ttk.Frame(input_frame)
        desc_frame.pack(fill=tk.X, pady=5)

        ttk.Label(desc_frame, text="Descripción:",
                  font=("Arial", 9)).pack(side=tk.LEFT, padx=5)
        self.entry_desc = ttk.Entry(desc_frame, width=50,
                                    font=("Arial", 9))
        self.entry_desc.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        # Frame para botones
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=10)

        # Botones con colores y estilo
        style = ttk.Style()
        style.configure('Success.TButton', foreground='green')
        style.configure('Danger.TButton', foreground='red')

        ttk.Button(btn_frame, text="Agregar Evento",
                   command=self.agregar_evento,
                   style='Success.TButton').pack(side=tk.LEFT, padx=10)

        ttk.Button(btn_frame, text="Eliminar Evento",
                   command=self.eliminar_evento,
                   style='Danger.TButton').pack(side=tk.LEFT, padx=10)

        ttk.Button(btn_frame, text="Salir",
                   command=self.root.quit).pack(side=tk.LEFT, padx=10)

    def agregar_evento(self):
        """Agrega un nuevo evento a la agenda personal"""
        fecha = self.entry_fecha.get().strip()
        hora = self.entry_hora.get().strip()
        desc = self.entry_desc.get().strip()

        # Validar que los campos no estén vacíos
        if not fecha or not hora or not desc:
            messagebox.showerror("Error", "Por favor complete todos los campos")
            return

        # Validar formato de fecha (sencillo)
        if len(fecha) != 10 or fecha[4] != '-' or fecha[7] != '-':
            messagebox.showerror("Error", "Formato de fecha incorrecto. Use: AAAA-MM-DD")
            return

        # Validar formato de hora (sencillo)
        if len(hora) != 5 or hora[2] != ':':
            messagebox.showerror("Error", "Formato de hora incorrecto. Use: HH:MM")
            return

        # Agregar a la lista y al TreeView
        self.eventos.append((fecha, hora, desc))
        self.tree.insert("", tk.END, values=(fecha, hora, desc))

        # Limpiar campos
        self.entry_desc.delete(0, tk.END)
        messagebox.showinfo("Evento agregado correctamente")

    def eliminar_evento(self):
        """Elimina el evento seleccionado"""
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Seleccione un evento para eliminar")
            return

        # Obtener los valores del evento seleccionado
        evento = self.tree.item(seleccion[0], 'values')

        # Confirmar eliminación
        if messagebox.askyesno("Confirmar",
                               f"¿Estás seguro de eliminar el evento?\n"
                               f"Fecha: {evento[0]}\n"
                               f"Hora: {evento[1]}\n"
                               f"Descripción: {evento[2]}"):
            for item in seleccion:
                self.tree.delete(item)

    def run(self):
        """Ejecuta la aplicación"""
        self.root.mainloop()


# Ejecutar la aplicación
if __name__ == "__main__":
    app = AgendaApp()
    app.run()



