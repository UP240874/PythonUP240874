# Suma de dos números
def add_two_numbers(a, b):
    return a + b

# Área de un círculo (π * r * r)
def area_of_circle(radio):
    pi = 3.1416
    return pi * radio * radio

# Suma de argumentos arbitrarios (verifica que todos sean números)
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    return "Todos los elementos deben ser números."

# Convertir de Celsius a Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Determinar estación según mes
def check_season(mes):
    mes = mes.lower()
    if mes in ['diciembre', 'enero', 'febrero']:
        return 'Invierno'
    elif mes in ['marzo', 'abril', 'mayo']:
        return 'Primavera'
    elif mes in ['junio', 'julio', 'agosto']:
        return 'Verano'
    elif mes in ['septiembre', 'octubre', 'noviembre']:
        return 'Otoño'
    else:
        return 'Mes no válido'

# Calcular la pendiente (y2 - y1) / (x2 - x1)
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# Resolver ecuación cuadrática ax² + bx + c = 0
import cmath
def solve_quadratic_eqn(a, b, c):
    d = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + d) / (2*a)
    x2 = (-b - d) / (2*a)
    return x1, x2

# Imprimir cada elemento de una lista
def print_list(lista):
    for item in lista:
        print(item)

# Invertir una lista usando bucles
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# Variante 2 del reverse
def reverse_list1(arr):
    return reverse_list(arr)

# Capitalizar los elementos de una lista
def capitalize_list_items(items):
    return [item.capitalize() for item in items]

# Agregar un elemento al final de una lista
def add_item(lista, item):
    lista.append(item)
    return lista

# Eliminar un elemento de una lista
def remove_item(lista, item):
    if item in lista:
        lista.remove(item)
    return lista

# Sumar todos los números hasta el número dado
def sum_of_numbers(n):
    return sum(range(n + 1))

# Sumar solo los impares hasta el número dado
def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

# Sumar solo los pares hasta el número dado
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)

#ejercicio 2
# Contar pares e impares desde 0 hasta un número
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = n + 1 - evens
    print(f"La cantidad de pares es {evens}.")
    print(f"La cantidad de impares es {odds}.")

# Calcular el factorial de un número
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Verificar si una variable está vacía
def is_empty(param):
    return not bool(param)

# Funciones estadísticas
from statistics import mean, median, mode, pstdev, variance

def calculate_mean(lista):
    return mean(lista)

def calculate_median(lista):
    return median(lista)

def calculate_mode(lista):
    return mode(lista)

def calculate_range(lista):
    return max(lista) - min(lista)

def calculate_variance(lista):
    return variance(lista)

def calculate_std(lista):
    return pstdev(lista)


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
from data.countries_data import countries_data  # Asegúrate de tener el archivo

def most_spoken_languages(top_n=10):
    lang_counter = Counter()
    for country in countries_data:
        lang_counter.update(country['languages'])
    return lang_counter.most_common(top_n)

# Países más poblados del mundo
def most_populated_countries(top_n=10):
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:top_n]




