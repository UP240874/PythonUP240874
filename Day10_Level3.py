#ejercicios 3

import countries
import countries_data


paises_con_land = [pais for pais in countries.countries if 'land' in pais]
print("Países que contienen 'land':", paises_con_land)

# Invertir una lista de frutas usando un bucle
frutas = ['banana', 'orange', 'mango', 'lemon']
frutas_invertidas = []

for i in range(len(frutas) - 1, -1, -1):
    frutas_invertidas.append(frutas[i])

print("Lista de frutas invertida:", frutas_invertidas)

# Calcular el número total de idiomas únicos
idiomas = set()

for pais in countries_data.countriesdata:
    for idioma in pais['languages']:
        idiomas.add(idioma)

print("Número total de idiomas:", len(idiomas))

# Encontrar los 10 idiomas más hablados
from collections import Counter

contador_idiomas = Counter()

for pais in countries_data.countriesdata:
    contador_idiomas.update(pais['languages'])

idiomas_mas_hablados = contador_idiomas.most_common(10)
print("10 idiomas más hablados:")
for idioma, cantidad in idiomas_mas_hablados:
    print(f"{idioma}: {cantidad} países")

# Encontrar los 10 países más poblados
paises_mas_poblados = sorted(countries_data.countriesdata, key=lambda x: x['population'], reverse=True)[:10]

print("10 países más poblados:")
for pais in paises_mas_poblados:
    print(f"{pais['name']} - {pais['population']}")

