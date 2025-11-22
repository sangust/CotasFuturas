import sqlite3
from brapi import Brapi

#CRIAÇÃO DO BANCO DE DADOS E TABELAS
banco_dados = sqlite3.connect('models/bancoUsuarios.db')
cursor = banco_dados.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS dadosUsuarios (chaveApi text primary key)")
cursor.execute("CREATE TABLE IF NOT EXISTS cotas (sigla text primary key, valorAtual integer, nomeEmpresarial text, valorMinimoAnual integer, valorMaximoAnual integer)")


def coleta_dados_api(chaveApi):
    cursor.execute(f"Insert or ignore into dadosUsuarios values ('{chaveApi}')")
    banco_dados.commit()
    
        

#cursor.execute(f"Insert or ignore into cotas values('{cota}','{dados_cota[1]}', '{dados_cota[0]}', '{dados_cota[2]}', '{dados_cota[3]}')")


            
    
    
    
    
