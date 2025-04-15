operacion = 0
print("Bienvenido a la calculadora")

while operacion != 5:

    print("""Seleccione la operacion deseada: ")      
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Salir""")

    operacion = int(input())

    if operacion == 5:
        print("Saliendo de la calculadora")
        break

    print("Ingrese el primer numero ")
    numero1 = int(input())
    print("Ingrese el segundo numero ")
    numero2 = int(input())

    if operacion == 1:
        resultado = numero1 + numero2
        print(f"El resultado de la suma es: {resultado} \n")
    elif operacion == 2:
        resultado = numero1 - numero2
        print(f"El resultado de la resta es: {resultado} \n")
    elif operacion == 3:
        resultado = numero1 * numero2
        print(f"El resultado de la multiplicacion es: {resultado} \n")
    elif operacion == 4:
        resultado = numero1 / numero2
        print(f"El resultado de la multiplicacion es: {resultado} \n")
    elif operacion == 5:
        print("Saliendo de la calculadora \n")
    else:
        print("Operacion no valida \n")
