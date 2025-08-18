'''Faça um programa que leia uma lista de 5 números inteiros 
digitados pelo usuário e calcule a soma desses números.'''

numeros = []

for i in range(5):
    num = int(input(f"Digite o número inteiro: "))
    numeros.append(num)

soma = sum(numeros)
print(f"A soma dos números é: {soma} ")
