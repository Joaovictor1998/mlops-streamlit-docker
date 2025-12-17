import pandas as pd 

# 1. Carrega os dados que você acabou de gerar
df = pd.read_csv('dados_treinamento.csv')

# 2. Vamos simular um Drift na coluna 'renda_mensal'
# Vamos dizer que a renda de todo mundo subiu 3x (inflação ou mudança de público)
df_atual = df.copy()
df_atual['renda_mensal'] = df_atual['renda_mensal'] * 3

# 3. Salva como se fossem os logs da sua API hoje
df_atual.to_csv('logs_api_atuais.csv', index=False)
print("Arquivo 'logs_api_atuais.csv' gerado com sucesso!")
