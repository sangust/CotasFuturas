import pandas as pd
import sqlite3
import requests
from datetime import datetime
    




df_ticker = pd.read_excel("cms_files_148780_1710532689Empresas_da_B3.xlsx")
df_DRE = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2010.csv", encoding="latin1", sep=";")
dados_anuais_acionarios = [df_ticker, df_DRE]
lpa = ("3.99.01.01", "3.99.01.02")


empresasIBOV = []
contador = 1


for item in dados_anuais_acionarios:
    match contador:
        #Colocando o Ticker e CNPJ
        case 1:
            for empresa in item.itertuples():
                empresasIBOV.append({"Ticker": empresa[1], "Cnpj": str(empresa[5])})
        case 2:
            #Colocando o nome empresarial
            for linha in item.itertuples():

                for i in range(0, len(empresasIBOV)):
                    if linha[1] == empresasIBOV[i]["Cnpj"]:
                        if "Nm_empresarial" in empresasIBOV[i]:
                            pass
                        else:
                            empresasIBOV[i]["Nm_Empresarial"] = linha[4]

                        # if linha[-4] in lpa:
                        #     if linha[-2] in empresasIBOV[i]:
                        #         continue
                        #     else:
                        #         empresasIBOV[i].append(linha[-2])


    contador += 1




ticker_api = requests.get("https://ledev.com.br/api/cotacoes/").json()
hora = datetime.now()
hora = hora.strftime("%H:%M")

for itemBD in empresasIBOV:
    itemBD["Hr_Atualizacao"] = hora
    for itemAPI in range(0, len(ticker_api)):
        if itemBD["Ticker"] == ticker_api[itemAPI]['id']:
            itemBD["Pc_Atual"] = ticker_api[itemAPI]['price']
            










conn = sqlite3.connect("models/BancoDadosAcionario.db")
cursor = conn.cursor()
sql_query = "UPDATE EmpresaIBov SET cnpj = ? WHERE ticker = ?"



for item in empresasIBOV:
    # try:
    #     cursor.execute(f"insert into Acoes VALUES ('{item['Ticker']}', '{item['Cnpj']}', '{item['Nm_Empresarial']}', '{item['Pc_Atual']}', '{item['Hr_Atualizacao']}')")
    # except Exception as e:
    #     pass


#     try:
#         cursor.execute(f"Update Acoes SET Cnpj = '{empresasIBOV[i]['Cnpj']}' where ticker = '{empresasIBOV[i]['Ticker']}'")
#     except:
#         pass

#     try:
#         cursor.execute(f"Update Acoes SET Nm_Empresarial = '{empresasIBOV[i]['Nm_Empresarial']}' where ticker = '{empresasIBOV[i]['Ticker']}'")
#     except:
#         pass
    
#     try:
#         cursor.execute(f"Update Acoes SET Pc_Atual = '{empresasIBOV[i]['Pc_Atual']}' where ticker = '{empresasIBOV[i]['Ticker']}'")
#     except:
#         pass
    try:    
        cursor.execute(f"Update Acoes SET Hr_Atual = '{item['Hr_Atualizacao']}' where ticker = '{item['Ticker']}'")
    except:
        pass


conn.commit()