import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

def monitorar_e_retreinar():
    print("🧐 Passo 1: Analisando saúde do modelo...")
    ref = pd.read_csv('gerar_dados.csv')
    atual = pd.read_csv('logs_api_atuais.csv')

    # Executa o relatório internamente
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=ref, current_data=atual)
    resultado = report.as_dict()
    
    # Verifica se houve drift
    drift_detectado = resultado['metrics'][0]['result']['dataset_drift']

    if drift_detectado:
        print("🚨 DRIFT DETECTADO! Iniciando retreinamento com novos dados...")
        
        # Passo 2: Treinar novo modelo com os dados de 'produção' (logs_api_atuais)
        X_novo = atual.drop(columns=['target'])
        y_novo = atual['target']
        
        novo_modelo = LinearRegression()
        novo_modelo.fit(X_novo, y_novo)
        
        # Passo 3: Salvar a nova versão do modelo
        joblib.dump(novo_modelo, 'modelo_v2.pkl')
        print("✅ Modelo V2 salvo com sucesso! A produção agora está atualizada.")
    else:
        print("✅ Tudo sob controle. O modelo atual ainda é válido.")

if __name__ == "__main__":
    monitorar_e_retreinar()
