import pandas as pd
##Haz un programa que pregunte al usuario por las ventas de un rango de años y muestree en la pantalla una serie de datos de vebtas indexeadas por los años,.. antes y despues de aplicar un descuento
inicio = int(input('Introduce el año de ventas inicial: '))
fin = int(input('Introduce el año final de ventas: '))
ventas={}
for i in range(inicio,fin+1):
    ventas[i] = float(input('Introduce las ventas del año: '+ str(i)+': ' ))

ventas = pd.Series(ventas)
print('Ventas\n',ventas)
print('Ventas con descuentro ', ventas*0.9)

