# Set significa grupo o conjunto
# Un set es una colección de elementos únicos, no ordenados y mutables

primer = {1, 1, 2, 2, 3, 4, 5}
segundoSet = [3, 4, 5]
segundoSet = set(segundoSet)

print(primer | segundoSet)  # Unión de sets
print(primer & segundoSet)  # Intersección de sets
print(primer - segundoSet)  # Diferencia de sets
print(primer ^ segundoSet)  # Diferencia simétrica de sets
# Diferencia simétrica: elementos que están en uno de los sets pero no en ambos

# Con los sets no se puede acceder a los elementos por índice
