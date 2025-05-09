# Las funciones usan snake_case y dentro de la clase pasan a llamarse metodos
# Las clases usan PascalCase

class Perro:
    def habla(self):  # Siempre para poder llamar a un metodo de una clase se usa self
        print("Guau guau")


mi_perro = Perro()
print(type(mi_perro))
mi_perro.habla()  # Llamamos al metodo habla de la clase Perro
print(isinstance(mi_perro, Perro))
# isinstance() devuelve True si el objeto es una instancia de la clases
