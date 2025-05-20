import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')

df_rio = df[(df['uf'] == 'Rio de Janeiro') & (df['ano'].between(2013, 2017))]

chegadas_rio_mensal = df_rio.groupby(['ano', 'cod mes'])['chegadas'].sum().reset_index()

chegadas_rio_mensal['data'] = pd.to_datetime(chegadas_rio_mensal['ano'].astype(str) + '-' + chegadas_rio_mensal['cod mes'].astype(str) + '-01')

datas_completas = pd.date_range(start='2013-01-01', end='2017-12-01', freq='MS')
df_datas = pd.DataFrame({'data': datas_completas})

df_final_rio = df_datas.merge(chegadas_rio_mensal[['data', 'chegadas']], on='data', how='left')
df_final_rio['chegadas'] = df_final_rio['chegadas'].fillna(0).astype(int)

xticks_labels = df_final_rio['data'].dt.strftime('%Y-%m')
xticks_to_show = []

for i, date in enumerate(df_final_rio['data']):
    label = date.strftime('%Y-%m')
    if (i % 4 == 0) or (label in ['2014-01', '2016-08']):
        xticks_to_show.append(label)
    else:
        xticks_to_show.append('')

plt.figure(figsize=(14, 6))
plt.plot(df_final_rio['data'], df_final_rio['chegadas'], marker='o', color='dodgerblue')
plt.title('Chegadas de Estrangeiros no Rio de Janeiro (2013–2017)', fontsize=14)
plt.xlabel('Data (Ano-Mês)')
plt.ylabel('Total de Chegadas')
plt.grid(True)
plt.xticks(df_final_rio['data'], xticks_to_show, rotation=45)
plt.tight_layout()
plt.show()
