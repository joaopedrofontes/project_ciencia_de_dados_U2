import pandas as pd
import matplotlib.pyplot as plt

# Carregamento do dataset
df = pd.read_csv('../../../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')

# Filtro para chegadas da Alemanha em Pernambuco no período da Copa
df_alemanha_pe = df[(df['uf'] == 'Pernambuco') &
                    (df['ano'].between(2013, 2015)) &
                    (df['país'] == 'Alemanha')]

# Agrupamento por ano e mês
chegadas_alemanha_pe_mensal = df_alemanha_pe.groupby(['ano', 'cod mes'])['chegadas'].sum().reset_index()
chegadas_alemanha_pe_mensal['data'] = pd.to_datetime(chegadas_alemanha_pe_mensal['ano'].astype(str) + '-' + chegadas_alemanha_pe_mensal['cod mes'].astype(str) + '-01')

# Preenchimento de datas faltantes
datas_completas = pd.date_range(start='2013-01-01', end='2015-12-01', freq='MS')
df_datas = pd.DataFrame({'data': datas_completas})
df_final = df_datas.merge(chegadas_alemanha_pe_mensal[['data', 'chegadas']], on='data', how='left')
df_final['chegadas'] = df_final['chegadas'].fillna(0).astype(int)

# Plot do gráfico de colunas
plt.figure(figsize=(14, 6))
plt.bar(df_final['data'], df_final['chegadas'], color='darkblue', width=20)
plt.title('', fontsize=14)
plt.xlabel('Data (Ano-Mês)')
plt.ylabel('Total de Chegadas')
plt.xticks(df_final['data'], df_final['data'].dt.strftime('%Y-%m'), rotation=45)
plt.grid(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()

# Salvar como PNG com fundo transparente
plt.savefig('chegadas_alemanha_pernambuco_colunas.png', dpi=300, transparent=True)
plt.close()
