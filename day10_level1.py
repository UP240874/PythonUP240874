# Usando un bucle for
for i in range(11):
    print(i)

# Usando un bucle while
i = 0
while i <= 10:
    print(i)
    i += 1


# 2 Usando un bucle for (de 10 hasta 0)
for i in range(10, -1, -1):
    print(i)

#  Usando un bucle while
i = 10
while i >= 0:
    print(i)
    i -= 1

# 3 Usamos un bucle para construir línea por línea
for i in range(1, 8):
    print('#' * i)


# 4 Dos bucles: uno para las filas y otro para las columnas
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()  # Salto de línea al final de cada fila

#5 Imprime i x i = i*i para i del 0 al 10
for i in range(11):
    print(f"{i} x {i} = {i * i}")


# 6Recorremos e imprimimos cada elemento de la lista
tecnologias = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in tecnologias:
    print(item)

#7 Verificamos si el número es par usando i % 2 == 0
for i in range(101):
    if i % 2 == 0:
        print(i)


#8 Verificamos si el número es impar usando i % 2 != 0
for i in range(101):
    if i % 2 != 0:
        print(i)

