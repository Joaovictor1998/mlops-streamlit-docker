import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier

# 1. Dados de treino com Números e Palavras
X_treino = pd.DataFrame({
    'idade': [25, 30, 40, 35, 22], 
    'renda': [5000, 6000, 8000, 4500, None], # Tem um NaN
    'plano': ['Bronze', 'Prata', 'Ouro', 'Prata', 'Bronze'] # Palavras!
})
y_treino = [0, 1, 1, 1, 0] # Ex: Comprou seguro (0=Não, 1=Sim)

# 2. Definimos o que fazer com cada tipo de coluna
# Para números: tapa os buracos com a mediana
num_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median'))
])

# Para categorias: transforma as palavras em colunas de 0 e 1
cat_transformer = Pipeline(steps=[
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

# 3. O Maestro (ColumnTransformer) - Une as transformações
pre_processador = ColumnTransformer(
    transformers=[
        ('num', num_transformer, ['idade', 'renda']),
        ('cat', cat_transformer, ['plano'])
    ])

# 4. O Super Combo Final (Pré-processamento + Modelo)
super_combo = Pipeline(steps=[
    ('pre_process', pre_processador),
    ('modelo', RandomForestClassifier())
])

# 5. Treinar e Salvar
super_combo.fit(X_treino, y_treino)
joblib.dump(super_combo, 'super_pipeline.pkl')

print("✅ Super Pipeline salvo! Ele processa números, limpa buracos e entende palavras.")
