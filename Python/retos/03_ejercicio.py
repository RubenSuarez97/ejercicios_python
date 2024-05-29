'''
El problema es simple, queremos crear un programa con el cual podamos guardar los nombres y las 
identificaciones de múltiples personas (no sabemos cuántas) sin perder ninguna de ellas.
El usuario es el encargado de suministrar la información de cada persona. 
Vamos a suponer que el usuario solo podrá ingresar un máximo de tres personas, para así poder comprobar 
fácilmente nuestro programa. Sin embargo, puedes hacerlo sin límite si prefieres:
'''

# Creamos las listas (vacías al comienzo)
nombres = []
identificaciones = []

# Definimos un tamaño para las listas
# Lo puedes cambiar si quieres
tamaño = 3

# Leemos los datos y los agregamos a la lista
for i in range(tamaño):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    identificación = input("Identificación: ")

    nombres.append(nombre)
    identificaciones.append(identificación)

# Ahora mostremos las listas
for i in range(tamaño):
    print('-----------------------------------------')
    print("Mostrando los datos de la persona", i + 1)

    print("Nombre:", nombres[i])
    print("Identificación:", identificaciones[i])


#--------------------------------------------------------------------------------------------------------------

'''
El problema es simple, queremos crear un programa con el cual podamos guardar los nombres y las identificaciones
de múltiples personas (no sabemos cuántas) sin perder ninguna de ellas.
El usuario es el encargado de suministrar la información de cada persona.
Vamos a suponer que el usuario solo podrá ingresar un máximo de tres personas, para así poder comprobar
fácilmente nuestro programa. Sin embargo, puedes hacerlo sin límite si prefieres:
'''
usuarios = {
    'Nombres' : [],
    'Identificaciones': []
}

len_set = 3

for i in range(len_set):
    print('Ingrese los datos del Usuario', i + 1)
    nombre = input('Ingrese el nombre de usuario: ')
    identification = input('Ingrese la identificación del usuario: ')

    usuarios['Nombres'].append(nombre)

    usuarios['Identificaciones'].append(identification)

for i in range(len_set):
    print('Datos de usuario', i + 1)
    print('Nombre:', usuarios['Nombres'][i])
    print('Identificación:', usuarios['Identificaciones'][i])