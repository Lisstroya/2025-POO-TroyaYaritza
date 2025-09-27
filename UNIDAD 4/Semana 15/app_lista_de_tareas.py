import tkinter as tk
from tkinter import messagebox

# App Lista de Tareas

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LISTA DE TAREAS")
        self.root.geometry("500x400")

        # Campo de entrada para nuevas tareas
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)  # Permite presionar Enter para añadir tarea

        # Botones de control
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        add_btn = tk.Button(button_frame, text="Añadir Tarea", command=self.add_task)
        add_btn.grid(row=0, column=0, padx=5)

        complete_btn = tk.Button(button_frame, text="Marcar como Completada", command=self.complete_task)
        complete_btn.grid(row=0, column=1, padx=5)

        delete_btn = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)
        delete_btn.grid(row=0, column=2, padx=5)

        # Listbox para mostrar tareas
        self.task_listbox = tk.Listbox(root, width=60, height=25, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Permitir doble clic para marcar tarea como completada
        self.task_listbox.bind("<Double-Button-1>", self.complete_task)

        # Lista interna para manejar tareas
        self.tasks = []

    # Funciones de la aplicación
    def add_task(self, event=None):
        """Añade una nueva tarea a la lista"""
        task = self.entry.get().strip()
        if task != "":
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error, no puedes añadir una tarea vacía")

    def complete_task(self, event=None):
        """Marca una tarea como completada"""
        try:
            index = self.task_listbox.curselection()[0]
            task = self.tasks[index]

            # Si ya está completada, no la duplicamos
            if task.startswith("[✔] "):
                messagebox.showinfo("Esta tarea ya está completada")
            else:
                self.tasks[index] = "[✔] " + task
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, self.tasks[index])
        except IndexError:
            messagebox.showwarning("Selecciona una tarea para marcar como completada")

    def delete_task(self):
        """Elimina la tarea seleccionada"""
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks.pop(index)
            self.task_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()