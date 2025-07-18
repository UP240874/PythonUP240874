#NIVEL 3
# 1. Convertir una lista de edades en conjunto y comparar longitudes
edades = [22, 19, 24, 25, 26, 24, 25, 24]
edades_set = set(edades)
print("Longitud de la lista:", len(edades))
print("Longitud del conjunto:", len(edades_set))
print("El conjunto es más corto porque elimina duplicados")

# 2. Diferencia entre tipos de datos:
"""
string (cadena): secuencia de caracteres, inmutable. Ej: "Hola"
list (lista): colección ordenada y mutable. Ej: [1, 2, 3]
tuple (tupla): colección ordenada e inmutable. Ej: (1, 2, 3)
set (conjunto): colección no ordenada, mutable y sin elementos duplicados. Ej: {1, 2, 3}
"""

# 3. Contar palabras únicas en una oración
frase = "I am a teacher and I love to inspire and teach people"
palabras = frase.split()            # Dividimos la oración en palabras
palabras_unicas = set(palabras)     # Eliminamos duplicados usando set
print("Palabras únicas:", palabras_unicas)
print("Número de palabras únicas:", len(palabras_unicas))