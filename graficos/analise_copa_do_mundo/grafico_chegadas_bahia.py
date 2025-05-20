import pandas as pd
import matplotlib.pyplot as plt

# Carregamento e filtragem
df = pd.read_csv('../../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')
df_bahia = df[(df['uf'] == 'Bahia') & (df['ano'].between(2013, 2015))]

# Agrupamento
chegadas_bahia_mensal = df_bahia.groupby(['ano', 'cod mes'])['chegadas'].sum().reset_index()
chegadas_bahia_mensal['data'] = pd.to_datetime(chegadas_bahia_mensal['ano'].astype(str) + '-' + chegadas_bahia_mensal['cod mes'].astype(str) + '-01')

# Preenchimento de datas faltantes
datas_completas = pd.date_range(start='2013-01-01', end='2015-12-01', freq='MS')
df_datas = pd.DataFrame({'data': datas_completas})
df_final = df_datas.merge(chegadas_bahia_mensal[['data', 'chegadas']], on='data', how='left')
df_final['chegadas'] = df_final['chegadas'].fillna(0).astype(int)

# Plot como gráfico de colunas (barras verticais)
plt.figure(figsize=(14, 6))
plt.bar(df_final['data'], df_final['chegadas'], color='darkblue', width=20)
plt.xlabel('Data (Ano-Mês)')
plt.ylabel('Total de Chegadas')
plt.xticks(df_final['data'], df_final['data'].dt.strftime('%Y-%m'), rotation=45)

# Remover título, grid e bordas superiores/direitas
plt.title('')
plt.grid(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()

# Salvar como PNG com fundo transparente
plt.savefig('chegadas_bahia_colunas.png', transparent=True, dpi=300)
plt.close()
