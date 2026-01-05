
# Projeto de Análise Estelionato no RJ
# Ferramentas: Python (pandas, matplotlib)

import pandas as pd
import matplotlib.pyplot as plt

# Carregar base de dados
df = pd.read_csv('BaseDPEvolucaoMensalCisp.csv', sep=';', encoding='latin1')

# Filtrar crime de Estelionato
df_est = df[df['Tipo Crime'].str.contains('ESTELIONATO', case=False, na=False)]

# Criar coluna Data
df_est['Data'] = pd.to_datetime(df_est['Ano'].astype(str) + '-' + df_est['Mês'].astype(str) + '-01')

# Evolução mensal
evolucao = df_est.groupby('Data')['Quantidade'].sum().reset_index()

# Plotar gráfico de evolução
plt.figure()
plt.plot(evolucao['Data'], evolucao['Quantidade'])
plt.title('Evolução Mensal do Estelionato no RJ')
plt.xlabel('Ano')
plt.ylabel('Ocorrências')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Ranking de delegacias
ranking = (
    df_est.groupby('CISP')['Quantidade']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print('Top 10 Delegacias com mais registros de Estelionato:')
print(ranking)
