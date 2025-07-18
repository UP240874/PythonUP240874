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




