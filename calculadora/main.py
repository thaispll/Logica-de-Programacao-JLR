import calculadora

def menu():
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")

while True:
    menu()
    escolha = input("Escolha a operação desejada: ")

    if escolha == "0":
        print("Encerrando a calculadora")
        break

    if escolha in ["1", "2", "3", "4"]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == "1":
            print("Resultado: ", calculadora.soma(num1, num2))
        
        elif escolha == "2":
            print("Resultado: ", calculadora.subtracao(num1, num2))
        
        elif escolha == "3":
            print("Resultado: ", calculadora.multiplicacao(num1, num2))
        
        elif escolha == "4":
            print("Resultado: ", calculadora.divisao(num1, num2))
    else:
        print("Opção inválida!Tente novamente.")