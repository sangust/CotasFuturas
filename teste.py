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
            

##1 preço, 2 nome
empresas_faltando_dados = [[],['ALOS99', 'BBAS11', 'PCAR99', 'HAPV99', 'MLAS', 'SRNA3', 'ALUP11', 'ABCB10', 'CLSC4', 'CPLE5', 'POMO4', 'RNEW11', 'TASA4', 'TFCO4', 'ALPA4', 
'ELET5', 'CEDO4', 'OIBR4', 'RAPT4', 'BBML3', 'BRQB3', 'CTCA3', 'GRAO3', 'IGSN3', 'INNC3', 'LMED3', 'MSRO3', 'NUTR3', 'QUSW3', 'EUFA3', 'PTCA3', 'SAEN3', 'QVQP3', 'AESO3', 
'RPAD5', 'ALGT', 'ALTR', 'AZEV4', 'BALM4', 'BRIV4', 'BPAR3', 'BETP3', 'BOBR4', 'BRML', 'CABI3', 'MAPT4', 'CMGD', 'CMGT', 'CASN4', 'CEEB5', 'CEBR5', 'CEPE', 'COCE5', 'CSRN5', 
'CEED4', 'CGEE', 'EEEL', 'HBTS5', 'CATA4', 'MSPA4', 'PEAB4', 'PALF', 'CPFP', 'CTNM4', 'CTSA4', 'CMSA4', 'COMR3', 'PASS5', 'RPTA', 'ECOV', 'CRTE5', 'ASCP', 'RDVT', 'CRBD', 
'ANHB', 'ODER4', 'BRGE11', 'CPRE', 'CPFG', 'LLBI3', 'DBEN', 'DMFN3', 'DOHL4', 'DTCY4', 'ERDV', 'ENBR', 'ESCE', 'EBEN', 'EKTR4', 'ELPL', 'EMAE4', 'ENER', 'ENMT4', 'EQPA5', 
'BAUH4', 'FGEN', 'VSPT4', 'FIEI3', 'EGGY5', 'CGRA4', 'HAGA4', 'HETA4', 'HMOB3', 'HOOT4', 'IGTA', 'INEP4', 'FIGE4', 'ITPB', 'JMCD', 'JOPA4', 'KLAS3', 'CTKA', 'LIGH', 'MGEL4', 
'ESTR4', 'MTSA4', 'MMAQ4', 'NATU', 'NRTQ3', 'OCTS', 'RBRA', 'OSEC', 'PRBC', 'PDGS', 'PTNT4', 'PLSC', 'PPAR3', 'PSVM11', 'PRPT3', 'RESA', 'WTPI', 'RCSL4', 'AESL', 'GEPA4', 
'RBNS11', 'COLN', 'SAIP', 'SNST', 'SNSY5', 'STEN', 'AHEB5', 'BZRS', 'APTI4', 'SOND5', 'STKF', 'OPSE3', 'OPTS3', 'NEMO5', 'TCPA', 'TEGA3', 'TEKA4', 'TKNO4', 'TELB4', 'TEPE', 
'MNZC3', 'TMPE', 'TXRX4', 'LUXM4', 'APCS', 'OVSA', 'UPKP3', 'VERT', 'CBSC', 'WHRL4', 'YBRA4'], ['RRRP3', 'AERI3', 'AESB3', 'AGXY3', 'AALR3', 'ALLD3', 'ALPK3', 'AVLL3', 'AMBP3', 
'ANIM3', 'ARML3', 'CRFB3', 'AURE3', 'BBSE3', 'BMOB3', 'BLAU3', 'SOJA3', 'AGRO3', 'BRIT3', 'CXSE3', 'CAML3', 'CEAB3', 'CLSA3', 'VVEO3', 'CBAV3', 'CSAN3', 'CSED3', 'CSUD3', 
'CURY3', 'CVCB3', 'DMVF3', 'DESK3', 'DOTZ3', 'ELMD3', 'PGMN3', 'ENJU3', 'NINJ3', 'GGPS3', 'SOMA3', 'GMAT3', 'SBFG3', 'HBRE3', 'HBSA3', 'MATD3', 'IFCM3', 'INTB3', 'MEAL3', 
'IRBR3', 'JALL3', 'KRSA3', 'LAVV3', 'LVTC3', 'LWSA3', 'LOGG3', 'LJQQ3', 'CASH3', 'MELK3', 'MILS3', 'MTRE3', 'MBLY3', 'MOVI3', 'ESPA3', 'NTCO3', 'NGRD3', 'OPCT3', 'ONCO3', 
'ORVR3', 'OFSA3', 'PETZ3', 'RECV3', 'PLPL3', 'PRNR3', 'RADL3', 'RDOR3', 'SMTO3', 'ASAI3', 'SEQL3', 'SIMH3', 'SMFT3', 'TRAD3', 'LAND3', 'TIMS3', 'TTEN3', 'TUPY3', 'UCAS3', 
'FIQE3', 'VAMO3', 'VBBR3', 'VITT3', 'VIVA3', 'WEST3', 'PORT3', 'WIZC3', 'AZUL4', 'BPAC11', 'BRBI11', 'SAPR11', 'CMIN3', 'RAIZ4', 'BMGB4', 'AFLT3', 'ABEV3', 'CBEE3', 'ATOM3', 
'BAZA3', 'BMIN4', 'BNBR3', 'CEGR3', 'CGAS5', 'MERC4', 'EALT4', 'LIPR3', 'CRIV4', 'RSUL4', 'NORD3', 'ZAMP3']]

for item in empresasIBOV:
    if item["Ticker"] in empresas_faltando_dados[1] and len(item) < 4:
        empresas_faltando_dados[0].append(item["Ticker"])



conn = sqlite3.connect("models/BancoDadosAcionario.db")
cursor = conn.cursor()


for item in empresas_faltando_dados[0]:
    for linha in empresasIBOV:
        if item == linha["Ticker"]:
            linha["Pc_Atual"] = 0.0
            linha["Nm_Empresarial"] = "None"
            print(linha)





for item in empresasIBOV:
    try:
        cursor.execute(f"insert into Acoes VALUES ('{item['Ticker']}', '{item['Cnpj']}', '{item['Nm_Empresarial']}', '{item['Pc_Atual']}', '{item['Hr_Atualizacao']}')")
    except Exception as e:
        print(e)


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

cursor.execute("SELECT * FROM Acoes WHERE Ticker == 'FIGE4'")
fige4 = cursor.fetchall()
print(fige4)