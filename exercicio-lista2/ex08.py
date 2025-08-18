'''8.	Leia a distância em km e a quantidade de litros de gasolina 
consumidos por um carro em um percurso, calcule o consumo em km/l e 
escreva uma mensagem de acordo com a tabela abaixo:

'''

distancia = float(input("Digite a distância percorrida em km:")) 
litros =  float(input("Digite a quantidade de litros consumidos: "))

if litros == 0:
    print("Erro! Quantidade de litros não pode ser igual a zero")
else:
    consumo = distancia / litros

    print(f"Consumo: {consumo:.2f} km/l")

    if consumo < 8:
        print("Venda o carro!")
    elif 8 <= consumo <=14:
        print("Econômico")
    else:
        print("Super econômico!")