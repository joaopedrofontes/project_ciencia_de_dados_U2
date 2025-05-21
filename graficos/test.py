import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Nomes dos meses em português
meses_pt = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# Carrega o dataset
df = pd.read_csv('../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')

# Filtra apenas para turistas europeus a partir de 1995
df_europa = df[(df['ano'] >= 1995) & (df['país'] == 'Argentina')]

# Agrupamento por mês
chegadas_por_mes_europa = df_europa.groupby('cod mes')['chegadas'].sum().reset_index()
chegadas_por_mes_europa['nome_mes'] = chegadas_por_mes_europa['cod mes'].apply(lambda x: meses_pt[x - 1])
chegadas_por_mes_europa = chegadas_por_mes_europa.sort_values(by='cod mes')

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(data=chegadas_por_mes_europa, x='nome_mes', y='chegadas', color='darkblue', edgecolor='black')

# Ajustes visuais
plt.xlabel('Mês')
plt.ylabel('Total de Chegadas (Europa)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Eixo Y com separador de milhar por espaço
plt.gca().yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda x, _: f'{int(x):,}'.replace(',', ' '))
)

# Remove o título
plt.title('')

# Salvar imagem
plt.savefig('chegadas_europeus_por_mes_todos_os_anos.png', dpi=300, transparent=True)

plt.show()
