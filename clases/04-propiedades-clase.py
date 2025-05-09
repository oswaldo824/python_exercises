class Perro:
    patas = 4  # Propiedad de clase

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau")


mi_perro = Perro("Toby", 10)
mi_perro.habla()
