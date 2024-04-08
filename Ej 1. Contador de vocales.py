'''Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
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
    respuesta = input('(/e para salir)\n\nIngrese un valor\n--> ').lower()
    
    if respuesta == '/e':
        control = False
    else:
        for i in range(0,respuesta):
            if 'a' in respuesta:
                vocalA += 1
            if 'e' in respuesta:
                vocalE += 1
            if 'i' in respuesta:
                vocalI += 1
            if 'o' in respuesta:
                vocalO += 1
            if 'u' in respuesta:
                vocalU += 1
    
#SALIDA (cantidad de vocales)
os.system('cls')
totalVocales = (vocalA + vocalE + vocalI + vocalO +vocalU)
print(f'A = {vocalA}\nE = {vocalE}\nI = {vocalI}\nO = {vocalO}\nU = {vocalU}\n\nTotal = {totalVocales} ')
