#----------------------------------------Operaciones con cadenas de caracteres-------------------------------------------

python = '''Es un lenguaje de programación ampliamente utilizado en las aplicaciones
web, el desarrollo de software,la ciencia de datos entre otros.'''

print(python)

# Concatenación

nombre = 'Hola'
apellido = 'Python'

nombre_completo = nombre + apellido  # Hola python

print(nombre_completo)

# repetición 

print(nombre * 2) # HolaHola

# Indexation 

print(nombre[0] + nombre[1] + nombre[2] + nombre[3] )

# Longitud

print(len(nombre))

# Slicing (porción)

print(apellido[2:6]) # thon
print(apellido[2:]) # thon
print(apellido[0:2]) # Py
print(apellido[:2]) # Py

# Búsqueda 

print('o' in nombre) # True
print('k' in nombre) # False

# Reemplazo 

print(nombre.replace("H","R")) #Rola

# Division 

print(apellido.split("t")) # ['Py', 'hon']

# Mayúsculas y minúsculas

print(nombre.upper()) # HOLA
print(nombre.lower()) # hola
print('ruben suarez'.title()) # Ruben Suarez
print('ruben suarez'.capitalize()) # Ruben suarez

# eliminación de espacios al principio y al final

print(' Ruben suarez '.strip()) # elimina los espacios al principio y al final. 

# busqueda al principio y al final

print(nombre.startswith('Ho')) # True
print(nombre.startswith('py')) # False
print(nombre.endswith('la')) # True
print(nombre.endswith('ton')) # False

# Búsqueda de posición

print('Ruben Suarez Arismendi'.find('Suarez')) # la posición donde comienza la cadena 

# búsqueda de ocurrencias 

var_nueva = 'Aprendiendo python en casa'
print(var_nueva.lower().count('casa'))

# Formateo

print('saludos:{} lenguaje:{}'.format(nombre , apellido))

# interpolación 

print(f'saludos:{nombre} lenguaje:{apellido}')


# Transformación en la lista de caracteres

print(list(var_nueva))

# Transformacion de una lista a una cadena 

l1 = [nombre, ',', apellido, ',', var_nueva, '!']
print('-'.join(l1))

# transformaciones numericas 

s4 = '1234'
s4 = int(s4)
print(int(s4)) # 1234


# Comprobaciones varias 
s4 = '1234'
print(nombre.isalnum()) # True
print(nombre.isalpha()) # True
print(s4.isalpha()) # False
print(s4.isnumeric()) # True




