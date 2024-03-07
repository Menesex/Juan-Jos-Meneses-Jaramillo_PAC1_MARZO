'''
Escribe un programa que permita al usuario convertir una temperatura en grados centígrados a Fahrenheit o viceversa. El programa debe
solicitar al usuario ingresar la temperatura y la unidad de medida (C para Celsius, F para Fahrenheit) y luego realizar la conversión
correspondiente, el programa debe manejar un menú de opciones y solo detenerse cuando se presione la opción finalizar.
Grados centígrados = (grados Fahrenheit - 32) x 5/9.
Grados Fahrenheit = (grados centígrados x 9/5) +32.
'''
import os
#BUCLE WHILE PARA EL MENÚ CONTROLADO
control = True
while control == True:
    os.system("cls") 
    print('\t.:Convertidor de temperatura (C) & (F):.')
    
    #Entrada (temperatura y unidad de medida)
    
    temperatura1 = int(input('Ingrese la temperatura en números enteros\n--> '))
    unidadMedida1 = input('Seleccione la unidad de medida\n[C]Celsius[F]Fahrenheit\n-->')

    #Proceso (conversión)
    
    #de fahrenheit a centigrados
    if unidadMedida1 == 'F' or unidadMedida1 == 'f':
        #Grados centígrados = (grados Fahrenheit - 32) x 5/9..
        temperatura2 =  ((temperatura1 -32 ) * 5)/9
        unidadMedida2 = 'C'
        
    #de centigrados a fahrenheit
    elif unidadMedida1 == 'C' or unidadMedida1 == 'c':
        temperatura2 =  (((temperatura1 * 9)/ 5) + 32)
        unidadMedida2 = 'F'
    
    #salida
    print(f'\n\t..:Conversión:..\n\n{temperatura1} {unidadMedida1} = {temperatura2} {unidadMedida2} ')
    
    control2 = input('\n\t¿Desea continuar?\n[Enter] para continuar\n[1]Finalizar\n--> ')
    if control2 == '1':
        control = False

  