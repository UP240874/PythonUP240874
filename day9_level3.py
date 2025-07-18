#LEVEL 3
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Verificar existencia de 'skills' y obtener la habilidad media
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])

# Verificar si sabe Python
    has_python = 'Python' in skills
    print("Has Python skill:", has_python)

# Título según habilidades
    if set(skills) == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif {'Node', 'MongoDB', 'Python'}.issubset(skills):
        print("He is a backend developer")
    elif {'React', 'Node', 'MongoDB'}.issubset(skills):
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# Verificar si está casado y vive en Finlandia
if person['is_marred'] and person['country'] == 'Finland':
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name} lives in Finland. He is married.")