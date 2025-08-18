'''6.	Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou por 5,
 mas não simultaneamente por ambos.'''

numero = int(input("Digite um número inteiro: "))

if (numero % 3 == 0) ^ ( numero % 5 == 0):
    print(f" O número {numero} é divisível por 3 ou por 5, mas não por ambos")
else:
    print(f" O número {numero} não atende à condição especificada.")
