import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Carregar e processar os dados
df = pd.read_csv('../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')
df = df[df['ano'] >= 1995]
df['chegadas'] = pd.to_numeric(df['chegadas'], errors='coerce')

# Agrupar e obter os top 10 países
top_paises = df.groupby('país')['chegadas'].sum().nlargest(10)

# Função para formatar com separador de milhar (espaço)
def formatar_milhar(x, pos):
    return f'{int(x):,}'.replace(',', ' ')

formatter = FuncFormatter(formatar_milhar)

# Plot
plt.figure(figsize=(10, 6))
ax = top_paises.plot(kind='bar', color='coral', edgecolor='black')
ax.yaxis.set_major_formatter(formatter)

plt.title('')
plt.xlabel('País')
plt.ylabel('Quantidade de Chegadas')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Salvar como PNG com fundo transparente
plt.savefig('top10_paises_chegadas.png', transparent=True, dpi=300)
plt.show()
