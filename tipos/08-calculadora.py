n1 = input("Digite un primer número: ")
n2 = input("Digite un segundo número: ")

n1 = int(n1)  # Convertir a entero
n2 = int(n2)  # Convertir a entero

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

mensaje = f"""Para los numeros {n1} y {n2}:
Suma: {suma}
Resta: {resta}
Multiplicacion: {multiplicacion}
Division: {division}"""

print(mensaje)
