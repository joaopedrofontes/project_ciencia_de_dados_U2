import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import calendar

df = pd.read_csv('../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')

chegadas_mensais = df.groupby(['ano', 'cod mes'])['chegadas'].sum().reset_index()

chegadas_mensais['nome_mes'] = chegadas_mensais['cod mes'].apply(lambda x: calendar.month_name[x])

chegadas_mensais = chegadas_mensais.sort_values(by=['ano', 'cod mes'])

plt.figure(figsize=(14, 7))
sns.lineplot(data=chegadas_mensais, x='cod mes', y='chegadas', hue='ano', palette='tab20', marker='o')
plt.title('Chegadas por Mês e Ano (1995–2024)', fontsize=16)
plt.xlabel('Mês')
plt.ylabel('Total de Chegadas')
plt.xticks(ticks=range(1, 13), labels=calendar.month_abbr[1:])
plt.legend(title='Ano', bbox_to_anchor=(1.05, 1), loc='upper left', ncol=2)
plt.tight_layout()
plt.savefig('../imagens/grafico_chegadas_mensal_por_ano.png', dpi=300)

plt.show()
