import pandas as pd
import matplotlib.pyplot as plt

val_df = pd.read_csv('../valorizacao_csv_processado/ARS_BRL_Dados_Históricos_v2.csv', sep=',', encoding='UTF-8')

val_df['ano'] = val_df['Data'].str[-4:].astype(int)
val_df['média'] = val_df['média'].str.replace(',', '.', regex=False).astype(float)

val_anual = val_df[val_df['ano'] >= 2005].groupby('ano')['média'].mean().reset_index()

cheg_df = pd.read_csv('../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')

cheg_arg = cheg_df[(cheg_df['país'] == 'Argentina') & (cheg_df['ano'] >= 2005)]
chegadas_anual = cheg_arg.groupby('ano')['chegadas'].sum().reset_index()

fig, ax1 = plt.subplots(figsize=(13, 6))

ax1.plot(val_anual['ano'], val_anual['média'], color='royalblue', marker='o', label='Valor Médio do Peso (R$)')
ax1.set_xlabel('Ano')
ax1.set_ylabel('Valor Médio do Peso (R$)', color='royalblue')
ax1.tick_params(axis='y', labelcolor='royalblue')

ax2 = ax1.twinx()
ax2.plot(chegadas_anual['ano'], chegadas_anual['chegadas'], color='darkorange', marker='s', label='Chegadas (Argentina)')
ax2.set_ylabel('Total de Chegadas', color='darkorange')
ax2.tick_params(axis='y', labelcolor='darkorange')

anos = list(range(2005, 2025))
ax1.set_xticks(anos)
ax1.set_xticklabels(anos, rotation=45)

plt.title('Valor Médio do Peso e Chegadas dos Argentinos ao Brasil (2005–2024)', fontsize=14)

fig.tight_layout()
plt.grid(True)
plt.show()
