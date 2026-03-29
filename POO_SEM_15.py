import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas - Semana 15")
        self.root.geometry("400x450")

        # --- Interfaz Gráfica ---

        # Campo de entrada (Entry)
        self.task_entry = tk.Entry(root, font=("Arial", 12))
        self.task_entry.pack(pady=10, padx=10, fill=tk.X)

        # Evento de teclado: Presionar Enter para añadir tarea
        self.task_entry.bind('<Return>', lambda event: self.add_task())

        # Botones de acción
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        # Uso del argumento 'command' para vincular manejadores de eventos
        self.add_button = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task, bg="#4caf50", fg="white")
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(btn_frame, text="Marcar Completada", command=self.complete_task, bg="#2196f3",
                                         fg="white")
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task, bg="#f44336",
                                       fg="white")
        self.delete_button.grid(row=0, column=2, padx=5)

        # Lista de tareas (Listbox)
        self.tasks_listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Evento adicional: Doble clic para completar
        self.tasks_listbox.bind('<Double-1>', lambda event: self.complete_task())

    # --- Lógica de la Aplicación y Manejadores de Eventos ---

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Limpiar entrada
        else:
            messagebox.showwarning("Advertencia", "Debes escribir una tarea.")

    def complete_task(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            task = self.tasks_listbox.get(index)
            # Cambio visual: Añadir un prefijo de completado
            if not task.startswith("✔ "):
                self.tasks_listbox.delete(index)
                self.tasks_listbox.insert(index, f"✔ {task}")
                self.tasks_listbox.itemconfig(index, fg="gray")  # Cambiar color
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea para completar.")

    def delete_task(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()