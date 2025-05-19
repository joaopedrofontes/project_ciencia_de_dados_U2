# REMOVER a coluna mês e deixar todas as colunas em letras minúsculas.
import pandas as pd

df = pd.read_csv('../chegadas_csv_processados/chegadas_1995_to_2024_concatenadas.csv', sep=';', encoding='ISO-8859-1')

df = df.drop(columns=['Mês'])

df.columns = [col.lower() for col in df.columns]

df['chegadas'] = df['chegadas'].astype('Int64')

df.to_csv('../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv',
          index=False, sep=';', encoding='ISO-8859-1')