# proyecto_poo.py

class Empleado:
    """Clase Base que demuestra Encapsulación y Herencia."""

    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        # Encapsulación: El atributo __salario_base es privado (double underscore)
        self.__salario_base = salario_base

    def obtener_salario(self):
        """Método para acceder al atributo privado (Getter)."""
        return self.__salario_base

    def calcular_pago(self):
        """Método que será sobrescrito (Polimorfismo)."""
        return self.__salario_base

    def __str__(self):
        return f"Empleado: {self.nombre}"


class Desarrollador(Empleado):
    """Clase Derivada que demuestra Herencia."""

    def __init__(self, nombre, salario_base, lenguaje):
        # Llamada al constructor de la clase base
        super().__init__(nombre, salario_base)
        self.lenguaje = lenguaje

    def calcular_pago(self):
        """Polimorfismo: Sobrescritura de método con un bono por especialidad."""
        bono_lenguaje = 500
        return self.obtener_salario() + bono_lenguaje

    def __str__(self):
        return f"Desarrollador: {self.nombre} (Lenguaje: {self.lenguaje})"


class Gerente(Empleado):
    """Otra clase derivada para reforzar Polimorfismo."""

    def calcular_pago(self):
        """Polimorfismo: Los gerentes tienen un bono del 20%."""
        return self.obtener_salario() * 1.20


# --- Demostración de Funcionalidad ---

if __name__ == "__main__":
    # Creación de instancias (Objetos)
    dev = Desarrollador("Ana García", 2500, "Python")
    jefe = Gerente("Carlos Pérez", 4000)

    # Lista de empleados para demostrar Polimorfismo en un ciclo
    empleados = [dev, jefe]

    print("--- Reporte de Pagos ---")
    for emp in empleados:
        # Aquí ocurre el Polimorfismo: se llama al mismo método 'calcular_pago'
        # pero cada objeto responde según su propia implementación.
        print(f"{emp} | Pago Total: ${emp.calcular_pago():.2f}")