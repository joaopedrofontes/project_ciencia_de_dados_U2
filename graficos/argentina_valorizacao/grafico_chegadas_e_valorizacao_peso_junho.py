import pandas as pd
import matplotlib.pyplot as plt

# Carrega o CSV com a valorização da moeda
val_df = pd.read_csv('../../valorizacao_csv_processado/ARS_BRL_Dados_Históricos_v2.csv', sep=',', encoding='UTF-8')

# Filtra apenas os dias 01 de junho de cada ano
val_junho = val_df[val_df['Data'].str.startswith('01.06.')].copy()
val_junho['ano'] = val_junho['Data'].str[-4:].astype(int)
val_junho['média'] = val_junho['média'].str.replace(',', '.', regex=False).astype(float)
val_junho = val_junho[val_junho['ano'] >= 2005]
val_junho = val_junho.sort_values(by='ano')

# Carrega os dados de chegadas
cheg_df = pd.read_csv('../../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')

# Filtra chegadas no mês de junho (cod mes == 6) a partir de 2005
cheg_junho = cheg_df[(cheg_df['cod mes'] == 6) & (cheg_df['ano'] >= 2005)]
cheg_junho_arg = cheg_junho[cheg_junho['país'] == 'Argentina']
chegadas_por_ano_jun = cheg_junho_arg.groupby('ano')['chegadas'].sum().reset_index()

# Gráfico
fig, ax1 = plt.subplots(figsize=(13, 6))

ax1.plot(val_junho['ano'], val_junho['média'], color='green', marker='o', label='Valor Médio do Peso (R$)')
ax1.set_xlabel('Ano')
ax1.set_ylabel('Valor Médio do Peso (R$)', color='green')
ax1.tick_params(axis='y', labelcolor='green')

ax2 = ax1.twinx()
ax2.plot(chegadas_por_ano_jun['ano'], chegadas_por_ano_jun['chegadas'], color='royalblue', marker='s', label='Chegadas (Argentina)')
ax2.set_ylabel('Total de Chegadas', color='royalblue')
ax2.tick_params(axis='y', labelcolor='royalblue')

anos = list(range(2005, 2025))
ax1.set_xticks(anos)
ax1.set_xticklabels(anos, rotation=45)

plt.title('Chegadas de argentinos e valor do peso em junho (2005-2024)', fontsize=14)

fig.tight_layout()
plt.grid(True)
plt.savefig('chegadas_argentina_peso_junho_2005_2024.png', dpi=300)
plt.show()
