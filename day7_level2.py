#nivel 2
# Definimos dos conjuntos A y B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 28, 27}

# 1. Unir los conjuntos A y B
print("Unión de A y B:", A.union(B))

# 2. Encontrar la intersección de A y B
print("Intersección de A y B:", A.intersection(B))

# 3. Verificar si A es subconjunto de B
print("¿A es subconjunto de B?", A.issubset(B))

# 4. Verificar si A y B son conjuntos disjuntos
print("¿A y B son disjuntos?", A.isdisjoint(B))

# 5. Unir A con B y B con A (es lo mismo, la unión es conmutativa)
print("Unión A ∪ B:", A.union(B))
print("Unión B ∪ A:", B.union(A))

# 6. Diferencia simétrica (elementos que están en A o B pero no en ambos)
print("Diferencia simétrica:", A.symmetric_difference(B))

# 7. Eliminar completamente los conjuntos
del A
del B
