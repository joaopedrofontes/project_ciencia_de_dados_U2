import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')

euro_2002_paises = [
    'Alemanha', 'Áustria', 'Bélgica', 'Espanha', 'Finlândia',
    'França', 'Grécia', 'Irlanda', 'Itália', 'Luxemburgo',
    'Países Baixos', 'Portugal'
]

df_janeiro = df[(df['cod mes'] == 1) & (df['ano'] >= 2002)]

df_janeiro_euro = df_janeiro[df_janeiro['país'].isin(euro_2002_paises)]

chegadas_por_ano = df_janeiro_euro.groupby('ano')['chegadas'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(chegadas_por_ano['ano'], chegadas_por_ano['chegadas'], marker='o', linestyle='-', color='royalblue')
plt.title('Chegadas em Janeiro (2002–2024) - Países que Adotaram o Euro em 2002', fontsize=14)
plt.xlabel('Ano')
plt.ylabel('Total de Chegadas')
plt.xticks(ticks=range(2002,2025))
plt.grid(True)
plt.tight_layout()
plt.show()
