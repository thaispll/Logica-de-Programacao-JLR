'''7.	Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. 
Escreva uma mensagem de erro se a opção for inválida.
 Escolha a opção:
 1 - Soma de 2 números
 2 - Diferença entre 2 números (maior pelo menor)
 3 - Produto entre 2 números
 4 - Divisão entre 2 números (o denominador não pode ser zero)
 Opção:
'''
print("Escolha a opção: ") 
print("1 - Soma de 2 números ")
print("2 - Diferença entre 2 números (maior pelo menor) ")
print("3 - Produto entre 2 números")
print("4 - Divisão entre 2 números (o denominador não pode ser zero)")

opcao = input("Opção: ")

if opcao in ["1", "2", "3", "4"]:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        resultado = num1 + num2
        print(f"Soma: {resultado}")
    elif opcao == "2":
        resultado = num1 - num2
        print(f"Subtração: {resultado}")
    elif opcao == "3":
        resultado = num1 * num2
        print(f"Produto: {resultado}")
    elif opcao == "4":
        if num2 == 0:
            print("Denominador NÃO pode ser igual a zero.")
        else:
            resultado = num1 / num2
            print(f"Divisão: {resultado}")
else:
    print("Erro! Opção Inválida!")