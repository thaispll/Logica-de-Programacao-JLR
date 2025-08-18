'''Crie um programa que peça ao usuário para digitar seu nome e 
sua idade. Imprima uma mensagem endereçada a ele que diga em que ano 
ele completará 100 anos.'''
#Usando importação 
from datetime import datetime

#pedir nome e idade
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

#fazer cálculo
ano_atual = datetime.now().year

ano_cem = ano_atual + (100 - idade)

#mostrar ano ao usuário
print(f"Você terá 100 anos em {ano_cem}")