# Definimos un conjunto de empresas de tecnología
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Obtener la longitud del conjunto
print("Longitud:", len(it_companies))

# 2. Agregar 'Twitter' al conjunto
it_companies.add('Twitter')
print("Después de agregar Twitter:", it_companies)

# 3. Agregar varias empresas al mismo tiempo
it_companies.update(['Spotify', 'Netflix', 'Intel'])
print("Después de agregar varias empresas:", it_companies)

# 4. Eliminar una empresa del conjunto
it_companies.remove('Oracle')  # Da error si 'Oracle' no existe
print("Después de eliminar Oracle:", it_companies)

# 5. Diferencia entre remove y discard:
# remove(): lanza un error si el elemento no existe en el conjunto
# discard(): NO lanza error si el elemento no está presente
it_companies.discard('Yahoo')  # No hace nada si 'Yahoo' no está


