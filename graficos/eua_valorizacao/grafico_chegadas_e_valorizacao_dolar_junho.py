import pandas as pd
import matplotlib.pyplot as plt

# Carrega o histórico da cotação do dólar
val_df = pd.read_csv('../../valorizacao_csv_processado/USD_BRL_Dados_Históricos_v2.csv', sep=',', encoding='UTF-8')

# Filtra apenas os dados de 01 de junho de cada ano
val_junho = val_df[val_df['Data'].str.startswith('01.06.')].copy()
val_junho['ano'] = val_junho['Data'].str[-4:].astype(int)
val_junho['média'] = val_junho['média'].str.replace(',', '.', regex=False).astype(float)
val_junho = val_junho[val_junho['ano'] >= 1995]
val_junho = val_junho.sort_values(by='ano')

# Carrega os dados de chegadas
cheg_df = pd.read_csv('../../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')

# Filtra apenas chegadas dos EUA em junho
cheg_junho = cheg_df[(cheg_df['cod mes'] == 6) & (cheg_df['ano'] >= 1995)]
cheg_junho_eua = cheg_junho[cheg_junho['país'] == 'Estados Unidos']
chegadas_por_ano_jun = cheg_junho_eua.groupby('ano')['chegadas'].sum().reset_index()

# Cria o gráfico com dois eixos Y
fig, ax1 = plt.subplots(figsize=(13, 6))

# Eixo da cotação do dólar
ax1.plot(val_junho['ano'], val_junho['média'], color='green', marker='o', label='Valor Médio do Dólar (R$)')
ax1.set_xlabel('Ano')
ax1.set_ylabel('Valor Médio do Dólar (R$)', color='green')
ax1.tick_params(axis='y', labelcolor='green')

# Eixo das chegadas
ax2 = ax1.twinx()
ax2.plot(chegadas_por_ano_jun['ano'], chegadas_por_ano_jun['chegadas'], color='royalblue', marker='s', label='Chegadas (Estados Unidos)')
ax2.set_ylabel('Total de Chegadas', color='royalblue')
ax2.tick_params(axis='y', labelcolor='royalblue')
ax2.set_ylim(0, 140000)

# Eixo X
anos = list(range(1995, 2025))
ax1.set_xticks(anos)
ax1.set_xticklabels(anos, rotation=45)

# Título e ajustes
plt.title('Chegadas de estadunidenses e valor do dólar em junho (1995-2024)', fontsize=14)
fig.tight_layout()
plt.grid(True)

# Salvar imagem (opcional)
plt.savefig('chegadas_eua_dolar_junho_1995_2024.png', dpi=300)

plt.show()
