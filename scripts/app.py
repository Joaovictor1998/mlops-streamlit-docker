import streamlit as st
import joblib
import pandas as pd
import numpy as np
import sqlite3

# --- 1. CONFIGURAÇÃO DE SEGURANÇA ---
def verificar_login():
    """Cria campos de login na barra lateral e retorna True se autorizado."""
    if "autenticado" not in st.session_state:
        st.session_state["autenticado"] = False

    st.sidebar.title("🔐 Acesso Restrito")
    usuario = st.sidebar.text_input("Usuário")
    senha = st.sidebar.text_input("Senha", type="password")
    
    if st.sidebar.button("Entrar"):
        # Aqui você define seu usuário e senha
        if usuario == "admin" and senha == "mlops123":
            st.session_state["autenticado"] = True
            st.sidebar.success("Login efetuado!")
            st.rerun() # Atualiza a página para liberar o conteúdo
        else:
            st.sidebar.error("Usuário ou senha incorretos")

    return st.session_state["autenticado"]

# --- 2. FUNÇÕES DE SUPORTE (Banco de Dados) ---
def salvar_no_banco(idade, renda, plano, prob):
    conn = sqlite3.connect('historico_ia.db')
    c = conn.cursor()
    c.execute("INSERT INTO previsoes (idade, renda, plano, probabilidade) VALUES (?, ?, ?, ?)",
              (idade, renda, plano, prob))
    conn.commit()
    conn.close()

# --- 3. LÓGICA PRINCIPAL ---
if verificar_login():
    # TODO O SEU CÓDIGO ANTERIOR VAI AQUI DENTRO
    st.title("🤖 Preditor de Perfil de Cliente")
    
    # Carregar o modelo
    modelo = joblib.load('models/super_pipeline.pkl')
    
    # Interface
    col1, col2 = st.columns(2)
    with col1:
        idade = st.number_input("Idade do Cliente", min_value=18, max_value=100, value=30)
    with col2:
        renda = st.number_input("Renda Mensal (0 para vazio)", min_value=0, value=5000)
    
    plano = st.selectbox("Plano de Interesse", ["Bronze", "Prata", "Ouro"])
    renda_final = renda if renda > 0 else np.nan

    if st.button("Analisar Cliente"):
        novo_cliente = pd.DataFrame({'idade': [idade], 'renda': [renda_final], 'plano': [plano]})
        probabilidade = modelo.predict_proba(novo_cliente)[0][1]
        
        # Salva no Banco e Mostra Resultado
        salvar_no_banco(idade, renda_final, plano, probabilidade)
        
        st.divider()
        if probabilidade > 0.5:
            st.success(f"🔥 Alta Probabilidade: {probabilidade*100:.2f}%")
        else:
            st.warning(f"❄️ Baixa Probabilidade: {probabilidade*100:.2f}%")

    if st.sidebar.button("Sair"):
        st.session_state["autenticado"] = False
        st.rerun()
else:
    st.warning("Por favor, faça login na barra lateral para acessar a IA.")
    st.image("https://cdn-icons-png.flaticon.com/512/6195/6195700.png", width=100)
    