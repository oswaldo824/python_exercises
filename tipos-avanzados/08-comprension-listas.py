# Utilizando la comprension de listas se pueden crear otras listas a partir de otras listas
# Se puede hacer una lista de comprensión para crear una lista de nombres a partir de una lista de usuarios

usuarios = [["Chanchito", 4], ["Melvin", 1], ["Wolfgang", 3]]

# nombre = []
# for usuario in usuarios:
#     nombre.append(usuario[0])
# print(nombre)

# Map
# De esta manera se puede hacer una lista de comprensión
nombre = [usuario[0] for usuario in usuarios]

# Filter
# Para filtrar la lista
nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# Map y Filter
# Para filtrar y transformar la lista
nombres2 = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# Usando la funcion map
# Se puede usar la funcion map para transformar la lista
nombre3 = list(map(lambda usuario: usuario[0], usuarios))

# Se puede usar la funcion filter para filtrar la lista
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
