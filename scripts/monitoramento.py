import pandas as pd
# Importação básica para testar
try:
    from evidently.report import Report
    from evidently.metric_preset import DataDriftPreset
    print("✅ Sucesso! Bibliotecas carregadas.")
except Exception as e:
    print(f"❌ Erro de importação: {e}")
    exit()

# Carregar dados
try:
    ref = pd.read_csv('dados_treinamento.csv')
    cur = pd.read_csv('logs_api_atuais.csv')
    
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=ref, current_data=cur)
    report.save_html('meu_relatorio_drift.html')
    print("🚀 Relatório gerado: meu_relatorio_drift.html")
except FileNotFoundError:
    print("❌ Arquivos CSV não encontrados. Rode gerar_dados.py e simular_producao.py")
