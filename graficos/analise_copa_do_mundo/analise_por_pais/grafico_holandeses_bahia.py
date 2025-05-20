
#Gráfico comparando as chegadas de holandeses por mês, na Bahia, durante o período da copa do mundo


import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('../../../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')


df_holanda_bahia = df[(df['uf'] == 'Bahia') &
                      (df['ano'].between(2013, 2015)) &
                      (df['país'] == 'Holanda')]

chegadas_holanda_bahia_mensal = df_holanda_bahia.groupby(['ano', 'cod mes'])['chegadas'].sum().reset_index()

chegadas_holanda_bahia_mensal['data'] = pd.to_datetime(chegadas_holanda_bahia_mensal['ano'].astype(str) + '-' + chegadas_holanda_bahia_mensal['cod mes'].astype(str) + '-01')

datas_completas = pd.date_range(start='2013-01-01', end='2015-12-01', freq='MS')
df_datas = pd.DataFrame({'data': datas_completas})

df_final = df_datas.merge(chegadas_holanda_bahia_mensal[['data', 'chegadas']], on='data', how='left')
df_final['chegadas'] = df_final['chegadas'].fillna(0).astype(int)

plt.figure(figsize=(14, 6))
plt.plot(df_final['data'], df_final['chegadas'], marker='o', color='orange')
plt.title('Chegadas de Holandeses na Bahia (2013–2015)', fontsize=14)
plt.xlabel('Data (Ano-Mês)')
plt.ylabel('Total de Chegadas')
plt.grid(True)
plt.xticks(df_final['data'], df_final['data'].dt.strftime('%Y-%m'), rotation=45)
plt.tight_layout()
plt.show()
