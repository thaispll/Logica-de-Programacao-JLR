'''Crie uma classe Elevador com atributos para andar atual, total de andares e capacidade. 
Implemente métodos para subir e descer andares.'''

class Elevador:
    def __init__ (self, capacidade, total_andares):
        self.capacidade = capacidade
        self.total_andares = total_andares
        self.andar_atual = 0 
    
    def subir(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual +=1
            print(f"Subindo para o andar {self.andar_atual}")
        else:
            print(f"Você já está no último andar")

    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual -=1
            print(f"Descendo para o andar {self.andar_atual}")
        else:
            print(f"Você já está térreo")
    
    def info(self):
        print(f"Andar atual: {self.andar_atual}")
        print(f"Capacidade: {self.capacidade}")
        print(f"Total de andares: {self.total_andares}")


elevador = Elevador(12,5)
elevador.info()
elevador.subir()
elevador.info()
elevador.descer()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()