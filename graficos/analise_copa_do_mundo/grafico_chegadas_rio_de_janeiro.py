import pandas as pd
import matplotlib.pyplot as plt

# Leitura e filtragem
df = pd.read_csv('../../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')
df_rio = df[(df['uf'] == 'Rio de Janeiro') & (df['ano'].between(2013, 2017))]

# Agrupamento
chegadas_rio_mensal = df_rio.groupby(['ano', 'cod mes'])['chegadas'].sum().reset_index()
chegadas_rio_mensal['data'] = pd.to_datetime(chegadas_rio_mensal['ano'].astype(str) + '-' + chegadas_rio_mensal['cod mes'].astype(str) + '-01')

# Preenchimento de datas faltantes
datas_completas = pd.date_range(start='2013-01-01', end='2017-12-01', freq='MS')
df_datas = pd.DataFrame({'data': datas_completas})
df_final_rio = df_datas.merge(chegadas_rio_mensal[['data', 'chegadas']], on='data', how='left')
df_final_rio['chegadas'] = df_final_rio['chegadas'].fillna(0).astype(int)

# Gráfico de colunas (barras verticais)
plt.figure(figsize=(14, 6))
plt.bar(df_final_rio['data'], df_final_rio['chegadas'], color='darkblue', width=20)
plt.xlabel('Data (Ano-Mês)')
plt.ylabel('Total de Chegadas')

# Ajuste nos rótulos do eixo X
xticks_labels = df_final_rio['data'].dt.strftime('%Y-%m')
xticks_to_show = []
for i, date in enumerate(df_final_rio['data']):
    label = date.strftime('%Y-%m')
    if (i % 4 == 0) or (label in ['2014-01', '2016-08']):
        xticks_to_show.append(label)
    else:
        xticks_to_show.append('')
plt.xticks(df_final_rio['data'], xticks_to_show, rotation=45)

# Estética
plt.title('')
plt.grid(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()

# Salvar como imagem com fundo transparente
plt.savefig('chegadas_rio_colunas.png', transparent=True, dpi=300)
plt.close()
