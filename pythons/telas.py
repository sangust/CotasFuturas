import customtkinter as ctk
import pythons.dados_usuarios as du
import pandas as pd
from brapi import Brapi
import webbrowser
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("system")
        self.geometry("500x450")
        self.title("Profitly")

        #Criar o frame da tela atual.
        self.tela_atual = None
        self.trocar_tela(TelaLogin)
        self.mainloop()

    #Função para trocar de telas.
    def trocar_tela(self, classe_tela):
        
        nova_tela = classe_tela(self)
        if self.tela_atual is not None:
            self.tela_atual.destroy()
        self.tela_atual = nova_tela
        self.tela_atual.pack(fill='both', expand=True)


class TelaLogin(ctk.CTkFrame):
    #esse master é a tela na qual esse frame (tela de login) vai aparecer, no caso é self, pois ele é chamado dentro da classe app
    #então ele é chamado pra dentro da tela app que ocorre o mainloop().
    #Os self dentro das label e entry, é pq tem que aparecer dentro desse frame, não na tela "principal" que é o app.

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        ctk.CTkLabel(self, text="Bem vindo ao Profitly", font=('', 33)).place(relx=0.5, rely=0.1, anchor='center')

        ctk.CTkLabel(self, text="Você irá digitar alguma ação da bolsa de valores\n e aqui mostrará as suas principais informações" \
        "\n e probabilidade de valorização da ação em anos.", font=('', 15)).place(relx=0.5, rely= 0.25, anchor='center')

        ctk.CTkLabel(self, text="Cole a sua Chave API:", font=('', 15)).place(relx=0.5, rely=0.42, anchor="center")

        ctk.CTkButton(self, text="Entrar", command=self.processar_cadastro).place(relx=0.5, rely=0.63, anchor="center")

        self.error = ctk.CTkLabel(self, text='', )
        self.error.place(relx=0.5, rely=0.48,anchor="center")

        self.url = 'https://brapi.dev/'
        ctk.CTkLabel(self, text='Caso não tenha uma chave api, entre no link e crie uma.',).place(relx=0.5, rely=0.9 ,anchor="center")
        link=ctk.CTkLabel(self, text='https://brapi.dev/', text_color="cyan")
        link.place(relx=0.5, rely=0.95,anchor="center")


        #Comandos para passar o mouse encima do link e ele funcionar
        link.bind("<Button-1>", lambda evento: self.abrir_link(self.url))
        link.bind("<Enter>", lambda evento: link.configure(cursor="hand2"))
        link.bind("<Enter>", lambda evento: link.configure(text_color="deep sky blue"))
        link.bind("<Leave>", lambda evento: link.configure(cursor=""))
        link.bind("<Leave>", lambda evento: link.configure(text_color="cyan"))


        self.chaveApi_cadastro_input = ctk.CTkEntry(self, placeholder_text="Token")
        self.chaveApi_cadastro_input.place(relx=0.5, rely=0.55, anchor="center")



    def abrir_link(self, url):
        webbrowser.open_new(url)



    def processar_cadastro(self):
        token_chave_api = self.chaveApi_cadastro_input.get()
        chaveApi = Brapi(api_key=token_chave_api)
        try:
            #vai validar a chave api, se tiver incorreta ele já vai para o erro
            dados = chaveApi.quote.retrieve(tickers="EQTL3")

            #Vai armazenar a chave api dele no banco de dados
            du.coleta_dados_api(token_chave_api)
            self.master.trocar_tela(TelaCotacao)
        except Exception as e:
            self.error.configure(text=f"Erro, Chave api invalida, Tente novamente\n{e}", text_color="red")

       

class TelaCotacao(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg_color="transparent", **kwargs)
        
        
        ctk.CTkLabel(self, text="Profitly", font=('', 35), text_color="#eeff00").place(relx=0.05, rely=0.05)
        ctk.CTkLabel(self, text="Digite a sigla da ação:").place(relx=0.5, rely=0.3, anchor="center")

        ctk.CTkButton(self, text="Buscar", command=self.pesquisar_cota).place(relx=0.5, rely=0.5, anchor="center")
        

        self.pesquisar_acao_input = ctk.CTkEntry(self, placeholder_text="EX: PETR4, BBAS3")
        self.pesquisar_acao_input.place(relx=0.5, rely=0.4, anchor="center")


    def pesquisar_cota(self):

        acao = self.pesquisar_acao_input.get()
        df = pd.read_sql("select * from dadosUsuarios", du.banco_dados)
        chaveApi = df.iloc[0,0]
        chaveApi = Brapi(api_key=chaveApi)

        try:
            dados_cota = chaveApi.quote.retrieve(tickers=acao)
            dados_cota = {"nomeEmpresario": dados_cota.results[0].long_name,
                        "sigla": dados_cota.results[0].logourl,
                        f"Preço Atual Da {dados_cota.results[0].symbol}":"BRL:" + str(dados_cota.results[0].regular_market_price),
                        "Volatilidade_1ano":(dados_cota.results[0].fifty_two_week_range),
                        "min_1ano": dados_cota.results[0].fifty_two_week_low,
                        "max_1ano": dados_cota.results[0].fifty_two_week_high}
            print(dados_cota)
            
            
        except Exception as e:
            print(e)

        

app = App()
