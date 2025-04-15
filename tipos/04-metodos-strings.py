animal = "  Gato feliz   "
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())
print(animal.title())
print(animal.find("feliz"))  # Devuelve el indice, cuando es -1 no lo encuentra
print(animal.replace("feliz", "triste"))
# Devuelve si encuentra el caracter o cadena por medio de un booleano
print("feliz" in animal)
