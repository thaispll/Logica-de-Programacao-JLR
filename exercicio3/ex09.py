'''Crie uma classe Jogador com atributos para nome e pontos e métodos para adicionar pontos 
e zerar a pontuação.'''
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0

    def adicionar_pontos(self, quantidade):
        self.pontos += quantidade
        print(f"{quantidade} pontos adicionados para {self.nome}. Total: {self.pontos}")

    def zerar_pontuacao(self):
        self.pontos = 0
        print(f"A pontuação de {self.nome} foi zerada.")

jogador1 = Jogador("Maria")
jogador1.adicionar_pontos(10)
jogador1.zerar_pontuacao()
