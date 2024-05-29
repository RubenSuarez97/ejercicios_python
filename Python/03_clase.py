#---------------------------------Uso y creación de listas en Python-----------------------------------------------

# Ejemplo de listas

names = ['Jose','Pedro','Pablo','juan'] # Aquí se creo una lista con nombre (Tipo de datos texto).

mixed_data_type = ['Hola', 23, 23.4, True] # Se pueden crear lista con tipos de datos mixtos cada uno separado por coma(,).

# Obtener el valor de un elemento de una lista en Python de forma individual.
# De esta forma podemos obtener el nombre de la lista según el numero del indice que corresponda dentro de la lista.
# Ejemplo: names[0] = Jose, names[1] = Pedro... La numeración comienza en cero.
print(names[0]) # Jose
print(names[1]) # Pedro
print(names[2]) # Pablo
print(names[3]) # juan
print(names[-1]) #  Así un modo sencillo de obtener el último elemento es con [-1]. 

#-----------------------------------------------------------------------------------------------------------------------

# Recorrer una lista 
# utilizando un bucle 'for'
age = [12, 13, 30, 46, 50]

for i in age:
    print(i) # 12, 13, 30, 46, 50

#-----------------------------------------------------------------------------------------------------------------------
# Utilizando la función enumerate
#'enumerate' es una función built-in en Python que permite iterar sobre una lista y tener un contador automático junto con ella.
frutas = ['Manzana', 'Pera', 'Uva']
for i, fruta in enumerate(frutas):
    print(f'{i}, {fruta}')

#-----------------------------------------------------------------------------------------------------------------------

# Utilizando un bucle while

color = ['Amarillo', 'Azul', 'Rojo', 'Verde']
index = 0

while index < len(color):
    print(color[index])
    index += 1

#---------------------------------------------Agregar y remover elementos a una lista---------------------------------------------------
# La función append() nos ayuda a agregar elementos a una lista.
heroes_dc = [] # Se crea una lista vacía
heroes_dc.append('Batman') 
heroes_dc.append('superman')
heroes_dc.append('flash')
print(heroes_dc) 

#-----------------------------------------------------------------------------------------------------------------------
# Otro manera es unir una lista ya existente a la lista original. 
heroes_marvel = []

heroes_marvel = heroes_marvel + ['Iron-man','Hulk','Spider-man']

print(heroes_marvel) 

#-----------------------------------------------------------------------------------------------------------------------
# La función pop() nos ayuda a remover elementos de una lista.
# Se indica la posición del elemento que quieres eliminar dentro de la lista. 
heroes_marvel.pop(0)

print(heroes_marvel)

# También podemos usar la función remove.
#La función remove, removerá un elemento según el valor que este tenga al interior de la lista.
heroes_marvel.remove('Hulk')

print(heroes_marvel)

#-----------------------------------------------------------------------------------------------------------------------

# Ejemplos de Tupla

tupla = (1,2,3)
print(tupla) # (1,2,3)

# También se pueden declarar sin () separados por coma ','.
tupla_dos = 1,2,3
print(tupla_dos) # (1,2,3)

# Anidadas 
tupla_tres = 1, 2,('a' , 'b'), 3, 4

print(tupla_tres)

# Convertir una lista en tupla haciendo uso de al función tuple().

tupla_cuatro = tuple(heroes_marvel) 
print(tupla_cuatro) # ('Spider-man',)

# asignar el valor de una tupla con n elementos a n variables. 

tupla_cinco = (5, 6, 7)
(x,y,z) = tupla_cinco

print(x,y,z) # 5, 6, 7

#-----------------------------------------------------------------------------------------------------------------------
# Ejemplos de diccionario (set)

my_set = {
    'Nombre': 'Tony',
    'Usuario' : '@Tony20'
}
# Para obtener un valor especifico dentro del set usamos el mismo método que con las listas. pero en lugar de indice usamos la llave.
print(my_set['Nombre']) # Tony
print(my_set['Usuario'])

for k in my_set:
    print(k, ':' , my_set[k])





