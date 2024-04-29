#--------------------------------------------Operadores y estructuras de control-----------------------------------------------------------

# Operadores aritméticos

example_1 = 10 + 3 # suma(+) me suma los valores 
example_2 = 10 - 3 # resta(-) e resta los valores 
example_3 = 10 * 3 # Multiplicación(*) me multiplica los valores 
example_4 = 10 / 3 # División(/) me divide los valores dándome la division completa(3.3333333333333335)
example_5 = 10 // 3 # División entera(//)  me divide los valores dándome la division entera redondeada a la baja(3)
example_6 = 10 % 3 # Modulo(%) me devuelve el resto de la division
example_7 = 10 ** 3 # Exponente(**) me eleva el valor a la potencia

print(f"Suma: 10 + 3 = {example_1}")
print(f"Resta: 10 - 3 = {example_2}")
print(f"Multiplicación: 10 * 3 = {example_3}")
print(f"Division: 10 / 3 = {example_4}")
print(f"Division entera: 10 // 3 = {example_5}")
print(f"Modulo: 10 % 3 = {example_6}")
print(f"Exponente: 10 ** 3 = {example_7}")

#----------------------------------------------------------------------------------------------------------------
# Operadores de comparación 

example_8 = 10 == 3 # Igualdad(==) me compara si los valores son iguales
example_9 = 12 != 13 # Distinto de (!=) me compara si los valores son distintos
example_10 = 10 > 3 # Mayor que(>) me compara si el valor de la izquierda es mayor que el de la derecha
example_11 = 10 < 3 # Menor que(<) me compara si el valor de la izquierda es menor que el de la derecha
example_12 = 10 >= 3 # Mayor o igual que(>=) me compara si el valor de la izquierda es mayor o igual que el de la derecha
example_13 = 4 <= 3 # Menor o igual que(<=) me compara si el valor de la izquierda es menor o igual que el de la derecha

print(f"Igualdad: 10 == 3 es: {example_8}")
print(f"Distinto de: 12 != 13 es: {example_9}")
print(f"Mayor que: 10 > 3 es: {example_10}")
print(f"Menor que: 10 < 3 es: {example_11}")
print(f"Mayor o igual que: 10 >= 3 es: {example_12}")
print(f"Menor o igual que: 3 <= 3 es: {example_13}")

#-------------------------------------------------------------------------------------------------------------------
# Operadores Lógicos

example_14 = 100
example_15 = 200

# AND: Ambas condiciones deben ser verdaderas. 
print(f"AND: 100 + 200 = 300 y 200 - 100 = 10: {example_14 + example_15 == 300 and example_15 - example_14 == 100}")# El resultado es True porque ambas condiciones se cumplen.

# OR: Al menos una condición debe ser verdadera.

print(f"OR: 100 + 200 = 200 o 200 - 100 = 100: {example_14 + example_15 == 200 or example_15 - example_14 == 100}")# El resultado es True porque una de las condiciones se cumple.

# NOT: Invierte el valor de la condición.

print(f"100 + 200 = 100: {not example_14 + example_15 == 100}")# El resultado es True porque la condición no se cumple.

#-------------------------------------------------------------------------------------------------------------------
# Operadores de asignación 

example_16 = 13 # Asignación 
print(f"= :{example_16}")

example_16 += 14 # Suma y asignación
print(f"+= :{example_16}")
example_16 -= 18 # Resta y asignación
print(f"-= :{example_16}")
example_16 *= 12 # Multiplicación y asignación
print(f"*= :{example_16}")
example_16 /= 19 # División y asignación
print(f"/= :{example_16}")
example_16 %= 112 # Módulo y asignación
print(f"%= :{example_16}")
example_16 //= 17 # División entera y asignación
print(f"//= :{example_16}")
example_16 **= 2 # Potencia y asignación
print(f"**= :{example_16}")

#-------------------------------------------------------------------------------------------------------------------
# Operadores de identidad

example_17 = 16
example_18 = 16

print(f"IS: example_17 is 17: {example_17 is 17}") # El resultado es False porque el valor de la variable es 16.
print(f"IS: example_17 is example_18: {example_17 is example_18}") # El resultado es True porque el valor de la variable es 16.
print(f"IS NOT: example_17 is not = 18: {example_17 is not 18}") # El resultado es True porque el valor de la variable es 16.

#-------------------------------------------------------------------------------------------------------------------
# Operadores de pertenencia 

example_list = [1,2,3,4,5,]
example_list_string = "Ruben Suarez"

print(f"IN: ¿3 esta en example_list?: {3 in example_list}") # El resultado es True porque el valor 3 esta en la lista.
print(f"NOT IN: ¿6 no esta example_list?: {6 not in example_list }") # El resultado es True porque el valor 6 no esta en la lista. 

# Mismo ejemplo con string 

print(f"IN: ¿R esta en example_list_string?: {"R" in example_list_string}") # El resultado es True porque el valor R esta en la lista.
print(f"NOT IN: ¿P no esta en example_list_string?: {"P" not in example_list_string}") #  el resultado es Tue porque el valor P no esta en la lista.

#-------------------------------------------------------------------------------------------------------------------
# Operadores de Bit

example_19 = 10 # 1010
example_20 = 3 # 0011

print(f"AND: 10 & 3 = {10 & 3}")
print(f"OR: 10 | 3 = {10 | 3}")
print(f"XOR: 10 ^ 3 = {10 ^ 3}")
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")

#-------------------------------------------------------------------------------------------------------------------
# Estructuras de control
#Condicionales

my_list = ["Ruben", "Jesus", "Freddy"]
my_name = "Ruben"
#my_name = input("Ingrese su nombre: ").capitalize()  "Asi se podría hacer para que el usuario ingrese su nombre por pantalla."
 

if my_name in my_list:
    print(f"{my_name} Si esta en la lista")
else:
    print(f"Lo siento pero {my_name} no esta en la lista")

 #-------------------------------------------------------------------------------------------------------------------  
# Iterativas

# FOR: se usa para recorrer estructuras que tienen mas de un elemento o ejecutar una acción varias veces. 
for i in range(1,11): # la función "range" se usa para crear un rango de números.
     print(f"---------Tabla del {i}---------")
     for t in range(1,11):
        result = i * t
        print(f"{i} * {t} = {result}")
    
print('[Tabla de  multiplicar con "while"]')        
# WHILE: se usa para ejecutar una acción mientras se cumpla una condición.

my_number_v2 = 1
my_number_v3 = 1

while my_number_v2 < 11:
    print(f"---------Tabla del {my_number_v2}---------")
    my_number_v2 += 1
    while my_number_v3 < 11:
        result_v2 = my_number_v2 * my_number_v3
        print(f"{my_number_v2} * {my_number_v3} = {result_v2}")
        my_number_v3 += 1
    my_number_v3 = 1

#-------------------------------------------------------------------------------------------------------------------
# Manejo de excepciones

try:
    print(10 / 0)
except:
    print("Se a producido un error el en programa")
