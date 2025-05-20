# REMOVER a coluna 'via' da versão v2
import pandas as pd

df = pd.read_csv('../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v2.csv', sep=';', encoding='ISO-8859-1')

df = df.drop(columns=['via'])

df['chegadas'] = df['chegadas'].astype('Int64')

df.to_csv('../chegadas_csv_processados/chegadas_1995_to_2024_concatenados_v3.csv',
          index=False, sep=';', encoding='ISO-8859-1')
