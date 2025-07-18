# level 2 Desempaquetar siblings y padres de family_members
family_members = ['irma ', 'victor', 'wanda', 'lexcy']

# Unpacking
mother, father, sister1, sister2 = family_members

print("Padres:", mother, "y", father)
print("Hermanas:", sister1, "y", sister2)


# Crear tuplas de frutas, verduras y productos animales
fruits = ('Mango', 'Kiwi')
vegetables = ('Papa', 'Brócoli')
animal_products = ('Huevo', 'Queso')

# Unir las tres tuplas en una sola
food_stuff_tp = fruits + vegetables + animal_products

# Convertir la tupla a lista
food_stuff_lt = list(food_stuff_tp)

# Sacar el ítem o ítems del medio
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1:middle_index + 1]
else:
    middle_items = [food_stuff_lt[middle_index]]

# Sacar los primeros tres y últimos tres elementos
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

# Eliminar completamente la tupla food_stuff_tp
del food_stuff_tp

# Verificar si un ítem está en una tupla
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

'Estonia' in nordic_countries
'Iceland' in nordic_countries
