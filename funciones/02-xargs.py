def suma(*numeros):  # con el asterisco le decimos que puede recibir un numero indefinido de argumentos
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 4, 8, 9, 7, 5, 6, 3, 2, 1)
