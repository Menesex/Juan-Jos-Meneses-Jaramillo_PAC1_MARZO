'''Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
'''
import os
def fnt_contadorVocales(palabras):
    global vocalA
    global vocalE
    global vocalI
    global vocalO
    global vocalU

    n = len(palabras)
    for i in range(0,n):
        if 'a' in palabras:
            vocalA += 1
        if 'e' in palabras:
            vocalE += 1
        if 'i' in palabras:
            vocalI += 1
        if 'o' in palabras:
            vocalO += 1
        if 'u' in palabras:
            vocalU += 1

control = True
while control == True:
    vocalA = 0
    vocalE = 0
    vocalI = 0
    vocalO = 0
    vocalU = 0
    os.system("cls")
    print('\t.:Contador de vocales menesex:.')
    print(f'A = {vocalA}\nE = {vocalE}\nI = {vocalI}\nO = {vocalO}\nU = {vocalU}\n')
    
    #entrada pedir al usuario que ingrese un valor
    #proceso
    respuesta = input('Ingrese un valor\n--> ').lower()

    fnt_contadorVocales(respuesta)
    os.system('cls')
    totalVocales = (vocalA + vocalE + vocalI + vocalO +vocalU)
    print(f'A = {vocalA}\nE = {vocalE}\nI = {vocalI}\nO = {vocalO}\nU = {vocalU}\n\nTotal = {totalVocales} ')
    
    while True:
        try:
            control2 = input('[ENTER] Continuar\n[E] Salir\n-> ').strip().lower()[0]
            if control2 == 'e':
                control = False
                break
            else:
                # Si no se ingresa 'e' ni se produce IndexError, continuamos con el bucle
                break
        except IndexError:
            # Si se produce un IndexError (es decir, si el usuario presiona Enter sin ingresar nada),
            # simplemente continuamos con el bucle
            break
