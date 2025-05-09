class Perro:
    def __init__(self, nombre, edad):
        # Constructor de la clase Perro
        # Se ejecuta al crear una instancia de la clase
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau")


mi_perro = Perro("Toby", 10)
mi_perro.habla()
