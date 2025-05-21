import pandas as pd
import matplotlib.pyplot as plt

# Leitura e filtragem
df = pd.read_csv('../../../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')

df_alemanha_bahia = df[
    (df['uf'] == 'Bahia') &
    (df['ano'].between(2013, 2015)) &
    (df['país'] == 'Alemanha')
]

# Agrupamento
chegadas_alemanha_bahia_mensal = df_alemanha_bahia.groupby(['ano', 'cod mes'])['chegadas'].sum().reset_index()
chegadas_alemanha_bahia_mensal['data'] = pd.to_datetime(
    chegadas_alemanha_bahia_mensal['ano'].astype(str) + '-' + chegadas_alemanha_bahia_mensal['cod mes'].astype(str) + '-01'
)

# Preenchimento de datas ausentes
datas_completas = pd.date_range(start='2013-01-01', end='2015-12-01', freq='MS')
df_datas = pd.DataFrame({'data': datas_completas})
df_final = df_datas.merge(chegadas_alemanha_bahia_mensal[['data', 'chegadas']], on='data', how='left')
df_final['chegadas'] = df_final['chegadas'].fillna(0).astype(int)

# Gráfico de barras
plt.figure(figsize=(14, 6))
plt.bar(df_final['data'], df_final['chegadas'], color='darkblue', width=20)
plt.xlabel('Data (Ano-Mês)')
plt.ylabel('Total de Chegadas')
plt.xticks(df_final['data'], df_final['data'].dt.strftime('%Y-%m'), rotation=45)

# Estilo e layout
plt.title('')
plt.grid(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()

# Salvar como imagem com fundo transparente
plt.savefig('chegadas_alemanha_bahia_colunas.png', transparent=True, dpi=300)
plt.close()
