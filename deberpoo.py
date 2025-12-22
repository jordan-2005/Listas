class Mascota:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.hambre = 50

    def mostrar_estado(self):
        print(f"{self.nombre} es un {self.especie} y su nivel de hambre es {self.hambre}.")

    def alimentar(self, cantidad):
        # Restamos la cantidad al hambre actual
        self.hambre = self.hambre - cantidad
        # Evitamos que el hambre sea menor a 0
        if self.hambre < 0:
            self.hambre = 0
        print(f"🍴 Has alimentado a {self.nombre}.")
mi_perro = Mascota("Saturno","Golden_Retrieve")
mi_perro.alimentar(20)
mi_perro.mostrar_estado()