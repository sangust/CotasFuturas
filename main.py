import sqlite3

banco_dados = sqlite3.connect('infos.db')
cursor = banco_dados.cursor()


cursor.execute("Create table IF NOT EXISTS usuarios(nome text, chaveApi text primary key)")


cursor.execute("select * from usuarios")
dados = cursor.fetchall()

for item in dados:
    print(f"Nome: {item[0]}, chave API:{item[1]}")
