def get_product(**datos):
    print(datos["apellido"])


get_product(nombre="Oswaldo", apellido="feliz", edad=30, ciudad="Quito")
# En este caso, el argumento **datos es un diccionario, por lo que puedo pasarle cualquier cantidad de argumentos y se guardaran en un diccionario
# Tener en cuenta que siempre se debe nombrar el argumento, ya que no se puede pasar sin nombre, como en el caso de los argumentos *args
