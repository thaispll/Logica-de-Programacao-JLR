'''Faça uma classe Produto com atributos nome, preço e quantidade em estoque, e um método para descontar um valor do estoque.'''
class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def descontar_estoque(self, quantidade):
        if quantidade <= self.quantidade_estoque:
            self.quantidade_estoque -= quantidade
            print(f"{quantidade} unidades de {self.nome} foram descontadas do estoque.")
        else:
            print(f"Estoque insuficiente para descontar {quantidade} unidades de {self.nome}.")

produto1 = Produto("Caneta", 2.50, 100)
produto1.descontar_estoque(10)
print(f"Quantidade restante em estoque: {produto1.quantidade_estoque}")
