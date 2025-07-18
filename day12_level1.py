import random
import string

# 1. Generar un ID aleatorio de 6 caracteres
def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print("ID aleatorio:", random_user_id())

# 2. Generar múltiples IDs personalizados por el usuario
def user_id_gen_by_user():
    caracteres = int(input("Número de caracteres por ID: "))
    cantidad = int(input("Cantidad de IDs a generar: "))
    for _ in range(cantidad):
        print(''.join(random.choices(string.ascii_letters + string.digits, k=caracteres)))

# Descomenta para probar:
# user_id_gen_by_user()

# 3. Generar un color RGB aleatorio
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print("Color RGB aleatorio:", rgb_color_gen())




