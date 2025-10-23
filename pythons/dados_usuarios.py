import sqlite3
from brapi import Brapi




def coleta_dados(chaveApi, cota):
    banco_dados = sqlite3.connect('models/bancoUsuarios.db')
    cursor = banco_dados.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS dadosUsuarios (chaveApi text primary key)")
    cursor.execute("CREATE TABLE IF NOT EXISTS cotas (sigla text primary key, valorAtual integer, nomeEmpresarial text, valorMinimoAnual integer, valorMaximoAnual integer)")


    key = chaveApi
    chaveApi = Brapi(api_key=chaveApi)

    try:
        dados_cota = chaveApi.quote.retrieve(tickers=cota)
        if dados_cota:

            dados_cota = [
                    dados_cota.results[0].long_name, 
                    dados_cota.results[0].regular_market_price,
                    dados_cota.results[0].fifty_two_week_low, 
                    dados_cota.results[0].fifty_two_week_high]
            
            cursor.execute(f"Insert or ignore into dadosUsuarios values ('{key}')")
            cursor.execute(f"Insert or ignore into cotas values('{cota}','{dados_cota[1]}', '{dados_cota[0]}', '{dados_cota[2]}', '{dados_cota[3]}')")
            banco_dados.commit()
            
    except Exception as e:
        print(f"Chave API incorreta --> {e}")
    
    
