#solicitar número para o usuário
numero = int(input("Digite um número inteiro: "))

#verificar condição: divísivel por 3 ou 5, mas NÃO por ambos ao mesmo tempo

if (numero % 3 == 0) ^ (numero % 5 ==0):
    print(f"O número {numero} é divisível por 3 ou por 5, mas não por ambos")
else:
    print(f"O número {numero} não atende à condição especificada.")