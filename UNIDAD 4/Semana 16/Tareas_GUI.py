import tkinter as tk
from tkinter import messagebox

class ListaDeTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("LISTA DE TAREAS PENDIENTES")
        self.root.geometry("500x400")

        # Campo de entrada para nueva tarea
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)
        self.entry.focus()

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        # Botón Añadir
        self.add_btn = tk.Button(btn_frame, text="Añadir", command=self.add_task,
                                 bg="#A8E6CF", fg="black", font=("Arial", 10, "bold"))
        self.add_btn.grid(row=0, column=0, padx=5)

        # Botón Completar
        self.complete_btn = tk.Button(btn_frame, text="Completar", command=self.complete_task,
                                      bg="#FFF9C4", fg="black", font=("Arial", 10, "bold"))
        self.complete_btn.grid(row=0, column=1, padx=5)

        # Botón Eliminar
        self.delete_btn = tk.Button(btn_frame, text="Eliminar", command=self.delete_task,
                                    bg="#FFD3B6", fg="black", font=("Arial", 10, "bold"))
        self.delete_btn.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=40, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Atajos de teclado
        self.task_listbox.bind("<c>", lambda event: self.complete_task())  # Presiona C para completar
        self.task_listbox.bind("<d>", lambda event: self.delete_task())  # Presiona D para eliminar
        self.task_listbox.bind("<Delete>", lambda event: self.delete_task())  # Supr
        root.bind("<Return>", lambda event: self.add_task())  # Enter siempre añade
        root.bind("<Escape>", lambda event: root.quit())  # Escape siempre cierra
    def add_task(self):
        task = self.entry.get().strip()
        if task:
            index = self.task_listbox.size()  # posición al final
            self.task_listbox.insert(tk.END, task)
            self.task_listbox.itemconfig(index, {'fg': 'black'})  # color normal
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "No puedes añadir una tarea vacía.")

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(index)

            if not task.startswith("✔ "):  # evita marcar varias veces
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, f"✔ {task}")
                self.task_listbox.itemconfig(index, {'fg': 'green'})  # tarea completada en verde
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeTareas(root)
    root.mainloop()