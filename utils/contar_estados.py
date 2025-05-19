import pandas as pd

df = pd.read_csv('../chegadas_csv_original/chegadas_2024.csv', sep=';', encoding='ISO-8859-1')

quantidade_estados = df['cod uf'].nunique()

print(f"Número de estados diferentes na coluna 'UF': {quantidade_estados}")
