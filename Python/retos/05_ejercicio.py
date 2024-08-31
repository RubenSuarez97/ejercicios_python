'''
-Crea una agenda de contactos por terminal.
-Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
-Cada contacto debe tener un nombre y un numero de teléfono. 
-El programa solicita en primer lugar cual es la operación que se quiere realizar, y a continuación los 
datos necesarios para llevarla a cabo.
-El programa no debe dejar introducir numero de teléfonos no numéricos y con mas de 11 dígitos.
-También se debe proponer una actualización de finalización del programa.
'''
agenda = {}

def contactos_en_agenda():
    def contact_data():
        print('Datos del contacto:')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, Teléfono {valor}')
    
    while True:
        print('1. Buscar un contacto')
        print('2. Insertar un contacto')
        print('3. Actualización del contacto')
        print('4. Eliminar un contacto')
        print('5. Salir')

        opción = input('\nIngrese una de las opciones: ')

        match opción:
            case '1':
                nombre = input('Ingrese el nombre del contacto: ')
                if nombre in agenda:
                    print(f'El contacto {nombre} esta en la agenda estos son sus datos: {agenda[nombre]} ')

                else:
                    print(f'El contacto {nombre} no esta en la agenda ☹')
            case '2':
                nombre = input('Ingrese el nombre del contacto: ')
                if nombre in agenda:
                    print('El contacto ya existe. Desea consultar datos?')
                    print('1. Si')
                    print('2. No')
                    opción_consul = input('Ingrese una de las opciones: ').lower()
                    if opción_consul == 'Si':
                        contact_data()    
                    else:
                        continue
                else:
                    teléfono = input('Ingrese el número de teléfono: ')
                    if len(teléfono) != 11 or not teléfono.isdigit():
                        print('El número de teléfono debe ser de 11 dígitos')
                        print('1. Intente de nuevo')
                        print('2. Salir')
                        opción = input('Ingrese una de las opciones: ')
                        if opción == '1':
                            teléfono = input('Ingrese el número de teléfono: ')
                            agenda[nombre] = teléfono
                        else:    
                            continue
                    else:                   
                        agenda[nombre] = teléfono
            case '3':
                nombre = input('Ingrese el nombre del contacto a actualizar: ')
                if nombre in agenda:
                    teléfono = input('Ingrese el nuevo número de teléfono: ')
                    agenda[nombre] = teléfono
                    contact_data()
                else:
                    print(f'El contacto {nombre} no esta en la agenda ☹')
            
            case '4':
                nombre = input('Ingrese el nombre del contacto a eliminar: ')
                if nombre in agenda:
                    del agenda[nombre]
                    print('Contacto a sido eliminado')
                    
            case '5':
                print('Saliendo de la agenda')
                break

            case _:
                print('Error❌ Ingrese una opción valida')

            
contactos_en_agenda()
