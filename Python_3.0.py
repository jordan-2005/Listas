# ==========================================
# 1. DEFINICIÓN DEL MODELO DE DATOS
# ==========================================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters y Setters (Encapsulamiento)
    @property
    def id(self): return self._id

    @property
    def nombre(self): return self._nombre

    @property
    def cantidad(self): return self._cantidad

    @cantidad.setter
    def cantidad(self, valor): self._cantidad = max(0, int(valor))

    @property
    def precio(self): return self._precio

    @precio.setter
    def precio(self, valor): self._precio = max(0.0, float(valor))

    def __str__(self):
        return f"ID: {self._id:03} | {self._nombre[:15]:<15} | Cant: {self._cantidad:>3} | Precio: ${self._precio:>8.2f}"


# ==========================================
# 2. LÓGICA DEL SISTEMA (CONTROLADOR)
# ==========================================
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Regla de negocio: ID único
        if any(p.id == producto.id for p in self.productos):
            return False
        self.productos.append(producto)
        return True

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.id == id_producto:
                self.productos.remove(p)
                return True
        return False

    def actualizar_producto(self, id_p, n_cant=None, n_prec=None):
        for p in self.productos:
            if p.id == id_p:
                if n_cant is not None: p.cantidad = n_cant
                if n_prec is not None: p.precio = n_prec
                return True
        return False

    def buscar_por_nombre(self, termino):
        return [p for p in self.productos if termino.lower() in p.nombre.lower()]

    def mostrar_todo(self):
        if not self.productos:
            print("\n>>> Inventario vacío.")
        else:
            print(f"\n{'ID':<5} | {'NOMBRE':<15} | {'CANT':<4} | {'PRECIO':<9}")
            print("-" * 45)
            for p in self.productos:
                print(p)


# ==========================================
# 3. INTERFAZ DE USUARIO Y FLUJO PRINCIPAL
# ==========================================
def ejecutar_sistema():
    sistema = Inventario()

    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Añadir | 2. Eliminar | 3. Actualizar | 4. Buscar | 5. Ver Todo | 6. Salir")
        opcion = input("Seleccione (1-6): ")

        try:
            if opcion == "1":
                id_i = int(input("ID (numérico): "))
                nom = input("Nombre: ")
                can = int(input("Cantidad: "))
                pre = float(input("Precio: "))
                if sistema.agregar_producto(Producto(id_i, nom, can, pre)):
                    print("✔ Producto añadido.")
                else:
                    print("✘ Error: El ID ya existe.")

            elif opcion == "2":
                id_i = int(input("ID a eliminar: "))
                if sistema.eliminar_producto(id_i):
                    print("✔ Producto eliminado.")
                else:
                    print("✘ No se encontró el ID.")

            elif opcion == "3":
                id_i = int(input("ID del producto: "))
                print("(Enter para omitir cambio)")
                c_in = input("Nueva cantidad: ")
                p_in = input("Nuevo precio: ")

                # Conversión opcional
                c = int(c_in) if c_in else None
                p = float(p_in) if p_in else None

                if sistema.actualizar_producto(id_i, c, p):
                    print("✔ Actualizado con éxito.")
                else:
                    print("✘ Producto no encontrado.")

            elif opcion == "4":
                nom = input("Nombre a buscar: ")
                resultados = sistema.buscar_por_nombre(nom)
                if resultados:
                    for r in resultados: print(r)
                else:
                    print("✘ No hay coincidencias.")

            elif opcion == "5":
                sistema.mostrar_todo()

            elif opcion == "6":
                print("Finalizando programa...")
                break
            else:
                print("Opción inválida.")

        except ValueError:
            print("⚠ Error: Por favor, introduce datos válidos.")


if __name__ == "__main__":
    ejecutar_sistema()