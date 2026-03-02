import json


# --- CLASE PRODUCTO ---
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Método para facilitar la impresión del objeto
    def __str__(self):
        return f"ID: {self.id:<5} | Nombre: {self.nombre:<15} | Cantidad: {self.cantidad:<8} | Precio: ${self.precio:.2f}"


# --- CLASE INVENTARIO ---
class Inventario:
    def __init__(self):
        # Usamos un DICCIONARIO para búsqueda rápida por ID (Complejidad O(1))
        self.productos = {}
        self.nombre_archivo = "inventario_data.txt"
        # Al iniciar, cargamos los datos previos si existen
        self.cargar_datos()

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            print(f"\n[!] Error: El ID {producto.id} ya existe.")
        else:
            self.productos[producto.id] = producto
            print(f"\n[+] Producto '{producto.nombre}' añadido con éxito.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            eliminado = self.productos.pop(id_producto)
            print(f"\n[-] Producto '{eliminado.nombre}' eliminado.")
        else:
            print("\n[!] Error: No se encontró un producto con ese ID.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].cantidad = nueva_cantidad
            if nuevo_precio is not None:
                self.productos[id_producto].precio = nuevo_precio
            print("\n[*] Producto actualizado correctamente.")
        else:
            print("\n[!] Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        # Usamos una LISTA para filtrar productos que coincidan
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            print(f"\n--- Resultados para '{nombre}' ---")
            for p in encontrados:
                print(p)
        else:
            print(f"\n[!] No se encontraron productos con el nombre: {nombre}")

    def mostrar_inventario(self):
        if not self.productos:
            print("\n[i] El inventario está vacío.")
        else:
            print("\n" + "=" * 50)
            print(f"{'ID':<5} | {'NOMBRE':<15} | {'STOCK':<8} | {'PRECIO'}")
            print("-" * 50)
            for p in self.productos.values():
                print(p)
            print("=" * 50)

    # --- PERSISTENCIA DE DATOS ---
    def guardar_datos(self):
        try:
            # Convertimos el diccionario de objetos a un formato serializable (JSON)
            datos_serializables = {id_p: vars(p) for id_p, p in self.productos.items()}
            with open(self.nombre_archivo, "w") as f:
                json.dump(datos_serializables, f, indent=4)
            print("\n[OK] Datos guardados en archivo.")
        except Exception as e:
            print(f"\n[!] Error al guardar: {e}")

    def cargar_datos(self):
        try:
            with open(self.nombre_archivo, "r") as f:
                datos = json.load(f)
                for id_p, info in datos.items():
                    # Reconstruimos los objetos Producto a partir del diccionario cargado
                    self.productos[id_p] = Producto(info['id'], info['nombre'], info['cantidad'], info['precio'])
        except (FileNotFoundError, json.JSONDecodeError):
            # Si el archivo no existe o está corrupto, empezamos con inventario vacío
            self.productos = {}


# --- INTERFAZ DE USUARIO ---
def mostrar_menu():
    mi_inventario = Inventario()

    while True:
        print("\n--- GESTIÓN DE INVENTARIO AVANZADO ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad/precio")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todo el inventario")
        print("6. Guardar y Salir")

        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            try:
                id_p = input("ID único: ")
                nom = input("Nombre del producto: ")
                cant = int(input("Cantidad inicial: "))
                prec = float(input("Precio unitario: "))
                mi_inventario.añadir_producto(Producto(id_p, nom, cant, prec))
            except ValueError:
                print("\n[!] Error: Cantidad y Precio deben ser valores numéricos.")

        elif opcion == "2":
            id_p = input("Ingrese el ID del producto a eliminar: ")
            mi_inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("ID del producto a modificar: ")
            print("Deje en blanco si no desea modificar el campo.")
            c = input("Nueva cantidad: ")
            p = input("Nuevo precio: ")

            # Solo enviamos el valor si el usuario escribió algo
            mi_inventario.actualizar_producto(
                id_p,
                int(c) if c.strip() else None,
                float(p) if p.strip() else None
            )

        elif opcion == "4":
            nom = input("Nombre a buscar: ")
            mi_inventario.buscar_por_nombre(nom)

        elif opcion == "5":
            mi_inventario.mostrar_inventario()

        elif opcion == "6":
            mi_inventario.guardar_datos()
            print("Saliendo del sistema... ¡Hasta pronto!")
            break
        else:
            print("\n[!] Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    mostrar_menu()