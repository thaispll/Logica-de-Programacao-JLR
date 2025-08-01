'''Crie um sistema simples para registrar e exibir 
relacionamentos amorosos entre pessoas'''

class Pessoa:
    def __init__(self, nome): #init: inicializar um objeto
        self.nome = nome
        self.parceiros = []
    
    def adicionar_parceiro(self, relacionamento):
        self.parceiros.append(relacionamento)

    def mostrar_parceiros(self):
        if not self.parceiros:
            print(f"{self.nome} não possui parceiros registrados.")
        else:
            print(f"Parceiros amorosos de {self.nome}:")
            for rel in self.parceiros:
                if rel.pessoa1 == self:
                    parceiro = rel.pessoa2
                else:
                    parceiro = rel.pessoa1
                print(f" - {parceiro.nome}, desde {rel.ano_inicio}")

class Relacionamento:
    def __init__(self, pessoa1, pessoa2, ano_inicio): #self: relacionado ao objeto que está sendo criado/manipulado
        self.pessoa1 = pessoa1
        self.pessoa2 = pessoa2
        self.ano_inicio = ano_inicio

    def mostrar_informacao(self):
        print(f"{self.pessoa1.nome} e {self.pessoa2.nome} estão juntos desde {self.ano_inicio}")


#Criando pessoas
ana = Pessoa("Ana")
brino = Pessoa("Brino")
felca = Pessoa("Felca")
menina_veneno = Pessoa("Menina Veneno")
chico_moedas = Pessoa("Chico")
luisa = Pessoa("Luisa")
igona = Pessoa("Igona")
davi_brito = Pessoa("Davi Brito - Calabreso")

#Criando relacionamento
relacionamento1 = Relacionamento(ana,davi_brito, 2015)
relacionamento2 = Relacionamento(igona,chico_moedas, 2024)
relacionamento3 = Relacionamento(brino, felca, 2021)
relacionamento4 = Relacionamento(menina_veneno, luisa, 2023)
relacionamento5= Relacionamento(chico_moedas,davi_brito,2022)

#Associar relacionamento às Pessoas
ana.adicionar_parceiro(relacionamento1)
davi_brito.adicionar_parceiro(relacionamento1)

igona.adicionar_parceiro(relacionamento2)
chico_moedas.adicionar_parceiro(relacionamento2)

brino.adicionar_parceiro(relacionamento3)
felca.adicionar_parceiro(relacionamento3)

menina_veneno.adicionar_parceiro(relacionamento4)
luisa.adicionar_parceiro(relacionamento4)

chico_moedas.adicionar_parceiro(relacionamento5)
davi_brito.adicionar_parceiro(relacionamento5)


#Exibir 
#ana.mostrar_parceiros()  
chico_moedas.mostrar_parceiros()

