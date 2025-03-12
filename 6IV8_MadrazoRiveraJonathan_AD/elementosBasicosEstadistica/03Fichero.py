import pandas as pd
def resumen_cotizacion(fichero):
    df= pd.read_csv(fichero,sep=';',decimal=',',thousands=',',index_col=0)
    return pd.DataFrame([df.min(),df.max(),df.mean(),df.std()],index=['Mínima','Máxima','Media','Desviación estándar'])

print(resumen_cotizacion('C:/analisisdedatoMRJ/6IV8_MadrazoRiveraJonathan_AD\elementosBasicosEstadistica/cotizacion.csv'))
    