import pandas as pd
import matplotlib.pyplot as plt



df= pd.read_csv('C:/analisisdedatoMRJ/6IV8_MadrazoRiveraJonathan_AD\elementosBasicosEstadistica/housing.csv')
print(df.head())
#mostrar ultimas 5 filas
print(df.tail())
#mostrar una fila en especifico
print(df.iloc[7])
#mostrar una columna en especifico
print(df['ocean_proximity'])
#obtener media de la columna total_rooms
mediadecuarto= df['total_rooms'].mean()
print(f'La media de total room es: {mediadecuarto}')

#mediana
medianacuarto= df['median_house_value'].median()
print(f'La mediana de median_house_value es: {medianacuarto}')

#suma popular
salariototal= df['population'].sum()
print(f'La suma de population es: {salariototal}')
#para poder filtrar
filtro=df[df['ocean_proximity']=='ISLAND']
print(filtro)




#vamos a hacer un grafico de dispersión
plt.scatter(df['ocean_proximity'][:10],df['median_house_value'][:10])
#nombramos los ejes
plt.xlabel('Proximidad')
plt.ylabel('Precio')
plt.title('Grafico de dispersión al Oceano vs Precio')
plt.show()