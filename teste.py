import pandas as pd
import sqlite3
import requests
import time

    
conn = sqlite3.connect("models/BancoDadosAcionario.db")
cursor = conn.cursor()


dados_anuais_acionarios = []
df_ticker = pd.read_excel("cms_files_148780_1710532689Empresas_da_B3.xlsx")
df_DRE = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2010.csv", encoding="latin1", sep=";")


dados_anuais_acionarios.append(df_ticker)
dados_anuais_acionarios.append(df_DRE)

lpa1 = "3.99.01.01"
lpa2 = "3.99.01.02"

empresasIBOV = []
contador = 1


for item in dados_anuais_acionarios:
    match contador:
        #Colocando o Ticker e CNPJ
        case 1:
            for empresa in item.itertuples():
                empresasIBOV.append([empresa[1], empresa[5]])
        case 2:
            #Colocando o nome empresarial
            for linha in item.itertuples():
                for i in range(0, len(empresasIBOV)):
                    if linha[1] == empresasIBOV[i][1]:
                        if linha[4] in empresasIBOV[i]:
                            pass
                        else:
                            empresasIBOV[i].append(linha[4])

                        if linha[-4] == lpa1 or linha[-4] == lpa2:
                            if linha[-2] in empresasIBOV[i]:
                                continue
                            else:
                                empresasIBOV[i].append(linha[-2])


    contador += 1

# print(empresasIBOV)

result = requests.get("https://ledev.com.br/api/cotacoes/")
result = result.json()

def funcc(resultado):
    lista = []
    for i in range(0, len(resultado)):
        lista.append(resultado[i]['id'])
    return lista
hora = time.time()
for i in range(0, len(empresasIBOV)):
    if empresasIBOV[i][0] in funcc(result):
        for item in range(0, len(result)):
            if result[item]['id'] == empresasIBOV[i][0]:
                new_lista = [result[item]['price'], hora]
                empresasIBOV[i].append(new_lista[0])
                empresasIBOV[i].append(new_lista[1])


print(empresasIBOV)
        
for i in range(0, len(empresasIBOV)):
    try:
        cursor.execute(f"Update EmpresasIBOV SET cnpj = '{empresasIBOV[i][1]}' where ticker = '{empresasIBOV[i][0]}'")
    except:
        pass

    try:
        cursor.execute(f"Update EmpresasIBOV SET nomeEmpresarial = '{empresasIBOV[i][2]}' where ticker = '{empresasIBOV[i][0]}'")
    except:
        pass
    
    try:
        cursor.execute(f"Update EmpresasIBOV SET precoAtual = '{empresasIBOV[i][-2]}' where ticker = '{empresasIBOV[i][0]}'")
    except:
        pass
    try:    
        cursor.execute(f"Update EmpresasIBOV SET horarioAtualizacaoPreco = '{empresasIBOV[i][-1]}' where ticker = '{empresasIBOV[i][0]}'")
    except:
        pass
conn.commit()
