# 1. Declarar una lista vacía
lista_vacia = []

# 2. Declarar una lista con más de 5 elementos
frutas = ['manzana', 'plátano', 'mango', 'uva', 'kiwi', 'piña']

# 3. Obtener la longitud de la lista
print("Longitud de la lista:", len(frutas))

# 4. Obtener el primer, medio y último elemento de la lista
print("Primer elemento:", frutas[0])
print("Elemento del medio:", frutas[len(frutas)//2])
print("Último elemento:", frutas[-1])

# 5. Lista con datos personales
mixed_data_types = ['Andrea', 18, 1.73, 'Soltera', 'Peñuelas 101']
print("Datos personales:", mixed_data_types)

# 6. Declarar lista de empresas tecnológicas
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("Empresas de tecnología:", it_companies)

# 7. Imprimir el número de empresas
print("Número de empresas:", len(it_companies))

# 8. Imprimir la primera, media y última empresa
print("Primera empresa:", it_companies[0])
print("Empresa del medio:", it_companies[len(it_companies)//2])
print("Última empresa:", it_companies[-1])

# 9. Modificar una empresa
it_companies[2] = 'Meta'
print("Lista modificada:", it_companies)

# 10. Agregar una empresa al final
it_companies.append('Tesla')
print("Lista con nueva empresa:", it_companies)

# 11. Insertar empresa en la mitad
it_companies.insert(len(it_companies)//2, 'Adobe')
print("Lista con empresa insertada:", it_companies)

# 12. Convertir una empresa a mayúsculas (excepto IBM)
it_companies[1] = it_companies[1].upper()
print("Empresa en mayúsculas:", it_companies)

# 13. Unir empresas con un separador
empresas_unidas = '#; '.join(it_companies)
print("Empresas unidas:", empresas_unidas)

# 14. Verificar si existe una empresa
print("¿Existe 'Oracle'? ->", 'Oracle' in it_companies)

# 15. Ordenar la lista alfabéticamente
it_companies.sort()
print("Lista ordenada:", it_companies)

# 16. Invertir la lista en orden descendente
it_companies.reverse()
print("Lista invertida:", it_companies)

# 17. Cortar las primeras 3 empresas
print("Primeras 3 empresas:", it_companies[:3])

# 18. Cortar las últimas 3 empresas
print("Últimas 3 empresas:", it_companies[-3:])

# 19. Cortar empresa(s) del medio
medio = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    print("Empresas del medio:", it_companies[medio-1:medio+1])
else:
    print("Empresa del medio:", it_companies[medio])

# 20. Eliminar la primera empresa
it_companies.pop(0)
print("Sin la primera empresa:", it_companies)

# 21. Eliminar empresa del medio
it_companies.pop(len(it_companies)//2)
print("Sin empresa del medio:", it_companies)

# 22. Eliminar la última empresa
it_companies.pop()
print("Sin la última empresa:", it_companies)

# 23. Eliminar todas las empresas
it_companies.clear()
print("Lista vacía:", it_companies)

# 24. Eliminar por completo la lista
del it_companies

# 25. Unir listas de frontend y backend
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print("Stack completo:", full_stack)

# 26. Insertar Python y SQL después de Redux
index_redux = full_stack.index('Redux')
full_stack.insert(index_redux + 1, 'Python')
full_stack.insert(index_redux + 2, 'SQL')
print("Stack actualizado:", full_stack)
