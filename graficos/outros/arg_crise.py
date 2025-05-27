import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('../../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')

# Filtrar dados da Argentina para janeiro dos anos desejados e via aérea
df_arg_jan_aire = df[
    (df['país'] == 'Argentina') &
    (df['cod mes'] == 1) &
    (df['ano'].isin([1999, 2000, 2001, 2002, 2003, 2004])) &
    (df['via'] == 'Aérea')  # ajuste o nome e valor conforme seu dataset
]

# Agrupar por ano e somar chegadas
chegadas_arg_aire = df_arg_jan_aire.groupby('ano')['chegadas'].sum().reset_index()

# Plotar gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(chegadas_arg_aire['ano'].astype(str), chegadas_arg_aire['chegadas'], color='darkorange', width=0.6)

plt.xlabel('Ano')
plt.ylabel('Total de Chegadas (Via Aérea)')
plt.title('')
plt.grid(False)
plt.tight_layout()
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.savefig('chegadas_argentina_janeiro_1999_2004.png', dpi=300, transparent=True)
plt.show()