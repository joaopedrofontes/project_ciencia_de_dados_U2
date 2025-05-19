import pandas as pd
import os

pasta_entrada = '../chegadas_csv_original/'
pasta_saida = '../chegadas_csv_processados/'
arquivo_saida = os.path.join(pasta_saida, 'chegadas_1995_to_2024_concatenadas.csv')

anos = list(range(2024, 1994, -1))

df_padrao = pd.read_csv(os.path.join(pasta_entrada, 'chegadas_2024.csv'), sep=';', encoding='ISO-8859-1')
colunas_padrao = df_padrao.columns.tolist()

dfs = []

for ano in anos:
    caminho = os.path.join(pasta_entrada, f'chegadas_{ano}.csv')

    try:
        df = pd.read_csv(caminho, sep=';', encoding='ISO-8859-1')

        df.columns = colunas_padrao

        dfs.append(df)
        print(f"> Adicionado: {ano}")

    except Exception as e:
        print(f"Erro ao processar {ano}: {e}")

df_total = pd.concat(dfs, ignore_index=True)

try:
    df_total['Chegadas'] = df_total['Chegadas'].astype('Int64')  # Suporta NaN
    print("\n✔️ Coluna 'Chegadas' convertida para inteiro com sucesso.")
except Exception as e:
    print(f"❌ Erro ao converter 'Chegadas' para inteiro: {e}")

df_total.to_csv(arquivo_saida, index=False, sep=';', encoding='ISO-8859-1')
print(f"\n✅ Arquivo final salvo com sucesso em: {arquivo_saida}")
