import tkinter as tk
from tkinter import messagebox


class AppGestionDatos:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Información V1.0")
        self.root.geometry("400x450")

        # --- Componentes GUI ---

        # 1. Etiqueta de instrucción
        self.label_instruccion = tk.Label(root, text="Ingrese un nuevo elemento:", font=("Arial", 10))
        self.label_instruccion.pack(pady=10)

        # 2. Campo de texto (Entry)
        self.entrada_texto = tk.Entry(root, width=40)
        self.entrada_texto.pack(pady=5)

        # 3. Contenedor para botones (Frame para alineación horizontal)
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=15)

        self.btn_agregar = tk.Button(self.frame_botones, text="Agregar", command=self.agregar_item, bg="#4CAF50",
                                     fg="white", width=10)
        self.btn_agregar.pack(side=tk.LEFT, padx=5)

        self.btn_limpiar = tk.Button(self.frame_botones, text="Limpiar Lista", command=self.limpiar_lista, bg="#f44336",
                                     fg="white", width=10)
        self.btn_limpiar.pack(side=tk.LEFT, padx=5)

        # 4. Lista para mostrar datos (Listbox) con su Scrollbar
        self.label_lista = tk.Label(root, text="Elementos guardados:", font=("Arial", 10, "bold"))
        self.label_lista.pack()

        self.lista_datos = tk.Listbox(root, width=50, height=10)
        self.lista_datos.pack(pady=10, padx=20)

    # --- Lógica y Manejo de Eventos ---

    def agregar_item(self):
        """Toma el texto del Entry y lo añade a la Listbox."""
        texto = self.entrada_texto.get().strip()  # .strip() elimina espacios vacíos extra

        if texto:
            self.lista_datos.insert(tk.END, texto)  # Inserta al final de la lista
            self.entrada_texto.delete(0, tk.END)  # Limpia el campo de entrada
        else:
            messagebox.showwarning("Campo vacío", "Por favor, escribe algo antes de agregar.")

    def limpiar_lista(self):
        """Borra todos los elementos de la lista visual."""
        confirmacion = messagebox.askyesno("Confirmar", "¿Deseas vaciar toda la lista?")
        if confirmacion:
            self.lista_datos.delete(0, tk.END)


# --- Ejecución de la aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = AppGestionDatos(root)
    root.mainloop()