import customtkinter as ctk
import pythons.dados_usuarios as du



class App(ctk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        ctk.set_appearance_mode("system")
        self.geometry("420x450")
        self.title("Profitly")

        self.tela_login = TelaLogin(self)
        

        self.mainloop()


class TelaLogin(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        ctk.CTkLabel(master, text="Bem vindo ao Profitly", font=('', 25)).place(relx=0.5, rely=0.1, anchor='center')
        ctk.CTkLabel(master, text="Cole a sua Chave API:").place(relx=0.5, rely=0.54, anchor="center")
        ctk.CTkButton(master, text="Login", command=self.processar_cadastro).place(relx=0.5, rely=0.91, anchor="center")

        self.chaveApi_cadastro_input = ctk.CTkEntry(master, placeholder_text="Chave Api")
        self.chaveApi_cadastro_input.place(relx=0.5, rely=0.61, anchor="center")

    def processar_cadastro(self):
        chaveApi = self.chaveApi_cadastro_input.get()
        du.coleta_dados(chaveApi)
        



class TelaCotacao(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        
        ctk.CTkLabel(master, text="Profitly", font=('', 22), text_color="#00ffff").place(relx=0.05, rely=0.05)
        ctk.CTkLabel(master, text="Digite a sigla da cota:").place(relx=0.5, rely=0.3, anchor="center")

        ctk.CTkButton(master, text="Login", command=self.pesquisar_cota).place(relx=0.5, rely=0.55, anchor="center")
        

        self.chaveApi_cadastro_input = ctk.CTkEntry(master, placeholder_text="cota")
        self.chaveApi_cadastro_input.place(relx=0.5, rely=0.4, anchor="center")

    def pesquisar_cota(self):
        cota = self.chaveApi_cadastro_input.get()

        cotacao_atual = cota
        cotacao_atual = {"Nome da Empresa:": cotacao_atual.results[0].long_name,
                        "Logo da Empresa:": cotacao_atual.results[0].logourl,
                        f"Preço Atual Da {cotacao_atual.results[0].symbol}":"BRL:" + str(cotacao_atual.results[0].regular_market_price),
                        "Volatilidade_1ano":(cotacao_atual.results[0].fifty_two_week_range),
                        "min_1ano": cotacao_atual.results[0].fifty_two_week_low,
                        "max_1ano": cotacao_atual.results[0].fifty_two_week_high
                    }
        print(cotacao_atual)
    




app = App()
