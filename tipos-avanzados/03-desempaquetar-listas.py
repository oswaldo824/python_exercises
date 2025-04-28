numeros = [1, 2, 3]

primero, segundo, tercero = numeros
print(primero, segundo, tercero)
# Desempaquetar listas
primero, *otros, tercero = numeros
# otros contiene todos los elementos de la lista, salvo el primero o los que yo defina aparte
print(primero, otros, tercero)
#
