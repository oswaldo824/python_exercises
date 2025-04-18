saludo = "Hola global"
# En este caso, la variable saludo es global, por lo que no se puede acceder a ella desde dentro de la funcion


def saludar():
    saludo = "Hola"
    print(saludo)  # imprime la variable saludo que esta dentro de la funcion


def saludar_perro():
    saludo = "Guau"
    print(saludo)  # imprime la variable saludo que esta dentro de la funcion

# Es mala practica usar variables globales, es recomendable siempre usar variables locales, ya que si no se puede perder el control de las variables y es mas complicado depurar el codigo
# se pueden usar variables globales, pero es recomendable no hacerlo


# def saludar_gato():
#    global saludo  # le decimos que la variable saludo es global
#    saludo = "Miau"  # cambia el valor de la variable saludo
#    print(saludo)  # imprime la variable saludo que esta dentro de la funcion
saludar()
saludar_perro()
print(saludo)  # imprime la variable saludo que esta fuera de la funcion
