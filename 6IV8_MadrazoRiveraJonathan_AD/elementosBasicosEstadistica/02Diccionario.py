import pandas as pd
##Escribir una funcion que reciba un diccionario con las notsa de los estudiantes del curso y cevuelve una serie con minimo,maximo, media, desvicacion tipica
def estadistica_notas(notas):
    notas= pd.Series(notas) 
    estadisticas = pd.Series([notas.min(),notas.max(),notas.mean(),notas.std()],index=['Minimo','Maximo','Media','Desviacion estandar'])
    return estadisticas
notas = {'Juan':9,'Juanita':7,'Pedro':6.6,'Fabian':8.5,'Maximiliano':7.5,'Sandra':9.8,'Rosario':9}
print(estadistica_notas(notas))  