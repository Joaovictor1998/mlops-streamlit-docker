import sqlite3
from passlib.hash import pbkdf2_sha256 # NOVO: Biblioteca de criptografia

# Senha: 'mlops123' criptografada (o hash real será diferente)
SENHA_ADMIN_HASH = pbkdf2_sha256.hash("mlops123") 

def criar_banco():
    conn = sqlite3.connect('data/historico_ia.db')
    c = conn.cursor()
    
    # 1. Tabela de Previsões (já existe)
    c.execute('''
        CREATE TABLE IF NOT EXISTS previsoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            idade INTEGER,
            renda REAL,
            plano TEXT,
            probabilidade REAL
        )
    ''')

    # 2. NOVO: Tabela de Usuários
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password_hash TEXT
        )
    ''')

    # 3. NOVO: Inserir o primeiro usuário (admin)
    c.execute("SELECT COUNT(*) FROM usuarios WHERE username='admin'")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO usuarios (username, password_hash) VALUES (?, ?)", 
                  ('admin', SENHA_ADMIN_HASH))
        print("Usuário 'admin' inserido com sucesso!")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_banco()
    print("✅ Banco de dados e Tabela de Usuários prontos!")
