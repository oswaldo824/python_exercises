def es_palindromo(texto):
    texto = quitar_espacios(texto)
    texto_al_reves = reverse(texto)
    return texto == texto_al_reves


def quitar_espacios(texto):
    cadena = texto.replace(" ", "").lower()
    return cadena


def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


print(es_palindromo("Hola mundo"))
print(es_palindromo("La ruta natural"))
