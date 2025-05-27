import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('../../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')


df_usa_aerea_trim = df[
    (df['país'] == 'Estados Unidos') &
    (df['via'] == 'Aérea') &
    (df['ano'].between(2000, 2002)) &
    (df['cod mes'].isin([9, 10, 11]))
]

chegadas_agrupadas = df_usa_aerea_trim.groupby(['ano', 'cod mes'])['chegadas'].sum().reset_index()

anos_periodo = range(2000, 2003)
meses_periodo = [9, 10, 11]
idx_completo = pd.MultiIndex.from_product([anos_periodo, meses_periodo], names=['ano', 'cod mes'])
df_base_plotagem = pd.DataFrame(index=idx_completo).reset_index()


df_plot = pd.merge(df_base_plotagem, chegadas_agrupadas, on=['ano', 'cod mes'], how='left')
df_plot['chegadas'] = df_plot['chegadas'].fillna(0).astype(int)


plt.figure(figsize=(12, 7))
anos_para_plotar = sorted(df_plot['ano'].unique())
nomes_meses_map = {9: 'Setembro', 10: 'Outubro', 11: 'Novembro'}

cores_anos = {
    2000: 'steelblue',
    2001: 'firebrick',
    2002: 'seagreen'
}

for ano in anos_para_plotar:
    df_ano = df_plot[df_plot['ano'] == ano].sort_values('cod mes')

    plt.plot(
        df_ano['cod mes'].map(nomes_meses_map),
        df_ano['chegadas'],
        marker='o',
        linestyle='--' if ano == 2001 else '-',
        linewidth=2.8 if ano == 2001 else 1.8,
        color=cores_anos[ano],
        label=str(ano),
        zorder=5 if ano == 2001 else 1
    )

# Estética
plt.xlabel('Mês')
plt.ylabel('Chegadas dos EUA por Via Aérea')
plt.title('Chegadas dos EUA por via aérea em setembro, outubro e novembro (2000-2002)')
plt.legend(title='Ano', loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
#plt.show()
plt.savefig("grafico_eua_2001.png")
