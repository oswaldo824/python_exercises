buscar = 10

for numero in range(5):
    print(numero)
    if numero == buscar:
        print(f'encontrado en {numero}', buscar)
        break
else:
    print('no encontrado')
