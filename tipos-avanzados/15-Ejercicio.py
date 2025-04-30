# 1. Eliminar los espacios en blanco de un string y devolver una lista con los caracteres restantes


cadenas = "hola mundo bonito"


def eliminar_espacios(texto):
    lista = []
    for cadena in cadenas:
        if cadena != " ":
            lista.append(cadena)
    return lista


# print(eliminar_espacios(cadenas))

# 2. Contar en un diccionario cuántas veces aparece cada letra en un string


def contar_letras(texto):
    contador = {}  # Diccionario para contar cada letra
    for letra in texto:
        if letra != " ":  # Ignorar espacios
            if letra in contador:
                contador[letra] += 1  # Incrementar el valor existente
            else:
                contador[letra] = 1  # Inicializar el conteo
    return contador


# print(contar_letras(cadenas))

# 3. Odenar las llaves de un diccionario por el valor que tienen y devolver una lista que contiene tuplas


def ordenar_diccionario(diccionario):
    diccionario = {}
    for cadena in cadenas:
        if cadena != " ":
            diccionario[cadena] = cadena
    # Ordenar el diccionario por valor
    diccionario_ordenado = sorted(diccionario.items(), key=lambda x: x[1])
    return diccionario_ordenado


# print(ordenar_diccionario(cadenas))

# 4. De un listado de tuplas , devolver las tuplas que tengan el mayor valor


def mayor_tuplas():
    tuplas = [(1, 2), (3, 4), (5, 6), (7, 8)]
    mayor = max(tuplas, key=lambda x: x[1])
    return mayor


print(mayor_tuplas())

# 5. Crear un mensaje que diga : "Los caracteres que mas se repiten con x repeticiones son:"


def mensaje_repeticiones(texto):
    contador = contar_letras(texto)
    max_repeticiones = max(contador.values())
    caracteres_mas_repetidos = [letra for letra, repeticiones in contador.items(
    ) if repeticiones == max_repeticiones]
    return f"Los caracteres que más se repiten con {max_repeticiones} repeticiones son: {', '.join(caracteres_mas_repetidos)}"


print(mensaje_repeticiones(cadenas))
