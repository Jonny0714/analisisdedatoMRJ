import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
#Conocer las ventas totales del comercio
#Conocer cuantos socios tienen adeudo y cuantos no tienen adeudo con su porcentaje correspondiente
#Grafica donde se pueda observar las ventas totales respecto del tiempo, en una grafica de barras 
#Grafica donde se pueda visualizar la desviación estándar de los pagos realizados del comercio respecto del tiempo
#Cuanto es la deuda total de los clientes
#Cuanto es el porcentaje de utilidad del comercio a partir de el total de las ventas respecto del adeudo 
#Crear un grafico circular de ventas por sucursal.
#Presentar un grafico de cuales son las deudas totales por cada sucursal respecto del margen de utilidad de cada sucursal.
proyecto1=pd.read_csv("C:/analisisdedatoMRJ/6IV8_MadrazoRiveraJonathan_AD/elementosBasicosEstadistica/proyecto1.csv")
catalogo=pd.read_csv("C:/analisisdedatoMRJ/6IV8_MadrazoRiveraJonathan_AD/elementosBasicosEstadistica/Catalogo_sucursal.csv")
#Conocer las ventas totales del comercio
ventas_totales=proyecto1["ventas_tot"].sum()
print("Las ventas totales del comercio son: ",ventas_totales)
#Conocer cuantos socios tienen adeudo y cuantos no tienen adeudo con su porcentaje correspondiente
adeudo=(proyecto1["B_adeudo"]=='Con adeudo').sum()
no_adeudo=(proyecto1["B_adeudo"]=='Sin adeudo').sum()
xd=no_adeudo/len(proyecto1)*100
dx=adeudo/len(proyecto1)*100
print("El porcentaje de socios que no tienen adeudo es: ",xd,'%')
print("El porcentaje de socios que tienen adeudo es: ",dx,'%')

print("Los socios que tienen adeudo son: ",adeudo)
print("Los socios que no tienen adeudo son: ",no_adeudo)
#Grafica donde se pueda observar las ventas totales respecto del tiempo, en una grafica de barras


ventas_por_tiempo = proyecto1.groupby('B_mes')['ventas_tot'].sum()
ventas_por_tiempo.plot(kind='bar', color='blue')
plt.title('Ventas totales respecto del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Ventas totales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.figure()


#Grafica donde se pueda visualizar la desviación estándar de los pagos realizados del comercio respecto del tiempo
media = proyecto1["ventas_tot"].mean()
desviacion_estandar = proyecto1["ventas_tot"].std()
plt.figure(figsize=(12, 6))

# Crear gráfico de desviación estándar

    
desviacion_por_tiempo = proyecto1.groupby('B_mes')['ventas_tot'].std()
desviacion_por_tiempo.plot(kind='line', marker='o', color='green')
plt.title('Desviación estándar de pagos respecto del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Desviación estándar')
plt.grid(True)
plt.tight_layout()
plt.figure()

  
# Cuanto es la deuda total de los clientes
deuda_total = proyecto1.loc[proyecto1['B_adeudo'] == 'Con adeudo', 'ventas_tot'].sum()
print("La deuda total de los clientes es:", deuda_total)

# Cuanto es el porcentaje de utilidad del comercio a partir de el total de las ventas respecto del adeudo
porcentaje_utilidad = ((ventas_totales - deuda_total) / ventas_totales) * 100
print(f"El porcentaje de utilidad del comercio es: {porcentaje_utilidad:.2f}%")

# Crear un grafico circular de ventas por sucursal

datos_completos = pd.merge(proyecto1, catalogo, on='id_sucursal')

# Agrupar ventas por sucursal
ventas_por_sucursal = datos_completos.groupby('suc')['ventas_tot'].sum()

# Crear gráfico circular
plt.figure(figsize=(10, 8))
plt.pie(ventas_por_sucursal, labels=ventas_por_sucursal.index, autopct='%1.1f%%', 
        shadow=True, startangle=90)
plt.axis('equal')  
plt.title('Ventas por sucursal')
plt.tight_layout()
plt.figure()




plt.show()