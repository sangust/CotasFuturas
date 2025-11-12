import pandas as pd
import sqlite3
import requests
import time

    




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
hora = time.time()
##ARRUMAR ESSA ITERAÇÂO ABAIXO
for j in range(0, len(ticker_api[0])):
    print(ticker_api[j])
    for i in range(0, len(empresasIBOV)):
            if ticker_api[j]["id"] == empresasIBOV[i]["Ticker"]:
                empresasIBOV[i]['Preco'] = ticker_api[j]['price']
                empresasIBOV[i]['HR_PrecoAtual'] = hora



print(empresasIBOV)


# print(empresasIBOV)




# conn = sqlite3.connect("models/BancoDadosAcionario.db")
# cursor = conn.cursor()
# for i in range(0, len(empresasIBOV)):
#     try:
#         cursor.execute(f"Update EmpresasIBOV SET cnpj = '{empresasIBOV[i][1]}' where ticker = '{empresasIBOV[i][0]}'")
#     except:
#         pass

#     try:
#         cursor.execute(f"Update EmpresasIBOV SET nomeEmpresarial = '{empresasIBOV[i][2]}' where ticker = '{empresasIBOV[i][0]}'")
#     except:
#         pass
    
#     try:
#         cursor.execute(f"Update EmpresasIBOV SET precoAtual = '{empresasIBOV[i][-2]}' where ticker = '{empresasIBOV[i][0]}'")
#     except:
#         pass
#     try:    
#         cursor.execute(f"Update EmpresasIBOV SET horarioAtualizacaoPreco = '{empresasIBOV[i][-1]}' where ticker = '{empresasIBOV[i][0]}'")
#     except:
#         pass
# conn.commit()