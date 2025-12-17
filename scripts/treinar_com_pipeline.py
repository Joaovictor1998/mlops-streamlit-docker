import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression

# 1. Dados de treino (com alguns buracos propositais)
x_treino = pd.DataFrame({'idade': [25, 30, 40, 35, 22],
                         'renda': [5000, 6000, 8000, 4500, None]}) # Note o None
y_treino = [1, 1, 0, 1, 1] # Ex: Aprovado ou não

# 2. Criamos o COMBO (Pipeline)
# Passo 1: Limpa (Imputer) -> Passo 2: Preve (Model)
combo_modelo = Pipeline([
    ('limpador', SimpleImputer(strategy='median')),
    ('modelo_ia', LinearRegression())
])

# 3. Treinamos o COMBO inteiro de uma vez
combo_modelo.fit(x_treino, y_treino)

# 4. Salvamos o combo completo em UM ÚNICO ARQUIVO
joblib.dump(combo_modelo, 'modelo_final_blindado.pkl')

print("✅ Combo salvo! Agora o modelo sabe se limpar sozinho.")
