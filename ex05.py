'''Ler 10 números e imprimir a soma, o maior e o menor'''
numeros = []

def ler_numeros():
    soma = 0
    maior = None
    menor = None #None: nenhum valor/ valor indefinido
    
    for i in range(10):
        num = float(input(f"Digite o {i+1}º número:"))
        #range: gera uma sequência de números inteiros no intervalo

        soma += num

        if maior is None or num> maior:
            maior = num

        if menor is None or num < menor:
            menor = num
    
    print(f"Soma dos números: {soma}")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")

ler_numeros()
