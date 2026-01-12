"""
Programa: Simulador de Gestión de Biblioteca
Funcionalidad: Calcula el costo de una multa por retraso en la entrega de un libro
               y verifica si el usuario tiene permiso para nuevos préstamos.
"""


def calcular_multa_biblioteca(dias_retraso, costo_por_dia):
    """
    Calcula el total de la multa multiplicando los días por el costo unitario.
    """
    # Realizamos una operación matemática simple: multiplicación
    total_multa = dias_retraso * costo_por_dia
    return total_multa


def main():
    # --- Identificadores y Tipos de Datos ---

    # String (Cadena de texto): Nombre del libro
    titulo_libro = "Cien años de soledad"

    # Integer (Entero): Días que el usuario se pasó de la fecha límite
    dias_atraso = 5

    # Float (Flotante): Precio de la multa por cada día de retraso
    tarifa_diaria = 1.50

    # Boolean (Booleano): Estado de la cuenta del usuario
    cuenta_activa = True

    # --- Lógica del Programa ---

    # Calculamos la multa llamando a nuestra función
    monto_total = calcular_multa_biblioteca(dias_atraso, tarifa_diaria)

    # Mostramos los resultados en consola
    print(f"--- Recibo de Biblioteca ---")
    print(f"Libro: {titulo_libro}")
    print(f"Días de retraso: {dias_atraso}")
    print(f"Total a pagar: ${monto_total}")

    # Verificamos una condición lógica
    if monto_total > 0 and cuenta_activa:
        print("Estado: Usted tiene una deuda pendiente, pero su cuenta sigue activa.")
    else:
        print("Estado: Sin deudas pendientes.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()