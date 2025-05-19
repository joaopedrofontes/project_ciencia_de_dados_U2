import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../valorizacao_csv_processado/EUR_BRL_Dados_Históricos_v2.csv', sep=',', encoding='UTF-8')

df_janeiro = df[df['Data'].str.startswith('01.01.')].copy()

df_janeiro['ano'] = df_janeiro['Data'].str[-4:].astype(int)
df_janeiro['média'] = df_janeiro['média'].str.replace(',', '.', regex=False).astype(float)

df_janeiro = df_janeiro[df_janeiro['ano'] >= 2002]

df_janeiro = df_janeiro.sort_values(by='ano')

plt.figure(figsize=(12, 6))
plt.plot(df_janeiro['ano'], df_janeiro['média'], marker='o', linestyle='-', color='royalblue')
plt.title('Valor Médio do Euro em Janeiro de Cada Ano', fontsize=14)
plt.xlabel('Ano')
plt.ylabel('Valor Médio (R$)')
plt.grid(True)
plt.xticks(df_janeiro['ano'], rotation=45)
plt.tight_layout()
plt.show()
