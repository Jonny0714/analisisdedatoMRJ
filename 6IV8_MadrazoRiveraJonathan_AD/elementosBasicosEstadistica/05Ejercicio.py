import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/analisisdedatoMRJ/6IV8_MadrazoRiveraJonathan_AD/elementosBasicosEstadistica/housing.csv")

# Seleccionar las columnas de interés
columns = ['median_house_value', 'total_bedrooms', 'population']

# Calcular estadísticas descriptivas
stats = {
    'Media': [],
    'Mediana': [],
    'Moda': [],
    'Rango': [],
    'Varianza': [],
    'Desviación Estándar': []
}
for column in columns:
    stats['Media'].append(df[column].mean())
    stats['Mediana'].append(df[column].median())
    stats['Moda'].append(df[column].mode().iloc[0])
    stats['Rango'].append(df[column].max() - df[column].min())
    stats['Varianza'].append(df[column].var())
    stats['Desviación Estándar'].append(df[column].std())

# Convertir a DataFrame con estadísticas como filas
stats_df = pd.DataFrame(stats, index=columns).T
print("Estadísticas Descriptivas:")
print(stats_df)

# Función para calcular tablas de frecuencias
def calculate_frequency_table(column):
      frequencies = df[column].value_counts().sort_index()
      total = frequencies.sum()
      relative_frequencies = frequencies / total
      absolute_relative_frequencies = relative_frequencies * 100  # En porcentaje

      frequency_table = pd.DataFrame({
          'Valor': frequencies.index,
          'Frecuencia Absoluta': frequencies.values,
          'Frecuencia Relativa': relative_frequencies.values,
          'Frecuencia Absoluta Relativa (%)': absolute_relative_frequencies.values
      })
      frequency_table['Columna'] = column  # Agregar el nombre de la columna
      return frequency_table

  # Generar tablas de frecuencias para cada columna
for col in columns:
      frequency_table = calculate_frequency_table(col)
      print(f"\nTabla de Frecuencias para {col}:")
      print(frequency_table.head(10))  # Mostrar las primeras 10 filas

  # Graficar histograma de median_house_value con comparación
def plot_histogram():
      plt.figure(figsize=(12, 6))
      sns.histplot(df['median_house_value'], bins=50, kde=True, color='blue', label='Median House Value')
      sns.histplot(df['total_bedrooms'], bins=50, kde=True, color='red', label='Total Bedrooms', alpha=0.6)
      sns.histplot(df['population'], bins=50, kde=True, color='green', label='Population', alpha=0.6)
    
      plt.xlabel("Valor")
      plt.ylabel("Frecuencia")
      plt.legend()
      plt.title("Histograma de Median House Value comparado con Total Bedrooms y Population")
      plt.show()

plot_histogram()
