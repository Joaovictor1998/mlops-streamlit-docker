import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# 1. Criamos dados com um valor faltando (np.nan)
dados = pd.DataFrame({'renda': [2000, 3000, np.nan, 5000]})
print("Antes (com buraco):")
print(dados)

# 2. Configuramos o 'tapa-buraco' para usar a média
imputador = SimpleImputer(strategy='mean')

# 3. Aplicamos nos dados
dados_preenchidos = imputador.fit_transform(dados)

print("\nDepois (buraco preenchido com a média 3333.33):")
print(dados_preenchidos)
