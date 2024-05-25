
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
# Algunas funciones vistas en los ejercicios:

print() # Nos permite imprimir por terminal algún resultado.
len("Hola") # Nos devuelve un valor entero que indica la cantidad de caracteres en la cadena de entrada.
type(20)  # Nos permite saber el tipo de dato que estamos usando en el código.
"hola".upper() # upper() Convierte una cadena a mayúsculas.
range(1,4) # Genera una secuencia de números que van desde 0 (o cualquier numero) por defecto hasta el número que se pasa como parámetro menos 1.

#----------------------------------------------------------------------------------------------------------------------- 

# Variables globales 

global_var = "python"

def variable_global():
    print(f'Hello {global_var}!')

variable_global()
#----------------------------------------------------------------------------------------------------------------------- 

# Variable_local

def variable_local():
    local_var = "Hello" # Esta variable tiene un alcance local ya que este definida dentro de la función y no se puede llamar fuera de ella.
    print(f'{local_var} {global_var}!')

variable_local()

# print(local_var) # Automáticamente python nos indica que hay un error debido a que la variable no es global.

#----------------------------------------------------------------------------------------------------------------------- 
'''
Crea una función que reciba dos parámetros de tipo cadena de texto  t retorne un numero.
- la función imprime todo los numero del 1 al 100. Teniendo en cuenta que:
    - Si el numero es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el numero es múltiplo de 5, muestra la cadena del texto del segundo parámetro.
    - Si el numero es múltiplo de 3 y de 5, muestra las dos cadenas del texto concatenadas.
    - La función retorna el numero de veces que se ha impreso el numero en lugar de los textos.
'''

def return_text_number(text_1, text_2):
    count = 0 
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(text_1 , text_2)
        elif i % 3 == 0:
            print(text_1)
        elif i % 5 == 0:
            print(text_2)
        else:
            print(i)
            count += 1
    return count

print(return_text_number('Fizz', 'Buzz'))





