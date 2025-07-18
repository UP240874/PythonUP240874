#LEVEL3
import random
import string
# 7. Función que revuelve aleatoriamente una lista
def shuffle_list(lista):
    lista_copia = lista.copy()
    random.shuffle(lista_copia)
    return lista_copia

mi_lista = [1, 2, 3, 4, 5, 6, 7]
print("Lista mezclada:", shuffle_list(mi_lista))

# 8. Función que devuelve 7 números únicos aleatorios entre 0 y 9
def unique_random_numbers():
    return random.sample(range(10), 7)

print("7 números únicos aleatorios:", unique_random_numbers())
