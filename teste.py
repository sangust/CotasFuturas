import pandas as pd
import sqlite3
import requests


    
conn = sqlite3.connect("models/BancoDadosAcionario.db")
cursor = conn.cursor()


dados_anuais_acionarios = []
df_ticker = pd.read_excel("cms_files_148780_1710532689Empresas_da_B3.xlsx")
df_DRE = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DRE_con_2010.csv", encoding="latin1", sep=";")
df_BPA = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_BPA_con_2010.csv", encoding="latin1", sep=";")
df_BPP = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_BPP_con_2010.csv", encoding="latin1", sep=";")
df_DFC = pd.read_csv("csvs/dfp_cia_aberta_2010/dfp_cia_aberta_DFC_MI_con_2010.csv", encoding="latin1", sep=";")


dados_anuais_acionarios.append(df_ticker)
dados_anuais_acionarios.append(df_DRE)
dados_anuais_acionarios.append(df_DFC)
dados_anuais_acionarios.append(df_BPA)
dados_anuais_acionarios.append(df_BPP)

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

               
        case 3:
            pass
        case 4:
            pass
        case 5:    
            pass

    contador += 1

print(empresasIBOV)


#https://ledev.com.br/api/cotacoes/
  
        
# for i in range(0, len(empresasIBOV)):
#     try:
#         cursor.execute(f"Update EmpresasIBOV SET nomeEmpresarial = '{empresasIBOV[i][2]}' where ticker = '{empresasIBOV[i][0]}'")
#     except:
#         continue
# conn.commit()
