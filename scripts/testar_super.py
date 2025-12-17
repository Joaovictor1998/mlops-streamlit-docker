import joblib
import pandas as pd
import numpy as np


# Carregar o super pipeline
modelo = joblib.load('super_pipeline.pkl')

# Cliente novo: Renda faltando e plano em texto
novo_cliente = pd.DataFrame({
    'idade': [28],
    'renda': [np.nan],
    'plano': ['Ouro']
})

# O Pipeline faz TUDO: preenche o NaN e converte 'Ouro' para números internamente
probabilidade = modelo.predict_proba(novo_cliente)

print(f"Dados do Cliente:\n{novo_cliente}")
print(f"\n🚀 Probabilidade de compra: {probabilidade[0][1]*100:.2f}%")
