import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos dados de chegadas
cheg_df = pd.read_csv('../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')
cheg_df.columns = cheg_df.columns.str.strip().str.lower()

# Filtra para Estados Unidos e converte 'chegadas' para numérico
cheg_df = cheg_df[cheg_df['país'] == 'Estados Unidos']
cheg_df['chegadas'] = pd.to_numeric(cheg_df['chegadas'], errors='coerce')

# Soma as chegadas por ano
chegadas_ano = cheg_df.groupby('ano')['chegadas'].sum().reset_index()

# Leitura dos dados do dólar
dolar_df = pd.read_csv('../valorizacao_csv_processado/USD_BRL_Dados_Históricos_v2.csv', sep=',', encoding='UTF-8')
dolar_df.columns = dolar_df.columns.str.strip().str.lower()

# Converte a coluna 'média' para float
dolar_df['média'] = dolar_df['média'].str.replace(',', '.', regex=False).astype(float)

# Extrai o ano da data (assume formato 'dd.mm.aaaa')
dolar_df['ano'] = dolar_df['data'].str[-4:].astype(int)

# Calcula a média anual do dólar
media_dolar_ano = dolar_df.groupby('ano')['média'].mean().reset_index()

# Junta os dois DataFrames pelo ano
merged = pd.merge(chegadas_ano, media_dolar_ano, on='ano')

# Plotagem
fig, ax1 = plt.subplots(figsize=(13, 6))

# Chegadas (Eixo Y da esquerda)
ax1.plot(merged['ano'], merged['chegadas'], color='darkorange', marker='o', label='Chegadas (EUA)')
ax1.set_xlabel('Ano')
ax1.set_ylabel('Total de Chegadas', color='darkorange')
ax1.tick_params(axis='y', labelcolor='darkorange')

# Dólar (Eixo Y da direita)
ax2 = ax1.twinx()
ax2.plot(merged['ano'], merged['média'], color='royalblue', marker='s', label='Valor Médio Anual do Dólar (R$)')
ax2.set_ylabel('Valor Médio do Dólar (R$)', color='royalblue')
ax2.tick_params(axis='y', labelcolor='royalblue')

# Eixo X
ax1.set_xticks(merged['ano'])
ax1.set_xticklabels(merged['ano'], rotation=45)

plt.title('Chegadas dos EUA e Valor Médio do Dólar (Ano a Ano)', fontsize=14)
fig.tight_layout()
plt.grid(True)
plt.show()
