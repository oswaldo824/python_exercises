# En esta linea , el argumento apellido es opcional, si paso un argumento desde un llamado al metodo, tomara el que le pase en vez del que tiene por defecto, en este caso "feliz"
def hola(nombre, apellido="feliz"):
    print("Hola, mundo!")
    print(f"Bienvenido {nombre} {apellido}")


hola("Oswaldo")
