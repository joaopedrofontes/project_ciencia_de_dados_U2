# Gráfico comparando as chegadas por mês, em Pernambuco, durante o período da Copa do Mundo

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')

df_pe = df[(df['uf'] == 'Pernambuco') & (df['ano'].between(2013, 2015))]

chegadas_pe_mensal = df_pe.groupby(['ano', 'cod mes'])['chegadas'].sum().reset_index()

chegadas_pe_mensal['data'] = pd.to_datetime(chegadas_pe_mensal['ano'].astype(str) + '-' + chegadas_pe_mensal['cod mes'].astype(str) + '-01')

datas_completas = pd.date_range(start='2013-01-01', end='2015-12-01', freq='MS')
df_datas = pd.DataFrame({'data': datas_completas})

df_final_pe = df_datas.merge(chegadas_pe_mensal[['data', 'chegadas']], on='data', how='left')
df_final_pe['chegadas'] = df_final_pe['chegadas'].fillna(0).astype(int)

plt.figure(figsize=(14, 6))
plt.plot(df_final_pe['data'], df_final_pe['chegadas'], marker='o', color='darkblue')
plt.title('Chegadas de Estrangeiros em Pernambuco (2013–2015)', fontsize=14)
plt.xlabel('Data (Ano-Mês)')
plt.ylabel('Total de Chegadas')
plt.grid(True)
plt.xticks(df_final_pe['data'], df_final_pe['data'].dt.strftime('%Y-%m'), rotation=45)
plt.tight_layout()
plt.show()
