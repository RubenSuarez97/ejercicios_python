'''
Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje. 
Utiliza operaciones de inserción, borrado, actualización y y ordenación.
'''
# Lista
# Creación
my_list: list = ['Rojo', 'Azul', 'Verde'] 
print(my_list) # ['Rojo', 'Azul', 'Verde']
# Inserción
my_list.append('Amarillo')
print(my_list) # ['Rojo', 'Azul', 'Verde', 'Amarillo']
# acceso
print(my_list[1]) # 'Azul'
# Eliminar
my_list.remove('Rojo')
print(my_list) # ['Azul', 'Verde', 'Amarillo']
# Actualización
my_list[1] = 'Negro' 
print(my_list) # ['Azul', 'Negro', 'Amarillo']
# Ordenar
my_list.sort() 
print(my_list) # ['Amarillo', 'Azul', 'Negro']

#----------------------------------------------------------------------------------------------------------------------

# Tuplas
# Creación
my_tuple: tuple = ('Fresa', 'Manzana', 'Pera')
print(my_tuple) # ('Fresa', 'Manzana', 'Pera')
# Inserción
my_tuple = my_tuple + ('Naranja',)
print(my_tuple) # ('Fresa', 'Manzana', 'Pera', 'Naranja')
# acceso
print(my_tuple[1]) # 'Manzana'

#----------------------------------------------------------------------------------------------------------------------

# Sets
# Creación
my_set: set = {'Rojo', 'Azul', 'Verde'}
print(my_set) # {'Rojo', 'Azul', 'Verde'}
# Inserción
my_set.add('Amarillo')
print(my_set) # {'Rojo', 'Azul', 'Verde', 'Amarillo'}
# Borrado
my_set.remove('Rojo')
print(my_set) # {'Azul', 'Verde', 'Amarillo'}

#----------------------------------------------------------------------------------------------------------------------

# Diccionario
# Creación
my_dict: dict = {
    'name': 'Jesus',
    'surname': 'Perez',
    'alias': '@Jesus2p',
    'age':23
}
print(my_dict) # {'name': 'Jesus', 'surname': 'Perez', 'alias': '@Jesus2p', 'age': 23}
# Inserción
my_dict['email'] = 'jesus@p.com'
print(my_dict) # {'name': 'Jesus', 'surname': 'Perez', 'alias': '@Jesus2p', 'age': 23, 'email': 'jesus@p.com'}
# acceso 
print(my_dict['name']) # Jesus
# Eliminar
del my_dict['alias']
print(my_dict) # {'name': 'Jesus', 'surname': 'Perez', 'age': 23, 'email': 'jesus@p.com'}
# ordenar
my_dict = dict(sorted(my_dict.items()))
print(my_dict)

#----------------------------------------------------------------------------------------------------------------------

contactos = {
    'nombres': [],
    'teléfonos' : []
}
x = 3

for i in range(x):
    if i < x:
        print('Ingrese los datos del usuario', i + 1)
        nombre = input('Ingrese nombre del usuario: ')
        teléfono = int(input('Ingrese el numero de teléfono del usuario: '))

        contactos['nombres'].append(nombre)

        contactos['teléfonos'].append(teléfono)

for i in range(x):
    print(f'Nombre de usuario {i + 1}')
    print('Nombre', contactos['nombres'][i])
    print('Teléfono', contactos['teléfonos'][i])
    
print(contactos)