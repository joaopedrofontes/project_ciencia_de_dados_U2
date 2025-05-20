import pandas as pd

df = pd.read_csv('../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v3.csv', sep=';',
                 encoding='ISO-8859-1')

for ano in range(1995, 2025):
    estados = df[df['ano'] == ano]['uf'].dropna().unique()
    estados_ordenados = sorted(estados)

    print(f"{ano}:")
    for estado in estados_ordenados:
        print(estado)
    print()
