'''
Ejercicio 2: Tabla de Multiplicar (2.0)
Crea un programa que solicite al usuario ingresar un número entero positivo (N). El programa debe mostrar la tabla de
multiplicar del número, teniendo en cuenta que se debe generar la tabla con los primeros 10 valores de dicha tabla.
'''

import os
os.system("cls")

    #Entrada 
numero = int(input('\t.:Tablas de multiplicar menesex:.\n\n¿De qué número desea sus tablas? --> '))
#controlar los números negativos
while numero < 0:
    numero = int(input('Porfavor ingrese un número positivo'))

    #Proceso (Sacar las 10 tablas)
print(f'\n\n\t.:Tablas del número {numero}:.')
i = 1
while i < 11:
    multIterativa = (numero * i)
    print (f'{numero} * {i}  = {multIterativa}')
    i += 1
