'''
Ejercicio 1. Contador de Vocales (1.0)
Crea un programa que solicite al usuario ingresar valores y este debe verificar cuando se ingresa una vocal, el programa
debe contar y mostrar la cantidad de vocales (a, e, i, o, u) ingresadas cuantas, de cada una y la cantidad total, importante
tener en cuenta que la aplicación se detiene con una opción de menú llamada finalizar.
'''
import os

vocalA = 0
vocalE = 0
vocalI = 0
vocalO = 0
vocalU = 0
control = True
while control == True:
    os.system("cls")
    print('\t.:Contador de vocales menesex:.')
    print(f'A = {vocalA}\nE = {vocalE}\nI = {vocalI}\nO = {vocalO}\nU = {vocalU}\n')
    
    #entrada pedir al usuario que ingrese un valor
    #proceso
    respuesta = input('Ingrese un valor\n--> ')
    if respuesta == 'a' or respuesta == 'A':
        vocalA += 1
    if respuesta == 'e' or respuesta == 'E':
        vocalE += 1
    if respuesta == 'i' or respuesta == 'I':
        vocalI += 1
    if respuesta == 'o' or respuesta == 'O':
        vocalO += 1
    if respuesta == 'u' or respuesta == 'U':
        vocalU += 1
    
    control2 = input('\n\t¿Desea continuar?\n[Enter] para continuar\n[1]Finalizar\n--> ')
    if control2 == '1':
        control = False

#SALIDA (cantidad de vocales)
totalVocales = (vocalA + vocalE + vocalI + vocalO +vocalU)
print(f'A = {vocalA}\nE = {vocalE}\nI = {vocalI}\nO = {vocalO}\nU = {vocalU}\n\nTotal = {totalVocales} ')