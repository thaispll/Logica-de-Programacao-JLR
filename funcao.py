#Função x Classe
#Função: bloco de código que executa uma tarefa
#Classe:modelo para criar objetos
#Objeto: estrutura que representa uma entidade do mundo real
#conceito abstrato dentro de um programa
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
    #Quando utilizar __init__: quando precisa inicializar
    # o objeto com algum valor ou configuração   
        self.titular = titular # instância atual do objeto
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor #self.saldo =self.saldo + valor
            print(f"Depósito de R${valor:.2f}")
        else:
            print("Valor de depósito inválido!")
    #criar funções sacar e consultar_saldo
    def sacar(self, saque):
        if 0 < saque <= self.saldo:
            self.saldo -= saque
            print(f"Saque de R${saque:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido!")
    
    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

conta = ContaBancaria("José", 1000)
conta.consultar_saldo()
conta.depositar(500)
conta.sacar(200)
conta.consultar_saldo()


    