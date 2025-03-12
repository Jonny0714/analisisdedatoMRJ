# Madrazo Rivera Jonathan 6IV8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/analisisdedatoMRJ/6IV8_MadrazoRiveraJonathan_AD/elementosBasicosEstadistica/housing.csv")

columns = ['median_house_value', 'total_bedrooms', 'population']

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

stats_df = pd.DataFrame(stats, index=columns).T
print("Estadísticas Descriptivas:")
print(stats_df)

def calculate_frequency_table(column):
      frequencies = df[column].value_counts().sort_index()
      total = frequencies.sum()
      relative_frequencies = frequencies / total
      absolute_relative_frequencies = relative_frequencies * 100

      frequency_table = pd.DataFrame({
          'Valor': frequencies.index,
          'Frecuencia Absoluta': frequencies.values,
          'Frecuencia Relativa': relative_frequencies.values,
          'Frecuencia Absoluta Relativa (%)': absolute_relative_frequencies.values
      })
      frequency_table['Columna'] = column
      return frequency_table

for col in columns:
      frequency_table = calculate_frequency_table(col)
      print(f"\nTabla de Frecuencias para {col}:")
      print(frequency_table.head(10))

def plot_histograms():
      plt.figure(figsize=(18, 6))

      plt.subplot(1, 3, 1)
      sns.histplot(df['median_house_value'], bins=50, kde=True, color='blue')
      plt.axvline(df['median_house_value'].mean(), color='red', linestyle='--', label='Promedio Median House Value')
      plt.xlabel("Median House Value")
      plt.ylabel("Frecuencia")
      plt.title("Histograma de Median House Value")
      plt.legend()

      plt.subplot(1, 3, 2)
      sns.histplot(df['population'], bins=50, kde=True, color='green')
      plt.axvline(df['median_house_value'].mean(), color='red', linestyle='--', label='Promedio Median House Value')
      plt.xlabel("Population")
      plt.ylabel("Frecuencia")
      plt.title("Histograma de Population")
      plt.xlim(0, 5000)
      plt.legend()

      plt.subplot(1, 3, 3)
      sns.histplot(df['total_bedrooms'], bins=50, kde=True, color='orange')
      plt.axvline(df['median_house_value'].mean(), color='red', linestyle='--', label='Promedio Median House Value')
      plt.xlabel("Total Bedrooms")
      plt.ylabel("Frecuencia")
      plt.title("Histograma de Total Bedrooms")
      plt.xlim(0, 10)
      plt.legend()

      plt.tight_layout()
      plt.show()

plot_histograms()