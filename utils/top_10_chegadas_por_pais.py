import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')

df = df[df['ano'] >= 2005]

df['chegadas'] = pd.to_numeric(df['chegadas'], errors='coerce')


top_paises = df.groupby('país')['chegadas'].sum().nlargest(10)

plt.figure(figsize=(10, 6))
top_paises.plot(kind='bar', color='coral', edgecolor='black')
plt.title('Top 10 Países com Mais Chegadas')
plt.xlabel('País')
plt.ylabel('Quantidade de Chegadas')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
