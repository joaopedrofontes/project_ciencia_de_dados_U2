import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Nomes dos meses em português
meses_pt = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# Carrega o dataset
df = pd.read_csv('../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')

# Mantém dados a partir de 1995 (sem exclusão de anos)
df = df[df['ano'] >= 1995]

# Agrupamento por mês
chegadas_por_mes = df.groupby('cod mes')['chegadas'].sum().reset_index()
chegadas_por_mes['nome_mes'] = chegadas_por_mes['cod mes'].apply(lambda x: meses_pt[x - 1])
chegadas_por_mes = chegadas_por_mes.sort_values(by='cod mes')

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(data=chegadas_por_mes, x='nome_mes', y='chegadas', color='darkblue', edgecolor='black')

# Ajustes visuais
plt.xlabel('Mês')
plt.ylabel('Total de Chegadas')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Eixo Y com separador de milhar por espaço
plt.gca().yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda x, _: f'{int(x):,}'.replace(',', ' '))
)

plt.title('Total de chegadas por mês (1995-2024)')

# Salvar imagem
plt.savefig('chegadas_por_mes_com_todos_os_anos.png', dpi=300, transparent=True)

plt.show()
