'''Função que calcula a área do retângulo'''
def area(base, altura):
    resultado = base * altura
    print(f"A área do retângulo é: {resultado} ")

base = int(input("Digite a base do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

#chamo a função
area(base, altura)

'''Função que calcula a área do retângulo'''
def area():
    base = int(input("Digite a base do retângulo: "))
    altura = int(input("Digite a altura do retângulo: "))
    resultado = base * altura
    print(f"A área do retângulo é: {resultado} ")

    return resultado

#chamo a função
area_do_retangulo = area()