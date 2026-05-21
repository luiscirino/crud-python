# Importando sqlite
import sqlite3 as lite

# Criando conexão
con = lite.connect('dados.db')

# Criando tabelas

with con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS formulario(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        telefone TEXT,
        dia_em DATE,
        estado TEXT,
        assunto TEXT
    )
    """)