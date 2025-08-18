'''Crie uma classe Banco com um método para adicionar clientes (objetos da classe Cliente) e outro 
para listar todos os clientes.'''

class Cliente:
    def __init__ (self, nome):
        self.nome = nome
    def __str__ (self):
        return self.nome
    
class Banco:
    def __init__ (self):
        self.clientes = []

    def adicionar_cliente(self,cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente} adicionado com sucesso!")

    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado")
        else:
            print("Lista de clientes:")
            for cliente in self.clientes:
                print(f"- {cliente}")

banco = Banco()

cliente1 = Cliente("Luana")
cliente2 = Cliente("Breno")

banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)

