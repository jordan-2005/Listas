class Libro:
    """Representa un libro con atributos inmutables y categorías."""

    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos una tupla para autor y título: son datos que no cambian.
        self.info_inmutable = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info_inmutable[0]} por {self.info_inmutable[1]} (Categoría: {self.categoria})"


class Usuario:
    """Representa a un usuario y su registro de préstamos."""

    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para gestionar libros prestados (permite añadir/quitar fácilmente).
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    """Gestiona la lógica principal de libros, usuarios y préstamos."""

    def __init__(self):
        # Diccionario para búsqueda eficiente por ISBN {isbn: objeto_libro}.
        self.libros_disponibles = {}
        # Conjunto para asegurar que los IDs de usuario sean únicos.
        self.usuarios_registrados = set()
        # Diccionario auxiliar para guardar objetos Usuario {id: objeto_usuario}.
        self.datos_usuarios = {}

    # --- Gestión de Libros ---
    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro añadido: {libro}")
        else:
            print("Error: El libro ya existe en el sistema.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Error: Libro no encontrado.")

    # --- Gestión de Usuarios ---
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.datos_usuarios[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario.nombre}")
        else:
            print("Error: El ID de usuario ya está en uso.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)
            del self.datos_usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} eliminado.")
        else:
            print("Error: Usuario no registrado.")

    # --- Préstamos y Devoluciones ---
    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros_disponibles and id_usuario in self.usuarios_registrados:
            libro = self.libros_disponibles.pop(isbn)  # Quitar de disponibles
            usuario = self.datos_usuarios[id_usuario]
            usuario.libros_prestados.append(libro)  # Añadir a lista del usuario
            print(f"Libro '{libro.info_inmutable[0]}' prestado a {usuario.nombre}.")
        else:
            print("Error: Préstamo no posible (verifique ISBN o ID de usuario).")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.datos_usuarios:
            usuario = self.datos_usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro  # Volver a disponibles
                    print(f"Libro '{libro.info_inmutable[0]}' devuelto exitosamente.")
                    return
            print("Error: El usuario no tiene este libro prestado.")
        else:
            print("Error: Usuario no encontrado.")

    # --- Búsquedas ---
    def buscar_libro(self, criterio, valor):
        """Busca por título, autor o categoría."""
        encontrados = []
        for libro in self.libros_disponibles.values():
            if valor.lower() in str(libro).lower():
                encontrados.append(libro)

        if encontrados:
            print(f"\nResultados de búsqueda para '{valor}':")
            for lib in encontrados: print(f"- {lib}")
        else:
            print(f"No se encontraron libros con {criterio}: {valor}")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.datos_usuarios:
            user = self.datos_usuarios[id_usuario]
            print(f"\nLibros actuales de {user.nombre}:")
            for lib in user.libros_prestados: print(f"- {lib}")
        else:
            print("Usuario no encontrado.")


# --- PRUEBAS DEL SISTEMA ---
mi_biblioteca = Biblioteca()

# 1. Crear Libros
l1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo Mágico", "978-01")
l2 = Libro("1984", "George Orwell", "Distopía", "978-02")
l3 = Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "978-03")

# 2. Añadir Libros
mi_biblioteca.añadir_libro(l1)
mi_biblioteca.añadir_libro(l2)
mi_biblioteca.añadir_libro(l3)

# 3. Registrar Usuarios
u1 = Usuario("Ana López", "USR001")
u2 = Usuario("Carlos Ruiz", "USR002")
mi_biblioteca.registrar_usuario(u1)
mi_biblioteca.registrar_usuario(u2)

# 4. Realizar Préstamos
mi_biblioteca.prestar_libro("978-01", "USR001")  # Ana se lleva el de Gabo
mi_biblioteca.prestar_libro("978-02", "USR001")  # Ana se lleva 1984

# 5. Listar libros prestados
mi_biblioteca.listar_libros_prestados("USR001")

# 6. Buscar un libro
mi_biblioteca.buscar_libro("Categoría", "Infantil")

# 7. Devolución
mi_biblioteca.devolver_libro("978-01", "USR001")