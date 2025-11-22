import pandas as pd
import sqlite3
import requests
from datetime import datetime
    

# conn = sqlite3.connect("models/BancoDadosAcionario.db")
# cursor = conn.cursor()
# ticker_api = requests.get("https://ledev.com.br/api/cotacoes/").json()
# hora = datetime.now()
# hora = hora.strftime("%H:%M")

# cursor.execute("SELECT Ticker FROM Acoes where Cnpj == 'None'")
# tickers = cursor.fetchall()
# lista_temp = []
# for ticker in tickers:
#     for letra in ticker[0]:
#         if letra in ["1","2","3","4","5","6","7","8","9"]:
#             new_ticker = ticker[0].replace(letra, "")
#     lista_temp.append(new_ticker)

# lista_temp2 = []
# for ticket in lista_temp:
#     try:
#         cursor.execute(f"SELECT Cnpj FROM Acoes where Ticker LIKE '{ticket}%'")       
#         dados = cursor.fetchall()
#         lista_temp2.append(dados[0])
#         print(f"CNPJ DO {ticket}: {dados}")
#     except:
#         pass


# add = [[i[0] for i in tickers], [y[0] for y in lista_temp2]]
# for item in range(len(add[0])):
#     cursor.execute(f"UPDATE Acoes SET Cnpj = '{add[1][item]}' where ticker = '{add[0][item]}'")
    



# df_ticker = pd.read_excel("cms_files_148780_1710532689Empresas_da_B3.xlsx")
# df_DRE10 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2010.csv", encoding="latin1", sep=";")
# df_DRE11 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2011.csv", encoding="latin1", sep=";")
# df_DRE12 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2012.csv", encoding="latin1", sep=";")
# df_DRE13 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2013.csv", encoding="latin1", sep=";")
# df_DRE14 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2014.csv", encoding="latin1", sep=";")
# df_DRE15 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2015.csv", encoding="latin1", sep=";")
# df_DRE16 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2016.csv", encoding="latin1", sep=";")
# df_DRE17 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2017.csv", encoding="latin1", sep=";")
# df_DRE18 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2018.csv", encoding="latin1", sep=";")
# df_DRE19 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2019.csv", encoding="latin1", sep=";")
# df_DRE20 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2020.csv", encoding="latin1", sep=";")
# df_DRE21 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2021.csv", encoding="latin1", sep=";")
# df_DRE22 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2022.csv", encoding="latin1", sep=";")
# df_DRE23 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2023.csv", encoding="latin1", sep=";")
# df_DRE24 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2024.csv", encoding="latin1", sep=";")
# df_DRE25 = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2025.csv", encoding="latin1", sep=";")

# dados_anuais_acionarios = [df_ticker, df_DRE10, df_DRE11, df_DRE12, df_DRE13, df_DRE14, df_DRE15, df_DRE16, 
#                            df_DRE17, df_DRE18, df_DRE19, df_DRE20, df_DRE21,df_DRE22, df_DRE23, df_DRE24, df_DRE25]

# lpa = ("3.99.01.01", "3.99.01.02")

# # print(dados_anuais_acionarios)

# empresasIBOV = []
# contador = 1


# for item in dados_anuais_acionarios:
#     match contador:
#         #Colocando o Ticker e CNPJ
#         case 1:
            
#             for empresa in item.itertuples():
#                 empresasIBOV.append({"Ticker": empresa[1], "Cnpj": str(empresa[-1]), "Hr_Atualizacao": hora})

#             emp = set(i["Ticker"] for i in empresasIBOV)
#             for i in ticker_api:
#                 if i["id"] not in emp:
#                     empresasIBOV.append({"Ticker": i["id"], "Pc_Atual":i["price"], "Nm_Empresarial":"None", "Cnpj":"None", "Hr_Atualizacao":hora})
            
            
#         case _:
#             #Colocando o nome empresarial
#             for linha in item.itertuples():
#                 for i in range(0, len(empresasIBOV)):
#                     if linha[1] == empresasIBOV[i]["Cnpj"]:
#                         if "Nm_empresarial" not in empresasIBOV[i]:
#                             empresasIBOV[i]["Nm_Empresarial"] = linha[4]
                        
                    


#                         # if linha[-4] in lpa:
#                         #     if linha[-2] in empresasIBOV[i]:
#                         #         continue
#                         #     else:
#                         #         empresasIBOV[i].append(linha[-2])
        

#     contador += 1

            


# for itemBD in empresasIBOV:
#     for itemAPI in range(0, len(ticker_api)):
#         if itemBD["Ticker"] == ticker_api[itemAPI]['id']:
#             itemBD["Pc_Atual"] = ticker_api[itemAPI]['price']
            

# for item in empresasIBOV:
#     if "Nm_Empresarial" not in item:
#         item["Nm_Empresarial"] = "None"
#     if "Pc_Atual" not in item:
#         item["Pc_Atual"] = 0.0
#     if "Cnpj" not in item:
#         item["Cnpj"] = "00.000.000/0000-00"
#     if "Hr_Atualizacao" not in item:
#         item["Hr_Atualizacao"] = hora


# for item in empresasIBOV:
#     valores = (
#         item.get('Ticker'), 
#         item.get('Cnpj'), 
#         item.get('Nm_Empresarial'), 
#         item.get('Pc_Atual'), 
#         item.get('Hr_Atualizacao')
#     )

#     try:
#         cursor.execute("""
#             INSERT OR IGNORE INTO Acoes (Ticker, Cnpj, Nm_Empresarial, Pc_Atual, Hr_Atual) 
#             VALUES (?, ?, ?, ?, ?)
#         """, valores)
        
#     except sqlite3.Error as e:
#         print(f"Erro no banco para {item.get('Ticker')}: {e}")
    
    

#     try:
#         cursor.execute(f"Update Acoes SET Cnpj = '{item['Cnpj']}' where ticker = '{item['Ticker']}'")
#     except:
#         pass

#     try:
#         cursor.execute(f"Update Acoes SET Nm_Empresarial = '{item['Nm_Empresarial']}' where ticker = '{item['Ticker']}'")
#     except:
#         pass
    
#     try:
#         cursor.execute(f"Update Acoes SET Pc_Atual = '{item['Pc_Atual']}' where ticker = '{item['Ticker']}'")
#     except:
#         pass
#     try:    
#         cursor.execute(f"Update Acoes SET Hr_Atual = '{item['Hr_Atualizacao']}' where ticker = '{item['Ticker']}'")
#     except:
#         pass


# conn.commit()


