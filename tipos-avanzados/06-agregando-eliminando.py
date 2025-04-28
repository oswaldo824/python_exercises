mascotas = ["Pelusa", "Pulga", "Felipe",
            "Pulga", "Chanchito feliz", "Wolfgang"]

# Agregar elementos a la lista de acuerdo al indice que seleccionemos
mascotas.insert(1, "Melvin")
# Agregar elementos al final de la lista
mascotas.append("Chanchito Triste")
# Elimina la primera coincidencia de la lista
mascotas.remove("Pulga")
# Elimina ultimo elemento de la lista, o el que se le indique en el indice
mascotas.pop()
# Elimina el primer elemento de la lista o lo que indiquemos en el indice
del mascotas[0]
# Elimina todos los elementos de la lista
mascotas.clear()

print(mascotas)
