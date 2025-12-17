import joblib
import pandas as pd
import numpy as np

# O arquivo salvo no passo anterior:
MODEL_FILE = 'modelo_final_blindado.pkl'

# 1. Carrega o combo completo (Imputador + Modelo)
try:
    combo_modelo = joblib.load(MODEL_FILE)
    print(f"✅ Combo '{MODEL_FILE}' carregado com sucesso!")
except FileNotFoundError:
    print(f"❌ Erro: Arquivo {MODEL_FILE} não encontrado. Execute 'treinar_com_pipeline.py' primeiro!")
    exit()

# 2. Cria um novo cliente com DADOS FALTANTES
# O cliente não informou a renda (renda = NaN)
novo_cliente = pd.DataFrame({
    'idade': [38],
    'renda': [np.nan] # <--- O 'buraco' que causaria erro
})

print("\n⚠️ Cliente de teste com dado faltante:")
print(novo_cliente)

# 3. Faz a previsão
# O Pipeline fará a imputação internamente antes de prever
predicao = combo_modelo.predict(novo_cliente)

print(f"\n🚀 Previsão do Combo (Model + Imputer): {predicao[0]:.2f}")
