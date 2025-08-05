class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome #atributo público
        self.__idade = idade #atributo privado

    def mostrar_idade(self):
        print(f"Idade: {self.__idade}")

p = Pessoa("Thais", 27)
print(p.nome) #acesso público
p.mostrar_idade() #acesso privado via método

#print(p.__idade) erro
        