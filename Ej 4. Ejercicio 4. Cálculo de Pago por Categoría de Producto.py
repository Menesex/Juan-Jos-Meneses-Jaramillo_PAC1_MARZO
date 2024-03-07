'''
Escribe un programa en Python que permita calcular el pago de un producto en una tienda, tomando en cuenta que los productos se encuentran
clasificados en cinco categorías: Ferretería, Aseo, Seguridad, Alimentos y Electrodomésticos. Cada categoría tiene un descuento diferente aplicado al
precio del producto, el cual debe presentar un menú de opciones donde solo se termina el sistema con la opción “TERMINAR”.
Descuentos por Categoría: Ferretería: 10% Aseo: 5% Seguridad: 15% Alimentos: 8% Electrodomésticos: 12%
El programa debe solicitar al usuario ingresar la categoría y el precio de cada producto comprado, y luego calcular el precio final con el descuento
aplicado. Al finalizar, debe mostrar la cantidad de productos comprados por cada categoría y el total recaudado.
'''
import os
#Definir
    #Constantes (descuentos según categoría)
dtoFerreteria = 0.10
dtoAseo = 0.05
dtoSeguridad = 0.15
dtoAlimentos = 0.08
dtoElectrodomesticos = 0.12
    #Contador de productos comprados
cantFerreteria = 0
cantAseo = 0
cantSeguridad = 0
cantAlimentos = 0
cantElectrodomesticos = 0
    
    #subtotal = sin dto ; total= con el dto aplicado
subtotal = 0
total = 0 

#BUCLE WHILE PARA EL MENÚ CONTROLADO
control = True
while control == True:
    os.system("cls") 
    print('\t.:Tienda Meneses:.\n\nA continuación rellene los datos para su calculo')
    
    #ENTRADA  (categoría y precio)
    tipoProducto = int(input('\n\nSeleccione el tipo de producto\n[1]Ferretería\n[2]Aseo\n[3]Seguridad\n[4]Alimentos\n[5]Electrodomesticos\n--> '))
    if 0 < tipoProducto < 6:
        precio = int(input('Ingrese el precio del producto\n--> '))
    else:
        print("\nError, opción incorrecta")
        control = False
    #proceso
    
    #Ferreteria
    if tipoProducto == 1:
        cantFerreteria += 1
        subtotal += precio
        total += ((precio)-(precio * dtoFerreteria))
    
    #Aseo
    if tipoProducto == 2:
        cantAseo += 1
        subtotal += precio
        total += ((precio)-(precio * dtoAseo))
        
    #Seguridad
    if tipoProducto == 3:
        cantSeguridad += 1
        subtotal += precio
        total += ((precio)- (precio * dtoSeguridad))
        
    #Alimentos
    if tipoProducto == 4:
        cantAlimentos += 1
        subtotal += precio
        total += ((precio) - (precio * dtoAlimentos))
        
    #Electrodomesticos
    if tipoProducto == 5:
        cantElectrodomesticos += 1
        subtotal += precio
        total += ((precio) - (precio * dtoElectrodomesticos))
    
    control2 = input('\n\t¿Desea continuar?\n[Enter] para continuar\n[1]Finalizar\n--> ')
    if control2 == '1':
        control = False
    
#Salida (cantidad de productos comprados por cada categoría y el total recaudado.)
    print(f'\t.:Facturación:.\n\nCantidad de productos:\nFerretería = {cantFerreteria}\nAseo = {cantAseo}\nSeguridad= {cantSeguridad}\nAlimentos = {cantAlimentos}\nElectrodomesticos = {cantElectrodomesticos}')
    
    print(f'\nsubTotal = {subtotal}\nTotal = {total}')