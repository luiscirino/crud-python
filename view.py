# Importando o SQLite

import sqlite3 as lite

# Criando conexão
con = lite.connect('dados.db')

# Inserir informações (Create)
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario(nome, email, telefone, dia_em, estado, assunto) VALUES(?, ?, ?, ?, ?, ?)"

        cur.execute(query, i)

# Ler informações (Read)
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"

        cur.execute(query)

        info = cur.fetchall()

        for i in info:
            lista.append(i)

        return lista


# # Atualizar informações (Update)
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?"
        cur.execute(query, i)

# # Remover informações (Delete)
def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)