'''Crie uma classe Funcionario que armazena nome e salário, e um método que retorna um aumento 
salarial de 10%.'''
class Funcionario:
    def __init__ (self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumento_salario(self):
        self.salario = self.salario + self.salario * 10/100
        return self.salario
    
    def mostra_salario(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")
        

funcionario = Funcionario("Gisseli", 3000)
funcionario.mostra_salario()
funcionario.aumento_salario()
funcionario.mostra_salario()
    