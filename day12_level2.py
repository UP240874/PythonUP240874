#LEVEL2
import random
import string
# 4. Función que devuelve una lista de colores en formato hexadecimal
def list_of_hexa_colors(cantidad):
    colores = []
    for _ in range(cantidad):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colores.append(color)
    return colores

print("Colores Hexa:", list_of_hexa_colors(3))

# 5. Función que devuelve una lista de colores RGB
def list_of_rgb_colors(cantidad):
    colores = []

    for _ in range(cantidad):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colores.append(f"rgb({r},{g},{b})")
    return colores

print("Colores RGB:", list_of_rgb_colors(3))

# 6. Función que puede generar colores en formato 'hexa' o 'rgb'
def generate_colors(tipo, cantidad):
    if tipo == 'hexa':
        return list_of_hexa_colors(cantidad)
    elif tipo == 'rgb':
        return list_of_rgb_colors(cantidad)
    else:
        return "Tipo inválido. Usa 'hexa' o 'rgb'."

print("Generar colores HEXA:", generate_colors('hexa', 2))
print("Generar colores RGB:", generate_colors('rgb', 2))