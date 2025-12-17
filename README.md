# 🚀 Sistema de MLOps: Monitoramento e Deploy de IA

## 📋 Visão Geral
Este projeto é uma aplicação de Machine Learning completa, focada em práticas de **MLOps**. Ele vai desde o tratamento de dados e treinamento de um modelo "blindado" até o deploy seguro utilizando Docker e monitoramento de performance.

## 🛠️ Tecnologias Utilizadas
* **Python 3.11**: Linguagem principal.
* **Streamlit**: Interface web do usuário.
* **Scikit-Learn**: Criação do Pipeline de Machine Learning.
* **Evidently AI**: Monitoramento de Data Drift.
* **SQLite**: Banco de dados para histórico e autenticação.
* **Docker**: Containerização da aplicação.
* **Passlib**: Criptografia de senhas.

## 📂 Estrutura de Pastas
O projeto está organizado da seguinte forma:
* `data/`: Banco de dados e arquivos CSV.
* `models/`: Modelos treinados (.pkl).
* `scripts/`: Automações de treino e monitoramento.
* `reports/`: Relatórios de performance gerados.
* `app.py`: Arquivo principal da interface.

## 🚀 Como Executar

### 1. Via Docker (Recomendado)
Certifique-se de ter o Docker instalado e rode:
```bash
# Construir a imagem
docker build -t minha-ia-seguro .

# Rodar o container
docker run -p 8501:8501 minha-ia-seguro
