import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../valorizacao_csv_processado/EUR_BRL_Dados_Históricos_v2.csv', sep=',', encoding='UTF-8')

df_junho = df[df['Data'].str.startswith('01.06.')].copy()

df_junho['ano'] = df_junho['Data'].str[-4:].astype(int)
df_junho['média'] = df_junho['média'].str.replace(',', '.', regex=False).astype(float)

df_junho = df_junho[df_junho['ano'] >= 2002]

df_junho = df_junho.sort_values(by='ano')

plt.figure(figsize=(12, 6))
plt.plot(df_junho['ano'], df_junho['média'], marker='o', linestyle='-', color='royalblue')
plt.title('Valor Médio do Euro em Junho de Cada Ano', fontsize=14)
plt.xlabel('Ano')
plt.ylabel('Valor Médio (R$)')
plt.grid(True)
plt.xticks(df_junho['ano'], rotation=45)
plt.tight_layout()
plt.show()
