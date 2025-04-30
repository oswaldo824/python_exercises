from collections import deque
# Las filas son FIFO (First In First Out)

# deque es una lista que permite añadir elementos al final y quitar del principio
# Se puede usar para implementar una cola
fila = deque([1, 2])
# Añadir elementos al final
fila.append(3)
fila.append(4)
fila.append(5)
print(fila)  # deque([1, 2, 3, 4, 5])
# Quitar elementos del principio
fila.popleft()
