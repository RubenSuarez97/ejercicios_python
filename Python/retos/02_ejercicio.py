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





