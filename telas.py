import customtkinter as ctk
import dados_usuarios



class App(ctk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        ctk.set_appearance_mode("system")
        self.geometry("420x450")
        self.title("Profitly")

class tela_cadastro(ctk.CTkFrame):
    def __init__(self, ):
        super().__init__(self)

class tela_login(ctk.CTkFrame):
    pass


class cadastro_login():
    def __init__(self):
        ctk.set_appearance_mode("system")
        self.tela = ctk.CTk()
        self.tela.geometry("420x450")
        self.tela.title("Profitly")
        
        #Cria "frames", são telas que possuem conteudos, aqui está definido como transparente para não aparecer
        self.cadastro_tela = ctk.CTkFrame(self.tela)
        self.login_tela = ctk.CTkFrame(self.tela)

        self.cadastrar(self.cadastro_tela)
        self.logar(self.login_tela)

        self.mostrar_tela_cadastro()
        self.tela.mainloop()

    def mostrar_tela_cadastro(self):
        self.login_tela.pack_forget()
        self.cadastro_tela.pack(fill="both", expand=True)

    def mostrar_tela_login(self):
        self.cadastro_tela.pack_forget()
        self.login_tela.pack(fill="both", expand=True)

        
    def cadastrar(self, tela_login):
        ctk.CTkLabel(tela_login, text="Bem vindo ao Profitly", font=('', 25)).place(relx=0.5, rely=0.1, anchor='center')
        ctk.CTkLabel(tela_login, text="Digite seu nome de usuario:").place(relx=0.5, rely=0.20, anchor="center") 
        ctk.CTkLabel(tela_login, text="Digite a sua senha: ").place(relx=0.5, rely=0.37, anchor="center")
        ctk.CTkLabel(tela_login, text="Cole a sua Chave API:").place(relx=0.5, rely=0.54, anchor="center")
        ctk.CTkLabel(tela_login, text="Se já possui conta, entre:").place(relx=0.5, rely=0.86, anchor="center")
        ctk.CTkButton(tela_login, text="Novo Cadastro", command=self.processar_cadastro, width=30).place(relx=0.5, rely=0.71, anchor="center") 
        ctk.CTkButton(tela_login, text="Login", command=self.mostrar_tela_login).place(relx=0.5, rely=0.91, anchor="center")



        self.usuario_cadastro_input = ctk.CTkEntry(tela_login, placeholder_text="usuario" )
        self.usuario_cadastro_input.place(relx=0.5, rely=0.27, anchor="center")

        
        self.senha_cadastro_input = ctk.CTkEntry(tela_login, placeholder_text="Senha")
        self.senha_cadastro_input.place(relx=0.5, rely=0.44, anchor="center")

        
        self.chaveApi_cadastro_input = ctk.CTkEntry(tela_login, placeholder_text="Chave Api")
        self.chaveApi_cadastro_input.place(relx=0.5, rely=0.61, anchor="center")






    def logar(self, tela_login):    

        ctk.CTkLabel(tela_login, text="Fazer Login", font=('', 25)).pack(pady=20)
        
        usuario_login = ctk.CTkEntry(tela_login, placeholder_text="usuario" )
        usuario_login.pack(pady=10)

        senha_login = ctk.CTkEntry(tela_login, placeholder_text="Senha")
        senha_login.pack(pady=15)
        
        ctk.CTkButton(tela_login, text="Entrar", command='').pack(pady=20)

        ctk.CTkButton(tela_login, text="Criar nova conta", command=self.mostrar_tela_cadastro, width=30).pack(pady=17.5)


    def processar_cadastro(self):
        usuario = self.usuario_cadastro_input.get()
        senha = self.senha_cadastro_input.get()
        chaveApi = self.chaveApi_cadastro_input.get()

        dados_usuarios.coleta_dados(usuario, senha, chaveApi)





app = cadastro_login()
