'''Crie um programa em Python que simule um sistema simples de biblioteca utilizando conceitos de Programação Orientada a Objetos (POO). O sistema deve:

Definir uma classe Livro que contenha, pelo menos, os atributos:

    titulo (nome do livro)

    autor (nome do autor)

Criar uma lista com pelo menos 10 objetos Livro, representando os livros disponíveis na biblioteca.

Solicitar ao usuário o nome do solicitante do empréstimo.

Exibir a lista de livros disponíveis, numerada para facilitar a seleção.

Pedir para o usuário escolher um número correspondente ao livro que deseja pegar emprestado.

Imprimir uma mensagem confirmando o empréstimo, informando o nome do solicitante e o livro selecionado (título e autor).'''
class Livro:
    def __init__ (self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

def main():
    #criar lista de livros disponíveis
    livros = [
        Livro("Dom Casmurro", "Machado de Assis"),
        Livro("Senhor dos Anéis", "J. R. R. Tolkien"),
        Livro("Harry Potter", "J. K. Rowling"),
        Livro("Café com Deus Pai", "Junior Rostirola"),
        Livro("A menina que roubava livros", "Markus Zusak"),
        Livro("Assassinato do Expresso Oriente", "Agatha Christie"),
        Livro("Fogo e sangue", "George RR Martin"),
        Livro("O pequeno príncipe", "Antoine de Saint-Exupéry"),
        Livro("Jogos Vorazes", "Suzanne Collins"),
        Livro("Quem é Você, Alaska?", "João Verde")
    ]

    #solicitar nome do usuario
    nome = input("Digite o seu nome: ")

    #exibir lista de livros disponíveis
    print("\n Livros disponíveis para empréstimo: ")
    for i, livro in enumerate(livros, start=1):
        print(f" {i}. {livro.titulo} - {livro.autor}")
    
    #Solicitar a escolha do livro pelo usuário
    while True:
        escolha =  int(input("\n Digite o número do livro que deseja pegar emprestado: "))

        if 1 <= escolha <= len(livros):
            livro_selecionado = livros[escolha -1]
            break
        else: 
            print(f"Por favor, digite um número entre 1 e {len(livros)}.")

    print(f"\n Empréstimo confirmado!")
    print(f"{nome} pegou emprestado o livro '{livro_selecionado.titulo}' de {livro_selecionado.autor}.")

main()
