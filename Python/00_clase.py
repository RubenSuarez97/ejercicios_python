#---------------------------------------------Ejercicio 1: comentarios, variables, tipos de datos ---------------------------------------------

# Esto es un comentario en python y esta es su URL oficial: https://www.python.org/
'''
Esto es un comentario 
en varias líneas de python.
'''

#Variables
my_variable = "Ruben Suarez"
MI_CONSTANTE = "Python no tiene constaste" # Esto es por convención de programación. 

# variables con tipos de datos

my_string = "Hola mundo!" # Tipo cadena de texto.
my_number = 26 # Tipo enteros.
my_bool = True # Tipo Boolean (Verdadero o Falso).
my_bool_2 = False # Tipo Boolean (Verdadero o Falso).
my_float = 26.5 # Tipo Flotante o decimal.

# Otra forma de saber que tipo de datos es: 
my_string_2: str = "Esto también es un string"
my_number_2: int = 27
my_float_2 : float = 27.4
my_bool_3: bool = True

# Imprimir por consola para ver resultados en pantalla. Función 'print()'. 
print("Hola, Python!")
print(26)

#'type' es una función del sistema que me permite ver el tipo de datos de una variable.
print(type(my_string))#<class 'str'>
print(type(my_number))#<class 'int'>
print(type(my_bool))#<class 'bool'>
print(type(my_bool_2))#<class 'bool'>
print(type(my_float))#<class 'float'>

print(my_string_2)
print(my_number_2)
print(my_float_2)
print(my_bool_3) 