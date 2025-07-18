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