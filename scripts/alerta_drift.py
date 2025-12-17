import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# 1. Carregar os dados
ref = pd.read_csv('dados_treinamento.csv')
cur = pd.read_csv('logs_api_atuais.csv')

# 2. Rodar o relatório em modo 'dicionário' (para o Python ler)
report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=ref, current_data=cur)
dict_report = report.as_dict()

# 3. Extrair métricas automáticas
drifts_detectados = dict_report['metrics'][0]['result']['number_of_drifted_columns']
total_colunas = dict_report['metrics'][0]['result']['number_of_columns']

print(f"🔍 Colunas analisadas: {total_colunas}")
print(f"🚨 Colunas com Drift: {drifts_detectados}")

# 4. Tomar decisão
if drifts_detectados > 0:
    print("\n--- 🛑 ALERTA DE MONITORAMENTO ---")
    print("O comportamento dos dados mudou drasticamente.")
    print("Ação sugerida: Retreinar o modelo com os novos dados de produção.")
else:
    print("\n✅ Modelo saudável. Nenhuma ação necessária.")
    