from brapi import Brapi
import matplotlib.pyplot as plt
import pandas as pd



class Usuario():
    def __init__(self, chave_api):
        self.api = Brapi(api_key=chave_api)


class Cotacao():
    def __init__(self, sigla_cota):
        self.sigla_cota = sigla_cota



    def buscar_preco_cotacao_atual(self, user):
        cotacao_atual = user.quote.retrieve(self.sigla_cota)
        cotacao_atual = {cotacao_atual.results[0].long_name:cotacao_atual.results[0].logourl,
                        cotacao_atual.results[0].currency:cotacao_atual.results[0].regular_market_price,
                        "Volatilidade_1ano":(cotacao_atual.results[0].fifty_two_week_range),
                        "min_1ano": cotacao_atual.results[0].fifty_two_week_low,
                        "max_1ano": cotacao_atual.results[0].fifty_two_week_high}
        return cotacao_atual
    
    def volatilidade(self):
        dados = self.buscar_preco_cotacao_atual(user0.api)
        variacao = [float(dados["min_1ano"]), float(dados["max_1ano"]), float(dados["BRL"])]
        plt.plot([0, 190, 365], variacao)
        plt.ylabel(f"Valores da {self.sigla_cota} esse ano")
        plt.xlabel(f"Dias do ano")
        plt.show()
        

user0 = Usuario('iZedUXQS99BeuxuSAL7rRi')


cota1 = Cotacao(input(str("Digite a cota:\n")))

print(cota1.buscar_preco_cotacao_atual(user0.api))

cota1.volatilidade()
