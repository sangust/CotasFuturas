import sqlite3
import pandas as pd


banco_dados = sqlite3.connect('bancoUsuarios.db')
cursor = banco_dados.cursor()
cursor.execute("Create table IF NOT EXISTS dadosUsuarios (id integer primary key,nome text,senha text,chaveApi text)")



#Usuario
def coleta_dados(user, senha, chaveApi):
    usuario = user

    if usuario.isalpha():
        print("Nome de usuário válido!")
    else:
        print("Nome de usuário inválido! Use apenas letras (sem espaços, números ou símbolos).")

    #Senha
    
    senha = senha

    if " " in senha:
        raise ValueError('A senha não pode conter espaços!')
        
    else:
        print('Senha válida!')


    #Chave Api
    api_usuario = chaveApi

    cursor.execute(f"Insert into dadosUsuarios values (2,'{usuario}','{senha}','{api_usuario}')")
    banco_dados.commit()


