#ejrcicios 2
# Calcular la suma de todos los números del 0 al 100
suma_total = 0
for i in range(101):
    suma_total += i
print("La suma de todos los números es", suma_total)

# Calcular la suma de los pares y la suma de los impares del 0 al 100
suma_pares = 0
suma_impares = 0

for i in range(101):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i

print("La suma de todos los pares es", suma_pares)
print("La suma de todos los impares es", suma_impares)

