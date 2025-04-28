numeros = [5, 2, 9, 1, 5, 6]
# Ordenar la lista de menor a mayor
numeros.sort()
print(numeros)
# Ordenar la lista de mayor a menor
numeros.sort(reverse=True)
print(numeros)
# Sorted devuelve una nueva lista sin alterar la original
sorted(numeros)


usuarios = [[4, "Chanchito"], [1, "Melvin"], [3, "Wolfgang"]]
# Esta funcion define la posicion en el indice por la que se va a ordenar
# En este caso se ordena por el primer elemento de la lista


def ordenar(elemento):
    return elemento[0]


# Ordenar la lista de menor a mayor
usuarios.sort(key=ordenar)

# Esta funcion es una forma mas corta de hacer lo mismo, pero con expresiones lambda,
# es una manera de reducir el codigo y no tener que crear una funcion aparte.
# PD: Solo usar cuando la funcion es muy corta y no va a ser usada en otros puntos del codigo.
usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
