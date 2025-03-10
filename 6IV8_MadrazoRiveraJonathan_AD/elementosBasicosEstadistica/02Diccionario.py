import pandas as pd
##Escribir una funcion que reciba un diccionario con las notsa de los estudiantes del curso y cevuelve una serie con minimo,maximo, media, desvicacion tipica
def estadistica_notas(notas):
    notas= pd.Series(notas) 
    estadisticas = pd.Series([notas.min(),notas.max(),notas.mean(),notas.std()],index=['Minimo','Maximo','Media','Desviacion estandar'])
    return estadisticas
notas = {'Juan':5.9,'Juanita':5,'Pedro':6.6,'Fabian':8.5,'Maximiliano':7.5,'Sandra':9.8,'Rosario':9}


def aprobados(notas):
    notas= pd.Series(notas)
    aprobados = notas[notas>=5].sort_values(ascending=False)
    return aprobados
print(aprobados(notas))
print(estadistica_notas(notas))  