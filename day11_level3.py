#ejerccicio 3
# Verificar si un número es primo
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Verificar si todos los elementos son únicos
def are_items_unique(lista):
    return len(lista) == len(set(lista))

# Verificar si todos los elementos son del mismo tipo
def are_same_type(lista):
    return all(type(i) == type(lista[0]) for i in lista)

# Verificar si una variable es un nombre válido en Python
def is_valid_variable(name):
    return name.isidentifier()

# Idiomas más hablados del mundo

from collections import Counter

import countries
import countries_data
def most_spoken_languages(top_n=10):
    lang_counter = Counter()
    for country in countries_data:
        lang_counter.update(country['languages'])
    return lang_counter.most_common(top_n)

# Países más poblados del mundo
def most_populated_countries(top_n=10):
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:top_n]
