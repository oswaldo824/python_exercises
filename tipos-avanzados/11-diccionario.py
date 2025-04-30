# Coleccion de datos por llave y valor
punto = {"x": 25, "y": 50}
print(punto["x"])  # Acceso a un elemento por su llave

punto["x"] = 100  # Modificación de un elemento

# El método get() devuelve None si la llave no existe
print(punto.get("x"))  # Acceso a un elemento por su llave

del (punto["x"])  # Eliminar un elemento por su llave


usuarios = [{"id": 1, "nombre": "Chanchito"}]
#
