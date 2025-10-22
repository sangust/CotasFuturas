import sqlite3
from brapi import Brapi
import time



def coleta_dados(chaveApi):
    banco_dados = sqlite3.connect('models/bancoUsuarios.db')
    cursor = banco_dados.cursor()
    cursor.execute("Create table IF NOT EXISTS dadosUsuarios (chaveApi text primary key)")


    key = chaveApi
    chaveApi = Brapi(api_key=chaveApi)

    try:
        dados_cota = chaveApi.quote.retrieve(tickers=f"EQTL3")
        print(dados_cota)
        if dados_cota:
            cursor.execute(f"Insert or ignore into dadosUsuarios values ('{key}')")
            banco_dados.commit()
    except Exception as e:
        print(f"Chave API incorreta --> {e}")
    
    

def buscar_preco_cotacao_atual(cota):
    cotacao_atual = cota
    cotacao_atual = {
                    cotacao_atual.results[0].long_name:cotacao_atual.results[0].logourl,
                    cotacao_atual.results[0].currency:cotacao_atual.results[0].regular_market_price,
                    "Volatilidade_1ano":(cotacao_atual.results[0].fifty_two_week_range),
                    "min_1ano": cotacao_atual.results[0].fifty_two_week_low,
                    "max_1ano": cotacao_atual.results[0].fifty_two_week_high
                    }
    return cotacao_atual
    
