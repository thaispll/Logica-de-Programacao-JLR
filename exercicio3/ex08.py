'''Implemente uma classe Telefone com atributos para marcar número, mostrar histórico de chamadas e desligar.'''
class Telefone:
    def __init__(self):
        self.historico_chamadas = []
        self.chamada_ativa = False
        self.numero_chamando = None

    def marcar_numero(self, numero):
        if not self.chamada_ativa:
            self.chamada_ativa = True
            self.numero_chamando = numero
            self.historico_chamadas.append(numero)
            print(f"Chamando {numero}...")
        else:
            print("Já há uma chamada em andamento. Desligue antes de fazer outra chamada.")

    def mostrar_historico(self):
        if self.historico_chamadas:
            print("Histórico de chamadas:")
            for i, num in enumerate(self.historico_chamadas, 1):
                print(f"{i}. {num}")
        else:
            print("Nenhuma chamada realizada.")

    def desligar(self):
        if self.chamada_ativa:
            print(f"Chamada para {self.numero_chamando} encerrada.")
            self.chamada_ativa = False
            self.numero_chamando = None
        else:
            print("Não há chamada em andamento para desligar.")

telefone = Telefone()
telefone.marcar_numero("1234-5678")
telefone.desligar()
telefone.mostrar_historico()
