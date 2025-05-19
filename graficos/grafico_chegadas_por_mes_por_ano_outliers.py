import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import calendar

df = pd.read_csv('../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')

chegadas_mensais = df.groupby(['ano', 'cod mes'])['chegadas'].sum().reset_index()

anos_excluidos = [2014, 2016, 2020, 2021]
media_historica = chegadas_mensais[~chegadas_mensais['ano'].isin(anos_excluidos)]
media_mensal = media_historica.groupby('cod mes')['chegadas'].mean().reset_index()
media_mensal['ano'] = 'Média histórica'

anos_especiais = chegadas_mensais[chegadas_mensais['ano'].isin(anos_excluidos)]

df_final = pd.concat([media_mensal, anos_especiais], ignore_index=True)

df_final['nome_mes'] = df_final['cod mes'].apply(lambda x: calendar.month_name[x])

df_final = df_final.sort_values(by=['ano', 'cod mes'])

plt.figure(figsize=(14, 7))
sns.lineplot(data=df_final, x='cod mes', y='chegadas', hue='ano', palette='Set1', marker='o')
plt.title('Chegadas por Mês — Comparação de Eventos Especiais com Média Histórica', fontsize=16)
plt.xlabel('Mês')
plt.ylabel('Total de Chegadas')
plt.xticks(ticks=range(1, 13), labels=calendar.month_abbr[1:])
plt.legend(title='Ano / Média', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('../imagens/grafico_chegadas_mensal_por_ano_outliers.png', dpi=300)
plt.show()