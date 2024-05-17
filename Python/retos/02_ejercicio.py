'''
-Crea ejemplos de funciones básicas que representen la diferentes posibilidades del lenguaje:
Sin parámetros ni retornos.
Con uno o varios parámetros.
Com retornos.
-Comprueba si puedes crear funciones dentro de funciones.
-Utiliza el ejemplo de funciones ya creadas en el lenguaje.
'''
#----------------------------------------- FUNCIONES Y ALCANCE ----------------------------------------------------------

# Funciones definidas por el usuario
# simples

def greet():
    print('Hola python')

greet()

#-----------------------------------------------------------------------------------------------------------------------
# con retorno 

def return_greet():
    return 'Hola, mundo' # Retornamos una acción.

greet = return_greet() # Se puede guardar la función dentro de una variable.

print(greet)

#-----------------------------------------------------------------------------------------------------------------------
# Con un argumento

def arg_greet(name): # Se agregar un argumento a la función.
    print(f"Hola, {name} como estas?")

arg_greet("Pedro")
arg_greet("Juan")

#-----------------------------------------------------------------------------------------------------------------------
# Con varios argumentos

def args_greet(greet, name): # Se están agregando varios argumentos a la función.
    print(f"{greet}, {name}")

print(f"Hi","Jesus")

# También se puede agregar la especificación de los parámetros al momento de ejecutar la acción.
def new_args_greet(greet, name): 
    print(f"{greet}, {name}!") # Asi se respeta el orden de los parámetros.

new_args_greet(name="pedro", greet="Hi")
#-----------------------------------------------------------------------------------------------------------------------
# Con un argumento predeterminado

def default_arg_greet(name="Hola"): # Si no se le proporciona valor al momento de llamar la función, imprime el parámetro por defecto.
    print(f"{name}")

default_arg_greet("pedro")

#-----------------------------------------------------------------------------------------------------------------------

# Con argumentos y retornos

def return_arg_greet(greet, name):
    return f"{greet}, {name}!"

print(return_arg_greet("ey", "Ruben"))

#-----------------------------------------------------------------------------------------------------------------------

# Retornando varios valores.

def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()# Se pueden crear variables para almacenar los valores del retorno. 
print(greet) # Hola
print(name) # Python

#-----------------------------------------------------------------------------------------------------------------------

# Con un numero variable de argumentos

def variable_arg_greet(*names): # Con un '*' indicamos que vamos a darle mas de un valor a la función.
    for name in names:
        print(f"Hola {name}!") # Esta acción se va a ejecutar tantas veces como nombres le demos a la función.

variable_arg_greet("pedro", "juan", "maria") # me imprime un saludo (Hola) para cada nombre. 

#-----------------------------------------------------------------------------------------------------------------------
# Con un numero variable de argumentos con palabras claves

def variable_key_args_greet(**name): # Al agregar '**' estamos diciendo que vamos a pasar parámetros clave, valor.
    for key, value in name.items():
        print(f"Hello, {value} ({key})!")


variable_key_args_greet(
    nombre="Jesus",
    alias="JesusDev",
    lenguaje="Python",
    edad=24
)
 #------resultado------
 # Hello, Jesus (nombre)!
 # Hello, JesusDev (alias)!
 # Hello, Python (lenguaje)!
 # Hello, 24 (edad)!

#-----------------------------------------------------------------------------------------------------------------------

# Funciones dentro de funciones

def outer_function(a,b):
    result = a + b
    if result > 20:
        def inner_function():
            print("El resultado es mayor a 20")
        inner_function()
    else:
        def inner_function():
            print("El resultado es menor a 20")
        inner_function()

print(outer_function(1,2))

#-----------------------------------------------------------------------------------------------------------------------

# Funciones propias del lenguaje (built-in)
# Algunas funciones:

print() # Nos permite imprimir por terminal algún resultado.
len("Hola") # Nos devuelve un valor entero que indica la cantidad de caracteres en la cadena de entrada.
type(20)  # Nos permite saber el tipo de dato que estamos usando en el código.
"hola".upper() # upper() Convierte una cadena a mayúsculas.
range(1,4) # Genera una secuencia de números que van desde 0 (o cualquier numero) por defecto hasta el número que se pasa como parámetro menos 1.

#----------------------------------------------------------------------------------------------------------------------- 