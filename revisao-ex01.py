'''Crie um programa que peça ao usuário para digitar seu nome e 
sua idade. Imprima uma mensagem endereçada a ele que diga em que ano 
ele completará 100 anos.'''

#pedir nome e idade
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

#fazer cálculo
ano_nascimento = 2025 - idade
idade_cem = ano_nascimento + 100

#mostrar ano ao usuário
print(f"Você terá 100 anos em {idade_cem}")