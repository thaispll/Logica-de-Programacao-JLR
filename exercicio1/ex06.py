'''Escreva um programa que peça um número ao usuário 
e informe se ele é par ou ímpar.'''

numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")