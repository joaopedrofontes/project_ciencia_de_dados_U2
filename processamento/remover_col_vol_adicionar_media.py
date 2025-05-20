import pandas as pd

df = pd.read_csv('../valorizacao_csv_original/ARS_BRL Dados Históricos.csv', sep=',', encoding='UTF-8')

df = df.drop(columns=['Vol.'])

for col in ['Máxima', 'Mínima']:
    df[col] = df[col].str.replace('.', '', regex=False)  # Remove separador de milhar (se existir)
    df[col] = df[col].str.replace(',', '.', regex=False).astype(float)

df['média'] = ((df['Máxima'] + df['Mínima']) / 2).round(4)

df['média'] = df['média'].astype(str).str.replace('.', ',')

df.to_csv('../valorizacao_csv_processado/ARS_BRL_Dados_Históricos_v2.csv', sep=',', index=False, encoding='UTF-8', quoting=1)
