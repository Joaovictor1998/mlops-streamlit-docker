import pandas as pd 
from sklearn.datasets import make_regression


# Criar 1000 linhas de dados com 3 características (features)
x, y = make_regression(n_samples=1000, n_features=3, noise=10.5, random_state=42)

# Transformar em um DataFrame do Pandas para ficar organizado
df = pd.DataFrame(x, columns=['idade', 'renda_mensal', 'tempo_casa_anos'])
df['target'] = y

# Salvar como o seu arquivo de "Referência"
df.to_csv('dados_treinamento.csv', index=False)
print('Dataset de treinamento criado com sucesso!')