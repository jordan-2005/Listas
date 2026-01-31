import os
import subprocess
import platform
from pathlib import Path


class DashboardPOO:
    """
    Clase principal para la gestión y ejecución de proyectos de Programación
    Orientada a Objetos. Automatiza la navegación y visualización de scripts.
    """

    def __init__(self):
        # Usamos Path para que funcione en Windows, Mac y Linux sin errores de barras / o \
        self.ruta_base = Path(__file__).parent
        self.unidades = {
            '1': 'Unidad 1',
            '2': 'Unidad 2'
        }

    def limpiar_pantalla(self):
        """Detecta el sistema operativo y limpia la consola."""
        os.system('cls' if platform.system() == 'Windows' else 'clear')

    def leer_codigo(self, ruta):
        """Extrae el contenido de un archivo con manejo de errores robusto."""
        try:
            return ruta.read_text(encoding='utf-8')
        except Exception as e:
            return f"Error al leer el archivo: {e}"

    def ejecutar_script(self, ruta):
        """Lanza el script en una terminal independiente para no bloquear el dashboard."""
        try:
            if platform.system() == 'Windows':
                subprocess.Popen(['cmd', '/k', 'python', str(ruta)])
            else:
                # Intenta abrir en sistemas Unix (requiere xterm o similar)
                subprocess.Popen(['xterm', '-hold', '-e', 'python3', str(ruta)])
        except Exception as e:
            print(f"No se pudo ejecutar el script: {e}")

    def mostrar_menu(self):
        """Bucle principal de la interfaz de usuario."""
        while True:
            self.limpiar_pantalla()
            print("\n" + "=" * 30)
            print("  SISTEMA GESTOR - POO")
            print("=" * 30)

            for key, nombre in self.unidades.items():
                print(f"[{key}] - {nombre}")
            print("[0] - Salir")

            eleccion = input("\nSeleccione una opción: ")

            if eleccion == '0':
                print("Finalizando sistema...")
                break
            elif eleccion in self.unidades:
                self.gestionar_sub_menu(self.ruta_base / self.unidades[eleccion])
            else:
                input("Opción inválida. Presione Enter para reintentar...")

    def gestionar_sub_menu(self, ruta_unidad):
        """Navega por las subcarpetas de la unidad seleccionada."""
        if not ruta_unidad.exists():
            input(f"Error: La carpeta {ruta_unidad.name} no existe. Enter para volver...")
            return

        sub_carpetas = [f for f in ruta_unidad.iterdir() if f.is_dir()]

        while True:
            self.limpiar_pantalla()
            print(f"\n--- SUBMENÚ: {ruta_unidad.name} ---")
            for i, carpeta in enumerate(sub_carpetas, 1):
                print(f"{i}. {carpeta.name}")
            print("0. Regresar")

            opcion = input("\nSeleccione carpeta: ")
            if opcion == '0': break

            try:
                indice = int(opcion) - 1
                if 0 <= indice < len(sub_carpetas):
                    self.gestionar_scripts(sub_carpetas[indice])
            except ValueError:
                pass

    def gestionar_scripts(self, ruta_carpeta):
        """Muestra y permite ejecutar archivos .py."""
        scripts = list(ruta_carpeta.glob("*.py"))

        while True:
            self.limpiar_pantalla()
            print(f"\n--- SCRIPTS EN: {ruta_carpeta.name} ---")
            for i, script in enumerate(scripts, 1):
                print(f"{i}. {script.name}")
            print("0. Volver")

            opcion = input("\nSeleccione archivo: ")
            if opcion == '0': break

            try:
                idx = int(opcion) - 1
                if 0 <= idx < len(scripts):
                    script_sel = scripts[idx]
                    print(f"\n--- CONTENIDO: {script_sel.name} ---\n")
                    print(self.leer_codigo(script_sel))

                    if input("\n¿Ejecutar? (s/n): ").lower() == 's':
                        self.ejecutar_script(script_sel)
                    input("\nPresione Enter para continuar...")
            except ValueError:
                pass


# Punto de entrada del programa
if __name__ == "__main__":
    app = DashboardPOO()
    app.mostrar_menu()
