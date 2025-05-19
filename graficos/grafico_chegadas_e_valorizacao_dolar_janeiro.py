
# Gráfico com chegadas de estrangeiros dos EUA e valorização do dólar em relação ao real.
# Comparação entre janeiro de cada ano (1994-2024)


import pandas as pd
import matplotlib.pyplot as plt

val_df = pd.read_csv('../valorizacao_csv_processado/USD_BRL_Dados_Históricos_v2.csv', sep=',', encoding='UTF-8')
val_janeiro = val_df[val_df['Data'].str.startswith('01.01.')].copy()
val_janeiro['ano'] = val_janeiro['Data'].str[-4:].astype(int)
val_janeiro['média'] = val_janeiro['média'].str.replace(',', '.', regex=False).astype(float)
val_janeiro = val_janeiro[val_janeiro['ano'] >= 1995]
val_janeiro = val_janeiro.sort_values(by='ano')

cheg_df = pd.read_csv('../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')

cheg_janeiro = cheg_df[(cheg_df['cod mes'] == 1) & (cheg_df['ano'] >= 1995)]
cheg_janeiro_eua = cheg_janeiro[cheg_janeiro['país'] == 'Estados Unidos']
chegadas_por_ano_jan = cheg_janeiro_eua.groupby('ano')['chegadas'].sum().reset_index()

fig, ax1 = plt.subplots(figsize=(13, 6))

ax1.plot(val_janeiro['ano'], val_janeiro['média'], color='royalblue', marker='o', label='Valor Médio do Dólar (R$)')
ax1.set_xlabel('Ano')
ax1.set_ylabel('Valor Médio do Dólar (R$)', color='royalblue')
ax1.tick_params(axis='y', labelcolor='royalblue')

ax2 = ax1.twinx()
ax2.plot(chegadas_por_ano_jan['ano'], chegadas_por_ano_jan['chegadas'], color='darkorange', marker='s', label='Chegadas (Estados Unidos)')
ax2.set_ylabel('Total de Chegadas', color='darkorange')
ax2.tick_params(axis='y', labelcolor='darkorange')

anos = list(range(1995, 2025))
ax1.set_xticks(anos)
ax1.set_xticklabels(anos, rotation=45)

plt.title('Valor Médio do dólar e Chegadas dos Estados Unidos ao Brasil (Janeiro, 1995–2024)', fontsize=14)

fig.tight_layout()
plt.grid(True)
plt.show()
